# Imports NumPy library (numerical operations)and Pyplot module from Matplotlib (plotting results on a graph)
import numpy as np
import matplotlib.pyplot as plt

# Function to sample from a given range - used for exposure. This is based on a uniform distribution
def sample_from_exposure_range(minimum, maximum):
    return np.random.uniform(minimum, maximum)

# Function to sample from a given range - used for occurence. This is based on a triangular function
def sample_from_range(best, expected, worst):
    return np.random.triangular(best, expected, worst)

# Function to perform the simulation it also creates an empty list to store each loss from each iteration
def simulation(N):
    total_loss = []

    for _ in range(N):# Inside a loop running N times, it samples values 
        # Step 1: Sample from Node A (Exposure)
        exposure = sample_from_exposure_range(400,600)

        # Step 2: Sample from Node B (Occurrence)
        occurrence = sample_from_range(40, 50, 100)

        # Step 3: Calculate probability of an event
        probability_event = occurrence / exposure  # Assuming releative frequency

        # Step 4: Sample from Node C (Impact) conditionally
        impact = sample_from_range(300000, 400000, 1000000) if np.random.rand() < probability_event else 0 #samples the impact va lue from the triangular distributio. If a randomly generated number (from a uniform disribution) is less than calculated probability_event it samples the impact value. Otherwise it sets the impact to 0. 

        total_loss.append(impact)

    # Sort the losses in descending order
    sorted_losses = sorted(total_loss, reverse=True)

    # Create Loss Exceedance Curve
    exceedance_prob = np.arange(1, N + 1) / N

    # Plot the curve
    plt.plot(sorted_losses, exceedance_prob)
    plt.title('Loss Exceedance Curve')

    plt.xlabel('Loss')
    plt.ylabel('Probability')
    plt.show()

    # Calculates the required statistics
    num_iterations = N
    single_loss_average = np.mean(total_loss)
    min_possible_loss = np.min(total_loss)
    max_possible_loss = np.max(total_loss)
    average_possible_loss = np.mean(total_loss)

    lowest_frequency = min_possible_loss * (occurrence / exposure)
    average_frequency = average_possible_loss * (occurrence / exposure)
    highest_frequency = max_possible_loss * (occurrence / exposure)

    # Print the results
    print("Number of Iterations:", num_iterations)
    print("Single Loss Average:", single_loss_average)
    print("Minimum Possible Loss:", min_possible_loss)
    print("Max Possible Loss:", max_possible_loss)
    print("Average Possible Loss:", average_possible_loss)
    print("Lowest Frequency:", lowest_frequency)
    print("Average Frequency:", average_frequency)
    print("Highest Frequency:", highest_frequency)

# Set the number of iterations (N)
N = 100000

# Run the simulation and plot the Loss Exceedance Curve
simulation(N)