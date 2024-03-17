from dataclasses import dataclass


@dataclass
class Person:
    email_me: str = None
    first_name: str = None
