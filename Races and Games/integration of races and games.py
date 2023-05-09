condition = input("1) two contestants or 2) three contestants or 3)four members game =")

if condition == "1":
    condition = input("1)different distance or 2)finding time or 3) to find distance by time or "
                  "\n4)finding distance by speed ratios or "
                  "5)finding two speeds or to 6) find one speed = ")



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
        time_taken_by_A = (first_race_time_difference * A_distance - B_distance * other_time_difference) / (B_distance - A_distance)
        print(f'time taken by A = {first_race_time_difference}*{A_distance}-{B_distance}*{other_time_difference}/{B_distance}-{A_distance}')
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

    else:
        condition = input("need to find speed = 1)kph or 2)m/sec =")
        if condition == "1":
            A_distance = float(input("A covered distance ="))
            A_gives_B = float(input("A gives B a Start of ="))
            B_distance = A_distance - A_gives_B
            print(f'B distance covered = {A_distance}- {A_gives_B}')
            print(f'B distance covered= {B_distance}')

            A_speed = float(input("speed of A = ")) * (5 / 18)
            A_beat_B = float(input("A beats by B in secs ="))
            time_taken_by_A = (A_distance / A_speed)
            print(f'time taken by A = {A_distance}/{A_speed}')
            print("time taken by A =" + str(time_taken_by_A) + "sec")

            time_taken_by_B = time_taken_by_A + A_beat_B
            print(f'time taken by B = {time_taken_by_A} +{A_beat_B}')
            print("time taken by B =" + str(time_taken_by_B) + "sec")

            B_speed = (B_distance / time_taken_by_B) * (18 / 5)
            print(f'speed B = {B_distance}/{time_taken_by_B}*{18 / 5}')
            print("Speed of B =" + str(B_speed) + "kph")
        else:
            A_distance = float(input("A distance ="))
            A_gives_B = float(input("A gives B a Start of ="))
            B_distance = A_distance - A_gives_B
            print(f'B distance covered = {A_distance}- {A_gives_B}')
            print(f'B distance covered= {B_distance}')

            A_speed = float(input("speed of A = ")) * (18 / 5)
            A_beat_B = float(input("A beats by B in secs ="))
            time_taken_by_A = (A_distance / A_speed)
            print(f'time taken by A = {A_distance}/{A_speed}')
            print("time taken by A =" + str(round(time_taken_by_A, 5)) + "sec")

            time_taken_by_B = time_taken_by_A + A_beat_B
            print(f'time taken by B = {time_taken_by_A} +{A_beat_B}')
            print("time taken by B =" + str(round(time_taken_by_B, 5)) + "sec")

            B_speed = (B_distance / time_taken_by_B)
            print(f'speed B = {B_distance}/{time_taken_by_B}')
            print("Speed of B =" + str(round(B_speed, 5)) + "m/sec")

