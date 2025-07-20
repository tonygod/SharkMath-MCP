"""
Financial Calculations Module for SharkMath MCP Server

This module provides consolidated financial and business calculation functions including:
- Present value (PV) and Future value (FV) calculations
- Loan payment calculations (PMT)
- Return on Investment (ROI) analysis
- Depreciation calculations (straight-line, declining balance)
- Mortgage calculations
- Break-even analysis
- Cash flow analysis
- Compound and simple interest (migrated from solve_equations)

All functions follow the SharkMath error handling standards with ✅/❌ prefixes.
This is a consolidated tool using parameter-based routing.
"""

import math
from typing import Optional


def register_tools(mcp):
    """Register consolidated financial calculations tool with the MCP server."""
    
    @mcp.tool()
    async def financial_calculations(
        operation: str,
        principal: Optional[float] = None,
        rate: Optional[float] = None,
        time: Optional[float] = None,
        future_value: Optional[float] = None,
        present_value: Optional[float] = None,
        payment: Optional[float] = None,
        compounds_per_year: Optional[int] = None,
        initial_investment: Optional[float] = None,
        final_value: Optional[float] = None,
        cost_basis: Optional[float] = None,
        salvage_value: Optional[float] = None,
        useful_life: Optional[float] = None,
        declining_rate: Optional[float] = None,
        fixed_costs: Optional[float] = None,
        variable_cost_per_unit: Optional[float] = None,
        price_per_unit: Optional[float] = None,
        cash_flows: Optional[str] = None,
        discount_rate: Optional[float] = None
    ) -> str:
        """
        Perform various financial and business calculations.
        
        Args:
            operation: Type of calculation - "present_value", "future_value", "loan_payment", 
                      "roi", "straight_line_depreciation", "declining_balance_depreciation",
                      "mortgage_payment", "break_even_point", "net_present_value", 
                      "compound_interest", "simple_interest"
            principal: Initial amount for interest/loan calculations
            rate: Interest rate as decimal (e.g., 0.05 for 5%)
            time: Time period in years
            future_value: Future value for PV calculations
            present_value: Present value for FV calculations  
            payment: Payment amount for loan calculations
            compounds_per_year: Compounding frequency per year (default 1)
            initial_investment: Initial investment for ROI calculations
            final_value: Final value for ROI calculations
            cost_basis: Asset cost for depreciation
            salvage_value: Asset value at end of useful life
            useful_life: Asset useful life in years
            declining_rate: Declining balance depreciation rate
            fixed_costs: Fixed costs for break-even analysis
            variable_cost_per_unit: Variable cost per unit
            price_per_unit: Selling price per unit
            cash_flows: JSON string of cash flows for NPV (e.g., "[100, 200, 300]")
            discount_rate: Discount rate for NPV calculations
            
        Returns:
            String with calculation results and detailed breakdown
        """
        
        # Define valid operations
        valid_operations = {
            "present_value": _present_value,
            "future_value": _future_value,
            "loan_payment": _loan_payment,
            "roi": _return_on_investment,
            "straight_line_depreciation": _straight_line_depreciation,
            "declining_balance_depreciation": _declining_balance_depreciation,
            "mortgage_payment": _mortgage_payment,
            "break_even_point": _break_even_point,
            "net_present_value": _net_present_value,
            "compound_interest": _compound_interest,
            "simple_interest": _simple_interest
        }
        
        # Validate operation
        if operation not in valid_operations:
            valid_ops = ", ".join(valid_operations.keys())
            return f"❌ Invalid operation '{operation}'. Valid operations: {valid_ops}"
        
        try:
            # Route to appropriate function
            return valid_operations[operation](
                principal=principal, rate=rate, time=time,
                future_value=future_value, present_value=present_value,
                payment=payment, compounds_per_year=compounds_per_year,
                initial_investment=initial_investment, final_value=final_value,
                cost_basis=cost_basis, salvage_value=salvage_value,
                useful_life=useful_life, declining_rate=declining_rate,
                fixed_costs=fixed_costs, variable_cost_per_unit=variable_cost_per_unit,
                price_per_unit=price_per_unit, cash_flows=cash_flows,
                discount_rate=discount_rate
            )
            
        except Exception as e:
            return f"❌ Error in {operation} calculation: {str(e)}"


