"""
Consolidated Statistical Functions for SharkMath MCP Server
Consolidates all statistical operations into a single parameter-based tool.
"""
import statistics as stats_lib
from typing import List

class StatisticsTool:
    """Consolidated statistics calculator with parameter-based routing."""
    
    @staticmethod
    def _parse_numbers(numbers_str: str) -> List[float]:
        """Parse comma-separated numbers string into list of floats."""
        if not numbers_str or not numbers_str.strip():
            raise ValueError("No numbers provided!")
        
        try:
            # Handle both comma-separated and space-separated inputs
            if ',' in numbers_str:
                num_list = [float(x.strip()) for x in numbers_str.split(',') if x.strip()]
            else:
                num_list = [float(x.strip()) for x in numbers_str.split() if x.strip()]
            
            if not num_list:
                raise ValueError("No valid numbers found!")
            
            return num_list
        except ValueError as e:
            if "could not convert" in str(e).lower():
                raise ValueError("Invalid number format! Please provide comma-separated or space-separated numbers.")
            raise e
    
    @staticmethod
    def _validate_minimum_count(num_list: List[float], min_count: int, operation: str) -> None:
        """Validate that the list has enough numbers for the operation."""
        if len(num_list) < min_count:
            raise ValueError(f"Need at least {min_count} numbers to calculate {operation}!")
    
    @staticmethod
    def _format_result(operation: str, num_list: List[float], result) -> str:
        """Format the result with appropriate prefix and description."""
        if operation == "range_stats":
            min_val, max_val, range_val = result
            return f"✅ Range stats of {num_list}: Min = {min_val}, Max = {max_val}, Range = {range_val}"
        elif operation == "percentile":
            percentile, result_val = result
            return f"✅ {percentile}th percentile of {num_list} = {result_val}"
        else:
            operation_name = operation.replace('_', ' ').title()
            return f"✅ {operation_name} of {num_list} = {result}"
    
    @staticmethod
    def calculate(operation: str, numbers: str, percentile: float = None) -> str:
        """
        Calculate statistical functions with parameter-based routing.
        
        Args:
            operation: The statistical operation to perform
                - "mean": arithmetic mean (average)
                - "median": middle value when sorted
                - "mode": most frequent value
                - "standard_deviation": standard deviation (sample)
                - "variance": variance (sample)  
                - "range_stats": minimum, maximum, and range
                - "percentile": specified percentile (requires percentile parameter)
            numbers: Comma-separated or space-separated list of numbers
            percentile: Percentile value (0-100) for percentile calculation
            
        Returns:
            Formatted result string with ✅ success or ❌ error prefix
        """
        try:
            # Parse the input numbers
            num_list = StatisticsTool._parse_numbers(numbers)
            
            if operation == "mean":
                result = stats_lib.mean(num_list)
                return StatisticsTool._format_result(operation, num_list, result)
                
            elif operation == "median":
                result = stats_lib.median(num_list)
                return StatisticsTool._format_result(operation, num_list, result)
                
            elif operation == "mode":
                try:
                    result = stats_lib.mode(num_list)
                    return StatisticsTool._format_result(operation, num_list, result)
                except stats_lib.StatisticsError:
                    return "❌ Error: No unique mode found! All values appear equally often."
                    
            elif operation == "standard_deviation":
                StatisticsTool._validate_minimum_count(num_list, 2, "standard deviation")
                result = stats_lib.stdev(num_list)
                return StatisticsTool._format_result(operation, num_list, result)
                
            elif operation == "variance":
                StatisticsTool._validate_minimum_count(num_list, 2, "variance")
                result = stats_lib.variance(num_list)
                return StatisticsTool._format_result(operation, num_list, result)
                
            elif operation == "range_stats":
                min_val = min(num_list)
                max_val = max(num_list)
                range_val = max_val - min_val
                result = (min_val, max_val, range_val)
                return StatisticsTool._format_result(operation, num_list, result)
                
            elif operation == "percentile":
                if percentile is None:
                    return "❌ Error: percentile requires 'percentile' parameter (0-100)"
                
                if not (0 <= percentile <= 100):
                    return "❌ Error: percentile must be between 0 and 100"
                
                # Use a direct approach for percentile calculation
                if percentile == 0:
                    result_val = min(num_list)
                elif percentile == 100:
                    result_val = max(num_list)
                elif percentile == 50:
                    result_val = stats_lib.median(num_list)
                else:
                    # Use linear interpolation method for other percentiles
                    sorted_data = sorted(num_list)
                    n = len(sorted_data)
                    
                    if n == 1:
                        result_val = sorted_data[0]
                    else:
                        # Calculate index using standard percentile formula
                        index = (percentile / 100) * (n - 1)
                        
                        if index == int(index):
                            # Exact index
                            result_val = sorted_data[int(index)]
                        else:
                            # Linear interpolation between two values
                            lower_index = int(index)
                            upper_index = min(lower_index + 1, n - 1)
                            weight = index - lower_index
                            result_val = sorted_data[lower_index] * (1 - weight) + sorted_data[upper_index] * weight
                
                result = (percentile, result_val)
                return StatisticsTool._format_result(operation, num_list, result)
                
            else:
                return f"❌ Error: Operation '{operation}' is not supported. Supported: mean, median, mode, standard_deviation, variance, range_stats, percentile"
                
        except ValueError as e:
            return f"❌ Error: {str(e)}"
        except Exception as e:
            return f"❌ Error calculating {operation}: {str(e)}"

