#!/usr/bin/env python3

import json

print("Testing Phase 12 Matrix Operations")
print("=" * 50)

# Test matrix addition: [[1,2],[3,4]] + [[5,6],[7,8]] = [[6,8],[10,12]]
print("\n1. Matrix Addition Test:")
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
result = []
for i in range(len(m1)):
    row = []
    for j in range(len(m1[0])):
        row.append(m1[i][j] + m2[i][j])
    result.append(row)
print(f"   {m1} + {m2} = {result}")

# Test matrix multiplication: [[1,2],[3,4]] × [[5,6],[7,8]] = [[19,22],[43,50]]
print("\n2. Matrix Multiplication Test:")
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
result = []
for i in range(len(m1)):
    row = []
    for j in range(len(m2[0])):
        dot_product = sum(m1[i][k] * m2[k][j] for k in range(len(m1[0])))
        row.append(dot_product)
    result.append(row)
print(f"   {m1} × {m2} = {result}")

# Test matrix determinant: det([[1,2],[3,4]]) = 1*4 - 2*3 = -2
print("\n3. Matrix Determinant Test (2x2):")
m = [[1, 2], [3, 4]]
det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
print(f"   det({m}) = {det}")

# Test matrix determinant: det([[1,0,2],[−1,5,0],[0,3,−9]]) = 1*(5*(-9) - 0*3) = -45
print("\n4. Matrix Determinant Test (3x3):")
m = [[1, 0, 2], [-1, 5, 0], [0, 3, -9]]
# Using first row expansion
det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - 
       m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + 
       m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
print(f"   det({m}) = {det}")

# Test matrix transpose: [[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]]
print("\n5. Matrix Transpose Test:")
m = [[1, 2, 3], [4, 5, 6]]
transpose = []
for col in range(len(m[0])):
    new_row = []
    for row in range(len(m)):
        new_row.append(m[row][col])
    transpose.append(new_row)
print(f"   transpose({m}) = {transpose}")

print("\nJSON format examples for MCP server:")
print(f'   Matrix: {json.dumps([[1,2],[3,4]])}')
print(f'   Matrix: {json.dumps([[1,2,3],[4,5,6]])}')
