import scipy.stats as stats


def main():
    lambdo = 3
    p_of_0 = stats.poisson.pmf(0, lambdo)
    p_of_more_than_0 = 1 - p_of_0
    print(f"P(X=0) = {p_of_0:.4f}, P(X>0) = {p_of_more_than_0:.4f}")


if __name__ == "__main__":
    main()