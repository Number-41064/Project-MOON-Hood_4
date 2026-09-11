# Project MOON - Hood_4 🔍

A Python-based Subdomain Enumerator CLI tool for passive & active network reconnaissance.

## Features
- **DNS Resolution Brute-Force**: Checks subdomain availability using socket-based DNS lookups.
- **Custom Wordlist Support**: Easily load custom subdomain dictionaries.
- **Clean CLI Output**: Displays valid subdomains along with their resolved IP addresses.

## Requirements
- Python 3.x (No external dependencies required, uses standard `socket` and `sys` modules).

## Usage
Run with default target and wordlist:
```bash
python subdomain_enum.py github.com