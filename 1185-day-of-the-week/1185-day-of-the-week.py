class Solution(object):
    def dayOfTheWeek(self, day, month, year):

        if month == 1 or month == 2:
            month += 12
            year -= 1

        k = year % 100
        j = year // 100

        result = (day + (13 * (month + 1) // 5) + k + k // 4 + j // 4 + 5 * j) % 7

        if result == 0:
            return "Saturday"
        elif result == 1:
            return "Sunday"
        elif result == 2:
            return "Monday"
        elif result == 3:
            return "Tuesday"
        elif result == 4:
            return "Wednesday"
        elif result == 5:
            return "Thursday"
        else:
            return "Friday"