import importlib.metadata
import re

with open('requirements.txt', 'r') as f:
    lines = f.readlines()

packages = []

for line in lines:
    line= line.strip()

    # Skipping the libs that are not in use
    if not line or line.startswith('#'):
        continue

    if '==' in line:
        line = line.split('==')
        line = line[0]

    packages.append(line)


with open("requirements.txt","w") as f:
        
    for pkg in packages:
        try:
            version = importlib.metadata.version(pkg)
            line = f"{pkg}=={version}\n"

            print(line.strip())
            f.write(line)
        except importlib.metadata.PackageNotFoundError:
            print(f"{pkg} (not installed)")

