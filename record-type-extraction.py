import os

# Specify the folder path containing the text files
folder_path = "MDEC"

# Create a set to store unique record types
record_types = set()

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Extract the record type from the specified columns
            record_type = line[396:401].strip(';')

            # Add the record type to the set
            record_types.add(record_type)

# Print the unique record types
for record_type in record_types:
    print(record_type)
