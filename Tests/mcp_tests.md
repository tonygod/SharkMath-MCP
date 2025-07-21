# SharkMath MCP Server - AI Agent Test Prompts

## Overview
This document contains comprehensive mathematical questions designed to test the SharkMath MCP server through AI agent interactions. Each prompt is designed to trigger specific **MCP tools** and validate their functionality in real-world usage scenarios.

## Consolidated Tool Architecture

### **All Available Tools:**
1. **`calculate_arithmetic`** - All arithmetic and power operations (11 operations)
2. **`calculate_trigonometry`** - All trigonometric functions (10 operations)  
3. **`calculate_statistics`** - All statistical operations (7 operations)
4. **`convert_units`** - All unit conversions (80+ conversions)
5. **`calculate_logarithmic`** - Logarithmic and exponential functions (4 operations)
6. **`calculate_hyperbolic`** - Hyperbolic functions (3 operations)
7. **`format_precision`** - Precision and rounding functions (5 operations)
8. **`analyze_numbers`** - Number theory and combinatorics (9 operations)
9. **`solve_equations`** - Equation solvers (4 operations)
10. **`calculate_geometry_2d`** - 2D geometry calculations (8 operations)
11. **`calculate_geometry_3d`** - 3D geometry and vector operations (14 operations)
12. **`manipulate_matrices`** - Matrix operations (4 operations)
13. **`financial_calculations`** - Financial and business calculations (11 operations)
14. **`computer_science_tools`** - Computer science functions (12 operations)
15. **`data_analysis`** - Advanced data analysis functions (10 operations)
16. **`utility_functions`** - Utility functions (5 operations)

## Test Categories

### 1. Arithmetic Operations (calculate_arithmetic tool)

#### Test 1.1 - Simple Addition
**Prompt**: "What is 47 + 293?"
**Expected MCP Tool**: `calculate_arithmetic` with operation='add'
**Test ID**: ARITH_001

#### Test 1.2 - Subtraction with Negative Result
**Prompt**: "Calculate 125 - 347. What's the result?"
**Expected MCP Tool**: `calculate_arithmetic` with operation='subtract'
**Test ID**: ARITH_002

#### Test 1.3 - Multiplication of Decimals
**Prompt**: "I need to multiply 12.5 by 8.4. Can you help?"
**Expected MCP Tool**: `calculate_arithmetic` with operation='multiply'
**Test ID**: ARITH_003

#### Test 1.4 - Division with Remainder
**Prompt**: "Divide 157 by 23. What do you get?"
**Expected MCP Tool**: `calculate_arithmetic` with operation='divide'
**Test ID**: ARITH_004

#### Test 1.5 - Division by Zero (Error Handling)
**Prompt**: "What happens when I divide 50 by 0?"
**Expected MCP Tool**: `calculate_arithmetic` with operation='divide'
**Test ID**: ARITH_005

#### Test 1.6 - Complex Expression
**Prompt**: "Evaluate this expression: (15 + 3) * 4 - 8 / 2"
**Expected MCP Tool**: `calculate_arithmetic` with operation='calculate'
**Test ID**: ARITH_006

### 2. Power and Root Operations (calculate_arithmetic tool)

#### Test 2.1 - Basic Exponentiation
**Prompt**: "What is 3 raised to the power of 7?"
**Expected MCP Tool**: `calculate_arithmetic` with operation='power'
**Test ID**: POWER_001

#### Test 2.2 - Square Calculation
**Prompt**: "I need to find the square of 23."
**Expected MCP Tool**: `calculate_arithmetic` with operation='square'
**Test ID**: POWER_002

#### Test 2.3 - Perfect Square Root
**Prompt**: "What's the square root of 169?"
**Expected MCP Tool**: `calculate_arithmetic` with operation='square_root'
**Test ID**: POWER_003

#### Test 2.4 - Cube Calculation
**Prompt**: "Calculate 12 cubed."
**Expected MCP Tool**: `calculate_arithmetic` with operation='cube'
**Test ID**: POWER_004

#### Test 2.5 - Cube Root
**Prompt**: "Find the cube root of 216."
**Expected MCP Tool**: `calculate_arithmetic` with operation='cube_root'
**Test ID**: POWER_005

#### Test 2.6 - Fourth Root
**Prompt**: "What is the 4th root of 81?"
**Expected MCP Tool**: `calculate_arithmetic` with operation='nth_root'
**Test ID**: POWER_006

### 3. Trigonometric Functions (calculate_trigonometry tool)

