"""
Data Analysis Module for SharkMath MCP Server

This module provides consolidated advanced data analysis and statistical functions including:
- Advanced descriptive statistics (skewness, kurtosis, coefficient of variation)
- Correlation analysis (Pearson, Spearman)
- Z-score calculations and standardization  
- Quartile calculations and interquartile range
- Outlier detection methods
- Confidence intervals
- Data validation and cleaning helpers
- Distribution analysis

All functions follow the SharkMath error handling standards with ✅/❌ prefixes.
This is a consolidated tool using parameter-based routing.
"""

import math
import json
from typing import Optional, List


def register_tools(mcp):
    """Register consolidated data analysis tools with the MCP server."""
    
    @mcp.tool()
    async def data_analysis(
        operation: str,
        data: Optional[str] = None,
        value: Optional[float] = None,
        mean: Optional[float] = None,
        std_dev: Optional[float] = None,
        data2: Optional[str] = None,
        confidence_level: Optional[float] = None,
        method: Optional[str] = None,
        percentile: Optional[float] = None
    ) -> str:
        """
        Perform advanced data analysis and statistical calculations.
        
        Args:
            operation: Type of analysis - "z_score", "correlation", "quartiles", "skewness", 
                      "kurtosis", "coefficient_variation", "outliers", "confidence_interval",
                      "standardize_data", "iqr_analysis"
            data: JSON array of numerical data (e.g., "[1, 2, 3, 4, 5]")
            value: Individual value for z-score calculations
            mean: Mean value for z-score calculations
            std_dev: Standard deviation for z-score calculations  
            data2: Second dataset for correlation analysis (JSON array)
            confidence_level: Confidence level for intervals (e.g., 0.95 for 95%)
            method: Method type for correlation ("pearson" or "spearman")
            percentile: Percentile for quartile calculations (0-100)
            
        Returns:
            String with analysis results and statistical interpretations
        """
        
        # Define valid operations
        valid_operations = {
            "z_score": _z_score,
            "correlation": _correlation,
            "quartiles": _quartiles,
            "skewness": _skewness,
            "kurtosis": _kurtosis,
            "coefficient_variation": _coefficient_variation,
            "outliers": _outliers_detection,
            "confidence_interval": _confidence_interval,
            "standardize_data": _standardize_data,
            "iqr_analysis": _iqr_analysis
        }
        
        # Validate operation
        if operation not in valid_operations:
            valid_ops = ", ".join(valid_operations.keys())
            return f"❌ Invalid operation '{operation}'. Valid operations: {valid_ops}"
        
        try:
            # Route to appropriate function
            return valid_operations[operation](
                data=data, value=value, mean=mean, std_dev=std_dev,
                data2=data2, confidence_level=confidence_level,
                method=method, percentile=percentile
            )
            
        except Exception as e:
            return f"❌ Error in {operation} analysis: {str(e)}"


def _parse_data(data_str: str, param_name: str = "data") -> List[float]:
    """Helper function to parse JSON data with validation."""
    try:
        data_list = json.loads(data_str)
        if not isinstance(data_list, list):
            raise ValueError(f"{param_name} must be a JSON array")
        
        # Convert to float and validate
        numeric_data = []
        for i, item in enumerate(data_list):
            if not isinstance(item, (int, float)):
                raise ValueError(f"All {param_name} values must be numbers, found {type(item).__name__} at position {i}")
            numeric_data.append(float(item))
            
        if len(numeric_data) == 0:
            raise ValueError(f"{param_name} cannot be empty")
            
        return numeric_data
        
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format for {param_name}. Use format: '[1, 2, 3, 4, 5]'")


def _calculate_basic_stats(data: List[float]) -> dict:
    """Calculate basic statistical measures."""
    n = len(data)
    mean = sum(data) / n
    
    # Calculate variance and standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)
    
    # Sort data for median and quartiles
    sorted_data = sorted(data)
    
    # Calculate median
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    
    return {
        'n': n,
        'mean': mean,
        'median': median,
        'std_dev': std_dev,
        'variance': variance,
        'min': min(data),
        'max': max(data),
        'sorted_data': sorted_data
    }


