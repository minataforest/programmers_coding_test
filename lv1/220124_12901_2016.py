from datetime import datetime

def solution(a, b):
    datetime_date = datetime.strptime('2016-'+str(a)+'-'+str(b), '%Y-%m-%d')
    temp = datetime_date.weekday()
    
    day = {0: 'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    
    return day[temp]