def _present_value(future_value: Optional[float], rate: Optional[float], time: Optional[float], 
                  compounds_per_year: Optional[int] = None, **kwargs) -> str:
    """
    Calculate present value: PV = FV / (1 + r/n)^(nt)
    """
    if future_value is None or rate is None or time is None:
        return "❌ Present value requires parameters: future_value, rate, time"
    
    if compounds_per_year is None:
        compounds_per_year = 1
    
    # Input validation
    if future_value < 0:
        return "❌ Future value cannot be negative"
    if rate < 0:
        return "❌ Interest rate cannot be negative"
    if time < 0:
        return "❌ Time period cannot be negative"
    if compounds_per_year <= 0:
        return "❌ Compounds per year must be positive"
    
    # Calculate present value
    present_value = future_value / ((1 + rate / compounds_per_year) ** (compounds_per_year * time))
    rate_percent = rate * 100
    
    return (f"✅ Present Value Calculation:\n"
           f"   Future Value: ${future_value:,.2f}\n"
           f"   Rate: {rate_percent}% compounded {compounds_per_year}x/year\n"
           f"   Time: {time} years\n"
           f"   Present Value: ${present_value:,.2f}")


def _future_value(present_value: Optional[float], rate: Optional[float], time: Optional[float],
                 compounds_per_year: Optional[int] = None, **kwargs) -> str:
    """
    Calculate future value: FV = PV * (1 + r/n)^(nt)
    """
    if present_value is None or rate is None or time is None:
        return "❌ Future value requires parameters: present_value, rate, time"
    
    if compounds_per_year is None:
        compounds_per_year = 1
    
    # Input validation
    if present_value < 0:
        return "❌ Present value cannot be negative"
    if rate < 0:
        return "❌ Interest rate cannot be negative"
    if time < 0:
        return "❌ Time period cannot be negative"
    if compounds_per_year <= 0:
        return "❌ Compounds per year must be positive"
    
    # Calculate future value
    future_value = present_value * ((1 + rate / compounds_per_year) ** (compounds_per_year * time))
    rate_percent = rate * 100
    growth = future_value - present_value
    
    return (f"✅ Future Value Calculation:\n"
           f"   Present Value: ${present_value:,.2f}\n"
           f"   Rate: {rate_percent}% compounded {compounds_per_year}x/year\n"
           f"   Time: {time} years\n"
           f"   Future Value: ${future_value:,.2f}\n"
           f"   Growth: ${growth:,.2f}")


def _loan_payment(principal: Optional[float], rate: Optional[float], time: Optional[float],
                 compounds_per_year: Optional[int] = None, **kwargs) -> str:
    """
    Calculate loan payment: PMT = P * [r(1+r)^n] / [(1+r)^n - 1]
    """
    if principal is None or rate is None or time is None:
        return "❌ Loan payment requires parameters: principal, rate, time"
    
    if compounds_per_year is None:
        compounds_per_year = 12  # Monthly payments by default
    
    # Input validation
    if principal <= 0:
        return "❌ Principal amount must be positive"
    if rate < 0:
        return "❌ Interest rate cannot be negative"
    if time <= 0:
        return "❌ Time period must be positive"
    if compounds_per_year <= 0:
        return "❌ Compounds per year must be positive"
    
    # Convert to periodic rate and number of payments
    periodic_rate = rate / compounds_per_year
    num_payments = compounds_per_year * time
    
    if rate == 0:
        # No interest loan
        payment = principal / num_payments
        total_payments = principal
        total_interest = 0
    else:
        # Calculate payment using loan payment formula
        payment = principal * (periodic_rate * (1 + periodic_rate)**num_payments) / ((1 + periodic_rate)**num_payments - 1)
        total_payments = payment * num_payments
        total_interest = total_payments - principal
    
    rate_percent = rate * 100
    
    return (f"✅ Loan Payment Calculation:\n"
           f"   Principal: ${principal:,.2f}\n"
           f"   Rate: {rate_percent}% APR\n"
           f"   Term: {time} years ({int(num_payments)} payments)\n"
           f"   Payment: ${payment:,.2f}\n"
           f"   Total Payments: ${total_payments:,.2f}\n"
           f"   Total Interest: ${total_interest:,.2f}")


