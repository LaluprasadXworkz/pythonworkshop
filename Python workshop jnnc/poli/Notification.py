class Notification:

    def get_notification(self):
        pass

class Insagram(Notification):

    def get_notification(self):
        print("Notification from Insagram")

class FaceBook(Notification):

    def get_notification(self):
        print("Notification from FaceBook")


instgram=Insagram()
instgram.get_notification()
faceBook=FaceBook()
faceBook.get_notification()



