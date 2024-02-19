#!/usr/bin/python3

import requests

def top_ten(subreddit):
  """
  Prints the titles of the first 10 hot posts from a given subreddit.

  Args:
    subreddit: The name of the subreddit to query.
  """

  url = f"https://www.reddit.com/r/{subreddit}/hot.json"
  headers = {"User-Agent": "YourAppName/0.1 by YourUsername"}  # Replace with your app details

  try:
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()  # Raise an exception for error responses

    data = response.json()
    # Check if valid subreddit by looking for "data" key
    if not data.get("data"):
      print(None)
      return

    posts = data["data"]["children"]
    for post in posts[:10]:
      print(post["data"]["title"])

  except requests.exceptions.RequestException as e:
    print(f"Error fetching subreddit posts: {e}")

# Example usage
top_ten("programming")
top_ten("nonexistent_subreddit")  # Should print None
