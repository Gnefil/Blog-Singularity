---
title: Automated Deployment to AWS through Github Actions
date: 2023-01-15 12:23:53
categories: [Deployment]
tags: [Tech Stack, Github Actions, AWS]
thumbnail: images/thumbnails/auto_deploy.jpg
excerpt: Frustrated about git pushing - remote access - git pulling all the time? This post will show you a simple automated way to deploy code through GitHub Actions.
banner: 
sticky: 
expires: 2024-07-25 18:52:00
---

# Aims
In this post, we are going to learn how to make a simple automated deployment using **GitHub Actions**. `Deployment` may have various meanings depending on the context. In this particular one, we are talking about uploading automatically the code pushed to GitHub into a server (like AWS EC2). This is helpful in cases **where we need to take repetitive actions to set code into production**.

In my case, it increases a lot of efficiencies when updating my blog. I find it a bit redundant to repeat the same steps once I upload something new to the blog: 
```
-> Have the post written.
0. Build and test the compiled blog
1. Push code to GitHub
2. Connect to my server via SSH
3. Find the blog folder and git pull
4. Build the blog
-> Post available on the website.
``` 

After setting up GitHub Actions, I automated it into:
```
-> Have the post written.
1. Push code to Github
-> Post available on the website.
``` 

# Preparatives
Here are the key roles of this deployment.

## Github repo
First of all, we assume that we have a GitHub account. We will start a new repo as an example and call it "my_deployment_project", and place clone it somewhere in your computer.

![Create repo](images/illustrations/auto_deploy.create_repo.png)

```sh
Computer
-------
> git clone git@github.com:Gnefil/my_deployment_project.git
Cloning into 'my_deployment_project'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

> cd my_deployment_project
my_deployment_project>

> ls
README.md

> echo "Hello World!" >> some_file.txt # Create some random file as files we need to deploy

> ls
README.md  some_file.txt 
```

## Server
A hosted server like AWS EC2, with a folder that is prepared to be posted to the public internet. This can be achieved via `Apache`, `Nginx`, or other web-serving tools. You should have your SSH key to access the server as well.

To present this deployment with an example, I created a `deployed_folder` in my `home` directory on the server.

```sh
Server
-------
ubuntu@ip-172-31-44-130:~$ pwd # Where am I
/home/ubuntu
ubuntu@ip-172-31-44-130:~$ ls # What is in my current directory
deployed_folder
ubuntu@ip-172-31-44-130:~$ ls deployed_folder/ -la # Show me everything inside this deployed_folder
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Jan 19 16:24 . # There is
drwxr-xr-x 6 ubuntu ubuntu 4096 Jan 19 19:37 .. # nothing
ubuntu@ip-172-31-44-130:~$
```

Right now it is empty.

# Automate deployment

## Set up GitHub Actions
If we look right now at our `Actions` tab in the repo, we find it empty.
![Empty Github Actions](images/illustrations/auto_deploy.github_actions_empty.png)

You might have seen that there are all kinds of pre-established configurations for deployment to Azure, AWS, etc. servers, but in this post, we will use the simplest one there.

Click on the `configure` button in `Simple workflow` and this view comes out.

![New Workflow](images/illustrations/auto_deploy.new_workflow.png)

In essence, to run **Github Actions**, you must create a YAML file under the `my_project/.github/workflows/` folder. Name it as you want, I have called it *deployment.yml*

In this new YAML file, you should see the following content:
```yml
# This is a basic workflow to help you get started with Actions

name: CI

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the "main" branch
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v4

      # Runs a single command using the runners shell
      - name: Run a one-line script
        run: echo Hello, world!

      # Runs a set of commands using the runners shell
      - name: Run a multi-line script
        run: |
          echo Add other actions to build,
          echo test, and deploy your project.

```

## Understanding each part of the workflow
All these lines of code may sound bad enough, but don't worry, we go through each of them.

- `name` denotes the name of this deployment workflow, I have called it *Github Actions example deployment*.
- `on` refers to the moment you want to initialise this automated deployment (automated push to your server), set it to when `push` on branches `[ "main" ]` only. If you need to include a pull request as a condition, keep it. We are going to remove it for this little project.
  - Keep the `workflow_dispatch` in `on` as this will allow you to manually start the workflow.
