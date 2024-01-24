#!/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
    """Retrieves and displays the TODO list progress of a given employee using a REST API."""

    # Validate employee ID
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError("Employee ID should be a positive integer.")

    # Fetch TODO data from the REST API
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
        response.raise_for_status()  # Raise an exception for non-200 status codes
        todos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    # Process TODO data
    employee_name = todos[0].get("userId", "Unknown")  # Get name from the first todo (if available)
    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)
    number_of_done_tasks = len(completed_tasks)

    # Print progress summary
    print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_tasks}):")

    # Print completed task titles
    for task in completed_tasks:
        print("\t", task["title"])

# Example usage
if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_todo_progress(employee_id)
