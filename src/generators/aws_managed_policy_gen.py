from src.scanner.aws.policy_scanner import AWSManagedPolicyScanner

POLICY_URL = "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html"

IAM_RESOURCE_TYPES = ["AWS::IAM::Role", "AWS::IAM::User", "AWS::IAM::Group"]


class AWSManagedPolicyGenerator:

    def __init__(self):
        self._scanner = AWSManagedPolicyScanner()

    def generate(self, output_path: str) -> None:
        policies = self._scanner.scan(POLICY_URL)

        with open(output_path, "w") as f:
            f.write(self._render_yaml(policies))

        print(f"Generated Checkov policy with {len(policies)} rules -> {output_path}")

    def _render_yaml(self, policies: list[str]) -> str:
        resource_types_block = "\n".join(
            f"        - {rt}" for rt in IAM_RESOURCE_TYPES
        )

        conditions = []
        for i, policy in enumerate(policies):
            anchor = "&id001" if i == 0 else "*id001"
            conditions.append(
                f"    - cond_type: attribute\n"
                f"      resource_types: {anchor}\n"
                + (f"{resource_types_block}\n" if i == 0 else "")
                + f'      attribute: "ManagedPolicyArns[*]"\n'
                f"      operator: jsonpath_not_regex_match\n"
                f'      value: "^arn:aws:iam::aws:policy/{policy}$"'
            )

        conditions_str = "\n".join(conditions)

        return (
            "metadata:\n"
            "  name: Do not attach restricted AWS managed policies to IAM principals\n"
            "  id: CHI_POLICY_IAM_001\n"
            "  category: IAM\n"
            "  guideline: https://your-docs-link\n"
            "definition:\n"
            "  and:\n"
            f"{conditions_str}\n"
        )
