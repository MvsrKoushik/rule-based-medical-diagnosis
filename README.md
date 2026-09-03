# Rule-Based Medical Diagnosis

An explainable forward-chaining engine reconstructed from the Colab assignment. Rules map symptom sets to educational hypotheses and return the exact evidence that fired each rule.

```bash
pip install -e .[dev]
pytest
python -m medical_rules.cli fever cough fatigue
```

This is an educational software project, not a medical device. Its output must not be used for diagnosis or treatment decisions.

