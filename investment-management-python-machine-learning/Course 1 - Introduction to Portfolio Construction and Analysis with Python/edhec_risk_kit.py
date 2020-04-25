import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.optimize import minimize

# ################################################################
# Week 1


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


def var_historic(r, level=5):
    """
    Returns the historic Value at Risk at a specified level
    i.e. returns the number such that "level" percent of the returns
    fall below that number, and the (100-level) percent are above
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance(r, pd.Series):
        return -np.percentile(r, level)
    else:
        raise TypeError("Expected r to be a Series or DataFrame")


def cvar_historic(r, level=5):
    """
    Computes the Conditional VaR of Series or DataFrame
    """
    if isinstance(r, pd.Series):
        is_beyond = r <= -var_historic(r, level=level)
        return -r[is_beyond].mean()
    elif isinstance(r, pd.DataFrame):
        return r.aggregate(cvar_historic, level=level)
    else:
        raise TypeError("Expected r to be a Series or DataFrame")


def var_gaussian(r, level=5, modified=False):
    """
    Returns the Parametric Gaussian VaR of a Series or DataFrame
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


# ################################################################
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


def portfolio_return(weights, returns):
    """
    Given asset returns and a weight vector, returns the portfolio return
    """
    return weights.T @ returns  # (weights * returns).sum()


def portfolio_vol(weights, cov):
    return (weights.T @ cov @ weights) ** 0.5


def plot_ef2(n_points, expected_returns, covariance_matrix, style='.-'):
    """Plots the efficient frontier for two assets"""

    if expected_returns.shape != (2,) or covariance_matrix.shape != (2, 2):
        raise ValueError("plot_ef2 can only plot 2-asset frontiers!")

    weights = [np.array([w, 1-w]) for w in np.linspace(0, 1, n_points)]

    rets = [portfolio_return(w, expected_returns) for w in weights]
    vols = [portfolio_vol(w, covariance_matrix) for w in weights]

    ef = pd.DataFrame({"Returns": rets, "Volatility": vols})

    return ef.plot.line('Volatility', 'Returns', style=style)


def minimize_vol(target_return, expected_returns, covariance_matrix):
    """From a target return, go to a weight vector that achieves that return with
    the minimum volatility. I.e., find the point on the efficient frontier for
    that.

    """
    n = expected_returns.shape[0]
    initial_guess = np.repeat(1/n, n)

    # #### Constraints

    # bounds: weights should not go below zero (shorting) or above one
    # (leveraged long).
    # scipy expects a set of bounds per parameter (i.e. weight) to optimize
    bounds = ((0.0, 1.0),) * n

    # Total return should be 'return' (see docs:
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html)
    return_is_target = {
        'type': 'eq',
        'args': (expected_returns,),
        # w: weights
        # er: expected_returns
        'fun': lambda w, er: target_return - portfolio_return(w, er)
    }

    # Weights must sum to 1
    weights_sum_to_1 = {
        'type': 'eq',
        'fun': lambda weights: np.sum(weights) - 1
    }

    results = minimize(
        fun=portfolio_vol,  # objective function we want to minimize
        x0=initial_guess,
        args=(covariance_matrix,),
        bounds=bounds,  # each weight must be in [0, 1]
        constraints=(return_is_target, weights_sum_to_1),
        method="SLSQP",  # quadratic programming solver
        options={'disp': False},  # make the output non-verbose
    )

    return results.x


def optimal_weights(n_points, expected_returns, covariance_matrix):
    """Creates a list of weight vectors to run the optimizer on
    to minimize the volatility per expected return.
    Is used in plot_ef()"""

    # The EF's min is the minimum of all target returns (without shorting etc),
    # and its max is the maximum of all target returns
    target_returns = np.linspace(
        expected_returns.min(), expected_returns.max(), n_points
    )
    weights = [
        minimize_vol(tr, expected_returns, covariance_matrix)
        for tr in target_returns
    ]

    return weights