def _z_score(value: Optional[float], mean: Optional[float], std_dev: Optional[float], **kwargs) -> str:
    """
    Calculate z-score: z = (value - mean) / std_dev
    """
    if value is None or mean is None or std_dev is None:
        return "❌ Z-score requires parameters: value, mean, std_dev"
    
    if std_dev <= 0:
        return "❌ Standard deviation must be positive"
    
    z = (value - mean) / std_dev
    
    # Interpretation
    if abs(z) <= 1:
        interpretation = "within 1 standard deviation (typical)"
    elif abs(z) <= 2:
        interpretation = "within 2 standard deviations (somewhat unusual)"
    elif abs(z) <= 3:
        interpretation = "within 3 standard deviations (unusual)"
    else:
        interpretation = "beyond 3 standard deviations (very unusual/outlier)"
    
    return (f"✅ Z-Score Analysis:\n"
           f"   Value: {value}\n"
           f"   Mean: {mean}\n"
           f"   Std Dev: {std_dev}\n"
           f"   Z-Score: {z:.4f}\n"
           f"   Interpretation: {interpretation}")


def _correlation(data: Optional[str], data2: Optional[str], method: Optional[str] = None, **kwargs) -> str:
    """
    Calculate correlation between two datasets.
    """
    if data is None or data2 is None:
        return "❌ Correlation requires parameters: data, data2"
    
    if method is None:
        method = "pearson"
    
    if method.lower() not in ["pearson", "spearman"]:
        return "❌ Method must be 'pearson' or 'spearman'"
    
    # Parse data
    dataset1 = _parse_data(data, "data")
    dataset2 = _parse_data(data2, "data2")
    
    if len(dataset1) != len(dataset2):
        return "❌ Both datasets must have the same length"
    
    if len(dataset1) < 2:
        return "❌ Need at least 2 data points for correlation"
    
    # Calculate correlation based on method
    if method.lower() == "pearson":
        correlation_coef = _pearson_correlation(dataset1, dataset2)
        method_name = "Pearson"
    else:
        correlation_coef = _spearman_correlation(dataset1, dataset2)
        method_name = "Spearman"
    
    # Interpretation
    abs_corr = abs(correlation_coef)
    if abs_corr >= 0.9:
        strength = "very strong"
    elif abs_corr >= 0.7:
        strength = "strong"
    elif abs_corr >= 0.5:
        strength = "moderate"
    elif abs_corr >= 0.3:
        strength = "weak"
    else:
        strength = "very weak"
    
    direction = "positive" if correlation_coef > 0 else "negative" if correlation_coef < 0 else "no"
    
    return (f"✅ {method_name} Correlation Analysis:\n"
           f"   Dataset 1: {len(dataset1)} values\n"
           f"   Dataset 2: {len(dataset2)} values\n"
           f"   Correlation Coefficient: {correlation_coef:.4f}\n"
           f"   Strength: {strength} {direction} correlation\n"
           f"   R²: {correlation_coef**2:.4f} (coefficient of determination)")


def _pearson_correlation(x: List[float], y: List[float]) -> float:
    """Calculate Pearson correlation coefficient."""
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    sum_sq_x = sum((xi - mean_x) ** 2 for xi in x)
    sum_sq_y = sum((yi - mean_y) ** 2 for yi in y)
    
    denominator = math.sqrt(sum_sq_x * sum_sq_y)
    
    if denominator == 0:
        return 0.0  # No correlation when one variable is constant
    
    return numerator / denominator


def _spearman_correlation(x: List[float], y: List[float]) -> float:
    """Calculate Spearman rank correlation coefficient."""
    # Convert to ranks
    x_ranks = _convert_to_ranks(x)
    y_ranks = _convert_to_ranks(y)
    
    # Calculate Pearson correlation on ranks
    return _pearson_correlation(x_ranks, y_ranks)


def _convert_to_ranks(data: List[float]) -> List[float]:
    """Convert data to ranks (1-based)."""
    indexed_data = [(value, i) for i, value in enumerate(data)]
    indexed_data.sort(key=lambda x: x[0])
    
    ranks = [0] * len(data)
    for rank, (value, original_index) in enumerate(indexed_data):
        ranks[original_index] = rank + 1
        
    return ranks


