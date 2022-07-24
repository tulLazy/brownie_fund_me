from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrence_fee = fund_me.getEntranceFee()
    print(entrence_fee)
    print(f"The current entrance fee is {entrence_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrence_fee})
    return fund_me


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    return fund_me


def main():
    fund()
    withdraw()
