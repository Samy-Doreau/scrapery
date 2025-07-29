from pathlib import Path

import requests
from bs4 import BeautifulSoup

from config import TARGET_URL, CSS_SELECTOR


def scrape(url: str, selector: str):
    """Fetch *url* and return a list of text extracted by *selector*."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    return [elem.get_text(strip=True) for elem in soup.select(selector)]


def save_to_file(records, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(records), encoding="utf-8")


if __name__ == "__main__":
    # Run as standalone script via `make run-scraper`
    items = scrape(TARGET_URL, CSS_SELECTOR)
    out_file = Path("data") / "scraped.txt"
    save_to_file(items, out_file)
    print(f"Saved {len(items)} items to {out_file.relative_to(Path.cwd())}") 