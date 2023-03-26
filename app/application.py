from pathlib import Path
from .functions import find_apps


def main(cc: str):
    dir = Path("/Applications")
    apps = []
    for app in dir.iterdir():
        find_apps(app, apps, cc)

    print(apps)
