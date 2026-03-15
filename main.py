import sys
import argparse
sys.path.insert(0, ".")

from src.generators.aws_managed_policy_gen import AWSManagedPolicyGenerator

GENERATORS = {
    "aws-managed-policy": AWSManagedPolicyGenerator,
}


def main():
    parser = argparse.ArgumentParser(
        prog="checkov-policy-generator",
        description="Generate Checkov custom policies from various sources.",
    )
    parser.add_argument(
        "generator",
        choices=GENERATORS.keys(),
        help="Policy generator to use (e.g. aws-managed-policy)",
    )
    parser.add_argument(
        "output",
        help="Output YAML file path (e.g. blocked_managed_policies.yaml)",
    )

    args = parser.parse_args()
    GENERATORS[args.generator]().generate(args.output)


if __name__ == "__main__":
    main()
