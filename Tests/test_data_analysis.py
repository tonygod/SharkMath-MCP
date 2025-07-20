"""
Comprehensive test suite for data_analysis consolidated tool.

This test suite covers all data analysis operations including:
- Z-score calculations and interpretations
- Correlation analysis (Pearson and Spearman)
- Quartile calculations and IQR analysis
- Skewness and kurtosis measurements
- Coefficient of variation analysis
- Outlier detection methods
- Confidence intervals
- Data standardization

Each test validates both successful calculations and error handling.
"""

import unittest
import json
import math
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from data_analysis import (
        _z_score, _correlation, _quartiles, _skewness, _kurtosis,
        _coefficient_variation, _outliers_detection, _confidence_interval,
        _standardize_data, _iqr_analysis, _parse_data, _calculate_basic_stats
    )
except ImportError:
    print("Warning: Could not import data_analysis functions directly")


class TestDataAnalysis(unittest.TestCase):
    """Test suite for consolidated data analysis tools."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.sample_data_json = json.dumps(self.sample_data)
        self.normal_data = [10, 12, 12, 13, 12, 11, 14, 13, 15, 10, 15, 12, 14, 13, 13, 14, 10, 12, 11, 13]
        self.normal_data_json = json.dumps(self.normal_data)
        
    def test_z_score_calculation(self):
        """Test z-score calculation with valid parameters."""
        result = _z_score(value=85, mean=75, std_dev=10)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Z-Score: 1.0000", result)
        self.assertIn("within 1 standard deviation", result)
        
    def test_z_score_outlier(self):
        """Test z-score calculation for outlier value."""
        result = _z_score(value=110, mean=75, std_dev=10)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Z-Score: 3.5000", result)
        self.assertIn("very unusual/outlier", result)
        
    def test_z_score_missing_params(self):
        """Test z-score with missing parameters."""
        result = _z_score(value=None, mean=75, std_dev=10)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("requires parameters", result)
        
    def test_z_score_zero_std_dev(self):
        """Test z-score with zero standard deviation."""
        result = _z_score(value=85, mean=75, std_dev=0)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("must be positive", result)
        
    def test_correlation_pearson(self):
        """Test Pearson correlation calculation."""
        data1 = json.dumps([1, 2, 3, 4, 5])
        data2 = json.dumps([2, 4, 6, 8, 10])  # Perfect positive correlation
        result = _correlation(data=data1, data2=data2, method="pearson")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Correlation Coefficient: 1.0000", result)
        self.assertIn("very strong positive correlation", result)
        
    def test_correlation_negative(self):
        """Test negative correlation."""
        data1 = json.dumps([1, 2, 3, 4, 5])
        data2 = json.dumps([10, 8, 6, 4, 2])  # Perfect negative correlation
        result = _correlation(data=data1, data2=data2, method="pearson")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Correlation Coefficient: -1.0000", result)
        self.assertIn("very strong negative correlation", result)
        
    def test_correlation_spearman(self):
        """Test Spearman rank correlation."""
        data1 = json.dumps([1, 3, 2, 5, 4])
        data2 = json.dumps([2, 6, 4, 10, 8])
        result = _correlation(data=data1, data2=data2, method="spearman")
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Spearman Correlation Analysis", result)
        
    def test_correlation_missing_params(self):
        """Test correlation with missing parameters."""
        result = _correlation(data=None, data2=self.sample_data_json)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("requires parameters", result)
        
    def test_correlation_different_lengths(self):
        """Test correlation with different length datasets."""
        data1 = json.dumps([1, 2, 3])
        data2 = json.dumps([4, 5, 6, 7])
        result = _correlation(data=data1, data2=data2)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("same length", result)
        
    def test_correlation_invalid_method(self):
        """Test correlation with invalid method."""
        data1 = json.dumps([1, 2, 3])
        data2 = json.dumps([4, 5, 6])
        result = _correlation(data=data1, data2=data2, method="invalid")
        self.assertTrue(result.startswith("❌"))
        self.assertIn("pearson", result)
        
    def test_quartiles_calculation(self):
        """Test quartile calculations."""
        result = _quartiles(data=self.sample_data_json)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Q1 (25th percentile)", result)
        self.assertIn("Q2 (Median)", result)
        self.assertIn("Q3 (75th percentile)", result)
        self.assertIn("Interquartile Range", result)
        
    def test_quartiles_insufficient_data(self):
        """Test quartiles with insufficient data."""
        result = _quartiles(data=json.dumps([1, 2]))
        self.assertTrue(result.startswith("❌"))
        self.assertIn("at least 4 data points", result)
        
    def test_skewness_calculation(self):
        """Test skewness calculation for symmetric data."""
        # Approximately symmetric data
        symmetric_data = [1, 2, 3, 3, 3, 4, 5]
        result = _skewness(data=json.dumps(symmetric_data))
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Skewness:", result)
        self.assertIn("Distribution:", result)
        
    def test_skewness_right_skewed(self):
        """Test skewness calculation for right-skewed data."""
        right_skewed = [1, 1, 2, 2, 3, 4, 8, 10, 15]
        result = _skewness(data=json.dumps(right_skewed))
        self.assertTrue(result.startswith("✅"))
        self.assertIn("right (positive)", result)
        
    def test_skewness_insufficient_data(self):
        """Test skewness with insufficient data."""
        result = _skewness(data=json.dumps([1, 2]))
        self.assertTrue(result.startswith("❌"))
        self.assertIn("at least 3 data points", result)
        
    def test_kurtosis_calculation(self):
        """Test kurtosis calculation."""
        result = _kurtosis(data=self.normal_data_json)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Kurtosis:", result)
        self.assertIn("Excess Kurtosis:", result)
        self.assertIn("Distribution:", result)
        
    def test_kurtosis_insufficient_data(self):
        """Test kurtosis with insufficient data."""
        result = _kurtosis(data=json.dumps([1, 2, 3]))
        self.assertTrue(result.startswith("❌"))
        self.assertIn("at least 4 data points", result)
        
    def test_coefficient_variation(self):
        """Test coefficient of variation calculation."""
        result = _coefficient_variation(data=self.sample_data_json)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("CV:", result)
        self.assertIn("Interpretation:", result)
        
    def test_coefficient_variation_zero_mean(self):
        """Test coefficient of variation with zero mean."""
        zero_mean_data = json.dumps([-5, 0, 5])
        result = _coefficient_variation(data=zero_mean_data)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("mean is zero", result)
        
    def test_outliers_detection(self):
        """Test outlier detection using IQR method."""
        # Data with clear outliers
        data_with_outliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]  # 100 is an outlier
        result = _outliers_detection(data=json.dumps(data_with_outliers))
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Outliers Found:", result)
        self.assertIn("Outlier Values:", result)
        self.assertIn("100", result)
        
    def test_outliers_no_outliers(self):
        """Test outlier detection with no outliers."""
        result = _outliers_detection(data=self.sample_data_json)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Outliers Found: 0", result)
        
    def test_outliers_insufficient_data(self):
        """Test outlier detection with insufficient data."""
        result = _outliers_detection(data=json.dumps([1, 2]))
        self.assertTrue(result.startswith("❌"))
        self.assertIn("at least 4 data points", result)
        
    def test_confidence_interval_default(self):
        """Test confidence interval with default 95% level."""
        result = _confidence_interval(data=self.sample_data_json)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Confidence Level: 95.0%", result)
        self.assertIn("Confidence Interval:", result)
        
    def test_confidence_interval_custom_level(self):
        """Test confidence interval with custom confidence level."""
        result = _confidence_interval(data=self.sample_data_json, confidence_level=0.99)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Confidence Level: 99.0%", result)
        
    def test_confidence_interval_invalid_level(self):
        """Test confidence interval with invalid confidence level."""
        result = _confidence_interval(data=self.sample_data_json, confidence_level=1.5)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("between 0 and 1", result)
        
    def test_confidence_interval_insufficient_data(self):
        """Test confidence interval with insufficient data."""
        result = _confidence_interval(data=json.dumps([5]))
        self.assertTrue(result.startswith("❌"))
        self.assertIn("at least 2 data points", result)
        
    def test_standardize_data(self):
        """Test data standardization."""
        result = _standardize_data(data=self.sample_data_json)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Standardized Data:", result)
        self.assertIn("Standardized Mean:", result)
        self.assertIn("Standardized Std Dev:", result)
        # Check that standardized mean is close to 0
        self.assertIn("0.0000", result)  # Mean should be approximately 0
        
    def test_standardize_zero_std_dev(self):
        """Test data standardization with zero standard deviation."""
        constant_data = json.dumps([5, 5, 5, 5])
        result = _standardize_data(data=constant_data)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("standard deviation is zero", result)
        
    def test_iqr_analysis_comprehensive(self):
        """Test comprehensive IQR analysis."""
        result = _iqr_analysis(data=self.sample_data_json)
        self.assertTrue(result.startswith("✅"))
        self.assertIn("10th Percentile:", result)
        self.assertIn("Q1 (25th):", result)
        self.assertIn("Median (50th):", result)
        self.assertIn("Q3 (75th):", result)
        self.assertIn("90th Percentile:", result)
        self.assertIn("IQR/Range Ratio:", result)
        
    def test_iqr_analysis_insufficient_data(self):
        """Test IQR analysis with insufficient data."""
        result = _iqr_analysis(data=json.dumps([1, 2]))
        self.assertTrue(result.startswith("❌"))
        self.assertIn("at least 4 data points", result)
        
    def test_parse_data_valid_json(self):
        """Test data parsing with valid JSON."""
        data = _parse_data("[1, 2, 3, 4, 5]")
        self.assertEqual(data, [1.0, 2.0, 3.0, 4.0, 5.0])
        
    def test_parse_data_invalid_json(self):
        """Test data parsing with invalid JSON."""
        with self.assertRaises(ValueError) as context:
            _parse_data("invalid json")
        self.assertIn("Invalid JSON format", str(context.exception))
        
    def test_parse_data_non_array(self):
        """Test data parsing with non-array JSON."""
        with self.assertRaises(ValueError) as context:
            _parse_data('{"not": "array"}')
        self.assertIn("must be a JSON array", str(context.exception))
        
    def test_parse_data_non_numeric(self):
        """Test data parsing with non-numeric values."""
        with self.assertRaises(ValueError) as context:
            _parse_data('["string", 2, 3]')
        self.assertIn("must be numbers", str(context.exception))
        
    def test_parse_data_empty_array(self):
        """Test data parsing with empty array."""
        with self.assertRaises(ValueError) as context:
            _parse_data('[]')
        self.assertIn("cannot be empty", str(context.exception))
        
    def test_calculate_basic_stats(self):
        """Test basic statistics calculation."""
        stats = _calculate_basic_stats([1, 2, 3, 4, 5])
        self.assertEqual(stats['n'], 5)
        self.assertEqual(stats['mean'], 3.0)
        self.assertEqual(stats['median'], 3.0)
        self.assertEqual(stats['min'], 1)
        self.assertEqual(stats['max'], 5)
        self.assertAlmostEqual(stats['std_dev'], math.sqrt(2), places=4)


if __name__ == '__main__':
    print("Running Data Analysis Tests...")
    print("=" * 60)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDataAnalysis)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print(f"\nFailures:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
            
    if result.errors:
        print(f"\nErrors:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun) * 100
    print(f"\nSuccess Rate: {success_rate:.1f}%")
