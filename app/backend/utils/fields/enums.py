# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_enumfield.enum import Enum


class BlogCategory(Enum):
    update = 0


class NewsCategory(Enum):
    update = 0


class InvoiceStatus(Enum):
    draft = 0
    open = 1
    paid = 2
    uncollectible = 3
    void = 4


class SessionMode(Enum):
    payment = 0
    setup = 1
    subscription = 2


class SessionStatus(Enum):
    expired = 0
    open = 1
    complete = 2
