from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_metorite_analysis(
    df,
    # optional arguments
    min_long=110,
    max_long=155,
    min_lat=-45,
    max_lat=-10,
):
    log_mass = np.log(df['mass (g)'])

    fig = plt.figure()
    # setup map projection.
    m = Basemap(
        # Lower left corner longitude
        llcrnrlon=min_long,
        # Upper right corner longitude
        urcrnrlon=max_long,
        # Lower left corner latitude
        llcrnrlat=min_lat,
        # Upper right corner latitude
        urcrnrlat=max_lat,
        projection='mill',
    )
    # Draw in Austrlia and map lines
    m.drawcoastlines()
    m.fillcontinents()
    m.drawparallels(np.arange(-90,90,10),labels=[1,1,0,1])
    m.drawmeridians(np.arange(-180,180,10),labels=[1,1,0,1])

    # Convert your data to the Basemap coordinates and add it to the plot
    x, y = m(df['reclong'], df['reclat'])
    # Make the scatter dots size propotional to the mass
    plt.scatter(x, y, edgecolors='0', s=log_mass)
    plt.show()

    sns.kdeplot(np.log10(df['mass (g)']))
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('Australian_Metorite_Landings.csv')
    plot_metorite_analysis(df)