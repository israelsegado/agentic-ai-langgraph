import re
from typing import List
from pathlib import Path
from langchain_core.tools import tool

TOOLS_DIR = Path(__file__).resolve().parent
TEST_LOG_DIR = (TOOLS_DIR / "../test-logs").resolve()

LOG_DIR = Path("/var/log").resolve()

def safe_load(filename: str) -> Path:
    """Load a log file from the system log directory."""
    file = (LOG_DIR / filename).resolve()
    if LOG_DIR not in file.parents or not file.is_file():
        raise ValueError(f"File {file} not in {LOG_DIR}.")
    else:
        return file

@tool
def read_log_chunk(filename: str, start: int = 50, n_lines: int = 200) -> List[str]:
    """Read a chunk of the log file starting from line `start` for up to `n_lines`."""
    path = safe_load(filename)
    out_file = []
    with open(path, 'r') as f:   
        for i, line in enumerate(f):
            if i < start:
                continue
            elif i >= start + n_lines:
                break
            out_file.append(f"{i}: {line.rstrip()}")
    return out_file

@tool
def search_pattern(filename: str, regex: str, max_results: int = 50) -> str:
    """Search for a regex pattern in the log file, returning total matches and examples."""
    path = safe_load(filename)
    try:
        rx = re.compile(pattern=regex)
    except re.error as e:
        print(f"Invalid regex: {e}")

    counter = 0
    hits = []
    with open(path, 'r') as f:
        for i, line in enumerate(f):
            if rx.search(line):
                counter += 1
                if len(hits) < max_results:
                    hits.append(f"{i}: {line.rstrip()}")

    hits_str = "\n".join(hits)
    return f"Total coincidences {counter} \n {hits_str}"

@tool
def count_by_level(filename:str) -> str:
    """Count INFO, WARNING and ERROR lines in the log file."""
    path = safe_load(filename)

    counts = {"FAIL": 0, "WARNING": 0, "INFO": 0}
    with open(path, 'r') as f:
        for line in f:
            low = line.lower()
            for k in counts:
                if k in low:
                    counts[k] += 1

    return str(counts)