def msr(riskfree_rate, expected_returns, covariance_matrix):
    """Compute the weights for the Maximum Sharpe Ratio portfolio
    """
    n = expected_returns.shape[0]
    initial_guess = np.repeat(1/n, n)

    # #### Constraints

    # bounds: weights should not go below zero (shorting) or above one
    # (leveraged long).
    # scipy expects a set of bounds per parameter (i.e. weight) to optimize
    bounds = ((0.0, 1.0),) * n

    # Weights must sum to 1
    weights_sum_to_1 = {
        'type': 'eq',
        'fun': lambda weights: np.sum(weights) - 1
    }

    def neg_sharpe_ratio(weights, riskfree_rate, er, cov):
        r = portfolio_return(weights, er)
        vol = portfolio_vol(weights, cov)
        sharpe = (r - riskfree_rate) / vol
        return -sharpe

    results = minimize(
        fun=neg_sharpe_ratio,  # objective function we want to minimize
        x0=initial_guess,
        args=(riskfree_rate, expected_returns, covariance_matrix),
        bounds=bounds,  # each weight must be in [0, 1]
        constraints=(weights_sum_to_1),
        method="SLSQP",  # quadratic programming solver
        options={'disp': False},  # make the output non-verbose
    )

    return results.x


def gmv(cov):
    """Returns the weights of the global minimum variance portfolio
    given a covariance matrix"""

    # Dirty trick: Get the MSR portfolio if all expected returns are the same
    # Then the optimizer can only improve the Sharpe ratio if he minimizes the
    # volatility :D
    # def msr(riskfree_rate, expected_returns, covariance_matrix):
    n = cov.shape[0]
    return msr(
        riskfree_rate=0.12345,  # not used anyway
        expected_returns=np.repeat(1, n),
        covariance_matrix=cov
    )


def plot_ef(n_points, expected_returns, covariance_matrix,
            show_cml=False, riskfree_rate=0, style='.-',
            show_ew=False, show_gmv=False):
    """Plots the efficient frontier for n assets.
    show_cml: Show the Capital Market Line from the riskfree rate (vol=0)
              to the MSR portfolio
    show_ew:  Show the point for the equal-weighted portfolio.
    show_gmv: Show the global minimum variance portfolio
    """

    # The major change from 2 to n assets is finding the correct weights
    # that result *on* the efficient frontier
    # For that, you'll need to minimize the volatility for each target return,
    #   and get the weights that do that.
    weights = optimal_weights(n_points, expected_returns, covariance_matrix)

    rets = [portfolio_return(w, expected_returns) for w in weights]
    vols = [portfolio_vol(w, covariance_matrix) for w in weights]

    ef = pd.DataFrame({"Returns": rets, "Volatility": vols})

    # Plot the EF
    ax = ef.plot.line('Volatility', 'Returns', style=style)

    # Add the individual securities
    ax.scatter(np.sqrt(np.diag(covariance_matrix)), expected_returns, c="red")

    # Add the equally-weighted portfolio point
    if show_ew:
        n = expected_returns.shape[0]
        w_ew = np.repeat(1/n, n)
        r_ew = portfolio_return(w_ew, expected_returns)
        vol_ew = portfolio_vol(w_ew, covariance_matrix)
        ax.plot(vol_ew, r_ew, color='goldenrod', marker="o", markersize=12)

    # Add the Global Minimum Variance portfolio
    if show_gmv:
        w_gmv = gmv(covariance_matrix)
        r_gmv = portfolio_return(w_gmv, expected_returns)
        vol_gmv = portfolio_vol(w_gmv, covariance_matrix)
        ax.plot(vol_gmv, r_gmv, color='midnightblue',
                marker="o", markersize=12)

    # Add the Capital Market Line (CML)
    if show_cml:
        ax.set_xlim(left=0)
        w_msr = msr(riskfree_rate, expected_returns, covariance_matrix)
        r_msr = portfolio_return(w_msr, expected_returns)
        vol_msr = portfolio_vol(w_msr, covariance_matrix)
        # Two x and y coordinates for the CML
        cml_x = [0, vol_msr]
        cml_y = [riskfree_rate, r_msr]
        ax.plot(cml_x, cml_y, color="green",
                marker="o", linestyle="dashed", markersize=6, linewidth=2)

    return ax


# ################################################################
# Week 3

def get_ind_size():
    """This table holds the average size of the companies
    in this industry
    """
    ind = pd.read_csv('../data/ind30_m_size.csv', index_col=0)
    ind.index = pd.to_datetime(ind.index, format="%Y%m").to_period('M')
    ind.columns = ind.columns.str.strip()
    return ind


def get_ind_nfirms():
    """This table holds the number of firms
    in this industry
    """
    ind = pd.read_csv('../data/ind30_m_nfirms.csv', index_col=0)
    ind.index = pd.to_datetime(ind.index, format="%Y%m").to_period('M')
    ind.columns = ind.columns.str.strip()
    return ind


