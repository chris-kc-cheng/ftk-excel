# Financial Toolkit in Excel

## Time Series Analysis

The Excel spreadsheet [ftk.xlsx](ftk.xlsx) implements the most commonly used functions for time series analysis. All function are user defined functions written in plain Excel formulas as lambda functions and stored in name range. No VBA is used.

<details>
    <summary>My journey of time series analysis using Microsoft Excel</summary>

    Excel is more than 40 years old but it remains to be one of the most widely used application software in the world for a good reason - it constantly updates.

    Time series analysis

    VBA

    CSF

    Spill, dynamic array function

    Python, but slow
</details>

Functions are classified in the following categories:

1. Performance
2. Risk
3. Regression
4. Efficiency
5. Value at Risk
6. Time Horizon

For details, please refer to [the formula sheet](formula.md).

## Quartile Chart (Stacked Column Chart) with Negative Values

Excel's built-in stacked column chart cannot span the X axis. To workaround this limitation, we have to create two series (positive and negative) as well as blank. In the [quartile.xlsx](quartile.xlsx), spreadsheet we used dynamic array formulas to construct the required series.

<img src="images/quartile.png" alt="Quartile Chart" width="500" />

Credit: https://peltiertech.com/Excel/Charts/StackedColumnsAboveAndBelow.html

## Black Scholes Model



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