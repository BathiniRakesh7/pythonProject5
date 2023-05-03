
A_beat_B = int(input("A beat B="))
B_beat_C = int(input("B beat C="))
A = int(input("Winner distance of A= "))
B = A - A_beat_B
b = int(input("Winning distance of b="))
C = b - B_beat_C
distance = (A / B * b / C)
a_beat_c = int(input("A beat C in how much distance="))
A_beat_C = a_beat_c - (a_beat_c / distance)
print("A_beat_C ="+ str(A_beat_C))