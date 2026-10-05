---
name: spec-driven-enforcer
description: Enforces Spec-Driven Development (SDD) for complex tasks.
---

# Spec-Driven Development Enforcer

**Directives:**
1. When asked to build a new feature or perform a massive architectural change, DO NOT start writing code immediately.
2. First, generate a markdown specification file in `.agents/specs/` outlining the plan, architecture, and expected test cases.
3. Use the `ask_question` tool to have the user approve the spec.
4. Only upon user approval, proceed to implement the code strictly according to the spec.
