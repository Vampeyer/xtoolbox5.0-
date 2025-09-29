import subprocess
import sys

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {' '.join(command)}: {e.stderr}", file=sys.stderr)
        sys.exit(1)

        
def main():
    # Stage all changes
    run_git_command(['git', 'add', '.'])
    
    # Commit changes with message 'autopush'
    run_git_command(['git', 'commit', '-m', 'autopushed it.'])
    
    # Push changes to the remote repository
    run_git_command(['git', 'push'])

if __name__ == "__main__":
    main()