from collections import defaultdict
import re
import sys


def parse_log_line(line: str) -> dict:
    """
    Parse a log line and extract its components.
    Args:
        line (str): A log line string in the format "YYYY-MM-DD HH:MM:SS LEVEL message".
    Returns:
        dict: A dictionary containing the parsed log components with keys:
            - 'date': The date part of the log entry
            - 'time': The time part of the log entry
            - 'level': The log level (e.g., DEBUG, INFO, WARNING, ERROR)
            - 'message': The log message content
    Raises:
        ValueError: If the log line does not contain exactly 4 space-separated elements.
    """

    elements = line.split(' ', 3)

    if len(elements) == 4:
        return {
            'date': elements[0],
            'time': elements[1],
            'level': elements[2],
            'message': elements[3]
        }
    else:
        raise ValueError(f"Invalid log line format. \n Log line: {line}")

def load_logs(file_path: str) -> list:
    """
    Load log entries from a file.
    Args:
        file_path (str): The path to the log file to read.
    Returns:
        list: A list of log entries, with each entry as a string.
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If an error occurs while reading the file.
    """

    logs = []

    with open(file_path, 'r', encoding='utf-8') as file:  
        for log_entry in file:
            logs.append(log_entry.strip())
        
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filter logs by a specific log level.
    Args:
        logs (list): A list of log dictionaries
        level (str): The log level to filter by (case-insensitive).
    Returns:
        list: A filtered list of log dictionaries matching the specified level.
    """

    return list(filter(lambda log: log['level'].upper() == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    """
    Count the number of logs by their severity level.
    Args:
        logs (list): A list of log dictionaries, each containing a 'level' key
                     that represents the severity level of the log entry.
    Returns:
        dict: A dictionary where keys are log levels and values are the count
              of logs for each level.
    """

    counts = defaultdict(int)
    for log in logs:
        level = log['level']
        counts[level] += 1
    return counts

def display_log_counts(counts: dict):
    """
    Display log level counts in a formatted table.
    Args:
        counts (dict): A dictionary where keys are log level names (str) 
                      and values are the count of logs (int) for each level.
    Returns:
        None: Prints the filtered logs to standard output.
    """

    print("Log Level   | Count")
    print("------------|------")
    for level, count in counts.items():
        print(f"{level:<11} | {count}")

def display_logs_by_level(logs: list, level: str):
    """
    Display log messages filtered by a specific log level.
    Args:
        logs (list): A list of log dictionaries.
        level (str): The log level to filter by (e.g., 'debug', 'info', 'warning', 'error').
    Returns:
        None: Prints the filtered logs to standard output.
    """

    print(f"Details for logs with level '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python task3.py <log_file> <log_level>")
        return
    
    log_file = sys.argv[1]
    
    # Load logs from the specified file
    try:
        logs = load_logs(log_file)
    except FileNotFoundError:
        print(f"Log file {log_file} not found.")
        return
    except Exception as e:
        print(f"Error loading log file {log_file}: {e}")
        return
    
    # Parse log lines and handle potential parsing errors
    try:
        logs_parsed = [parse_log_line(log) for log in logs]
    except ValueError as e:
        print(f"Error parsing log lines: {e}")
        return
    
    logs_count = count_logs_by_level(logs_parsed)
    
    display_log_counts(logs_count)

    if (len(sys.argv) == 3):
        logs_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs_parsed, logs_level)
        display_logs_by_level(filtered_logs, logs_level)

if __name__ == "__main__":
    main()