import matplotlib.pyplot as plt

# plot form of approximation of region
def plot_approximation(region, point):
    # create closed loop by repeating the first coordinate
    region.append(region[0])
    # create lists of x and y values
    xs, ys = zip(*region)
    # plot figure
    plt.figure()
    plt.plot(xs,ys)
    plt.plot(point[0], point[1], 'r+')
    plt.show() # if you need...
