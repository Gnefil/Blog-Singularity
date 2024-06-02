# Gnefil's Singularity

Welcome to the repository of Gnefil's Singularity. This blog is built using [Hexo](https://hexo.io/), a fast, simple and powerful blog framework. Theme used: [Redefine](https://github.com/EvanNotFound/hexo-theme-redefine).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Node.js](https://nodejs.org/)
- [Hexo](https://hexo.io/)

### Installation

1. Clone the repository
```sh
git clone https://github.com/Gnefil/Blog-Singularity.git
```
2. Install dependencies
```sh
npm install
```
3. Generate content and run the local server
```sh
hexo clean
hexo generate
hexo server
```
4. Visit `http://localhost:4000` in your browser

## Deployment

For deployment this project uses GitHub Actions to control the CI/CD, adding on `ssh` to push to remote server. 

## Last notes

This repo is not intended for collaborative development but any issues, pull requests and suggestions are welcomed!
