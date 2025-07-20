# SharkMath Server Enhancement Tasks - Phase 2

## Overview
Building on the complete implementation of 70+ mathematical tools across 12 domains, this enhancement phase focuses on expanding existing modules with additional functionality and improving user experience.

## Current Baseline - All Phases Complete ✅
- **12 Mathematical Domains** implemented and documented
- **70+ Functions** across arithmetic, trigonometry, statistics, conversions, etc.
- **Modular Architecture** with consistent error handling
- **Full VS Code Integration** via MCP protocol

---

## Enhancement Phase 1: Expanded Unit Conversions
**File: `conversions.py`**

### Current Conversions (14 functions) ✅
- Angle: degrees ↔ radians
- Temperature: Celsius ↔ Fahrenheit  
- Length: meters ↔ feet, inches ↔ centimeters, kilometers ↔ miles
- Weight: kilograms ↔ pounds
- Volume: liters ↔ US gallons

### New Energy Conversions
✅ **watts_to_kilowatts(watts)** - Convert watts to kilowatts
✅ **kilowatts_to_watts(kilowatts)** - Convert kilowatts to watts
✅ **kilowatts_to_kilowatt_hours(kilowatts, hours)** - Convert power × time to energy
✅ **kilowatt_hours_to_kilowatts(kwh, hours)** - Convert energy ÷ time to power
✅ **watts_to_horsepower(watts)** - Convert watts to horsepower
✅ **horsepower_to_watts(horsepower)** - Convert horsepower to watts
✅ **joules_to_calories(joules)** - Convert joules to calories
✅ **calories_to_joules(calories)** - Convert calories to joules
✅ **btu_to_joules(btu)** - Convert British Thermal Units to joules
✅ **joules_to_btu(joules)** - Convert joules to British Thermal Units

### New Time Conversions
✅ **seconds_to_minutes(seconds)** - Convert seconds to minutes
✅ **minutes_to_seconds(minutes)** - Convert minutes to seconds
✅ **minutes_to_hours(minutes)** - Convert minutes to hours
✅ **hours_to_minutes(hours)** - Convert hours to minutes
✅ **hours_to_days(hours)** - Convert hours to days
✅ **days_to_hours(days)** - Convert days to hours
✅ **days_to_weeks(days)** - Convert days to weeks
✅ **weeks_to_days(weeks)** - Convert weeks to days
✅ **days_to_months(days)** - Convert days to months (using 30.44 days/month average)
✅ **months_to_days(months)** - Convert months to days (using 30.44 days/month average)
✅ **months_to_years(months)** - Convert months to years
✅ **years_to_months(years)** - Convert years to months
✅ **days_to_years(days)** - Convert days to years (using 365.25 days/year)
✅ **years_to_days(years)** - Convert years to days (using 365.25 days/year)
✅ **seconds_to_hours(seconds)** - Convert seconds directly to hours
✅ **hours_to_seconds(hours)** - Convert hours directly to seconds
✅ **milliseconds_to_seconds(milliseconds)** - Convert milliseconds to seconds
✅ **seconds_to_milliseconds(seconds)** - Convert seconds to milliseconds

### New Area Conversions
🔲 **square_meters_to_square_feet(sq_meters)** - Convert square meters to square feet
🔲 **square_feet_to_square_meters(sq_feet)** - Convert square feet to square meters
🔲 **acres_to_square_meters(acres)** - Convert acres to square meters
🔲 **square_meters_to_acres(sq_meters)** - Convert square meters to acres
🔲 **hectares_to_acres(hectares)** - Convert hectares to acres
🔲 **acres_to_hectares(acres)** - Convert acres to hectares

### New Speed/Velocity Conversions
🔲 **meters_per_second_to_kilometers_per_hour(mps)** - Convert m/s to km/h
🔲 **kilometers_per_hour_to_meters_per_second(kmh)** - Convert km/h to m/s
🔲 **miles_per_hour_to_kilometers_per_hour(mph)** - Convert mph to km/h
🔲 **kilometers_per_hour_to_miles_per_hour(kmh)** - Convert km/h to mph
🔲 **knots_to_kilometers_per_hour(knots)** - Convert nautical knots to km/h
🔲 **kilometers_per_hour_to_knots(kmh)** - Convert km/h to nautical knots

