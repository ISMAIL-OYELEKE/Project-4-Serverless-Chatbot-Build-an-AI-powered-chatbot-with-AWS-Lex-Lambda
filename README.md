# Serverless AI Chatbot with AWS Lex & Lambda 🤖

**A conversational AI assistant built to engage recruiters and hire me instantly.**

This project demonstrates the deployment of a fully serverless chatbot integrated into a personal portfolio website. It leverages **Amazon Lex** for Natural Language Understanding (NLU), **AWS Lambda** for serverless backend logic, and **Kommunicate.io** for the frontend user interface.

---

## 📖 Project Overview
Static portfolio websites often lack engagement. To solve this, I built an intelligent agent that provides instant, 24/7 responses to recruiters. Instead of searching through pages, visitors can simply ask:
> *"Do you know AWS?"*
> *"Show me your projects."*
> *"How do I contact you?"*

The bot answers instantly with dynamic data fetched from the cloud.

## 🏗️ Architecture

![Architecture Diagram](Add_Your_Architecture_Diagram_Here.png)
*(Replace the link above with your actual architecture diagram image)*

The solution uses a **Serverless Event-Driven Architecture**:
1.  **Frontend:** The user chats via the **Kommunicate.io** widget embedded on the portfolio site.
2.  **NLU Layer:** **Amazon Lex V2** processes the text to understand User Intent (e.g., "GetSkills").
3.  **Compute Layer:** **AWS Lambda** (Python) triggers the specific logic for that intent and returns the response.
4.  **Security:** **AWS IAM** roles ensure least-privilege access between Lex and Lambda.

---

## 🛠️ Tech Stack
* **Cloud Provider:** AWS
* **AI/ML Service:** Amazon Lex V2 (Natural Language Understanding)
* **Compute:** AWS Lambda (Python 3.9)
* **Frontend Integration:** Kommunicate.io (JavaScript Widget)
* **Security:** AWS IAM (Roles & Policies)
* **Version Control:** Git & GitHub

---

## 🚀 Key Features
* **Auto-Greeting:** Initiates conversation immediately when the site loads using a custom JavaScript trigger.
* **Smart Fallback:** Handles unknown queries gracefully by guiding the user back to known topics.
* **Rich Media Responses:** Returns clickable links for GitHub repositories and Credly badges.
* **Context Awareness:** Distinguishes between similar queries (e.g., "Skills" vs. "Projects") using a high NLU confidence threshold (0.70).

---

## 📸 Implementation Highlights

### 1. Building the "Brain" (AWS Lambda)
I wrote a Python script to handle backend fulfillment. This script acts as the central logic, deciding what text or links to send back based on the user's question.

👉 **View the full source code here:** [`lambda_function.py`](./lambda_function.py)

<img width="1920" height="1280" alt="2  script" src="https://github.com/user-attachments/assets/a2c56201-dbbe-4146-83c3-81f56899be9b" />


### 2. Creating the Bot (Amazon Lex)
I configured a custom bot with 6 specific intents covering the most common recruitment questions:
* `GetIntroduction`
* `GetSkills`
* `GetProjects`
* `GetCertifications`
* `GetContact`
* `GetGreetings`

<img width="1920" height="1280" alt="4  intent" src="https://github.com/user-attachments/assets/e2bf0bf7-5995-4214-a752-47691aead4af" />


### 3. Frontend Integration
I integrated the bot into my `index.html` using a custom script that forces a "Welcome" event on load, ensuring the user sees the menu immediately.

<img width="1920" height="1280" alt="8  ai incorporation" src="https://github.com/user-attachments/assets/715109fc-ff03-4974-b4d0-08ca22a92b23" />


---

## 💡 Challenges & Solutions

### Challenge 1: The "Silent Welcome" Bug
**Issue:** The chat widget would load but say nothing, or trigger an error because it sent a hidden "Welcome" signal the bot didn't understand.
**Solution:** I programmed a custom `onInit` function in JavaScript to manually trigger a `GetGreetings` intent 1 second after the widget loads.

### Challenge 2: NLU Overfitting
**Issue:** The bot confused "What is your favorite food?" with "What is your stack?" because the sentence structure was identical.
**Solution:** I increased the **Confidence Score Threshold** to **0.70**, forcing the bot to only answer when it is sure, eliminating false positives.

---

## 🏆 Project Outcome
I successfully deployed a fully functional AI assistant on ismailoyeleke.com. The bot correctly identifies user intent, serves dynamic content (links, lists) via Python, and handles errors gracefully. This project demonstrates proficiency in Serverless Logic, Natural Language Understanding, and Frontend-Backend Integration.

* **Cost:** $0.00 (Utilizing AWS Free Tier for Lambda & Lex).
* **Performance:** Sub-second response latency.
* **Availability:** 24/7 uptime with no server management required.

---
*Created by [Oyeleke Ismail](https://www.linkedin.com/in/ismail-oyeleke-6930b6317/) - AWS Certified Solutions Architect*
