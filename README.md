# CyberSecurity-Quiz

## Project Setup

This project uses Streamlit and Google Generative AI. Follow the steps below to set up the environment, install dependencies, and run the application.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/djmahe4/CyberSecurity-Quiz
    cd CyberSecurity-Quiz
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. **Set up the Google Generative AI API key:**

    - Go to https://ai.google.dev to get the API key.
    - Add your API key to the `.env` file:

    ```env
    GENERATIVE_AI_KEY='your_api_key_here'
    ```

### Running the Application

1. **Run the `main.py` script:**

    ```sh
    streamlit run main.py
    ```
2. **Go to http://localhost:8501 to view and interact with the app**

### Notes

- Ensure that your `.env` file is not included in version control to keep your API key secure.
- For more information on obtaining a Google Generative AI API key, refer to the [Google AI documentation](https://ai.google.dev/gemini-api/docs/api-key).

  ## Topics covered
    ### Blockchain Security
    "Smart Contract Vulnerabilities",
    "Blockchain Data Encryption",
    "Cryptographic Hash Functions",
    "Digital Signature Algorithms",
    "Blockchain Network Consensus Mechanisms",
    "Blockchain Scalability and Performance",
    "Blockchain Regulatory Compliance",
    "Blockchain Identity Management",
    "Blockchain Access Control",
    "Blockchain Data Integrity",

    ### IoT Security
    "IoT Device Authentication",
    "IoT Network Security Protocols",
    "IoT Data Encryption Methods",
    "IoT Device Vulnerability Management",
    "IoT Secure Communication Protocols",
    "IoT Data Analytics Security",
    "IoT Cloud Security",
    "IoT Endpoint Security",
    "IoT Firmware Security",
    "IoT Secure Boot Mechanisms",

    ### Cryptography
    "Public-Key Cryptography",
    "Symmetric-Key Cryptography",
    "Hash Functions",
    "Digital Signatures",
    "Key Exchange Algorithms",
    "Elliptic Curve Cryptography",
    "Quantum Cryptography",
    "Homomorphic Encryption",
    "Zero-Knowledge Proofs",
    "Secure Multi-Party Computation",

    ### Network Security
    "Firewall Configuration",
    "Intrusion Detection Systems",
    "Virtual Private Networks (VPNs)",
    "Network Segmentation",
    "Wireless Network Security",
    "Network Access Control",
    "Secure Sockets Layer/Transport Layer Security (SSL/TLS)",
    "Secure Shell (SSH) Protocol",
    "Network Monitoring and Analysis",
    "Denial-of-Service (DoS) Attack Prevention",
    ### Threat Intelligence
    "Threat Modeling",
    "Vulnerability Assessment",
    "Penetration Testing",
    "Incident Response",
    "Malware Analysis",
    "Phishing Attack Prevention",
    "Social Engineering Attack Prevention",
    "Advanced Persistent Threats (APTs)",
    "Insider Threats",
    "Cyber Threat Intelligence Sharing",

    ### Cloud Security
    "Cloud Access Security Broker (CASB)",
    "Cloud Security Gateways",
    "Cloud Encryption",
    "Cloud Identity and Access Management",
    "Cloud Compliance and Governance",
    "Cloud Network Security",
    "Cloud Storage Security",
    "Cloud Computing Security Standards",
    "Cloud Security Architecture",
    "Cloud Security Monitoring",

    ### Artificial Intelligence and Machine Learning Security
    "AI/ML Model Security",
    "AI/ML Data Security",
    "AI/ML Explainability",
    "AI/ML Transparency",
    "AI/ML Bias and Fairness",
    "AI/ML Robustness",
    "AI/ML Adversarial Attacks",
    "AI/ML Security Analytics",
    "AI/ML Incident Response",
    "AI/ML Security Standards"
