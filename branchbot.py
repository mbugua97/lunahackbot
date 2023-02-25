from github import Github
from datetime import datetime, timedelta

access_token = "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"
g = Github(access_token)

owner = "mbugua97"
repo_name = "isas"
inactive_days =10

repo = g.get_repo(f"{owner}/{repo_name}")
branches = repo.get_branches()

inactive_branches = []
for branch in branches:
    last_commit_date = branch.commit.committer.date
    days_since_last_commit = (datetime.now() - last_commit_date).days
    if days_since_last_commit > inactive_days:
        inactive_branches.append(branch.name)

print(f"Inactive branches: {inactive_branches}")
