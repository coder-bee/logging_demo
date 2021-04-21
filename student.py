import logging
from pythonjsonlogger import jsonlogger

#terminal_format = "%(asctime)s:%(name)s:%(levelname)s:%(message)s"
log_format = "%(asctime)s:%(name)s:%(lineno)s:%(levelname)s:%(message)s"
json_formatter = jsonlogger.JsonFormatter(log_format)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

#terminal_handler = logging.StreamHandler()
#terminal_handler.setFormatter(logging.Formatter(terminal_format))

file_handler = logging.FileHandler('student.log')
file_handler.setFormatter(json_formatter)
#file_handler.setLevel(logging.ERROR)

json_stream_handler = logging.StreamHandler()
json_stream_handler.setFormatter(json_formatter)
json_stream_handler.setLevel(logging.CRITICAL)

# log.addHandler(terminal_handler)
log.addHandler(json_stream_handler)
log.addHandler(file_handler)


class Student(object):
    def __init__(self, name, gpa):
        self.name = name
        self.grades = gpa

        log.info(f'Student info created for "{name}"')
        log.info(f'Student info created for "{name}"', extra={'age':24, 'city':'Berlin'})


        # German Education System 😋
        if gpa > 3.85:
            log.critical('grades are far too low. Please consider putting more work')

        if gpa == 0:
            log.error("GPA can't be zero")


s = Student('Jane', 1.3)
s = Student('Max', 3.9)
s = Student('Puppy', 0)
