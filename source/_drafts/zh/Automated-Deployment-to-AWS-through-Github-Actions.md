---
title: Automated Deployment to AWS through Github Actions
date: 2023-01-15 12:24:01
categories: [部署]
tags: [Github Actions, AWS]
thumbnail: 
excerpt: 一直在为git push - 远程访问 - git pull而苦恼？这篇文章将向你展示通过GitHub Actions部署代码的简单自动化方法。
banner: 
sticky: 
---

# 目标
在这篇文章中，我们将学习如何使用**GitHub Actions**做一个简单的自动部署。部署 "可能有不同的含义，取决于上下文。在这个特定的环境中，我们谈论的是将推送到GitHub的代码自动上传到服务器（如AWS EC2）。这在我们需要**采取重复性行动将代码设置到生产环境中**很有帮助。

就我而言，它在更新我的博客时提高了很多效率。我发现一旦我向博客上传新的东西，有挺多步骤是一直重复的。
```
- 写好文章。
1. 建立并测试编译后的博客
2. Push代码到GitHub
3. 通过SSH连接到我的服务器
4. 找到博客文件夹和git pull
- 在网站上发布可用信息。
``` 

设置完GitHub Actions后，我把它自动化成：
```
- 有写好的帖子。
1. 推送代码到Github
- 在网站上发布可用的帖子。
``` 

# 准备工作
以下是这次部署的关键作用。

### Github repo
首先，我们假设我们有一个GitHub账户。我们将启动一个新的 repo 作为例子，并将其称为 "my_deployment_project"，并将其克隆到你的电脑中的某个地方。

