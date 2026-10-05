---
name: dependency-compiler
description: Maps code dependencies without full file context bloat.
---

# Dependency Compiler (AST-Deps)

**Directives:**
1. When navigating a new codebase or fixing a type issue, DO NOT read the full contents of imported files.
2. Run standard grep/AST scripts (like your `ast-search` CLI wrapper) to find exported types, interfaces, or signatures.
3. Keep the context window minimal by only loading function signatures and structural maps.
