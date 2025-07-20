"""
Statistical functions module for SharkMath MCP server.
Contains mean, median, mode, standard deviation, variance, and range statistics.
"""
import statistics as stats_lib
from typing import List

def register_tools(mcp):
    """Register all statistical tools with the MCP server."""
    
    @mcp.tool()
    async def mean(numbers: str) -> str:
        """Calculate the arithmetic mean of a list of numbers. Input as comma-separated values."""
        try:
            # Parse comma-separated numbers
            num_list = [float(x.strip()) for x in numbers.split(',')]
            
            if not num_list:
                return "❌ Error: No numbers provided!"
            
            result = stats_lib.mean(num_list)
            return f"✅ Mean of {num_list} = {result}"
        except ValueError:
            return "❌ Error: Invalid number format! Please provide comma-separated numbers."
        except Exception as e:
            return f"❌ Error calculating mean: {str(e)}"

    @mcp.tool()
    async def median(numbers: str) -> str:
        """Calculate the median of a list of numbers. Input as comma-separated values."""
        try:
            # Parse comma-separated numbers
            num_list = [float(x.strip()) for x in numbers.split(',')]
            
            if not num_list:
                return "❌ Error: No numbers provided!"
            
            result = stats_lib.median(num_list)
            return f"✅ Median of {num_list} = {result}"
        except ValueError:
            return "❌ Error: Invalid number format! Please provide comma-separated numbers."
        except Exception as e:
            return f"❌ Error calculating median: {str(e)}"

    @mcp.tool()
    async def mode(numbers: str) -> str:
        """Calculate the mode (most frequent value) of a list of numbers. Input as comma-separated values."""
        try:
            # Parse comma-separated numbers
            num_list = [float(x.strip()) for x in numbers.split(',')]
            
            if not num_list:
                return "❌ Error: No numbers provided!"
            
            result = stats_lib.mode(num_list)
            return f"✅ Mode of {num_list} = {result}"
        except ValueError:
            return "❌ Error: Invalid number format! Please provide comma-separated numbers."
        except stats_lib.StatisticsError:
            return "❌ Error: No unique mode found! All values appear equally often."
        except Exception as e:
            return f"❌ Error calculating mode: {str(e)}"

    @mcp.tool()
    async def standard_deviation(numbers: str) -> str:
        """Calculate the standard deviation of a list of numbers. Input as comma-separated values."""
        try:
            # Parse comma-separated numbers
            num_list = [float(x.strip()) for x in numbers.split(',')]
            
            if len(num_list) < 2:
                return "❌ Error: Need at least 2 numbers to calculate standard deviation!"
            
            result = stats_lib.stdev(num_list)
            return f"✅ Standard deviation of {num_list} = {result}"
        except ValueError:
            return "❌ Error: Invalid number format! Please provide comma-separated numbers."
        except Exception as e:
            return f"❌ Error calculating standard deviation: {str(e)}"

    @mcp.tool()
    async def variance(numbers: str) -> str:
        """Calculate the variance of a list of numbers. Input as comma-separated values."""
        try:
            # Parse comma-separated numbers
            num_list = [float(x.strip()) for x in numbers.split(',')]
            
            if len(num_list) < 2:
                return "❌ Error: Need at least 2 numbers to calculate variance!"
            
            result = stats_lib.variance(num_list)
            return f"✅ Variance of {num_list} = {result}"
        except ValueError:
            return "❌ Error: Invalid number format! Please provide comma-separated numbers."
        except Exception as e:
            return f"❌ Error calculating variance: {str(e)}"

    @mcp.tool()
    async def range_stats(numbers: str) -> str:
        """Calculate min, max, and range of a list of numbers. Input as comma-separated values."""
        try:
            # Parse comma-separated numbers
            num_list = [float(x.strip()) for x in numbers.split(',')]
            
            if not num_list:
                return "❌ Error: No numbers provided!"
            
            min_val = min(num_list)
            max_val = max(num_list)
            range_val = max_val - min_val
            
            return f"✅ Range stats of {num_list}: Min = {min_val}, Max = {max_val}, Range = {range_val}"
        except ValueError:
            return "❌ Error: Invalid number format! Please provide comma-separated numbers."
        except Exception as e:
            return f"❌ Error calculating range statistics: {str(e)}"
