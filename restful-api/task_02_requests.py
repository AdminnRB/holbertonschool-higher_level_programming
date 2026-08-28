#!/usr/bin/env python3
"""Consume and process data from an API using the requests library."""
import csv

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles.

    Prints the response status code, then, if the request succeeded,
    prints the title of every post returned by the API.
    """
    response = requests.get(API_URL)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save them to posts.csv.

    Writes a CSV file named posts.csv with columns id, title, body,
    one row per post. Does nothing if the request fails.
    """
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        fieldnames = ["id", "title", "body"]
        rows = [
            {key: post[key] for key in fieldnames}
            for post in posts
        ]

        with open("posts.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