elif condition == "2":
    condition = input("1) three different distance or 2) two distance or 3)finding time or 4)same distance")

    if condition == "1":
        A_beat_B = float(input("A beat B="))
        B_beat_C = float(input("B beat C="))
        A = float(input("Winner distance of A= "))
        B = A - A_beat_B
        print(f'B distance covered = {A}-{A_beat_B}')
        print(f'B distance covered = {B}')
        b = float(input("Winning distance of b="))
        C = b - B_beat_C
        print(f'C distance covered = {b}-{B_beat_C}')
        print(f'B distance covered = {C}')
        distance = (A / B * b / C)
        print(f'distance = {A}/{B}*{b}/{C}')
        print(f'distance = {round(distance, 3)}')
        a_beat_c = float(input("A beat C in how much distance="))
        A_beat_C = a_beat_c - (a_beat_c / distance)
        print("A_beat_C =" + str(A_beat_C) + "m")

    elif condition == "2":
        condition = input("1)B_beat_C or 2)C_beat_B=")

        if condition == "1":
            A_beat_B = float(input("A beat B="))
            A_beat_C = float(input("A beat C="))
            A = float(input("Winner distance of A= "))
            B = A - A_beat_B
            print(f'B distance covered = {A}-{A_beat_B}')
            print(f'B distance covered = {B}')
            C = A - A_beat_C
            print(f'C distance covered = {A}-{A_beat_C}')
            print(f'B distance covered = {C}')
            distance = (B / A * A / C)
            print(f'distance = {B}/{A}*{A}/{C}')
            print(f'distance = {round(distance, 3)}')
            b_beat_c = float(input("B beat C in how much distance="))
            B_beat_C = b_beat_c - (b_beat_c / distance)
            print(f'B beat C = {b_beat_c}-{b_beat_c}/{distance}')
            print("B_beat_C =" + str(B_beat_C) + "m")
        else:
            A_beat_B = float(input("A beat B="))
            A_beat_C = float(input("A beat C="))
            A = float(input("Winner distance of A= "))
            B = A - A_beat_B
            print(f'B distance covered = {A}-{A_beat_B}')
            print(f'B distance covered = {B}')
            C = A - A_beat_C
            print(f'C distance covered = {A}-{A_beat_C}')
            print(f'B distance covered = {C}')
            distance = (C / A * A / B)
            c_beat_b = float(input("C beat B in how much distance="))
            C_beat_B = c_beat_b - (c_beat_b / distance)
            print(f'B beat C = {c_beat_b}-{c_beat_b}/{distance}')
            print("C_beat_B =" + str(C_beat_B) + 'm')

    elif condition == "3":
        race_distance = float(input("Enter the race distance in meters="))
        A_beat_B_time = float(input("Enter A beats by B time in sec="))
        B_beat_C_time = float(input("Enter A beats by C time in sec="))
        A_beat_C = float(input("Enter A beats C distance ="))
        time_taken_C = (A_beat_B_time + B_beat_C_time)
        print(f' time taken by C = {A_beat_B_time} +{B_beat_C_time} sec')
        print("Time taken by C =" + str(time_taken_C) + "sec")

        total_time_taken_C = (time_taken_C / A_beat_C * race_distance)
        print(f'total time taken by C ={time_taken_C}/{time_taken_C}*{race_distance}')

        time_taken_A = (total_time_taken_C - time_taken_C)
        print(f'Time taken by A = {total_time_taken_C}-{time_taken_C}')
        print("Time taken by A =" + str(time_taken_A) + "sec")

    else:
        def A_beat_C():
            A_beat_B = int(input("A beat B="))
            B_beat_C = int(input("B beat C="))
            A = int(input("Winner distance of A= "))
            B = A - A_beat_B
            print(f'B covered distance = {A} - {A_beat_B} ')
            b = int(input("Winning distance of b="))
            C = b - B_beat_C
            print(f'A covered distance ={b}-{B_beat_C}')
            distance = (A / B * b / C)
            print(f'distance ={A}/{B}*{b}/{C}')
            A_beat_C = A - (A / distance)
            print(f'A beat C= {A}-{A}/{distance}')
            return A_beat_C


        def B_beat_C():
            B_beat_A = int(input("B beat A="))
            A_beat_C = int(input("A beat C="))
            B = int(input("Winner distance of B= "))
            A = B - B_beat_A
            print(f'A = {B} - {B_beat_A} ')
            a = int(input("Winning distance of a="))
            C = a - A_beat_C
            print(f'A ={a}-{A_beat_C}')
            distance = (B / A * a / C)
            print(f'distance ={B}/{A}*{a}/{C}')
            B_beat_C = B - (B / distance)
            print(f'B beat C= {B}-{B}/{distance}')
            return B_beat_C


        def C_beat_A():
            C_beat_B = int(input("C beat B="))
            B_beat_A = int(input("B beat A="))
            C = int(input("Winner distance of C= "))
            B = C - C_beat_B
            print(f'B = {C} - {C_beat_B} ')
            b = int(input("Winning distance of b="))
            A = b - B_beat_A
            print(f'A ={b}-{B_beat_A}')
            distance = (C / B * b / A)
            print(f'distance ={C}/{B}*{b}/{A}')
            C_beat_A = C - (C / distance)
            print(f'C beat A= {C}-{C}/{distance}')
            return C_beat_A


        condition = input("1)A_beat_C or 2)B_beat_C or 3)C_beat_A=")
        if condition == "1":
            print("A_beat_C=" + str(A_beat_C()) + 'm')

        elif condition == "2":
            print("B_beat_C=" + str(B_beat_C()) + 'm')

        else:
            print("C_beat_A=" + str(C_beat_A()) + 'm')

else:
    a = list(map(int, input().split()))
    length = len(a)
    total = 0
    for i in range(length):
        for j in range(length):
            total = a[j] / 2
            a[j] = a[j] / 2
            a[length - i - 1] += total
        print(a)
