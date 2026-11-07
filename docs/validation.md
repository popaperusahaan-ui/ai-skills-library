# Skill Validation

This document explains how Skills are validated in AI Skills Library.

## Purpose

The validation system helps maintain consistent structure, metadata, and documentation quality across the repository.

## Automated Validation

AI Skills Library uses GitHub Actions to validate Skill files automatically.

Validation runs when:

- Changes are pushed to the main branch.
- Pull requests modify Skill files.
- The workflow is started manually.

## Validation Requirements

Every Skill must contain:

- Valid YAML frontmatter.
- A name field.
- A description field.
- A Purpose section.
- An Instructions section.
- A Workflow section.
- A Rules section.
- An Output section.

## Running Validation Locally

Run the following command from the repository root:

```bash
python scripts/validate_skills.py
