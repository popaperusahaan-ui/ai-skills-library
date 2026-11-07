---
name: secure-coding
description: Secure coding skill for writing, reviewing, and improving software code using secure development principles and vulnerability prevention practices.
---

# Secure Coding Skill

## Purpose

Help AI assistants produce secure, reliable, and maintainable source code.

## Instructions

When writing or reviewing code:

1. Understand the application requirements.
2. Identify security-sensitive components.
3. Validate all untrusted input.
4. Apply secure authentication and authorization.
5. Protect sensitive information.
6. Handle errors safely.
7. Review dependencies.
8. Follow language-specific security practices.
9. Test security controls.
10. Document important security decisions.

## Workflow

### 1. Security Analysis

Identify:
- Sensitive data.
- Trust boundaries.
- User-controlled inputs.
- Privileged operations.
- External dependencies.

### 2. Input and Output Security

Apply:
- Input validation.
- Output encoding.
- Safe serialization.
- Parameterized database queries.
- File upload validation.

### 3. Authentication and Authorization

Ensure:
- Authentication is properly verified.
- Permissions are checked server-side.
- Access follows least-privilege principles.
- Sessions are handled securely.

### 4. Data Protection

Use:
- Secure password hashing.
- Appropriate encryption.
- Secret management.
- Data minimization.
- Secure communication.

### 5. Error Handling

Ensure:
- Errors do not expose secrets.
- Logs avoid sensitive information.
- Failures are handled consistently.
- Debug settings are not exposed in production.

### 6. Dependency Security

Review:
- Dependency versions.
- Known vulnerabilities.
- Package sources.
- Unnecessary dependencies.
- Update requirements.

### 7. Verification

Use code review, static analysis, and authorized tests to evaluate security improvements.

## Rules

- Never hardcode passwords or API keys.
- Never store plaintext passwords.
- Never trust unvalidated input.
- Avoid unsafe database queries.
- Do not expose internal secrets in error messages.
- Preserve existing functionality.
- Use established security libraries.
- Never claim code is secure without sufficient verification.

## Output

Provide:

1. Security review.
2. Identified risks.
3. Secure implementation.
4. Explanation of improvements.
5. Testing recommendations.
6. Remaining limitations.
