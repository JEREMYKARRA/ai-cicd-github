import subprocess
import sys
import json

def check_coverage():
    subprocess.run(["pytest", "--cov=src", "--cov-report=json", "-q"], capture_output=True, text=True)

    try:
        with open("coverage.json", "r") as file:
            data = json.load(file)
            return data['totals']['percent_covered']
    except (FileNotFoundError, KeyError):
        return 0.0

def main():
    threshold = float(sys.argv[1]) if len(sys.argv) > 1 else 80.0
    coverage_percent = check_coverage()

    return 1 if coverage_percent < threshold else 0

if __name__=="__main__":
    sys.exit(main())