# Devaten On-Premises

## How to Install 

To run the On-Premise MySQL Agent Docker Compose File locally, you must have Git, Docker and Docker Compose installed and do the following:

# Manual Installation Guide

This guide describes how to manually install and run the Devaten On-Premises Agent and supporting services.  
Use this if you are not using Azure auto-deploy or prefer manual setup.

---

## 1. Update System Packages

```bash
sudo apt-get update
```

---

## 2. Install Dependencies

```bash
sudo apt-get install -y docker.io curl git snapd
```

Enable Docker service:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

---

## 3. Clone Repository

```bash
cd /home/<your-admin-username>
git clone https://github.com/devatengit/onpremises-common-agent.git
cd onpremises-common-agent
mkdir -p whisper
```
> Replace `<your-admin-username>` with your actual VM username.

---

## 4. Install Docker Compose

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

---

## 5. Start Containers

```bash
sudo docker-compose pull
sudo docker-compose up -d
```

---

## 6. Install Ollama & Pull Model

```bash
sudo snap install ollama
sleep 10
ollama pull llama3:8b
```

---

## How to Run

### ✅ Check running containers

```bash
sudo docker ps
```

### 🌐 Access the Dashboard

Open [http://localhost:8081/](http://localhost:8081/) in your browser.

---

### Add your agent

- Add your application and database
- Start monitoring

---

## ⚙️ Manage Containers

**Stop containers:**
```bash
sudo docker-compose pause
```

**Resume containers:**
```bash
sudo docker-compose unpause
```

**View logs:**
```bash
sudo docker logs -f <Container_Name>
```

**Remove containers:**
```bash
sudo docker-compose down
```
## 📡 API Usage

After the Docker Compose setup is up and running, and Ollama has been pulled,  
you can start using the APIs.

You can send audio files and receive transcriptions and classifications via AI.

**Transcription API Example:**
```
POST http://host:8081/devaten/audio/transcribe/?file
```
- Send an audio file as `multipart/form-data` with the key `file`.
- The response will contain the transcription.

**Classification:**
- The current prompts are defined in the `docker-compose.yml` file.
- There is a demo set up for "Patients" classification, which you can customize to fit your own use case.

**Prompt configuration keys:**
- `ollama.request.prompt`
- `ollama.classification.prompt`

Edit these in your `docker-compose.yml` to change the AI's behavior for your scenario.
