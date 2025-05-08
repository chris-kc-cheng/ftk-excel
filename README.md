# Financial Toolkit in Excel

## Project 1: Time Series Analysis

The Excel spreadsheet [ftk.xlsx](ftk.xlsx) implements around 70 most commonly used functions for time series analysis. All functions are, written in plain Excel formulas as lambda functions, and stored in named ranges. No auxiliary cells or columns are used, and no VBA is involved.

<img src="images/lambda.png" alt="Lambda functions in name range" width="500" />

Functions are classified in the following categories:

1. Performance
2. Risk
3. Regression
4. Efficiency
5. Value at Risk
6. Time Horizon - These generic functions works in conjunction with the risk and performance functions above to provide comprehensive analysis across multiple periods.

For details, please refer to [the formula sheet](formula.md).

The spreadsheet provides Python implementations of the same functions for comparison and extended analysis.

## Project 2: Quartile Chart (Stacked Column Chart) with Negative Values

Excel's built-in stacked column chart cannot span the X axis. To workaround this limitation, we have to create two series (positive and negative) as well as blank. In the [quartile.xlsx](quartile.xlsx), spreadsheet we used dynamic array formulas to construct the required series.

<img src="images/quartile.png" alt="Quartile Chart" width="500" />

Credit: https://peltiertech.com/Excel/Charts/StackedColumnsAboveAndBelow.html

## Project 3: Black Scholes Model

The [bsm.xlsx](bsm.xlsx) demonstrates how theoretical option values, based on the Black-Scholes model, change with variations in a single input while keeping all other inputs constant.

<img src="images/options.png" alt="Option Values" width="500" />

## Project 4: MSCI Index Data

### Real time index data

The [MSCI Real Time Index.xlsx](MSCI%20Real%20Time%20Index.xlsx) spreadsheet uses PowerQuery to retrieve real-time performance data from the [MSCI website](https://www.msci.com/real-time-index-data-search) and displays it in a table format. The data is delayed by 20 minutes and is refreshed every minute. The base currency is predetermined and not user-configurable.

<img src="images/msci-rt.png" alt="MSCI Real-Time Index" width="500" />

### End of day index data

The [MSCI End of Day Index.xlsx](MSCI%20End%20of%20Day%20Index.xlsx) spreadsheet uses PowerQuery to retrieve end-of-day performance data from the [MSCI website](https://www.msci.com/end-of-day-data-search). The table presents performance data as price returns in CAD terms by default. However, the index variant (e.g., net or gross total return), currency, data frequency, as well as the start and end dates are all user-configurable.

<img src="images/msci-eod.png" alt="MSCI End of Day Index" width="500" />

## Appendix 1: List of Excel's Dynamic Array Formulas
| Lookup  | Lambda    | Shaping    | Summarizing | Miscellaneous |
|---------|-----------|------------|-------------|---------------|
| XLOOKUP | LAMBDA    | VSTACK     | FILTER      | LET           |
| XMATCH  | MAP       | HSTACK     | SORT        | SEQUENCE      |
|         | REDUCE    | TOROW      | SORTBY      | RANDARRAY     |
|         | SCAN      | TOCOL      | UNIQUE      | STOCKHISTORY  |
|         | BYROW     | WRAPROWS   | GROUPBY     |
|         | BYCOL     | WRAPCOLS   | PIVOTBY     |
|         | MAKEARRAY | TAKE       |
|         | ISOMITTED | DROP       |
|         |           | CHOOSEROWS |
|         |           | CHOOSECOLS |
|         |           | EXPAND     |


<!--
<details>
    <summary>My journey of time series analysis using Microsoft Excel</summary>

    Excel is more than 40 years old but it remains to be one of the most widely used application software in the world for a good reason - it constantly updates.

    Time series analysis

    VBA

    CSF

    Spill, dynamic array function

    Python, but slow
</details>
-->