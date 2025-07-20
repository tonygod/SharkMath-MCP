"""
Convert Units - Consolidated Unit Conversion Tool for SharkMath MCP Server
Production implementation with parameter-based routing for 42+ unit conversions.
"""

import math


class ConversionTool:
    """Base conversion tool functionality"""
    @staticmethod  
    def format_result(value: float, from_unit: str, to_unit: str, result: float) -> str:
        return f"✅ {value} {from_unit} = {result} {to_unit}"


def validate_positive(value: float, name: str = "value") -> bool:
    """Validate that a value is positive"""
    return value > 0

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
        - Area: square_meters, square_feet, acres, hectares
        - Speed: mps, kmh, mph, knots
        - Pressure: pascals, atmospheres, psi, bar
        - Data: bytes, kilobytes, megabytes, gigabytes, terabytes, petabytes, bits
        
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
            if from_unit in ["kilograms", "pounds"] and value < 0:
                return f"❌ Weight cannot be negative"
            if from_unit in ["liters", "gallons"] and value < 0:
                return f"❌ Volume cannot be negative"
            if from_unit in ["square_meters", "square_feet", "acres", "hectares"] and value < 0:
                return f"❌ Area cannot be negative"
            if from_unit in ["mps", "kmh", "mph", "knots"] and value < 0:
                return f"❌ Speed cannot be negative"
            if from_unit in ["pascals", "atmospheres", "psi", "bar"] and value < 0:
                return f"❌ Pressure cannot be negative"
            if from_unit in ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes", "petabytes", "bits"] and value < 0:
                return f"❌ Data size cannot be negative"
                
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
                
                # Area conversions
                "square_meters_to_square_feet": lambda x: x * 10.7639,
                "square_feet_to_square_meters": lambda x: x / 10.7639,
                "square_meters_to_hectares": lambda x: x / 10000,
                "hectares_to_square_meters": lambda x: x * 10000,
                "hectares_to_acres": lambda x: x * 2.47105,
                "acres_to_hectares": lambda x: x / 2.47105,
                "square_feet_to_acres": lambda x: x / 43560,
                "acres_to_square_feet": lambda x: x * 43560,
                
                # Speed conversions
                "mps_to_kmh": lambda x: x * 3.6,
                "kmh_to_mps": lambda x: x / 3.6,
                "mps_to_mph": lambda x: x * 2.23694,
                "mph_to_mps": lambda x: x / 2.23694,
                "kmh_to_mph": lambda x: x * 0.621371,
                "mph_to_kmh": lambda x: x / 0.621371,
                "knots_to_mps": lambda x: x * 0.514444,
                "mps_to_knots": lambda x: x / 0.514444,
                "knots_to_mph": lambda x: x * 1.15078,
                "mph_to_knots": lambda x: x / 1.15078,
                "knots_to_kmh": lambda x: x * 1.852,
                "kmh_to_knots": lambda x: x / 1.852,
                
                # Pressure conversions  
                "pascals_to_atmospheres": lambda x: x / 101325,
                "atmospheres_to_pascals": lambda x: x * 101325,
                "pascals_to_psi": lambda x: x / 6895,
                "psi_to_pascals": lambda x: x * 6895,
                "pascals_to_bar": lambda x: x / 100000,
                "bar_to_pascals": lambda x: x * 100000,
                "atmospheres_to_psi": lambda x: x * 14.696,
                "psi_to_atmospheres": lambda x: x / 14.696,
                "atmospheres_to_bar": lambda x: x * 1.01325,
                "bar_to_atmospheres": lambda x: x / 1.01325,
                "psi_to_bar": lambda x: x / 14.504,
                "bar_to_psi": lambda x: x * 14.504,
                
                # Data conversions
                "bits_to_bytes": lambda x: x / 8,
                "bytes_to_bits": lambda x: x * 8,
                "bytes_to_kilobytes": lambda x: x / 1024,
                "kilobytes_to_bytes": lambda x: x * 1024,
                "kilobytes_to_megabytes": lambda x: x / 1024,
                "megabytes_to_kilobytes": lambda x: x * 1024,
                "megabytes_to_gigabytes": lambda x: x / 1024,
                "gigabytes_to_megabytes": lambda x: x * 1024,
                "gigabytes_to_terabytes": lambda x: x / 1024,
                "terabytes_to_gigabytes": lambda x: x * 1024,
                "terabytes_to_petabytes": lambda x: x / 1024,
                "petabytes_to_terabytes": lambda x: x * 1024,
                "bytes_to_megabytes": lambda x: x / (1024 * 1024),
                "megabytes_to_bytes": lambda x: x * (1024 * 1024),
                "bytes_to_gigabytes": lambda x: x / (1024 * 1024 * 1024),
                "gigabytes_to_bytes": lambda x: x * (1024 * 1024 * 1024),
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
    print(f"✅ Supports 80+ unit conversions across 11 categories")
    print("✅ Ready for MCP integration testing")
