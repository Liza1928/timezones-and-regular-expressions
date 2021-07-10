from typing import Dict, List

from db.database import database

insert_birthday = (
    'INSERT INTO birthday (fio, birthday, birthday_timezone, residence_timezone)'
    'VALUES (:fio, :birthday, :birthday_timezone, :residence_timezone)'
    'RETURNING  id'
)

query_birthday = (
    "SELECT fio, birthday, birthday_timezone, residence_timezone "
    "FROM birthday "
    "WHERE id=:id"
)


async def read_birthday(id: int) -> Dict[str, str]:
    results = await database.fetch_all(query_birthday, {"id": id})
    return dict(results[0])


async def create_birthday(birthday) -> None:
    id = await database.execute(
        insert_birthday,
        {
            "fio": birthday.fio,
            "birthday": birthday.birthday,
            "birthday_timezone": birthday.birthday_timezone,
            "residence_timezone": birthday.residence_timezone,
        },
    )
    return id





