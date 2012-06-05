#!/usr/bin/python

import collections
import sys

routes = collections.defaultdict(list)

best_routes = []
best_score = 0

def recurse(route, score, current, visited, start_at):
  global best_routes
  global best_score

  if current == start_at:
    if score > best_score:
      best_routes = []
      best_score = score
    if score == best_score:
      print '%s\t%s' % (best_score, route)
      best_routes.append(list(route))
    return

  for outbound in routes[current]:
    code = outbound[0]
    dist = outbound[1]
    if code not in visited:
      route.append(code)
      visited.add(code)
      recurse(route, score + dist, code, visited, start_at)
      route.pop()
      visited.remove(code)

def main(args):
  route_data = open(args[1], 'r')
  for line in route_data:
    from_code, to_code, distance = line.split(',')
    routes[from_code].append([to_code, int(distance.strip())])

  start_at = args[2]
  visited = set()

  for outbound in routes[start_at]:
    code = outbound[0]
    dist = outbound[1]
    route = [start_at, code]
    visited.add(code)
    recurse(route, dist, code, visited, start_at)
    visited.remove(code)

if __name__ == "__main__":
  main(sys.argv)
