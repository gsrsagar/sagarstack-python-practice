

class SMSService:

    def notify(self):
        print("Send sms ")

class EmailService:

    def notify(self):
        print("Send email")

def getNotity(service):
    return service.notify()


o = getNotity(SMSService()) #depdendency it is procees of ginving teh refeernce
obj1 = getNotity(EmailService())


