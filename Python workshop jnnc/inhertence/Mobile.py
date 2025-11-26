class Mobile:

    def callings(self):
        print('Invoking Calling Function')

    def sms(self):
        print("Invoking SMS Method")

    def games(self):
        print("Invoking games")


class Mi_note_8_pro(Mobile):

    def cam(self):
        print("Invoking cam Method")

    def music(self):
        print("Invoking music Method")

    def vedio_call(self):
        print("Invoking Vedio call Method")


minote8pro=Mi_note_8_pro()
minote8pro.music()