# Simple Interest Calculator

def calculate_simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

print("=== Simple Interest Calculator ===")

try:
    principal = float(input("Enter Principal amount: "))
    rate = float(input("Enter Rate of interest (%): "))
    time = float(input("Enter Time (years): "))

    result = calculate_simple_interest(principal, rate, time)

    print(f"\nSimple Interest = {result}")

except ValueError:
    print("❌ Please enter valid numeric values!")