- `jobs` refers to the set of actions to be carried out. However, it is not as granular as `ls`, and `cd`, these kinds of commands. A clear distinction between job and job is that they can/need to run in two different **runners**. 
> **Runners** are essentially other machines (computers, virtual machines) that run the commands that you list. It can make a copy of your code repo if you need to compile any code that you produce. Notice that each runner is assigned by the name of its **operating system**, as commands and environments are different for each operating system.
- In the next indented level inside `jobs` we raise one job called *push-to-server*.
- Then, `runs-on` denotes the type of operating system we want; the runner we want to run on. Use `ubuntu-latest` as it is quite a popular option.
- Finally, inside of `steps`, we place all the commands we want into snippets that contribute to the same action.

For now, the file should look like this:
```yml
name: Github Actions example deployment

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  push-to-server:
    runs-on: ubuntu-latest

    steps:

```

## Add steps to push code to the server automatically
Reminding that our final goal is to deploy the code to the server automatically whenever we make a git push. In order to complete that, we can divide our steps as:
1. Copy the entire repo to the runner
2. Access the remote server through SSH
3. Copy the repo in the runner to the remote server

To complete **step 1** we write down the following code:
```yml
uses: actions/checkout@v4
```
This line scans through your repo so that your job can manipulate it.

**Step 2** is essentially storing your SSH Key into the runner:
```yml
env:
  SSH_KEY: SomeRandomTextThatPretendsToBeASSHKey
run: |
  mkdir ~/.ssh/
  echo "${{ env.SSH_KEY }}" > ~/.ssh/id_rsa
  chmod 700 ~/.ssh/id_rsa
```
Now, some explanations for this snippet. The keyword `env` denotes any variables that you want to use in the following snippet, to avoid redundancy. `run` followed by a `|` means that you are writing multiple commands in the same step. And inside this step, your `run` command retrieves a variable via invoking a variable under `env.` (e.g. `env.SSH_KEY`), and this needs to be enclosed by `${{  }}` so that the word is not taken literary as a string.

Later, the SSH key must be stored in a folder with file name *~/.ssh/id_rsa*. `chmod` changes the mode to read-only, which makes sense as we don't want to modify the SSH key in any of the cases. 

Also, you might have noticed that it is really unsafe to store SSH keys or other sensible pieces of information explicitly there in the code. Therefore, Github provides a helpful function called **Environment Secrets**. It is in the `Settings` tab in the Github repo, `Security`, and then `Secrets and Variables` - `Actions`.

![Environment Secrets](images/illustrations/auto_deploy.env_secrets.png)

Click on `New Repository Secret` and add your SSH key. I have called it SSH_KEY. Once you have done that, you will see `SSH_KEY` in the `Repository Secrets`. And this can be now invoked in Github Actions by variable name **secrets.SSH_KEY**.

![SSH Key](images/illustrations/auto_deploy.ssh_key.png)

Then we can change our **step 2** to by calling *secrets.name_of_key*:
```yml
env:
  SSH_KEY: ${{ secrets.SSH_KEY }}
run: |
  mkdir ~/.ssh/
  echo "${{ env.SSH_KEY }}" > ~/.ssh/id_rsa
  chmod 700 ~/.ssh/id_rsa
```

Finally, in **step 3** we make use of `scp`, to copy the contents of the current folder of the runner into the remote server.

![Current working directory of the runner](images/illustrations/auto_deploy.runners_working_directory.png)

From this screenshot, we can see that the current working directory of the runner is already the repo itself. But we want to copy the entire repo, thus, we cd out a level, and use `./my_deployment_project` as the source of copy in `scp`. By the way, details of each run of workflow can be found in the `Actions` tab in Github. Click on any of the workflows for more details.

```yml
run: |
  cd ..
  scp -o StrictHostKeyChecking=no -r ./my_deployment_project ubuntu@13.40.196.20:/home/ubuntu/deployed_folder
```

> `scp`, if you are not that familiar with it, stands for Secure CoPy, by using SSH. This command literally says "copy the current folder into this user@server:this_folder". Dash o to disable an option that warns a message that comes out when it is the first time this computer trying to connect to this server by SSH, and dash r to recursively copy.

