import webbrowser


def browse(url: str) -> None:
    webbrowser.open(url, new=1)
