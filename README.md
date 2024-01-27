### Create a random schedule with given conditions with ease

Create your own data.py file in the same folder with other .py files for your personal circumstances.
In this file you should import methods.

```
from methods import timeToInt
```

then create a few variables

```
START = timeToInt(hour, minute)
END = timeToInt(hour, minute)
work_days = ["day_when_you_work_1", "day_when_you_work_2", ...]

students_conditions = {
    "name of a student": timeToInt(hour_when_he_can_start, minute_when_he_can_start),
    .
    .
    .
}

students_available_lessons = {
    "name of a student": [length_of_1st_lesson, length_of_2nd_lesson, ...],
    .
    .
    .
}

full_schedule = {
    "working day": [],
    "monday": [],
    .
    .
    .
}
```

Then navigate to the folder via terminal where you can run this command:

```
python3 main.py
```
