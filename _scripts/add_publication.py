#!/usr/bin/env python3
"""
Add a new publication entry to your website.
Run: python3 add_publication.py
"""

import shutil
from datetime import date
from pathlib import Path

# ── USER CONFIG ───────────────────────────────────────────────────────────────
WEBSITE_ROOT = Path("/Users/caro/Developer/lacinoire.github.io")
WORKS_DIR    = WEBSITE_ROOT / "_works"
IMAGES_DIR   = WEBSITE_ROOT / "assets" / "img" / "works"
PDFS_DIR     = WEBSITE_ROOT / "publications"
# ─────────────────────────────────────────────────────────────────────────────


def ask(prompt, required=True):
    """
    Collect input, supporting multi-line pastes.
    A blank line (just Enter on an empty line) signals end-of-input,
    but only after at least one non-empty line has been entered.
    """
    print(f"  {prompt}:")
    lines = []
    while True:
        try:
            line = input("    ")
        except EOFError:
            break
        if line.strip() == "":
            if lines:
                break           # blank line = done
            if not required:
                return ""
            # Required but nothing yet — keep waiting
        else:
            lines.append(line)
    return "\n".join(lines).strip()


def ask_authors():
    """Ask for a comma-separated author list and join with ·"""
    print("  Authors (comma-separated, e.g. Alice Smith, Bob Jones):")
    while True:
        raw = input("    ").strip()
        if raw:
            authors = [a.strip() for a in raw.split(",") if a.strip()]
            return " · ".join(authors)
        print("  (required, please enter at least one author)")


def ask_file(prompt, extension):
    while True:
        print(f"  {prompt}:")
        raw = input("    ").strip().strip("'\"")
        path = Path(raw).expanduser()
        if not path.exists():
            print(f"  File not found: {path}")
        elif path.suffix.lower() != f".{extension}":
            print(f"  Expected a .{extension} file, got: {path.suffix}")
        else:
            return path


def main():
    print("\n── Add publication ──────────────────────────────────────────")
    print("  (Paste freely into any field. Press Enter on a blank line when done.)\n")

    slug     = ask("Slug (filename base, e.g. lueders-humanaise26)")
    title    = ask("Title").replace("\n", " ")
    authors  = ask_authors()
    venue    = ask("Venue / conference / journal (e.g. HumanAISE'26)")
    abstract = ask("Abstract")
    doi      = ask("DOI or URL (leave blank to skip)", required=False)

    print()
    pdf_src = ask_file("Path to PDF  (drag file here or type path)", "pdf")
    png_src = ask_file("Path to cover image  (drag file here or type path)", "png")

    # ── Build markdown ────────────────────────────────────────────────────────
    today   = date.today().strftime("%Y-%m-%d")
    pdf_url = f"https://carolin-brandt.de/publications/{slug}.pdf"

    if doi:
        doi_block = f"  - name: DOI\n    url: {doi}"
    else:
        doi_block = "  # - name: DOI\n  #   url: https://doi.org/..."

    md = f"""---
title: "{title}"
category: {venue}
category_slug: peer-reviewed
layout: publication
slug: {slug}
type: content
image: assets/img/works/{slug}.png
date: {today}
links:
  - name: Full Publication
    url: {pdf_url}
  # - name: Presentation Slides
  #   url: https://carolin-brandt.de/publications/{slug}-slides.pdf
  # - name: Replication Package
  #   url: https://zenodo.org/doi/...
{doi_block}
---

{authors}

### Abstract
{abstract}
"""

    # ── Write files ───────────────────────────────────────────────────────────
    WORKS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    PDFS_DIR.mkdir(parents=True, exist_ok=True)

    md_dest  = WORKS_DIR  / f"{slug}.md"
    pdf_dest = PDFS_DIR   / f"{slug}.pdf"
    png_dest = IMAGES_DIR / f"{slug}.png"

    md_dest.write_text(md, encoding="utf-8")
    shutil.copy2(pdf_src, pdf_dest)
    shutil.copy2(png_src, png_dest)

    print(f"""
── Done ─────────────────────────────────────────────────────
  {md_dest}
  {pdf_dest}
  {png_dest}
─────────────────────────────────────────────────────────────
""")


if __name__ == "__main__":
    main()
