"""Contact form UX. This validates locally; connect a backend to deliver messages."""
from pyscript import document

def handle_submit(event):
    event.preventDefault()
    form = document.getElementById("contactForm")
    banner = document.getElementById("alertBanner")
    if not form.reportValidity():
        return
    banner.textContent = (
        "Thanks, " + document.getElementById("contactName").value.strip()
        + "! Your form passed validation. To deliver this message, connect the form to a server or email service."
    )
    banner.className = "alert-banner success"
    banner.hidden = False
    form.reset()
