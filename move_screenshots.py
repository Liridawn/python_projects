import os
import shutil

# Define the source directory and the target directory
source_dir = os.path.expanduser('/Users/liridonbislimi/Desktop')
target_dir = os.path.join(source_dir, 'Random screenshots')

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    
image_counter = 0

# Loop through each file in the source directory'
for file_name in os.listdir(source_dir):
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        image_counter += 1
        # Construct full file path
        source_file = os.path.join(source_dir, file_name)
        target_file = os.path.join(target_dir, file_name)

        # Move the file
        shutil.move(source_file, target_file)
        print(f'Moved {file_name} to {target_dir}')

if image_counter == 0:
    print("No screenshots on the desktop, all good.")
else: 
    print(f"{image_counter} screenshots were moved.")