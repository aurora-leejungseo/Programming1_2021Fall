## This week

# str.join()
# str.replace()
# str. strip()
# use list.pop()
# use list.reverse() : change the order of the list
# use f-strings()

# START LAB EXERCISE 02
print('Lab Exercise 02 \n')

companies = 'Ford, 11.54; Honda, 29.82; General Motors Company, 57.22; Toyota, 150.77; Tesla, 709.44'
#  string with different motor companies followed by their stock prices


# PROBLEM 1 (4 points): replace the puctuation ',' with ':'

company_stocks = companies.replace(',',':')

print(company_stocks)


# PROBLEM 2 (4 points): creating a list by splitting the string called automotive_stock


automotive_stocks = company_stocks.split('; ')
print(automotive_stocks)

# PROBLEM 3 (4 points): use len, # of elements in this list, 
companies_num = len(automotive_stocks)
print(companies_num)

# PROBLEM 4 (4 points): building an formatted string literal (f-string)
## example of f-string
## f_string: f"My favorite Michigan basketball player if {favorite)basketball_player}"

statement = f"In this list, there are {companies_num} automotive companies and their stock prices on May 1st, 2021."
print(statement)


# PROBLEM 5 (4 points): list slicing, assign first three companies + their stock prices

three_lowest_companies = automotive_stocks[0:3]
print(three_lowest_companies)

# END LAB EXERCISE



