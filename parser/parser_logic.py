def parse_ticket(text):
    lines = text.split("\n")

    data = {
        "feature": "",
        "type": "feature",
        "requirements": [],
        "validations": []
    }

    capture_description = False
    capture_validation = False

    for line in lines:
        line = line.strip()

        if line.startswith("Title:"):
            data["feature"] = line.replace("Title:", "").strip()

        elif line.startswith("Description:"):
            capture_description = True
            capture_validation = False
            continue

        elif line.startswith("Acceptance Criteria:"):
            capture_validation = True
            capture_description = False
            continue

        elif capture_description and line != "":
            data["requirements"].append(line)

        elif capture_validation and line.startswith("-"):
            data["validations"].append(line.replace("-", "").strip())

    return data