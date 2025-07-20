#!/usr/bin/env python3

import math

print("Testing Phase 11 Advanced Calculator Functions")
print("=" * 50)

# Test quadratic formula: x² - 5x + 6 = 0
# Should factor to (x-2)(x-3) = 0, so x = 2 and x = 3
print("\n1. Quadratic Solver Test: x² - 5x + 6 = 0")
a, b, c = 1, -5, 6
discriminant = b**2 - 4*a*c
print(f"   Discriminant: {discriminant}")
if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"   Solutions: x₁ = {x1}, x₂ = {x2}")
    print(f"   Verification: {x1}² - 5({x1}) + 6 = {x1**2 - 5*x1 + 6}")
    print(f"   Verification: {x2}² - 5({x2}) + 6 = {x2**2 - 5*x2 + 6}")

# Test 2D distance: (0,0) to (3,4) should be 5
print("\n2. Distance Formula Test: (0,0) to (3,4)")
distance = math.sqrt((3-0)**2 + (4-0)**2)
print(f"   Distance: {distance} (should be 5 for 3-4-5 triangle)")

# Test slope: (0,0) to (2,2) should be 1
print("\n3. Slope Test: (0,0) to (2,2)")
slope_val = (2-0)/(2-0)
print(f"   Slope: {slope_val} (should be 1 for 45° line)")

# Test compound interest: $1000 at 5% for 10 years, monthly compounding
print("\n4. Compound Interest Test: $1000 at 5% for 10 years, monthly")
principal, rate, time, n = 1000, 0.05, 10, 12
final_amount = principal * (1 + rate/n)**(n*time)
interest_earned = final_amount - principal
print(f"   Principal: ${principal:,.2f}")
print(f"   Final Amount: ${final_amount:,.2f}")
print(f"   Interest Earned: ${interest_earned:,.2f}")
print(f"   Effective Rate: {((final_amount/principal)**(1/time) - 1)*100:.2f}% per year")
