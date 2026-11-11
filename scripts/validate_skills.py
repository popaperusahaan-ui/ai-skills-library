
from pathlib import Path
import re
import sys

SKILLS_DIR = Path("skills")

REQUIRED_SECTIONS = [
    "## Purpose",
    "## Instructions",
    "## Workflow",
    "## Rules",
    "## Output",
]

REQUIRED_METADATA = ["name", "description"]


def validate_skill(file_path):
    errors = []

    try:
        content = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        return [f"{file_path}: Cannot read file: {error}"]

    if not content.startswith("---\n"):
        return [f"{file_path}: Missing YAML frontmatter."]

    parts = content.split("---", 2)

    if len(parts) < 3:
        return [f"{file_path}: Invalid YAML frontmatter."]

    metadata = parts[1]
    body = parts[2]

    metadata_values = {}

    for key in REQUIRED_METADATA:
        matches = re.findall(
            rf"^{key}:\s*(.*?)\s*$",
            metadata,
            re.MULTILINE
        )

        if not matches:
            errors.append(f"{file_path}: Missing {key}.")
        elif len(matches) > 1:
            errors.append(f"{file_path}: Duplicate {key} field.")
        elif not matches[0].strip():
            errors.append(f"{file_path}: Empty {key}.")
        else:
            metadata_values[key] = matches[0].strip()

    skill_name = metadata_values.get("name")

    if skill_name:
        expected_name = file_path.parent.name

        if skill_name != expected_name:
            errors.append(
                f"{file_path}: Skill name '{skill_name}' "
                f"does not match folder '{expected_name}'."
            )

    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(
                f"{file_path}: Missing section {section}."
            )

    if not body.strip():
        errors.append(f"{file_path}: Skill content is empty.")

    return errors


def validate_skill_directories():
    errors = []

    for directory in sorted(SKILLS_DIR.iterdir()):
        if not directory.is_dir():
            continue

        skill_file = directory / "SKILL.md"

        if not skill_file.exists():
            errors.append(
                f"{directory}: Missing SKILL.md file."
            )

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

    # Validate every Skill file.
    for skill_file in skill_files:
        errors.extend(validate_skill(skill_file))

    # Validate Skill directory structure.
    errors.extend(validate_skill_directories())

    # Detect duplicate Skill names.
    skill_names = {}

    for skill_file in skill_files:
        try:
            content = skill_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        parts = content.split("---", 2)

        if len(parts) < 3:
            continue

        matches = re.findall(
            r"^name:\s*(.*?)\s*$",
            parts[1],
            re.MULTILINE
        )

        if not matches or not matches[0].strip():
            continue

        name = matches[0].strip()

        if name in skill_names:
            errors.append(
                f"Duplicate Skill name '{name}': "
                f"{skill_names[name]} and {skill_file}."
            )
        else:
            skill_names[name] = skill_file

    if errors:
        print("Skill validation failed:")

        for error in errors:
            print(f"- {error}")

        print(f"\nFound {len(errors)} error(s).")
        sys.exit(1)

    print(
        f"Success: {len(skill_files)} skills validated."
    )


if __name__ == "__main__":
    main()
    