def _return_on_investment(initial_investment: Optional[float], final_value: Optional[float], **kwargs) -> str:
    """
    Calculate ROI: ROI = (Final Value - Initial Investment) / Initial Investment * 100%
    """
    if initial_investment is None or final_value is None:
        return "❌ ROI requires parameters: initial_investment, final_value"
    
    # Input validation
    if initial_investment <= 0:
        return "❌ Initial investment must be positive"
    
    # Calculate ROI
    gain_loss = final_value - initial_investment
    roi = (gain_loss / initial_investment) * 100
    
    return (f"✅ Return on Investment Calculation:\n"
           f"   Initial Investment: ${initial_investment:,.2f}\n"
           f"   Final Value: ${final_value:,.2f}\n"
           f"   Gain/Loss: ${gain_loss:,.2f}\n"
           f"   ROI: {roi:.2f}%")


def _straight_line_depreciation(cost_basis: Optional[float], salvage_value: Optional[float], 
                               useful_life: Optional[float], **kwargs) -> str:
    """
    Calculate straight-line depreciation: Annual Depreciation = (Cost - Salvage Value) / Useful Life
    """
    if cost_basis is None or salvage_value is None or useful_life is None:
        return "❌ Straight-line depreciation requires parameters: cost_basis, salvage_value, useful_life"
    
    # Input validation
    if cost_basis < 0:
        return "❌ Cost basis cannot be negative"
    if salvage_value < 0:
        return "❌ Salvage value cannot be negative"
    if useful_life <= 0:
        return "❌ Useful life must be positive"
    if salvage_value > cost_basis:
        return "❌ Salvage value cannot exceed cost basis"
    
    # Calculate depreciation
    depreciable_amount = cost_basis - salvage_value
    annual_depreciation = depreciable_amount / useful_life
    
    return (f"✅ Straight-Line Depreciation:\n"
           f"   Cost Basis: ${cost_basis:,.2f}\n"
           f"   Salvage Value: ${salvage_value:,.2f}\n"
           f"   Useful Life: {useful_life} years\n"
           f"   Depreciable Amount: ${depreciable_amount:,.2f}\n"
           f"   Annual Depreciation: ${annual_depreciation:,.2f}")


def _declining_balance_depreciation(cost_basis: Optional[float], declining_rate: Optional[float],
                                  useful_life: Optional[float], **kwargs) -> str:
    """
    Calculate declining balance depreciation for first year: Depreciation = Cost Basis * Declining Rate
    """
    if cost_basis is None or declining_rate is None or useful_life is None:
        return "❌ Declining balance depreciation requires parameters: cost_basis, declining_rate, useful_life"
    
    # Input validation  
    if cost_basis < 0:
        return "❌ Cost basis cannot be negative"
    if declining_rate <= 0 or declining_rate > 1:
        return "❌ Declining rate must be between 0 and 1 (e.g., 0.2 for 20%)"
    if useful_life <= 0:
        return "❌ Useful life must be positive"
    
    # Calculate first year depreciation
    first_year_depreciation = cost_basis * declining_rate
    remaining_value = cost_basis - first_year_depreciation
    rate_percent = declining_rate * 100
    
    return (f"✅ Declining Balance Depreciation (Year 1):\n"
           f"   Cost Basis: ${cost_basis:,.2f}\n"
           f"   Declining Rate: {rate_percent}%\n"
           f"   Useful Life: {useful_life} years\n"
           f"   Year 1 Depreciation: ${first_year_depreciation:,.2f}\n"
           f"   Remaining Book Value: ${remaining_value:,.2f}")


