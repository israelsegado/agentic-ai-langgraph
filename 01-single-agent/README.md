# 01-single-agent: Collection of LangChain Agents

This directory contains two independent agents built with LangChain and Groq, each designed for specific analysis tasks.

## Agent Comparison

| Metric | Repository Documentation Agent | Log Analyzer Agent |
|--------|-------------------------------|---------------------|
| **Primary Purpose** | Traverses a repo, finds undocumented code, generates README proposals | Analyzes system logs, counts severity levels, searches patterns |
| **Key Tools** | `list_tree`, `read_file`, `find_undocumented`, `write_proposal` | `read_log_chunk`, `search_pattern`, `count_by_level` |
| **Typical Steps per Task** | 4-6 steps (prompt user → traverse → detect undocumented → generate README → save proposals) | 3-5 steps (prompt user → read/chunk → search/count → generate report) |
| **Observed Failures** | - Depth limits cause incomplete traversal of deeply nested repos<br>- Missing docstrings not detected in `__pycache__` or excluded dirs<br>- Proposal content can be too verbose for large codebases | - Permission errors on restricted log files (e.g., `boot.log` requires sudo)<br>- Regex patterns may match too broadly or miss context-specific terms<br>- Log chunk size limits affect completeness of analysis |
| **LLM Model** | `openai/gpt-oss-20b` (configurable in `src/config.py`) | Configurable in `src/config.py` |
| **Output Format** | Markdown proposals saved to `proposals/` folder | Structured `Report` JSON with summary, incidents, recommended_actions |

---

## When a single agent is not enough

In practice, a single-agent setup hits limits when a task requires both broad exploration and deep specialized analysis. The repository documentation agent excels at traversing code structures and identifying undocumented elements, but struggles with deeply nested directories and producing concise proposals. The log analyzer agent is powerful for pattern matching and severity counting, yet fails on permission-restricted logs and contextual pattern detection. Each agent works well within its domain, but neither can efficiently switch between exploration and exploitation modes without manual reconfiguration. These complementary weaknesses make the case for a multi-agent system where specialized agents collaborate: one to explore and map the domain, another to analyze and report, with coordination logic to hand off context and aggregate results.

---

## Getting Started

Each agent lives in its own subdirectory. See their individual README.md files for setup, usage, and customization details.

- [repo-documentation/](repo-documentation/README.md) — Agent that analyzes local repositories and generates documentation proposals.
- [log-analyzer/](log-analyzer/README.md) — Agent that analyzes system logs using Groq LLMs.

To run an agent:

```bash
cd 01-single-agent/repo-documentation
python agent.py
```

or

```bash
cd 01-single-agent/log-analyzer
python agent.py
```