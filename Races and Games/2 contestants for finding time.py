race_distance=float(input("Enter the race distance in meters="))
A_beat_B_distance=float(input("Enter A beats by B distance in meters="))
A_beat_B_time=float(input("Enter A beats by B time in sec="))
time_taken_B=(A_beat_B_time/A_beat_B_distance*race_distance)
print("Time taken by B ="+str(time_taken_B)+"sec")
time_taken_A=(time_taken_B - A_beat_B_time)
print("Time taken by A ="+str(time_taken_A)+"sec")
