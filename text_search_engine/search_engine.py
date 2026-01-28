import argparse
import re
from collections import deque

def search_file(filepath, keyword, ignore_case=False, use_regex=False, context=0):

    if ignore_case and not use_regex:
        keyword = keyword.lower()
    
    buffer = deque(maxlen=context)
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for line_number, line in enumerate(file, start=1):
            original_line = line.rstrip('\n')
            match_found = False
            
            if use_regex:
                flag = re.IGNORECASE if ignore_case else 0
                match = re.search(keyword, original_line, flag)
                match_found = match is not None
            else:
                search_line = original_line.lower() if ignore_case else original_line
                if keyword in search_line:
                    match_found = True
                    
            if match_found:
                print("\n==============================")
                print(f"Match found at line {line_number}")

                # print context before
                if context > 0:
                    print("\n--- Context Before ---")
                    for prev_line in buffer:
                        print(prev_line)

                # print matched line
                print("\n--- Matched Line ---")
                print(original_line)

                print("==============================")

            # update context buffer
            buffer.append(original_line)
            
def main():
    parser = argparse.ArgumentParser(description="Text Search Engine (Mini Grep)")

    parser.add_argument("file", help="File path to search")
    parser.add_argument("keyword", help="Keyword or regex pattern")

    parser.add_argument("--ignore-case", action="store_true",
                        help="Case-insensitive search")

    parser.add_argument("--regex", action="store_true",
                        help="Enable regex search")

    parser.add_argument("--context", type=int, default=0,
                        help="Number of context lines before match")

    args = parser.parse_args()
    
    search_file(args.file, args.keyword, args.ignore_case, args.regex, args.context)
    
if __name__ == "__main__":
    main()
        