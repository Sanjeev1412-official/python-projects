import re
from collections import defaultdict
from statistics import mean


# -----------------------------
# log pattern
# -----------------------------

LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - '
    r'\[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\w+) (?P<endpoint>[^ ]+) HTTP/[^"]+" '
    r'(?P<status>\d{3}) (?P<size>\d+) (?P<response_time>\d+\.\d+)'
)

class LogAnalyzer:
    def __init__(self):
        self.total_requests = 0
        self.status_counts = defaultdict(int)
        self.endpoint_hits = defaultdict(int)
        self.errors = []
        self.response_times = []
        
    # -----------------------------
    # parsing function
    # -----------------------------
        
    def parse_log_line(self, line):
        match = LOG_PATTERN.match(line)
        
        if not match:
            return None
        return match.groupdict()
    
    # -----------------------------
    # analysis function
    # -----------------------------

    def analyse_log(self, filepath):
        with open(filepath,'r') as file:
            for line in file:
                line = line.strip()
                
                parsed = self.parse_log_line(line)
                if not parsed:
                    print(f"Malformed log line: {line}")
                    continue
                
                self.total_requests += 1
                
                status = int(parsed['status'])
                endpoint = parsed['endpoint']
                response_time = float(parsed['response_time'])
                
                self.status_counts[status] += 1
                self.endpoint_hits[endpoint] += 1
                self.response_times.append(response_time)
                
                if status >= 400:
                    self.errors.append(parsed)
                    
    # -----------------------------
    # generate report function
    # -----------------------------
    def generate_report(self):
        print("\n========== LOG ANALYSIS REPORT ==========\n")

        print(f"Total Requests: {self.total_requests}\n")

        print("Status Code Distribution:")
        for status, count in sorted(self.status_counts.items()):
            print(f"  {status}: {count}")
        print()

        if self.response_times:
            print("Response Time Stats (seconds):")
            print(f"  Average: {mean(self.response_times):.3f}")
            print(f"  Min: {min(self.response_times):.3f}")
            print(f"  Max: {max(self.response_times):.3f}")
            print()

        print("Top Endpoints:")
        for endpoint, count in sorted(self.endpoint_hits.items(), key=lambda x: x[1], reverse=True):
            print(f"  {endpoint}: {count}")
        print()

        print("Errors (4xx / 5xx):")
        for err in self.errors:
            print(
                f'  [{err["timestamp"]}] {err["method"]} {err["endpoint"]} '
                f'Status: {err["status"]} Time: {err["response_time"]}'
            )

        print("\n========================================\n")
    

if __name__ == "__main__":
    log_file = 'log_analyzer/logs.txt'
    log = LogAnalyzer()
    log.analyse_log(log_file)
    log.generate_report()