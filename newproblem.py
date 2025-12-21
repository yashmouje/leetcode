#!/usr/bin/env python3
"""
newproblem.py — scaffold a LeetCode problem folder.

Usage:
  python newproblem.py "Two Sum"
  python newproblem.py "23. Merge k Sorted Lists"
  python newproblem.py "Valid Parentheses" --force
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


def slugify(name: str) -> str:
    s = name.strip().lower()

    # Turn common separators into spaces
    s = re.sub(r"[_/]+", " ", s)

    # Remove anything that's not alnum/space/hyphen/dot
    s = re.sub(r"[^a-z0-9\s\-.]", "", s)

    # Convert dots/spaces to single hyphens
    s = re.sub(r"[\s\.]+", "-", s)

    # Collapse multiple hyphens
    s = re.sub(r"-{2,}", "-", s).strip("-")

    return s or "untitled-problem"


def write_file(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"{path} already exists. Use --force to overwrite.")
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scaffold a LeetCode problem directory."
    )
    parser.add_argument("name", help='Problem name, e.g. "Two Sum"')
    parser.add_argument(
        "-r",
        "--root",
        default=".",
        help="Root directory to create the problem folder in (default: current dir).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files if they already exist.",
    )
    args = parser.parse_args()

    original = args.name.strip()
    slug = slugify(original)

    root = Path(args.root).resolve()
    problem_dir = root / slug
    problem_dir.mkdir(parents=True, exist_ok=True)

    md_path = problem_dir / f"{slug}.md"
    py_path = problem_dir / "sol.py"

    today = date.today().isoformat()

    md_template = f"""# {original}

- Date: {today}
- Link: [Problem]()
- Difficulty: Easy/Medium/Hard
- Tags: <!-- e.g. Hashmap, Two Pointers -->
---
## Description


## Examples


## Constraints

---

## Solution Complexity
- Time: O(?)
- Space: O(?)
"""

    py_template = f'''"""
{original}
Created: {today}

Python {sys.version.split()[0] or "3.12"}
"""

class Solution:
    def solve(self, *args, **kwargs):
        """
        Change this to the required LeetCode signature.
        """
        raise NotImplementedError

'''

    try:
        write_file(md_path, md_template, args.force)
        write_file(py_path, py_template, args.force)
    except FileExistsError as e:
        print(f"[!] {e}")
        print(f"    Directory: {problem_dir}")
        return

    print(f"[+] Created: {problem_dir}")
    print(f"    - {md_path.name}")
    print(f"    - {py_path.name}")


if __name__ == "__main__":
    main()
