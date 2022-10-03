def computepay(h, r):
    if h > 40.0:
        return ((h - 40) * r * 1.5) + (40 * r)
    return h * r

hrs = float(input("Enter Hours:\n"))
rate = float(input("Enter Rate per Hour:\n"))
p = computepay(hrs, rate)
print("Pay", p)