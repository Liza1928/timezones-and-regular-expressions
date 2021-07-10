from datetime import datetime
import re
from dynaconf import settings

birthday_regex = re.compile(r'.*?|')
data_regex = re.compile(r'(\d{4})-(\d{2})-(\d{2}) (\d{2})-(\d{2})-(\d{2})')


async def parse_record(stroke: str):
    parsed_data = {}
    data = stroke.split('|')
    data_format = settings.DATA_FORMAT
    if len(data) != len(data_format):
        print('Неправильный формат')
        return
    for key, value in zip(data_format, data):
        if key == settings.DATA_CHECK:
            parsed_value = re.match(data_regex, value)
            if parsed_value is not None:
                value = parsed_value.group(0)
                value = datetime.strptime(value, '%Y-%m-%d %H-%M-%S')
            else:
                print('Неправильный формат даты')
                return
        parsed_data.update({key: value})
    return parsed_data

