from .jira_client import fetch_jira_ticket
from .parser_logic import parse_ticket

print("🚀 USING JIRA API FLOW")

if __name__ == "__main__":
    issue_key = input("Enter Jira Issue Key: ")

    ticket = fetch_jira_ticket(issue_key)

    print("\n--- RAW TICKET ---")
    print(ticket)

    parsed = parse_ticket(ticket["description"])

    print("\n--- PARSED OUTPUT ---")
    print(parsed)