"""
Consolidated Tools Test Suite for SharkMath MCP Server
Tests for parameter-based routing tools and consolidated functionality.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import asyncio
from convert_units import register_tools as register_convert_units

class TestConsolidatedTools(unittest.TestCase):
    """Test suite for consolidated SharkMath tools."""
    
    def setUp(self):
        """Set up test fixtures with MockMCP."""
        class MockMCP:
            def __init__(self):
                self.tools = {}
            
            def tool(self):
                def decorator(func):
                    tool_name = func.__name__
                    self.tools[tool_name] = func
                    return func
                return decorator
        
        self.mock_mcp = MockMCP()
        register_convert_units(self.mock_mcp)
        
    async def async_test_helper(self, tool_name, *args, **kwargs):
        """Helper to run async tool functions in tests."""
        if tool_name in self.mock_mcp.tools:
            return await self.mock_mcp.tools[tool_name](*args, **kwargs)
        else:
            raise ValueError(f"Tool {tool_name} not found")
    
    # Energy Conversion Tests
    def test_convert_units_watts_to_kilowatts(self):
        """Test watts to kilowatts conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'watts', 'kilowatts', 1500.0
        ))
        self.assertIn("✅", result)
        self.assertIn("1.5", result)
        
    def test_convert_units_kilowatts_to_watts(self):
        """Test kilowatts to watts conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'kilowatts', 'watts', 2.5
        ))
        self.assertIn("✅", result)
        self.assertIn("2500", result)
        
    def test_convert_units_kilowatts_to_kwh(self):
        """Test kilowatts to kilowatt hours conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'kilowatts', 'kilowatt_hours', 5.0, 3.0
        ))
        self.assertIn("✅", result)
        self.assertIn("15", result)
        self.assertIn("3.0 hours", result)
        
    def test_convert_units_horsepower_to_watts(self):
        """Test horsepower to watts conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'horsepower', 'watts', 10.0
        ))
        self.assertIn("✅", result)
        self.assertIn("7457", result)
        
    def test_convert_units_joules_to_calories(self):
        """Test joules to calories conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'joules', 'calories', 1000.0
        ))
        self.assertIn("✅", result)
        self.assertIn("239", result)  # Approximately 239 calories
        
    # Temperature Conversion Tests  
    def test_convert_units_celsius_to_fahrenheit(self):
        """Test celsius to fahrenheit conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'celsius', 'fahrenheit', 25.0
        ))
        self.assertIn("✅", result)
        self.assertIn("77", result)
        
    def test_convert_units_fahrenheit_to_celsius(self):
        """Test fahrenheit to celsius conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'fahrenheit', 'celsius', 77.0
        ))
        self.assertIn("✅", result)
        self.assertIn("25", result)
        
    # Time Conversion Tests
    def test_convert_units_hours_to_minutes(self):
        """Test hours to minutes conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'hours', 'minutes', 2.5
        ))
        self.assertIn("✅", result)
        self.assertIn("150", result)
        
    def test_convert_units_days_to_weeks(self):
        """Test days to weeks conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'days', 'weeks', 21.0
        ))
        self.assertIn("✅", result)
        self.assertIn("3", result)
        
    def test_convert_units_years_to_days(self):
        """Test years to days conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'years', 'days', 2.0
        ))
        self.assertIn("✅", result)
        self.assertIn("730.5", result)  # 2 * 365.25
        
    def test_convert_units_milliseconds_to_seconds(self):
        """Test milliseconds to seconds conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'milliseconds', 'seconds', 1000.0
        ))
        self.assertIn("✅", result)
        self.assertIn("1", result)
        
    # Length Conversion Tests
    def test_convert_units_meters_to_feet(self):
        """Test meters to feet conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'meters', 'feet', 10.0
        ))
        self.assertIn("✅", result)
        self.assertIn("32.8", result)
        
    def test_convert_units_kilometers_to_miles(self):
        """Test kilometers to miles conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'kilometers', 'miles', 50.0
        ))
        self.assertIn("✅", result)
        self.assertIn("31.0", result)
        
    # Weight and Volume Conversion Tests
    def test_convert_units_pounds_to_kilograms(self):
        """Test pounds to kilograms conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'pounds', 'kilograms', 150.0
        ))
        self.assertIn("✅", result)
        self.assertIn("68", result)
        
    def test_convert_units_gallons_to_liters(self):
        """Test gallons to liters conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'gallons', 'liters', 5.0
        ))
        self.assertIn("✅", result)
        self.assertIn("18.9", result)
        
    # Angle Conversion Tests
    def test_convert_units_degrees_to_radians(self):
        """Test degrees to radians conversion."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'degrees', 'radians', 90.0
        ))
        self.assertIn("✅", result)
        self.assertIn("1.57", result)  # π/2 ≈ 1.5708
        
    # Error Handling Tests
    def test_convert_units_invalid_conversion(self):
        """Test invalid conversion handling."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'invalid_unit', 'another_invalid', 100.0
        ))
        self.assertIn("❌", result)
        self.assertIn("not supported", result)
        
    def test_convert_units_negative_power(self):
        """Test negative power value handling."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'watts', 'kilowatts', -1500.0
        ))
        self.assertIn("❌", result)
        self.assertIn("cannot be negative", result)
        
    def test_convert_units_negative_time(self):
        """Test negative time value handling."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'seconds', 'minutes', -60.0
        ))
        self.assertIn("❌", result)
        self.assertIn("cannot be negative", result)
        
    def test_convert_units_invalid_time_hours(self):
        """Test invalid time_hours parameter."""
        result = asyncio.run(self.async_test_helper(
            'convert_units', 'kilowatts', 'kilowatt_hours', 5.0, -2.0
        ))
        self.assertIn("❌", result)
        self.assertIn("must be positive", result)



