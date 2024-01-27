Create your own data.py file for your own circumstances
. In this file you should import methods.

```
from methods import timeToInt
```

then create a few variables

```
START = timeToInt(hour, minute)
END = timeToInt(hour, minute)

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
