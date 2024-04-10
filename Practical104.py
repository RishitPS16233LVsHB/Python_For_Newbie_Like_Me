class Clock:
    def __init__(self, time):
        self.time = time

    def display_time(self):
        print("Time:", self.time)

class Calendar:
    def __init__(self, date):
        self.date = date

    def display_date(self):
        print("Date:", self.date)

class CalendarClock(Clock, Calendar):
    def __init__(self, time, date):
        Clock.__init__(self, time)
        Calendar.__init__(self, date)

# Example usage:
calendar_clock = CalendarClock("10:00 AM", "2024-04-10")
calendar_clock.display_time()
calendar_clock.display_date()
