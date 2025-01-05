# Financial Toolkit in Excel

## Useful functions
Excel formulas that implements the most commonly used functions by an investment professional.

User defined functions are written in plain Excel formulas as lambda function in named range. No VBA is used.

Functions written so far include:

1. Trailing Returns
2. Rolling Returns, Volatility, Beta, Alpha and Jensen's Alpha
3. Up/Down Market Capture
4. Sortino Ratio
5. Maximum Drawdown

## Quartile Chart (Stacked Column Chart) with Negative Values

Excel's built-in stacked column chart cannot span the X axis. To workaround this limitation, we have to create two series (positive and negative) as well as blank. In [quartile.xlsx](quartile.xlsx), we used dynamic array formulas to construct the required series.

<img src="images/quartile.png" alt="Quartile Chart" width="500" />

Credit: https://peltiertech.com/Excel/Charts/StackedColumnsAboveAndBelow.html

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