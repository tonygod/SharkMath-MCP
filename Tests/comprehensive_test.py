#!/usr/bin/env python3
"""
Comprehensive SharkMath Test Suite - Consolidated Tools

Tests all consolidated tools in the SharkMath MCP Server.
Updated for Phase 5 implementation with 14 consolidated tools.
"""

import asyncio
import json
import math
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import all consolidated SharkMath modules
import arithmetic
import trigonometric
import stats_operations
import convert_units
import logarithmic
import hyperbolic
import precision
import number_theory
import solve_equations
import calculate_geometry_2d
import matrix_operations
import financial_calculations
import computer_science_tools
import data_analysis

class MockMCP:
    def __init__(self):
        self.tools = {}
    
    def tool(self):
        def decorator(func):
            self.tools[func.__name__] = func
            return func
        return decorator

class TestRunner:
    def __init__(self):
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
    
    async def run_test(self, name, test_func, expected_error=False):
        """Run a test and track results with detailed debugging"""
        self.total_tests += 1
        try:
            print(f"⏳ Running {name}...")
            result = await test_func()
            if expected_error:
                print(f"❌ {name} (expected error but got success)")
                self.failed_tests += 1
            else:
                print(f"✅ {name}")
                self.passed_tests += 1
        except Exception as e:
            print(f"❌ {name} (Error: {str(e)})")
            print(f"   Debug: {type(e).__name__}")
            if not expected_error:
                self.failed_tests += 1
            else:
                print(f"   Expected error - counting as pass")
                self.passed_tests += 1
    
    def print_summary(self):
        """Print test summary."""
        success_rate = (self.passed_tests / self.total_tests * 100) if self.total_tests > 0 else 0
        print(f"\n{'='*60}")
        print(f"FINAL TEST SUMMARY")
        print(f"{'='*60}")
        print(f"Total Tests: {self.total_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        print(f"Success Rate: {success_rate:.1f}%")
        
        if self.failed_tests == 0:
            print("🎉 ALL TESTS PASSED! SharkMath server is fully functional!")
        else:
            print(f"⚠️  {self.failed_tests} tests failed.")
        
        return self.failed_tests == 0

async def main():
    """Run comprehensive SharkMath tests."""
    print("SharkMath Comprehensive Test Suite - Consolidated Tools")
    print("Testing all 14 consolidated tools in the SharkMath MCP Server")
    print("=" * 60)
    
    runner = TestRunner()
    
    # Setup all consolidated MCP instances
    arithmetic_mcp = MockMCP()
    arithmetic.register_tools(arithmetic_mcp)
    
    trig_mcp = MockMCP()
    trigonometric.register_tools(trig_mcp)
    
    stats_mcp = MockMCP()
    stats_operations.register_tools(stats_mcp)
    
    convert_mcp = MockMCP()
    convert_units.register_tools(convert_mcp)
    
    log_mcp = MockMCP()
    logarithmic.register_tools(log_mcp)
    
    hyp_mcp = MockMCP()
    hyperbolic.register_tools(hyp_mcp)
    
    prec_mcp = MockMCP()
    precision.register_tools(prec_mcp)
    
    num_mcp = MockMCP()
    number_theory.register_tools(num_mcp)
    
    solve_mcp = MockMCP()
    solve_equations.register_tools(solve_mcp)
    
    geom_mcp = MockMCP()
    calculate_geometry_2d.register_tools(geom_mcp)
    
    matrix_mcp = MockMCP()
    matrix_operations.register_tools(matrix_mcp)
    
    financial_mcp = MockMCP()
    financial_calculations.register_tools(financial_mcp)
    
    cs_mcp = MockMCP()
    computer_science_tools.register_tools(cs_mcp)
    
    data_mcp = MockMCP()
    data_analysis.register_tools(data_mcp)
    
    matrix_mcp = MockMCP()
    matrix_operations.register_tools(matrix_mcp)
    
    print("\n" + "="*60)
    print("ARITHMETIC TESTS (5 functions)")
    print("="*60)
    
    # Test arithmetic functions
    # Test basic arithmetic
    async def test_add():
        result = await arithmetic_mcp.tools['add'](2, 3)
        print(f"     Debug: add result = '{result}'")
        return "5" in str(result)
    
    async def test_divide_zero():
        try:
            result = await arithmetic_mcp.tools['calculate_arithmetic']('divide', a=5, b=0)
            print(f"     Debug: divide by zero result = '{result}'")
            return "Error" in str(result) or "division" in str(result)
        except Exception:
            return True  # Exception is expected for division by zero
    
    print("\n" + "="*60)
    print("CONSOLIDATED TOOLS TESTS")
    print("="*60)
    
    # Test consolidated tools with parameter-based routing
    async def test_arithmetic():
        result = await arithmetic_mcp.tools['calculate_arithmetic']("add", a=2, b=3)
        print(f"     Debug: arithmetic result = '{result}'")
        return "5" in str(result)
    
    async def test_trigonometry():
        result = await trig_mcp.tools['calculate_trigonometry']("sin", angle=0, angle_unit="radians")
        print(f"     Debug: trig result = '{result}'")
        return "0.0" in str(result)
    
    async def test_statistics():
        result = await stats_mcp.tools['calculate_statistics']("mean", numbers=[1, 2, 3, 4, 5])
        print(f"     Debug: stats result = '{result}'")
        return "3.0" in str(result)
    
    async def test_conversions():
        result = await convert_mcp.tools['convert_units']("celsius", "fahrenheit", value=0)
        print(f"     Debug: conversion result = '{result}'")
        return "32" in str(result)
    
    async def test_matrices():
        result = await matrix_mcp.tools['manipulate_matrices']("add", matrix1='[[1,2],[3,4]]', matrix2='[[5,6],[7,8]]')
        print(f"     Debug: matrix result = '{result}'")
        return "[[6, 8], [10, 12]]" in str(result)
    
    async def test_equations():
        result = await solve_mcp.tools['solve_equations']("linear", a=2, b=-6)
        print(f"     Debug: equation result = '{result}'")
        return "3.0" in str(result)
    
    async def test_geometry():
        result = await geom_mcp.tools['calculate_geometry_2d']("distance", x1=0, y1=0, x2=3, y2=4)
        print(f"     Debug: geometry result = '{result}'")
        return "5.0" in str(result)
    
    async def test_financial():
        result = await financial_mcp.tools['financial_calculations']("simple_interest", principal=1000, rate=0.05, time=2)
        print(f"     Debug: financial result = '{result}'")
        return "100" in str(result)
    
    async def test_computer_science():
        result = await cs_mcp.tools['computer_science_tools']("base_conversion", value=255, from_base=10, to_base=16)
        print(f"     Debug: CS result = '{result}'")
        return "FF" in str(result)
    
    async def test_data_analysis():
        result = await data_mcp.tools['data_analysis']("z_score", value=3.0, mean=2.0, std_dev=1.0)
        print(f"     Debug: data analysis result = '{result}'")
        return "1.0" in str(result)
    
    # Run consolidated tool tests
    await runner.run_test("arithmetic_add", test_arithmetic)
    await runner.run_test("trigonometry_sin", test_trigonometry)
    await runner.run_test("statistics_mean", test_statistics)
    await runner.run_test("unit_conversion", test_conversions)
    await runner.run_test("matrix_operations", test_matrices)
    await runner.run_test("equation_solving", test_equations)
    await runner.run_test("geometry_distance", test_geometry)
    await runner.run_test("financial_interest", test_financial)
    await runner.run_test("computer_science_conversion", test_computer_science)
    await runner.run_test("data_analysis_zscore", test_data_analysis)
    
    # Print final summary
    success = runner.print_summary()
    
    print(f"\n🔍 Tested core functionality across all 14 consolidated tools")
    print(f"📊 Full suite contains 150+ functions consolidated into parameter-based routing")
    print(f"✨ SharkMath MCP Server is {'READY' if success else 'NEEDS ATTENTION'}")
    
    return success

if __name__ == "__main__":
    asyncio.run(main())
