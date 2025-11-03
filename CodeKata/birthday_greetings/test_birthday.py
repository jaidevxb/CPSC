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


# ✅ 1. Regular birthday case
def test_regular_birthday():
    john = Friend("Doe", "John", "1990-10-31", "john@example.com")
    mary = Friend("Ann", "Mary", "1992-11-01", "mary@example.com")

    repo = DummyRepo([john, mary])
    notifier = DummyNotifier()
    service = BirthdayService(repo, notifier)

    service.send_greetings(date(2025, 10, 31))

    assert "John" in notifier.sent
    assert len(notifier.reminders) == 1  # Mary got a reminder


# ✅ 2. Leap year Feb 29
def test_feb_29_leap_year():
    leap = Friend("Leap", "Leo", "2000-02-29", "leo@example.com")
    repo = DummyRepo([leap])
    notifier = DummyNotifier()
    service = BirthdayService(repo, notifier)

    service.send_greetings(date(2024, 2, 29))
    assert "Leo" in notifier.sent


# ✅ 3. Non-leap year Feb 29 handled as Feb 28
def test_feb_29_non_leap_year():
    leap = Friend("Leap", "Leo", "2000-02-29", "leo@example.com")
    repo = DummyRepo([leap])
    notifier = DummyNotifier()
    service = BirthdayService(repo, notifier)

    service.send_greetings(date(2025, 2, 28))
    assert "Leo" in notifier.sent


# ✅ 4. Multiple birthdays on same day
def test_multiple_birthdays_same_day():
    a = Friend("One", "Alice", "1990-05-20", "alice@example.com")
    b = Friend("Two", "Bob", "1995-05-20", "bob@example.com")
    c = Friend("Three", "Charlie", "2000-08-15", "charlie@example.com")

    repo = DummyRepo([a, b, c])
    notifier = DummyNotifier()
    service = BirthdayService(repo, notifier)

    service.send_greetings(date(2025, 5, 20))

    assert "Alice" in notifier.sent
    assert "Bob" in notifier.sent
    assert "Charlie" not in notifier.sent
    # Charlie should get a reminder about Alice & Bob
    assert ("Charlie", ["Alice", "Bob"]) in notifier.reminders


# ✅ 5. No birthdays today
def test_no_birthdays_today():
    a = Friend("One", "Alice", "1990-05-20", "alice@example.com")
    b = Friend("Two", "Bob", "1995-06-01", "bob@example.com")

    repo = DummyRepo([a, b])
    notifier = DummyNotifier()
    service = BirthdayService(repo, notifier)

    service.send_greetings(date(2025, 7, 1))

    assert notifier.sent == []  # No birthday messages
    assert len(notifier.reminders) == 0  # No reminders since no birthdays exist


# ✅ 6. Reminder content accuracy
def test_reminder_content_accuracy():
    a = Friend("One", "Alice", "1990-10-31", "alice@example.com")
    b = Friend("Two", "Bob", "1995-07-20", "bob@example.com")
    repo = DummyRepo([a, b])
    notifier = DummyNotifier()
    service = BirthdayService(repo, notifier)

    service.send_greetings(date(2025, 10, 31))

    # Alice gets greeting
    assert "Alice" in notifier.sent
    # Bob gets reminder about Alice
    assert notifier.reminders == [("Bob", ["Alice"])]


# ✅ 7. Edge case – invalid date of birth (should raise ValueError)
import pytest

def test_invalid_date_raises_value_error():
    with pytest.raises(ValueError):
        Friend("Error", "Eve", "invalid-date", "eve@example.com")
