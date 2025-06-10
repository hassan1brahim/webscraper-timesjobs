# WebScraper for TimesJobs

This Python script scrapes job listings from [TimesJobs](https://www.timesjobs.com) with the keyword **Python** and saves recently posted jobs (posted "a few days ago") to a text file named `jobs.txt`.

---

## Features

- Fetches job postings using `requests` and parses HTML with `BeautifulSoup`.
- Filters jobs based on posting date to get recent listings.
- Extracts company name, required skills, publication date, and job link.
- Appends new job information to a local file `jobs.txt`.
- Runs continuously every 10 minutes to update the job list.

---

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install dependencies via pip:

```bash
pip install requests beautifulsoup4