#### Test 3.1 - Sine of Common Angle
**Prompt**: "What is the sine of π/2 radians?"
**Expected MCP Tool**: `calculate_trigonometry` with operation='sin'
**Test ID**: TRIG_001

#### Test 3.2 - Cosine in Degrees
**Prompt**: "Calculate the cosine of 60 degrees."
**Expected MCP Tool**: `calculate_trigonometry` with operation='cos' and angle_unit='degrees'
**Test ID**: TRIG_002

#### Test 3.3 - Tangent of Zero
**Prompt**: "What is tan(0)?"
**Expected MCP Tool**: `calculate_trigonometry` with operation='tan'
**Test ID**: TRIG_003

#### Test 3.4 - Inverse Sine
**Prompt**: "Find the arcsine of 0.5."
**Expected MCP Tool**: `calculate_trigonometry` with operation='asin'
**Test ID**: TRIG_004

#### Test 3.5 - Two-Argument Arctangent
**Prompt**: "Calculate atan2(4, 3)."
**Expected MCP Tool**: `calculate_trigonometry` with operation='atan2'
**Test ID**: TRIG_005

### 4. Logarithmic and Exponential Functions (calculate_logarithmic tool)

#### Test 4.1 - Natural Logarithm
**Prompt**: "What is the natural log of e squared?"
**Expected MCP Tool**: `calculate_logarithmic` with operation='natural_log'
**Test ID**: LOG_001

#### Test 4.2 - Base-10 Logarithm
**Prompt**: "Calculate log₁₀(1000)."
**Expected MCP Tool**: `calculate_logarithmic` with operation='log_base_10'
**Test ID**: LOG_002

#### Test 4.3 - Custom Base Logarithm
**Prompt**: "Find log₂(32)."
**Expected MCP Tool**: `calculate_logarithmic` with operation='log_base'
**Test ID**: LOG_003

#### Test 4.4 - Exponential Function
**Prompt**: "Calculate e^3."
**Expected MCP Tool**: `calculate_logarithmic` with operation='exponential'
**Test ID**: LOG_004

### 5. Statistical Operations (calculate_statistics tool)

#### Test 5.1 - Mean of Dataset
**Prompt**: "Find the average of these numbers: 12, 15, 18, 22, 25, 30"
**Expected MCP Tool**: `calculate_statistics` with operation='mean'
**Test ID**: STATS_001

#### Test 5.2 - Median of Odd Dataset
**Prompt**: "What's the median of: 7, 12, 3, 19, 25, 8, 14?"
**Expected MCP Tool**: `calculate_statistics` with operation='median'
**Test ID**: STATS_002

#### Test 5.3 - Mode Identification
**Prompt**: "Find the mode in this dataset: 1, 2, 3, 2, 4, 2, 5, 6, 2"
**Expected MCP Tool**: `calculate_statistics` with operation='mode'
**Test ID**: STATS_003

#### Test 5.4 - Standard Deviation
**Prompt**: "Calculate the standard deviation of: 10, 12, 14, 16, 18"
**Expected MCP Tool**: `calculate_statistics` with operation='standard_deviation'
**Test ID**: STATS_004

#### Test 5.5 - Range and Statistics
**Prompt**: "What are the min, max, and range of: 25, 12, 38, 45, 7, 33?"
**Expected MCP Tool**: `calculate_statistics` with operation='range_stats'
**Test ID**: STATS_005

### 6. Matrix Operations (manipulate_matrices tool)

#### Test 6.1 - Matrix Addition
**Prompt**: "Add these two 2x2 matrices: [[1,2],[3,4]] and [[5,6],[7,8]]"
**Expected MCP Tool**: `manipulate_matrices` with operation='add'
**Test ID**: MATRIX_001

#### Test 6.2 - Matrix Multiplication
**Prompt**: "Multiply matrices A = [[2,1],[3,4]] and B = [[1,0],[2,5]]"
**Expected MCP Tool**: `manipulate_matrices` with operation='multiply'
**Test ID**: MATRIX_002

#### Test 6.3 - Matrix Determinant
**Prompt**: "Find the determinant of [[3,2],[1,4]]"
**Expected MCP Tool**: `manipulate_matrices` with operation='determinant'
**Test ID**: MATRIX_003

#### Test 6.4 - Matrix Transpose
**Prompt**: "Transpose the matrix [[1,2,3],[4,5,6]]"
**Expected MCP Tool**: `manipulate_matrices` with operation='transpose'
**Test ID**: MATRIX_004

### 7. Unit Conversions (convert_units tool)

