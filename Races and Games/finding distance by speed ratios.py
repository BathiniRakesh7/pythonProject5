
race_distace=float(input("race distance ="))
A_speed_ratio=int(input("speed ratio of A ="))
B_speed_ratio=int(input("speed ratio of B ="))
A_is_start_of_B=float(input("A has start of B ="))

distance_covered_A=(race_distace - A_is_start_of_B)
print("distance covered by A =" + str(distance_covered_A))

distance_covered_B=(B_speed_ratio/A_speed_ratio*distance_covered_A)
print("distance covered by B =" + str(distance_covered_B))

A_wins_by=(race_distace - distance_covered_B )
print("A wins by ="+ str(A_wins_by))