def _mortgage_payment(principal: Optional[float], rate: Optional[float], time: Optional[float], **kwargs) -> str:
    """
    Calculate monthly mortgage payment (specialized loan payment for real estate)
    """
    if principal is None or rate is None or time is None:
        return "❌ Mortgage payment requires parameters: principal, rate, time"
    
    # Input validation
    if principal <= 0:
        return "❌ Principal amount must be positive"
    if rate < 0:
        return "❌ Interest rate cannot be negative"
    if time <= 0:
        return "❌ Time period must be positive"
    
    # Convert to monthly rate and payments
    monthly_rate = rate / 12
    num_payments = time * 12
    
    if rate == 0:
        # No interest mortgage
        monthly_payment = principal / num_payments
        total_payments = principal
        total_interest = 0
    else:
        # Calculate monthly payment
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
        total_payments = monthly_payment * num_payments
        total_interest = total_payments - principal
    
    rate_percent = rate * 100
    
    return (f"✅ Mortgage Payment Calculation:\n"
           f"   Loan Amount: ${principal:,.2f}\n"
           f"   Interest Rate: {rate_percent}% APR\n"
           f"   Term: {time} years\n"
           f"   Monthly Payment: ${monthly_payment:,.2f}\n"
           f"   Total Payments: ${total_payments:,.2f}\n"
           f"   Total Interest: ${total_interest:,.2f}")


def _break_even_point(fixed_costs: Optional[float], variable_cost_per_unit: Optional[float],
                     price_per_unit: Optional[float], **kwargs) -> str:
    """
    Calculate break-even point in units: Break-even = Fixed Costs / (Price per Unit - Variable Cost per Unit)
    """
    if fixed_costs is None or variable_cost_per_unit is None or price_per_unit is None:
        return "❌ Break-even analysis requires parameters: fixed_costs, variable_cost_per_unit, price_per_unit"
    
    # Input validation
    if fixed_costs < 0:
        return "❌ Fixed costs cannot be negative"
    if variable_cost_per_unit < 0:
        return "❌ Variable cost per unit cannot be negative"
    if price_per_unit <= 0:
        return "❌ Price per unit must be positive"
    if price_per_unit <= variable_cost_per_unit:
        return "❌ Price per unit must be greater than variable cost per unit"
    
    # Calculate break-even point
    contribution_margin = price_per_unit - variable_cost_per_unit
    break_even_units = fixed_costs / contribution_margin
    break_even_revenue = break_even_units * price_per_unit
    
    return (f"✅ Break-Even Analysis:\n"
           f"   Fixed Costs: ${fixed_costs:,.2f}\n"
           f"   Variable Cost per Unit: ${variable_cost_per_unit:.2f}\n"
           f"   Price per Unit: ${price_per_unit:.2f}\n"
           f"   Contribution Margin: ${contribution_margin:.2f}\n"
           f"   Break-Even Point: {break_even_units:,.0f} units\n"
           f"   Break-Even Revenue: ${break_even_revenue:,.2f}")


def _net_present_value(cash_flows: Optional[str], discount_rate: Optional[float], **kwargs) -> str:
    """
    Calculate Net Present Value of cash flows: NPV = Σ(CF_t / (1 + r)^t)
    """
    if cash_flows is None or discount_rate is None:
        return "❌ NPV requires parameters: cash_flows (JSON array), discount_rate"
    
    # Parse cash flows
    try:
        import json
        cash_flow_list = json.loads(cash_flows)
        if not isinstance(cash_flow_list, list):
            return "❌ cash_flows must be a JSON array (e.g., '[100, 200, 300]')"
    except json.JSONDecodeError:
        return "❌ Invalid JSON format for cash_flows. Use format: '[100, 200, 300]'"
    
    # Input validation
    if discount_rate < 0:
        return "❌ Discount rate cannot be negative"
    if len(cash_flow_list) == 0:
        return "❌ At least one cash flow value is required"
    
    # Calculate NPV
    npv = 0
    for t, cash_flow in enumerate(cash_flow_list):
        if not isinstance(cash_flow, (int, float)):
            return f"❌ All cash flows must be numbers, found {type(cash_flow).__name__} at position {t}"
        discounted_value = cash_flow / ((1 + discount_rate) ** (t + 1))
        npv += discounted_value
    
    rate_percent = discount_rate * 100
    
    # Format cash flows for display
    cash_flows_str = ", ".join([f"${cf:,.2f}" for cf in cash_flow_list])
    
    return (f"✅ Net Present Value Calculation:\n"
           f"   Cash Flows: [{cash_flows_str}]\n"
           f"   Discount Rate: {rate_percent}%\n"
           f"   Number of Periods: {len(cash_flow_list)}\n"
           f"   Net Present Value: ${npv:,.2f}")


