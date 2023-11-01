from typing import TypedDict

class BookDict(TypedDict):
    isbn: str
    title: str
    authors: list[str]
    pagecount: int

pp = BookDict(title='Programming Pearls',
              authors='Jon Bentley',
              isbn='0201657880',
              pagecount=256)
print(pp)
print(type(pp))