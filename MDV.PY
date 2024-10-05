import pandas as pd

# Load the file
file_path = 'File_name.xlsx'
df = pd.read_excel(file_path, sheet_name='sheet_name')

# Print the first few rows to verify upload
df.head()

# Fill missing device_fingerprint values with the preceding non-null value this will help in merged cases
df['device_fingerprint'].fillna(method='ffill', inplace=True)

# Group by the identifier and count the number of accounts per device
device_account_counts = df.groupby('device_fingerprint').size()

#Filter devices with more than n accounts, make sure to replace n with a numeric value how many you want to filter.
devices_with_more_than_3_accounts = device_account_counts[device_account_counts > n]

#Retrieve the associated accounts for that identifier
associated_accounts = df[df['device_fingerprint'].isin(devices_with_more_than_3_accounts.index)]

# Save the result to a new Excel file
output_file_path = 'filtered_devices_accounts.xlsx' 
associated_accounts.to_excel(output_file_path, sheet_name='Filtered Data', index=False)

print(f"Filtered data saved to {output_file_path}")
