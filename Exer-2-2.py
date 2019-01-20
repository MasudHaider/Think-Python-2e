# Exer-2-2(1)
r = 5
pi = 3.14159
sphere = 4/3 * pi * r**3
print(sphere)

# Exer-2-2(2)
price_of_cover = 24.95
discount = price_of_cover * 0.40
price_after_discount = price_of_cover - discount
total_copies = 60
shipping = 3 + (total_copies - 1) * 0.75
cost_for_sixty_copy = total_copies * price_after_discount + shipping
print(cost_for_sixty_copy)

# Exer-2-2(3)
house_leaving_time = (6 * 60 + 52) * 60
easy_pace = 8 * 60 + 15
tempo_pace = 7 * 60 + 12

miles_on_easy_pace = 2
miles_on_tempo_pace = 3

time_on_easy_pace = miles_on_easy_pace * easy_pace
time_on_tempo_pace = tempo_pace * miles_on_tempo_pace

finish_run_hour = (house_leaving_time + time_on_easy_pace + time_on_tempo_pace) / (60*60.0)
finish_run_floored = (house_leaving_time + time_on_easy_pace + time_on_tempo_pace) // (60*60.0)
finish_run_min = (finish_run_hour - finish_run_floored) * 60

print("%d:%d" %(finish_run_hour, finish_run_min))
