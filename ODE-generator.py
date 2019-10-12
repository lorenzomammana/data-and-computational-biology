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
    """
    :param reactants: List of strings representing reactants names
    :param reaction_rate: List of exactly 2 strings or integers representing the reaction rate of both forward and
    backward chemical reaction (if possible)
    :param products: List of strings representing products names
    :return: Add the ODEs corresponding the given set of chemical reactions to the global variable odedict
    """
    print_reaction(reactants, reaction_rate[0], products)
    generate_prod(reactants, reaction_rate[0], products)
    generate_react(reactants, reaction_rate[0], products)

    if len(reaction_rate) == 2:
        print_reaction(products, reaction_rate[1], reactants)
        generate_prod(products, reaction_rate[1], reactants)
        generate_react(products, reaction_rate[1], reactants)


def print_reaction(reactants, reaction_rate, products):
    output = ""
    output += " + ".join(reactants)
    output += " --[" + str(reaction_rate) + "]-> "
    output += " + ".join(products)

    print(output)


if __name__ == '__main__':
    generate_ode(["S", "E"], ["K1", "K_1"], ["C"])
    generate_ode(["C"], ["K2"], ["P", "E"])

    print("-----------")

    for k, v in collections.OrderedDict(sorted(odedict.items())).items():
        print(k + " = " + v)
