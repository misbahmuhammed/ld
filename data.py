import pandas as pd
columns = ['Batch', 'Course Type', 'Course Name', 'Duration', 'Online/Offline', 'Trainer']

# Create an empty DataFrame with the specified columns
df = pd.DataFrame(columns=columns)

# Save the DataFrame to an Excel file
df.to_excel('allocated_courses.xlsx', index=False)