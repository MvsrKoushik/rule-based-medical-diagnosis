import argparse
from .engine import diagnose


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("symptoms", nargs="+")
    parser.add_argument("--minimum-coverage", type=float, default=0.5)
    args = parser.parse_args()
    for item in diagnose(args.symptoms, minimum_coverage=args.minimum_coverage):
        print(f"{item.condition}: {item.coverage:.0%} ({', '.join(item.matched)})")


if __name__ == "__main__":
    main()

