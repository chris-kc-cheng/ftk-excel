# Formulas

Under construction

| Performance | Risk | Regression | Efficiency | Value at Risk | Time Horizon |
|-------------|------|------------|------------|---------------|--------------|
| | | | | | [Cumulative](#cumulative) |
| | | | | | [Trailing](#trailing) |
| | | | | | [Rolling](#rolling) |
| | | | | | [CalendarYear](#calendaryear) |

Credit: https://www.excelformulabeautifier.com/

## Performance
### Cumulative Returns
### Returns (Annualized)
### Growth of $100

### Number of Observations
### Number of Positive Periods
### Number of Negative Periods

### Average Return
### Average Positive Return
### Average Negative Return

### Best Period
### Worst Period

### Max Consecutive Gain Return
### Max Consecutive Loss Return
### Number of Consecutive Positive Periods
### Number of Consecutive Negative Periods

### Down Period Percent
### Up Period Percent

### Cumulative Excess Returns
### Excess Returns
### Excess Returns - Geometric

### Periods Above Benchmark
### Percentage Above Benchmark
### Percent Profitable Periods

## Risk
### Standard Deviation (Annualized)
### Variance (Annualized)

### Skewness
### Kurtosis (Excess)
### Jarque-Bera [reclassified as risk]

### Max Drawdown
### Average Drawdown
### Current Drawdown

### Semi Deviation (vs Mean, Annualized)
### Gain Deviation (MAR)
### Loss Deviation

### Bias Ratio
### Gain/Loss Ratio

## Regression
### Beta
### Beta T-Stat
### Beta (Rfr Adjusted)

### Alpha (Annualized)
### Jensen Alpha

### Correlation Coefficient
### R-Squared
### Standard Error
### Autocorrelation

### Kendall's Tau
### Kendall's Tau

## Efficiency

### Sharpe Ratio
### Reward to Risk Ratio
### Treynor Ratio
### Sortino Ratio
### Sterling Ratio
### Calmar Ratio

### Up Market Return
### Down Market Return

### Up Market Capture Ratio
### Down Market Capture Ratio

### Tracking Error
### Information Ratio
### Batting Average
### Rolling Batting Average

## Value at Risk

### Gaussian VaR
### Conditional VaR
### Cornish-Fisher VaR

## Time Horizon
Generic functions that can pair up with any of the above functions for charting. For example `ROLLING` that can be combined with `BETA`o calculate rolling beta.

```swift
=ROLLING(HSTACK(fnd, idx), 36, BETA)
```

All these generic functions are essentially a loop that iterates over different period using a sliding or expanding window. There is no loop in Excel but its behaviour can be mimicked using `SEQUENCE` and `MAP`. The performance or risk formula is passed as the second argument.

### Cumulative

An expanding window that start from the first period.

Cumulative calculations measure the entire track record since inception. However, it may include the earlier period when the characteristics are substantially different from now or before your investment is made.

Cumulative calculations are often use in line charts.

```swift
=LAMBDA(
    ts, func,
    LET(
        n, ROWS(ts),
        i, SEQUENCE(n),
        MAP(i,
            LAMBDA(j,
                func(CHOOSEROWS(ts, SEQUENCE(j, , 1)))
            )
        )
    )
)
```

### Trailing

An expanding window that start from the last period.

Commonly used trailing windows include [MRQ](## "Most Recent Quarter"), [TTM](## "Trailing Twelve Months"), and trailing 3, 5, 7, 10 years.

Trailing measures focus on the most recent past. A recent bad month would negatively impact all the trailing measures.

Trailing calculations are more often used in tables or bar charts. It can be counterintuitive to show trailing calculations in line charts.

```swift
=LAMBDA(
    ts, func,
    LET(
        n, ROWS(ts),
        i, SEQUENCE(n),
        MAP(i,
            LAMBDA(j,
                func(CHOOSEROWS(ts, SEQUENCE(j, , n-j+1)))
            )
        )
    )
)
```

### Rolling

An fixed-size sliding window over time.

Rolling is useful in evaluating the consistency of a measure.

Note that there is a second parameter `n` that specifies the size of the rolling window. For example, an `n` of `36` means rolling 3 years. The formula returns `N/A` if the windows does not have `n` returns.

```swift
=LAMBDA(
    ts, n, func,
    LET(
        i, SEQUENCE(ROWS(ts)),
        MAP(i,
            LAMBDA(j,
                IF(j<n, NA(),
                    func(CHOOSEROWS(ts, SEQUENCE(n, , j-n+1)))
                )
            )
        )
    )
)
```

### CalendarYear

The calculation is grouped by the calendar year of the second parameter `dates`.

```swift
=LAMBDA(ts, dates, func,
    LET(
        start, MIN(YEAR(dates)),
        end, MAX(YEAR(dates)),
        years, SEQUENCE(end - start + 1,, start),
        HSTACK(
            years,
            MAP(years,
                LAMBDA(y,
                    LET(
                        n, SEQUENCE(ROWS(ts)),
                        d, IF(YEAR(dates) = y, n, 0),
                        func(CHOOSEROWS(ts, FILTER(d, d > 0)))
                    )
                )
            )
        )
    )
)
```