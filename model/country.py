from dataclasses import dataclass


@dataclass
class Country:
    CCode: int
    StateAbb: str
    StateNme: str

    def __str__(self):
        return f"{self.StateNme}"

    def __hash__(self):
        return self.CCode
