class App:
    def __init__(self, name: str, bundle_id: str, url: str, path: str):
        self.name = name
        self.bundle_id = bundle_id
        self.url = url
        self.path = path

    def __repr__(self) -> str:
        return f"{self.name} - {self.url} \n"
