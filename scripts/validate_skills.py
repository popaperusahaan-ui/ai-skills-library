from pathlib import Path
import sys

SKILLS_DIR = Path("skills")

REQUIRED_SECTIONS = [
    "## Purpose",
    "## Instructions",
    "## Workflow",
    "## Rules",
    "## Output",
]


def validate_skill(file_path):
    errors = []
    content = file_path.read_text(encoding="utf-8")

    if not content.startswith("---\n"):
        return [f"{file_path}: Missing YAML frontmatter."]

    parts = content.split("---", 2)

    if len(parts) < 3:
        return [f"{file_path}: Invalid YAML frontmatter."]

    metadata = parts[1]
    body = parts[2]

    if "name:" not in metadata:
        errors.append(f"{file_path}: Missing name.")

    if "description:" not in metadata:
        errors.append(f"{file_path}: Missing description.")

    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"{file_path}: Missing section {section}.")

    return errors


def main():
    if not SKILLS_DIR.exists():
        print("Error: skills directory not found.")
        sys.exit(1)

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))

    if not skill_files:
        print("Error: No SKILL.md files found.")
        sys.exit(1)

    errors = []

    for skill_file in skill_files:
        errors.extend(validate_skill(skill_file))

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print(f"Success: {len(skill_files)} skills validated.")


if __name__ == "__main__":
    main()
