import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
from owslib.wcs import WebCoverageService

# Connect to the WCS service
wcs = WebCoverageService('https://wms.zh.ch/DEMWCS', version='1.0.0')

# Get the list of coverages
coverages = list(wcs.contents)

# Get the first coverage
coverage = wcs.contents[coverages[0]]

# Get the coverage data
response = wcs.getCoverage(identifier=coverage.id,  bbox=(8.5, 47.3, 8.6, 47.4), format='image/tiff', crs='EPSG:4326', width=1000, height=1000)

# Save the coverage data to a file
with open('aufgabe_10/output.tif', 'wb') as file:
    file.write(response.read())
    file.close()  # Ensure the file is closed

# Open the DTM file with rasterio
with rasterio.open('aufgabe_10/output.tif') as dtm_src:
    # Read the first band into an array
    dtm = dtm_src.read(1)

# Open the DOM file with rasterio
with rasterio.open('aufgabe_10/output.tif') as dom_src:
    # Read the first band into an array
    dom = dom_src.read(1)

# Create a figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot the DTM data
show(dtm, ax=ax1, cmap='terrain', title='DTM')

# Plot the DOM data
show(dom, ax=ax2, cmap='terrain', title='DOM')

# Show the plot
plt.show()