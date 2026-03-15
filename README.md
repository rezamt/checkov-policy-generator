# Checkov Policy Generator

https://www.checkov.io/

Generates Checkov custom policies from various AWS sources.

## Architecture

- **Scanner** — responsible for fetching and parsing data from a source (e.g. scraping a web page, calling an API). Returns a list of raw values.
- **Generator** — takes the scanner output and transforms it into a Checkov-compatible YAML policy file.

Each generator has its own scanner under `src/scanner/` and its own generator under `src/generators/`.

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
