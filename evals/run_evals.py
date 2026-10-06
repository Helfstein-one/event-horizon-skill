#!/usr/bin/env python3
import json, sys, os

def run_evals():
    tasks_path = os.path.join(os.path.dirname(__file__), "tasks.json")
    if not os.path.exists(tasks_path):
        print(f"Error: {tasks_path} not found.")
        sys.exit(1)

    with open(tasks_path, "r") as f:
        tasks = json.load(f)

    print(f"=== Event Horizon Evaluation Suite ===")
    print(f"Loaded {len(tasks)} benchmark evaluation tasks.\n")

    for t in tasks:
        print(f"[{t['id']}] ({t['category']})")
        print(f"  Prompt: {t['prompt']}")
        print(f"  Target: {t['success_criteria']}")
        print("  Status: READY FOR TRAJECTORY AUDIT\n")

if __name__ == "__main__":
    run_evals()
