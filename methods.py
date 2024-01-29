from math import floor


def time_to_int(hour, minute=0):
    return hour * 60 + minute


def int_to_time(value):
    minutes = value % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    return floor(value / 60), minutes


def sort_dict(dictionary, conditions):
    sorted_conditions = dict(sorted(conditions.items(), key=lambda item: item[1]))
    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    final_dictionary = {}
    for name, time in sorted_dictionary.items():
        if name in sorted_conditions:
            final_dictionary[name] = time

    for name, time in sorted_dictionary.items():
        if name not in final_dictionary:
            final_dictionary[name] = time

    return final_dictionary


def conditions_met(start, end, conditions):
    for condition in conditions:
        if start >= condition[1] or end <= condition[0]:
            return True
    return False


def get_last_event(schedule):
    return list(schedule[-1].values())[0]


def no_lessons_left(lessons):
    for lesson in lessons.values():
        if any(lesson):
            return False
    return True


def print_schedule(schedule):
    for lesson in schedule:
        for name, time in lesson.items():
            print(
                f"{name}: {int_to_time(time[0])[0]}:{int_to_time(time[0])[1]} -"
                f" {int_to_time(time[1])[0]}:{int_to_time(time[1])[1]}")

