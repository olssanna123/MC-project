import googlemaps
# API key for google maps
gmaps = googlemaps.Client(key='AIzaSyC16dY7QjOJl2isIQrDoO1uT5Ctit-F8wY')

# Calculate travel distances from sample to Sahlgrenska Universitetssjukhuset using Google Maps distance matrix
def calculate_distances(samples):
    distances = []
    i = 0
    while i < len(samples):
        parameter1 = samples[i]
        parameter2 = "Sahlgrenska Universitetssjukhuset"
        distance_result = gmaps.distance_matrix(parameter1, parameter2)
        # Parse returned json
        distance = distance_result["rows"][0]["elements"][0]['distance']['text']
        distances.append(distance)
        i += 1
    return distances