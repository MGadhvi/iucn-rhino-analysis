import os
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

def read_dataset(file_path):
    """Read the shapefile dataset."""
    print("Reading Data File:" + file_path)
    return gpd.read_file(file_path)

def plot_species_distribution(gdf, save_path):
    """Plot the distribution of species in a pie chart."""
    plt.figure(figsize=(6, 6))
    gdf['SCI_NAME'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Distribution of Species in Sample')
    plt.ylabel('')  # Hide the y-label
    plt.savefig(save_path)
    plt.close()  # Close the figure to free memory

def plot_sightings_count(gdf, save_path):
    """Plot the number of sightings per species in a bar chart."""
    sightings_count = gdf.groupby('SCI_NAME').size().reset_index(name='COUNT')
    
    plt.figure(figsize=(20, 20))
    sns.barplot(data=sightings_count, x='SCI_NAME', y='COUNT', palette='viridis')
    plt.title('Number of Sightings per SCI_NAME')
    plt.xlabel('Species Name')
    plt.ylabel('Number of Sightings')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()  # Close the figure to free memory

def plot_map(gdf, save_path):
    """Plot a map of sightings."""
    plt.figure(figsize=(20, 20))  # Adjust the figure size as needed
    ax = gdf.plot(column='SCI_NAME',  
                   cmap='viridis',  
                   legend=True,  
                   edgecolor='black')  

    plt.title('Map from Shapefile')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()  # Close the figure to free memory

# Main execution
if __name__ == "__main__":
    # Create the visualisations directory if it doesn't exist
    os.makedirs('../visualisations', exist_ok=True)  # Adjusted path to go up one level
    gdf = read_dataset('../data/data_0.shp')
    plot_species_distribution(gdf, '../visualisations/species_distribution.png')
    plot_sightings_count(gdf, '../visualisations/sightings_count.png')
    plot_map(gdf, '../visualisations/map_of_sightings.png')
