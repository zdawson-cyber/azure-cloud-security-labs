# Azure RBAC Role Review

## Review Date

May 2026

## Purpose

This document reviews Azure role assignments and identifies least privilege recommendations for the Azure cloud security lab environment.

## Reviewed Scope

| Scope Type | Scope Name | Reviewed |
|---|---|---|
| Subscription | Azure subscription | Yes |
| Resource Group | rg-azure-security-labs | Yes |

## Role Assignment Review

| Scope | Principal Type | Role Assigned | Risk Level | Notes | Recommended Action |
|---|---|---|---|---|---|
| Subscription | User | Owner | High | Owner has full control and can assign access to others. | Limit Owner access to only required administrators. |
| Resource Group | User | Contributor | Medium/High | Contributor can create and modify resources but cannot assign roles. | Use only when resource management is required. |
| Resource Group | User | Reader | Low | Reader can view resources but cannot make changes. | Appropriate for view-only access. |
| Resource Group | User | Owner | High | Owner access is inherited from the subscription scope. | Review whether Owner access is required at the subscription level and limit high-privilege access where possible. |

## Least Privilege Findings

### Finding 1: Owner access should be limited

Owner access is highly privileged because it allows full control over resources and access assignments.

**Recommendation:**  
Use Owner only when required. For most operational work, use Contributor or a more specific role.

### Finding 2: Assign access at the lowest necessary scope

Assigning permissions at the subscription level can expose more resources than necessary.

**Recommendation:**  
Assign roles at the resource group or individual resource level when possible.

### Finding 3: Use Reader for view-only access

Users who only need to review settings, logs, or configurations do not need Contributor access.

**Recommendation:**  
Use Reader for audit, review, or documentation tasks.

## Security Impact

Strong RBAC management helps reduce the risk of:

- Unauthorized changes
- Excessive privileges
- Accidental resource deletion
- Privilege escalation
- Poor separation of duties
- Audit and compliance gaps

## GRC / RMF Connection

Azure RBAC supports governance, risk management, and compliance by enforcing least privilege access and documenting who has access to cloud resources.

This type of review supports:

- Access control validation
- Audit readiness
- Identity governance
- Cloud security posture management
- Zero Trust alignment

## Summary

This review demonstrates how Azure RBAC can be used to evaluate user access, identify privileged roles, and recommend least privilege improvements in a cloud environment.
