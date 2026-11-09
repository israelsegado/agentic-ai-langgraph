# Log Analyzer Agent

A LangChain agent that analyzes system logs using Groq LLMs. The agent can read log chunks, search for patterns, and count lines by severity level, returning a structured JSON report.

## Features

- **Log reading**: `read_log_chunk` - Reads specific portions of a log file
- **Pattern search**: `search_pattern` - Searches for regular expressions in the log and returns matches
- **Severity counting**: `count_by_level` - Counts lines with ERROR, WARNING and INFO patterns
- **Structured output**: Reports follow the `Report` schema with summary, incidents and recommended_actions
- **Configurable log directory**: By default points to `/var/log/`, but can be reconfigured for other directories

## Project Structure

```
log-analyzer/
├── agent.py          # Main agent entry point
├── README.md         # This file
└── src/
│   ├── config.py         # Configuration: SYSTEM_PROMPT, LLM_MODEL, AGENT_PROMPT
│   ├── generate_log.py   # Script to generate test mock logs
│   ├── schemas.py        # Pydantic models: Report, Incident, ConfidenceEnum
│   └── tools.py          # LangChain tools for log analysis
└── test-logs/          # Test logs directory (data.log mock)
```

## How It Works

1. The agent uses a Groq LLM model (configurable in `config.py`)
2. Three tools are available:
   - `read_log_chunk(filename, start, n_lines)`: Reads `n_lines` lines starting from `start`
   - `search_pattern(filename, regex, max_results)`: Searches a regex, returns total matches and examples
   - `count_by_level(filename)`: Counts lines with "fail", "warning" and "info"
3. The `SYSTEM_PROMPT` instructs the agent to use only the filename (not the full path), since the tools know logs are in `/var/log/`
4. Results follow the `Report` schema with:
   - `summary`: General analysis description
   - `incidents`: List of Incident objects (patterns, counts, evidence_lines, confidence)
   - `recommended_actions`: List of recommended actions

## Requirements

- Python 3.10+
- `langchain`, `langchain-groq`, `pydantic` installed
- `GROQ_API_KEY` environment variable configured
- Read access to files in `/var/log/` (some may require root permissions)

## Usage

Run the agent:

```bash
cd 01-single-agent/log-analyzer
python agent.py
```

The agent will prompt for input. Example usage:

```text
Make a report about the file 'messages' inside /var/log/
Search for 'Failed password' in the log file
Count INFO, WARNING and ERROR lines in boot.log
```

## Customization

- **Change LLM model**: Modify `LLM_MODEL` in `src/config.py`
- **Adjust system prompt**: Edit `SYSTEM_PROMPT` in `src/config.py`
- **Point to different log directory**: Modify `LOG_DIR` in `src/tools.py`
- **Use mock logs**: Run `python src/generate_log.py` to generate `test-logs/data.log`

## Log Permissions Note

Some logs in `/var/log/` (like `boot.log` with `-rw-------` permissions) require running the agent with `sudo` to be readable.