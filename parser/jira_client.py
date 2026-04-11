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

    if isinstance(adf, dict):
        for item in adf.get("content", []):
            text += extract_text_from_adf(item)

    elif isinstance(adf, list):
        for item in adf:
            text += extract_text_from_adf(item)

    elif isinstance(adf, str):
        text += adf + " "

    return text


def fetch_jira_ticket(issue_key):
    print("🔥 CALLING JIRA API")

    url = f"{JIRA_DOMAIN}/rest/api/3/issue/{issue_key}"
    print("URL:", url)

    response = requests.get(
        url,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN),
        headers={"Accept": "application/json"}
    )

    print("STATUS:", response.status_code)

    data = response.json()
    fields = data.get("fields", {})

    description_adf = fields.get("description", {})
    description_text = extract_text_from_adf(description_adf)

    return {
    "title": fields.get("summary"),
    "description": description_text
}


