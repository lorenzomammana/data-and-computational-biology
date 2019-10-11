import numpy as np
import collections

odedict = {}


def generate_prod(reactants, reaction_rate, products):
    for p in products:
        y = "d[" + p + "]/dt"
        f = str(reaction_rate)

        for r in reactants:
            f += "[" + r + "]"

        if y in odedict:
            odedict[y] += " + " + f
        else:
            odedict[y] = f


def generate_react(reactants, reaction_rate, products):
    output = []
    for r in reactants:
        y = "d[" + r + "]/dt"
        f = "-" + str(reaction_rate)

        for r2 in reactants:
            f += "[" + r2 + "]"

        if y in odedict:
            odedict[y] += " " + f
        else:
            odedict[y] = f


def generate_ode(reactants, reaction_rate, products):
    generate_prod(reactants, reaction_rate[0], products)
    generate_react(reactants, reaction_rate[0], products)

    if len(reaction_rate) == 2:
        generate_prod(products, reaction_rate[1], reactants)
        generate_react(products, reaction_rate[1], reactants)


if __name__ == '__main__':
    generate_ode(["S", "E"], ["K1", "K_1"], ["C"])
    generate_ode(["C"], ["K2"], ["P", "E"])

    for k, v in collections.OrderedDict(sorted(odedict.items())).items():
        print(k + " = " + v)
