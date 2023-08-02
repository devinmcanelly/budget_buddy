

# Navigate workbook.

## Important cells
* [Bills!]B2:E22 Table, Recurring Monthly
* [Bills!]G2:F22 Table, Recurring Yearly
* [Bills!]L2:O22 Table, Estimates future
* [Transactions!]A:E Table, Transaction log

# Modify workbook
input daily report into transaction record.

# Roadmap, ala chatGPT
Absolutely, your plan sounds logical and well-structured. Here's a roadmap that breaks down the steps to get there:

### Phase 1: Basic Data Entry
<s>1. **Set Up Environment**: Ensure that you have all the necessary libraries installed (`openpyxl`, `pandas`, etc.).</s>

2. **Create a Function to Add Values to Spreadsheet**:
    - Write a Python function that takes in values (e.g., transaction amount, category, date) as parameters.
    - Use `openpyxl` to open your Excel file and add the values to the appropriate cells.
    - Save the changes to the Excel file.

3. **Test Data Entry**:
    - Run your script and enter some sample data to ensure that the function is working correctly and that data is being saved to the Excel file.

### Phase 2: Object-Oriented Design
4. **Design Budget Class**:
    - Create a `Budget` class that represents your entire budget.
    - Define attributes for the class such as categories, total income, total expenses, etc.
    - Define methods for adding transactions, calculating totals, and other relevant actions.

5. **Design Category Class**:
    - Create a `Category` class that represents a single budget category (e.g., groceries, rent).
    - Define attributes such as name, budgeted amount, actual amount spent, etc.
    - Define methods for adding transactions to the category, calculating the remaining budget, etc.

6. **Design Account Class**:
    - Create an `Account` class that represents a bank account or other financial account.
    - Define attributes such as account name, balance, transactions, etc.
    - Define methods for depositing, withdrawing, and transferring funds.

### Phase 3: Data Analysis and Projections
7. **Integrate Pandas for Data Analysis**:
    - Use Pandas to read the data from your Excel file into a DataFrame.
    - Perform analysis on the data, such as calculating averages, sums, etc.
    - Use Pandas to make projections based on historical data.

8. **Visualize Data** (Optional):
    - Use a library like `matplotlib` to create graphs and charts based on your data.

### Phase 4: Refinement and Testing
9. **Refine and Organize Code**:
    - Organize your code into modules and packages for better structure and maintainability.
    - Refactor any redundant or inefficient code.

10. **Testing**:
    - Write tests for your classes and functions to ensure that they are working as expected.
    - Perform manual testing by running your script and entering data.

### Phase 5: Future Expansion
11. **Web Application**:
    - If you decide to turn this into a web application, choose a web framework like Flask or Django.
    - Create a web interface for users to interact with your budgeting tool.
    - Implement user authentication and database integration.

12. **Deployment**:
    - Research deployment options for your web application.
    - Deploy your application to a web server or cloud service.

Remember to commit your code to a version control system like Git regularly, and consider pushing it to a remote repository for backup and collaboration.

This roadmap should give you a structured approach to building your budgeting tool. Take it step by step, and don't hesitate to seek help or resources if you encounter challenges along the way. Good luck!
