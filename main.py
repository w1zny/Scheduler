from data import *
from methods import *
from random import randrange

sorted_students = sort_dict(students_start, additional_conditions)
finished = False
schedule = []

while not finished:

    for name, start_time in sorted_students.items():
        if not any(lessons[name]):
            continue

        lesson_index = randrange(len(lessons[name]))
        lesson_len = lessons[name][lesson_index]

        start_event = None
        if not any(schedule):
            if start_time <= START:
                start_event = START
        else:
            last_event_end = get_last_event(schedule)[1]
            if start_time <= last_event_end:
                start_event = last_event_end

        if not start_event:
            continue

        end_event = start_event + lesson_len
        if end_event > END:
            finished = True
            break

        if name not in additional_conditions:
            schedule.append({name: (start_event, end_event)})
            lessons[name].pop(lesson_index)
            continue

        if conditions_met(start_event, end_event, additional_conditions[name]):
            schedule.append({name: (start_event, end_event)})
            lessons[name].pop(lesson_index)

    START += 10

print(day)
print_schedule(schedule)

