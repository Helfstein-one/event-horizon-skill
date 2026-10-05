---
name: tdd-enforcer
description: Strictly enforces Test-Driven Development before logic implementation.
---

# TDD Enforcer

**Directives:**
1. NEVER write or refactor implementation code first.
2. ALWAYS write a failing test case for the requested feature or bug fix.
3. Use `run_command` to execute the test suite and verify that it fails exactly as expected.
4. Only then, implement the minimum code required to make the test pass.
5. This guarantees token-efficient implementation and eliminates guesswork.
