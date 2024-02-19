#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[]):
  """
  Recursively retrieves titles of all hot articles for a subreddit.

  Args:
    subreddit: The name of the subreddit to query.
    hot_list (list, optional): Accumulated list of hot article titles. Defaults to [].

  Returns:
    list: List of all hot article titles, or None if an error occurs or no results found.
  """

  url = f"https://www.reddit.com/r/{subreddit}/hot.json"
  headers = {"User-Agent": "YourAppName/0.1 by YourUsername"}  # Replace with your app details

  try:
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()  # Raise an exception for error responses

    data = response.json()
    # Check if valid subreddit by looking for "data" key
    if not data.get("data"):
      return None

    posts = data["data"]["children"]

    # Extract titles and add to list
    hot_list.extend([post["data"]["title"] for post in posts])

    # Check if there are more pages using "after" key
    after = data["data"]["after"]

    # Base case: No more pages, return complete list
    if not after:
      return hot_list

    # Recursive call for next page
    return recurse(subreddit, hot_list)

  except requests.exceptions.RequestException as e:
    print(f"Error fetching subreddit posts: {e}")
    return None

# Example usage
all_titles = recurse("askreddit")
if all_titles:
  print(f"Titles of all hot articles in r/askreddit:")
  for title in all_titles:
    print(title)
else:
  print("No hot articles found for the subreddit.")
