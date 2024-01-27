from random import randrange
from methods import is_finished, is_listed, print_schedule
from data import work_days, students_conditions, students_available_lessons, full_schedule, START, END

finished = is_finished(students_available_lessons)

while not finished:
    for name, available_lessons in students_available_lessons.items():
        if any(available_lessons):
            lesson_index = randrange(0, len(available_lessons))
            lesson_len = available_lessons[lesson_index]
            day_index = randrange(0, len(work_days))
            day = work_days[day_index]
            if not any(full_schedule[day]):
                if students_conditions[name] <= START:
                    full_schedule[day].append(
                        {name: (students_conditions[name], students_conditions[name] + lesson_len)})
                    students_available_lessons[name].pop(lesson_index)
            else:
                if not is_listed(name, day, full_schedule):
                    previous_end_time = list(
                        full_schedule[day][-1].values())[-1][-1]
                    if previous_end_time + lesson_len > END:
                        work_days.pop(day_index)
                    else:
                        if students_conditions[name] <= previous_end_time:
                            full_schedule[day].append(
                                {name: (previous_end_time, previous_end_time+lesson_len)})
                            students_available_lessons[name].pop(lesson_index)
        finished = is_finished(students_available_lessons)

print_schedule(full_schedule)
