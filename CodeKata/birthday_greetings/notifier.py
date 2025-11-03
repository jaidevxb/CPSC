class EmailNotifier:
    def send_birthday_greeting(self, friend):
        subject = "Happy birthday!"
        body = f"Happy birthday, dear {friend.first_name}!"
        print(f"To: {friend.email}\nSubject: {subject}\n\n{body}\n")

    def send_birthday_reminder(self, receiver, birthday_friends):
        names = ", ".join([f"{f.first_name} {f.last_name}" for f in birthday_friends])
        subject = "Birthday Reminder"
        body = f"Dear {receiver.first_name},\n\nToday is {names}'s birthdays.\nDon't forget to send them each a message!"
        print(f"To: {receiver.email}\nSubject: {subject}\n\n{body}\n")
