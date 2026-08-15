class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg

class TooOldException(Exception):
    def __init__(self, msg):
        self.msg = msg

age = 11

if age < 18:
    raise TooYoungException("Age < 20")
elif age > 60:
    raise TooOldException("Age > 60")
else:
    print(age)