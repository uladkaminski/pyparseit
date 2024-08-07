# scripts/bump_version.py

import re
import sys

version_file = 'setup.py'

if len(sys.argv) != 2:
    print("Usage: bump_version.py <new_version>")
    sys.exit(1)

new_version = sys.argv[1]

if not re.match(r'^\d+\.\d+\.\d+$', new_version):
    print("Invalid version format. Use x.y.z")
    sys.exit(1)

with open(version_file, 'r') as file:
    content = file.read()

current_version = re.search(r"version=['\"](\d+\.\d+\.\d+)['\"]", content).group(1)

updated_content = content.replace(f"version='{current_version}'", f"version='{new_version}'")

with open(version_file, 'w') as file:
    file.write(updated_content)

print(f"Updated version: {current_version} -> {new_version}")
