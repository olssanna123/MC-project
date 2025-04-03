import matplotlib.pyplot as plt

# North east south west coordinates [latitude, longitude]
Ale = [[58.116472, 12.397922], [57.990763, 12.410281], [57.805393, 12.016147], [58.002408, 12.130130]]

# plot form of approximation of region
def plot_approximation(region):
    # create closed loop by repeating the first coordinate
    region.append(region[0])
    # create lists of x and y values
    xs, ys = zip(*region)
    # plot figure
    plt.figure()
    plt.plot(xs,ys)
    plt.show() # if you need...

plot_approximation(Ale)