def get_total_market_index_returns():
    """Load the 30 industry portfolio data and derive the returns of a capweighted
    total market index

    """
    ind_nfirms = get_ind_nfirms()
    ind_size = get_ind_size()
    ind_return = get_ind_returns()
    ind_mktcap = ind_nfirms * ind_size
    total_mktcap = ind_mktcap.sum(axis=1)
    ind_capweight = ind_mktcap.divide(total_mktcap, axis="rows")
    total_market_return = (ind_capweight * ind_return).sum(axis="columns")
    return total_market_return


def run_cppi(risky_r, safe_r=None, m=3, start=1000, floor=0.8,
             riskfree_rate=0.03, drawdown=None):
    """Run a backtest of the CPPI strategy, given a set of returns for the risky
    asset Returns a dictionary containing: Asset Value History, Risk Budget
    History, Risky Weight History
    """

    # set up the CPPI parameters
    dates = risky_r.index
    n_steps = len(dates)
    account_value = start
    floor_value = start*floor
    peak = account_value
    if isinstance(risky_r, pd.Series):
        risky_r = pd.DataFrame(risky_r, columns=["R"])

    if safe_r is None:
        safe_r = pd.DataFrame().reindex_like(risky_r)
        # fast way to set all values to a number:
        safe_r.values[:] = riskfree_rate / 12
    # set up some DataFrames for saving intermediate values
    account_history = pd.DataFrame().reindex_like(risky_r)
    risky_w_history = pd.DataFrame().reindex_like(risky_r)
    cushion_history = pd.DataFrame().reindex_like(risky_r)
    floorval_history = pd.DataFrame().reindex_like(risky_r)
    peak_history = pd.DataFrame().reindex_like(risky_r)

    for step in range(n_steps):
        if drawdown is not None:
            peak = np.maximum(peak, account_value)
            floor_value = peak*(1-drawdown)
        cushion = (account_value - floor_value)/account_value
        risky_w = m*cushion
        risky_w = np.minimum(risky_w, 1)
        risky_w = np.maximum(risky_w, 0)
        safe_w = 1-risky_w
        risky_alloc = account_value*risky_w
        safe_alloc = account_value*safe_w
        # recompute the new account value at the end of this step
        account_value = risky_alloc * (1+risky_r.iloc[step]) + \
            safe_alloc * (1+safe_r.iloc[step])
        # save the histories for analysis and plotting
        cushion_history.iloc[step] = cushion
        risky_w_history.iloc[step] = risky_w
        account_history.iloc[step] = account_value
        floorval_history.iloc[step] = floor_value
        peak_history.iloc[step] = peak
    risky_wealth = start*(1+risky_r).cumprod()
    backtest_result = {
        "Wealth": account_history,
        "Risky Wealth": risky_wealth,
        "Risk Budget": cushion_history,
        "Risky Allocation": risky_w_history,
        "m": m,
        "start": start,
        "floor": floor,
        "risky_r": risky_r,
        "safe_r": safe_r,
        "drawdown": drawdown,
        "peak": peak_history,
        # "floor": floorval_history  # duplicate dict key!!!!!111
    }
    return backtest_result


def summary_stats(r, riskfree_rate=0.03):
    """Return a DataFrame that contains aggregated summary stats for the
    returns in the columns of r"""
    ann_r = r.aggregate(annualize_rets, periods_per_year=12)
    ann_vol = r.aggregate(annualize_vol, periods_per_year=12)
    ann_sr = r.aggregate(sharpe_ratio,
                         riskfree_rate=riskfree_rate, periods_per_year=12)
    dd = r.aggregate(lambda r: drawdown(r).Drawdown.min())
    skew = r.aggregate(skewness)
    kurt = r.aggregate(kurtosis)
    cf_var5 = r.aggregate(var_gaussian, modified=True)
    hist_cvar5 = r.aggregate(cvar_historic)
    return pd.DataFrame({
        "Annualized Return": ann_r,
        "Annualized Vol": ann_vol,
        "Skewness": skew,
        "Kurtosis": kurt,
        "Cornish-Fisher VaR (5%)": cf_var5,
        "Historic CVaR (5%)": hist_cvar5,
        "Sharpe Ratio": ann_sr,
        "Max Drawdown": dd
    })
