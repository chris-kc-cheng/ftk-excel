# Formulas

## Generic Functions

### ROLLING
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

### TRAILING
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

### CALENDARYEAR
```swift
=LAMBDA(ts, dates, func,
    LET(
        start, MIN(YEAR(dates)),
        end, MAX(YEAR(dates)),
        years, SEQUENCE(end - start + 1,, start),
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
```