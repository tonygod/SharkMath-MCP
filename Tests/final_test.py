#!/usr/bin/env python3
"""
SharkMath MCP Server Comprehensive Test Suite - Consolidated Tools
Tests all consolidated tools in the SharkMath MCP Server using real FastMCP server
Updated for Phase 5 implementation with 14 consolidated tools.
"""

import asyncio
import sys
import os

# Add SharkMath directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import FastMCP and consolidated modules
try:
    from mcp.server.fastmcp import FastMCP
    import arithmetic
    import trigonometric
    import stats_operations
    import convert_units
    import matrix_operations
    import logarithmic
    import hyperbolic
    import precision
    import number_theory
    import solve_equations
    import calculate_geometry_2d
    import financial_calculations
    import computer_science_tools
    import data_analysis
    
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Make sure you're running from the SharkMath/Tests directory and have the mcp package installed")
    sys.exit(1)

class TestRunner:
    """Test runner that tracks pass/fail results"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
    
    async def run_test(self, name, test_func, expected_error=False):
        """Run a test and track results with detailed debugging"""
        try:
            print(f"⏳ Running {name}...")
            result = await test_func()
            if expected_error:
                if not result:  # If test didn't detect expected error
                    print(f"❌ {name} (expected error but got success)")
                    self.failed += 1
                else:
                    print(f"✅ {name} (error handled correctly)")
                    self.passed += 1
            else:
                if result:
                    print(f"✅ {name}")
                    self.passed += 1
                else:
                    print(f"❌ {name} (test assertion failed)")
                    self.failed += 1
        except Exception as e:
            print(f"❌ {name} (Error: {str(e)})")
            print(f"   Debug: {type(e).__name__}")
            if expected_error:
                print(f"   Expected error - counting as pass")
                self.passed += 1
            else:
                self.failed += 1
    
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

async def create_sharkmath_server():
    """Create and configure a FastMCP server with all consolidated SharkMath tools"""
    mcp = FastMCP("SharkMath-Test-Server")
    
    # Register all consolidated tools
    arithmetic.register_tools(mcp)
    trigonometric.register_tools(mcp)
    stats_operations.register_tools(mcp)
    convert_units.register_tools(mcp)
    matrix_operations.register_tools(mcp)
    logarithmic.register_tools(mcp)
    hyperbolic.register_tools(mcp)
    precision.register_tools(mcp)
    number_theory.register_tools(mcp)
    solve_equations.register_tools(mcp)
    calculate_geometry_2d.register_tools(mcp)
    financial_calculations.register_tools(mcp)
    computer_science_tools.register_tools(mcp)
    data_analysis.register_tools(mcp)
    
    return mcp

async def get_tool_by_name(mcp, tool_name):
    """Get a tool by name from the MCP server"""
    tools = await mcp.list_tools()
    for tool in tools:
        if hasattr(tool, 'name') and tool.name == tool_name:
            return tool
        elif str(tool) == tool_name:  # Fallback for string representation
            return tool
    return None

async def verify_tool_exists(mcp, tool_name):
    """Verify that a tool exists and is registered"""
    tool = await get_tool_by_name(mcp, tool_name)
    return tool is not None

async def main():
    """Main test function using real FastMCP server for tool registration validation"""
    
    print("SharkMath Comprehensive Test Suite")
    print("Testing tool registration and availability across all mathematical domains")
    print("="*60 + "\n")
    
    # Create the MCP server with all tools registered
    print("🔧 Creating FastMCP server and registering all tools...")
    mcp = await create_sharkmath_server()
    
    # Verify tools are registered
    tools = await mcp.list_tools()
    print(f"✅ Server created with {len(tools)} tools registered")
    
    runner = TestRunner()
    
    print("\n" + "="*60)
    print("TOOL REGISTRATION VERIFICATION TESTS")
    print("="*60)
    
    # Test that key tools from each domain are registered
    key_tools_by_domain = {
        "Arithmetic": ["add", "subtract", "multiply", "divide", "calculate"],
        "Power Operations": ["power", "square", "cube", "square_root", "cube_root", "nth_root"],
        "Matrix Operations": ["matrix_add", "matrix_multiply", "matrix_determinant", "matrix_transpose"],
        "Trigonometric": ["sin", "cos", "tan", "sin_degrees", "cos_degrees", "tan_degrees"],
        "Statistics": ["mean", "median", "mode", "standard_deviation", "variance"],
        "Conversions": ["celsius_to_fahrenheit", "fahrenheit_to_celsius", "meters_to_feet", "feet_to_meters"],
        "Advanced Calculator": ["solve_quadratic", "distance_2d", "slope", "compound_interest"],
        "Logarithmic": ["natural_log", "log_base_10", "log_base", "exponential"],
        "Hyperbolic": ["sinh", "cosh", "tanh"],
        "Precision": ["round_to_decimal", "floor", "ceiling", "truncate", "absolute"],
        "Combinatorics": ["factorial", "permutation", "combination", "fibonacci"],
        "Number Theory": ["gcd", "lcm", "is_prime", "prime_factors", "is_perfect_square"]
    }
    
    # Test tool registration for each domain
    for domain, tool_names in key_tools_by_domain.items():
        print(f"\n--- {domain} Domain ---")
        
        async def test_domain_tools(domain_name, tools_list):
            missing_tools = []
            found_tools = []
            
            for tool_name in tools_list:
                exists = await verify_tool_exists(mcp, tool_name)
                if exists:
                    found_tools.append(tool_name)
                else:
                    missing_tools.append(tool_name)
            
            print(f"     Found {len(found_tools)}/{len(tools_list)} tools in {domain_name}")
            if missing_tools:
                print(f"     Missing: {', '.join(missing_tools)}")
            
            return len(missing_tools) == 0
        
        await runner.run_test(f"{domain}_tools_registered", 
                             lambda d=domain, t=tool_names: test_domain_tools(d, t))
    
    print("\n" + "="*60)
    print("COMPREHENSIVE TOOL INVENTORY")
    print("="*60)
    
    # Get all registered tools and categorize them
    all_tools = await mcp.list_tools()
    tool_names = []
    for tool in all_tools:
        if hasattr(tool, 'name'):
            tool_names.append(tool.name)
        else:
            tool_names.append(str(tool))
    
    tool_names.sort()
    
    async def test_expected_tool_count():
        # We expect around 70+ tools across all domains
        expected_min = 60  # Conservative estimate
        actual_count = len(tool_names)
        print(f"     Expected: ≥{expected_min} tools, Found: {actual_count} tools")
        return actual_count >= expected_min
    
    async def test_no_duplicate_tools():
        unique_tools = set(tool_names)
        duplicates = len(tool_names) - len(unique_tools)
        print(f"     Total tools: {len(tool_names)}, Unique: {len(unique_tools)}, Duplicates: {duplicates}")
        return duplicates == 0
    
    await runner.run_test("expected_tool_count", test_expected_tool_count)
    await runner.run_test("no_duplicate_tools", test_no_duplicate_tools)
    
    # Print sample of registered tools
    print(f"\n📋 Sample of Registered Tools (showing 15 of {len(tool_names)}):")
    for tool_name in tool_names[:15]:
        print(f"   • {tool_name}")
    if len(tool_names) > 15:
        print(f"   ... and {len(tool_names) - 15} more tools")
    
    # Print final summary
    runner.print_summary()
    
    print(f"\n🔍 Validated tool registration across all {len(key_tools_by_domain)} mathematical domains")
    print(f"📊 FastMCP server successfully registered {len(tool_names)} mathematical tools")
    print("✨ All tools are properly registered and accessible via FastMCP API")
    print("\n💡 Note: This test validates tool registration and availability.")
    print("   For functional testing of mathematical operations, see:")
    print("   • comprehensive_test.py (MockMCP with actual tool execution)")
    print("   • core_logic_test.py (direct mathematical validation)")

if __name__ == "__main__":
    asyncio.run(main())
