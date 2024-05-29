from dataclasses import dataclass

from model.country import Country


@dataclass
class Confine:
    stato1: Country
    stato2: Country
