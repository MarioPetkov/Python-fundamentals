all_stops = input()
command = input()
while command != "Travel":
    tokens = command.split(':')
    if tokens[0] == "Add Stop":
        index, string = int(tokens[1]), tokens[2]
        if index in range(len(all_stops)):
            all_stops = all_stops[:index] + string + all_stops[index: ]
    elif tokens[0] == "Remove Stop":
        start_index, end_index = int(tokens[1]), int(tokens[2])
        if start_index in range(len(all_stops)) and end_index in range(len(all_stops)):
            all_stops = all_stops[:start_index] + all_stops[end_index + 1:]
    elif tokens[0] == "Switch":
        old_string, new_string = tokens[1], tokens[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
    print(all_stops)
    command = input()
print(f"Ready for world tour! Planned stops: {all_stops}")