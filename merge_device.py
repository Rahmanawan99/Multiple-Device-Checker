import pandas as pd

#Step 2
#Here the data will come from umerge.py

# Function to save device fingerprints in separate columns and merge with account numbers
def save_device_ids_in_separate_cells(accounts_csv, devices_csv, output_csv):
    accounts_df = pd.read_csv(accounts_csv)
    devices_df = pd.read_csv(devices_csv)
    
    # Merge both dataframes on 'account' column in the required data in accounts_to_block.csv
    merged_df = pd.merge(devices_df[['device_fingerprint', 'account']], accounts_df, on='account', how='right')

    expanded = merged_df.pivot_table(index='account', columns=merged_df.groupby('account').cumcount(), 
                                     values='device_fingerprint', aggfunc='first')

    # saveing users with multiple fingerprints
    expanded.columns = [f'device_fingerprint_{i+1}' for i in range(expanded.shape[1])]
    expanded.reset_index(inplace=True)
    result_df = pd.merge(accounts_df, expanded, on='account', how='left')

    # Save the updated dataframe to a new CSV file
    result_df.to_csv(output_csv, index=False)
    print(f"Saved updated data with separate device fingerprint columns to {output_csv}")

# Example usage
devices_csv = 'unmerged_23.csv'  # Original file with all merged data
accounts_csv = 'Accounts_to_Block.csv'  # CSV with exclusive account numbers to block
output_csv = '23-oct.csv'  # Output CSV file 
save_device_ids_in_separate_cells(accounts_csv, devices_csv, output_csv)
