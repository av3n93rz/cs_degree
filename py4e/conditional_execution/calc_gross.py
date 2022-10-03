hrs = float(input("Enter Hours:\n"))
rate = float(input("Enter Rate per hour:\n"))
if hrs > 40:
    print(((hrs - 40) * (rate * 1.5)) + (40 * rate))
else:
    print(hrs * rate)