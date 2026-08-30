def print_sunset(data):

    from datetime import datetime, timezone, timedelta

    sunrise_timestamp = data["sys"]["sunrise"]
    sunset_timestamp = data["sys"]["sunset"]
    timezone_offset = data["timezone"]

    local_tz = timezone(timedelta(seconds=timezone_offset))

    sunrise = datetime.fromtimestamp(sunrise_timestamp, tz=local_tz)
    sunset = datetime.fromtimestamp(sunset_timestamp, tz=local_tz)

    print("Sunrise:", sunrise.strftime("%H:%M"))
    print("Sunset:", sunset.strftime("%H:%M"))