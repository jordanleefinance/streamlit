import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import random as random
import time
import yfinance as yf

data_df = pd.DataFrame()


class StockPortfolioAnalysis:
    def __init__(self, portfolio, num_shares, start_date='', end_date='', freq='', index_stock=''):
        self.portfolio = portfolio
        self.num_shares = num_shares
        self.start_date = start_date
        self.end_date = end_date
        self.freq = freq
        self.index_stock = index_stock
        global data_df
        for stock, numb in zip(portfolio, num_shares):
            time.sleep(.12)
            data_df[stock] = yf.download(tickers=stock, start=start_date, end=end_date)["Adj Close"]
        if freq == "D":
            data_df = pd.DataFrame(data_df)
        else:
            data_df.resample(rule=freq).apply(StockPortfolioAnalysis.last_element)
            data_df = pd.DataFrame(data_df)

    def __str__(self):
        return "The portfolio's risk is {:.2%}, returns {:.2%} annually, and " \
               "has a beta of {:.2f} in correlation to the S&P 500. " \
               "The current sharpe ratio is {:.2f}.The optimal weights for this group of stocks are {}.".format(
            self.get_portfolio_risk(self.portfolio, self.num_shares, self.start_date, self.end_date, self.freq),
            self.get_portfolio_return(self.portfolio, self.num_shares, self.start_date, self.end_date, self.freq),
            self.get_portfolio_beta(self.portfolio, self.num_shares, self.start_date, self.end_date, self.freq),
            self.sharpe_ratio(self.portfolio, self.num_shares, self.start_date, self.end_date, self.freq),
            self.optimize_portfolio(self.portfolio, self.num_shares, self.start_date, self.end_date, self.freq,
                                    self.index_stock))

    def last_element(self, list_of_items):
        return list_of_items[-1]

    def get_price_df(self, portfolio, num_shares, start_date, end_date, freq):
        df = pd.DataFrame()
        for stock, numb in zip(portfolio, num_shares):
            time.sleep(1)
            df[stock] = yf.download(tickers=stock, start=start_date, end=end_date)["Adj Close"]
        if freq == "D":
            return pd.DataFrame(df)
        else:
            df.resample(rule=freq).apply(StockPortfolioAnalysis.last_element)
            return pd.DataFrame(df)

    def get_return_df(self):
        global data_df
        returns_df = data_df.pct_change()
        return returns_df

    def get_average_daily_return_df(self):
        returns_df = self.get_return_df()
        average_daily_return = returns_df.mean(axis=0)
        return pd.DataFrame(average_daily_return)

    def get_average_weekly_return_df(self):
        returns_df = self.get_return_df()
        average_weekly_return = returns_df.mean(axis=0)
        return pd.DataFrame(average_weekly_return)

    def get_average_monthly_return_df(self):
        returns_df = self.get_return_df()
        average_monthly_return = returns_df.mean(axis=0)
        return pd.DataFrame(average_monthly_return)

    def get_average_quarterly_return_df(self):
        returns_df = self.get_return_df()
        average_quarterly_return = returns_df.mean(axis=0)
        return pd.DataFrame(average_quarterly_return)

    def get_stock_average_annual_return(self, freq):
        average_daily_return = self.get_average_daily_return_df()
        average_weekly_return = self.get_average_weekly_return_df()
        average_monthly_return = self.get_average_monthly_return_df()
        average_quarterly_return = self.get_average_quarterly_return_df()
        if freq == "D":
            average_annual_return = average_daily_return * 252
            return pd.DataFrame(average_annual_return)
        elif freq == "W":
            average_annual_return = average_weekly_return * 52
            return pd.DataFrame(average_annual_return)
        elif freq == "M":
            average_annual_return = average_monthly_return * 12
            return pd.DataFrame(average_annual_return)
        elif freq == "Q":
            average_annual_return = average_quarterly_return * 4
            return pd.DataFrame(average_annual_return)

    def get_stock_average_annual_risk(self, freq):
        returns_df = self.get_return_df()
        if freq == "D":
            var = returns_df.var()
            annualized_var = var * 252
            return pd.DataFrame(np.sqrt(annualized_var))
        elif freq == "W":
            var = returns_df.var()
            annualized_var = var * 52
            return pd.DataFrame(np.sqrt(annualized_var))
        elif freq == "M":
            var = returns_df.var()
            annualized_var = var * 12
            return pd.DataFrame(np.sqrt(annualized_var))
        elif freq == "Q":
            var = returns_df.var()
            annualized_var = var * 4
            return pd.DataFrame(np.sqrt(annualized_var))

    def get_portfolio_annual_matrix(self, freq):
        returns_df = self.get_return_df()
        if freq == "D":
            df_var_cov_matrix = returns_df.cov()
            df_annual_var_cov_matrix = df_var_cov_matrix * 252
            return pd.DataFrame(df_annual_var_cov_matrix)
        elif freq == "W":
            df_var_cov_matrix = returns_df.cov()
            df_annual_var_cov_matrix = df_var_cov_matrix * 52
            return pd.DataFrame(df_annual_var_cov_matrix)
        elif freq == "M":
            df_var_cov_matrix = returns_df.cov()
            df_annual_var_cov_matrix = df_var_cov_matrix * 12
            return pd.DataFrame(df_annual_var_cov_matrix)
        elif freq == "Q":
            df_var_cov_matrix = returns_df.cov()
            df_annual_var_cov_matrix = df_var_cov_matrix * 4
            return pd.DataFrame(df_annual_var_cov_matrix)

    def get_weights(self, portfolio, num_shares, start_date, end_date):
        total_amount_invested = 0
        df = pd.DataFrame()
        current_weights = []
        for stock, numb in zip(portfolio, num_shares):
            df[stock] = yf.download(tickers=stock, start=start_date, end=end_date)["Adj Close"]
            total_amount_invested += float(numb) * df[stock].iloc[-1]
        for stock, numb in zip(portfolio, num_shares):
            weight = float(numb) * df[stock].iloc[-1] / total_amount_invested
            current_weights.append(weight)
        return current_weights

    def get_portfolio_return(self, portfolio, num_shares, start_date, end_date, freq, current_weights=None):
        if current_weights is None:
            current_weights = self.get_weights(portfolio, num_shares, start_date, end_date)
        average_annual_return = self.get_stock_average_annual_return(freq)
        return np.dot(current_weights, average_annual_return)

    def get_portfolio_risk(self, portfolio, num_shares, start_date, end_date, freq, current_weights=None):
        if current_weights is None:
            current_weights = self.get_weights(portfolio, num_shares, start_date, end_date)
        df_annual_var_cov_matrix = self.get_portfolio_annual_matrix(freq)
        annualized_portfolio_risk = np.dot(current_weights, np.dot(df_annual_var_cov_matrix, current_weights))
        return np.sqrt(annualized_portfolio_risk)

    def get_beta_df(self, portfolio, start_date, end_date, index_stock):
        global data_df
        betas = []
        data_df[index_stock] = yf.download(tickers=index_stock, start=start_date, end=end_date)["Adj Close"]
        df_returns_spy = data_df.pct_change()
        cov = df_returns_spy.cov()
        var = df_returns_spy[index_stock].var()

        for b in portfolio:
            beta = cov.loc[b, index_stock] / var
            betas.append(beta)

        beta_dict = {}
        for key, val in zip(portfolio, betas):
            beta_dict[key] = val

        beta_df = pd.DataFrame.from_dict(beta_dict, orient='index')
        data_df = data_df.drop(columns=[index_stock], axis=1)
        return beta_df

    def get_portfolio_beta(self, portfolio, num_shares, start_date, end_date, index_stock, current_weights=None):
        if current_weights is None:
            current_weights = self.get_weights(portfolio, num_shares, start_date, end_date)
        beta_df = self.get_beta_df(portfolio, start_date, end_date, index_stock)
        beta = np.dot(current_weights, beta_df)
        return round(float(beta), 2)

    def treynor_ratio(self, portfolio, num_shares, start_date, end_date, freq, index_stock, risk_free_rate=0.0006,
                      current_weights=None):
        if current_weights is None:
            current_weights = self.get_weights(portfolio, num_shares, start_date, end_date)
        average_annual_return = self.get_stock_average_annual_return(freq)
        portfolio_return = np.dot(current_weights, average_annual_return)
        portfolio_beta = self.get_portfolio_beta(portfolio, num_shares,
                                                 start_date, end_date, index_stock, current_weights)
        return float((portfolio_return - risk_free_rate)/portfolio_beta)

    def sharpe_ratio(self, portfolio, num_shares, start_date, end_date, freq, risk_free_rate=0.0006,
                     current_weights=None):
        if current_weights is None:
            current_weights = self.get_weights(portfolio, num_shares, start_date, end_date)
        average_annual_return = self.get_stock_average_annual_return(freq)
        portfolio_return = np.dot(current_weights, average_annual_return)
        portfolio_matrix = self.get_portfolio_annual_matrix(freq)
        annualized_portfolio_risk = np.dot(current_weights, np.dot(portfolio_matrix, current_weights))
        portfolio_risk = np.sqrt(annualized_portfolio_risk)
        return float((portfolio_return - risk_free_rate) / portfolio_risk)

    def save_spreadsheet(self, portfolio, num_shares, start_date, end_date, freq, index_stock):
        df_returns = self.get_return_df()
        df_annual_var_cov_matrix = self.get_portfolio_annual_matrix(freq)
        average_annual_return = self.get_stock_average_annual_return(freq)
        average_annual_risk = self.get_stock_average_annual_risk(freq)
        annualized_portfolio_return = self.get_portfolio_return(portfolio, num_shares, start_date, end_date, freq)
        portfolio_risk = self.get_portfolio_risk(portfolio, num_shares, start_date, end_date, freq)
        optimal_portfolio = self.optimize_portfolio(portfolio, num_shares, start_date, end_date, freq, index_stock)
        clustered_portfolio = self.cluster_stocks(portfolio, freq)
        beta = self.get_portfolio_beta(portfolio, num_shares, start_date, end_date, freq)
        sharpe_ratio = self.sharpe_ratio(portfolio, num_shares, start_date, end_date, freq)
        treynor_ratio = self.treynor_ratio(portfolio, num_shares, start_date, end_date, freq, index_stock)
        optimal_sharpe_ratio = optimal_portfolio[1]
        optimal_treynor_ratio = optimal_portfolio[3]

        writer = pd.ExcelWriter(
            r"C:\Users\jorda\OneDrive\Documents\
            Work\Side works\JMM Group LLC\Portfolios\Personal_Test_Portfolio.xlsx",
            engine='xlsxwriter')

        portfolio_overview = pd.DataFrame((round(float(portfolio_risk), 2),
                                           round(float(annualized_portfolio_return), 2), beta,
                                           round(float(sharpe_ratio), 2), round(float(treynor_ratio), 2),
                                           optimal_sharpe_ratio, optimal_treynor_ratio),
                                          columns=["Current Portfolio"],
                                          index=["Annualized Portfolio Risk",
                                                 "Annualized Portfolio Return",
                                                 "Portfolio Beta (S&P 500)",
                                                 "Portfolio Sharpe Ratio",
                                                 "Portfolio Treynor Ratio",
                                                 "Optimal Sharpe Ratio",
                                                 "Optimal Treynor Ratio"])

        optimal_sharpe_portfolio = pd.DataFrame.from_dict(optimal_portfolio[0],
                                                          orient='index', columns=["Optimal Sharpe Portfolio"])
        optimal_sharpe_portfolio["Amount to Invest"] = optimal_sharpe_portfolio * 2000
        optimal_sharpe_portfolio["Optimal Sharpe Portfolio"] = optimal_sharpe_portfolio["Optimal Sharpe Portfolio"].map("{:.2%}".format)
        optimal_sharpe_portfolio["Amount to Invest"] = optimal_sharpe_portfolio["Amount to Invest"].map("${:.4}".format)
        optimal_sharpe_portfolio.to_excel(writer, sheet_name="Optimal Sharpe Portfolio")

        optimal_treynor_portfolio = pd.DataFrame.from_dict(optimal_portfolio[2], orient='index', columns=["Optimal Treynor Portfolio"])
        optimal_treynor_portfolio["Amount to Invest"] = optimal_treynor_portfolio * 2000
        optimal_treynor_portfolio["Optimal Treynor Portfolio"] = optimal_treynor_portfolio["Optimal Treynor Portfolio"].map("{:.2%}".format)
        optimal_treynor_portfolio["Amount to Invest"] = optimal_treynor_portfolio["Amount to Invest"].map("${:.4}".format)
        optimal_treynor_portfolio.to_excel(writer, sheet_name="Optimal Treynor Portfolio")


        average_annual_return = average_annual_return.rename(columns={0: "Annualized Average"})
        average_annual_risk = average_annual_risk.rename(columns={0: "Annualized Average Risk"})

        returns_overview = pd.concat([average_annual_return, average_annual_risk], axis=1)

        portfolio_overview.to_excel(writer, sheet_name="Portfolio Overview")
        df_returns.applymap(lambda x: str(round(x * 100, 2)) + "%",
                            na_action='ignore').to_excel(writer, sheet_name="Stock Returns")
        returns_overview.applymap(lambda x: str(round(x * 100, 2)) + "%",
                                  na_action='ignore').to_excel(writer, sheet_name="Averages")
        df_annual_var_cov_matrix.style.to_excel(writer, sheet_name="Cov-Var Matrix", float_format="%.4f")
        clustered_portfolio.to_excel(writer, sheet_name="Scaled Portfolio")

        writer.save()

        return "Done"

    def simulate_weights(self, portfolio):
        # random.seed(100)
        weights = []
        normalized_weights = []
        for i in range(len(portfolio)):
            weights.append(random.random())
        for j in weights:
            normalized_weights.append(j / sum(weights))
        return normalized_weights

    def optimize_portfolio(self, portfolio, num_shares, start_date, end_date, freq, index_stock, n=100):
        sharpe_optimal_weights = []
        treynor_optimal_weights = []
        best_sharpe_ratio = 0
        best_treynor_ratio = 0
        best_sharpex = 0
        best_sharpey = 0
        best_treynorx = 0
        best_treynory = 0
        best_sharpe_book = {}
        best_treynor_book = {}
        portfolio_returns = []
        portfolio_risks = []
        average_annual_return = self.get_stock_average_annual_return(freq)
        average_annual_matrix = self.get_portfolio_annual_matrix(freq)

        for i in range(n):
            test_weights = self.simulate_weights(portfolio)
            portfolio_return = np.dot(test_weights, average_annual_return)
            portfolio_returns.append(float(portfolio_return))
            portfolio_risk = np.sqrt(np.dot(test_weights, np.dot(average_annual_matrix, test_weights)))
            portfolio_risks.append(portfolio_risk)
            current_sharpe_ratio = self.sharpe_ratio(portfolio, num_shares, start_date, end_date, freq,
                                                     current_weights=test_weights)
            current_treynor_ratio = self.treynor_ratio(portfolio, num_shares, start_date, end_date, freq, index_stock,
                                                       current_weights=test_weights)
            if current_sharpe_ratio > best_sharpe_ratio:
                best_sharpe_ratio = current_sharpe_ratio
                sharpe_optimal_weights = test_weights
                best_sharpex = portfolio_risk
                best_sharpey = portfolio_return

            if current_treynor_ratio > best_treynor_ratio:
                best_treynor_ratio = current_treynor_ratio
                treynor_optimal_weights = test_weights
                best_treynorx = portfolio_risk
                best_treynory = portfolio_return

        for key, val in zip(portfolio, treynor_optimal_weights):
            best_treynor_book[key] = val

        for key, val in zip(portfolio, sharpe_optimal_weights):
            best_sharpe_book[key] = val

        plt.figure(figsize=(8, 6))
        plt.scatter(x=portfolio_risks, y=portfolio_returns, marker='.', edgecolors='black', color='red')
        plt.scatter(x=best_sharpex, y=best_sharpey, color="green")
        plt.scatter(x=best_treynorx, y=best_treynory, color="red")
        plt.xlabel('Portfolio Risk')
        plt.ylabel('Portfolio Return')
        plt.title('Portfolio Risk-Portfolio Return')
        plt.savefig(r"C:\Users\jorda\OneDrive\Documents\Work\Side works\JMM Group LLC\Portfolios\Graphs\Markowitz_Analysis.png")

        return best_sharpe_book, round(float(best_sharpe_ratio), 2), best_treynor_book, round(float(best_treynor_ratio), 2), \
               portfolio_returns, portfolio_risks

    def cluster_stocks(self, portfolio, freq):
        returns = self.get_stock_average_annual_return(freq)
        risks = self.get_stock_average_annual_risk(freq)

        risks = risks.rename(columns={0: "Risks"})
        returns = returns.rename(columns={0: "Returns"})

        fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(20, 7))
        fig.tight_layout()
        ax1 = ax[0, 0]
        ax2 = ax[0, 1]
        ax3 = ax[1, 0]
        ax4 = ax[1, 1]

        ax1.scatter(x=risks, y=returns)
        ax1.set_title("Risks-Returns")
        ax1.set_xlabel("Risks")
        ax1.set_ylabel("Returns")
        df_risks_returns = pd.concat([risks, returns], axis=1)

        # use MinMaxScaler to normalize both risks and returns for the 26 stocks
        scaler = MinMaxScaler()

        scaled_data = scaler.fit_transform(df_risks_returns)
        df_scaled_data = pd.DataFrame(scaled_data, columns=["Scaled Risks", "Scaled Returns"], index=[portfolio])
        ax2.scatter(x=df_scaled_data["Scaled Risks"], y=df_scaled_data["Scaled Returns"])
        ax2.set_title("Scaled Risks-Returns")
        ax2.set_xlabel("Scaled Risks")
        ax2.set_ylabel("Scaled Returns")

        # Cluster Scaled Data
        k_means_object = KMeans(n_clusters=6, max_iter=1000)
        clustered_data = k_means_object.fit(df_scaled_data)

        # Cluster labels
        df_scaled_data["Cluster Label"] = clustered_data.labels_

        # Plot results
        ax3.scatter(x=df_scaled_data["Scaled Risks"], y=df_scaled_data["Scaled Returns"],
                    c=df_scaled_data["Cluster Label"])
        ax3.set_title("Clustered Scaled Risks-Returns")
        ax3.set_xlabel("Scaled Risks")
        ax3.set_ylabel("Scaled Returns")

        # Annotate stocks tickers on scatterplot
        for i, txt in enumerate(portfolio):
            ax3.annotate(txt, (df_scaled_data["Scaled Risks"][i] * 1.01, df_scaled_data["Scaled Returns"][i] * 1.01))
            ax2.annotate(txt, (df_scaled_data["Scaled Risks"][i] * 1.01, df_scaled_data["Scaled Returns"][i] * 1.01))
            ax1.annotate(txt, (df_risks_returns["Risks"][i] * 1.01, df_risks_returns["Returns"][i] * 1.01))

        # for a range of k, calculate
        # within-clusters sum of squares
        wcss = []
        for k in range(2, len(portfolio) - 1):
            k_means_object = KMeans(n_clusters=k, max_iter=1000)
            clustered_data = k_means_object.fit(df_scaled_data)
            wcss.append(clustered_data.inertia_)

        ks = range(2, len(portfolio) - 1)
        # ELBOW METHOD (Best k is at the elbow on the graph) to find best ncluster
        ax4.plot(ks, wcss, "*-")
        ax4.set_title("WCSS")
        ax4.set_xlabel("K")
        ax4.set_ylabel("Sum of Squares")
        plt.savefig(
            r"C:\Users\jorda\OneDrive\Documents\Work\Side works\JMM Group LLC\Portfolios\Graphs\Clustered_Analysis.png")
        return df_scaled_data


