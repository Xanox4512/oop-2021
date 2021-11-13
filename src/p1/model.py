
## MODEL
from dataclasses import dataclass


@dataclass
class Request:
    userid: int


@dataclass
class Client:
    id: int
    name: str


@dataclass
class Employee:
    id: int
    name: str