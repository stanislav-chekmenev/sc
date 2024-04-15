# Income taxes
INCOME_TAX = 0.42 # income tax rate for salaries above 66760 Euro/year
INCOME_THRESHOLD = 10600 # used in the calculation of the income tax
VAT = 0.19 # value-added tax rate for self-employed
ADD_SP_TAX = 0.03 # additional trade tax rate for self-employed 
SOL_TAX = 0.05 # solidarity tax rate for self-employed

# Social security contributions
HEALTH_MAX = 993 # max health insurance contribution (capped at 84600 Euro/year)
RETIRE_MAX = 1311 # max retirement contribution (capped at 84600 Euro/year)
UNEMP_MAX= 170 # unemployment contribution rate


def estimate_net_salary(salary, self_employed=True):
    if self_employed:
        additional_income_tax_cash = salary * (VAT + ADD_SP_TAX)
        sum_social_security = HEALTH_MAX * 12 + RETIRE_MAX * 12 + UNEMP_MAX * 12
        income_tax_cash = (salary - sum_social_security) * INCOME_TAX - INCOME_THRESHOLD
        sol_tax_cash = income_tax_cash * SOL_TAX
    else:
        additional_income_tax_cash = 0
        sum_social_security = (HEALTH_MAX * 12 + RETIRE_MAX * 12 + UNEMP_MAX * 12) / 2 # half paid by the employer
        income_tax_cash = (salary - sum_social_security) * INCOME_TAX - INCOME_THRESHOLD
        sol_tax_cash = income_tax_cash * SOL_TAX

    net_salary = salary - income_tax_cash - sol_tax_cash - additional_income_tax_cash - sum_social_security
    return round(net_salary, 0)