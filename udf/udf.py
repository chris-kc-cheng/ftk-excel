from typing import Annotated
import pandas as pd
import xlwings as xw
import toolkit as ftk

@xw.func
@xw.arg("tickers", ndim=1)
def yahoo(tickers: Annotated[list, {"doc": "List of tickers"}], period: str="2y") -> pd.DataFrame:
    return ftk.get_yahoo_bulk(tickers, period)