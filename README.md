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

| Generator | Description | Docs |
|---|---|---|
| `aws-managed-policy` | Scrapes all AWS managed policies and generates a Checkov policy that blocks them from being attached to IAM principals | [doc/generators/aws-managed-policy.md](doc/generators/aws-managed-policy.md) |

### Example

```bash
uv run main.py aws-managed-policy blocked_managed_policies.yaml
```