Now, if everything went successfully, you should see in your server-side:
```sh
Server
------
ubuntu@ip-172-31-44-130:~$ ls
deployed_folder
ubuntu@ip-172-31-44-130:~$ ls deployed_folder/ # Effectively deployed
my_deployment_project
ubuntu@ip-172-31-44-130:~$ ls deployed_folder/my_deployment_project/ # The content of repo are copied
README.md  some_file.txt
ubuntu@ip-172-31-44-130:~$
```

However, if you repeat this process various times, you find this error.
![A build error](images/illustrations/auto_deploy.error.png)
This is because the second time we are trying to `scp` in the same folder, we are essentially replacing the original ones. To avoid that, we could remove the production folder and copy the new one to it again.

```yml
run: |
  cd ..
  ssh -o StrictHostKeyChecking=no ubuntu@13.40.196.20 rm -rf ~/deployed_folder # Remove production folder
  scp -o StrictHostKeyChecking=no -r ./my_deployment_project ubuntu@13.40.196.20:~/deployed_folder
```

> Of course, this is one way to workaround this problem. It will derive an impaired web service for the duration of the deployment. If a few seconds or minutes of downtime is not a problem for you, then you can try this You could also try pushing the code first to the home directory temporally, move its content to the production folder, and then remove the temp folder. Old unwanted files won't be removed though. More advanced and complete techniques would be to `rm` the differences between the two folders. Or to use two alternate folder locations, and while one is being deployed, run the other one in operation. 

And... we are done! Now you have a simple workflow that automatically pushes your code to `~/deployed_folder` whenever you make a git push to the main branch! This is the resulting code.

```yml
name: GitHub Actions example deployment

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  push-to-server:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Access and push to remote server
        env:
          SSH_KEY: ${{ secrets.SSH_KEY }}
        run: |
          mkdir ~/.ssh/
          echo "${{ env.SSH_KEY }}" > ~/.ssh/id_rsa
          chmod 700 ~/.ssh/id_rsa
          cd ..
          ssh -o StrictHostKeyChecking=no ubuntu@13.40.196.20 rm -rf ~/deployed_folder # Remove production folder
          scp -o StrictHostKeyChecking=no -r ./my_deployment_project ubuntu@13.40.196.20:~/deployed_folder
```

# Personalise to your needs
This is only a very beginner and simple deployment script, which can be enhanced depending on your own needs. For example, the version I use for my blog (at the moment of edit) is:
```yml
name: Deploy to production server
run-name: ${{ github.actor }} is deploying blog to production server

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

  workflow_dispatch:

jobs:
  Deploy:
    runs-on: ubuntu-latest

    env:
      ssh-prefix: ssh -o StrictHostKeyChecking=no ubuntu@13.40.196.20
      scp-prefix: scp -o StrictHostKeyChecking=no -r
      temp-dir: /home/ubuntu/blog
      prod-dir: /var/www/html/blog
      esc-prod-dir: \/var\/www\/html\/blog

    steps:
      - uses: actions/checkout@v4

      - name: Clean install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Deploy to remote server
        run: |
          mkdir ~/.ssh/
          echo "${{ secrets.SSH_KEY }}" > ~/.ssh/id_rsa
          chmod 700 ~/.ssh/id_rsa
          mv ./public ./blog
          ${{ env.ssh-prefix }} rm -rf ${{ env.temp-dir }}
          ${{ env.scp-prefix }} ./blog ubuntu@13.40.196.20:${{ env.temp-dir }}

      - name: Check content existence
        run: ${{ env.ssh-prefix }} 'if [ -d ${{ env.temp-dir }} ]; then echo "temporal folder is not empty"; else echo "temporal folder is empty"; fi'

      - name: Update production folder
        run: | 
          ${{ env.ssh-prefix }} sudo rm -rf ${{ env.prod-dir }}
          ${{ env.ssh-prefix }} sudo mv ${{ env.temp-dir }} ${{ env.prod-dir }}

```

In this script, I saved the installation, compilation and testing time by introducing `npm` (Node Package Manager) commands that I need to use to create the style of my blog. Before I used GitHub Actions, I would need to compile the whole project on my computer with `hexo g` (hexo is a Node-based blog framework), and push with `hexo d` to only push the `public` folder. And now that I use GitHub Actions, I can forget all about it and just push it. The workflow deals with the rest.