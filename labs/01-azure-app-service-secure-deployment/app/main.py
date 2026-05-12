from fastapi import FastAPI

app = FastAPI(
    title="Azure Cloud Security Lab 01",
    description="A starter Python FastAPI app for Azure App Service secure deployment.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Azure Cloud Security Lab 01 is running.",
        "lab": "Azure App Service Secure Deployment",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "FastAPI on Azure App Service",
    }


@app.get("/security-summary")
def security_summary():
    return {
        "security_concepts": [
            "HTTPS-only access",
            "No hardcoded secrets",
            "Least privilege planning",
            "Secure cloud deployment",
            "Azure App Service hosting",
        ],
        "azure_services": [
            "Azure App Service",
            "Azure Resource Group",
            "App Service Plan",
        ],
        "portfolio_value": "Demonstrates a Python application prepared for secure Azure deployment.",
    }
