# citools is "continuous integration (CI) tools"

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
Remember to copy your new personal access token when it's done. You won’t be able to see it again!  
You may also regenerate a token if you forget it, but this means the old token will be invalid.

1. Now githubrelease.py needs to access this token during the build.  
But you can't put it directly in .travis.yml file, because then everyone would see it, especially on a public repo.  
A secure way is to put this token at Travis-CI's repository setting. You can read the details [here](https://docs.travis-ci.com/user/environment-variables/#defining-variables-in-repository-settings).  
Simply put, go to this url `https://travis-ci.com/<your_username>/<your_repo>/settings`, add an environment variable, whose name is "GITHUBTOKEN" and value is the token.  
Remember to **DISABLE** "display value in build log" switch, otherwise anyone who sees your build log can steal your access token.

1. Now finally, edit your .travis.yml file, adding following configs. Explanation follows.
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
    `sudo apt-get install -y python3-pip` This line installs pip3. We need it to install pip modules.  
    `sudo pip3 install PyGithub` This line installs PyGithub, which is a lib of github's web api. githubrelease.py uses it.  
    `wget ...` This line downloads githubrelease.py.  
    `script: python3 githubrelease.py "file1.zip" "file2.exe"` This line tells the githubrelease.py to upload files.  

1. Notice that we use `on:` `tags:true`. This means that githubrelease.py will only run after you publish a release.  
Go to your github repo's release page and publish a release. A travis build will be triggered.  
After a while, the build would finish and githubrelease.py will upload files to the release as assets. Congrats!

1. There are many ways to customize the release/upload process, the above method is just what I use.  
If you have some questions or need a different approach, feel free to open an issue or even a PR.
