import os
import shutil

def merge_folders(base_dir):
    # Find all folders starting with 'sampled'
    sampled_folders = sorted(
        [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f)) and f.startswith('sampled')],
        key=lambda x: int(x.replace('sampled', ''))
    )

    # Create corresponding 'test_sampled' folders and copy contents
    for i, sampled_folder in enumerate(sampled_folders):
        # Determine the path to the 'sampled' folder
        sampled_folder_path = os.path.join(base_dir, sampled_folder)

        # Copy contents to all relevant 'test_sampled' folders
        for j in range(i, len(sampled_folders)):
            test_sampled_folder = f'test_{sampled_folders[j]}'
            test_sampled_folder_path = os.path.join(base_dir, test_sampled_folder)

            # Ensure the destination folder exists
            os.makedirs(test_sampled_folder_path, exist_ok=True)

            # Copy all files and directories from the sampled folder to the test_sampled folder
            for item in os.listdir(sampled_folder_path):
                src_path = os.path.join(sampled_folder_path, item)
                dst_path = os.path.join(test_sampled_folder_path, item)

                # Check if the item is a file or directory and copy accordingly
                if os.path.isdir(src_path):
                    shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
                else:
                    shutil.copy2(src_path, dst_path)

# Usage example
base_dir = '/home/cc/praxi/demos/ic2e_demo/demo_tagsets/data4_sampled_one_batch_batched_3'
merge_folders(base_dir)
