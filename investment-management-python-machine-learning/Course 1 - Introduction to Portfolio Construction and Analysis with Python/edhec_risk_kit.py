import pandas as pd
from scipy.stats import norm


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


def get_ind_returns():
    """Load and format the Industry 30 returns originally
    from Ken French's data website"""
    ind = pd.read_csv('../data/ind30_m_vw_rets.csv', index_col=0)
    ind /= 100
    ind.index = pd.to_datetime(ind.index, format="%Y%m").to_period('M')
    ind.columns = ind.columns.str.strip()
    return ind


def skewness(r):
    """
    Alternative to scipy.stats.skew() (uh, and pd.Series.skew())
    Computes the skewness of the supplied Series or DataFrame
    Returns a float or a Series
    """
    demeaned_r = r - r.mean()
    # use the population standard deviation, so set dof=0
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**3).mean()
    return exp/sigma_r**3


def kurtosis(r):
    """
    Alternative to scipy.stats.kurtosis() and pd.Series.kurtosis()
    Computes the kurtosis of the supplied Series or DataFrame
    Returns a float or a Series
    """
    demeaned_r = r - r.mean()
    # use the population standard deviation, so set dof=0
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**4).mean()
    return exp/sigma_r**4


def var_gaussian(r, level=5, modified=False):
    """
    Returns the Parametric Gauusian VaR of a Series or DataFrame
    If "modified" is True, then the modified VaR is returned,
    using the Cornish-Fisher modification
    """
    # compute the Z score assuming it was Gaussian
    z = norm.ppf(level/100)
    if modified:
        # modify the Z score based on observed skewness and kurtosis
        s = skewness(r)
        k = kurtosis(r)
        z = (
            z +
            (z**2 - 1) * s/6 +
            (z**3 - 3*z) * (k-3)/24 -
            (2*z**3 - 5*z) * (s**2)/36
        )
    return -(r.mean() + z*r.std(ddof=0))


# Week 2

def annualize_rets(r, periods_per_year):
    """
    Annualizes a set of returns (in the 0.04 format for a 4% monthly return)
    Works for pd.Series and pd.DataFrame
    """
    compounded_growth = (1+r).prod()
    n_periods = r.shape[0]
    return compounded_growth ** (periods_per_year / n_periods) - 1


def annualize_vol(r, periods_per_year):
    """
    Dito for the volatility
    """
    return r.std() * (periods_per_year ** 0.5)


def sharpe_ratio(r, riskfree_rate, periods_per_year):
    """
    Computes the annualized sharpe ratio of a set of returns
    Works for a pd.Series or per-column for a pd.DataFrame
    """
    rf_per_period = (1+riskfree_rate) ** (1/periods_per_year) - 1
    excess_return = r - rf_per_period
    ann_ex_ret = annualize_rets(excess_return, periods_per_year)
    ann_vol = annualize_vol(r, periods_per_year)
    return ann_ex_ret / ann_vol
