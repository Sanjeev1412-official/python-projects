
# File Organizer (Python CLI)

A practical command-line utility that organizes files in a target folder into categorized subfolders (Images, Videos, Documents, etc.). It supports a safe preview mode and an optional date-based hierarchy.

## Why this project

This is a real-world automation script that demonstrates:

- Building a clean CLI with `argparse`
- Filesystem traversal and file operations
- Defensive behavior (skip folders, skip name collisions)
- Safe operational workflows (`--dry-run` before mutating anything)

## Features

- Organizes files into category folders based on file extension:
	- `Images`, `Videos`, `Documents`, `Audio`, `Archives`, `Code`, `Others`
- Optional date mode: group files into `Category/YYYY-MM/` based on **modified time** (`--date`)
- Dry-run preview: prints the moves without changing anything (`--dry-run`)
- Skips:
	- subdirectories (only moves files)
	- files that would overwrite an existing destination path




## Usage

```bash
python organizer.py <folder> [--date] [--dry-run]
```



## Output structure

Default organization:

```text
<target folder>/
	Images/
	Videos/
	Documents/
	Audio/
	Archives/
	Code/
	Others/
```

With `--date` enabled:

```text
<target folder>/
	Documents/
		2026-01/
		2026-02/
	Images/
		2026-01/
	...
```

## How it works

- File type is determined by extension (`FILE_CATEGORIES`). Unknown extensions go to `Others`.
- Date grouping uses the file’s **last modified time** (`os.path.getmtime`) formatted as `YYYY-MM`.
- Moves are performed with `shutil.move`, which keeps the operation simple and cross-platform.

## Learning outcomes

- Using `argparse` to design safe, user-friendly CLI tools
- Working with the filesystem: listing directories, identifying file types, creating folders
- Writing automation scripts with “preview before apply” (`--dry-run`) workflows
- Handling edge cases: skip directories, avoid overwrites, normalize extensions


## Notes and limitations

- The tool currently categorizes by extension only (not file content).
- Name collisions are skipped (it does not auto-rename duplicates yet).
- Categories are defined in code; extending is as simple as adding extensions to `FILE_CATEGORIES`.

## Ideas for improvement

- Add `--recursive` to organize nested folders
- Add `--copy` mode (copy instead of move)
- Add `--rename-duplicates` (e.g., `file (1).pdf`) instead of skipping
- Add configurable categories via JSON/YAML

