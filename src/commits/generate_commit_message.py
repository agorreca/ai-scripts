import sys
import subprocess
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def generate_commit_message(diff_file):
    with open(diff_file, 'r') as file:
        diff = file.read()
    prompt = (
        f"Generate a detailed conventional commit message based on the following git diff:\n{diff}\n"
        "The commit message should include:\n"
        "- A type (e.g., feat, fix, docs, style, refactor, test, chore)\n"
        "- A short description\n"
        "- A detailed description of the changes made\n"
        "- Any breaking changes (if applicable)\n"
        "- The ticket number ATM-123\n"
        "Commit message format:\n"
        "type(scope): Short description\n\n"
        "Detailed description...\n\n"
        "BREAKING CHANGE: Description of breaking changes (if any)\n\n"
        "Ticket: ATM-123"
    )
    try:
        result = subprocess.run(
            ['ollama', 'run', 'codegeex4', prompt],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'  # Replace encoding errors with a placeholder
        )
        stdout_output = result.stdout.strip() if result.stdout else ""
        return stdout_output
    except subprocess.CalledProcessError as e:
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_commit_message.py <diff_file>")
        sys.exit(1)

    diff_file = sys.argv[1]
    commit_message = generate_commit_message(diff_file)

    if commit_message:
        print(commit_message)  # Directly print the commit message for the batch script to capture
    else:
        print("Failed to generate commit message.")
