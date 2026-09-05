# 🌐 Portfolio Website

A personal portfolio website built using **Flask, HTML, CSS, and JavaScript** and deployed using **Docker, GitHub Actions CI/CD, Kubernetes, and Render**.

The project demonstrates an automated deployment pipeline where changes pushed to GitHub are automatically built and deployed to the live website.

---

## 🚀 Live Website

🌐 **Live Portfolio:**  
https://portfolio-wedsite.onrender.com

---

## 📌 Project Overview

This portfolio website showcases my:

- 👨‍💻 Skills
- 📚 Education
- 🚀 Projects
- 💼 Experience
- 📄 Resume
- 📧 Contact information

The main objective of this project is not only to create a portfolio website but also to implement a **Continuous Integration and Continuous Deployment (CI/CD) pipeline**.

Whenever I make changes to the project and push them to GitHub, the application is automatically deployed to the live website.

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask

### DevOps

- Git
- GitHub
- GitHub Actions
- Docker
- Docker Hub
- Kubernetes
- Render

---

## 📂 Project Structure

```text
portfolio/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md

⚙️ Application Architecture

                   ┌─────────────────┐
                   │     User        │
                   └────────┬────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │ Live Website    │
                   │    Render       │
                   └────────┬────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │ Flask Backend   │
                   └────────┬────────┘
                            │
             ┌──────────────┴──────────────┐
             ▼                             ▼
       HTML/CSS/JS                    REST API



CI/CD Pipeline

The project uses GitHub Actions to automate the build and deployment process.

Developer
    │
    │ git push
    ▼
┌──────────────┐
│    GitHub    │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│ GitHub Actions   │
│     CI/CD        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Docker Build     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   Docker Hub     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   Kubernetes     │
└──────────────────┘


📈 CI/CD Benefits

This project demonstrates:

✅ Continuous Integration
✅ Continuous Deployment
✅ Automated Docker image building
✅ Automated Docker Hub publishing
✅ Kubernetes deployment
✅ Automatic Render deployment
✅ Git-based version control
✅ Automated deployment after Git push
✅ Containerized Flask application
🎯 Future Improvements
Add a custom domain
Add HTTPS configuration
Add database integration
Add automated testing
Add code quality checks
Add monitoring
Add application logging
Add Kubernetes cloud deployment
Add production-grade secrets management
👨‍💻 Author
Ketan Patil

Engineering Student | Python & Flask | AI & DevOps Learner

GitHub

https://github.com/KetanPatil9907

⭐ Project Highlights

A Flask-based portfolio website with Docker containerization and automated CI/CD deployment using GitHub Actions and Render.

GitHub → GitHub Actions → Docker → Docker Hub → Kubernetes / Render → Live Website
