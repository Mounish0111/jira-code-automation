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

        if line.lower().startswith("title:"):
            data["feature"] = line.replace("Title:", "").strip()

        elif line.lower().startswith("description:"):
            capture_description = True
            capture_validation = False
            continue

        elif line.lower().startswith("acceptance criteria:"):
            capture_validation = True
            capture_description = False
            continue

        elif capture_description:
            if line != "":
                data["requirements"].append(line)

        elif capture_validation:
            if line.startswith(("-", "*")):
                data["validations"].append(line[1:].strip())

    if not data["feature"]:
        data["feature"] = "Unknown Feature"

    return data