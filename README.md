# 🔎 link-scout

A lightweight microservice that fetches **metadata (title, description, OpenGraph image)** and optional **screenshots** from any URL.
Built with **FastAPI**, **BeautifulSoup**, and **Playwright**.

---

## 📂 Project Structure

```
link-scout/
│── .gitignore
│── README.md
│── requirements.txt
│── Dockerfile
│── main.py
│── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── utils.py
│   └── screenshots/
│── tests/
│   └── test_api.py
│── .github/
│   └── workflows/
│       └── docker-build.yml
```

---

## ⚙️ Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/link-scout.git
   cd link-scout
   ```

2. **Create virtual environment & install deps**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on macOS/Linux
   venv\Scripts\activate      # on Windows

   pip install -r requirements.txt
   ```

3. **Install Playwright browser**

   ```bash
   playwright install chromium
   ```

---

## ▶️ Run the Service (Local)

```bash
uvicorn main:app --reload
```

* API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 Usage

### **Fetch metadata only**

```bash
curl -X POST http://127.0.0.1:8000/api/parse \
-H "Content-Type: application/json" \
-d '{"url": "https://example.com"}'
```

### **Fetch metadata + screenshot**

```bash
curl -X POST "http://127.0.0.1:8000/api/parse?screenshot=true" \
-H "Content-Type: application/json" \
-d '{"url": "https://example.com"}'
```

---

## 🐳 Docker Deployment

### **Dockerfile**

This project includes a `Dockerfile` that builds a container with all Playwright dependencies pre-installed (for Chromium screenshots).

Build & run:

```bash
docker build -t link-scout .
docker run -p 8000:8000 link-scout
```

Service will be live at: [http://localhost:8000](http://localhost:8000)

---

## 🤖 GitHub Actions (CI/CD)

### **Workflow file**

Located at: `.github/workflows/docker-build.yml`

This workflow:

* Builds the Docker image on every push to `main`
* Pushes it to Docker Hub

### **Setup**

1. In GitHub repo → **Settings → Secrets and variables → Actions**
   Add:

   * `DOCKER_USERNAME` = your Docker Hub username
   * `DOCKER_PASSWORD` = your Docker Hub token

2. Push to `main`, and your image will be available at:

   ```
   docker pull your-dockerhub-username/link-scout:latest
   ```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 📜 License

MIT License © 2025 \[Ali]

---