#### Test 7.1 - Temperature Conversion
**Prompt**: "Convert 25°C to Fahrenheit."
**Expected MCP Tool**: `convert_units` with from_unit='celsius', to_unit='fahrenheit'
**Test ID**: CONV_001

#### Test 7.2 - Distance Conversion
**Prompt**: "How many miles is 50 kilometers?"
**Expected MCP Tool**: `convert_units` with from_unit='kilometers', to_unit='miles'
**Test ID**: CONV_002

#### Test 7.3 - Weight Conversion
**Prompt**: "Convert 150 pounds to kilograms."
**Expected MCP Tool**: `convert_units` with from_unit='pounds', to_unit='kilograms'
**Test ID**: CONV_003

#### Test 7.4 - Volume Conversion
**Prompt**: "How many liters are in 5 gallons?"
**Expected MCP Tool**: `convert_units` with from_unit='gallons', to_unit='liters'
**Test ID**: CONV_004

#### Test 7.5 - Angle Conversion
**Prompt**: "Convert 90 degrees to radians."
**Expected MCP Tool**: `convert_units` with from_unit='degrees', to_unit='radians'
**Test ID**: CONV_005

### 8. Advanced Mathematical Operations

#### Test 8.1 - Quadratic Equation
**Prompt**: "Solve the quadratic equation: x² - 5x + 6 = 0"
**Expected MCP Tool**: `solve_equations` with equation_type='quadratic'
**Test ID**: ADV_001

#### Test 8.2 - Distance Between Points
**Prompt**: "Find the distance between points (3,4) and (7,1)."
**Expected MCP Tool**: `calculate_geometry_2d` with operation='distance'
**Test ID**: ADV_002

#### Test 8.3 - Slope Calculation
**Prompt**: "What's the slope of the line passing through (2,3) and (6,11)?"
**Expected MCP Tool**: `calculate_geometry_2d` with operation='slope'
**Test ID**: ADV_003

#### Test 8.4 - 3D Distance Calculation (Critical User Case)
**Prompt**: "Calculate the distance between the 3D points [10,10,10] and [120,130,140]."
**Expected MCP Tool**: `calculate_geometry_3d` with operation='distance_3d'
**Test ID**: ADV_004

#### Test 8.5 - Compound Interest
**Prompt**: "Calculate compound interest: $1000 principal, 5% annual rate, 3 years, compounded annually."
**Expected MCP Tool**: `financial_calculations` with operation='compound_interest'
**Test ID**: ADV_005

### 9. 3D Geometry and Vector Operations (calculate_geometry_3d tool)

#### Test 9.1 - 3D Distance Between Points
**Prompt**: "Find the distance between 3D points (0,0,0) and (3,4,12)."
**Expected MCP Tool**: `calculate_geometry_3d` with operation='distance_3d'
**Test ID**: GEO3D_001

#### Test 9.2 - 3D Midpoint Calculation
**Prompt**: "What is the midpoint between 3D points (2,4,6) and (8,12,18)?"
**Expected MCP Tool**: `calculate_geometry_3d` with operation='midpoint_3d'
**Test ID**: GEO3D_002

#### Test 9.3 - Vector Magnitude
**Prompt**: "Calculate the magnitude of vector [5,12,13]."
**Expected MCP Tool**: `calculate_geometry_3d` with operation='vector_magnitude'
**Test ID**: GEO3D_003

#### Test 9.4 - Vector Dot Product
**Prompt**: "Find the dot product of vectors [1,2,3] and [4,5,6]."
**Expected MCP Tool**: `calculate_geometry_3d` with operation='vector_dot_product'
**Test ID**: GEO3D_004

#### Test 9.5 - Vector Cross Product
**Prompt**: "Calculate the cross product of unit vectors i=[1,0,0] and j=[0,1,0]."
**Expected MCP Tool**: `calculate_geometry_3d` with operation='vector_cross_product'
**Test ID**: GEO3D_005

#### Test 9.6 - Angle Between Vectors
**Prompt**: "What is the angle between vectors [1,0,0] and [0,1,0] in degrees?"
**Expected MCP Tool**: `calculate_geometry_3d` with operation='vector_angle'
**Test ID**: GEO3D_006

#### Test 9.7 - Sphere Volume
**Prompt**: "Calculate the volume of a sphere with radius 4 units."
**Expected MCP Tool**: `calculate_geometry_3d` with operation='sphere_volume'
**Test ID**: GEO3D_007

