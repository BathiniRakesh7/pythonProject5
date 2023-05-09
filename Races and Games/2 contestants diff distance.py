condition = input("1)different distance or 2)finding time or 3) to find distance by time or 4)finding distance by speed ratios or 5)findind two speeds or to 6)find one speed = ")

if condition == "1":
    A = float(input("A runs a distance ="))
    B = float(input("B runs a distance ="))
    distance = (B/A)
    print(f'distance = {B/A}')

    dif_distance = float(input("B beat A in how much distance ="))
    B_beat_A = dif_distance-(dif_distance/distance)
    print(f'B beat A = {dif_distance}- {dif_distance}/{distance}')
    print("B beats by A =" + str(B_beat_A) + "m")

elif condition == "2":
    race_distance = float(input("Enter the race distance in meters="))
    A_beat_B_distance = float(input("Enter A beats by B distance in meters="))
    A_beat_B_time = float(input("Enter A beats by B time in sec="))
    time_taken_B = (A_beat_B_time / A_beat_B_distance * race_distance)

    print(f'time taken by B = {A_beat_B_time}/{A_beat_B_distance}*{race_distance}')
    print("Time taken by B =" + str(time_taken_B) + "sec")

    time_taken_A = (time_taken_B - A_beat_B_time)
    print(f'time taken by A = {time_taken_B}-{A_beat_B_time}')
    print("Time taken by A =" + str(time_taken_A) + "sec")

elif condition == "3":
    race_distance = int(input("enter race distance = "))
    time_taken_by_winner = int(input("enter time taken by winner = "))
    time_taken_by_losser = int(input("enter time taken by losser = "))
    time_difference = time_taken_by_losser - time_taken_by_winner
    winner_beats_by_losser = (race_distance / time_taken_by_losser * time_difference)
    print(f' winner beat losser = {race_distance}/{time_taken_by_losser}*{time_difference}')
    print("winner_beat_losser =" + str(winner_beats_by_losser) + 'm')
elif condition == "4":
    condition = input("1)To find race distance or 2)To find win by = ")

    if condition == "1":
        A_speed_ratio = int(input("speed ratio of A ="))
        B_speed_ratio = int(input("speed ratio of B ="))
        speed_gain_by_winner = (A_speed_ratio - B_speed_ratio)
        A_gives_start_to_B = float(input("A gives a start ="))
        race_distance = (A_speed_ratio * A_gives_start_to_B / speed_gain_by_winner)
        print(f"race distance = {A_speed_ratio}*{A_gives_start_to_B}/{speed_gain_by_winner}")
        print("race distance=" + str(race_distance) + "m")

    else:
        race_distance = float(input("race distance ="))
        A_speed_ratio = int(input("speed ratio of A ="))
        B_speed_ratio = int(input("speed ratio of B ="))
        A_is_start_of_B = float(input("A has start of B ="))

        distance_covered_A = (race_distance - A_is_start_of_B)
        print(f'distance covered by A = {race_distance}-{A_is_start_of_B}')
        print("distance covered by A =" + str(distance_covered_A))

        distance_covered_B = (B_speed_ratio / A_speed_ratio * distance_covered_A)
        print(f'distance covered by B = {B_speed_ratio}/{A_speed_ratio}*{distance_covered_A}')
        print("distance covered by B =" + str(distance_covered_B))

        A_wins_by = (race_distance - distance_covered_B)
        print(f'A wins by = {race_distance}-{distance_covered_B}')
        print("A wins by =" + str(A_wins_by) + "m")

elif condition == "5":
    A_distance = float(input("A distance covered = "))
    A_beats_B = float(input(" A beats by B distance = "))
    B_distance = (A_distance - A_beats_B)
    print(f'B covered distance ={B_distance}')
    first_race_time_difference = float(input("first race time difference ="))
    other_time_difference = float(input("another race time difference ="))
    time_taken_by_A = (first_race_time_difference * A_distance - B_distance * other_time_difference) / (
                B_distance - A_distance)
    print(
        f'time taken by A = {first_race_time_difference}*{A_distance}-{B_distance}*{other_time_difference}/{B_distance}-{A_distance}')
    print(f'time taken by A = {time_taken_by_A} sec')
    time_taken_by_B = (time_taken_by_A + first_race_time_difference)
    print(f'time taken by B = {time_taken_by_A}+{first_race_time_difference}')
    print(f'time taken by B = {time_taken_by_B} sec')
    speed_of_A = (A_distance / time_taken_by_A)
    print(f'speed of A = {A_distance}/{time_taken_by_A}')
    speed_of_B = (B_distance / time_taken_by_B)
    print(f'speed of A = {B_distance}/{time_taken_by_A}')
    print(f'speed of A =  {round(speed_of_A, 2)} m/sec')
    print(f'speed of B = {round(speed_of_B, 2)} m/sec')