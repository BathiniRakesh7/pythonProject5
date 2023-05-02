def calculating_A_beats_by_B(time_taken_by_A, time_taken_by_B, race_distance, time_difference):
    A_beats_by_B = (race_distance / time_taken_by_B * time_difference)
    print(A_beats_by_B)


def calculating_B_beats_by_A(time_taken_by_A, time_taken_by_B, race_distance, time_difference):
    B_beats_by_A = (race_distance / time_taken_by_A * time_difference)
    print(B_beats_by_A)

race_distance = int(input("enter race distance = "))
time_taken_by_A = int(input("enter time taken by A = "))
time_taken_by_B = int(input("enter time taken by B = "))
condition = input('a)A_beats_by_B or b)B_beats_by_A ').lower()

if condition == "a":
    time_difference = time_taken_by_B - time_taken_by_A
    calculating_A_beats_by_B(time_taken_by_A, time_taken_by_B, race_distance, time_difference)
else:
    time_difference = time_taken_by_A - time_taken_by_B
    calculating_B_beats_by_A(time_taken_by_A, time_taken_by_B, race_distance, time_difference)
