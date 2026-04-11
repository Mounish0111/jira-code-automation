import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")


def extract_text_from_adf(adf):
    text = ""

    if not adf or "content" not in adf:
        return ""

    for block in adf["content"]:
        if block["type"] == "paragraph":
            for item in block.get("content", []):
                if item["type"] == "text":
                    text += item["text"]
            text += "\n"

        elif block["type"] == "bulletList":
            for item in block.get("content", []):
                for sub in item.get("content", []):
                    for txt in sub.get("content", []):
                        if txt["type"] == "text":
                            text += "- " + txt["text"] + "\n"

    return text


def fetch_jira_ticket(issue_key):
    url = f"{JIRA_DOMAIN}/rest/api/3/issue/{issue_key}"

    print("\nDEBUG INFO:")
    print("URL:", url)
    print("EMAIL:", JIRA_EMAIL)

    response = requests.get(
        url,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN),
        headers={"Accept": "application/json"}
    )

    print("\nSTATUS CODE:", response.status_code)
    print("RESPONSE TEXT:", response.text[:500])  # limit output

    if response.status_code != 200:
        raise Exception("Failed to fetch Jira issue")

    issue = response.json()

    title = issue["fields"]["summary"]

    raw_description = issue["fields"]["description"]
    description = extract_text_from_adf(raw_description)

    return {
        "title": title,
        "description": description
    }