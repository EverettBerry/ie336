import matplotlib.pyplot as plt
import random


def binomial_model():
    up = 500
    price = 1
    stock = []

    for x in range(1000):
        if random.random() < up / 1000:
            price = price * 1.02
            up -= 1
        else:
            price = price / 1.02
            up += 1

        stock.append(price)

    plt.plot(stock)
    plt.ylabel('Stock price')
    plt.xlabel('Days')
    plt.show()

binomial_model()