#### Test 9.8 - Cylinder Surface Area
**Prompt**: "Find the total surface area of a cylinder with radius 3 and height 8."
**Expected MCP Tool**: `calculate_geometry_3d` with operation='cylinder_surface_area'
**Test ID**: GEO3D_008

#### Test 9.9 - Cone Volume
**Prompt**: "What is the volume of a cone with radius 6 and height 9?"
**Expected MCP Tool**: `calculate_geometry_3d` with operation='cone_volume'
**Test ID**: GEO3D_009

#### Test 9.10 - Rectangular Prism (Box) Surface Area
**Prompt**: "Calculate the surface area of a box with dimensions 5×4×3."
**Expected MCP Tool**: `calculate_geometry_3d` with operation='rectangular_prism_surface_area'
**Test ID**: GEO3D_010

### 10. Combinatorics and Number Theory (analyze_numbers tool)

#### Test 10.1 - Factorial
**Prompt**: "What is 8 factorial?"
**Expected MCP Tool**: `analyze_numbers` with operation='factorial'
**Test ID**: COMB_001

#### Test 10.2 - Permutation
**Prompt**: "How many ways can I arrange 5 items taken 3 at a time?"
**Expected MCP Tool**: `analyze_numbers` with operation='permutation'
**Test ID**: COMB_002

#### Test 10.3 - Combination
**Prompt**: "Calculate C(10,4) - combinations of 10 items taken 4 at a time."
**Expected MCP Tool**: `analyze_numbers` with operation='combination'
**Test ID**: COMB_003

#### Test 10.4 - Fibonacci Number
**Prompt**: "What is the 12th Fibonacci number?"
**Expected MCP Tool**: `analyze_numbers` with operation='fibonacci'
**Test ID**: COMB_004

#### Test 10.5 - Prime Check
**Prompt**: "Is 97 a prime number?"
**Expected MCP Tool**: `analyze_numbers` with operation='is_prime'
**Test ID**: NUM_001

#### Test 10.6 - GCD Calculation
**Prompt**: "Find the greatest common divisor of 48 and 18."
**Expected MCP Tool**: `analyze_numbers` with operation='gcd'
**Test ID**: NUM_002

### 11. Precision and Rounding Operations (format_precision tool)

#### Test 11.1 - Decimal Rounding
**Prompt**: "Round 3.14159 to 3 decimal places."
**Expected MCP Tool**: `format_precision` with operation='round'
**Test ID**: PREC_001

#### Test 11.2 - Floor Function
**Prompt**: "What is the floor of -2.7?"
**Expected MCP Tool**: `format_precision` with operation='floor'
**Test ID**: PREC_002

#### Test 11.3 - Ceiling Function
**Prompt**: "Calculate the ceiling of 4.1."
**Expected MCP Tool**: `format_precision` with operation='ceiling'
**Test ID**: PREC_003

#### Test 11.4 - Absolute Value
**Prompt**: "Find the absolute value of -15.8."
**Expected MCP Tool**: `format_precision` with operation='absolute'
**Test ID**: PREC_004

### 12. Hyperbolic Functions (calculate_hyperbolic tool)

#### Test 12.1 - Hyperbolic Sine
**Prompt**: "Calculate sinh(2)."
**Expected MCP Tool**: `calculate_hyperbolic` with operation='sinh'
**Test ID**: HYP_001

#### Test 12.2 - Hyperbolic Cosine
**Prompt**: "What is cosh(0)?"
**Expected MCP Tool**: `calculate_hyperbolic` with operation='cosh'
**Test ID**: HYP_002

#### Test 12.3 - Hyperbolic Tangent
**Prompt**: "Find tanh(1)."
**Expected MCP Tool**: `calculate_hyperbolic` with operation='tanh'
**Test ID**: HYP_003

### 13. Complex Multi-Step Problems (Multiple Consolidated Tools)

#### Test 13.1 - Engineering Problem
**Prompt**: "A circular tank has a radius of 5 meters. Calculate its area and then find the volume if the height is 3 meters. Also convert the volume to gallons."
**Expected MCP Tools**: `calculate_arithmetic` (power, multiply), `convert_units` (liters_to_gallons)
**Test ID**: COMPLEX_001

#### Test 13.2 - Financial Analysis
**Prompt**: "I invest $5000 at 4% annual interest compounded quarterly for 10 years. What's the final amount? Then calculate what percentage increase this represents."
**Expected MCP Tools**: `financial_calculations`, `calculate_arithmetic` (subtract, divide, multiply)
**Test ID**: COMPLEX_002