def register_tools(mcp):
    """Register consolidated statistics tool with the MCP server."""
    
    @mcp.tool()
    async def calculate_statistics(
        operation: str,
        numbers: str,
        percentile: float = None
    ) -> str:
        """
        Calculate statistical functions on a dataset.
        
        This consolidated tool handles all statistical operations:
        - Basic stats: mean, median, mode
        - Spread measures: standard_deviation, variance, range_stats
        - Percentiles: percentile (requires percentile parameter 0-100)
        
        Parameters:
        - operation: mean, median, mode, standard_deviation, variance, range_stats, or percentile
        - numbers: Comma-separated or space-separated list of numbers (e.g., "1,2,3,4,5" or "1 2 3 4 5")
        - percentile: For percentile calculation, specify value between 0-100 (e.g., 25 for 25th percentile)
        
        Examples:
        - calculate_statistics("mean", "1,2,3,4,5")
        - calculate_statistics("median", "10 20 30 40 50")
        - calculate_statistics("standard_deviation", "2.5, 3.0, 3.5, 4.0")
        - calculate_statistics("percentile", "1,2,3,4,5,6,7,8,9,10", percentile=75)
        """
        return StatisticsTool.calculate(operation, numbers, percentile)

# Support direct execution for testing
if __name__ == "__main__":
    # Test cases for verification
    test_cases = [
        # Basic statistics
        ("mean", {"numbers": "1,2,3,4,5"}),
        ("median", {"numbers": "1,3,3,6,7,8,9"}),
        ("mode", {"numbers": "1,2,2,3,4,4,4"}),
        
        # Spread measures
        ("standard_deviation", {"numbers": "2,4,4,4,5,5,7,9"}),
        ("variance", {"numbers": "2,4,4,4,5,5,7,9"}),
        ("range_stats", {"numbers": "1,3,5,7,9"}),
        
        # Percentiles
        ("percentile", {"numbers": "1,2,3,4,5,6,7,8,9,10", "percentile": 25}),
        ("percentile", {"numbers": "1,2,3,4,5,6,7,8,9,10", "percentile": 75}),
        
        # Space-separated input
        ("mean", {"numbers": "10 20 30 40 50"}),
        
        # Error cases
        ("standard_deviation", {"numbers": "5"}),  # Too few numbers
        ("mode", {"numbers": "1,2,3,4"}),  # No unique mode
        ("percentile", {"numbers": "1,2,3", "percentile": 150}),  # Invalid percentile
        ("invalid", {"numbers": "1,2,3"}),  # Invalid operation
    ]
    
    print("Testing Consolidated Statistics Tool:")
    print("=" * 50)
    
    for operation, params in test_cases:
        result = StatisticsTool.calculate(operation, **params)
        print(f"{operation}({params}): {result}")
        print()
