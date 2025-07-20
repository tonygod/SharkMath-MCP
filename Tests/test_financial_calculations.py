"""
Comprehensive test suite for financial_calculations consolidated tool.

This test suite covers all financial operations including:
- Present value and future value calculations
- Loan and mortgage payments
- Return on Investment (ROI)
- Depreciation methods (straight-line and declining balance)
- Break-even analysis
- Net Present Value (NPV)
- Compound and simple interest (migrated from solve_equations)

Each test validates both successful calculations and error handling.
"""

import unittest
import json
from unittest.mock import AsyncMock
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from financial_calculations import (
        _present_value, _future_value, _loan_payment, _return_on_investment,
        _straight_line_depreciation, _declining_balance_depreciation,
        _mortgage_payment, _break_even_point, _net_present_value,
        _compound_interest, _simple_interest
    )
except ImportError:
    print("Warning: Could not import financial_calculations functions directly")


class TestFinancialCalculations(unittest.TestCase):
    """Test suite for consolidated financial calculations tool."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.valid_financial_params = {
            'principal': 10000.0,
            'rate': 0.05,  # 5%
            'time': 5.0,
            'future_value': 12762.82,
            'present_value': 10000.0,
            'compounds_per_year': 1
        }
        
    def test_present_value_calculation(self):
        """Test present value calculation with valid parameters."""
        result = _present_value(
            future_value=12762.82,
            rate=0.05,
            time=5.0,
            compounds_per_year=1
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Present Value: $10,000.00", result)
        self.assertIn("Future Value: $12,762.82", result)
        
    def test_present_value_missing_params(self):
        """Test present value with missing required parameters."""
        result = _present_value(future_value=None, rate=0.05, time=5.0)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("requires parameters", result)
        
    def test_present_value_negative_values(self):
        """Test present value with negative input values."""
        result = _present_value(future_value=-1000, rate=0.05, time=5.0)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("cannot be negative", result)
        
    def test_future_value_calculation(self):
        """Test future value calculation with valid parameters."""
        result = _future_value(
            present_value=10000.0,
            rate=0.05,
            time=5.0,
            compounds_per_year=1
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Future Value: $12,762.82", result)
        self.assertIn("Growth: $2,762.82", result)
        
    def test_future_value_missing_params(self):
        """Test future value with missing required parameters."""
        result = _future_value(present_value=10000.0, rate=None, time=5.0)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("requires parameters", result)
        
    def test_loan_payment_calculation(self):
        """Test loan payment calculation with valid parameters."""
        result = _loan_payment(
            principal=200000.0,
            rate=0.06,  # 6% APR
            time=30.0,  # 30 years
            compounds_per_year=12  # Monthly payments
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Payment: $1,199.10", result)
        self.assertIn("360 payments", result)
        
    def test_loan_payment_zero_interest(self):
        """Test loan payment with zero interest rate."""
        result = _loan_payment(
            principal=12000.0,
            rate=0.0,
            time=4.0,
            compounds_per_year=12
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Payment: $250.00", result)
        self.assertIn("Total Interest: $0.00", result)
        
    def test_loan_payment_invalid_params(self):
        """Test loan payment with invalid parameters."""
        result = _loan_payment(principal=-1000, rate=0.05, time=5.0)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("must be positive", result)
        
    def test_roi_calculation(self):
        """Test return on investment calculation."""
        result = _return_on_investment(
            initial_investment=10000.0,
            final_value=15000.0
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("ROI: 50.00%", result)
        self.assertIn("Gain/Loss: $5,000.00", result)
        
    def test_roi_loss_scenario(self):
        """Test ROI calculation with investment loss."""
        result = _return_on_investment(
            initial_investment=10000.0,
            final_value=8000.0
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("ROI: -20.00%", result)
        self.assertIn("Gain/Loss: $-2,000.00", result)
        
    def test_roi_missing_params(self):
        """Test ROI with missing parameters."""
        result = _return_on_investment(initial_investment=None, final_value=15000.0)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("requires parameters", result)
        
    def test_straight_line_depreciation(self):
        """Test straight-line depreciation calculation."""
        result = _straight_line_depreciation(
            cost_basis=50000.0,
            salvage_value=5000.0,
            useful_life=10.0
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Annual Depreciation: $4,500.00", result)
        self.assertIn("Depreciable Amount: $45,000.00", result)
        
    def test_straight_line_depreciation_invalid_salvage(self):
        """Test depreciation with salvage value exceeding cost basis."""
        result = _straight_line_depreciation(
            cost_basis=10000.0,
            salvage_value=15000.0,
            useful_life=5.0
        )
        self.assertTrue(result.startswith("❌"))
        self.assertIn("cannot exceed cost basis", result)
        
    def test_declining_balance_depreciation(self):
        """Test declining balance depreciation calculation."""
        result = _declining_balance_depreciation(
            cost_basis=50000.0,
            declining_rate=0.2,  # 20%
            useful_life=10.0
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Year 1 Depreciation: $10,000.00", result)
        self.assertIn("Remaining Book Value: $40,000.00", result)
        
    def test_declining_balance_invalid_rate(self):
        """Test declining balance with invalid rate."""
        result = _declining_balance_depreciation(
            cost_basis=50000.0,
            declining_rate=1.5,  # 150% - invalid
            useful_life=10.0
        )
        self.assertTrue(result.startswith("❌"))
        self.assertIn("between 0 and 1", result)
        
    def test_mortgage_payment_calculation(self):
        """Test mortgage payment calculation (30-year fixed)."""
        result = _mortgage_payment(
            principal=300000.0,
            rate=0.045,  # 4.5% APR
            time=30.0
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Monthly Payment: $1,520.06", result)
        self.assertIn("Total Interest: $247,220.13", result)
        
    def test_break_even_analysis(self):
        """Test break-even point calculation."""
        result = _break_even_point(
            fixed_costs=50000.0,
            variable_cost_per_unit=15.0,
            price_per_unit=25.0
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Break-Even Point: 5,000 units", result)
        self.assertIn("Contribution Margin: $10.00", result)
        
    def test_break_even_invalid_pricing(self):
        """Test break-even with price less than variable cost."""
        result = _break_even_point(
            fixed_costs=50000.0,
            variable_cost_per_unit=25.0,
            price_per_unit=20.0
        )
        self.assertTrue(result.startswith("❌"))
        self.assertIn("must be greater than variable cost", result)
        
    def test_net_present_value_calculation(self):
        """Test NPV calculation with positive cash flows."""
        cash_flows = json.dumps([1000, 1500, 2000, 1200])
        result = _net_present_value(
            cash_flows=cash_flows,
            discount_rate=0.08
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Number of Periods: 4", result)
        self.assertIn("Net Present Value:", result)
        
    def test_net_present_value_invalid_json(self):
        """Test NPV with invalid JSON format."""
        result = _net_present_value(
            cash_flows="invalid json",
            discount_rate=0.08
        )
        self.assertTrue(result.startswith("❌"))
        self.assertIn("Invalid JSON format", result)
        
    def test_net_present_value_non_array(self):
        """Test NPV with non-array JSON."""
        result = _net_present_value(
            cash_flows='{"not": "array"}',
            discount_rate=0.08
        )
        self.assertTrue(result.startswith("❌"))
        self.assertIn("must be a JSON array", result)
        
    def test_compound_interest_calculation(self):
        """Test compound interest calculation (migrated from solve_equations)."""
        result = _compound_interest(
            principal=10000.0,
            rate=0.05,
            time=5.0,
            compounds_per_year=4  # Quarterly compounding
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Final Amount: $12,820.37", result)
        self.assertIn("compounded quarterly", result)
        
    def test_compound_interest_annual_compounding(self):
        """Test compound interest with annual compounding."""
        result = _compound_interest(
            principal=5000.0,
            rate=0.06,
            time=3.0,
            compounds_per_year=1
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("compounded annually", result)
        self.assertIn("Final Amount: $5,955.08", result)
        
    def test_compound_interest_daily_compounding(self):
        """Test compound interest with daily compounding."""
        result = _compound_interest(
            principal=1000.0,
            rate=0.04,
            time=2.0,
            compounds_per_year=365
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("compounded daily", result)
        
    def test_simple_interest_calculation(self):
        """Test simple interest calculation (migrated from solve_equations)."""
        result = _simple_interest(
            principal=10000.0,
            rate=0.05,
            time=3.0
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Final Amount: $11,500.00", result)
        self.assertIn("Interest Earned: $1,500.00", result)
        
    def test_simple_interest_zero_rate(self):
        """Test simple interest with zero interest rate."""
        result = _simple_interest(
            principal=5000.0,
            rate=0.0,
            time=5.0
        )
        self.assertTrue(result.startswith("✅"))
        self.assertIn("Final Amount: $5,000.00", result)
        self.assertIn("Interest Earned: $0.00", result)
        
    def test_compound_interest_missing_params(self):
        """Test compound interest with missing required parameters."""
        result = _compound_interest(principal=None, rate=0.05, time=5.0)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("requires parameters", result)
        
    def test_simple_interest_negative_principal(self):
        """Test simple interest with negative principal."""
        result = _simple_interest(principal=-1000.0, rate=0.05, time=3.0)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("cannot be negative", result)
        
    def test_compound_interest_negative_rate(self):
        """Test compound interest with negative rate."""
        result = _compound_interest(
            principal=10000.0,
            rate=-0.05,
            time=5.0
        )
        self.assertTrue(result.startswith("❌"))
        self.assertIn("cannot be negative", result)
        
    def test_compound_interest_zero_compounds_per_year(self):
        """Test compound interest with invalid compounding frequency."""
        result = _compound_interest(
            principal=10000.0,
            rate=0.05,
            time=5.0,
            compounds_per_year=0
        )
        self.assertTrue(result.startswith("❌"))
        self.assertIn("must be positive", result)
        
    def test_loan_payment_zero_time(self):
        """Test loan payment with zero time period."""
        result = _loan_payment(principal=10000.0, rate=0.05, time=0.0)
        self.assertTrue(result.startswith("❌"))
        self.assertIn("must be positive", result)


if __name__ == '__main__':
    print("Running Financial Calculations Tests...")
    print("=" * 60)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFinancialCalculations)
    
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
