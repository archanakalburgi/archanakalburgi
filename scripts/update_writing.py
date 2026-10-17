#!/usr/bin/env python3
"""Refresh the Writing section of README.md from the blog's Atom feed.

Rewrites whatever sits between the POSTS:START / POSTS:END markers and leaves
the rest of the README alone. Standard library only, so the workflow needs no
pip install step.
"""

import html
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

FEED_URL = os.environ.get("FEED_URL", "https://archanakalburgi.github.io/feed.xml")
LIMIT = int(os.environ.get("POST_LIMIT", "3"))
SUMMARY_CHARS = 190
README = Path(__file__).resolve().parent.parent / "README.md"
ATOM = {"a": "http://www.w3.org/2005/Atom"}
START, END = "<!-- POSTS:START -->", "<!-- POSTS:END -->"


def clean(text):
    """Strip tags and collapse whitespace in a feed summary."""
    text = re.sub(r"<[^>]+>", "", html.unescape(text or ""))
    return re.sub(r"\s+", " ", text).strip()


def shorten(text, limit=SUMMARY_CHARS):
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:—-") + "…"


def fetch_posts(url, limit):
    with urllib.request.urlopen(url, timeout=30) as response:
        root = ET.fromstring(response.read())

    posts, seen = [], set()
    for entry in root.findall("a:entry", ATOM):
        title = clean(entry.findtext("a:title", "", ATOM))
        link = entry.find("a:link[@rel='alternate']", ATOM)
        href = link.get("href") if link is not None else None
        # A draft republished under a later date keeps its slug, so key on
        # that rather than the title, which often gets reworded in between.
        slug = href.rstrip("/").rsplit("/", 1)[-1].removesuffix(".html")
        if not title or not href or slug in seen:
            continue
        seen.add(slug)

        summary = shorten(clean(entry.findtext("a:summary", "", ATOM)))
        published = entry.findtext("a:published", "", ATOM)
        posts.append({"title": title, "url": href, "summary": summary, "date": published})
        if len(posts) == limit:
            break
    return posts


def render(posts):
    lines = []
    for post in posts:
        line = f"- **[{post['title']}]({post['url']})**"
        if post["summary"]:
            line += f" — {post['summary']}"
        try:
            stamp = datetime.fromisoformat(post["date"]).strftime("%-d %b %Y")
            line += f" <br><sub>{stamp}</sub>"
        except ValueError:
            pass
        lines.append(line)
    return "\n".join(lines)


def main():
    readme = README.read_text()
    if START not in readme or END not in readme:
        sys.exit(f"markers {START} / {END} not found in {README.name}")

    posts = fetch_posts(FEED_URL, LIMIT)
    if not posts:
        sys.exit("feed returned no usable entries; leaving README untouched")

    block = f"{START}\n{render(posts)}\n{END}"
    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END), lambda _: block, readme, flags=re.S
    )

    if updated == readme:
        print(f"no change ({len(posts)} posts already current)")
        return
    README.write_text(updated)
    print(f"updated with {len(posts)} posts:")
    for post in posts:
        print(f"  - {post['title']}")


if __name__ == "__main__":
    main()
