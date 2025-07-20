#!/usr/bin/env python3
"""
SharkMath Test Runner

Comprehensive testing suite for all SharkMath MCP server modules.
Tests all 70 mathematical functions across 12 domains with edge cases.
"""

import asyncio
import json
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

# Import all test modules (consolidated tools after refactoring)
from test_calculate_arithmetic import TestCalculateArithmetic
from test_calculate_trigonometry import TestCalculateTrigonometry
from test_calculate_statistics import TestCalculateStatistics
from test_calculate_logarithmic import TestCalculateLogarithmic
from test_calculate_hyperbolic import TestCalculateHyperbolic
from test_format_precision import TestFormatPrecision
from test_analyze_numbers import TestAnalyzeNumbers
from test_conversions import TestConversions
# Phase 4 consolidated test files
from test_solve_equations import TestSolveEquations
from test_calculate_geometry_2d import TestCalculateGeometry2D
from test_manipulate_matrices import TestManipulateMatrices


class TestRunner:
    """Main test runner for all SharkMath modules."""
    
    def __init__(self):
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.test_results = []
    
    def run_test_class(self, test_class):
        """Run all tests in a test class."""
        class_name = test_class.__class__.__name__
        print(f"\n{'='*60}")
        print(f"Running {class_name}")
        print(f"{'='*60}")
        
        class_passed = 0
        class_total = 0
        
        # Get all test methods
        test_methods = [method for method in dir(test_class) if method.startswith('test_')]
        
        for test_method_name in test_methods:
            test_method = getattr(test_class, test_method_name)
            if callable(test_method):
                class_total += 1
                self.total_tests += 1
                
                try:
                    # Run the test
                    if asyncio.iscoroutinefunction(test_method):
                        result = asyncio.run(test_method())
                    else:
                        result = test_method()
                    
                    if result:
                        print(f"✅ {test_method_name}")
                        class_passed += 1
                        self.passed_tests += 1
                    else:
                        print(f"❌ {test_method_name}")
                        self.failed_tests += 1
                        
                except Exception as e:
                    print(f"❌ {test_method_name} - Exception: {str(e)}")
                    self.failed_tests += 1
        
        success_rate = (class_passed / class_total * 100) if class_total > 0 else 0
        print(f"\n{class_name} Results: {class_passed}/{class_total} passed ({success_rate:.1f}%)")
        
        self.test_results.append({
            'class': class_name,
            'passed': class_passed,
            'total': class_total,
            'success_rate': success_rate
        })
    
    def print_summary(self):
        """Print final test summary."""
        print(f"\n{'='*60}")
        print(f"FINAL TEST SUMMARY")
        print(f"{'='*60}")
        
        for result in self.test_results:
            print(f"{result['class']:<25} {result['passed']:>3}/{result['total']:<3} ({result['success_rate']:>5.1f}%)")
        
        overall_success_rate = (self.passed_tests / self.total_tests * 100) if self.total_tests > 0 else 0
        
        print(f"\n{'='*60}")
        print(f"OVERALL RESULTS:")
        print(f"Total Tests: {self.total_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        print(f"Success Rate: {overall_success_rate:.1f}%")
        print(f"{'='*60}")
        
        if self.failed_tests == 0:
            print("🎉 ALL TESTS PASSED! SharkMath server is fully functional!")
        else:
            print(f"⚠️  {self.failed_tests} tests failed. Please review the issues above.")
        
        return self.failed_tests == 0


def main():
    """Run all SharkMath tests."""
    print("SharkMath Comprehensive Test Suite")
    print(f"Testing all 70 functions across 12 mathematical domains")
    print(f"{'='*60}")
    
    runner = TestRunner()
    
    # Initialize all test classes (consolidated tools after refactoring)
    test_classes = [
        TestCalculateArithmetic(),
        TestCalculateTrigonometry(),
        TestCalculateStatistics(),
        TestCalculateLogarithmic(),
        TestCalculateHyperbolic(),
        TestFormatPrecision(),
        TestAnalyzeNumbers(),
        TestConversions(),
        # Phase 4 consolidated tools
        TestSolveEquations(),
        TestCalculateGeometry2D(),
        TestManipulateMatrices()
    ]
    
    # Run all test classes
    for test_class in test_classes:
        runner.run_test_class(test_class)
    
    # Print final summary
    success = runner.print_summary()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
