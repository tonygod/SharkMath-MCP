# SharkMath MCP Server - AI Agent Test Prompts

## Overview
This document contains comprehensive mathematical questions designed to test the SharkMath MCP server through AI agent interactions. Each prompt is designed to trigger specific MCP tools and validate their functionality in real-world usage scenarios.

## Test Categories

### 1. Basic Arithmetic Operations

#### Test 1.1 - Simple Addition
**Prompt**: "What is 47 + 293?"
**Expected MCP Tool**: `add`
**Test ID**: ARITH_001

#### Test 1.2 - Subtraction with Negative Result
**Prompt**: "Calculate 125 - 347. What's the result?"
**Expected MCP Tool**: `subtract`
**Test ID**: ARITH_002

#### Test 1.3 - Multiplication of Decimals
**Prompt**: "I need to multiply 12.5 by 8.4. Can you help?"
**Expected MCP Tool**: `multiply`
**Test ID**: ARITH_003

#### Test 1.4 - Division with Remainder
**Prompt**: "Divide 157 by 23. What do you get?"
**Expected MCP Tool**: `divide`
**Test ID**: ARITH_004

#### Test 1.5 - Division by Zero (Error Handling)
**Prompt**: "What happens when I divide 50 by 0?"
**Expected MCP Tool**: `divide`
**Test ID**: ARITH_005

#### Test 1.6 - Complex Expression
**Prompt**: "Evaluate this expression: (15 + 3) * 4 - 8 / 2"
**Expected MCP Tool**: `calculate`
**Test ID**: ARITH_006

### 2. Power and Root Operations

#### Test 2.1 - Basic Exponentiation
**Prompt**: "What is 3 raised to the power of 7?"
**Expected MCP Tool**: `power`
**Test ID**: POWER_001

#### Test 2.2 - Square Calculation
**Prompt**: "I need to find the square of 23."
**Expected MCP Tool**: `square`
**Test ID**: POWER_002

#### Test 2.3 - Perfect Square Root
**Prompt**: "What's the square root of 169?"
**Expected MCP Tool**: `square_root`
**Test ID**: POWER_003

#### Test 2.4 - Cube Calculation
**Prompt**: "Calculate 12 cubed."
**Expected MCP Tool**: `cube`
**Test ID**: POWER_004

#### Test 2.5 - Cube Root
**Prompt**: "Find the cube root of 216."
**Expected MCP Tool**: `cube_root`
**Test ID**: POWER_005

#### Test 2.6 - Fourth Root
**Prompt**: "What is the 4th root of 81?"
**Expected MCP Tool**: `nth_root`
**Test ID**: POWER_006

### 3. Trigonometric Functions

#### Test 3.1 - Sine of Common Angle
**Prompt**: "What is the sine of π/2 radians?"
**Expected MCP Tool**: `sin`
**Test ID**: TRIG_001

#### Test 3.2 - Cosine in Degrees
**Prompt**: "Calculate the cosine of 60 degrees."
**Expected MCP Tool**: `cos_degrees`
**Test ID**: TRIG_002

#### Test 3.3 - Tangent of Zero
**Prompt**: "What is tan(0)?"
**Expected MCP Tool**: `tan`
**Test ID**: TRIG_003

#### Test 3.4 - Inverse Sine
**Prompt**: "Find the arcsine of 0.5."
**Expected MCP Tool**: `asin`
**Test ID**: TRIG_004

#### Test 3.5 - Two-Argument Arctangent
**Prompt**: "Calculate atan2(4, 3)."
**Expected MCP Tool**: `atan2`
**Test ID**: TRIG_005

### 4. Logarithmic and Exponential Functions

#### Test 4.1 - Natural Logarithm
**Prompt**: "What is the natural log of e squared?"
**Expected MCP Tool**: `natural_log`
**Test ID**: LOG_001

#### Test 4.2 - Base-10 Logarithm
**Prompt**: "Calculate log₁₀(1000)."
**Expected MCP Tool**: `log_base_10`
**Test ID**: LOG_002

#### Test 4.3 - Custom Base Logarithm
**Prompt**: "Find log₂(32)."
**Expected MCP Tool**: `log_base`
**Test ID**: LOG_003

#### Test 4.4 - Exponential Function
**Prompt**: "Calculate e^3."
**Expected MCP Tool**: `exponential`
**Test ID**: LOG_004

### 5. Statistical Operations

#### Test 5.1 - Mean of Dataset
**Prompt**: "Find the average of these numbers: 12, 15, 18, 22, 25, 30"
**Expected MCP Tool**: `mean`
**Test ID**: STATS_001

