---
name: schema-dumper
description: Dumps compressed database schemas without row data context bloat.
---

# Schema Dumper

**Directives:**
1. When asked to analyze a database or write SQL, DO NOT query raw rows (`SELECT *`) unless explicitly requested.
2. Run schema dump commands instead (e.g., `sqlite3 db.sqlite ".schema"`, or standard `pg_dump --schema-only`).
3. You can also write a quick minimal script to extract only table names and column types. 
4. The goal is to provide structural context to the LLM with zero data bloat.
