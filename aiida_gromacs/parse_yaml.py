import yaml
from pathlib import Path

file_path = Path(__file__).parent / "software.yml"

with open(file_path, "r") as f:
    data = yaml.safe_load(f)

print("Tool:", data.get("name"))
print("Version:", data.get("version"))
print("Description:", data.get("description"))
print("Authors:", ", ".join(data.get("authors", [])))
print("License:", data.get("license"))
print("Repository:", data["links"].get("repository"))
print("Documentation:", data["links"].get("documentation"))
print("Citation:", data["links"].get("citation"))
import yaml
from pathlib import Path
from datetime import date

# 1. Read metadata
file_path = Path(__file__).parent / "software.yml"

with open(file_path, "r") as f:
    data = yaml.safe_load(f)

# 2. Automatically update fields
data["status"]["last_updated"] = str(date.today())
data["status"]["work_in_progress"] = False

# 3. Write updated metadata to a new file
output_path = Path(__file__).parent / "updated_metadata.yml"

with open(output_path, "w") as f:
    yaml.dump(data, f, sort_keys=False)

# 4. Display summary
print("Updated metadata written to updated_metadata.yml")
print("Tool:", data.get("name"))
print("Version:", data.get("version"))
print("Last Updated:", data["status"]["last_updated"])
