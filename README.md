# GitHub User Activity CLI

A simple command-line application that fetches and displays the recent public activity of a GitHub user using the GitHub API.

This project was built as part of the roadmap.sh GitHub User Activity project to practice working with APIs, JSON data, command-line arguments, and error handling in Python.

## Project URL

\## Project URL



https://roadmap.sh/projects/github-user-activity



\[GitHub User Activity Project](https://roadmap.sh/projects/github-user-activity)



## Features

* Accepts a GitHub username as a command-line argument
* Fetches recent GitHub activity using the GitHub Events API
* Displays repository activity in the terminal
* Supports multiple GitHub event types
* Handles invalid GitHub usernames
* Handles GitHub API connection errors
* Handles users with no recent activity
* Uses only Python built-in libraries

## Technologies Used

* Python
* GitHub REST API
* JSON
* Python urllib
* Command-line interface

## Project Structure

github-user-activity/
github\_activity.py
README.md

## Requirements

* Python 3.x
* Internet connection
* A GitHub username

No external Python libraries are required.

## How to Run

Open Command Prompt and navigate to the project folder:

cd C:\\github-user-activity

Run the program:

python github\_activity.py yerramsettisairamanakoushik85-arch

## Example Output

## GitHub Activity

* Pushed commits to yerramsettisairamanakoushik85-arch/shadowfox
* Pushed commits to yerramsettisairamanakoushik85-arch/shadowfox
* Pushed commits to yerramsettisairamanakoushik85-arch/shadowfox
* Pushed commits to yerramsettisairamanakoushik85-arch/shadowfox
* Public in yerramsettisairamanakoushik85-arch/shadowfox

## Supported Activity Types

* Push events
* Issue events
* Pull request events
* Star events
* Create events
* Fork events
* Delete events
* Release events

## Error Handling

### Invalid GitHub Username

Error: GitHub user not found.

### No Recent Activity

No recent activity found.

### Connection Error

Error: Unable to connect to GitHub.

## How It Works

1. The application receives a GitHub username from the command line.
2. It creates a request to the GitHub Events API.
3. The API returns recent public activity in JSON format.
4. The program converts the JSON response into Python data.
5. Each event is processed according to its event type.
6. The activity is displayed in the terminal.
7. API and connection errors are handled gracefully.

## Learning Outcomes

Through this project, I practiced:

* Working with REST APIs
* Sending HTTP requests in Python
* Processing JSON responses
* Using command-line arguments
* Handling API errors
* Working with Python functions
* Building a simple CLI application
* Using GitHub API data in a Python project

## API Endpoint

https://api.github.com/users/username/events

## Author

Koushik

GitHub: https://github.com/yerramsettisairamanakoushik85-arch

