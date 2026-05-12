# Lab 01: Azure App Service Secure Deployment

## Objective

Deploy a Python FastAPI application to Microsoft Azure App Service and document the deployment as a cloud security portfolio lab.

## Why This Lab Matters

This lab turns a local Python project into a real Azure-hosted application. It demonstrates hands-on experience with Azure App Service, cloud deployment, GitHub project documentation, and secure configuration awareness.

## Azure Services Used

- Azure App Service
- Azure Resource Group
- App Service Plan
- GitHub
- GitHub Actions later
- Microsoft Entra ID later
- Managed Identity later

## Security Concepts Demonstrated

- Secure cloud application deployment
- Least privilege planning
- Avoiding hardcoded secrets
- HTTPS-only application access
- Deployment documentation
- Cloud resource organization
- Evidence collection through screenshots

## Planned Architecture

```text
GitHub Repository
        |
        v
Python FastAPI App
        |
        v
Azure App Service
        |
        v
Live Web App URL
```

## Lab Steps

### Phase 1: GitHub Setup

- [x] Create the `azure-cloud-security-labs` repository
- [x] Add main repository README
- [x] Create Lab 01 folder
- [x] Add starter Python FastAPI app
- [x] Add requirements file
- [x] Add Azure startup script

### Phase 2: Local Python App

- [ ] Create a simple FastAPI application
- [ ] Test the app locally
- [ ] Confirm `/docs` loads successfully
- [ ] Confirm `/health` endpoint works
- [ ] Confirm `/security-summary` endpoint works

### Phase 3: Azure Deployment

- [ ] Create Azure account
- [ ] Create Resource Group
- [ ] Create Azure App Service
- [ ] Deploy Python app
- [ ] Confirm live URL works
- [ ] Screenshot Azure App Service overview
- [ ] Screenshot live FastAPI docs page

### Phase 4: Security Review

- [ ] Confirm HTTPS-only setting
- [ ] Review App Service configuration
- [ ] Document identity and access considerations
- [ ] Document secrets handling approach
- [ ] Add lessons learned

## Local Testing Instructions

Before deploying to Azure, the app should be tested locally.

### 1. Open the Lab 01 folder

```bash
cd labs/01-azure-app-service-secure-deployment
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI app

```bash
uvicorn app.main:app --reload
```

### 5. Open the app in the browser

Main app:

```text
http://127.0.0.1:8000
```

FastAPI documentation page:

```text
http://127.0.0.1:8000/docs
```

Health check endpoint:

```text
http://127.0.0.1:8000/health
```

Security summary endpoint:

```text
http://127.0.0.1:8000/security-summary
```

## Expected Local Test Results

The `/health` endpoint should return:

```json
{
  "status": "healthy",
  "service": "FastAPI on Azure App Service"
}
```

The `/security-summary` endpoint should return a list of security concepts and Azure services used in this lab.

## Screenshots to Add

Screenshots will be added after Azure deployment.

Planned screenshots:

```text
screenshots/azure-resource-group.png
screenshots/app-service-overview.png
screenshots/fastapi-live-docs.png
screenshots/app-service-configuration.png
screenshots/github-repository.png
```

## Lessons Learned

This section will be updated after the lab is completed.

Planned reflection points:

- What I learned about deploying Python applications to Azure App Service
- How Azure App Service hosts and runs a FastAPI application
- What security settings should be reviewed before deployment
- Why HTTPS-only access matters for cloud-hosted applications
- Why secrets should not be hardcoded in application code
- How GitHub supports cloud project documentation and portfolio evidence
- What screenshots and proof are useful for demonstrating hands-on Azure experience

## Portfolio Summary

This lab demonstrates hands-on Azure cloud deployment by preparing a Python FastAPI application for Azure App Service. The lab documents local testing, planned Azure deployment steps, security considerations, and evidence collection for a cybersecurity cloud security portfolio.