### New Pressure Conversions
🔲 **pascals_to_atmospheres(pascals)** - Convert pascals to atmospheres
🔲 **atmospheres_to_pascals(atmospheres)** - Convert atmospheres to pascals
🔲 **psi_to_pascals(psi)** - Convert pounds per square inch to pascals
🔲 **pascals_to_psi(pascals)** - Convert pascals to pounds per square inch
🔲 **bar_to_psi(bar)** - Convert bar to PSI
🔲 **psi_to_bar(psi)** - Convert PSI to bar

### New Data/Computer Conversions
🔲 **bytes_to_kilobytes(bytes)** - Convert bytes to kilobytes (1024-based)
🔲 **kilobytes_to_bytes(kilobytes)** - Convert kilobytes to bytes
🔲 **kilobytes_to_megabytes(kilobytes)** - Convert KB to MB
🔲 **megabytes_to_kilobytes(megabytes)** - Convert MB to KB
🔲 **megabytes_to_gigabytes(megabytes)** - Convert MB to GB
🔲 **gigabytes_to_megabytes(gigabytes)** - Convert GB to MB
🔲 **gigabytes_to_terabytes(gigabytes)** - Convert GB to TB
🔲 **terabytes_to_gigabytes(terabytes)** - Convert TB to GB
🔲 **terabytes_to_petabytes(terabytes)** - Convert TB to PB
🔲 **petabytes_to_terabytes(petabytes)** - Convert PB to TB
🔲 **bits_to_bytes(bits)** - Convert bits to bytes
🔲 **bytes_to_bits(bytes)** - Convert bytes to bits

### Phase 1 Testing Requirements
**Test Files to Update:**
🔲 **Tests/test_conversions.py** - Add 28 new test functions for energy and time conversions
🔲 **Tests/test_conversions_area.py** - Create new test file for area conversions (6 functions)  
🔲 **Tests/test_conversions_speed.py** - Create new test file for speed conversions (6 functions)
🔲 **Tests/test_conversions_pressure.py** - Create new test file for pressure conversions (6 functions)
🔲 **Tests/test_conversions_data.py** - Create new test file for data/computer conversions (12 functions)

**AI Agent Test Files to Update:**
🔲 **Tests/mcp_tests.md** - Add 52 new test prompts (Energy: 10, Time: 18, Area: 6, Speed: 6, Pressure: 6, Data: 6)
🔲 **Tests/mcp_test_expected.md** - Add 52 corresponding expected results with proper formatting

**Test Categories to Add:**
- **ENERGY_001-010**: Energy conversion tests (watts, kW, kWh, HP, joules, calories, BTU)
- **TIME_001-018**: Time conversion tests (ms to years, all combinations)
- **AREA_001-006**: Area conversion tests (sq meters, sq feet, acres, hectares)
- **SPEED_001-006**: Speed conversion tests (m/s, km/h, mph, knots)  
- **PRESSURE_001-006**: Pressure conversion tests (pascals, atmospheres, PSI, bar)
- **DATA_001-012**: Data conversion tests (bytes to PB, bits to bytes)

**Documentation Updates:**
🔲 **Tests/README.md** - Update test coverage table and add new conversion categories
🔲 **Tests/README.md** - Update total test count from 45 to 97+ tests  
🔲 **Tests/README.md** - Add Phase 1 enhancement testing methodology section

---

## Enhancement Phase 2: Advanced Statistics
**File: `stats_operations.py` (rename from `statistics.py`)**

### Current Statistics (6 functions) ✅
- mean, median, mode, standard_deviation, variance, range_stats

