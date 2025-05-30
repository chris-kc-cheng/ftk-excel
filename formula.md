# Formulas

Under construction

| Performance | Risk | Regression | Efficiency | Value at Risk | Time Horizon |
|-------------|------|------------|------------|---------------|--------------|
| [CUMRET](#cumulative-return) | | | | | [CUMULATIVE](#cumulative) |
| [ANNRET](#annualized-return) | | | | | [TRAILING](#trailing) |
| | | | | | [ROLLING](#rolling) |
| | | | | | [CALENDARYEAR](#calendaryear) |

Credit: https://www.excelformulabeautifier.com/

## Performance
### Cumulative Return
`CUMRET` is the time-weighted, compounded product of periodic returns over a period.

```math
R_\text{cumulative} = \prod_{t=1}^{n} (1 + r_t) - 1
```

```Swift
=LAMBDA(
    ts,
    FVSCHEDULE(1, ts) - 1
)
```

### Annualized Return
`ANNRET` is the geometric mean of returns with respect to one year.

```math
R_{\text{annualized}} = (1 + R_{\text{cumulative}})^{\frac{1}{T}} - 1
```


```Swift
=LAMBDA(
    ts,
    GEOMEAN(
        1 + ts
    ) ^ 12 - 1
)
```

### Growth of $100
`GROWTHOF` returns the growth of $100 over a period.

```math
\text{Growth of \$100} = 100 \times \prod_{t=1}^{n}(1 + r_t)
```

```swift
=LAMBDA(
    ts, init,
    IF(
        ISOMITTED(init),
        100,
        init
    ) * (CUMULATIVERETURN(ts) + 1 )
)
```

### Number of Observations
`PER`
```math
N = \text{length of } \{ r_1, r_2, ..., r_n \}
```
```swift
=LAMBDA(
    ts,
    COUNT(ts)
)
```

### Number of Positive Periods
`PERPOS`
$$ N_{+} = \sum_{t=1}^{n} \mathbf{1}_{(r_t > 0)} $$
```swift
=LAMBDA(
    ts,
    COUNTIF(ts, ">0")
)
```

### Number of Negative Periods
`PERNEG`
$$ N_{-} = \sum_{t=1}^{n} \mathbf{1}_{(r_t < 0)} $$
```swift
=LAMBDA(
    ts,
    COUNTIF(ts, "<0")
)
```

### Average Return
`AVGRET`
$$ \bar{r} = \frac{1}{n} \sum_{t=1}^{n} r_t $$
```swift
=LAMBDA(
    ts,
    AVERAGE(ts)
)
```

### Average Positive Return
`AVGPOS`
$$ \bar{r}_{+} = \frac{1}{N_{+}} \sum_{r_t > 0} r_t $$
```swift
=LAMBDA(
    ts,
    AVERAGEIF(ts, ">0")
)
```

### Average Negative Return
`AVGNEG`
$$ \bar{r}_{-} = \frac{1}{N_{-}} \sum_{r_t < 0} r_t $$
```swift
=LAMBDA(
    ts,
    AVERAGEIF(ts, "<0")
)
```

### Best Period
$$ r_{\text{max}} = \max_{t} (r_t) $$
```swift
=LAMBDA(
    ts,
    MAX(ts)
)
```

### Worst Period
$$ r_{\text{min}} = \min_{t} (r_t) $$
```swift
=LAMBDA(
    ts,
    MIN(ts)
)
```

### Max Consecutive Gain Return
`MAXCONSECGAINRET`
$$ \max \left( \prod_{i=1}^{k} (1 + r_i) - 1 \right), \text{ for consecutive } r_i > 0 $$
```swift
=LAMBDA(
    ts,
    MAX(
        SCAN(
            1, ts,
            LAMBDA(
                x, y,
                IF(
                    y > 0,
                    x * ( 1 + y ),
                    1
                )
            )
        )
    ) - 1
)
```

### Max Consecutive Loss Return
`MAXCONSECLOSSRET`
$$ \min \left( \prod_{i=1}^{k} (1 + r_i) - 1 \right), \text{ for consecutive } r_i < 0 $$
```swift
=LAMBDA(
    ts,
    MIN(
        SCAN(
            1, ts,
            LAMBDA(
                x, y,
                IF(
                    y < 0,
                    x * ( 1 + y ),
                    1
                )
            )
        )
    ) - 1
)
```

### Number of Consecutive Positive Periods
`MAXCONSECGAINPER`
$$ \max(\text{streak length } | r_t > 0) $$
```swift
=LAMBDA(
    ts,
    MAX(
        SCAN(
            0,
            SIGN(ts) > 0,
            LAMBDA(
                x, y
                IF(y, x + y, 0)
            )
        )
    )
)
```

### Number of Consecutive Negative Periods
`MAXCONSECLOSSPER`
$$ \max(\text{streak length } | r_t < 0) $$
```swift
=LAMBDA(
    ts,
    MAX(
        SCAN(
            0,
            SIGN(ts) < 0,
            LAMBDA(
                x, y,
                IF(y, x + y, 0)
            )
        )
    )
)
```

### Cumulative Excess Returns
$$ R_{\text{excess}} = \prod_{t=1}^{n}(1 + r_t) - \prod_{t=1}^{n}(1 + b_t) $$
```swift
```

### Excess Returns - Arithmetic
$$ \text{R}_{\text{excess, arithmetic}} = \left( \prod_{t=1}^{n} (1 + r_{t}) \right)^{\frac{1}{T}} - \left( \prod_{t=1}^{n} (1 + b_{t}) \right)^{\frac{1}{T}}
 $$
```swift
```

### Excess Returns - Geometric
$$ R_{\text{excess, geometric}} = \frac{\prod_{t=1}^{n}(1 + r_t)}{\prod_{t=1}^{n}(1 + b_t)} - 1 $$
```swift
```

### Periods Above Benchmark
$$ N_{\text{above}} = \sum_{t=1}^{n} \mathbf{1}_{(r_t > b_t)} $$
```swift
```

### Percentage Above Benchmark
$$ \frac{N_{\text{above}}}{N} $$
```swift
```

### Percent Profitable Periods
$$ \frac{N_{+}}{N} $$
```swift
```

## Risk
### Standard Deviation (Annualized)
$$ s_{\text{annualized}} = \sqrt{\frac{N_{\text{periods per year}}}{n - 1} \sum_{i=1}^{n} (r_i - \bar{r})^2 } $$
```swift
```

### Variance (Annualized)
$$ s^2_{\text{annualized}} = \frac{N_{\text{periods per year}}}{n - 1} \sum_{i=1}^{n} (r_i - \bar{r})^2 $$
```swift
```

### Skewness
$$ S = \frac{n}{(n - 1)(n - 2)} \sum_{t=1}^{n} \left( \frac{r_t - \bar{r}}{s} \right)^3 $$

```swift
```

### Kurtosis (Excess)
$$ K = \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum_{t=1}^{n} \left( \frac{r_t - \bar{r}}{s} \right)^4 - \frac{3(n-1)^2}{(n-2)(n-3)} $$
```swift
```

### Jarque-Bera [reclassified as risk]
$$ \text{JB} = \frac{n}{6} \left( S^2 + \frac{K^2}{4} \right) $$
```swift
```

### Max Drawdown
$$ \text{Max Drawdown} = \max_{t \in [1,T]} \left( \frac{\max_{s \in [1,t]} V_s - V_t}{\max_{s \in [1,t]} V_s} \right) $$

where

$$ \text{V}_t = \text{V}_0 \times \prod_{i=1}^{t}(1 + r_i) $$
```swift
```

### Average Drawdown
$$ \text{Average Drawdown} = \frac{1}{K} \sum_{i=1}^{K} \text{Drawdown}_i $$
```swift
```

### Current Drawdown
$$ \text{Current Drawdown} = \frac{\text{Current Value} - \text{Last Peak}}{\text{Last Peak}} $$
```swift
```

### Semi Deviation (vs Mean, Annualized)
$$ \text{SemiDev}_{\text{annualized}} = \sqrt{\frac{N_{\text{periods per year}}}{n_{-}} \sum_{r_t < \bar{r}} (r_t - \bar{r})^2 } $$
```swift
```

### Gain Deviation (vs MAR)
$$ \text{Gain Deviation} = \sqrt{ \frac{N_{\text{periods per year}}}{n} \sum_{r_t > \text{MAR}} (r_t - \text{MAR})^2 } $$
```swift
```

### Loss Deviation (vs RFR)
$$ \text{Loss Deviation} = \sqrt{ \frac{N_{\text{periods per year}}}{n_{-}} \sum_{r_t < r_f} (r_t - r_f)^2 } $$
```swift
```

### Bias Ratio
$$ \text{Bias Ratio} = \frac{\#(0 \leq r_t \leq \sigma)}{1 + \#(-\sigma \leq r_t < 0)} $$
```swift
```

### Gain/Loss Ratio
$$ \text{Gain/Loss Ratio} = \frac{\bar{r}_{+}}{|\bar{r}_{-}|} $$
```swift
```

## Regression
### Beta
$$ \beta = \frac{\text{Cov}(r, b)}{\text{Var}(b)} = \frac{\sum_{i=1}^{n} (r_i - \bar{r})(b_i - \bar{b})}{\sum_{i=1}^{n} (b_i - \bar{b})^2} $$
```swift
```

### Beta T-Stat
$$ t_{\beta} = \frac{\hat{\beta}}{\text{SE}(\hat{\beta})} $$
```swift
```

### Beta (Rfr Adjusted)
$$ \beta_{\text{adj}} = \frac{\text{Cov}(r - r_f, b - r_f)}{\text{Var}(b - r_f)} $$
```swift
```

### Alpha (Annualized)
$$ \alpha_{\text{annual}} = (r - \beta \cdot b + 1)^{N_{\text{periods per year}}} - 1 $$
```swift
```

### Jensen Alpha
$$ \alpha_{\text{Jensen}} = (\bar{r} - \left[ r_f + \beta \cdot (\bar{b} - r_f) \right] + 1)^{N_{\text{periods per year}}} - 1 $$
```swift
```

### Correlation Coefficient
$$ \rho_{r,b} = \frac{\text{Cov}(r, b)}{\sigma_r \sigma_b} $$
```swift
```

### R-Squared
$$ R^2 = \left( \frac{\text{Cov}(r, b)}{\sigma_r \sigma_b} \right)^2 $$
```swift
```

### Standard Error
$$ \text{SE} = \sqrt{ \frac{1}{n - 2} \sum_{t=1}^{n} (r_t - \hat{r}_t)^2 } $$
```swift
```

### Autocorrelation
$$ \rho_1 = \frac{\sum_{t=2}^{n} (r_t - \bar{r})(r_{t-1} - \bar{r})}{\sum_{t=1}^{n} (r_t - \bar{r})^2} $$
```swift
```

### Kendall's Tau-b
$$ \tau_b = \frac{C - D}{\sqrt{(C + D + T_x)(C + D + T_y)}} $$
```swift
```

### Kendall's Tau-c
$$ \tau_c = \frac{2 (C - D)}{n^2 (k - 1) / k} $$
```swift
```

## Efficiency
### Sharpe Ratio
$$ \text{Sharpe Ratio}_{\text{annual}} = \frac{r_{\text{annual}} - b_{\text{annual}}}{s_{\text{annual}}} $$
```swift
```

### Reward to Risk Ratio
$$ \text{Reward to Risk Ratio} = \frac{r_{\text{annual}}}{s_{\text{annual}}} $$
```swift
```

### Treynor Ratio
$$ \text{Treynor Ratio} = \frac{r_{\text{annual}} - b_{\text{annual}}}{\beta} $$
```swift
```

### Sortino Ratio
$$ \text{Sortino Ratio} = \frac{r_{\text{annual}} - b_{\text{annual}}}{\text{Loss Deviation}} $$
```swift
```

### Sterling Ratio
$$ \text{Sterling Ratio} = \frac{r_{\text{annual}}}{\left| \text{Average Drawdown} \right| + 0.10} $$
```swift
```

### Calmar Ratio
$$ \text{Calmar Ratio} = \frac{r_{\text{annual}}}{\text{Max Drawdown}} $$
```swift
```

### Up Market Return
$$ \text{Up Market Return} = \left[ \prod_{i=1}^{n_{\text{up}}} (1 + r_{i}) \right]^{\frac{12}{n_{\text{up}}}} - 1 $$

where $r_i$ is the portfolio return in month $𝑖$ when the benchmark return $b_i$ is positive.

```swift
```

### Down Market Return
$$ \text{Down Market Return} = \left[ \prod_{i=1}^{n_{\text{down}}} (1 + r_{i}) \right]^{\frac{12}{n_{\text{down}}}} - 1 $$

where $r_i$ is the portfolio return in month $𝑖$ when then benchmark return $b_i$ is negative.

```swift
```

### Up Market Capture Ratio
$$ \text{Up Market Capture Ratio} = \frac{\left[ \prod_{i=1}^{n_{\text{up}}} (1 + r_{i}) \right]^{\frac{12}{n_{\text{up}}}} - 1}{\left[ \prod_{i=1}^{n_{\text{up}}} (1 + b_{i}) \right]^{\frac{12}{n_{\text{up}}}} - 1} $$

where $r_i$ is the portfolio return in month $𝑖$ when the benchmark return $b_i$ is positive.

```swift
```

### Down Market Capture Ratio
$$ \text{Down Market Capture Ratio} = \frac{\left[ \prod_{i=1}^{n_{\text{down}}} (1 + r_{i}) \right]^{\frac{12}{n_{\text{down}}}} - 1}{\left[ \prod_{i=1}^{n_{\text{down}}} (1 + b_{i}) \right]^{\frac{12}{n_{\text{down}}}} - 1} $$

where $r_i$ is the portfolio return in month $𝑖$ when then benchmark return $b_i$ is negative.
```swift
```

### Tracking Error
$$ \text{Tracking Error} = \sqrt{ \frac{N_{\text{periods per year}}}{n-1} \sum_{t=1}^{n} (r_t - b_t)^2 } $$
```swift
```

### Information Ratio
$$ \text{Information Ratio} = \frac{r_{\text{annual}} - b_{\text{annual}}}{\text{Tracking Error}} $$
```swift
```

### Batting Average
$$ \text{Batting Average} = \frac{\text{count} (r_t > b_t)}{n} $$
```swift
```
### Up Period Batting Average
$$ \text{Up Period Batting Average} = \frac{\text{count} \left\{ i : r_{i} > b_{i}, b_{i} > 0 \right\}}{\text{count} \left\{ i : b_{i} > 0 \right\}} $$
```swift
```

### Down Period Batting Average
$$ \text{Down Period Batting Average} = \frac{\text{count} \left\{ i : r_{i} > b_{i}, b_{i} < 0 \right\}}{\text{count}\left\{ i : b_{i} < 0 \right\}} $$
```swift
```

### Rolling Batting Average
$$ \text{Rolling Batting Average} = \frac{1}{T - w + 1} \sum_{t=w}^{T} \frac{\text{count} \left\{ i : r_{p,i} > r_{b,i}, i \in [t-w+1, t] \right\}}{\text{count} \left\{ i : r_{b,i}, i \in [t-w+1, t] \right\}} $$
```swift
```

## Value at Risk
### Historical VaR
$$ \text{VaR}_{\alpha} = \text{Quantile}_{\alpha}\left(\{r_1, r_2, \dots, r_T\}\right) $$
```swift
```

### Historical Conditional VaR / Expected Shortfall
$$ \text{CVaR}_{\alpha} = \frac{1}{N_{\alpha}} \sum_{i=1}^{N_{\alpha}} r_i $$
```swift
```

### Gaussian VaR
$$ \text{VaR}_{\alpha} = \bar{r} - z_{1 - \alpha} \cdot s $$
```swift
```

### Gaussian Conditional VaR / Expected Shortfall
$$ \text{ES}_{\alpha} = \bar{r} - \frac{\phi\left(\Phi^{-1}(1 - \alpha)\right)}{\alpha} \cdot s $$
```swift
```

### Cornish-Fisher VaR
$$ \text{VaR}_{\alpha} = \bar{r} + s \left[ z_{\alpha} + (z_{\alpha}^2 - 1) \frac{S}{6} + (z_{\alpha}^3-3z_{\alpha}) \frac{K}{24} -(2z_{\alpha}^3-5z_{\alpha})\frac{S^2}{36} \right] $$
```swift
```

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