# Expense Tracker Application

A simple yet powerful Python application for tracking personal finances, recording income and expenses, and visualizing financial data over time.

## Features

- **Transaction Management**: Add and track financial transactions with date, amount, category, and description
- **Date Range Reports**: View transaction history and financial summaries within custom date ranges
- **Data Visualization**: Generate time-series plots to visualize income and expense trends
- **Data Persistence**: All transactions stored in CSV format for easy access and portability
- **User-friendly Interface**: Simple command-line interface for easy interaction

## Requirements

- Python 3.x
- Libraries:
  - pandas
  - matplotlib
  - datetime
  - csv

## Installation

1. Clone this repository or download the files
2. Install required dependencies:
   ```
   pip install pandas matplotlib
   ```

## Usage

Run the application using Python:

```
python main.py
```

### Main Menu Options

The application provides a simple menu-driven interface:

1. **Insert New Record**: Add a new income or expense transaction
2. **View Transactions**: View all transactions within a date range and get summary statistics
3. **Exit**: Quit the application

### Adding Transactions

When adding a new transaction, you'll be prompted to enter:
- Date (format: dd-mm-yyyy) - defaults to current date if left blank
- Amount (must be positive)
- Category (Income or Expense)
- Description (optional)

### Transaction Reports

View your financial data by specifying a date range. The application will:
- Display all transactions within that range
- Calculate total income, expenses, and savings
- Optionally generate visual plots of your financial activity

## File Structure

- `main.py`: Main application file with core functionality
- `data_entery.py`: Helper functions for data input and validation
- `financial_data.csv`: CSV database storing all financial transactions

## Data Format

The financial data is stored in CSV format with the following columns:
- `date`: Transaction date (dd-mm-yyyy)
- `amount`: Transaction amount
- `category`: Transaction category (Income or Expense)
- `description`: Optional transaction description

## License

This project is open-source and available for personal use.

## Future Enhancements

Potential features for future versions:
- Multiple currency support
- Budget planning and limit notifications
- Custom categories for better expense tracking
- Data export to other formats
- Web or GUI interface