### New Statistical Functions
🔲 **percentile(numbers, percentile)** - Calculate nth percentile of dataset
🔲 **quartiles(numbers)** - Calculate Q1, Q2 (median), Q3, and IQR
🔲 **correlation_coefficient(x_values, y_values)** - Pearson correlation coefficient
🔲 **z_score(value, mean, std_dev)** - Calculate z-score for a value
🔲 **coefficient_of_variation(numbers)** - Calculate CV (std_dev/mean)
🔲 **skewness(numbers)** - Calculate skewness of dataset
🔲 **kurtosis(numbers)** - Calculate kurtosis of dataset
🔲 **moving_average(numbers, window_size)** - Calculate moving average

### Phase 2 Testing Requirements
**Test Files to Update:**
🔲 **Tests/test_statistics.py** - Expand existing file with 8 new advanced statistical tests
🔲 **Tests/test_advanced_statistics.py** - Create dedicated file for advanced statistical functions

**AI Agent Test Files to Update:**  
🔲 **Tests/mcp_tests.md** - Add ADVANCED_STATS_001-008 test prompts
🔲 **Tests/mcp_test_expected.md** - Add corresponding expected results for advanced statistics

**Test Categories to Add:**
- **ADVANCED_STATS_001**: Percentile calculations with various datasets
- **ADVANCED_STATS_002**: Quartile and IQR calculations
- **ADVANCED_STATS_003**: Pearson correlation coefficient tests
- **ADVANCED_STATS_004**: Z-score calculations for outlier detection
- **ADVANCED_STATS_005**: Coefficient of variation tests
- **ADVANCED_STATS_006**: Skewness measurement tests
- **ADVANCED_STATS_007**: Kurtosis calculation tests
- **ADVANCED_STATS_008**: Moving average with different window sizes

---

## Enhancement Phase 3: Financial Mathematics
**File: `financial_calc.py` (new module)**

### Investment & Interest Calculations
🔲 **simple_interest(principal, rate, time)** - Calculate simple interest
🔲 **present_value(future_value, rate, periods)** - Calculate present value
🔲 **future_value(present_value, rate, periods)** - Calculate future value
🔲 **annuity_present_value(payment, rate, periods)** - PV of annuity
🔲 **annuity_future_value(payment, rate, periods)** - FV of annuity
🔲 **loan_payment(principal, rate, periods)** - Calculate loan payment
🔲 **mortgage_payment(loan_amount, annual_rate, years)** - Mortgage payment calculator

### Business & Economics
🔲 **break_even_point(fixed_costs, price_per_unit, variable_cost_per_unit)** - Break-even analysis
🔲 **roi(gain, cost)** - Return on investment calculation  
🔲 **cagr(beginning_value, ending_value, periods)** - Compound annual growth rate
🔲 **depreciation_straight_line(cost, salvage_value, useful_life)** - Straight-line depreciation

### Phase 3 Testing Requirements
**Test Files to Create:**
🔲 **Tests/test_financial_calc.py** - Complete test suite for all 11 financial functions
🔲 **Tests/test_financial_integration.py** - Multi-step financial calculation tests

**AI Agent Test Files to Update:**
🔲 **Tests/mcp_tests.md** - Add FINANCIAL_001-015 test prompts (includes complex scenarios)
🔲 **Tests/mcp_test_expected.md** - Add financial calculation expected results

**Test Categories to Add:**
- **FINANCIAL_001-007**: Investment calculations (simple interest, PV, FV, annuities)
- **FINANCIAL_008-011**: Business calculations (ROI, CAGR, break-even, depreciation)
- **FINANCIAL_012-015**: Complex multi-step financial scenarios

---

## Enhancement Phase 4: Geometry Extensions
**File: `geometry_calc.py` (new module)**

### 2D Geometry (extends current `advanced_calc.py`)
🔲 **circle_area(radius)** - Calculate area of circle
🔲 **circle_circumference(radius)** - Calculate circumference of circle
🔲 **triangle_area(base, height)** - Calculate triangle area
🔲 **triangle_area_heron(a, b, c)** - Triangle area using Heron's formula
🔲 **rectangle_area(length, width)** - Calculate rectangle area
🔲 **rectangle_perimeter(length, width)** - Calculate rectangle perimeter
🔲 **polygon_area(sides, side_length)** - Regular polygon area
🔲 **polygon_perimeter(sides, side_length)** - Regular polygon perimeter

