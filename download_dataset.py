import kagglehub
import os
import shutil

# Create data folder if it doesn't exist
data_folder = "data"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    print(f"Created {data_folder} folder")

# Download latest version
print("Downloading IBM HR Analytics Attrition dataset...")
path = kagglehub.dataset_download("pavansubhasht/ibm-hr-analytics-attrition-dataset")

print("Path to dataset files:", path)

# Move files to data folder
if os.path.exists(path):
    # List all files in the downloaded path
    files = os.listdir(path)
    print(f"Found {len(files)} file(s) in the dataset:")
    
    for file in files:
        source_file = os.path.join(path, file)
        destination_file = os.path.join(data_folder, file)
        
        # Copy file to data folder
        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_file)
            print(f"Copied {file} to {data_folder}/")
        elif os.path.isdir(source_file):
            # If it's a directory, copy the entire directory
            if os.path.exists(destination_file):
                shutil.rmtree(destination_file)
            shutil.copytree(source_file, destination_file)
            print(f"Copied directory {file} to {data_folder}/")
    
    print(f"\nAll dataset files have been stored in the '{data_folder}' folder")
    
    # List contents of data folder
    print(f"\nContents of {data_folder} folder:")
    for item in os.listdir(data_folder):
        item_path = os.path.join(data_folder, item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f"  📄 {item} ({size:,} bytes)")
        else:
            print(f"  📁 {item}/")
else:
    print("Error: Dataset path not found")
