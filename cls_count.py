import pandas as pd

# Load the CSV
df = pd.read_csv("/media/dibakar/DATA/Training_point_process/Point_process_3/tile_12/combined_Training_Data.csv")

# Count occurrences of each class
class_counts = df['LC'].value_counts()

# Print result
print(class_counts)






