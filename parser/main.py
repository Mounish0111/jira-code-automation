from parser_logic import parse_ticket

with open("sample_ticket.txt") as f:
    text = f.read()

print(parse_ticket(text))