import pandas as pd

#This code is step 1 from the file downloaded from MissionControl

# Load the file > as downloaded from Tableau 
file_path = '23-Oct - Sheet 1.csv'
df = pd.read_csv(file_path)

# Fill missing values in the specific columns using forward fill this will add fingerprint from previous fingerptint 
columns_to_fill = ['device_fingerprint']
df[columns_to_fill] = df[columns_to_fill].ffill()

# Save the updated file
output_file_path = 'unmerged_23.csv'
df.to_csv(output_file_path, index=False)

print(f"Updated data saved to {output_file_path}")