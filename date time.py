 datetime import datetime
my_date_string = "september 11 2022 11:31AM"
datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')
print(type(datetime_object))
print(datetime_object)