def _quartiles(data: Optional[str], **kwargs) -> str:
    """
    Calculate quartiles and related statistics.
    """
    if data is None:
        return "❌ Quartiles analysis requires parameter: data"
    
    dataset = _parse_data(data)
    if len(dataset) < 4:
        return "❌ Need at least 4 data points for quartile analysis"
    
    stats = _calculate_basic_stats(dataset)
    sorted_data = stats['sorted_data']
    n = len(sorted_data)
    
    # Calculate quartiles
    q1_pos = (n + 1) / 4
    q2_pos = (n + 1) / 2  # median
    q3_pos = 3 * (n + 1) / 4
    
    q1 = _interpolate_percentile(sorted_data, q1_pos)
    q2 = stats['median']  # Already calculated
    q3 = _interpolate_percentile(sorted_data, q3_pos)
    
    iqr = q3 - q1
    
    return (f"✅ Quartile Analysis:\n"
           f"   Sample Size: {n}\n"
           f"   Minimum: {stats['min']}\n"
           f"   Q1 (25th percentile): {q1:.2f}\n"
           f"   Q2 (Median): {q2:.2f}\n"
           f"   Q3 (75th percentile): {q3:.2f}\n"
           f"   Maximum: {stats['max']}\n"
           f"   Interquartile Range (IQR): {iqr:.2f}")


def _interpolate_percentile(sorted_data: List[float], position: float) -> float:
    """Interpolate percentile value at given position."""
    if position <= 1:
        return sorted_data[0]
    elif position >= len(sorted_data):
        return sorted_data[-1]
    else:
        lower_index = int(position) - 1
        upper_index = lower_index + 1
        
        if upper_index >= len(sorted_data):
            return sorted_data[lower_index]
        
        # Linear interpolation
        fraction = position - int(position)
        return sorted_data[lower_index] + fraction * (sorted_data[upper_index] - sorted_data[lower_index])


def _skewness(data: Optional[str], **kwargs) -> str:
    """
    Calculate skewness (measure of asymmetry).
    """
    if data is None:
        return "❌ Skewness analysis requires parameter: data"
    
    dataset = _parse_data(data)
    if len(dataset) < 3:
        return "❌ Need at least 3 data points for skewness calculation"
    
    stats = _calculate_basic_stats(dataset)
    n = stats['n']
    mean = stats['mean']
    std_dev = stats['std_dev']
    
    if std_dev == 0:
        return "❌ Cannot calculate skewness: standard deviation is zero"
    
    # Calculate skewness: E[(X - μ)³] / σ³
    skew = sum((x - mean) ** 3 for x in dataset) / (n * std_dev ** 3)
    
    # Interpretation
    if abs(skew) < 0.5:
        interpretation = "approximately symmetric"
    elif abs(skew) < 1:
        interpretation = "moderately skewed"
    else:
        interpretation = "highly skewed"
    
    if skew > 0:
        direction = "right (positive)"
    elif skew < 0:
        direction = "left (negative)"
    else:
        direction = "symmetric"
    
    return (f"✅ Skewness Analysis:\n"
           f"   Sample Size: {n}\n"
           f"   Mean: {mean:.2f}\n"
           f"   Std Dev: {std_dev:.2f}\n"
           f"   Skewness: {skew:.4f}\n"
           f"   Distribution: {interpretation}\n"
           f"   Direction: {direction} skew")


def _kurtosis(data: Optional[str], **kwargs) -> str:
    """
    Calculate kurtosis (measure of tail heaviness).
    """
    if data is None:
        return "❌ Kurtosis analysis requires parameter: data"
    
    dataset = _parse_data(data)
    if len(dataset) < 4:
        return "❌ Need at least 4 data points for kurtosis calculation"
    
    stats = _calculate_basic_stats(dataset)
    n = stats['n']
    mean = stats['mean']
    std_dev = stats['std_dev']
    
    if std_dev == 0:
        return "❌ Cannot calculate kurtosis: standard deviation is zero"
    
    # Calculate kurtosis: E[(X - μ)⁴] / σ⁴
    kurt = sum((x - mean) ** 4 for x in dataset) / (n * std_dev ** 4)
    excess_kurt = kurt - 3  # Excess kurtosis (subtract 3 for normal distribution)
    
    # Interpretation
    if abs(excess_kurt) < 0.5:
        interpretation = "approximately normal (mesokurtic)"
    elif excess_kurt > 0.5:
        interpretation = "heavy-tailed (leptokurtic)"
    else:
        interpretation = "light-tailed (platykurtic)"
    
    return (f"✅ Kurtosis Analysis:\n"
           f"   Sample Size: {n}\n"
           f"   Mean: {mean:.2f}\n"
           f"   Std Dev: {std_dev:.2f}\n"
           f"   Kurtosis: {kurt:.4f}\n"
           f"   Excess Kurtosis: {excess_kurt:.4f}\n"
           f"   Distribution: {interpretation}")


