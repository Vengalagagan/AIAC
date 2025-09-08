def greet_user(name, gender):
    """Return a greeting using an honorific that supports gender-neutral forms.

    - Male inputs: "male", "m", "man", "boy", "masculine", "he", "him" -> "Mr."
    - Female inputs: "female", "f", "woman", "girl", "feminine", "she", "her" -> "Ms."
    - Gender-neutral inputs (and unknown): "non-binary", "nonbinary", "nb", "enby",
      "neutral", "mx", "agender", "genderqueer", "other", "unspecified",
      "prefer not to say" -> "Mx."
    - Any unrecognized or empty value safely defaults to "Mx.".
    """

    normalized = (gender or "").strip().lower()

    male_inputs = {
        "male", "m", "man", "boy", "masculine", "he", "him",
    }
    female_inputs = {
        "female", "f", "woman", "girl", "feminine", "she", "her",
    }
    neutral_inputs = {
        "non-binary", "nonbinary", "nb", "enby", "neutral", "mx",
        "agender", "genderqueer", "other", "unspecified", "prefer not to say",
        "prefer_not_to_say", "unknown", "n/a", "na", "",
    }

    if normalized in male_inputs:
        title = "Mr."
    elif normalized in female_inputs:
        title = "Ms."
    else:
        title = "Mx."

    return f"Hello, {title} {name}! Welcome."
