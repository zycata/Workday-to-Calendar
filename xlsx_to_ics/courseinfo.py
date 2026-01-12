from typing import NamedTuple


# course info for a schedule
class Course_Info(NamedTuple):
    name: str
    section: str
    instructor: str
    start_date: str
    end_date: str

obama = Course_Info(*["soy", "admen", "sussy", "reak", "end"])

print(obama)