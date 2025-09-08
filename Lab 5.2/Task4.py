import sys


def prompt_float(prompt: str, min_value: float | None = None, max_value: float | None = None) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if min_value is not None and value < min_value:
                print(f"Value must be >= {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be <= {max_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def prompt_choice(prompt: str, choices: dict[str, float]) -> float:
    options = ", ".join([f"{k}={v}" for k, v in choices.items()])
    while True:
        key = input(f"{prompt} ({options}): ").strip().lower()
        if key in choices:
            return choices[key]
        print("Invalid choice. Try again.")


def normalize_weights(weights: dict[str, float]) -> dict[str, float]:
    total = sum(weights.values())
    if total == 0:
        return {k: 0.0 for k in weights}
    return {k: (v / total) for k, v in weights.items()}


def compute_score(features: dict[str, float], weights: dict[str, float]) -> tuple[float, dict[str, float]]:
    normalized_weights = normalize_weights(weights)
    contributions: dict[str, float] = {}
    score = 0.0
    for name, value in features.items():
        w = normalized_weights.get(name, 0.0)
        contrib = value * w
        contributions[name] = contrib
        score += contrib
    return score, contributions


def audit_bias(weights: dict[str, float], feature_metadata: dict[str, dict]) -> list[str]:
    findings: list[str] = []

    normalized_weights = normalize_weights(weights)

    # Identify protected attributes and their normalized weights
    protected_attributes = [name for name, meta in feature_metadata.items() if meta.get("protected", False)]
    for attr in protected_attributes:
        w = normalized_weights.get(attr, 0.0)
        if abs(w) > 0.0:
            findings.append(
                f"Protected attribute '{attr}' has non-zero weight ({w:.2f}). Consider removing or setting to 0."
            )

    # Flag unusually large weights relative to others
    non_protected = [k for k in weights if k not in protected_attributes]
    if non_protected:
        avg = sum(abs(normalized_weights[k]) for k in non_protected) / len(non_protected)
        for k in non_protected:
            w = abs(normalized_weights[k])
            if avg > 0 and w > 2.5 * avg:
                findings.append(
                    f"Feature '{k}' weight ({normalized_weights[k]:.2f}) is disproportionately high vs avg {avg:.2f}."
                )

    # Check for negative weights that could indirectly penalize protected groups
    for k, w in normalized_weights.items():
        if w < 0:
            findings.append(
                f"Feature '{k}' has negative weight ({w:.2f}). Verify this does not create indirect discrimination."
            )

    if not findings:
        findings.append("No overt bias signals found in weight configuration. Continue to monitor outcomes.")

    return findings


def main() -> None:
    print("Job Applicant Scoring System with Bias Analysis")
    print("-" * 48)

    # Define feature encodings and metadata
    education_levels = {
        "highschool": 0.4,
        "diploma": 0.6,
        "bachelor": 0.8,
        "master": 0.9,
        "phd": 1.0,
    }

    gender_map = {
        # Note: This is encoded but will be discouraged in weighting
        "female": 0.5,
        "male": 0.5,
        "nonbinary": 0.5,
        "prefer_not": 0.5,
    }

    # Feature metadata to guide bias audit
    feature_metadata = {
        "education": {"protected": False, "desc": "Education level (0-1)"},
        "experience": {"protected": False, "desc": "Years of relevant experience normalized [0-1]"},
        "skills": {"protected": False, "desc": "Skills match score [0-1]"},
        "gender": {"protected": True, "desc": "Self-identified gender (encoded constant)"},
        "age": {"protected": True, "desc": "Age bucket normalized [0-1]"},
    }

    print("Enter applicant details:")

    edu_val = prompt_choice("Education level", education_levels)

    years_exp = prompt_float("Years of relevant experience (0-40): ", 0, 40)
    exp_norm = min(years_exp / 20.0, 1.0)

    skills = prompt_float("Skills match (0-100): ", 0, 100) / 100.0

    gender_val = prompt_choice("Gender (for auditing only)", gender_map)

    age_years = prompt_float("Age in years (18-70): ", 18, 70)
    # Normalize age to mid-career sweet spot around 30-45 without biasing extremes
    # We use a gentle bell-like shape centered at 37.5 mapped to [0.5, 1.0]
    mid = 37.5
    spread = 12.5
    age_norm = max(0.0, 1.0 - (abs(age_years - mid) / (2 * spread)))
    age_norm = 0.5 + 0.5 * age_norm

    features = {
        "education": edu_val,
        "experience": exp_norm,
        "skills": skills,
        "gender": gender_val,
        "age": age_norm,
    }

    print("\nEnter feature weights (they will be normalized to sum to 1):")
    default_weights = {
        "education": 0.35,
        "experience": 0.40,
        "skills": 0.25,
        "gender": 0.0,
        "age": 0.0,
    }

    def prompt_weight(name: str, default: float) -> float:
        while True:
            raw = input(f"Weight for {name} [default {default}]: ").strip()
            if raw == "":
                return default
            try:
                return float(raw)
            except ValueError:
                print("Enter a numeric value or press Enter for default.")

    weights = {k: prompt_weight(k, v) for k, v in default_weights.items()}

    # Compute score
    score, contributions = compute_score(features, weights)

    print("\nScore breakdown (weights normalized):")
    normalized_weights = normalize_weights(weights)
    for k in features:
        print(f"- {k}: value={features[k]:.2f}, weight={normalized_weights.get(k, 0.0):.2f}, contrib={contributions.get(k, 0.0):.2f}")

    print(f"\nFinal applicant score: {score:.2f} (0-1 scale)")

    # Bias audit
    print("\nBias audit:")
    findings = audit_bias(weights, feature_metadata)
    for item in findings:
        print(f"- {item}")

    # Guidance
    print("\nGuidance:")
    print("- Use job-related features (education, experience, skills).")
    print("- Avoid assigning non-zero weights to protected attributes (gender, age).")
    print("- Validate outcomes with real data to detect disparate impact.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(1)
