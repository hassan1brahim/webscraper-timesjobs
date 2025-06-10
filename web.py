from bs4 import BeautifulSoup
import requests, time

# Removes extra spaces from the skills string
def removeSpace(words):
    words = ' '.join(words.split())
    finalword = ''
    in_word = False 
    for char in words:
        if char != ' ':
            finalword += char
            in_word = True
        else:
            if in_word:
                finalword += ' '
                in_word = False
    return finalword.strip()

# Scrapes Python jobs from TimesJobs
def get_jobs():
    try:
        # Send GET request to TimesJobs for 'python' keyword
        html_txt = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
        html_txt.raise_for_status() # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_txt.text, 'html.parser')

    # Find all job boxes
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    count = 0

    for job in jobs:
        # Extract key elements
        company_name = job.find('h3', class_='joblist-comp-name')  # Company name
        skills = job.find('div', class_='srp-skills')              # Required skills
        link = job.find('a', class_='posoverlay_srp')              # Job link
        published_date = job.find('span', class_='sim-posted')     # Posting date

        # Check if posting is recent and all required fields exist
        if published_date and 'few' in published_date.text:
            if company_name and skills and link:
                with open('jobs.txt', 'a') as f:
                    f.write(f"Company Name: {company_name.text.strip()}\n")
                    f.write(f"Skills Required: {removeSpace(skills.text)}\n")
                    f.write(f"Published Date: {published_date.text.strip()}\n")
                    f.write(f"Job Link: {link['href']}\n")
                    f.write('\n-------------------------------\n\n')
                count += 1  # Count saved jobs

    print(f"Saved {count} new jobs.")

# Run scraping every 10 minutes
while True:
    get_jobs()
    time_wait = 10
    print(f"Waiting for {time_wait} minutes...\n")
    time.sleep(time_wait * 60)