## citools is "continuous integration (CI) tools"

## QuickStart

### githubrelease.py
This script allows your Travis-CI build to upload files to a GitHub release

1. Before using this script, make sure that you've already set up Travis-CI corretly, and your builds are running fine.  
If you've never used Travis-CI before, check its [website](https://docs.travis-ci.com/) for more info.
1. Files in a github release are called assets. In order to upload assets, githubrelease.py needs some permission. This is done by providing a "GITHUB OAUTH TOKEN".
1. add following to .travis.yml

```yaml
before_install:
    - sudo apt-get install -y python3-pip
before_deploy:
    # install PyGithub
    - sudo pip3 install PyGithub
    # download githubrelease.py
    - wget https://raw.githubusercontent.com/Immueggpain/citools/master/githubrelease.py
deploy:
    provider: script
    script: python3 githubrelease.py "file1.zip" "file2.exe"
    skip_cleanup: true
    on:
        tags: true
```
