from datetime import date
from friend import Friend
from birthday_service import BirthdayService

class DummyRepo:
    def __init__(self, friends):
        self._friends = friends
    def get_all_friends(self):
        return self._friends

class DummyNotifier:
    def __init__(self):
        self.sent = []
        self.reminders = []
    def send_birthday_greeting(self, friend):
        self.sent.append(friend.first_name)
    def send_birthday_reminder(self, receiver, birthday_friends):
        self.reminders.append((receiver.first_name, [f.first_name for f in birthday_friends]))

def test_regular_birthday():
    john = Friend("Doe", "John", "1990-10-31", "john@example.com")
    mary = Friend("Ann", "Mary", "1992-11-01", "mary@example.com")

    repo = DummyRepo([john, mary])
    notifier = DummyNotifier()
    service = BirthdayService(repo, notifier)

    service.send_greetings(date(2025, 10, 31))

    assert "John" in notifier.sent
    assert len(notifier.reminders) == 1 

def test_feb_29_leap_year():
    leap = Friend("Leap", "Leo", "2000-02-29", "leo@example.com")
    repo = DummyRepo([leap])
    notifier = DummyNotifier()
    service = BirthdayService(repo, notifier)

    service.send_greetings(date(2024, 2, 29))
    assert "Leo" in notifier.sent

def test_feb_29_non_leap_year():
    leap = Friend("Leap", "Leo", "2000-02-29", "leo@example.com")
    repo = DummyRepo([leap])
    notifier = DummyNotifier()
    service = BirthdayService(repo, notifier)

    service.send_greetings(date(2025, 2, 28))
    assert "Leo" in notifier.sent
