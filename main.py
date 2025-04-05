from calculate_travel import distance_matrix
from generate_data import generate_data
from region import random_pos_within_region

# coordinates for approximation region as tuples
# North east south west coordinates (latitude, longitude)
Ale = [(58.116472, 12.397922), (57.990763, 12.410281), (57.805393, 12.016147), (58.002408, 12.130130)]

# generate array to sample from
#sampling_array = generate_data.create_sampling_array()
# draw samples with monte carlo simulation
# samples = generate_data.monte_carlo(3,len(sampling_array), sampling_array)
# calculate distance between region and sahlgrenska using google distance matrix
#distances = distance_matrix.calculate_distances(samples)
#print(distances)

p = random_pos_within_region.random_point_within_region(Ale)
print(p)
