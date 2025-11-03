from datetime import date
from friend_repository import FriendRepository
from notifier import EmailNotifier
from birthday_service import BirthdayService

if __name__ == "__main__":
    repo = FriendRepository("friends.csv")
    notifier = EmailNotifier()
    service = BirthdayService(repo, notifier)
    service.send_greetings(date.today())
