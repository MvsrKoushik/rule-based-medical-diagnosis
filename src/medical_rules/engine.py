from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    condition: str
    symptoms: frozenset[str]


@dataclass(frozen=True)
class Diagnosis:
    condition: str
    matched: tuple[str, ...]
    coverage: float


DEFAULT_RULES = (
    Rule("influenza-like illness", frozenset({"fever", "cough", "fatigue", "body aches"})),
    Rule("migraine-like presentation", frozenset({"headache", "nausea", "light sensitivity"})),
    Rule("allergic rhinitis-like presentation", frozenset({"sneezing", "runny nose", "itchy eyes"})),
    Rule("gastroenteritis-like presentation", frozenset({"nausea", "vomiting", "diarrhea", "abdominal pain"})),
    Rule("asthma-like presentation", frozenset({"wheezing", "shortness of breath", "chest tightness"})),
)


def normalize(value: str) -> str:
    return " ".join(value.lower().replace("_", " ").split())


def diagnose(symptoms: list[str], rules: tuple[Rule, ...] = DEFAULT_RULES, minimum_coverage: float = 0.5) -> list[Diagnosis]:
    observed = {normalize(item) for item in symptoms}
    results = []
    for rule in rules:
        matched = tuple(sorted(rule.symptoms & observed))
        coverage = len(matched) / len(rule.symptoms)
        if coverage >= minimum_coverage:
            results.append(Diagnosis(rule.condition, matched, coverage))
    return sorted(results, key=lambda item: (-item.coverage, item.condition))

