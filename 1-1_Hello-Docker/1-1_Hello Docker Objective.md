# 🎯 PROJECT 1.1 – Hello Docker

**Difficulty:** Beginner | **Duration:** 3–4 hours | **Tech Stack:** Docker, Python, Bash

---

## 📌 Objective

Create and run your **first Docker container** with a simple Python script. Understand the fundamental concepts of Docker: images, containers, Dockerfile.

**Learning objective:** Move from "I've heard of Docker" to "I built and ran a container myself."

---

## 📋 Specifications

### What You'll Build

A **Docker container** that:

1. Uses a Python 3.x base image
2. Contains a simple Python script that displays "Hello Docker World!"
3. Runs the script when you start the container
4. Can be rebuilt and restarted at will

### Deliverables

- [ ]  **Dockerfile**: configuration file for building the image
- [ ]  [**hello.py**](http://hello.py/): simple Python script
- [ ]  [**README.md**](http://readme.md/): explains how to build and run the container
- [ ]  **GitHub repo**: the code, committed and pushed
- [ ]  **Screenshot/log**: proof that the container ran

---

## 🔧 Prerequisites

- [ ]  **Docker Desktop installed** and working
    - Download: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
    - Verification: `docker --version` in the terminal
    - Quick test: `docker run hello-world` (should display "Hello from Docker!")
- [ ]  **Comfortable with terminal/CLI**
    - Ability to navigate folders
    - Run basic commands (mkdir, cd, etc.)
- [ ]  **GitHub account** (for pushing code)
    - [https://github.comr](https://github.com/) (if not already done)
- [ ]  **Python 3 installed locally** (optional, but useful for testing before Docker)

---

## 📚 Official Resources

These resources will give you everything you need:

1. **Docker Official Getting Started** (8 min video)
    - [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)
    - Explains: images, containers, Dockerfile basics
2. **Dockerfile Reference (Official)**
    - [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
    - Search for keywords: `FROM`, `COPY`, `RUN`, `CMD`
3. **Docker Best Practices**
    - [https://docs.docker.com/develop/dev-best-practices/](https://docs.docker.com/develop/dev-best-practices/)
    - Why we structure it this way (not essential, but useful)
4. **YouTube: "Docker in 100 Seconds"** (if you prefer video)
    - [https://www.youtube.com/results?search_query=docker+in+100+seconds](https://www.youtube.com/results?search_query=docker+in+100+seconds)
    - https://youtu.be/Ud7Npgi6x8E?si=rsAOtzQHx0u14abX
    - https://www.youtube.com/playlist?list=PLsz00TDipIfcc6X5TECsuk0YNGWIx5HMl

---

## 🎯 Success Criteria

Before saying "I'm done," validate these points:

- [ ]  **Dockerfile exists** and is syntactically valid
    - No errors when you look at it
    - It contains the essential keywords
- [ ]  **Image builds without errors**
    - The `docker build` command succeeds
    - No "ERROR" or "fail" messages
- [ ]  **Container runs and displays output**
    - `Docker run` command displays "Hello Docker World!" (or similar)
    - Container terminates cleanly
- [ ]  **Code is versioned**
    - GitHub repo created
    - Dockerfile + [hello.py](http://hello.py/) + README committed and pushed
    - Descriptive commit message (e.g., "Initial commit: Hello Docker project")
- [ ]  **README is clear**
    - Someone else can read and understand how to build/run
    - Contains the exact steps
    - README
        
        

---

## 💡 Hints Gradually retrieve

**See the PROJECT_1.1_HINTS.md file if you get stuck.**

---

## 🛣️ Suggested steps (TRY THESE YOURSELF FIRST)

1. Create a local folder `/project-1-1` (or whatever name you want)
2. Create a `hello.py` file with a simple print statement
3. Create a `Dockerfile` (look up the structure in the Docker documentation)
4. Test locally if possible (run `python hello.py` just to see that the script works)
5. Create the Docker image: `docker build -t my-hello-docker .`
6. Launch the container: `docker run my-hello-docker`
7. Check the output
8. Create a GitHub repo and push your code
9. Create a README
10. Final commit & push

---

## 🚨 Common Mistakes to Avoid

(Don't read this until you've tried!)

- ❌ **Forgetting the `FROM` line**: Every Dockerfile needs a base image
- ❌ **Not understanding COPY vs ADD vs RUN**: Each does something different
- ❌ **CMD vs ENTRYPOINT confusion**: Both can run commands, but are used differently
- ❌ **Ignoring file paths**: Your COPY command needs correct source/destination
- ❌ **Not testing locally first**: Build your script locally before containerizing

---

## 📊 Difficulty Breakdown

| Step | Difficulty | Time Est. |
| --- | --- | --- |
| Install Docker | ✅ Easy | 5–10 min |
| Write [hello.py](http://hello.py/) | ✅ Easy | 5 min |
| Understand Dockerfile structure | ⚠️ Medium | 20–30 min |
| Write Dockerfile | ⚠️ Medium | 15–20 min |
| Build image | ✅ Easy | 2–3 min |
| Run container | ✅ Easy | 1 min |
| Set up GitHub + push | ⚠️ Medium | 10–15 min |
| Write README | ⚠️ Medium | 10–15 min |
| **TOTAL** |  | **90–110 min** |

**Realistic time if you search and debug:** 3–4 hours

---

## ✅ How to Know You're Done

When you can say:

> "I built a Docker image from scratch, ran a container, and the Python script executed inside it. I understand what a Dockerfile does and why we use it. The code is on GitHub."
> 

---

## 🎁 Bonus (After You Finish)

Once basic Hello Docker is working:

1. **Modify the script**: Make it ask for user input, do calculations, etc.
2. **Add environment variables**: Use ENV in Dockerfile
3. **Multi-stage build**: Learn how professionals structure Dockerfiles
4. **Docker Compose**: Run multiple containers together (preview of Project 1.2)

But **not required** for this project. Focus on nailing the basics first.

---

## 📅 Timeline

- **Week 1 (Jan 12–18)**: Read brief, start research, write [hello.py](http://hello.py/)
- Build Dockerfile, debug build errors
- Test + polish, write README, push to GitHub
- Project done, move to Project 1.2

---

**Ready? Start with research: Google "Python Docker tutorial" or check the official docs linked above. Good luck!** 🚀