import numpy as np
import pandas as pd

# The generate_data for region and number of citizens
data = {
  "Kommun": ['Ale','Alingsås','Bengtsfors','Bollebygd','Borås','Dals-Ed','Essunga','Falköping','Färgelanda','Grästorp','Gullspång','Göteborg','Götene','Herrljunga','Hjo','Härryda','Karlsborg','Kungälv','Lerum','Lidköping','Lilla Edet','Lysekil','Mariestad','Mark','Mellerud','Munkedal','Mölndal','Orust','Partille','Skara','Skövde','Sotenäs','Stenungsund','Strömstad','Svenljunga','Tanum','Tibro','Tidaholm','Tjörn','Tranemo','Trollhättan','Töreboda','Uddevalla','Ulricehamn','Vara','Vårgårda','Vänersborg','Åmål','Öckerö'],
  "Folkmangd": [32446,42382,9138,9733,114592,4606,5656,32991,6434,5563,5119,604616,13218,9441,9258,39875,7061,49785,43706,40539,14426,13969,24647,35287,9165,10502,70534,15333,40730,18654,57763,9052,27862,13476,10759,12865,11332,12839,16146,11883,59073,9141,57045,25087,16066,12384,40012,12006,12819]
}

# Pseudo-random number generator
# Seed used for reproducibility
rng = np.random.default_rng(seed=12345)

# Function creates an array with the name of the region repeated the number of times as the number of it's citizens
def create_sampling_array():
    df = pd.DataFrame(data)
    sampling_array_list_of_lists = []
    sampling_array = []
    i = 0
    while i < 49:
        name_region = df.loc[i].at["Kommun"]
        nb_citizens = df.loc[i].at["Folkmangd"]
        item = [name_region]*nb_citizens
        sampling_array_list_of_lists.append(item)
        i += 1
    # Make it a single list
    j = 0
    k = 0
    while j < 49:
        while k < len(sampling_array_list_of_lists[j]):
            tmp = sampling_array_list_of_lists[j][k]
            sampling_array.append(tmp)
            k += 1
        j += 1
    return sampling_array

# Model/function return random integer between 0 and highest_number
def model(highest_number):
    return rng.integers(0, highest_number)

# Monte Carlo simulation
def monte_carlo(n, highest_number, sampling_array):
    samples = []
    j = 0
    while j <= n:
        index = model(highest_number)
        value = sampling_array[index]
        samples.append(value)
        j += 1
    return samples

