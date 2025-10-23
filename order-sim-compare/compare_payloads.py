#!/usr/bin/env python3
import json
import sys
from deepdiff import DeepDiff

def textCompare(file1, file2):
    """Compare two JSON payloads and print differences."""
    with open(file1) as f1, open(file2) as f2:
        j1, j2 = json.load(f1), json.load(f2)

    diff = DeepDiff(j1, j2, ignore_order=True, significant_digits=6)
    if diff:
        print(f"❌ Payloads differ between {file1} and {file2}:")
        print(str(diff))

        return False
    else:
        print(f"✅ {file1} and {file2} match.")
        return True

if __name__ == "__main__":
    # Run all main comparisons
    all_pass = True
    tests = [
        ("OS_Request_UK.json", "OS_Request_PL.json"),
        ("OS_Response_UK.json", "OS_Response_PL.json"),
        ("OS_Request_PL.json", "OS_Response_PL.json")
    ]
    for a, b in tests:
        print(f"\n🔍 Comparing {a} ↔ {b}")
        if not textCompare(a, b):
            all_pass = False
    if not all_pass:
        sys.exit(1)  # Fail the CI if any mismatch
