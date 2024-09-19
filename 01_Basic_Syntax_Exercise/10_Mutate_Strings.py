starting_string = input()
finished_string = input()

previous_string = starting_string
current_string = ""

for index in range(len(starting_string)):
     for j in range(index + 1):
         current_string += finished_string[j]
     for k in range(index + 1, len(starting_string)):
         current_string += starting_string[k]
     if not current_string == previous_string:
         print(current_string)
     previous_string = current_string
     current_string = ""