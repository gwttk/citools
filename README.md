## citools

## QuickStart

### githubrelease.py

To allow Travis-CI upload assets to GitHub releases, add following to .travis.yml

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
