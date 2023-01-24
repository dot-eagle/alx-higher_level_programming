#!/usr/bin/python3

def safe_function(fct, *args):
    sol = 0

    while True:
        for s in range(1, 3):
            try:
                if s > a:
                    raise Exception("Too far")
                else:
                    sol += (a**b) / s

            except Exception:
                sol = a + b
                break
        return (sol)
