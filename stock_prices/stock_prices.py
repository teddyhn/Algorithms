#!/usr/bin/python

import argparse

def find_max_profit(prices):
  n = len(prices)
  
  max_profit_so_far = 0

  for i in range(n):

    for j in range(i + 1, n):
      temp = -(prices[i]) + prices[j]
      if max_profit_so_far == 0:
        max_profit_so_far = temp
      if temp > max_profit_so_far:
        max_profit_so_far = temp

  return max_profit_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))