#Project: Finding permutations and shallowness
#Class: Math 404, Combinatorics research
#Instructor: Dr. Alexander Woo, University of Idaho
#Authors: Noah Jones, Matthew Mills
#Date: 04/30/2019


import matplotlib.pyplot as plt

# This portion of code is a recursive algorithm that calculates all permutations of a given length
repository = []

def permute(partial_omega, omega_list):
    if len(omega_list) == 1:
        # print("base case")
        partial_omega.append(omega_list[0])
        repository.append(partial_omega)

    else:
        for digit in omega_list:
            # print(digit)
            new_partial_omega = partial_omega.copy()
            new_partial_omega.append(digit)
            # print(partial_omega)
            new_omega_list = omega_list.copy()
            new_omega_list.remove(digit)
            permute(new_partial_omega, new_omega_list)


# This code creates a list containing all cycles in a permutation

def find_cycles(omega):
    search_index = 0
    index_list = [i for i in range(len(omega))]

    visited_index = [0] * len(omega)
    cycle_list = []
    cycle = []

    count = 0

    while 0 in visited_index:
        # print(omega[search_index])
        cycle.append(omega[search_index])
        visited_index[search_index] = 1
        if omega[search_index] == search_index + 1:
            cycle_list.append(cycle)
            cycle = []
            # print('new cycle')
            if 0 in visited_index:
                search_index = visited_index.index(0)

        else:
            search_index = omega[search_index] - 1

        if omega[search_index] in cycle:
            cycle_list.append(cycle)
            cycle = []
            # print('new cycle')
            if 0 in visited_index:
                search_index = visited_index.index(0)

            continue

    return cycle_list

# This calculates the exceedence of a given permutation

def count_exceedance(perm):
    total_exceed = 0
    for element in perm:
        if int(element) > (perm.index(element)+1):
            exceed = (int(element) - (perm.index(element)+1))
            total_exceed = total_exceed + exceed

    return total_exceed

# This calculates the number of inversions in a given permutation

def count_inversions(perm):
    total_inversions = 0
    for element in perm:
        post_range = perm[perm.index(element)+1:]
        for post_element in post_range:
            if int(element) > int(post_element):
                total_inversions += 1

    return total_inversions

# This plots the cycle diagram of a given permutation says whether it is shallow or not

def plot_perm(perm, shallow_message):
    n = len(perm)
    perm_index = list(range(1, n+1))

    # Plots Horizontal Lines
    for number in perm:
        position = perm.index(number)+1
        plt.plot([number, position], [number, number], color=(0, 0, 1, .4), ls='-', linewidth=3)

    # Plots Vertical Lines
    for number in perm:
        position = perm.index(number)+1
        plt.plot([position, position], [position, number], color=(0, 0, 1, 1), ls='-', linewidth=3.5)

    # Plots Faint Points at x=y
    for number in perm:
        position = perm.index(number)+1
        plt.plot([position, position], [position, position], marker='.', color=(0, 0, 0, .35), markersize=6.5)

    # Plots Permutation Entries
    plt.plot(perm_index, perm, 'k.', markersize=15)

    # Settings For Figure
    plt.xticks(perm_index)
    plt.yticks(perm_index)
    plt.title(str(perm) + shallow_message)
    fig = plt.gcf()
    fig.set_size_inches(1*n, 1*n)
    # Show Figure
    plt.show()
    return

# This function calls the other functions, displays the information to the user,
# calculates whether or not a permutation is shallow, and displays the cycle diagram.

def shallow_graph(perm):
    perm_length = len(perm)
    string_perm = str(perm)
    # Counts/displays inversions, cycles, and exceedences
    inversions = count_inversions(perm)
    print("There are " + str(inversions) + " total inversions in " + string_perm)
    cycles = find_cycles(perm)
    num_cycles = len(cycles)
    print("There are " + str(num_cycles) + " cycles:")
    print(cycles)
    exceedances = count_exceedance(perm)
    print("The permutation " + string_perm + " has a total of " + str(exceedances) + " exceedances.")
    # Calculates reflection length of the permutation and whether it is shallow or not.
    reflection = perm_length - num_cycles
    shallow_message = " is not shallow"
    if exceedances == (reflection + inversions)/2:
        shallow_message = " is shallow"

    print(string_perm + shallow_message)
    # Calls the plot function and passes the shallow message
    plot_perm(perm, shallow_message)
    return


# The following code is the driver for this program

keyboard_input = "A"

while keyboard_input != "q":
    print("Enter 1 to view all permutations of a given length")
    print("Enter 2 to learn about a given permutation and see its cycle diagram.")
    print("Enter q to quit")
    keyboard_input = input()
    if keyboard_input == "q":
        continue

    elif keyboard_input == "1":
        print("Enter the length of the permutations:")
        keyboard_input = input()

        repository = []
        omega_list = [i for i in range(1, int(keyboard_input) + 1)]
        permute([], omega_list)
        print(repository)
        print("Number of permutations: " + str(len(repository)))

    elif keyboard_input == "2":
        print("Enter a permutation separated by spaces:")
        keyboard_input = input()
        keyboard_input = keyboard_input.split()
        keyboard_input = list(map(int, keyboard_input))

        shallow_graph(keyboard_input)

    else:
        print("Invalid input")
        
