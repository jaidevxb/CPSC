from datetime import date

class Friend:
    def __init__(self, last_name, first_name, dob, email):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date.fromisoformat(dob)
        self.email = email

    def is_birthday(self, today=None):
        today = today or date.today()
        # Handle Feb 29 special case
        if self.date_of_birth.month == 2 and self.date_of_birth.day == 29:
            if not (today.year % 4 == 0 and (today.year % 100 != 0 or today.year % 400 == 0)):
                return today.month == 2 and today.day == 28
        return (self.date_of_birth.month, self.date_of_birth.day) == (today.month, today.day)
