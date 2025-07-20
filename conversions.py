"""
Unit Conversions Module for SharkMath Server
Handles conversions between different units including angles, temperature, energy, and time.
Enhanced with energy (watts, kilowatts, kilowatt hours, horsepower, joules, calories, BTU)
and comprehensive time conversions (milliseconds to years).
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
    
    # Energy Conversions
    @mcp.tool()
    async def watts_to_kilowatts(watts: float) -> str:
        """Convert watts to kilowatts."""
        try:
            if watts < 0:
                return f"❌ Power cannot be negative"
            kilowatts = watts / 1000
            return f"✅ {watts} W = {kilowatts} kW"
            
        except Exception as e:
            return f"❌ Error converting watts to kilowatts: {str(e)}"
    
    @mcp.tool()
    async def kilowatts_to_watts(kilowatts: float) -> str:
        """Convert kilowatts to watts."""
        try:
            if kilowatts < 0:
                return f"❌ Power cannot be negative"
            watts = kilowatts * 1000
            return f"✅ {kilowatts} kW = {watts} W"
            
        except Exception as e:
            return f"❌ Error converting kilowatts to watts: {str(e)}"
    
    @mcp.tool()
    async def kilowatts_to_kilowatt_hours(kilowatts: float, hours: float) -> str:
        """Convert power × time to energy (kilowatts × hours = kilowatt hours)."""
        try:
            if kilowatts < 0:
                return f"❌ Power cannot be negative"
            if hours < 0:
                return f"❌ Time cannot be negative"
            kwh = kilowatts * hours
            return f"✅ {kilowatts} kW × {hours} hours = {kwh} kWh"
            
        except Exception as e:
            return f"❌ Error calculating kilowatt hours: {str(e)}"
    
    @mcp.tool()
    async def kilowatt_hours_to_kilowatts(kwh: float, hours: float) -> str:
        """Convert energy ÷ time to power (kilowatt hours ÷ hours = kilowatts)."""
        try:
            if kwh < 0:
                return f"❌ Energy cannot be negative"
            if hours <= 0:
                return f"❌ Time must be positive for power calculation"
            kilowatts = kwh / hours
            return f"✅ {kwh} kWh ÷ {hours} hours = {kilowatts} kW"
            
        except Exception as e:
            return f"❌ Error calculating kilowatts from energy: {str(e)}"
    
    @mcp.tool()
    async def watts_to_horsepower(watts: float) -> str:
        """Convert watts to horsepower."""
        try:
            if watts < 0:
                return f"❌ Power cannot be negative"
            # 1 horsepower = 745.7 watts
            horsepower = watts / 745.7
            return f"✅ {watts} W = {horsepower} HP"
            
        except Exception as e:
            return f"❌ Error converting watts to horsepower: {str(e)}"
    
    @mcp.tool()
    async def horsepower_to_watts(horsepower: float) -> str:
        """Convert horsepower to watts."""
        try:
            if horsepower < 0:
                return f"❌ Power cannot be negative"
            # 1 horsepower = 745.7 watts
            watts = horsepower * 745.7
            return f"✅ {horsepower} HP = {watts} W"
            
        except Exception as e:
            return f"❌ Error converting horsepower to watts: {str(e)}"
    
    @mcp.tool()
    async def joules_to_calories(joules: float) -> str:
        """Convert joules to calories."""
        try:
            if joules < 0:
                return f"❌ Energy cannot be negative"
            # 1 calorie = 4.184 joules
            calories = joules / 4.184
            return f"✅ {joules} J = {calories} cal"
            
        except Exception as e:
            return f"❌ Error converting joules to calories: {str(e)}"
    
    @mcp.tool()
    async def calories_to_joules(calories: float) -> str:
        """Convert calories to joules."""
        try:
            if calories < 0:
                return f"❌ Energy cannot be negative"
            # 1 calorie = 4.184 joules
            joules = calories * 4.184
            return f"✅ {calories} cal = {joules} J"
            
        except Exception as e:
            return f"❌ Error converting calories to joules: {str(e)}"
    
    @mcp.tool()
    async def btu_to_joules(btu: float) -> str:
        """Convert British Thermal Units to joules."""
        try:
            if btu < 0:
                return f"❌ Energy cannot be negative"
            # 1 BTU = 1055.06 joules
            joules = btu * 1055.06
            return f"✅ {btu} BTU = {joules} J"
            
        except Exception as e:
            return f"❌ Error converting BTU to joules: {str(e)}"
    
    @mcp.tool()
    async def joules_to_btu(joules: float) -> str:
        """Convert joules to British Thermal Units."""
        try:
            if joules < 0:
                return f"❌ Energy cannot be negative"
            # 1 BTU = 1055.06 joules
            btu = joules / 1055.06
            return f"✅ {joules} J = {btu} BTU"
            
        except Exception as e:
            return f"❌ Error converting joules to BTU: {str(e)}"
    
    # Time Conversions
    @mcp.tool()
    async def seconds_to_minutes(seconds: float) -> str:
        """Convert seconds to minutes."""
        try:
            if seconds < 0:
                return f"❌ Time cannot be negative"
            minutes = seconds / 60
            return f"✅ {seconds} seconds = {minutes} minutes"
            
        except Exception as e:
            return f"❌ Error converting seconds to minutes: {str(e)}"
    
    @mcp.tool()
    async def minutes_to_seconds(minutes: float) -> str:
        """Convert minutes to seconds."""
        try:
            if minutes < 0:
                return f"❌ Time cannot be negative"
            seconds = minutes * 60
            return f"✅ {minutes} minutes = {seconds} seconds"
            
        except Exception as e:
            return f"❌ Error converting minutes to seconds: {str(e)}"
    
    @mcp.tool()
    async def minutes_to_hours(minutes: float) -> str:
        """Convert minutes to hours."""
        try:
            if minutes < 0:
                return f"❌ Time cannot be negative"
            hours = minutes / 60
            return f"✅ {minutes} minutes = {hours} hours"
            
        except Exception as e:
            return f"❌ Error converting minutes to hours: {str(e)}"
    
    @mcp.tool()
    async def hours_to_minutes(hours: float) -> str:
        """Convert hours to minutes."""
        try:
            if hours < 0:
                return f"❌ Time cannot be negative"
            minutes = hours * 60
            return f"✅ {hours} hours = {minutes} minutes"
            
        except Exception as e:
            return f"❌ Error converting hours to minutes: {str(e)}"
    
    @mcp.tool()
    async def hours_to_days(hours: float) -> str:
        """Convert hours to days."""
        try:
            if hours < 0:
                return f"❌ Time cannot be negative"
            days = hours / 24
            return f"✅ {hours} hours = {days} days"
            
        except Exception as e:
            return f"❌ Error converting hours to days: {str(e)}"
    
    @mcp.tool()
    async def days_to_hours(days: float) -> str:
        """Convert days to hours."""
        try:
            if days < 0:
                return f"❌ Time cannot be negative"
            hours = days * 24
            return f"✅ {days} days = {hours} hours"
            
        except Exception as e:
            return f"❌ Error converting days to hours: {str(e)}"
    
    @mcp.tool()
    async def days_to_weeks(days: float) -> str:
        """Convert days to weeks."""
        try:
            if days < 0:
                return f"❌ Time cannot be negative"
            weeks = days / 7
            return f"✅ {days} days = {weeks} weeks"
            
        except Exception as e:
            return f"❌ Error converting days to weeks: {str(e)}"
    
    @mcp.tool()
    async def weeks_to_days(weeks: float) -> str:
        """Convert weeks to days."""
        try:
            if weeks < 0:
                return f"❌ Time cannot be negative"
            days = weeks * 7
            return f"✅ {weeks} weeks = {days} days"
            
        except Exception as e:
            return f"❌ Error converting weeks to days: {str(e)}"
    
    @mcp.tool()
    async def days_to_months(days: float) -> str:
        """Convert days to months (using 30.44 days/month average)."""
        try:
            if days < 0:
                return f"❌ Time cannot be negative"
            # Using 365.25 / 12 = 30.4375 days per month average
            months = days / 30.4375
            return f"✅ {days} days = {months} months (avg)"
            
        except Exception as e:
            return f"❌ Error converting days to months: {str(e)}"
    
    @mcp.tool()
    async def months_to_days(months: float) -> str:
        """Convert months to days (using 30.44 days/month average)."""
        try:
            if months < 0:
                return f"❌ Time cannot be negative"
            # Using 365.25 / 12 = 30.4375 days per month average
            days = months * 30.4375
            return f"✅ {months} months = {days} days (avg)"
            
        except Exception as e:
            return f"❌ Error converting months to days: {str(e)}"
    
    @mcp.tool()
    async def months_to_years(months: float) -> str:
        """Convert months to years."""
        try:
            if months < 0:
                return f"❌ Time cannot be negative"
            years = months / 12
            return f"✅ {months} months = {years} years"
            
        except Exception as e:
            return f"❌ Error converting months to years: {str(e)}"
    
    @mcp.tool()
    async def years_to_months(years: float) -> str:
        """Convert years to months."""
        try:
            if years < 0:
                return f"❌ Time cannot be negative"
            months = years * 12
            return f"✅ {years} years = {months} months"
            
        except Exception as e:
            return f"❌ Error converting years to months: {str(e)}"
    
    @mcp.tool()
    async def days_to_years(days: float) -> str:
        """Convert days to years (using 365.25 days/year)."""
        try:
            if days < 0:
                return f"❌ Time cannot be negative"
            # Using 365.25 days per year (accounts for leap years)
            years = days / 365.25
            return f"✅ {days} days = {years} years"
            
        except Exception as e:
            return f"❌ Error converting days to years: {str(e)}"
    
    @mcp.tool()
    async def years_to_days(years: float) -> str:
        """Convert years to days (using 365.25 days/year)."""
        try:
            if years < 0:
                return f"❌ Time cannot be negative"
            # Using 365.25 days per year (accounts for leap years)
            days = years * 365.25
            return f"✅ {years} years = {days} days"
            
        except Exception as e:
            return f"❌ Error converting years to days: {str(e)}"
    
    @mcp.tool()
    async def seconds_to_hours(seconds: float) -> str:
        """Convert seconds directly to hours."""
        try:
            if seconds < 0:
                return f"❌ Time cannot be negative"
            hours = seconds / 3600
            return f"✅ {seconds} seconds = {hours} hours"
            
        except Exception as e:
            return f"❌ Error converting seconds to hours: {str(e)}"
    
    @mcp.tool()
    async def hours_to_seconds(hours: float) -> str:
        """Convert hours directly to seconds."""
        try:
            if hours < 0:
                return f"❌ Time cannot be negative"
            seconds = hours * 3600
            return f"✅ {hours} hours = {seconds} seconds"
            
        except Exception as e:
            return f"❌ Error converting hours to seconds: {str(e)}"
    
    @mcp.tool()
    async def milliseconds_to_seconds(milliseconds: float) -> str:
        """Convert milliseconds to seconds."""
        try:
            if milliseconds < 0:
                return f"❌ Time cannot be negative"
            seconds = milliseconds / 1000
            return f"✅ {milliseconds} ms = {seconds} seconds"
            
        except Exception as e:
            return f"❌ Error converting milliseconds to seconds: {str(e)}"
    
    @mcp.tool()
    async def seconds_to_milliseconds(seconds: float) -> str:
        """Convert seconds to milliseconds."""
        try:
            if seconds < 0:
                return f"❌ Time cannot be negative"
            milliseconds = seconds * 1000
            return f"✅ {seconds} seconds = {milliseconds} ms"
            
        except Exception as e:
            return f"❌ Error converting seconds to milliseconds: {str(e)}"

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
