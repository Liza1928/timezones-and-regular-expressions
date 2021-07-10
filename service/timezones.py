from pytz import timezone
from datetime import datetime


async def timezone_offset(data: datetime, old_timezone:str, new_timezone: timezone):
    old_tz = timezone(old_timezone)
    new_tz = timezone(new_timezone)
    print(data)
    # old = old_tz.localize(data)
    # new = old.astimezone(new_tz)
    new_dt = data.replace(tzinfo=new_tz)
    print(new_dt)
    return new_dt