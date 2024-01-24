#!/usr/bin/python3
import requests
import csv

def get_employee_todo_progress_and_export_csv(employee_id):
    """Retrieves and displays employee TODO list progress, and exports all tasks to a CSV file."""

    # ... (Fetch and process TODO data as in the previous script)

    # Export data to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            csv_writer.writerow([
                todo["userId"],
                todo.get("userId", "Unknown"),  # Use name if available, else "Unknown"
                "Completed" if todo["completed"] else "Not Completed",
                todo["title"]
            ])

    print(f"Employee data exported to CSV file: {csv_filename}")

# Example usage (same as before)
if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_todo_progress_and_export_csv(employee_id)
