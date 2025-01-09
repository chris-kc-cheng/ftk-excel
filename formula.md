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
                    func(CHOOSEROWS(ts,SEQUENCE(n, , j-n+1)))
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
                func(CHOOSEROWS(ts,SEQUENCE(j, , n-j+1)))
            )
        )
    )
)
```