import sys
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def get_github_activity(username):
    url = "https://api.github.com/users/" + username + "/events"

    request = Request(
        url,
        headers={
            "User-Agent": "GitHub-Activity-CLI"
        }
    )

    try:
        with urlopen(request) as response:
            data = json.loads(response.read().decode("utf-8"))
            return data

    except HTTPError as error:
        if error.code == 404:
            print("Error: GitHub user not found.")
        else:
            print("Error: GitHub API returned an error.")
        return None

    except URLError:
        print("Error: Unable to connect to GitHub.")
        return None


def display_activity(activity):
    if not activity:
        print("No recent activity found.")
        return

    print("\nGitHub Activity")
    print("----------------")

    for event in activity:
        event_type = event.get("type")
        repository = event.get("repo", {}).get("name", "Unknown repository")

        if event_type == "PushEvent":
            print(f"- Pushed commits to {repository}")

        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action", "updated")
            print(f"- {action.capitalize()} an issue in {repository}")

        elif event_type == "WatchEvent":
            print(f"- Starred {repository}")

        elif event_type == "CreateEvent":
            ref_type = event.get("payload", {}).get("ref_type", "resource")
            print(f"- Created a {ref_type} in {repository}")

        elif event_type == "PullRequestEvent":
            action = event.get("payload", {}).get("action", "updated")
            print(f"- {action.capitalize()} a pull request in {repository}")

        elif event_type == "ForkEvent":
            print(f"- Forked {repository}")

        elif event_type == "DeleteEvent":
            ref_type = event.get("payload", {}).get("ref_type", "resource")
            print(f"- Deleted a {ref_type} in {repository}")

        elif event_type == "ReleaseEvent":
            action = event.get("payload", {}).get("action", "published")
            print(f"- {action.capitalize()} a release in {repository}")

        else:
            readable_type = event_type.replace("Event", "") if event_type else "Activity"
            print(f"- {readable_type} in {repository}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <username>")
        return

    username = sys.argv[1]

    activity = get_github_activity(username)

    if activity is not None:
        display_activity(activity)


if __name__ == "__main__":
    main()