from collections import defaultdict

def reconcile_transactions(transactions):
    balances = defaultdict(int)

    for transaction in transactions:
        payer, amount, *recipients = transaction.split('/')
        amount = int(amount)

        if len(recipients) == 1:
            # Expense settlement
            recipient = recipients[0]
            balances[payer] -= amount
            balances[recipient] += amount
        else:
            # Loan repayment
            lender = payer
            for recipient in recipients:
                balances[lender] -= amount
                balances[recipient] += amount
                lender = recipient

    return balances

def print_dues(balances):
    dues = sorted([(payer, recipient, amount) for payer, amount in balances.items() if amount != 0])

    for payer, recipient, amount in dues:
        print(f"{payer}/{recipient}/{amount}")

if __name__ == "__main__":
    N = int(input())
    transactions = [input().strip() for _ in range(N)]

    balances = reconcile_transactions(transactions)
print_dues(balances)

if not balances:
    print("NO DUES.")
