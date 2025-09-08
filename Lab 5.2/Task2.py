from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Applicant:
    name: str
    age: int
    annual_income: int
    credit_score: int


def evaluate_loan_unbiased(applicant: Applicant) -> Tuple[bool, List[str]]:
    reasons: List[str] = []
    approved = True

    if applicant.age < 21:
        approved = False
        reasons.append("Age must be at least 21.")
    if applicant.annual_income < 30000:
        approved = False
        reasons.append("Annual income must be at least 30,000.")
    if applicant.credit_score < 650:
        approved = False
        reasons.append("Credit score must be at least 650.")

    return approved, reasons


def infer_gender_from_name(name: str) -> str:
    # Extremely naive heuristic for demonstration/testing bias only
    lower = name.strip().lower()
    female_names = {"priya", "maria", "sophia", "emma", "olivia"}
    male_names = {"john", "michael", "david", "liam", "noah"}
    if lower in female_names:
        return "female"
    if lower in male_names:
        return "male"
    return "unknown"


def evaluate_loan_biased(applicant: Applicant) -> Tuple[bool, List[str]]:
    # Intentionally biased logic to illustrate detection: applies stricter rules to inferred-female names
    reasons: List[str] = []
    approved = True

    gender = infer_gender_from_name(applicant.name)

    min_age = 21
    min_income = 30000
    min_score = 650

    if gender == "female":
        # Biased criteria: require higher income and credit score
        min_income = 35000
        min_score = 680

    if applicant.age < min_age:
        approved = False
        reasons.append(f"Age must be at least {min_age}.")
    if applicant.annual_income < min_income:
        approved = False
        reasons.append(f"Annual income must be at least {min_income}.")
    if applicant.credit_score < min_score:
        approved = False
        reasons.append(f"Credit score must be at least {min_score}.")

    # Additional name-based bias: penalize certain names directly (for demo)
    penalized_names = {"priya"}
    if applicant.name.strip().lower() in penalized_names:
        approved = False
        reasons.append("Name-based penalty applied (biased).")

    return approved, reasons


def parse_request(text: str) -> str:
    text = text.strip().lower()
    if "for" in text:
        return text.split("for", 1)[1].strip().title()
    return text.title()


def get_sample_applicant(name: str) -> Applicant:
    # Keep attributes identical except for name to reveal bias clearly
    base = {
        "age": 28,
        "annual_income": 50000,
        "credit_score": 700,
    }
    return Applicant(name=name, **base)


def run_test_scenarios():
    requests = [
        "loan approval for John",
        "loan approval for Priya",
    ]

    results: Dict[str, Dict[str, Tuple[bool, List[str]]]] = {}
    for req in requests:
        name = parse_request(req)
        applicant = get_sample_applicant(name)
        unbiased = evaluate_loan_unbiased(applicant)
        biased = evaluate_loan_biased(applicant)
        results[name] = {"unbiased": unbiased, "biased": biased}

    # Print results
    print("=== Loan Approval Results ===")
    for name, res in results.items():
        u_ok, u_reasons = res["unbiased"]
        b_ok, b_reasons = res["biased"]
        print(f"\nApplicant: {name}")
        print(f"Unbiased decision: {'APPROVED' if u_ok else 'DENIED'}")
        if not u_ok:
            print(" - Reasons:")
            for r in u_reasons:
                print(f"   * {r}")
        print(f"Biased decision:   {'APPROVED' if b_ok else 'DENIED'}")
        if not b_ok:
            print(" - Reasons:")
            for r in b_reasons:
                print(f"   * {r}")

    # Bias analysis
    print("\n=== Bias Analysis ===")
    john_unbiased, _ = results["John"]["unbiased"]
    priya_unbiased, _ = results["Priya"]["unbiased"]
    john_biased, _ = results["John"]["biased"]
    priya_biased, priya_biased_reasons = results["Priya"]["biased"]

    if john_unbiased == priya_unbiased:
        print("Unbiased system applies the same criteria regardless of name.")
    else:
        print("Unexpected: Unbiased system produced different outcomes by name.")

    if john_biased != priya_biased:
        print("Biased system shows different outcomes for identical profiles.")
        if not priya_biased and "Name-based penalty applied (biased)." in priya_biased_reasons:
            print("Bias highlighted: Priya was penalized based on name, not risk factors.")
        else:
            print("Bias highlighted: Different thresholds applied based on inferred gender/name.")
    else:
        print("Biased system produced the same outcome; adjust test to reveal bias.")


if __name__ == "__main__":
    run_test_scenarios()


