from datetime import date
from calendar import monthrange

class MeetupDayException(Exception):
    pass

days = {'Monday' : 0,
'Tuesday' : 1,
'Wednesday' : 2,
'Thursday' : 3,
'Friday' : 4,
'Saturday' : 5,
'Sunday' : 6
}
week_selection = {'1st' : 0, '2nd' : 1, '3rd' : 2, '4th' : 3, '5th' : 4}
teenth_days = [13,14,15,16,17,18,19]

def meetup(year, month, week, day_of_week):
    # make list of all possible week days for the given day_of_week
    n_days_in_month = [x for x in monthrange(year,month)]
    days_matching_given_day_of_week = []
    for d in range(1,n_days_in_month[1]+1):
        if date(year, month, d).weekday() == days[day_of_week]:
            days_matching_given_day_of_week.append(d)
    # select the day of the week from the list
    if week == "teenth":
        day = list(set(teenth_days) & set(days_matching_given_day_of_week))[0]
    elif week == "last":
        day = days_matching_given_day_of_week[-1]
    else:
        if week_selection[week] >= len(days_matching_given_day_of_week):
            raise MeetupDayException(f"Invalid input.")
        else:
            day = days_matching_given_day_of_week[week_selection[week]]
    return date(year, month, day)

