from dataclasses import dataclass


def find_years(seconds):
    years = seconds // 31536000
    seconds = seconds - (31536000 * years)

    return years, seconds


def find_days(seconds):
    days = seconds // 86400
    seconds = seconds - (86400 * days)

    return days, seconds


def find_minutes(seconds):
    minutes = seconds // 60
    seconds = seconds - (60 * minutes)

    return minutes, seconds


def find_hours(seconds):
    hours = seconds // 3600
    seconds = seconds - (3600 * hours)

    return hours, seconds


def generate_output(datetime):
    output = ''

    num_of_items = len(datetime.items())
    for time, value in datetime.items():
        output += f'{value} {time}'
        if value > 1:
            output += 's'
        if num_of_items == 2:
            output += ' and '
        if num_of_items > 2:
            output += ', '

        num_of_items -= 1

    return output




def format_duration(second: int) -> str:
    if second == 0:
        return 'now'

    years, second = find_years(second)
    days, second = find_days(second)
    hours, second = find_hours(second)
    minutes, second = find_minutes(second)

    output_dict = {}
    if years:
        output_dict.update({'year':years})
    if days:
        output_dict.update({'day': days})
    if hours:
        output_dict.update({'hour': hours})
    if minutes:
        output_dict.update({'minute': minutes})
    if second:
        output_dict.update({'second': second})


    return generate_output(output_dict)


print(format_duration(
    (31536000 * 7) + (
                86400 * 246) + 54000 + 54 + 1920) == '7 years, 246 days, 15 hours, 32 minutes and 54 seconds')

print(format_duration(1) == '1 second')
print(format_duration(120) == '2 minutes')
print(format_duration(3600) == '1 hour')
print(format_duration(3662) == '1 hour, 1 minute and 2 seconds')

times = [("year", 365 * 24 * 60 * 60),
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

print(format_duration(
    (31536000 * 7) + (
                86400 * 246) + 54000 + 54 + 1920) == '7 years, 246 days, 15 hours, 32 minutes and 54 seconds')

