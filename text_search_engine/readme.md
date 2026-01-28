
# Text Search Engine (Mini Grep) — Python CLI

A lightweight command-line text search utility (a small “grep”-style tool) that scans a file line-by-line and prints matches with optional case-insensitive search, regex patterns, and configurable context lines.

## Why this project

This project is designed to be easy to review and demonstrates practical scripting skills you use in real work: parsing CLI args, efficient streaming file processing, and robust string/regex matching.

## Features

- Search a file for a **keyword** (substring match)
- Optional **case-insensitive** matching (`--ignore-case`)
- Optional **regex** matching (`--regex`)
- Print **N lines of context before** each match (`--context N`)
- Streams the file line-by-line (works on large files without loading everything into memory)

## Usage

```bash
python search_engine.py <file> <keyword> [--ignore-case] [--regex] [--context N]
```

## Sample output

```text
==============================
Match found at line 87

--- Context Before ---
One night--it was on the twentieth of March, 1888--I was returning from a journey...
...

--- Matched Line ---
To Sherlock Holmes she is always the woman.
==============================
```

## How it works (design notes)

- Uses `argparse` for a clean, self-documenting CLI.
- Reads the file using UTF-8 with `errors="ignore"` to avoid crashing on unexpected characters.
- Uses a fixed-size `collections.deque` as a rolling buffer to print context lines efficiently.
- Regex searches use `re.search(...)` and optionally enable `re.IGNORECASE`.

## Learning outcomes

- Building a reliable CLI with `argparse` (positional args + optional flags)
- Implementing streaming text processing (line-by-line scan for large files)
- Using regex safely and correctly (`re.search`, flags like `re.IGNORECASE`)
- Designing readable console output for debugging and analysis workflows



