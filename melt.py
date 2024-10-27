import pandas as pd

#Step 3
#Here the data file exported from merge_device will come

#use this data to block on MC

df = pd.read_csv('23-oct.csv')

# Merge the DataFrame to a single column
melted_df = df.melt(var_name='column', value_name='fingerprint')
melted_df = melted_df.drop('column', axis=1)

# Save to a new Excel file final file for Mission control
melted_df.to_csv('flattened_fingerprints_23oct.csv', index=False)
