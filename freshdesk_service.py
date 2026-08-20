import requests

FRESHDESK_DOMAIN = "https://suvitt-support.freshdesk.com"
FRESHDESK_API_KEY = "9SlPpAKy7-4B_xwGjnLT"


def _request(url):
    response = requests.get(
        url,   
        auth=(FRESHDESK_API_KEY, "X")
    )

    if response.status_code != 200:
        raise Exception(
            f"Freshdesk Error {response.status_code}: {response.text}"
        )

    return response.json()


# -----------------------------
# TOTAL TICKET COUNT
# -----------------------------
def get_ticket_count():
    total_count = 0
    page = 1

    while True:
        url = f"{FRESHDESK_DOMAIN}/api/v2/tickets?page={page}&per_page=100"

        tickets = _request(url)

        if not tickets:
            break

        total_count += len(tickets)
        page += 1

    return total_count


# -----------------------------
# GET TICKETS
# -----------------------------
def get_tickets(page=1, per_page=100):
    url = (
        f"{FRESHDESK_DOMAIN}/api/v2/tickets"
        f"?page={page}&per_page={per_page}"
    )

    return _request(url)


# -----------------------------
# GET TICKET DETAIL
# -----------------------------
def get_ticket_detail(ticket_id):
    url = f"{FRESHDESK_DOMAIN}/api/v2/tickets/{ticket_id}"

    return _request(url)


# -----------------------------
# GET CONVERSATIONS
# -----------------------------
def get_ticket_conversations(ticket_id):
    url = (
        f"{FRESHDESK_DOMAIN}"
        f"/api/v2/tickets/{ticket_id}/conversations"
    )

    return _request(url)


# -----------------------------
# SEARCH TICKETS
# -----------------------------
def search_tickets(query):
    url = (
        f"{FRESHDESK_DOMAIN}"
        f"/api/v2/search/tickets?query=\"{query}\""
    )

    return _request(url)


# -----------------------------
# GET AGENTS
# -----------------------------
def get_agents():
    url = f"{FRESHDESK_DOMAIN}/api/v2/agents"

    return _request(url)


# -----------------------------
# GET GROUPS
# -----------------------------
def get_groups():
    url = f"{FRESHDESK_DOMAIN}/api/v2/groups"

    return _request(url)