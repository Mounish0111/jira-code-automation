from jira_client import fetch_jira_ticket
from parser_logic import parse_ticket


if __name__ == "__main__":
    issue_key = input("Enter Jira Issue Key: ")

    try:
        ticket = fetch_jira_ticket(issue_key)

        print("\n--- RAW TICKET ---")
        print("Title:", ticket["title"])
        print("Description:\n", ticket["description"])

        parsed = parse_ticket(ticket)

        print("\n--- PARSED OUTPUT ---")
        print(parsed)

        print("\n--- AI PROMPT ---\n")
        print(f"""
You are a software developer.

Task:
Build a feature: {parsed['feature']}

Requirements:
{chr(10).join(parsed['requirements'])}

Acceptance Criteria:
{chr(10).join(['- ' + v for v in parsed['validations']])}
""")

    except Exception as e:
        print("Error:", e)