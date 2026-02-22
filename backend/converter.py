


'''
General Guide to what happens here

receive excel file

return err if bad

convert excel to courseinfo data type

use that to create .ics file

return any errs if errors occur


'''
from backend.src import courseinfo

from backend.src import excel
def parse_excel(file):
    try:
        Workday_s = excel.Workday_Schedule.read_workday_excel(file)
        return Workday_s.get_courses()
    except Exception as e:
        raise TypeError(f"Error parsing given file: {e}")

def get_ics(courses):
    try:
        scheduler = courseinfo.ScheduleMaker()
        scheduler.add_all_courses(courses)
        # should return some ics in io format
        return scheduler.get_ics_content()
    except Exception as e:
        raise ValueError("Error converting the contents of the excel to ics")

# Abstractionaholic? Abstractaholic? Abstraholic? Abst-holic? Aholic?
def convert_xlsx_to_ics(file):
    courses = parse_excel(file)
    return get_ics(courses)

# woahhhh extra functionality as a command line utility??? WHAttt???
if __name__ == "__main__":
    import sys 
    argc = len(sys.argv)
    if argc < 3:
        sys.exit(f"Not enough arguments, commandline usage: python {sys.argv[0]} [input excel] [output ics]")
    courses = parse_excel(sys.argv[1])
    scheduler = courseinfo.ScheduleMaker()
    scheduler.add_all_courses(courses)
    scheduler.write_ics(sys.argv[2])