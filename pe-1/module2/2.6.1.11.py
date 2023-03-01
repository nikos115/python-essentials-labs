hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

end_in_mins = hour * 60 + mins + dura

end_hour = end_in_mins // 60 % 24  # take care in case duration hours are more than a day
end_mins =  end_in_mins % 60

print (str(end_hour) + ':' + str(end_mins))
