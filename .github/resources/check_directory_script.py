import csv
import os
import sys

print("Directory Checker")

csv_file = "TranslatedMods.csv"
f = open(csv_file, newline="", encoding="utf-8")

reader = csv.reader(f)
header = next(reader)
lines = list(enumerate(reader, start=2))

print(f"Found entries: {len(lines)}")
print("\nChecking directories:")

failureMods = []
for line_num, line in lines:
    if len(line) < 3:
        continue

    mod_name = line[2].strip()

    if os.path.isdir(mod_name):
        print(f"\t\033[32mOK\033[0m: {mod_name}")
    else:
        print(
            f"::error file=TranslatedMods.csv,line={line_num}::Directory '{mod_name}' does not exist"
        )
        print(f"\t\033[31mFAIL\033[0m: {mod_name}")
        failureMods.append(mod_name)

f.close()

print("\nSummary:")
print("\t\033[32mSuccess\033[0m:", len(lines) - len(failureMods))
print("\t\033[31mFailure\033[0m:", len(failureMods))

if len(failureMods) > 0:
    print("\n\033[31mFailed directories:\033[0m")
    for mod in failureMods:
        print(f"\t- {mod}")

if len(failureMods) > 0:
    sys.exit(1)
