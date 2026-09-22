class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        from datetime import datetime,timedelta
        date1 = datetime.strptime(date1,"%Y-%m-%d")
        date2 = datetime.strptime(date2 ,"%Y-%m-%d")
        diff = abs(date1 - date2) 
        return diff.days