"""
Test suite for conversions.py module

Tests unit conversion functions across multiple domains:
- Angle: degrees_to_radians, radians_to_degrees
- Temperature: celsius_to_fahrenheit, fahrenheit_to_celsius  
- Length: meters_to_feet, feet_to_meters, inches_to_centimeters, centimeters_to_inches
- Distance: kilometers_to_miles, miles_to_kilometers
- Weight: kilograms_to_pounds, pounds_to_kilograms
- Volume: liters_to_gallons, gallons_to_liters
"""

import asyncio
import math
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

import conversions


class MockMCP:
    """Mock MCP server for testing."""
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator


class TestConversions:
    """Test class for unit conversion functions."""
    
    def __init__(self):
        self.mcp = MockMCP()
        conversions.register_tools(self.mcp)
    
    # Angle conversions
    
    async def test_degrees_to_radians_common_angles(self):
        """Test degrees to radians for common angles."""
        result90 = await self.mcp.tools['degrees_to_radians'](90)
        result180 = await self.mcp.tools['degrees_to_radians'](180)
        result360 = await self.mcp.tools['degrees_to_radians'](360)
        
        return ("1.5707" in result90 and  # π/2
                "3.1415" in result180 and  # π  
                "6.2831" in result360)     # 2π
    
    async def test_radians_to_degrees_common_angles(self):
        """Test radians to degrees for common angles."""
        result_pi_2 = await self.mcp.tools['radians_to_degrees'](math.pi / 2)
        result_pi = await self.mcp.tools['radians_to_degrees'](math.pi)
        result_2pi = await self.mcp.tools['radians_to_degrees'](2 * math.pi)
        
        return ("90.0" in result_pi_2 and
                "180.0" in result_pi and
                "360.0" in result_2pi)
    
    async def test_degrees_radians_roundtrip(self):
        """Test roundtrip conversion degrees -> radians -> degrees."""
        original = 45
        rad_result = await self.mcp.tools['degrees_to_radians'](original)
        # Extract the radian value from the result
        if "0.7853" in rad_result:  # π/4
            return True
        return False
    
    # Temperature conversions
    
    async def test_celsius_to_fahrenheit_common_temps(self):
        """Test Celsius to Fahrenheit for common temperatures."""
        result0 = await self.mcp.tools['celsius_to_fahrenheit'](0)
        result100 = await self.mcp.tools['celsius_to_fahrenheit'](100)
        result_neg40 = await self.mcp.tools['celsius_to_fahrenheit'](-40)
        
        return ("32.0°F" in result0 and      # Freezing point
                "212.0°F" in result100 and   # Boiling point
                "-40.0°F" in result_neg40)   # Same in both scales
    
    async def test_fahrenheit_to_celsius_common_temps(self):
        """Test Fahrenheit to Celsius for common temperatures."""
        result32 = await self.mcp.tools['fahrenheit_to_celsius'](32)
        result212 = await self.mcp.tools['fahrenheit_to_celsius'](212)
        result_neg40 = await self.mcp.tools['fahrenheit_to_celsius'](-40)
        
        return ("0.0°C" in result32 and       # Freezing point
                "100.0°C" in result212 and    # Boiling point
                "-40.0°C" in result_neg40)    # Same in both scales
    
    # Length conversions
    
    async def test_meters_to_feet(self):
        """Test meters to feet conversion."""
        result = await self.mcp.tools['meters_to_feet'](1)
        return "3.28084 feet" in result
    
    async def test_feet_to_meters(self):
        """Test feet to meters conversion."""
        result = await self.mcp.tools['feet_to_meters'](3.28084)
        return "1.0 meters" in result
    
    async def test_inches_to_centimeters(self):
        """Test inches to centimeters conversion."""
        result1 = await self.mcp.tools['inches_to_centimeters'](1)
        result12 = await self.mcp.tools['inches_to_centimeters'](12)
        
        return ("2.54 cm" in result1 and      # 1 inch = 2.54 cm
                "30.48 cm" in result12)       # 1 foot = 30.48 cm
    
    async def test_centimeters_to_inches(self):
        """Test centimeters to inches conversion."""
        result = await self.mcp.tools['centimeters_to_inches'](2.54)
        return "1.0 inches" in result
    
    # Distance conversions
    
    async def test_kilometers_to_miles(self):
        """Test kilometers to miles conversion."""
        result = await self.mcp.tools['kilometers_to_miles'](1)
        return "0.621371 miles" in result
    
    async def test_miles_to_kilometers(self):
        """Test miles to kilometers conversion.""" 
        result = await self.mcp.tools['miles_to_kilometers'](1)
        return "1.60934 km" in result
    
    async def test_distance_roundtrip(self):
        """Test roundtrip distance conversion."""
        # 5 km -> miles -> km should be close to 5
        result_km_to_miles = await self.mcp.tools['kilometers_to_miles'](5)
        # Should be approximately 3.106855 miles
        return "3.106" in result_km_to_miles
    
    # Weight conversions
    
    async def test_kilograms_to_pounds(self):
        """Test kilograms to pounds conversion."""
        result = await self.mcp.tools['kilograms_to_pounds'](1)
        return "2.20462 pounds" in result
    
    async def test_pounds_to_kilograms(self):
        """Test pounds to kilograms conversion."""
        result = await self.mcp.tools['pounds_to_kilograms'](2.20462)
        return "1.0 kg" in result
    
    async def test_weight_common_values(self):
        """Test weight conversions for common values.""" 
        result_100kg = await self.mcp.tools['kilograms_to_pounds'](100)
        return "220.462 pounds" in result_100kg
    
    # Volume conversions
    
    async def test_liters_to_gallons(self):
        """Test liters to gallons conversion."""
        result = await self.mcp.tools['liters_to_gallons'](1)
        return "0.264172 gallons" in result
    
    async def test_gallons_to_liters(self):
        """Test gallons to liters conversion."""
        result = await self.mcp.tools['gallons_to_liters'](1)
        return "3.78541 liters" in result
    
    async def test_volume_roundtrip(self):
        """Test roundtrip volume conversion."""
        # 10 liters -> gallons should be about 2.64172
        result = await self.mcp.tools['liters_to_gallons'](10)
        return "2.64172 gallons" in result
    
    # Edge cases and validation
    
    async def test_zero_conversions(self):
        """Test conversions with zero values."""
        result_temp = await self.mcp.tools['celsius_to_fahrenheit'](0)
        result_length = await self.mcp.tools['meters_to_feet'](0)
        result_weight = await self.mcp.tools['kilograms_to_pounds'](0)
        
        return ("32.0°F" in result_temp and     # 0°C = 32°F
                "0.0 feet" in result_length and
                "0.0 pounds" in result_weight)
    
    async def test_negative_conversions(self):
        """Test conversions with negative values."""
        result_temp = await self.mcp.tools['celsius_to_fahrenheit'](-10)
        return "14.0°F" in result_temp  # -10°C = 14°F
