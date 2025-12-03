import subprocess
# os for directory operations & subprocess for executing shell commands
from pathlib import Path
# pathlib to iterate through directories

# get path from user
repo_path = str(input("Enter a path: "))

def update_git_repo():
    path = Path(repo_path)
    print(f"Checking subdirectories from {path} \n")

    # for every subdirectory within path iterate through all subdirectories in supplied path
    for sub_directory in path.iterdir():
        # if dir is a git repo (check for .git)
        if sub_directory.is_dir and (sub_directory/".git").exists():
            # run git command and
            result = subprocess.run(["git", "-C", str(sub_directory), "pull"], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✓ Pulled {sub_directory.name}")
            else:
                # Show the actual error message
                error_lines = result.stderr.strip().splitlines()
                first_line = error_lines[0] if error_lines else "unknown error"
                print(f"✗ Failed {sub_directory.name} – {first_line}")

        else:
            print(f"✦ Skipping {sub_directory.name} - not a git repository")

update_git_repo()

