# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio


# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    save_csv_path = Path('./data/output/qualifying_loans.csv')
    test = ["testing"]
    save_csv(save_csv_path,"file", test)
    assert save_csv_path.exists()

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    filtered_loans = max_loan_size(loan, bank_data)
  
    filtered_loans = credit_score(current_credit_score, filtered_loans)

    filtered_loans = loan_to_value(loan_to_value_ratio,filtered_loans)

    filtered_loans = debt_to_income(monthly_debt_ratio, filtered_loans)

    #Is the loan showing up as expected
    assert len(filtered_loans)==6

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
