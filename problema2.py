from typing import List, Any


def evaluateFrauds(transactions: List[List[Any]]) -> List[int]:
    frauds = []
    evaluatedTransactions = []

    for transaction in transactions:
        evaluatedTransactions.append(transaction)
        if transaction[2] >= 10000:
            frauds.append(transaction[0])
            continue
        for evaluatedTransaction in evaluatedTransactions:
            if transaction[1] == evaluatedTransaction[1]:
                if transaction[3] != evaluatedTransaction[3] and (transaction[4]-evaluatedTransaction[4]) < 30:
                    frauds.append(transaction[0])
    return frauds


if __name__ == "__main__":
    lista = [
    [1, 1000, 500.00, "Vadodara", 0],
    [2, 1000, 500.00, "Mumbai", 5],
    [3, 1001, 500.00, "Mumbai", 10],
    [4, 1001, 10000.00, "Mumbai", 10],
    [5, 1002, 50.00, "Juarez", 20],
    [6, 1002, 50000.00, "Cancun", 49]
    ]

    print(evaluateFrauds(lista))