#### Test 13.3 - Statistical Analysis
**Prompt**: "Given the dataset [23, 45, 67, 34, 56, 78, 12, 89, 45, 56], find the mean, median, mode, and standard deviation. Then determine which values are within one standard deviation of the mean."
**Expected MCP Tools**: `calculate_statistics` (mean, median, mode, standard_deviation), `calculate_arithmetic` (subtract), `format_precision` (absolute)
**Test ID**: COMPLEX_003

#### Test 13.4 - Geometry and Trigonometry
**Prompt**: "In a right triangle, one leg is 3 units and the hypotenuse is 5 units. Find the other leg, then calculate all three angles in degrees."
**Expected MCP Tools**: `calculate_arithmetic` (power, subtract, square_root), `calculate_trigonometry` (asin, acos), `convert_units` (radians_to_degrees)
**Test ID**: COMPLEX_004

#### Test 13.5 - Matrix Operations Chain
**Prompt**: "Given matrix A = [[2,3],[1,4]] and B = [[1,2],[3,1]], calculate A+B, then find the determinant of the result, and finally check if this determinant is a perfect square."
**Expected MCP Tools**: `manipulate_matrices`, `analyze_numbers`
**Test ID**: COMPLEX_005

#### Test 13.6 - 3D Vector Analysis
**Prompt**: "Given vectors u=[2,3,6] and v=[1,4,2], calculate their dot product, cross product, and the angle between them. Then find the magnitude of the cross product vector."
**Expected MCP Tools**: `calculate_geometry_3d` (vector_dot_product, vector_cross_product, vector_angle, vector_magnitude)
**Test ID**: COMPLEX_006

## Test Execution Instructions

### How to Perform Tests

1. **Act as an AI Agent**: Process each test prompt naturally as an AI agent would when helping a user with a mathematical question
2. **Use Available MCP Tools**: When a prompt requires mathematical calculations, use the appropriate SharkMath MCP tools available to you
3. **Provide Complete Responses**: Give full, helpful responses to each prompt, including explanations and context as appropriate
4. **Record Actual Results**: Document the exact MCP tool calls made and their outputs
5. **Compare Against Expected**: After completing each test, compare your actual results with the expected outcomes in `mcp_test_expected.md`
6. **Document Discrepancies**: Note any differences between expected and actual tool usage, results, or response formats

### Testing Methodology

- **Natural Processing**: Don't force specific tool usage - respond to prompts as you naturally would
- **Tool Selection**: Let the prompt content guide which MCP tools are most appropriate to use
- **Result Validation**: Verify mathematical accuracy and appropriate error handling
- **Response Quality**: Ensure responses are complete, accurate, and user-friendly
- **Communicating Results**: Only provide an extremely brief summary of the results in chat.  Full results should be stored in MCP_TESTS_RESULTS.md

### Example Test Flow

1. **Read Prompt**: "What is 47 + 293?"
2. **Process Naturally**: Recognize this as a simple addition problem
3. **Use MCP Tool**: Call `mcp_sharkmath-mcp_calculate_arithmetic` with operation='add', a=47, b=293
4. **Provide Response**: "47 + 293 = 340"
5. **Record Results**: Document tool used, parameters, output, and final response
6. **Compare Expected**: Check against expected result of 340 and expected tool usage
7. **Note Status**: Mark as PASSED or FAILED with explanation

## Success Criteria

- **Natural Tool Selection**: Agent selects appropriate MCP tools based on prompt content (may differ from "expected" tools if multiple valid approaches exist)
- **Mathematical Accuracy**: All calculations return correct results within acceptable tolerance
- **Error Handling**: Invalid operations return appropriate error messages with ❌ prefix
- **Multi-Step Problems**: Complex problems are broken down logically using appropriate tool combinations
- **Response Completeness**: Agent provides complete, helpful answers with proper explanations
- **User Experience**: Responses feel natural and conversational while being mathematically precise

## Validation Notes

- **Tool Flexibility**: Multiple valid tool paths may exist for some problems - focus on correctness over exact tool matching
- **Response Format**: Responses should be natural and user-friendly, not necessarily matching exact expected formats
- **Mathematical Precision**: Results must be mathematically correct, with appropriate rounding and significant figures
- **Error Robustness**: System should handle edge cases gracefully without crashes

## Usage Notes

- Each test ID can be referenced when documenting results
- Tests are designed to cover all 70+ mathematical functions consolidated into the 15 SharkMath tools
- Complex tests validate the agent's ability to chain multiple MCP tool calls
- Error handling tests ensure robust operation under edge conditions
- All tools use parameter-based routing with operation-specific parameters
