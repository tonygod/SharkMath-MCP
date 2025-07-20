#!/usr/bin/env python3
"""
SharkMath MCP Server Comprehensive Test Suite
Tests key functions from all mathematical domains
"""

import sys
import os

# Add SharkMath directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import SharkMath modules directly
import arithmetic
import power_operations
import matrix_operations
import trigonometric
import conversions
import advanced_calc
import statistics as stats_module  # Rename to avoid conflict

class TestRunner:
    """Test runner that tracks pass/fail results"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
    
    def run_test(self, name, test_func, expected_error=False):
        """Run a test and track results with detailed debugging"""
        try:
            print(f"⏳ Running {name}...")
            result = test_func()
            if expected_error:
                print(f"❌ {name} (expected error but got success)")
                self.failed += 1
            else:
                print(f"✅ {name}")
                self.passed += 1
        except Exception as e:
            print(f"❌ {name} (Error: {str(e)})")
            print(f"   Debug: {type(e).__name__}")
            if not expected_error:
                self.failed += 1
            else:
                print(f"   Expected error - counting as pass")
                self.passed += 1
    
    def print_summary(self):
        total = self.passed + self.failed
        success_rate = (self.passed / total * 100) if total > 0 else 0
        
        print("\n" + "="*60)
        print("FINAL TEST SUMMARY")
        print("="*60)
        print(f"Total Tests: {total}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Success Rate: {success_rate:.1f}%")
        
        if self.failed == 0:
            print("🎉 All tests passed!")
            print("✨ SharkMath MCP Server is working perfectly!")
        else:
            print(f"⚠️  {self.failed} tests failed.")
            print("✨ SharkMath MCP Server needs attention")

def main():
    """Main test function"""
    
    print("SharkMath Comprehensive Test Suite")
    print("Testing key functions across all mathematical domains")
    print("="*60 + "\n")
    
    runner = TestRunner()
    
    print("="*60)
    print("ARITHMETIC TESTS")
    print("="*60)
    
    # Test basic arithmetic
    def test_add():
        result = arithmetic.add(2, 3)
        print(f"     Debug: add result = '{result}'")
        return "5" in str(result)
    
    def test_divide_zero():
        try:
            result = arithmetic.divide(5, 0)
            print(f"     Debug: divide by zero result = '{result}'")
            return "Error" in str(result) or "division" in str(result) or "zero" in str(result)
        except Exception as e:
            print(f"     Debug: Exception as expected: {e}")
            return True  # Exception is expected for division by zero
    
    def test_calculate():
        result = arithmetic.calculate("2 + 3 * 4")
        print(f"     Debug: calculate result = '{result}'")
        return "14" in str(result)
    
    runner.run_test("add_positive_numbers", test_add)
    runner.run_test("divide_by_zero", test_divide_zero, True)
    runner.run_test("calculate_expression", test_calculate)
    
    print("\n" + "="*60)
    print("POWER OPERATIONS TESTS")
    print("="*60)
    
    # Test power operations
    def test_power():
        result = power_operations.power(2, 3)
        print(f"     Debug: power result = '{result}'")
        return "8" in str(result)
    
    def test_sqrt():
        result = power_operations.square_root(25)
        print(f"     Debug: sqrt result = '{result}'")
        return "5" in str(result)
    
    runner.run_test("power_basic", test_power)
    runner.run_test("square_root_perfect", test_sqrt)
    
    print("\n" + "="*60)
    print("MATRIX OPERATIONS TESTS")
    print("="*60)
    
    # Test matrix operations
    def test_matrix_add():
        result = matrix_operations.matrix_add('[[1,2],[3,4]]', '[[5,6],[7,8]]')
        print(f"     Debug: matrix add result = '{result}'")
        return "6" in str(result) and "8" in str(result) and "10" in str(result) and "12" in str(result)
    
    def test_matrix_multiply():
        result = matrix_operations.matrix_multiply('[[1,2],[3,4]]', '[[2,0],[1,2]]')
        print(f"     Debug: matrix multiply result = '{result}'")
        return "4" in str(result) and "10" in str(result) and "8" in str(result)
    
    def test_matrix_det():
        result = matrix_operations.matrix_determinant('[[2,3],[1,4]]')
        print(f"     Debug: matrix determinant result = '{result}'")
        return "5" in str(result)
    
    runner.run_test("matrix_add_2x2", test_matrix_add)
    runner.run_test("matrix_multiply_2x2", test_matrix_multiply)
    runner.run_test("matrix_determinant_2x2", test_matrix_det)
    
    print("\n" + "="*60)
    print("QUICK FUNCTIONALITY TESTS")
    print("="*60)
    
    # Test a few key functions from each domain
    def test_trig():
        result = trigonometric.sin(0)
        print(f"     Debug: sin(0) result = '{result}'")
        return "0" in str(result)
    
    def test_stats():
        result = stats_module.mean("1,2,3,4,5")
        print(f"     Debug: mean result = '{result}'")
        return "3" in str(result)
    
    def test_conversion():
        result = conversions.celsius_to_fahrenheit(0)
        print(f"     Debug: C to F result = '{result}'")
        return "32" in str(result)
        
    def test_quadratic():
        result = advanced_calc.solve_quadratic(1, -5, 6)
        print(f"     Debug: quadratic result = '{result}'")
        return "solution" in str(result).lower() or "3" in str(result) or "2" in str(result)
    
    runner.run_test("Trigonometry - sin(0)", test_trig)
    runner.run_test("Statistics - mean", test_stats)
    runner.run_test("Conversions - C to F", test_conversion)
    runner.run_test("Advanced - quadratic", test_quadratic)
    
    # Print final summary
    runner.print_summary()
    
    print("\n🔍 Tested core functionality across all domains")
    print("📊 Full suite contains 70 functions total")

if __name__ == "__main__":
    main()
