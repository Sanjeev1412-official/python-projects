
# Log Analyzer (Python)

A small, production-style Python utility that parses web server access logs and prints a fast, readable health report: request volume, status code distribution, response-time stats, most-hit endpoints, and error events.


---

## Why this matters

When you’re on-call or troubleshooting incidents, you often need answers quickly:

- Are errors spiking (4xx/5xx)?
- Which endpoint is causing trouble?
- Are response times degrading?

This script turns raw logs into actionable metrics in seconds.

---

## What it does

- Parses each log line using a strict regex pattern (IP, timestamp, method, endpoint, HTTP version, status, payload size, response time)
- Tracks totals and distributions
- Computes response-time stats (average/min/max)
- Ranks endpoints by hit count
- Lists all error requests (status >= 400)
- Skips malformed lines safely (prints a warning)

---

## Skills demonstrated

- Python fundamentals: classes, data structures, file IO
- Robust parsing: regular expressions with named capture groups
- Analytics: aggregation with `defaultdict`, statistics via `statistics.mean`
- Defensive coding: malformed-line handling without crashing
- Clean reporting: readable, structured console output

---

## Tech stack

- Python 3.12+ (works on any modern Python 3)
- Standard library only (no external dependencies)

---

## Project structure

```text
log_analyzer/
	analyzer.py   # parser + aggregator + report generator
	logs.txt      # sample input log file
	README.md
```

---

## Quick start


```bash
python log_analyzer/analyzer.py
```

Expected output :

```text
========== LOG ANALYSIS REPORT ==========

Total Requests: 4

Status Code Distribution:
	200: 2
	404: 1
	500: 1

Response Time Stats (seconds):
	Average: 0.480
	Min: 0.111
	Max: 1.456

Top Endpoints:
	/api/login: 2
	/api/register: 1
	/api/data: 1

Errors (4xx / 5xx):
	[10/Jan/2026:10:05:22 +0530] POST /api/register Status: 500 Time: 1.456
	[10/Jan/2026:10:05:23 +0530] GET /api/data Status: 404 Time: 0.231

========================================
```

---

## Notes / current assumptions

- The script currently reads from a fixed path: `log_analyzer/logs.txt`.
- To analyze a different file, update the `log_file` variable at the bottom of `analyzer.py`.

---

## Reasonable next improvements

- Add a CLI interface (e.g., `python analyzer.py --file path/to/logs.txt`)
- Add unit tests for the parser and aggregations
- Export report to JSON/CSV for dashboards
- Add percentiles (p50/p95/p99) for response times

---

## Learning outcomes

- Designing and validating a log schema with Python `re` (named capture groups)
- Building a small analytics pipeline: parse → normalize → aggregate → report
- Using `defaultdict` for clean counting and ranking (sorting by frequency)
- Computing summary statistics with the standard library (`statistics.mean`, min/max)
- Writing defensive parsers that handle malformed data without breaking


