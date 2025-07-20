"""
Unit Conversions Module for SharkMath Server
Handles conversions between different units including angles and temperature.
"""

import math

def register_tools(mcp):
    """Register all unit conversion functions with the MCP server."""
    
    @mcp.tool()
    async def degrees_to_radians(degrees: float) -> str:
        """Convert degrees to radians."""
        try:
            radians = math.radians(degrees)
            return f"✅ {degrees}° = {radians} radians"
            
        except Exception as e:
            return f"❌ Error converting degrees to radians: {str(e)}"
    
    @mcp.tool()
    async def radians_to_degrees(radians: float) -> str:
        """Convert radians to degrees."""
        try:
            degrees = math.degrees(radians)
            return f"✅ {radians} radians = {degrees}°"
            
        except Exception as e:
            return f"❌ Error converting radians to degrees: {str(e)}"
    
    @mcp.tool()
    async def celsius_to_fahrenheit(celsius: float) -> str:
        """Convert temperature from Celsius to Fahrenheit."""
        try:
            fahrenheit = (celsius * 9/5) + 32
            return f"✅ {celsius}°C = {fahrenheit}°F"
            
        except Exception as e:
            return f"❌ Error converting Celsius to Fahrenheit: {str(e)}"
    
    @mcp.tool()
    async def fahrenheit_to_celsius(fahrenheit: float) -> str:
        """Convert temperature from Fahrenheit to Celsius."""
        try:
            celsius = (fahrenheit - 32) * 5/9
            return f"✅ {fahrenheit}°F = {celsius}°C"
            
        except Exception as e:
            return f"❌ Error converting Fahrenheit to Celsius: {str(e)}"
    
    # Length Conversions
    @mcp.tool()
    async def meters_to_feet(meters: float) -> str:
        """Convert length from meters to feet."""
        try:
            feet = meters * 3.28084
            return f"✅ {meters} meters = {feet} feet"
            
        except Exception as e:
            return f"❌ Error converting meters to feet: {str(e)}"
    
    @mcp.tool()
    async def feet_to_meters(feet: float) -> str:
        """Convert length from feet to meters."""
        try:
            meters = feet / 3.28084
            return f"✅ {feet} feet = {meters} meters"
            
        except Exception as e:
            return f"❌ Error converting feet to meters: {str(e)}"
    
    @mcp.tool()
    async def inches_to_centimeters(inches: float) -> str:
        """Convert length from inches to centimeters."""
        try:
            centimeters = inches * 2.54
            return f"✅ {inches} inches = {centimeters} cm"
            
        except Exception as e:
            return f"❌ Error converting inches to centimeters: {str(e)}"
    
    @mcp.tool()
    async def centimeters_to_inches(centimeters: float) -> str:
        """Convert length from centimeters to inches."""
        try:
            inches = centimeters / 2.54
            return f"✅ {centimeters} cm = {inches} inches"
            
        except Exception as e:
            return f"❌ Error converting centimeters to inches: {str(e)}"
    
    @mcp.tool()
    async def kilometers_to_miles(kilometers: float) -> str:
        """Convert distance from kilometers to miles."""
        try:
            miles = kilometers * 0.621371
            return f"✅ {kilometers} km = {miles} miles"
            
        except Exception as e:
            return f"❌ Error converting kilometers to miles: {str(e)}"
    
    @mcp.tool()
    async def miles_to_kilometers(miles: float) -> str:
        """Convert distance from miles to kilometers."""
        try:
            kilometers = miles / 0.621371
            return f"✅ {miles} miles = {kilometers} km"
            
        except Exception as e:
            return f"❌ Error converting miles to kilometers: {str(e)}"
    
    # Weight Conversions
    @mcp.tool()
    async def kilograms_to_pounds(kilograms: float) -> str:
        """Convert weight from kilograms to pounds."""
        try:
            pounds = kilograms * 2.20462
            return f"✅ {kilograms} kg = {pounds} lbs"
            
        except Exception as e:
            return f"❌ Error converting kilograms to pounds: {str(e)}"
    
    @mcp.tool()
    async def pounds_to_kilograms(pounds: float) -> str:
        """Convert weight from pounds to kilograms."""
        try:
            kilograms = pounds / 2.20462
            return f"✅ {pounds} lbs = {kilograms} kg"
            
        except Exception as e:
            return f"❌ Error converting pounds to kilograms: {str(e)}"
    
    # Volume Conversions
    @mcp.tool()
    async def liters_to_gallons(liters: float) -> str:
        """Convert volume from liters to US gallons."""
        try:
            gallons = liters * 0.264172
            return f"✅ {liters} liters = {gallons} US gallons"
            
        except Exception as e:
            return f"❌ Error converting liters to gallons: {str(e)}"
    
    @mcp.tool()
    async def gallons_to_liters(gallons: float) -> str:
        """Convert volume from US gallons to liters."""
        try:
            liters = gallons / 0.264172
            return f"✅ {gallons} US gallons = {liters} liters"
            
        except Exception as e:
            return f"❌ Error converting gallons to liters: {str(e)}"

# For direct execution testing
if __name__ == "__main__":
    # Test the conversion functions directly
    print("Testing Unit Conversion Functions:")
    
    # Mock MCP object for testing
    class MockMCP:
        def tool(self):
            def decorator(func):
                return func
            return decorator
    
    mock_mcp = MockMCP()
    register_tools(mock_mcp)
    
    # Test cases would go here for development/debugging
    print("Unit conversions module loaded successfully!")