def _compound_interest(principal: Optional[float], rate: Optional[float], time: Optional[float], 
                      compounds_per_year: Optional[int] = None, **kwargs) -> str:
    """
    Calculate compound interest using the formula: A = P(1 + r/n)^(nt)
    Migrated from solve_equations.py for financial calculations consolidation.
    """
    # Validate required parameters
    if principal is None or rate is None or time is None:
        return "❌ Compound interest requires parameters: principal, rate, time"
    
    # Default compounding frequency
    if compounds_per_year is None:
        compounds_per_year = 1
    
    # Input validation
    if principal < 0:
        return "❌ Principal amount cannot be negative"
    
    if rate < 0:
        return "❌ Interest rate cannot be negative"
        
    if time < 0:
        return "❌ Time period cannot be negative"
        
    if compounds_per_year <= 0:
        return "❌ Compounds per year must be positive integer"
    
    # Calculate compound interest
    # A = P(1 + r/n)^(nt)
    final_amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    interest_earned = final_amount - principal
    
    # Convert rate to percentage for display
    rate_percent = rate * 100
    
    # Determine compounding frequency description
    if compounds_per_year == 1:
        frequency = "annually"
    elif compounds_per_year == 2:
        frequency = "semi-annually"
    elif compounds_per_year == 4:
        frequency = "quarterly"
    elif compounds_per_year == 12:
        frequency = "monthly"
    elif compounds_per_year == 365:
        frequency = "daily"
    else:
        frequency = f"{compounds_per_year} times per year"
    
    return (f"✅ Compound Interest Calculation:\n"
           f"   Principal: ${principal:,.2f}\n"
           f"   Rate: {rate_percent}% compounded {frequency}\n"
           f"   Time: {time} years\n"
           f"   Final Amount: ${final_amount:,.2f}\n"
           f"   Interest Earned: ${interest_earned:,.2f}")


def _simple_interest(principal: Optional[float], rate: Optional[float], time: Optional[float], **kwargs) -> str:
    """
    Calculate simple interest using the formula: I = P × r × t, A = P + I
    Migrated from solve_equations.py for financial calculations consolidation.
    """
    # Validate required parameters
    if principal is None or rate is None or time is None:
        return "❌ Simple interest requires parameters: principal, rate, time"
    
    # Input validation
    if principal < 0:
        return "❌ Principal amount cannot be negative"
    
    if rate < 0:
        return "❌ Interest rate cannot be negative"
        
    if time < 0:
        return "❌ Time period cannot be negative"
    
    # Calculate simple interest
    # I = P × r × t
    interest_earned = principal * rate * time
    final_amount = principal + interest_earned
    
    # Convert rate to percentage for display
    rate_percent = rate * 100
    
    return (f"✅ Simple Interest Calculation:\n"
           f"   Principal: ${principal:,.2f}\n"
           f"   Rate: {rate_percent}% per year\n"
           f"   Time: {time} years\n"
           f"   Final Amount: ${final_amount:,.2f}\n"
           f"   Interest Earned: ${interest_earned:,.2f}")


# Support for direct execution (testing)
if __name__ == "__main__":
    print("Financial Calculations Functions Test")
    print("=" * 40)
    
    # Test cases would go here for development
    print("This module should be imported by sharkmath_server.py")