![创建 repo](https://raw.githubusercontent.com/Gnefil/Blog/main/img/post_images/automated_deployment_create_repo.png)

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

### 服务器
一个像AWS EC2这样的托管服务器，有一个准备发布到公共互联网的文件夹。这可以通过`Apache`、`Nginx`或其他网络服务工具实现。你也应该有你的SSH密钥来访问服务器。

为了介绍这个部署的例子，我在服务器的`home`目录下创建了一个`deployed_folder`。

```sh
Server
-------
ubuntu@ip-172-31-44-130:~$ pwd # Where I am
/home/ubuntu
ubuntu@ip-172-31-44-130:~$ ls # What is in my current directory
deployed_folder
ubuntu@ip-172-31-44-130:~$ ls deployed_folder/ -la # Show me everything inside this deployed_folder
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Jan 19 16:24 . # There is
drwxr-xr-x 6 ubuntu ubuntu 4096 Jan 19 19:37 .. # nothing
ubuntu@ip-172-31-44-130:~$
```

当然，现在它是空的。


# Automate deployment

### Set up GitHub Actions
If we look right now at our `Actions` tab in the repo, we find it empty.
![Empty Github Actions](https://raw.githubusercontent.com/Gnefil/Blog/main/img/post_images/automated_deployment_github_actions_empty.png)

You might have seen that there are all kinds of pre-established configurations for deployment to Azure, AWS, etc. servers, but in this post, we will use the simplest one there.

Click on the `configure` button in `Simple workflow` and this view comes out.

![New Workflow](https://raw.githubusercontent.com/Gnefil/Blog/main/img/post_images/automated_deployment_new_workflow.png)

In essence, to run **Github Actions**, you must create a YAML file under the `my_project/.github/workflows/` folder. Name it as you want, I have called it *deployment.yml*

In this new YAML file, you should see the following content:

# 自动部署

### 设置GitHub Actions
如果我们现在看一下repo中的 `Actions` 标签，我们会发现它是空的。
![Empty Github Actions](https://raw.githubusercontent.com/Gnefil/Blog/main/img/post_images/automated_deployment_github_actions_empty.png)

你可能已经看到，有各种预先建立的配置用于部署到Azure、AWS等服务器，但在这篇文章中，我们将使用那里最简单的配置。

点击 `configure` 中的 `Simple workflow` 按钮，这个视图就出来了。

![新workflow](https://raw.githubusercontent.com/Gnefil/Blog/main/img/post_images/automated_deployment_new_workflow.png)

实质上，要运行**Github Actions**，你必须在`my_project/.github/workflows/`文件夹下创建一个YAML文件。随意命名，我将其称为*deployment.yml*。

在这个新的YAML文件中，你应该看到以下内容。

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
      - uses: actions/checkout@v3

      # Runs a single command using the runners shell
      - name: Run a one-line script
        run: echo Hello, world!

      # Runs a set of commands using the runners shell
      - name: Run a multi-line script
        run: |
          echo Add other actions to build,
          echo test, and deploy your project.

```

### Understanding each part of the workflow
All these lines of code may sound like an overhead, but don't worry, we go through each of them.

- `name` denotes the name of this deployment workflow, I have called it *Github Actions example deployment*.
- `on` refers to the moment you want to initialise this automated deployment (automated push to your server), set it to when `push` on branches `[ "main" ]` only. If you need to include a pull request as a condition, keep it. We are going to remove it for this little project.
  - Keep the `workflow_dispatch` in `on` as this will allow you to manually start the workflow.
- `jobs` refers to the set of actions to be carried out. However, it is not as granular as `ls`, and `cd`, these kinds of commands. A clear distinction between job and job is that they can/need to run in two different **runners**. 
> **Runners** are essentially other machines (computers, virtual machines) that run the commands that you list. It can make a copy of your code repo if you need to compile any code that you produce. Notice that each runner is assigned by the name of its **operating system**, as commands and environments are different for each operating system.
- In the next indented level inside `jobs` we raise one job called *push-to-server*.
- Then, `runs-on` denotes the type of operating system we want; the runner we want to run on. Use `ubuntu-latest` as it is quite a popular option.
- Finally, inside of `steps`, we place all the commands we want into snippets that contribute to the same action.

For now, the file should look like this:

### 了解workflow的每个部分
所有这些代码行可能听起来像是恶魔的低语（？），但别担心，我们逐一进行讲解。

- `name`表示这个部署workflow的名称，我把它叫做*Github Actions example deployment*。
- `on`指的是你想初始化这个自动部署的时刻（自动推送到你的服务器），把它设置为当`push`到`[ "main"]`分支上时。如果你需要包括pull request作为条件，保留它。我们将在这个小项目中删除它。
  - 保留`workflow_dispatch`在`on`，因为这将允许你手动启动工作流。
- `jobs`指的是要执行的行动集合。然而，它不像`ls`，和`cd`这些种类的命令那样细化。一个显著区别你需要一个还是多个jobs的方法是，它们可以在两个不同的runners中运行。
> **runners**本质上是其他机器（计算机、虚拟机），运行你列出的命令。如果你需要编译你产生的任何代码，它可以对你的代码 repo 进行复制。注意，每个runner都是由其**操作系统**的名称来分配的，因为每个操作系统的命令和环境都是不同的。
- 在`jobs`里面的下一个缩进层，我们提出了一个名为*push-to-server*的job。
- 然后，`runs-on`表示我们想要的操作系统的类型；我们想要运行的runner。使用`ubuntu-latest`，因为它是一个相当流行的选项。
- 最后，在`steps`里面，我们把所有我们想要的命令放在有助于同一行动的片段中。

现在，该文件应该是这样的。

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

### 添加步骤，自动推送代码到服务器上
提醒一下，我们的最终目标是在我们进行git推送时自动将代码部署到服务器上。为了完成这个目标，我们可以将我们的步骤划分为。
1. 将整个repo复制到runner中
2. 通过SSH访问远程服务器
3. 将runner中的repo拷贝到远程服务器上

为了完成**步骤1**，我们写下以下代码：
```yml
uses: actions/checkout@v3
```
这一行将扫描你的repo，以便你的workflow可以操作它。

**第2步**主要是将你的SSH密钥存储到runner中：
```yml
env:
  SSH_KEY: SomeRandomTextThatPretendToBeASSHKey
run: |
  mkdir ~/.ssh/
  echo "${{ env.SSH_KEY }}" > ~/.ssh/id_rsa
  chmod 700 ~/.ssh/id_rsa
```
现在，对这个片断做一些解释。关键字`env`表示你想在下面的片段中使用的任何变量，以避免冗余。`run`后面有一个`|`表示你在同一步骤中编写多个命令。而在这个步骤里面，你的`run`命令通过调用`env.`下的变量（例如`env.SSH_KEY`）来检索一个变量，这需要用`${{ }}`括起来，这样就不会把这个词当成一个字符串。

之后，SSH密钥必须存储在文件名为 *~/.ssh/id_rsa* 的文件夹中。`chmod`将模式改为只读，因为我们不想在任何情况下修改SSH密钥。

另外，你可能已经注意到，在代码中明确存储SSH密钥或其他合理的信息确实不安全。因此，Github提供了一个名为**Environment Secrets**的有用功能。它在Github repo的 "Settings "标签中，"Security"，然后是 "Actions"。

![Environment Secrets](https://raw.githubusercontent.com/Gnefil/Blog/main/img/post_images/automated_deployment_env_secrets.png)

点击 `New Repository Secret` 并添加你的SSH密钥。我把它叫做SSH_KEY。一旦你完成了这些，你就会在`Repository Secrets`中看到`SSH_KEY`。现在可以通过变量名称**secrets.SSH_KEY**在Github Actions中调用这个。

![SSH Key](https://raw.githubusercontent.com/Gnefil/Blog/main/img/post_images/automated_deployment_ssh_key.png)

然后我们可以将我们的**步骤2**改为：
```yml
env:
  SSH_KEY: ${{ secrets.SSH_KEY }}
run: |
  mkdir ~/.ssh/
  echo "${{ env.SSH_KEY }}" > ~/.ssh/id_rsa
  chmod 700 ~/.ssh/id_rsa
```

最后，在**步骤3**中，我们使用`scp`，将runner当前文件夹的内容复制到远程服务器。

![runner的当前工作目录](https://raw.githubusercontent.com/Gnefil/Blog/main/img/post_images/automated_deployment_runners_working_directory.png)

从这个截图中，我们可以看到，runner的当前工作目录已经是 repo 本身。但我们想复制整个 repo，因此，我们cd出一个级别，并使用`./my_deployment_project`作为`scp`的复制源。顺便说一下，每个workflow的运行细节可以在Github的`Actions`标签中找到。点击任何一个workflow以获得更多细节。

```yml
run: |
  cd ..
  scp -o StrictHostKeyChecking=no -r ./my_deployment_project ubuntu@13.40.196.20:/home/ubuntu/deployed_folder
```

> `scp`，如果你对它不是那么熟悉的话，它是指通过使用SSH来确保CoPy的安全。这个命令的字面意思是 "将当前文件夹复制到这个user@server:this_folder"。-o是为了禁用一个选项，当这台电脑第一次试图通过SSH连接到这个服务器时，这个选项会发出警告信息，-r是为了递归复制。

现在，如果一切顺利，你应该在你的服务器端看到。
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

然而，如果你多次重复这个过程，你会发现这个错误。
![一个构建错误](https://raw.githubusercontent.com/Gnefil/Blog/main/img/post_images/automated_deployment_error.png)
这是因为第二次我们试图在同一个文件夹中`scp`，我们基本上是在替换原来的那些。为了避免这种情况，一个简单的解决方法是先把代码临时推送到临时文件夹，把它的内容移到生产文件夹，然后删除临时文件夹。

```yml
run: |
  cd ..
  scp -o StrictHostKeyChecking=no -r ./my_deployment_project ubuntu@13.40.196.20:/home/ubuntu/temp
  ssh -o StrictHostKeyChecking=no ubuntu@13.40.196.20 cp -r /home/ubuntu/temp/* /home/ubuntu/deployed_folder/ # Copy content from the temp folder to production folder
  ssh -o StrictHostKeyChecking=no ubuntu@13.40.196.20 rm -r /home/ubuntu/temp # Remove the temp folder
```

在某些时刻，这将在服务器中自动发生：
```sh
Server
------
ubuntu@ip-172-31-44-130:~$ ls
deployed_folder
ubuntu@ip-172-31-44-130:~$ ls
deployed_folder  temp
ubuntu@ip-172-31-44-130:~$ ls temp
README.md  some_file.txt
ubuntu@ip-172-31-44-130:~$ ls
deployed_folder  temp
ubuntu@ip-172-31-44-130:~$ ls
deployed_folder
```

> 当然，这不是一个解决替换问题的正确方案，因为它不会删除你在最近一次推送中删除的任何旧文件。另一个不是很解决问题的解决方案（就像这个）是在每次部署时删除整个生产文件夹并重新添加它。然而，这将暂时断掉本来正在运营的网站。更高级、更完整的技术是 "清除 "这两个文件夹之间的差异。或者使用两个备用的文件夹位置，当一个正在部署时，另一个承担起的运行的责任。

然后......我们就完成了! 现在你有了一个简单的workflow，每当你向主分支进行git push时，都会自动将你的代码推送到`~/deployed_folder`! 这就是最后产生的代码。

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
          scp -o StrictHostKeyChecking=no -r ./my_deployment_project ubuntu@13.40.196.20:/home/ubuntu/temp
          ssh -o StrictHostKeyChecking=no ubuntu@13.40.196.20 cp -r /home/ubuntu/temp/* /home/ubuntu/deployed_folder/
          ssh -o StrictHostKeyChecking=no ubuntu@13.40.196.20 rm -r /home/ubuntu/temp 
```

# 根据你的需要进行个性化定制
这只是一个非常初级和简单的部署脚本，可以根据你自己的需要来加强。例如，我为我的博客使用的版本是：
```yml
name: Blog test and deploy
run-name: ${{ github.actor }} is testing and deploying blog

on:
  workflow_dispatch:
  push:
    branches:
      - main
  pull_request:
    branches: 
      - main


jobs:
  Build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Clean install dependencies
        run: npm ci
      
      - name: Build
        run: npm run build

      - name: Deploy to remote server
        env:
          SSH_KEY: ${{ secrets.SSH_KEY }}
        run: |
          mkdir ~/.ssh/
          echo "${{ env.SSH_KEY }}" > ~/.ssh/id_rsa
          chmod 700 ~/.ssh/id_rsa
          scp -o StrictHostKeyChecking=no -r ./public ubuntu@13.40.196.20:/home/ubuntu/blog
          ssh -o StrictHostKeyChecking=no ubuntu@13.40.196.20 sudo cp -r /home/ubuntu/blog/* /var/www/html/blog/
          ssh -o StrictHostKeyChecking=no ubuntu@13.40.196.20 rm -r /home/ubuntu/blog

```

在这个脚本中，我通过引入`npm`（Node Package Manager）命令来节省安装、编译和测试的时间，我需要用这些命令来渲染我的博客。在使用GitHub Actions之前，我需要用`hexo g`在电脑上编译整个项目（hexo是一个基于Node的博客框架），然后用`hexo d`push，只push`public`文件夹。现在我使用GitHub Actions，我可以忘掉这一切，直接git push。Workflow会处理剩下的问题。