def _coefficient_variation(data: Optional[str], **kwargs) -> str:
    """
    Calculate coefficient of variation (CV = σ/μ).
    """
    if data is None:
        return "❌ Coefficient of variation requires parameter: data"
    
    dataset = _parse_data(data)
    if len(dataset) < 2:
        return "❌ Need at least 2 data points for coefficient of variation"
    
    stats = _calculate_basic_stats(dataset)
    mean = stats['mean']
    std_dev = stats['std_dev']
    
    if mean == 0:
        return "❌ Cannot calculate coefficient of variation: mean is zero"
    
    cv = std_dev / abs(mean)
    cv_percent = cv * 100
    
    # Interpretation
    if cv_percent < 15:
        interpretation = "low variability"
    elif cv_percent < 35:
        interpretation = "moderate variability"
    else:
        interpretation = "high variability"
    
    return (f"✅ Coefficient of Variation Analysis:\n"
           f"   Sample Size: {stats['n']}\n"
           f"   Mean: {mean:.2f}\n"
           f"   Std Dev: {std_dev:.2f}\n"
           f"   CV: {cv:.4f} ({cv_percent:.2f}%)\n"
           f"   Interpretation: {interpretation}")


def _outliers_detection(data: Optional[str], **kwargs) -> str:
    """
    Detect outliers using IQR method.
    """
    if data is None:
        return "❌ Outlier detection requires parameter: data"
    
    dataset = _parse_data(data)
    if len(dataset) < 4:
        return "❌ Need at least 4 data points for outlier detection"
    
    stats = _calculate_basic_stats(dataset)
    sorted_data = stats['sorted_data']
    n = len(sorted_data)
    
    # Calculate quartiles
    q1_pos = (n + 1) / 4
    q3_pos = 3 * (n + 1) / 4
    
    q1 = _interpolate_percentile(sorted_data, q1_pos)
    q3 = _interpolate_percentile(sorted_data, q3_pos)
    
    iqr = q3 - q1
    
    # Calculate outlier bounds
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Find outliers
    outliers = [x for x in dataset if x < lower_bound or x > upper_bound]
    outliers.sort()
    
    return (f"✅ Outlier Detection (IQR Method):\n"
           f"   Sample Size: {n}\n"
           f"   Q1: {q1:.2f}\n"
           f"   Q3: {q3:.2f}\n"
           f"   IQR: {iqr:.2f}\n"
           f"   Lower Bound: {lower_bound:.2f}\n"
           f"   Upper Bound: {upper_bound:.2f}\n"
           f"   Outliers Found: {len(outliers)}\n"
           f"   Outlier Values: {outliers}")


