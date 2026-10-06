#!/usr/bin/env python3
import sys, json, re

def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        print(json.dumps({"decision": "allow"}))
        return

    tool_call = payload.get("toolCall", {})
    name = tool_call.get("name", "")
    args = tool_call.get("args", {})

    # 1. Gate view_file on large / log files
    if name == "view_file":
        path = args.get("AbsolutePath", "")
        start_line = args.get("StartLine")
        end_line = args.get("EndLine")

        if path.endswith(".log"):
            # Block un-sliced reading of .log files
            if not start_line and not end_line:
                res = {
                    "decision": "deny",
                    "reason": "Event Horizon Hook: Direct view_file on *.log without slicing is denied to protect context tokens. Use tail, grep, or specify StartLine/EndLine."
                }
                print(json.dumps(res))
                return

    # 2. Gate run_command dangerous commands and auto-wrap verbose commands
    if name == "run_command":
        cmd = args.get("CommandLine", "").strip()

        # Danger checks
        if re.search(r"\brm\s+-(?:rf|fr)\s+(?:/|~|\$HOME|\.\.)", cmd) or re.search(r"\bgit\s+push\s+.*--force\b", cmd):
            res = {
                "decision": "deny",
                "reason": "Event Horizon Hook: Destructive command blocked by safety gate."
            }
            print(json.dumps(res))
            return

        # Auto-wrap verbose test/build commands with rtk if not already wrapped
        verbose_triggers = [r"^npm\s+(?:install|test|ci|run\s+test)", r"^cargo\s+test", r"^pytest\b", r"^go\s+test"]
        is_verbose = any(re.search(pat, cmd) for pat in verbose_triggers)

        if is_verbose and not cmd.startswith("rtk "):
            res = {
                "decision": "allow",
                "overwrite": {
                    "CommandLine": f"rtk {cmd}"
                }
            }
            print(json.dumps(res))
            return

    print(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
