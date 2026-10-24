#!/usr/bin/python3
"""Fetch and export JSONPlaceholder posts using requests."""

import csv
import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Print the HTTP status code and all post titles."""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    """Save all post IDs, titles, and bodies in posts.csv."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in response.json()
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