def _confidence_interval(data: Optional[str], confidence_level: Optional[float] = None, **kwargs) -> str:
    """
    Calculate confidence interval for the mean.
    """
    if data is None:
        return "❌ Confidence interval requires parameter: data"
    
    if confidence_level is None:
        confidence_level = 0.95
    
    if not (0 < confidence_level < 1):
        return "❌ Confidence level must be between 0 and 1 (e.g., 0.95 for 95%)"
    
    dataset = _parse_data(data)
    if len(dataset) < 2:
        return "❌ Need at least 2 data points for confidence interval"
    
    stats = _calculate_basic_stats(dataset)
    n = stats['n']
    mean = stats['mean']
    std_dev = stats['std_dev']
    
    # Standard error of the mean
    se = std_dev / math.sqrt(n)
    
    # Critical value (approximation for large samples)
    # For normal distribution: 90% -> 1.645, 95% -> 1.96, 99% -> 2.576
    critical_values = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
    
    if confidence_level in critical_values:
        z_critical = critical_values[confidence_level]
    else:
        # Approximate z-critical for other confidence levels
        # This is a simplification; exact values require inverse normal function
        z_critical = 1.96  # Default to 95%
    
    # Calculate margin of error
    margin_error = z_critical * se
    
    # Calculate confidence interval
    lower_bound = mean - margin_error
    upper_bound = mean + margin_error
    
    confidence_percent = confidence_level * 100
    
    return (f"✅ Confidence Interval for Mean:\n"
           f"   Sample Size: {n}\n"
           f"   Sample Mean: {mean:.4f}\n"
           f"   Standard Error: {se:.4f}\n"
           f"   Confidence Level: {confidence_percent}%\n"
           f"   Margin of Error: ±{margin_error:.4f}\n"
           f"   Confidence Interval: [{lower_bound:.4f}, {upper_bound:.4f}]")


def _standardize_data(data: Optional[str], **kwargs) -> str:
    """
    Standardize data (z-score transformation).
    """
    if data is None:
        return "❌ Data standardization requires parameter: data"
    
    dataset = _parse_data(data)
    if len(dataset) < 2:
        return "❌ Need at least 2 data points for standardization"
    
    stats = _calculate_basic_stats(dataset)
    mean = stats['mean']
    std_dev = stats['std_dev']
    
    if std_dev == 0:
        return "❌ Cannot standardize data: standard deviation is zero"
    
    # Standardize each value
    standardized = [(x - mean) / std_dev for x in dataset]
    
    # Verify standardization (should have mean≈0, std≈1)
    std_stats = _calculate_basic_stats(standardized)
    
    return (f"✅ Data Standardization:\n"
           f"   Original Data: {len(dataset)} values\n"
           f"   Original Mean: {mean:.4f}\n"
           f"   Original Std Dev: {std_dev:.4f}\n"
           f"   Standardized Data: {[round(x, 4) for x in standardized]}\n"
           f"   Standardized Mean: {std_stats['mean']:.4f} (should ≈ 0)\n"
           f"   Standardized Std Dev: {std_stats['std_dev']:.4f} (should ≈ 1)")


def _iqr_analysis(data: Optional[str], **kwargs) -> str:
    """
    Comprehensive interquartile range analysis.
    """
    if data is None:
        return "❌ IQR analysis requires parameter: data"
    
    dataset = _parse_data(data)
    if len(dataset) < 4:
        return "❌ Need at least 4 data points for IQR analysis"
    
    stats = _calculate_basic_stats(dataset)
    sorted_data = stats['sorted_data']
    n = len(sorted_data)
    
    # Calculate quartiles and percentiles
    q1_pos = (n + 1) / 4
    q3_pos = 3 * (n + 1) / 4
    
    q1 = _interpolate_percentile(sorted_data, q1_pos)
    q3 = _interpolate_percentile(sorted_data, q3_pos)
    
    iqr = q3 - q1
    
    # Calculate additional percentiles
    p10 = _interpolate_percentile(sorted_data, (n + 1) * 0.1)
    p90 = _interpolate_percentile(sorted_data, (n + 1) * 0.9)
    
    # Data spread analysis
    total_range = stats['max'] - stats['min']
    iqr_ratio = iqr / total_range if total_range > 0 else 0
    
    return (f"✅ Interquartile Range Analysis:\n"
           f"   Sample Size: {n}\n"
           f"   10th Percentile: {p10:.2f}\n"
           f"   Q1 (25th): {q1:.2f}\n"
           f"   Median (50th): {stats['median']:.2f}\n"
           f"   Q3 (75th): {q3:.2f}\n"
           f"   90th Percentile: {p90:.2f}\n"
           f"   IQR: {iqr:.2f}\n"
           f"   Total Range: {total_range:.2f}\n"
           f"   IQR/Range Ratio: {iqr_ratio:.2f}")


# Support for direct execution (testing)
if __name__ == "__main__":
    print("Data Analysis Functions Test")
    print("=" * 40)
    
    # Test cases would go here for development
    print("This module should be imported by sharkmath_server.py")
