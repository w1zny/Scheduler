from math import floor


def timeToInt(hours, minutes):
    return hours*60 + minutes


def intToTime(value):
    minutes = value % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    return (floor(value/60), minutes)


def is_finished(students):
    count = 0
    for name, arr in students.items():
        if not any(arr):
            count += 1
    if count == len(students):
        return True
    return False


def print_schedule(full_schedule):
    for day, daily_schedule in full_schedule.items():
        print(day)
        for item in daily_schedule:
            for name, time in item.items():
                time_pair_1 = intToTime(time[0])
                time_pair_2 = intToTime(time[1])
                print(
                    f"{name}: {time_pair_1[0]}:{time_pair_1[1]} - {time_pair_2[0]}:{time_pair_2[1]}")
        print("\n")


def is_listed(name, day, full_schedule):
    arr = full_schedule[day]
    for item in arr:
        if list(item.keys())[0] == name:
            return True
    return False
