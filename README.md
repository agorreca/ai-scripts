# Commit Message Automation

This project automates the generation of conventional commit messages using a set of shell and Python scripts. The automation ensures consistent and detailed commit messages, improving the readability and maintainability of the project's commit history.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
    - [check_and_run_ollama.sh](#check_and_run_ollamash)
    - [generate_commit.sh](#generate_commitsh)
    - [generate_commit_message.bat](#generate_commit_messagebat)
    - [generate_commit_message.py](#generate_commit_messagepy)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, clone the repository to your local machine:

```
git@github.com:agorreca/ai-scripts.git
cd ai-scripts
```

Ensure that you have the following dependencies installed:

- Python 3.x
- Git
- Ollama service

## Usage

### `check_and_run_ollama.sh`

This script checks if the Ollama service is running on port 11434. If the service is not running, it starts Ollama and waits for 5 seconds to ensure it is fully operational.

```
./src/commits/check_and_run_ollama.sh
```

### `generate_commit.sh`

This script automates the commit process by:

1. Ensuring Ollama is running by calling `check_and_run_ollama.sh`.
2. Retrieving the git diff of the staged changes.
3. Using a Python script to generate a commit message based on the diff.

To use this script, stage your changes with `git add` and then run:

```
./src/commits/generate_commit.sh
```

### `generate_commit_message.bat`

This batch script is similar to the shell script but designed for Windows environments. It calls `generate_commit_message.py` to generate a conventional commit message.

```
./src/commits/generate_commit_message.bat
```

### `generate_commit_message.py`

This Python script reads the git diff from a file and sends a prompt to the Ollama service to generate a conventional commit message. The generated message includes the type, short description, detailed description of changes, and any breaking changes.

```
python src/commits/generate_commit_message.py <diff_file>
```

## Contributing

We welcome contributions to enhance the functionality of this project. Please fork the repository, create a new branch, and submit a pull request with your changes. Ensure your code adheres to the existing style and includes tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
