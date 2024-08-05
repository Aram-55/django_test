def dry_author(author):
    data = {
        "id": author.id,
        "user": {
            "username": author.user.username,
            "full_name": " ".join([author.user.first_name, author.user.last_name])
        },
        "age": author.age,
        "gender": author.gender
    }
    return data