class TestParameterValidation(unittest.TestCase):
    """Test parameter validation for consolidated tools."""
    
    def setUp(self):
        """Set up validation test fixtures."""
        from consolidated_tool_template import (
            validate_positive, validate_non_zero, validate_range, validate_angle_unit
        )
        self.validate_positive = validate_positive
        self.validate_non_zero = validate_non_zero
        self.validate_range = validate_range
        self.validate_angle_unit = validate_angle_unit
        
    def test_validate_positive_valid(self):
        """Test positive validation with valid input."""
        try:
            self.validate_positive(5.0)
        except Exception:
            self.fail("validate_positive raised exception with valid input")
            
    def test_validate_positive_invalid(self):
        """Test positive validation with invalid input."""
        with self.assertRaises(ValueError):
            self.validate_positive(-1.0)
            
    def test_validate_non_zero_valid(self):
        """Test non-zero validation with valid input."""
        try:
            self.validate_non_zero(5.0)
            self.validate_non_zero(-5.0)
        except Exception:
            self.fail("validate_non_zero raised exception with valid input")
            
    def test_validate_non_zero_invalid(self):
        """Test non-zero validation with invalid input."""
        with self.assertRaises(ValueError):
            self.validate_non_zero(0.0)
            
    def test_validate_range_valid(self):
        """Test range validation with valid input."""
        try:
            self.validate_range(5.0, 0.0, 10.0)
        except Exception:
            self.fail("validate_range raised exception with valid input")
            
    def test_validate_range_invalid(self):
        """Test range validation with invalid input."""
        with self.assertRaises(ValueError):
            self.validate_range(15.0, 0.0, 10.0)
            
    def test_validate_angle_unit_valid(self):
        """Test angle unit validation with valid input."""
        try:
            self.validate_angle_unit("radians")
            self.validate_angle_unit("degrees")
        except Exception:
            self.fail("validate_angle_unit raised exception with valid input")
            
    def test_validate_angle_unit_invalid(self):
        """Test angle unit validation with invalid input."""
        with self.assertRaises(ValueError):
            self.validate_angle_unit("invalid")

if __name__ == '__main__':
    # Run the test suite
    print("Running Consolidated Tools Test Suite...")
    unittest.main(verbosity=2)
