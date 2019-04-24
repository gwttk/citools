import sys
import os
from github import Github

repo_fullname =os.environ['TRAVIS_REPO_SLUG']
tagname =os.environ['TRAVIS_TAG']

g = Github(os.environ['GITHUBTOKEN'])

print('uploading to repo:',repo_fullname)
repo = g.get_repo(repo_fullname)

print('uploading to tag:',tagname)
release = repo.get_release(tagname)

for a in release.get_assets():
	print('existed asset:',a.name)
	print('delete asset:',a.name)
	a.delete_asset()

for file in sys.argv[1:]:
	print('uploading file:',file)
	release.upload_asset(file)