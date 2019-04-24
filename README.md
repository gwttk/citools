## citools is "continuous integration (CI) tools"

## QuickStart

### githubrelease.py
This script allows your Travis-CI build to upload files to a GitHub release.

1. Before using this script, make sure that you've already set up Travis-CI corretly, and your builds are running fine.  
If you've never used Travis-CI before, check its [website](https://docs.travis-ci.com/) for more info.

1. Files in a github release are called assets. In order to upload assets, githubrelease.py needs some permission.  
This is done by providing a "github personal access token".  
To create such token, visit github's [Personal access tokens page](https://github.com/settings/tokens), then click "Generate new token" button.  
Now enter a mnemonic discription at "Token description", for example, "travis upload token".  
If you plan to use githubrelease.py only on public repositories, then select "public_repo" scope.  
However, if you want to use githubrelease.py on both public and private repositories, select "repo" scope.  
Click "Generate token" button to finish creating the token.  
Remember to copy your new personal access token now. You won’t be able to see it again!  
You may also regenerate a token if you forget it, but this means the old token will be invalid.

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
