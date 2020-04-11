import pandas as pd


def drawdown(return_series: pd.Series):
    """Takes a time series of asset returns.
    Returns a DF with columns for the wealth index,
    the previous peaks, and the percentage drawdown.
    """

    wealth_index = 1000 * (1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks) / previous_peaks
    return pd.DataFrame({
        'Wealth': wealth_index,
        'Previous Peak': previous_peaks,
        'Drawdown': drawdowns
    })


def get_ffme_returns():
    """
    Load the Fama-French Dataset for the returns of the top and bottom
    deciles by market cap
    """

    caps = pd.read_csv('../data/Portfolios_Formed_on_ME.CSV')
    caps = caps.rename(columns={'Unnamed: 0': 'date'})
    caps['date'] = pd.to_datetime(caps['date'].astype(str) + '01')
    caps = caps.set_index('date')
    caps.index = caps.index.to_period('M')
    caps = caps[['Lo 10', 'Hi 10']].rename(columns={
        'Lo 10': 'SmallCap',
        'Hi 10': 'LargeCap'
    })
    caps /= 100

    return caps


def get_hfi_returns():
    """
    Load and format the EDHEC Hedge Fund Index returns
    """
    
    hfi = pd.read_csv("../data/edhec-hedgefundindices.csv",
                      header=0, index_col=0, parse_dates=True)
    hfi /= 100
    hfi.index = hfi.index.to_period('M')
    return hfi