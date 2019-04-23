import sys
import os
import mimetypes
from github import Github

repo_fullname =os.environ['TRAVIS_REPO_SLUG']
tagname =os.environ['TRAVIS_TAG']

g = Github(print(os.environ['GITHUBRTOKEN']))

repo = g.get_repo(repo_fullname)
release = repo.get_release(tagname)
for file in sys.argv:
	mtype = mimetypes.guess_type(file)[0]
	print(mtype)
	release.upload_asset(file, '', mtype)
	print(release)