### Create a random schedule with given conditions

Create your data.py file in the same folder as other .py files for your circumstances.  
In this file, you should import methods.

```
from methods import time_to_int
```

then create a few variables

```
START = time_to_int(hour, minute)
END = time_to_int(hour, minute)
day = "day for schedule creation"

students_start = {
    "name of a student": time_to_int(hour_when_he_can_start, minute_when_he_can_start),
    .
    .
    .
}

# start of condition - the start of the event when a student can't attend
# end of condition - the end of the event when a student can't attend (when he can attend again)
additional_conditions = {
    "name of a student": [(time_to_int(start_of_condition), time_to_int(end_of_condition)), ...],
    .
    .
    .
}

lessons = {
    "name of a student": [length_of_lesson_1, length_of_lesson_2, ...],
    .
    .
    .
}
```

Then navigate to the folder via the terminal where you can run this command:

```
python3 main.py
```
