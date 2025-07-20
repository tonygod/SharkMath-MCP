"""
Convert Units - Consolidated Unit Conversion Tool for SharkMath MCP Server
Prototype implementation demonstrating parameter-based routing for 42+ unit conversions.
"""

from consolidated_tool_template import ConversionTool, validate_positive
import math

def register_tools(mcp):
    """Register the consolidated convert_units tool with the MCP server."""
    
    @mcp.tool()
    async def convert_units(from_unit: str, to_unit: str, value: float, time_hours: float = 1.0) -> str:
        """Universal unit converter supporting all unit types.
        
        Supported conversions:
        - Energy: watts, kilowatts, horsepower, joules, calories, btu
        - Temperature: celsius, fahrenheit  
        - Length: meters, feet, inches, centimeters, kilometers, miles
        - Time: seconds, minutes, hours, days, weeks, months, years, milliseconds
        - Weight: kilograms, pounds
        - Volume: liters, gallons
        - Area: square_meters, square_feet, acres, hectares (future)
        - Speed: mps, kmh, mph, knots (future)
        - Pressure: pascals, atmospheres, psi, bar (future)
        - Data: bytes, kilobytes, megabytes, gigabytes, terabytes, petabytes, bits (future)
        
        Args:
            from_unit: Source unit for conversion
            to_unit: Target unit for conversion  
            value: Numeric value to convert
            time_hours: Time duration for energy conversions (default: 1.0)
        """
        
        try:
            # Input validation
            if not isinstance(value, (int, float)):
                return f"❌ Value must be a number, got {type(value).__name__}"
                
            # Energy conversions that may require time validation
            energy_time_conversions = [
                "kilowatts_to_kilowatt_hours", "kilowatt_hours_to_kilowatts"
            ]
            
            conversion_key = f"{from_unit}_to_{to_unit}"
            
            if conversion_key in energy_time_conversions:
                if time_hours <= 0:
                    return f"❌ Time hours must be positive for energy conversions"
                    
            # Unit-specific validation
            if from_unit in ["watts", "kilowatts", "horsepower"] and value < 0:
                return f"❌ Power cannot be negative"
            if from_unit in ["joules", "calories", "btu"] and value < 0:
                return f"❌ Energy cannot be negative"
            if from_unit in ["seconds", "minutes", "hours", "days", "weeks", "months", "years", "milliseconds"] and value < 0:
                return f"❌ Time cannot be negative"
                
            # Conversion mappings with factors and special functions
            conversions = {
                # Energy conversions
                "watts_to_kilowatts": lambda x: x / 1000,
                "kilowatts_to_watts": lambda x: x * 1000,
                "kilowatts_to_kilowatt_hours": lambda x: x * time_hours,
                "kilowatt_hours_to_kilowatts": lambda x: x / time_hours,
                "watts_to_horsepower": lambda x: x / 745.7,
                "horsepower_to_watts": lambda x: x * 745.7,
                "joules_to_calories": lambda x: x / 4.184,
                "calories_to_joules": lambda x: x * 4.184,
                "btu_to_joules": lambda x: x * 1055.06,
                "joules_to_btu": lambda x: x / 1055.06,
                
                # Temperature conversions
                "celsius_to_fahrenheit": lambda x: (x * 9/5) + 32,
                "fahrenheit_to_celsius": lambda x: (x - 32) * 5/9,
                
                # Length conversions
                "meters_to_feet": lambda x: x * 3.28084,
                "feet_to_meters": lambda x: x / 3.28084,
                "inches_to_centimeters": lambda x: x * 2.54,
                "centimeters_to_inches": lambda x: x / 2.54,
                "kilometers_to_miles": lambda x: x * 0.621371,
                "miles_to_kilometers": lambda x: x / 0.621371,
                
                # Time conversions (comprehensive set)
                "seconds_to_minutes": lambda x: x / 60,
                "minutes_to_seconds": lambda x: x * 60,
                "minutes_to_hours": lambda x: x / 60,
                "hours_to_minutes": lambda x: x * 60,
                "hours_to_days": lambda x: x / 24,
                "days_to_hours": lambda x: x * 24,
                "days_to_weeks": lambda x: x / 7,
                "weeks_to_days": lambda x: x * 7,
                "days_to_months": lambda x: x / 30.4375,  # 365.25 / 12
                "months_to_days": lambda x: x * 30.4375,
                "months_to_years": lambda x: x / 12,
                "years_to_months": lambda x: x * 12,
                "days_to_years": lambda x: x / 365.25,
                "years_to_days": lambda x: x * 365.25,
                "seconds_to_hours": lambda x: x / 3600,
                "hours_to_seconds": lambda x: x * 3600,
                "milliseconds_to_seconds": lambda x: x / 1000,
                "seconds_to_milliseconds": lambda x: x * 1000,
                
                # Weight conversions
                "kilograms_to_pounds": lambda x: x * 2.20462,
                "pounds_to_kilograms": lambda x: x / 2.20462,
                
                # Volume conversions
                "liters_to_gallons": lambda x: x * 0.264172,
                "gallons_to_liters": lambda x: x / 0.264172,
                
                # Angle conversions  
                "degrees_to_radians": lambda x: math.radians(x),
                "radians_to_degrees": lambda x: math.degrees(x),
            }
            
            if conversion_key not in conversions:
                supported_conversions = list(conversions.keys())
                return f"❌ Conversion from '{from_unit}' to '{to_unit}' not supported. Available conversions: {len(supported_conversions)} total"
                
            # Perform conversion
            result = conversions[conversion_key](value)
            
            # Format response based on conversion type
            if conversion_key in energy_time_conversions and time_hours != 1.0:
                if conversion_key == "kilowatts_to_kilowatt_hours":
                    return f"✅ {value} kW × {time_hours} hours = {result} kWh"
                else:  # kilowatt_hours_to_kilowatts
                    return f"✅ {value} kWh ÷ {time_hours} hours = {result} kW"
            elif from_unit in ["days", "months"] and to_unit in ["months", "years", "days"]:
                return f"✅ {value} {from_unit} = {result} {to_unit} (avg)"
            else:
                return f"✅ {value} {from_unit} = {result} {to_unit}"
                
        except Exception as e:
            return f"❌ Error in unit conversion: {str(e)}"

# For direct execution testing
if __name__ == "__main__":
    print("Testing Consolidated Unit Conversion Tool:")
    
    # Mock MCP object for testing
    class MockMCP:
        def tool(self):
            def decorator(func):
                return func
            return decorator
    
    mock_mcp = MockMCP()
    register_tools(mock_mcp)
    
    print("✅ convert_units tool registered successfully!")
    print(f"✅ Supports 42+ unit conversions across 7 categories")
    print("✅ Ready for MCP integration testing")