if __name__ == "__main__":
    choice = ''
    # FIXME 4-a: Print the program name.
    print('Portfolio Evaluation Program')
    # portfolio = input("Enter the list of stocks in your portfolio separated by a space. (e.g. AAPL MMM TSLA) enter Q to quit:")
    # num = input("Enter a list of the number of shares you invested respect to the order above.")
    # freq = input("What time constraint would you like to analyze by: \'D\' \'W\' \'M\' or \'Q\'")
    portfolio1 = "EVH FB MSFT SPY SPYG INDS EQNR GLNCY AAPL ARE IBN SNAP SDY EMR"
    portfolio2 = "EVH FB MSFT SPY SPYG INDS"
    num = "8 0.919447 1 1.42 1.01 1.02 3 5 1 1 4 2 1 1"
    num2 = "3 20.9"
    freq1 = "D"
    while portfolio1 != 'Q':
        portfolio1 = portfolio1.split()
        num = num.split()
        tester = StockPortfolioAnalysis(portfolio1, num_shares=num, start_date='2017-01-01', end_date='2022-02-01', freq=freq1, index_stock='^GSPC')
        tester.get_price_df(portfolio1, num_shares=num, start_date='2017-01-01', end_date='2022-02-01', freq=freq1)
        #tester.optimize_portfolio(portfolio1, num_shares=num, start_date='2020-11-01', end_date='2021-11-01', freq=freq1)
        portfolio1 = input(
            "Enter the list of stocks in your portfolio separated by a space. (e.g. AAPL MMM TSLA) enter Q to quit:")
        if portfolio1 != 'Q':
            num = input("Enter a list of the number of shares you invested, in respect to the order above.")
        else:
            pass