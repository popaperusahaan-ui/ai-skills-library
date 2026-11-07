# Skill Format Specification

This document defines the standard format for all skills in AI Skills Library.

## 1. File Structure

Every skill must follow this structure:

    skills/
    └── skill-name/
        └── SKILL.md

## 2. Required Metadata

Every SKILL.md must begin with YAML frontmatter.

    ---
    name: skill-name
    description: Describe the skill and when to use it.
    ---

### Metadata Rules

- `name` must be unique.
- Use lowercase letters and hyphens.
- `description` must clearly explain the skill.
- Use valid YAML syntax.

## 3. Required Sections

Every skill must contain:

- Purpose
- Instructions
- Workflow
- Rules
- Output

## 4. Content Requirements

### Purpose
Explain the skill's primary objective.

### Instructions
Provide clear and actionable directions.

### Workflow
Describe the steps required to complete a task.

### Rules
Define limitations and quality standards.

### Output
Specify the expected response or deliverable.

## 5. Quality Standards

Every skill should be:

- Clear
- Accurate
- Reusable
- Modular
- Maintainable
- Well-documented

## 6. Compatibility

Skills should use portable instructions whenever possible.

Tool-specific features must be documented.

## 7. Validation

Before publishing a skill, verify:

- Valid YAML metadata.
- Required sections are present.
- Instructions are understandable.
- No secrets or credentials are included.
- Examples and outputs are relevant.

---

AI Skills Library