#### Test 5.2 - Median of Odd Dataset
**Prompt**: "What's the median of: 7, 12, 3, 19, 25, 8, 14?"
**Expected MCP Tool**: `median`
**Test ID**: STATS_002

#### Test 5.3 - Mode Identification
**Prompt**: "Find the mode in this dataset: 1, 2, 3, 2, 4, 2, 5, 6, 2"
**Expected MCP Tool**: `mode`
**Test ID**: STATS_003

#### Test 5.4 - Standard Deviation
**Prompt**: "Calculate the standard deviation of: 10, 12, 14, 16, 18"
**Expected MCP Tool**: `standard_deviation`
**Test ID**: STATS_004

#### Test 5.5 - Range and Statistics
**Prompt**: "What are the min, max, and range of: 25, 12, 38, 45, 7, 33?"
**Expected MCP Tool**: `range_stats`
**Test ID**: STATS_005

### 6. Matrix Operations

#### Test 6.1 - Matrix Addition
**Prompt**: "Add these two 2x2 matrices: [[1,2],[3,4]] and [[5,6],[7,8]]"
**Expected MCP Tool**: `matrix_add`
**Test ID**: MATRIX_001

#### Test 6.2 - Matrix Multiplication
**Prompt**: "Multiply matrices A = [[2,1],[3,4]] and B = [[1,0],[2,5]]"
**Expected MCP Tool**: `matrix_multiply`
**Test ID**: MATRIX_002

#### Test 6.3 - Matrix Determinant
**Prompt**: "Find the determinant of [[3,2],[1,4]]"
**Expected MCP Tool**: `matrix_determinant`
**Test ID**: MATRIX_003

#### Test 6.4 - Matrix Transpose
**Prompt**: "Transpose the matrix [[1,2,3],[4,5,6]]"
**Expected MCP Tool**: `matrix_transpose`
**Test ID**: MATRIX_004

### 7. Unit Conversions

#### Test 7.1 - Temperature Conversion
**Prompt**: "Convert 25°C to Fahrenheit."
**Expected MCP Tool**: `celsius_to_fahrenheit`
**Test ID**: CONV_001

#### Test 7.2 - Distance Conversion
**Prompt**: "How many miles is 50 kilometers?"
**Expected MCP Tool**: `kilometers_to_miles`
**Test ID**: CONV_002

#### Test 7.3 - Weight Conversion
**Prompt**: "Convert 150 pounds to kilograms."
**Expected MCP Tool**: `pounds_to_kilograms`
**Test ID**: CONV_003

#### Test 7.4 - Volume Conversion
**Prompt**: "How many liters are in 5 gallons?"
**Expected MCP Tool**: `gallons_to_liters`
**Test ID**: CONV_004

#### Test 7.5 - Angle Conversion
**Prompt**: "Convert 90 degrees to radians."
**Expected MCP Tool**: `degrees_to_radians`
**Test ID**: CONV_005

### 8. Advanced Mathematical Operations

#### Test 8.1 - Quadratic Equation
**Prompt**: "Solve the quadratic equation: x² - 5x + 6 = 0"
**Expected MCP Tool**: `solve_quadratic`
**Test ID**: ADV_001

#### Test 8.2 - Distance Between Points
**Prompt**: "Find the distance between points (3,4) and (7,1)."
**Expected MCP Tool**: `distance_2d`
**Test ID**: ADV_002

#### Test 8.3 - Slope Calculation
**Prompt**: "What's the slope of the line passing through (2,3) and (6,11)?"
**Expected MCP Tool**: `slope`
**Test ID**: ADV_003

#### Test 8.4 - Compound Interest
**Prompt**: "Calculate compound interest: $1000 principal, 5% annual rate, 3 years, compounded annually."
**Expected MCP Tool**: `compound_interest`
**Test ID**: ADV_004

### 9. Combinatorics and Number Theory

#### Test 9.1 - Factorial
**Prompt**: "What is 8 factorial?"
**Expected MCP Tool**: `factorial`
**Test ID**: COMB_001

#### Test 9.2 - Permutation
**Prompt**: "How many ways can I arrange 5 items taken 3 at a time?"
**Expected MCP Tool**: `permutation`
**Test ID**: COMB_002

#### Test 9.3 - Combination
**Prompt**: "Calculate C(10,4) - combinations of 10 items taken 4 at a time."
**Expected MCP Tool**: `combination`
**Test ID**: COMB_003

#### Test 9.4 - Fibonacci Number
**Prompt**: "What is the 12th Fibonacci number?"
**Expected MCP Tool**: `fibonacci`
**Test ID**: COMB_004

