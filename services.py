"""PyScript-powered live service search."""
from pyscript import document

def filter_services(event=None):
    query = document.getElementById("serviceSearch").value.lower().strip()
    cards = document.querySelectorAll("#servicesGrid .service-card")
    visible = 0
    for card in cards:
        haystack = (card.getAttribute("data-search") or "") + " " + (card.textContent or "")
        matches = query in haystack.lower()
        card.hidden = not matches
        if matches:
            visible += 1
    document.getElementById("serviceCount").textContent = f"{visible} service{'s' if visible != 1 else ''}"
    document.getElementById("noServices").hidden = visible != 0
