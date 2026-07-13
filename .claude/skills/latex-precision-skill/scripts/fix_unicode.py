#!/usr/bin/env python3
"""
Fix missing Unicode chars in MinerU Chinese LaTeX docs.
Inserts newunicodechar mappings after amsmath,amssymb line.
Usage: python3 fix_unicode.py <file.tex>
"""
import sys, shutil
from pathlib import Path

BS = chr(92)

PATCH = (
    "\n%%% FIX: Unicode chars missing in Latin Modern Roman %%%\n"
    + BS + "usepackage{newunicodechar}\n"
    + BS + "newunicodechar{" + "≤" + "}{" + BS + "ensuremath{" + BS + "leq}}\n"
    + BS + "newunicodechar{" + "≥" + "}{" + BS + "ensuremath{" + BS + "geq}}\n"
    + BS + "newunicodechar{" + "λ" + "}{" + BS + "ensuremath{" + BS + "lambda}}\n"
    "% U+F06C Wingdings bullet -> textbullet\n"
    + BS + "newunicodechar{" + "" + "}{" + BS + "textbullet}\n"
    "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
)

SEARCH = BS + "usepackage{amsmath,amssymb}"


def fix_tex(path: Path):
    content = path.read_text("utf-8")
    if SEARCH not in content:
        print("ERROR: cannot find " + repr(SEARCH))
        return False
    if PATCH.strip() in content:
        print("Already patched, skipping")
        return True
    shutil.copy2(path, path.with_suffix(path.suffix + ".bak"))
    content = content.replace(SEARCH, SEARCH + PATCH)
    path.write_text(content, "utf-8")
    print("OK - patched. Backup saved as .bak")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fix_unicode.py <file.tex>")
        sys.exit(1)
    fp = Path(sys.argv[1])
    if not fp.exists():
        print("File not found:", fp)
        sys.exit(1)
    fix_tex(fp)
