from medical_rules import diagnose


def test_diagnosis_is_ranked_and_explained():
    result = diagnose(["FEVER", "cough", "fatigue"], minimum_coverage=0.5)
    assert result[0].condition == "influenza-like illness"
    assert result[0].coverage == 0.75

