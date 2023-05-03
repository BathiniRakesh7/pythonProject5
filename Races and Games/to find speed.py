condition=input("need to find speed = 1)kmph or 2)m/sec")
if condition=="1":
    A_distance=int(input("A distance ="))
    A_gives_B=int(input("A gives B a Start of ="))
    B_distance=A_distance-A_gives_B
    A_speed=int(input("speed of A = "))*(5/18)
    A_beat_B=int(input("A beats by B in secs ="))
    time_taken_by_A=(A_distance/A_speed)
    print("time taken by A ="+ str(time_taken_by_A)+"sec")
    time_taken_by_B=time_taken_by_A + A_beat_B
    print("time taken by B ="+ str(time_taken_by_B)+"sec")
    B_speed= (B_distance/time_taken_by_B)*(18/5)
    print("Speed of B ="+ str(B_speed)+ "kmph")
else:
    A_distance=int(input("A distance ="))
    A_gives_B=int(input("A gives B a Start of ="))
    B_distance=A_distance-A_gives_B
    A_speed=int(input("speed of A = "))*(18/5)
    A_beat_B=int(input("A beats by B in secs ="))
    time_taken_by_A=(A_distance/A_speed)
    print("time taken by A ="+ str(time_taken_by_A)+"sec")
    time_taken_by_B=time_taken_by_A + A_beat_B
    print("time taken by B ="+ str(time_taken_by_B)+"sec")
    B_speed= (B_distance/time_taken_by_B)
    print("Speed of B ="+ str(B_speed)+ "m/sec")