### 3D Geometry
🔲 **sphere_volume(radius)** - Calculate sphere volume
🔲 **sphere_surface_area(radius)** - Calculate sphere surface area
🔲 **cylinder_volume(radius, height)** - Calculate cylinder volume
🔲 **cylinder_surface_area(radius, height)** - Calculate cylinder surface area
🔲 **cone_volume(radius, height)** - Calculate cone volume
🔲 **rectangular_prism_volume(length, width, height)** - Calculate box volume

### Phase 4 Testing Requirements
**Test Files to Create:**
🔲 **Tests/test_geometry_calc.py** - Complete test suite for all 14 geometry functions
🔲 **Tests/test_geometry_2d.py** - Specialized 2D geometry tests
🔲 **Tests/test_geometry_3d.py** - Specialized 3D geometry tests

**AI Agent Test Files to Update:**
🔲 **Tests/mcp_tests.md** - Add GEOMETRY_2D_001-008 and GEOMETRY_3D_001-006 test prompts
🔲 **Tests/mcp_test_expected.md** - Add geometry calculation expected results

**Test Categories to Add:**
- **GEOMETRY_2D_001-008**: 2D shape calculations (circles, triangles, rectangles, polygons)
- **GEOMETRY_3D_001-006**: 3D shape calculations (spheres, cylinders, cones, prisms)

---

## Enhancement Phase 5: Computer Science Functions
**File: `computer_science.py` (new module)**

### Number Base Conversions
🔲 **decimal_to_binary(decimal)** - Convert decimal to binary
🔲 **binary_to_decimal(binary)** - Convert binary to decimal
🔲 **decimal_to_hexadecimal(decimal)** - Convert decimal to hexadecimal
🔲 **hexadecimal_to_decimal(hexadecimal)** - Convert hex to decimal
🔲 **decimal_to_octal(decimal)** - Convert decimal to octal
🔲 **octal_to_decimal(octal)** - Convert octal to decimal

### Algorithm Complexity Helpers
🔲 **big_o_calculator(n, complexity_type)** - Calculate operations for given complexity
🔲 **hash_string(text, algorithm)** - Calculate hash values (educational)
🔲 **binary_search_steps(array_size)** - Calculate max steps in binary search

### Phase 5 Testing Requirements
**Test Files to Create:**
🔲 **Tests/test_computer_science.py** - Complete test suite for all 9 computer science functions
🔲 **Tests/test_number_base_conversions.py** - Specialized base conversion tests
🔲 **Tests/test_algorithm_helpers.py** - Algorithm complexity and helper function tests

**AI Agent Test Files to Update:**
🔲 **Tests/mcp_tests.md** - Add COMPSCI_001-012 test prompts
🔲 **Tests/mcp_test_expected.md** - Add computer science expected results

**Test Categories to Add:**
- **COMPSCI_001-006**: Number base conversions (binary, hex, octal, decimal)
- **COMPSCI_007-009**: Algorithm complexity helpers (Big O, hash, binary search)
- **COMPSCI_010-012**: Complex multi-step computer science problems

---

## Implementation Strategy

### Phase Priority
1. **Enhancement Phase 1** (Expanded Conversions) - Most requested, builds on existing
2. **Enhancement Phase 2** (Advanced Statistics) - High utility for data analysis  
3. **Enhancement Phase 3** (Financial) - New domain, high practical value
4. **Enhancement Phase 4** (Geometry) - Educational value, extends current geometry
5. **Enhancement Phase 5** (Computer Science) - Specialized but valuable for programming

### Development Standards
- **Maintain existing patterns** - Same error handling (✅/❌ prefixes)
- **Input validation** - Appropriate domain checks for each function type
- **Comprehensive testing** - Test all new functions thoroughly
- **Documentation updates** - Update copilot-instructions.md after each phase
- **Backward compatibility** - Existing functions must remain unchanged