#### Test 9.5 - Prime Check
**Prompt**: "Is 97 a prime number?"
**Expected MCP Tool**: `is_prime`
**Test ID**: NUM_001

#### Test 9.6 - GCD Calculation
**Prompt**: "Find the greatest common divisor of 48 and 18."
**Expected MCP Tool**: `gcd`
**Test ID**: NUM_002

### 10. Precision and Rounding Operations

#### Test 10.1 - Decimal Rounding
**Prompt**: "Round 3.14159 to 3 decimal places."
**Expected MCP Tool**: `round_to_decimal`
**Test ID**: PREC_001

#### Test 10.2 - Floor Function
**Prompt**: "What is the floor of -2.7?"
**Expected MCP Tool**: `floor`
**Test ID**: PREC_002

#### Test 10.3 - Ceiling Function
**Prompt**: "Calculate the ceiling of 4.1."
**Expected MCP Tool**: `ceiling`
**Test ID**: PREC_003

#### Test 10.4 - Absolute Value
**Prompt**: "Find the absolute value of -15.8."
**Expected MCP Tool**: `absolute`
**Test ID**: PREC_004

### 11. Hyperbolic Functions

#### Test 11.1 - Hyperbolic Sine
**Prompt**: "Calculate sinh(2)."
**Expected MCP Tool**: `sinh`
**Test ID**: HYP_001

#### Test 11.2 - Hyperbolic Cosine
**Prompt**: "What is cosh(0)?"
**Expected MCP Tool**: `cosh`
**Test ID**: HYP_002

#### Test 11.3 - Hyperbolic Tangent
**Prompt**: "Find tanh(1)."
**Expected MCP Tool**: `tanh`
**Test ID**: HYP_003

### 12. Complex Multi-Step Problems

#### Test 12.1 - Engineering Problem
**Prompt**: "A circular tank has a radius of 5 meters. Calculate its area and then find the volume if the height is 3 meters. Also convert the volume to gallons."
**Expected MCP Tools**: `power`, `multiply`, `meters_to_feet`, `liters_to_gallons`
**Test ID**: COMPLEX_001

#### Test 12.2 - Financial Analysis
**Prompt**: "I invest $5000 at 4% annual interest compounded quarterly for 10 years. What's the final amount? Then calculate what percentage increase this represents."
**Expected MCP Tools**: `compound_interest`, `subtract`, `divide`, `multiply`
**Test ID**: COMPLEX_002

#### Test 12.3 - Statistical Analysis
**Prompt**: "Given the dataset [23, 45, 67, 34, 56, 78, 12, 89, 45, 56], find the mean, median, mode, and standard deviation. Then determine which values are within one standard deviation of the mean."
**Expected MCP Tools**: `mean`, `median`, `mode`, `standard_deviation`, `subtract`, `absolute`
**Test ID**: COMPLEX_003

#### Test 12.4 - Geometry and Trigonometry
**Prompt**: "In a right triangle, one leg is 3 units and the hypotenuse is 5 units. Find the other leg, then calculate all three angles in degrees."
**Expected MCP Tools**: `power`, `subtract`, `square_root`, `asin`, `acos`, `radians_to_degrees`
**Test ID**: COMPLEX_004

#### Test 12.5 - Matrix Operations Chain
**Prompt**: "Given matrix A = [[2,3],[1,4]] and B = [[1,2],[3,1]], calculate A+B, then find the determinant of the result, and finally check if this determinant is a perfect square."
**Expected MCP Tools**: `matrix_add`, `matrix_determinant`, `is_perfect_square`
**Test ID**: COMPLEX_005

## Test Execution Instructions

1. **Run each test individually** by providing the prompt to an AI agent with access to the SharkMath MCP server
2. **Record the MCP tools used** by the agent for each prompt
3. **Compare results** with the expected outcomes in `mcp_test_expected.md`
4. **Note any discrepancies** between expected and actual tool usage
5. **Validate mathematical accuracy** of all computed results
6. **Test error handling** for edge cases and invalid inputs

## Success Criteria

- **Tool Selection**: Agent selects the expected MCP tool(s) for each prompt
- **Mathematical Accuracy**: All calculations return correct results
- **Error Handling**: Invalid operations return appropriate error messages
- **Multi-Step Problems**: Complex problems are broken down correctly using multiple tools
- **Response Completeness**: Agent provides complete answers with proper explanations

## Usage Notes

- Each test ID can be referenced when documenting results
- Tests are designed to cover all 70+ mathematical functions in the SharkMath server
- Complex tests validate the agent's ability to chain multiple MCP tool calls
- Error handling tests ensure robust operation under edge conditions
