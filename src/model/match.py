import re


class IsCellphone():
    def __init__(self):
        self.p = re.compile(r'[1][^1269]\d{9}')

    def iscellphone(self, number):
        res = self.p.match(number)
        if res:
            return True
        else:
            return False


class IsMail():
    def __init__(self):
        self.p = re.compile(r'[^\._][\w\._-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$')

    def ismail(self, str):
        res = self.p.match(str)
        if res:
            return True
        else:
            return False
