---
name: authentication-authorization
description: Authentication and authorization skill for implementing secure identity verification, access control, permissions, and user session management.
---

# Authentication & Authorization Skill

## Purpose

Help AI assistants design, implement, and maintain secure authentication and authorization systems.

## Instructions

When developing identity and access systems:

1. Understand identity requirements.
2. Identify user roles.
3. Select appropriate authentication methods.
4. Design authorization policies.
5. Implement secure session management.
6. Protect account credentials.
7. Apply access controls.
8. Handle authentication errors.
9. Test permission boundaries.
10. Document security behavior.

## Workflow

### 1. Requirements Analysis

Identify:
- User types.
- Registration requirements.
- Login methods.
- Account recovery.
- Role definitions.
- Permission requirements.

### 2. Authentication Design

Evaluate:
- Password-based authentication.
- Multi-factor authentication.
- OAuth and OpenID Connect.
- Secure token management.
- Account recovery methods.

### 3. Authorization Design

Define:
- Roles.
- Permissions.
- Resource ownership.
- Access policies.
- Administrative privileges.

### 4. Session Management

Consider:
- Secure session handling.
- Session expiration.
- Token expiration.
- Logout behavior.
- Session revocation.

### 5. Security

Apply:
- Secure password hashing.
- Rate limiting.
- Account protection.
- Server-side permission checks.
- Secure credential storage.
- Appropriate audit logging.

### 6. Testing

Verify:
- Valid and invalid login attempts.
- Registration behavior.
- Permission boundaries.
- Role restrictions.
- Session expiration.
- Account recovery.

## Rules

- Never store plaintext passwords.
- Never expose authentication tokens.
- Enforce authorization on the server.
- Apply least-privilege access.
- Do not trust client-side permission checks alone.
- Protect account recovery processes.
- Never claim security tests passed unless executed.

## Output

Provide:

1. Authentication architecture.
2. Authorization model.
3. Role and permission definitions.
4. Implementation examples.
5. Security recommendations.
6. Testing checklist.
