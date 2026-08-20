from mcp.server.fastmcp import FastMCP
from freshdesk_service import (
    get_ticket_count,
    get_agents,
    get_groups,
    get_tickets,
    get_ticket_detail,
    get_ticket_conversations,
    search_tickets
)

mcp = FastMCP("Freshdesk")


@mcp.tool()
def open_ticket_count():
    return f"Total tickets: {get_ticket_count()}"
    


@mcp.tool()
def list_agents():
    agents = get_agents()

    return [
        {
            "id": a["id"],
            "name": a["contact"]["name"]
        }
        for a in agents
    ]


@mcp.tool()
def list_groups():
    groups = get_groups()

    return [
        {
            "id": g["id"],
            "name": g["name"]
        }
        for g in groups
    ]


@mcp.tool()
def get_ticket(ticket_id: int):
    return get_ticket_detail(ticket_id)


@mcp.tool()
def get_conversations(ticket_id: int):
    return get_ticket_conversations(ticket_id)


@mcp.tool()
def find_tickets(query: str):
    return search_tickets(query)


@mcp.tool()
def latest_tickets():
    return get_tickets()


if __name__ == "__main__":
    mcp.run()