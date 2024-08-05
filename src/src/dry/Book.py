from .Author import dry_author


def dry_book(book):
    data = {
        "id": book.id,
        "author": dry_author(book.author),
        "name": book.name,
        "pagination": book.pagination
    }
    return data
