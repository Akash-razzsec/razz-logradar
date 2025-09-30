#!/usr/bin/env python3
"""
RAZZ-LogRadar — Safe log scanning tool with branded FIGlet banner + colors.
Scans a file or folder for user-provided keywords and prints a summary.
"""

import os
import sys
from pyfiglet import Figlet
from colorama import init, Fore, Style

init(autoreset=True)  # ensure colors reset automatically

def print_banner(name="RAZZ-LogRadar", color=Fore.RED):
    f = Figlet(font='slant')            # choose a FIGlet font
    banner = f.renderText(name)
    # Style.BRIGHT makes it bold-ish in many terminals
    print(color + Style.BRIGHT + banner + Style.RESET_ALL)

def analyze_file(file_path, keywords, results):
    try:
        with open(file_path, 'r', errors='ignore') as fh:
            for lineno, line in enumerate(fh, start=1):
                lower = line.lower()
                for kw in keywords:
                    if kw in lower:
                        # store a structured result: file, line number, matched keyword, line text
                        results.append((os.path.basename(file_path), lineno, kw, line.rstrip()))
                        break
    except Exception as e:
        print(Fore.YELLOW + f"Warning: could not read {file_path}: {e}")

def analyze_path(path, keywords):
    results = []
    if os.path.isfile(path):
        analyze_file(path, keywords, results)
        out_dir = os.path.dirname(path) or "."
    elif os.path.isdir(path):
        for name in os.listdir(path):
            if name.endswith(".log") or name.endswith(".txt"):
                analyze_file(os.path.join(path, name), keywords, results)
        out_dir = path
    else:
        print(Fore.RED + "Error: invalid path. Enter a file or folder path.")
        return

    # write results
    if results:
        out_file = os.path.join(out_dir, "suspicious_log.txt")
        with open(out_file, 'w') as out:
            for fname, lineno, kw, text in results:
                out_line = f"{fname}:{lineno}: [{kw}] {text}"
                out.write(out_line + "\n")

        print(Fore.CYAN + Style.BRIGHT + f"\n✅ Found {len(results)} matches. Results written to: {out_file}\n")
        # print a short preview
        for i, (fname, lineno, kw, text) in enumerate(results[:20], start=1):
            print(Fore.WHITE + f"{i}. {fname}:{lineno} [{kw}] {text}")
        if len(results) > 20:
            print(Fore.WHITE + f"...and {len(results)-20} more matches.")
    else:
        print(Fore.GREEN + "No matches found for the given keywords.")

def main():
    print_banner()   # prints RAZZ-LogRadar in color
    path = input("Enter file or folder path: ").strip()
    if not path:
        print(Fore.RED + "Path is required. Exiting.")
        return

    kws = input("Enter keywords (comma separated, e.g. failed,error,denied): ").strip()
    if not kws:
        print(Fore.RED + "At least one keyword required. Exiting.")
        return

    keywords = [kw.strip().lower() for kw in kws.split(",") if kw.strip()]
    print(Fore.MAGENTA + f"\nScanning {path} for keywords: {', '.join(keywords)}\n")

    analyze_path(path, keywords)

if __name__ == "__main__":
    main()
