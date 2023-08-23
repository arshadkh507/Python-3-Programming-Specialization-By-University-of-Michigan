# Note

# The technique of start small and keep improving is the basis of Agile software development. This practice is used widely in the industry.

# Ok, lets look at an example. Lets solve the problem posed in question 3 at the end of the Simple Python Data chapter. Ask the user for the time now (in hours 0 – 23), and ask for the number of hours to wait. Your program should output what the time will be on the clock when the alarm goes off.

# So, where to start? The problem requires two pieces of input from the user, so lets start there and make sure we can get the data we need.

# current_time = input("what is the current time (in hours)?")
# wait_time = input("How many hours do you want to wait")

# print(current_time)
# print(wait_time)


# If you haven’t yet, click Run: get in the habit of checking whether small things are working before you go on.

# So far so good. Now lets take the next step. We need to figure out what the time will be after waiting wait_time number of hours. A good first approximation to that is to simply add wait_time to current_time and print out the result. So lets try that.


current_time = input("what is the current time (in hours 0--23)?")
wait_time = input("How many hours do you want to wait")

print(current_time)
print(wait_time)

final_time = current_time + wait_time
print(final_time)
