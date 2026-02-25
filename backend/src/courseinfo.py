from typing import NamedTuple, List
from icalendar import Calendar, Event, vRecur
from datetime import datetime
import zoneinfo
# course info for a schedule
class Course_Info(NamedTuple):
    name: str
    section: str
    instructor: str
    meeting_times: str

# So fun fact, America in this case actually stands for North America and not the U S of A 
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Search on the page for Vancouver and it says it's BC (NOT THE USA VANCOUVER). 
# https://github.com/eggert/tz/blob/main/backward 
# ^^ According to this top link here, the Canadian Alias for "America/Vancouver" is "Canada/Pacific"
# Literally no canadian city gets a custom "Canada/City_name" and instead gets a "Canada/RegionOrProvince"
# Not even toronto but I hate toronto tho so toronto deserves that
vancouver_tz = zoneinfo.ZoneInfo("America/Vancouver")

class ScheduleMaker:
    
    def __init__(self):
        self.__cal__: Calendar = Calendar()
    def format_weekdays(self, week_day: List[str]):
        formatted = []
        for day in week_day:
            formatted.append(day[0:2].upper())
        return formatted

    def parse_meeting_pattern(self, pattern_string):
        parts = [p.strip() for p in pattern_string.split('|')]
        
        date_part = parts[0].split(' - ')

        # make it the last minute of the day
        end_date = datetime.strptime(date_part[1], "%Y-%m-%d").replace(hour=23, minute=59, second=59)

        weekdays = parts[1].split()
        

        start_date_str = date_part[0]
        time_str = parts[2].replace('.', '')
        time_parts = time_str.split(' - ')
        
        first_start = datetime.strptime(f"{start_date_str} {time_parts[0]}", "%Y-%m-%d %I:%M %p").replace(tzinfo=vancouver_tz)
        first_end = datetime.strptime(f"{start_date_str} {time_parts[1]}", "%Y-%m-%d %I:%M %p").replace(tzinfo=vancouver_tz)
        
        building = parts[4]
        room = parts[6].replace('Room: ', '')
        location = f"{building}, Room {room}"
        
        return end_date, first_start, first_end, location, weekdays
    
    # week_days is a list of strings in format MO TU WE TH FR SA SU
    def add_recurring_event(self, summary, desc, location, week_days: List[str], start_time: datetime, end_time: datetime, end_date: datetime):
        event = Event()
        event.add('summary', summary)
        event.add('description', desc)
        event.add('location', location)
        event.add('dtstart', start_time)
        event.add('dtend', end_time)

        event.add('rrule', {
            'freq': 'weekly',
            'byday': week_days,
            'until': end_date
        })
        self.__cal__.add_component(event)
    def add_course(self, course: Course_Info):
        # workday formatting is kinda stoopida 
        meeting_days = course.meeting_times.split("\n\n")
        for meets in meeting_days:
            
            end_date, first_start, first_end, location, weekdays = self.parse_meeting_pattern(meets)
            
            desc = ''.join([str(course.section), "\nInstructor: ", str(course.instructor)])
            weekdays = self.format_weekdays(weekdays)
            self.add_recurring_event(
                summary=course.name, 
                desc=desc, 
                location=location,
                week_days=weekdays, 
                start_time=first_start, 
                end_time=first_end, 
                end_date=end_date)
    
    def add_all_courses(self, courses: List[Course_Info]):
        for c in courses:
            try:
                self.add_course(c)
            except Exception as e:
                # just skip the course if it fails 
                error_type = type(e).__name__
                print(f"Error (type: {error_type}) occured: {e}")
                continue

        
    def write_ics(self, ics_name):
        with open(ics_name, 'wb') as f:
            f.write(self.__cal__.to_ical())
    
    def get_ics_content(self):
        return self.__cal__.to_ical()
