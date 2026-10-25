"""PyScript interactions for the Home module."""
from pyscript import document

def toggle_menu(event):
    links = document.getElementById("navLinks")
    button = document.getElementById("menuToggle")
    links.classList.toggle("active")
    is_open = links.classList.contains("active")
    button.setAttribute("aria-expanded", "true" if is_open else "false")
