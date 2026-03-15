# aws-managed-policy Generator

Scrapes the [AWS Managed Policy reference page](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html) and generates a Checkov custom policy that blocks all AWS managed policies from being attached to IAM principals.

## Usage

```bash
uv run main.py aws-managed-policy <output_file>
```

## What it does

1. Fetches the full list of AWS managed policies from the AWS docs
2. Generates a Checkov YAML policy with one condition per policy
3. Each condition uses `jsonpath_not_regex_match` to block the policy ARN

## Output format

```yaml
metadata:
  name: Do not attach restricted AWS managed policies to IAM principals
  id: CHI_POLICY_IAM_001
  category: IAM
  guideline: https://your-docs-link
definition:
  and:
    - cond_type: attribute
      resource_types: &id001
        - AWS::IAM::Role
        - AWS::IAM::User
        - AWS::IAM::Group
      attribute: "ManagedPolicyArns[*]"
      operator: jsonpath_not_regex_match
      value: "^arn:aws:iam::aws:policy/AdministratorAccess$"
    - cond_type: attribute
      resource_types: *id001
      attribute: "ManagedPolicyArns[*]"
      operator: jsonpath_not_regex_match
      value: "^arn:aws:iam::aws:policy/AmazonS3FullAccess$"
    ...
```

## Resource types covered

- `AWS::IAM::Role`
- `AWS::IAM::User`
- `AWS::IAM::Group`
