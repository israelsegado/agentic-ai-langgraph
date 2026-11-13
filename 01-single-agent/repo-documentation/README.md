# Repository Documentation Agent

A LangChain agent that analyzes local repositories and generates documentation proposals. The agent can traverse folder structures, find undocumented functions and classes, and generate a proposed README with description, installation, usage, and structure.

## Features

- **Repository traversal**: `list_tree` - Traverses folder structure up to specified depth
- **Undocumented detection**: `find_undocumented` - Detects functions and classes without docstrings
- **README generation**: Generates proposed README with description, installation, usage, and structure
- **Configurable proposals**: Save proposals to `proposals/` folder with indexed filenames
- **Smart filtering**: Automatically excludes `.git`, `__pycache__`, `.env`, and node_modules

## Project Structure

```
repo-documentation/
├── agent.py          # Main agent entry point
├── README.md         # This file
└── src/
│   ├── config.py         # Configuration: LLM_MODEL, SYSTEM_PROMPT, AGENT_PROMPT, USER_INPUT
│   ├── schemas.py        # Pydantic models: Readme, Docstring, Proposal
│   ├── tools.py          # LangChain tools for repo analysis
│   └── __pycache__/
└── proposals/          # Generated proposals folder
    ├── changes_1.md
    └── changes_2.md
```

## How It Works

1. The agent uses a Groq LLM model (configurable in `config.py`)
2. Three main tools are available:
   - `list_tree(path, depth)`: Lists all files and directories in a path
   - `read_file(path, max_lines)`: Reads lines inside a file
   - `find_undocumented(path, depth)`: Finds undocumented functions and classes
   - `write_proposal(path, content, index)`: Saves proposals to the proposals folder
3. The agent traverses the repository, finds undocumented items, and generates two proposals:
   - A proposed README with description, installation, usage, and structure
   - A list of undocumented functions and classes (missing docstrings)
4. Results are saved to the `proposals/` folder as markdown files

## Requirements

- Python 3.10+
- `langchain`, `langchain-groq`, `pydantic` installed
- `GROQ_API_KEY` environment variable configured
- Read access to the target repository

## Usage

Run the agent:

```bash
cd 01-single-agent/repo-documentation
python agent.py
```

The agent will prompt for input. Example workflow:

```text
Welcome to the repository documentation agent.

If you also want me to detect undocumented functions and classes answer "yes" or "no" after the following question.
Please enter the path of the project you want to analyze (e.g.: /home/user/project):
```

Answer "yes" or "no" to detect undocumented functions and classes. The agent will then:
1. Traverse the repository structure
2. Find undocumented functions and classes (if agreed)
3. Generate proposed README with repo structure and info
4. Save both proposals to the `proposals/` folder

## Customization

- **Change LLM model**: Modify `LLM_MODEL` in `src/config.py` (currently: `openai/gpt-oss-20b`)
- **Adjust system prompt**: Edit `SYSTEM_PROMPT` in `src/config.py`
- **Change traversal depth**: Modify `depth` parameter in tool calls
- **Point to different directory**: Pass different path to `list_tree` function

## Generated Proposals

Proposals are saved to the `proposals/` folder as markdown files:

- `changes_1.md`: First proposal containing the README and undocumented items
- `changes_2.md`: Second proposal (if multiple indexes are created)

Each proposal contains:
- README with description, installation, usage, and structure
- List of undocumented functions and classes with file paths and line numbers