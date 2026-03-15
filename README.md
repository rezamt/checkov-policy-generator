# checkov-policy-generator

Generates Checkov custom policies from various AWS sources.

## Requirements

- [uv](https://docs.astral.sh/uv/)

## Install

```bash
uv sync
```

## Usage

```bash
uv run main.py <generator> <output_file>
```

### Generators

| Generator | Description |
|---|---|
| `aws-managed-policy` | Scrapes all AWS managed policies and generates a Checkov policy that blocks them from being attached to IAM principals |

### Example

```bash
uv run main.py aws-managed-policy blocked_managed_policies.yaml
```

## Output

A Checkov-compatible YAML policy file using `jsonpath_not_regex_match` to block all AWS managed policies from being attached to `AWS::IAM::Role`, `AWS::IAM::User`, and `AWS::IAM::Group`.

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
    ...
```
