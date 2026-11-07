---
name: api-testing
description: API testing skill for validating API functionality, reliability, security, performance, and response correctness.
---

# API Testing Skill

## Purpose

Help AI assistants design, execute, and evaluate API tests to improve API quality and reliability.

## Instructions

When testing APIs:

1. Understand API requirements.
2. Identify available endpoints.
3. Review HTTP methods and parameters.
4. Define expected responses.
5. Prepare test cases.
6. Test valid and invalid inputs.
7. Verify authentication and authorization.
8. Evaluate error handling.
9. Check performance where appropriate.
10. Document test results.

## Workflow

### 1. API Discovery

Identify:
- Base URL.
- Endpoints.
- HTTP methods.
- Request parameters.
- Authentication requirements.
- Response formats.

### 2. Test Planning

Prepare tests for:
- Successful requests.
- Invalid inputs.
- Missing parameters.
- Authentication failures.
- Authorization failures.
- Unexpected responses.
- Error conditions.

### 3. Functional Testing

Verify:
- HTTP status codes.
- Response structure.
- Response data.
- Business logic.
- Data validation.
- CRUD operations.

### 4. Security Testing

Check authorized test environments for:
- Authentication weaknesses.
- Authorization failures.
- Sensitive information exposure.
- Input validation problems.
- Rate-limit behavior.

### 5. Performance Testing

Evaluate:
- Response time.
- Request throughput.
- Resource consumption.
- Behavior under expected workloads.

Avoid disruptive load testing.

### 6. Regression Testing

Re-run relevant tests after code or API changes.

Check that existing functionality remains correct.

### 7. Reporting

Document:
- Test cases.
- Expected results.
- Actual results.
- Failed tests.
- Identified defects.
- Recommendations.

## Rules

- Use authorized test environments.
- Never expose API credentials.
- Do not modify production data without permission.
- Use safe and controlled test inputs.
- Do not invent test results.
- Distinguish automated tests from manual reviews.
- Never claim tests passed unless executed.

## Output

Provide:

1. API test plan.
2. Test cases.
3. Test implementation.
4. Expected and actual results.
5. Identified issues.
6. Regression checklist.
7. Final test report.
