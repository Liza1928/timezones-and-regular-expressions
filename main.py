import asyncio
from datetime import datetime

from pytz import timezone, utc

from parsers.birthday_parser import parse_record
from readers.file_reader import read_file
from service.crud import create_birthday, read_birthday
from dto.schemas import BirthdayCreate
from db.database import database
from reporter.birthday_reporter import birthday_report


FILENAME = 'data/example.txt'


async def main():
    await database.connect()
    file_data = read_file(FILENAME)
    for record in file_data:
        data = await parse_record(record)
        local = timezone(data['residence_timezone'])
        local_dt = local.localize(data['birthday'], is_dst=None)
        utc_dt = local_dt.astimezone(utc)
        data['birthday'] = utc_dt
        if data is not None:
            data = BirthdayCreate(**data)
            id = await create_birthday(data)
            print(id)
            recorded_data = await read_birthday(id)
            recorded_data = BirthdayCreate(**recorded_data)
            report_data = {
                'ФИО': recorded_data.fio,
                'Дата и время рождения по московскому времени':
                    recorded_data.birthday.astimezone(timezone('Europe/Moscow')),
                'Текущее время в таймзоне проживания':
                    datetime.now(timezone(recorded_data.residence_timezone))
            }
            await birthday_report(report_data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())