def car_talk(miles, start, end):
    str_miles = str(miles)[start:end]
    return str_miles == str_miles[::-1]


def check_miles(mile):
    return (car_talk(mile, 2, 6) and
            car_talk(mile+1, 1, 6) and
            car_talk(mile+2, 1, 5) and
            car_talk(mile+3, 0, 6))


def check_all():
    init_mile = 100000
    while init_mile <= 999996:
        check_miles(init_mile)
        if check_miles(init_mile):
            print(init_mile)
        init_mile = init_mile + 1


print("The following are the possible odometer readings: ")
check_all()
print()
