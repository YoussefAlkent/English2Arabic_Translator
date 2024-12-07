# English to Arabic Translator Microservice

This is a microservice that translates English text to Arabic using a Groq-hosted AI model. Currently, the Llama 80B model is being used for its performance, though the final model may vary. The service is designed to be deployed in a Docker container for easy integration into larger microservices architectures.
Features: 

- Text Translation: Translates English text to Arabic using the Groq-hosted AI model.
- Drop in Ollama Replacement: Use Ollama instead for Groq for an open-source, locally hosted model (WIP)
- Dockerized: Easily deployable using Docker. (WIP
- Scalable: Suitable for use in a microservices architecture, supporting Kafka or REST API for communication. (WIP)
- Model: Currently using Llama 80B for high-performance translation. (WIP)
---
### Architecture

The service exposes an API endpoint for translating English to Arabic via HTTP POST requests. It also supports Kafka message consumption and production, making it suitable for event-driven architectures.
- Input: English text.
- Output: Translated Arabic text.
- Model: Groq-hosted model (currently Llama 80B).
---
### Requirements
Read requirements.txt file

---
### Setup
Coming Soon

---
### License 
This project is licensed under the MIT License - see the LICENSE file for details.
