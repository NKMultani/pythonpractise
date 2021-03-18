def withdraw(amountToWithdraw, currentBalance):
    if(amountToWithdraw > currentBalance):
        return "Insufficient Balance"
    newCurrentBalance = currentBalance - amountToWithdraw
    return newCurrentBalance