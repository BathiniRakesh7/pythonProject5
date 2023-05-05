def calculating_A_beats_by_B(time_taken_by_A, time_taken_by_B, race_distance, time_difference):
    A_beats_by_B = (race_distance / time_taken_by_B * time_difference)
    print(f'A beat B = {race_distance}/{time_taken_by_B}*{time_difference}')
    print("A_beat_B ="+str(A_beats_by_B) + 'm')


def calculating_B_beats_by_A(time_taken_by_A, time_taken_by_B, race_distance, time_difference):
    B_beats_by_A = (race_distance / time_taken_by_A * time_difference)
    print(f'B beat A = {race_distance}/{time_taken_by_A}*{time_difference}')
    print("B_beat_A ="+str(B_beats_by_A) + 'm')

condition = input('a)A_beats_by_B or b)B_beats_by_A =').lower()
race_distance = int(input("enter race distance = "))
time_taken_by_A = int(input("enter time taken by A = "))
time_taken_by_B = int(input("enter time taken by B = "))

if condition == "a":
    time_difference = time_taken_by_B - time_taken_by_A
    calculating_A_beats_by_B(time_taken_by_A, time_taken_by_B, race_distance, time_difference)
else:
    time_difference = time_taken_by_A - time_taken_by_B
    calculating_B_beats_by_A(time_taken_by_A, time_taken_by_B, race_distance, time_difference)
