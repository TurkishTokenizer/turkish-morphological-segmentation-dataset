"""Count word types (POS categories) in final_core_roots.json."""
import json
from pathlib import Path

data_path = Path(__file__).parent / "data" / "final_core_roots.json"

with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)

total = 0
print(f"{'Category':<12} {'Count':>8}")
print("-" * 22)
for category, words in sorted(data.items(), key=lambda x: len(x[1]), reverse=True):
    count = len(words)
    total += count
    print(f"{category:<12} {count:>8,}")

print("-" * 22)
print(f"{'TOTAL':<12} {total:>8,}")
