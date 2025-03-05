import requests
import sqlite3
import csv
from bs4 import BeautifulSoup
import pandas as pd

DB_FILE = "jobs.db"

def create_database():
    """Creates the jobs table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(job_title, company, location)
        )
    """)
    conn.commit()
    conn.close()

def scrape_jobs():
    """Scrapes job listings from the website."""
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    job_listings = []
    jobs = soup.find_all("div", class_="card-content")
    
    for job in jobs:
        job_title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="description").text.strip()
        application_link = job.find("a")["href"]

        job_listings.append((job_title, company, location, description, application_link))
    
    return job_listings

def insert_jobs(job_listings):
    """Inserts new jobs into the database and updates existing ones if needed."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for job in job_listings:
        job_title, company, location, description, application_link = job

        # Check if the job exists
        cursor.execute("""
            SELECT description, application_link FROM jobs 
            WHERE job_title = ? AND company = ? AND location = ?
        """, (job_title, company, location))
        existing_job = cursor.fetchone()

        if existing_job:
            existing_description, existing_link = existing_job
            if existing_description != description or existing_link != application_link:
                # Update the existing job listing
                cursor.execute("""
                    UPDATE jobs 
                    SET description = ?, application_link = ? 
                    WHERE job_title = ? AND company = ? AND location = ?
                """, (description, application_link, job_title, company, location))
        else:
            # Insert new job listing
            cursor.execute("""
                INSERT INTO jobs (job_title, company, location, description, application_link)
                VALUES (?, ?, ?, ?, ?)
            """, job)

    conn.commit()
    conn.close()

def filter_jobs(location=None, company=None):
    """Filters job listings by location or company."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    query = "SELECT job_title, company, location, description, application_link FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    
    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")
    
    cursor.execute(query, params)
    jobs = cursor.fetchall()
    conn.close()
    return jobs

def export_jobs_to_csv(filename, location=None, company=None):
    """Exports filtered jobs to a CSV file."""
    jobs = filter_jobs(location, company)
    
    if jobs:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Job Title", "Company", "Location", "Description", "Application Link"])
            writer.writerows(jobs)
        print(f"✅ Jobs exported to {filename}")
    else:
        print("⚠️ No jobs found for the given filters.")

# Run the script
if __name__ == "__main__":
    create_database()
    jobs = scrape_jobs()
    insert_jobs(jobs)

    # Example: Filter by location or company
    filtered_jobs = filter_jobs(location="New York")
    print("\n📌 Filtered Jobs in New York:")
    for job in filtered_jobs:
        print(job)

    # Example: Export filtered jobs to CSV
    export_jobs_to_csv("filtered_jobs.csv", location="New York")
