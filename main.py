from calculate_time import distance_matrix
from data import generate_data

# generate array to sample from
sampling_array = generate_data.create_sampling_array()
# draw samples with monte carlo simulation
samples = generate_data.monte_carlo(3,len(sampling_array), sampling_array)
# calculate distance between region and sahlgrenska using google distance matrix
distances = distance_matrix.calculate_distances(samples)
print(distances)
