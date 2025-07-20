"""
Test suite for convert_units.py module - Core conversion functionality

Tests the core unit conversion functions in the consolidated convert_units tool:
- Energy: watts, kilowatts, horsepower, joules, calories, btu
- Temperature: celsius, fahrenheit  
- Length: meters, feet, inches, centimeters, kilometers, miles
- Time: seconds, minutes, hours, days, weeks, months, years, milliseconds
- Weight: kilograms, pounds
- Volume: liters, gallons
- Angle: degrees, radians
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import convert_units


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestConvertUnits:
    """Test class for core unit conversion functions."""
    
    def __init__(self):
        self.mcp = MockMCP()
        convert_units.register_tools(self.mcp)
    
    # Energy conversions
    
    async def test_watts_to_kilowatts(self):
        """Test watts to kilowatts conversion."""
        result = await self.mcp.tools['convert_units']("watts", "kilowatts", 1000)
        return "1" in result and "kilowatts" in result
    
    async def test_kilowatts_to_watts(self):
        """Test kilowatts to watts conversion."""
        result = await self.mcp.tools['convert_units']("kilowatts", "watts", 1)
        return "1000" in result and "watts" in result
    
    async def test_watts_to_horsepower(self):
        """Test watts to horsepower conversion."""
        result = await self.mcp.tools['convert_units']("watts", "horsepower", 745.7)
        return "1" in result and "horsepower" in result
    
    async def test_horsepower_to_watts(self):
        """Test horsepower to watts conversion."""
        result = await self.mcp.tools['convert_units']("horsepower", "watts", 1)
        return "745.7" in result and "watts" in result
    
    async def test_joules_to_calories(self):
        """Test joules to calories conversion."""
        result = await self.mcp.tools['convert_units']("joules", "calories", 4.184)
        return "1" in result and "calories" in result
    
    async def test_calories_to_joules(self):
        """Test calories to joules conversion."""
        result = await self.mcp.tools['convert_units']("calories", "joules", 1)
        return "4.184" in result and "joules" in result
    
    # Temperature conversions
    
    async def test_celsius_to_fahrenheit(self):
        """Test Celsius to Fahrenheit conversion."""
        result = await self.mcp.tools['convert_units']("celsius", "fahrenheit", 0)
        return "32" in result and "fahrenheit" in result
    
    async def test_fahrenheit_to_celsius(self):
        """Test Fahrenheit to Celsius conversion."""
        result = await self.mcp.tools['convert_units']("fahrenheit", "celsius", 32)
        return "0" in result and "celsius" in result
    
    async def test_celsius_to_fahrenheit_100(self):
        """Test Celsius to Fahrenheit for boiling point."""
        result = await self.mcp.tools['convert_units']("celsius", "fahrenheit", 100)
        return "212" in result and "fahrenheit" in result
    
    # Length conversions
    
    async def test_meters_to_feet(self):
        """Test meters to feet conversion."""
        result = await self.mcp.tools['convert_units']("meters", "feet", 1)
        return "3.28084" in result and "feet" in result
    
    async def test_feet_to_meters(self):
        """Test feet to meters conversion."""
        result = await self.mcp.tools['convert_units']("feet", "meters", 3.28084)
        return "1" in result and "meters" in result
    
    async def test_inches_to_centimeters(self):
        """Test inches to centimeters conversion."""
        result = await self.mcp.tools['convert_units']("inches", "centimeters", 1)
        return "2.54" in result and "centimeters" in result
    
    async def test_centimeters_to_inches(self):
        """Test centimeters to inches conversion."""
        result = await self.mcp.tools['convert_units']("centimeters", "inches", 2.54)
        return "1" in result and "inches" in result
    
    async def test_kilometers_to_miles(self):
        """Test kilometers to miles conversion."""
        result = await self.mcp.tools['convert_units']("kilometers", "miles", 1)
        return "0.621371" in result and "miles" in result
    
    async def test_miles_to_kilometers(self):
        """Test miles to kilometers conversion."""
        result = await self.mcp.tools['convert_units']("miles", "kilometers", 1)
        return "1.609" in result and "kilometers" in result
    
    # Time conversions
    
    async def test_seconds_to_minutes(self):
        """Test seconds to minutes conversion."""
        result = await self.mcp.tools['convert_units']("seconds", "minutes", 60)
        return "1" in result and "minutes" in result
    
    async def test_minutes_to_seconds(self):
        """Test minutes to seconds conversion."""
        result = await self.mcp.tools['convert_units']("minutes", "seconds", 1)
        return "60" in result and "seconds" in result
    
    async def test_hours_to_minutes(self):
        """Test hours to minutes conversion."""
        result = await self.mcp.tools['convert_units']("hours", "minutes", 1)
        return "60" in result and "minutes" in result
    
    async def test_minutes_to_hours(self):
        """Test minutes to hours conversion."""
        result = await self.mcp.tools['convert_units']("minutes", "hours", 60)
        return "1" in result and "hours" in result
    
    async def test_days_to_hours(self):
        """Test days to hours conversion."""
        result = await self.mcp.tools['convert_units']("days", "hours", 1)
        return "24" in result and "hours" in result
    
    async def test_hours_to_days(self):
        """Test hours to days conversion."""
        result = await self.mcp.tools['convert_units']("hours", "days", 24)
        return "1" in result and "days" in result
    
    async def test_weeks_to_days(self):
        """Test weeks to days conversion."""
        result = await self.mcp.tools['convert_units']("weeks", "days", 1)
        return "7" in result and "days" in result
    
    async def test_days_to_weeks(self):
        """Test days to weeks conversion."""
        result = await self.mcp.tools['convert_units']("days", "weeks", 7)
        return "1" in result and "weeks" in result
    
    # Weight conversions
    
    async def test_kilograms_to_pounds(self):
        """Test kilograms to pounds conversion."""
        result = await self.mcp.tools['convert_units']("kilograms", "pounds", 1)
        return "2.20462" in result and "pounds" in result
    
    async def test_pounds_to_kilograms(self):
        """Test pounds to kilograms conversion."""
        result = await self.mcp.tools['convert_units']("pounds", "kilograms", 2.20462)
        return "1" in result and "kilograms" in result
    
    # Volume conversions
    
    async def test_liters_to_gallons(self):
        """Test liters to gallons conversion."""
        result = await self.mcp.tools['convert_units']("liters", "gallons", 1)
        return "0.264172" in result and "gallons" in result
    
    async def test_gallons_to_liters(self):
        """Test gallons to liters conversion."""
        result = await self.mcp.tools['convert_units']("gallons", "liters", 1)
        return "3.785" in result and "liters" in result
    
    # Angle conversions
    
    async def test_degrees_to_radians(self):
        """Test degrees to radians conversion."""
        result = await self.mcp.tools['convert_units']("degrees", "radians", 180)
        return "3.141" in result and "radians" in result
    
    async def test_radians_to_degrees(self):
        """Test radians to degrees conversion."""
        result = await self.mcp.tools['convert_units']("radians", "degrees", 3.14159)
        return "180" in result and "degrees" in result
    
    # Energy time conversions  
    
    async def test_kilowatts_to_kilowatt_hours(self):
        """Test kilowatts to kilowatt hours conversion."""
        result = await self.mcp.tools['convert_units']("kilowatts", "kilowatt_hours", 2, time_hours=3)
        return "2 kW × 3 hours = 6" in result and "kWh" in result
    
    async def test_kilowatt_hours_to_kilowatts(self):
        """Test kilowatt hours to kilowatts conversion."""
        result = await self.mcp.tools['convert_units']("kilowatt_hours", "kilowatts", 6, time_hours=3)
        return "6 kWh ÷ 3 hours = 2" in result and "kW" in result
    
    # Validation tests
    
    async def test_negative_power_validation(self):
        """Test validation for negative power values."""
        result = await self.mcp.tools['convert_units']("watts", "kilowatts", -100)
        return "❌ Power cannot be negative" in result
    
    async def test_negative_energy_validation(self):
        """Test validation for negative energy values."""
        result = await self.mcp.tools['convert_units']("joules", "calories", -50)
        return "❌ Energy cannot be negative" in result
    
    async def test_negative_time_validation(self):
        """Test validation for negative time values."""
        result = await self.mcp.tools['convert_units']("seconds", "minutes", -30)
        return "❌ Time cannot be negative" in result
    
    async def test_zero_time_hours_validation(self):
        """Test validation for zero time hours in energy conversions."""
        result = await self.mcp.tools['convert_units']("kilowatts", "kilowatt_hours", 5, time_hours=0)
        return "❌ Time hours must be positive for energy conversions" in result
    
    async def test_unsupported_conversion_error(self):
        """Test error handling for unsupported conversions."""
        result = await self.mcp.tools['convert_units']("unknown_unit", "another_unknown", 10)
        return "❌ Conversion from 'unknown_unit' to 'another_unknown' not supported" in result


async def run_core_conversion_tests():
    """Run all core conversion tests."""
    tester = TestConvertUnits()
    
    test_methods = [method for method in dir(tester) if method.startswith('test_')]
    passed = 0
    failed = 0
    
    print("🧪 Running Core Conversion Tests...")
    print("=" * 60)
    
    for test_method in test_methods:
        try:
            test_func = getattr(tester, test_method)
            result = await test_func()
            if result:
                print(f"✅ {test_method}")
                passed += 1
            else:
                print(f"❌ {test_method}")
                failed += 1
        except Exception as e:
            print(f"💥 {test_method}: {str(e)}")
            failed += 1
    
    print("=" * 60)
    print(f"📊 Core Conversion Test Results:")
    print(f"   ✅ Passed: {passed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📈 Success Rate: {(passed/(passed+failed)*100):.1f}%")
    
    return passed, failed


if __name__ == "__main__":
    print("Testing Core Convert Units Tool:")
    asyncio.run(run_core_conversion_tests())
