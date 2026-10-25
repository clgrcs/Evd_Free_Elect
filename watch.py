"""Video module: gracefully shows a helpful placeholder if the local video is missing."""
from pyscript import document

def _show_placeholder(event=None):
    document.getElementById("videoPlaceholder").style.display = "flex"
    document.getElementById("promoVideo").style.display = "none"

def _hide_placeholder(event=None):
    document.getElementById("videoPlaceholder").style.display = "none"
    document.getElementById("promoVideo").style.display = "block"

video = document.getElementById("promoVideo")
video.addEventListener("error", _show_placeholder)
video.addEventListener("loadeddata", _hide_placeholder)
# Some browsers don't fire the source error until loading is requested.
video.load()
