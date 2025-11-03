class BirthdayService:
    def __init__(self, repository, notifier):
        self.repository = repository
        self.notifier = notifier

    def send_greetings(self, today):
        friends = self.repository.get_all_friends()
        birthday_friends = [f for f in friends if f.is_birthday(today)]

        # Send birthday message
        for f in birthday_friends:
            self.notifier.send_birthday_greeting(f)

        # Send reminders to others
        for f in friends:
            if f not in birthday_friends:
                self.notifier.send_birthday_reminder(f, birthday_friends)
