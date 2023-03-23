
class BaseError(Exception):
    def __init__(self, detail: str) -> None:
        self.detail = detail

    def dict(self):
        return {"detail": self.detail}
