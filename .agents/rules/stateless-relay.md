# Stateless Relay (Context Pruning)

**Trigger:** `always_on`

**Directives:**
- Monitor the length of the conversation.
- If a task involves more than 5 multi-step iterations, DO NOT keep accumulating chat history.
- Write a highly dense `state_summary.txt` to the scratch folder.
- Clear/ignore previous conversation context and rely ONLY on the `state_summary.txt` to continue the workflow.
