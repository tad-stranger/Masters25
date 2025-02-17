''' This code plots the HR diagram for data from a FITS table obtained by querying the Gaia telescope
 DR3 database to obtain all strong H-alpha sources within a 500 pc radius '''

from astropy.io import fits
from astropy.table import Table
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")  # Use the TkAgg backend
import matplotlib.pyplot as plt

#Read Data and convert to Pandas Data frame (df)
file = "Test query All HI sources-result.fits"
hdul = fits.open(file)
table = hdul[1]
data = Table.read(file, hdu=1 )
df = data.to_pandas()


#Calculate Coulour index (G_BP - G_RP)
df["Colour"] = df["BPmag"] - df["RPmag"]

#Plot the HR diagram
plt.scatter(df["Colour"], df["Gmag"], c = df['pwd'], s = 1, cmap='viridis')
plt.gca().invert_yaxis() #Brightest stars at the top - I think this is right
plt.xlabel(r"$G_{BP} - G_{RP}$")
plt.ylabel(r"$M_G$")
plt.colorbar(label = "Prob WD")
plt.title("HR diagram for all H-alpha sources with EW > 0.5 within 500 pc from GAIA DR3")
plt.show()