### New Module Pattern
```python
# Example: financial_calc.py
def register_tools(mcp):
    """Register all financial calculation functions with the MCP server."""
    
    @mcp.tool()
    async def simple_interest(principal: float, rate: float, time: float) -> str:
        """Calculate simple interest using I = PRT formula."""
        try:
            # Input validation
            if principal < 0:
                return f"❌ Principal must be non-negative"
            if rate < 0:
                return f"❌ Interest rate must be non-negative"  
            if time < 0:
                return f"❌ Time must be non-negative"
                
            # Calculation
            interest = principal * rate * time
            total_amount = principal + interest
            
            return f"✅ Simple Interest: ${interest:.2f} | Total Amount: ${total_amount:.2f}"
            
        except Exception as e:
            return f"❌ Error calculating simple interest: {str(e)}"
```

### Testing Each Phase
- **Unit tests** for each function with valid/invalid inputs
- **Integration tests** with MCP server  
- **VS Code verification** - Test in Copilot chat interface
- **Documentation tests** - Verify all examples work as expected
- **AI agent testing** - Add prompts to `mcp_tests.md` and expected results to `mcp_test_expected.md`
- **Test coverage updates** - Update `Tests/README.md` with new test counts and categories

### Comprehensive Testing Strategy
**Test File Organization:**
- **Individual Module Tests**: `test_[module_name].py` - Unit tests for each enhancement
- **Integration Tests**: `test_[domain]_integration.py` - Multi-function workflow tests
- **AI Agent Tests**: `mcp_tests.md` + `mcp_test_expected.md` - Real-world usage scenarios

**Test Categories by Phase:**
- **Phase 1**: 52 new conversion tests across 5 categories (Energy, Time, Area, Speed, Pressure, Data)
- **Phase 2**: 8 new advanced statistics tests  
- **Phase 3**: 15 new financial mathematics tests
- **Phase 4**: 14 new geometry calculation tests
- **Phase 5**: 12 new computer science tests

**Total Testing Expansion:**
- **Current Tests**: 45 tests across 4 working test files
- **Enhanced Tests**: 146+ tests across 15+ test files
- **AI Agent Tests**: From 60 prompts to 161+ prompts in `mcp_tests.md`
- **Test Coverage**: From 70+ functions to 173+ functions (nearly 150% increase)

---

## Success Metrics
- **Function count target**: 173+ mathematical tools (up from current 70+)
- **Domain coverage**: 17+ mathematical domains (up from current 12)
- **Test coverage**: 146+ unit tests (up from current 45 tests)
- **AI agent test coverage**: 161+ test prompts (up from current 60 prompts)
- **Error rate**: <1% for valid inputs across all functions
- **Performance**: All functions respond within 100ms for typical inputs
- **User experience**: Consistent, clear output formatting across all functions
- **Test automation**: 100% of new functions have corresponding unit tests and AI agent test prompts

## Next Steps
1. **Review and prioritize** - Confirm which enhancement phases to tackle first
2. **Begin with Phase 1** - Start with expanded conversions (energy, time, area, speed)
3. **Implement with testing** - Create both functionality AND comprehensive tests for each function
4. **Update test documentation** - Keep Tests/README.md, mcp_tests.md, and mcp_test_expected.md current
5. **Iterative development** - Complete each phase (including tests) fully before moving to next
6. **Continuous testing** - Test integration after each new function added  
7. **Documentation maintenance** - Keep copilot-instructions.md updated throughout

**Testing-First Development Approach:**
- For each new function, create unit test FIRST
- Add AI agent test prompt to `mcp_tests.md`
- Add expected result to `mcp_test_expected.md`
- Implement function to pass tests
- Update README.md test coverage documentation
- Verify integration with MCP server

This enhancement plan will nearly double the functionality of SharkMath while maintaining the quality and consistency that makes it an excellent MCP learning resource.
