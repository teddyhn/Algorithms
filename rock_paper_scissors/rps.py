#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = [['rock'], ['paper'], ['scissors']]

  ans = []

  if n == 0:
      return [ans]
  if n == 1:
      return plays

  for rps in rock_paper_scissors(n - 1):
    for play in plays:
        ans.append(rps + play)

  return ans

    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')