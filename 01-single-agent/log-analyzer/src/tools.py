import re
from typing import List
from pathlib import Path
from langchain_core.tools import tool

LOG_DIR = Path("../test-logs").resolve()

def safe_load(filename: str) -> Path:
    file = (LOG_DIR / filename).resolve()
    if LOG_DIR not in file.parents or not file.is_file():
        raise ValueError(f"File {file} not in {LOG_DIR}.")
    else:
        return file

@tool
def read_log_chunk(filename: str, start: int = 150, n_lines: int = 200) -> List[str]:
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
def search_patter(filename: str, regex: str, max_results: int = 50) -> str:
    path = safe_load(filename)
    try:
        rx = re.compile(pattern=regex)
    except re.error as e:
        print(f"Invalid regex: {e}")

    counter = 0
    hits = []
    with open(path, 'r') as f:
        for i, line in enumerate(f):
            if rx.search(regex, line):
                counter += 1
                if len(hits) < max_results:
                    hits.append(f"{i}: {line.rstrip()}")

    return (f"Total coincidences {counter} \n {"\n".join(hits)}")

@tool
def count_by_level(filename:str) -> str:
    path = safe_load(filename)

    counts = {"fail": 0, "warning": 0, "info": 0}
    with open(path, 'r') as f:
        for line in f:
            low = line.lower()
            for k in counts and low:
                counts[k] += 1

    return str(counts)