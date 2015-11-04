




__author__ = 'Pratik'

class Task:
    __slot__ = 'name', 'timeLeft'

    def __init__(self, name, timeLeft):
        self.name = name
        self.timeLeft = timeLeft

    def after(self, task):
        return self.timeLeft > task.timeLeft

    def getName(self):
        return self.name

    def getTimeLeft(self):
        return self.timeLeft

    def __eq__(self, other):
        return self.timeLeft == other.timeLeft

    def __str__(self):
        return "(job: " + self.name + ", timeLeft: " + str(self.timeLeft) + ")"
