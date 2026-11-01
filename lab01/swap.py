first_room = input("Название первой аудитории: ")
second_room = input("Название второй аудитории: ")

print()
print(f"До обмена:    first_room = {first_room}, second_room = {second_room}")

temp_room = first_room
first_room = second_room
second_room = temp_room

print(f"После обмена: first_room = {first_room}, second_room = {second_room}")