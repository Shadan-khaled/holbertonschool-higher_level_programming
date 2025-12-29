#!/usr/bin/python3
import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts from API and print their titles"""
    response = requests.get(API_URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts from API and save them to a CSV file"""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()

        structured_posts = []
        for post in posts:
            structured_posts.append(
                {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body"),
                }
            )

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)
