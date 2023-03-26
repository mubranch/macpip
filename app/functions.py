from os import popen
from pathlib import Path
import requests
from .classes import App
from googlesearch import search


def find_apps(app: Path, nested_apps: list, cc: str) -> None:

    """
    Recursively finds all apps in a directory and its subdirectories and modifies the passed list to include
    all items confirmed as apps within the directory.
    """

    if is_app(app):
        confirmed_app = App(
            app.name[:-4],
            find_bundle_identifier(app),
            find_url_by_bundleid(find_bundle_identifier(app), cc),
            app,
        )

        if confirmed_app.url is None:
            confirmed_app.url = find_url_by_google(
                confirmed_app.name, confirmed_app.bundle_id
            )

        nested_apps.append(confirmed_app)
        return

    if is_directory(app):
        for item in app.iterdir():
            find_apps(item, nested_apps, cc)

    return


def is_app(app: Path) -> bool:
    """
    Return True if item in directory ends with .app
    """
    return str(app)[-3:] == "app"


def is_hidden(app: Path) -> bool:
    """
    Check if item is hidden, currently only works for hidden apps that start with '.' files.
    """
    if app.name.startswith("."):
        return True
    return False


def is_directory(app: Path) -> bool:
    """
    Checks if item is a directory
    """
    if app.is_dir():
        return True
    return False


def find_bundle_identifier(app: Path) -> str:
    """
    Finds the unique bundle identifier of an app using the mdls command.
    """
    return popen(f"mdls -name kMDItemCFBundleIdentifier -raw '{str(app)}'").read()


def find_url_by_bundleid(bundle_id: str, cc) -> any:
    """
    Find application's app store URL if app is distributed via mac app store.
    """
    url = f"http://itunes.apple.com/{cc}/lookup?bundleId={bundle_id}"
    r = requests.get(url)
    try:
        content = r.json()["results"][0]["trackViewUrl"]
    except IndexError:
        content = None
    return content


def find_url_by_google(name: str, bundle_id: str) -> str:
    """
    Find link to download app by name.
    """
    query = f"{name} {bundle_id} download"
    for result in search(query, num_results=1):
        return result
