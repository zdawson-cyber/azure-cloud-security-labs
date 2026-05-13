# Lab 02: Azure RBAC Least Privilege Review

## Objective

Review Azure role-based access control assignments and document least privilege recommendations for a cloud security environment.

## Why This Lab Matters

Identity and access management is one of the most important parts of cloud security. Misconfigured permissions can allow users, groups, or applications to access more resources than needed.

This lab demonstrates how Azure RBAC is used to manage access to Azure resources and how least privilege principles can be applied to reduce security risk.

## Azure Services Used

- Microsoft Azure Portal
- Microsoft Entra ID
- Azure Role-Based Access Control
- Azure Resource Groups
- Access Control (IAM)

## Security Concepts Demonstrated

- Least privilege access
- Role-based access control
- Scope-based permissions
- Identity and access review
- Separation of duties
- Privileged access risk
- Cloud security documentation

## Key Azure RBAC Concepts

Azure RBAC controls access using three main parts:

| Concept | Meaning |
|---|---|
| Security principal | The user, group, service principal, or managed identity receiving access |
| Role definition | The permissions being granted |
| Scope | Where the permissions apply, such as subscription, resource group, or resource |

## Common Azure Built-In Roles

| Role | Access Level | Security Risk |
|---|---|---|
| Owner | Full access, including permission to assign roles | High |
| Contributor | Can create and manage resources but cannot assign roles | Medium/High |
| Reader | Can view resources but cannot make changes | Low |
| User Access Administrator | Can manage user access to Azure resources | High |

## Least Privilege Review Questions

During this lab, review the following:

- Who has access to the subscription?
- Who has access to the resource group?
- Are any users assigned Owner unnecessarily?
- Are permissions assigned at the broadest scope?
- Can Reader access be used instead of Contributor?
- Are any permissions assigned directly to users instead of groups?
- Are high-privilege roles documented?
- Are role assignments aligned to job responsibilities?

## Lab Steps

### Phase 1: Azure Portal Review

- [ ] Sign in to Azure Portal
- [ ] Open the Azure subscription
- [ ] Review Access Control (IAM)
- [ ] Review role assignments
- [ ] Identify high-privilege roles
- [ ] Review access at the resource group level

### Phase 2: Least Privilege Analysis

- [ ] Identify any Owner assignments
- [ ] Identify any Contributor assignments
- [ ] Determine if Reader would be more appropriate
- [ ] Document unnecessary broad access
- [ ] Document recommended remediation

### Phase 3: Evidence Collection

- [ ] Screenshot subscription IAM page
- [ ] Screenshot resource group IAM page
- [ ] Screenshot role assignments view
- [ ] Screenshot role details with sensitive information hidden
- [ ] Add screenshots to the screenshots folder

### Phase 4: Documentation

- [ ] Complete role review table
- [ ] Add lessons learned
- [ ] Add portfolio summary
- [ ] Commit changes to GitHub

## Role Review Table

| Scope | Principal Type | Role Assigned | Risk Level | Recommended Action |
|---|---|---|---|---|
| Subscription | User | Owner | High | Limit Owner role and use least privilege |
| Resource Group | User | Contributor | Medium/High | Use Reader if only view access is needed |
| Resource Group | User | Reader | Low | Appropriate for view-only access |

## Screenshots to Add

Screenshots will be added after completing the Azure portal review.

Planned screenshots:

```text
screenshots/subscription-iam-overview.png
screenshots/resource-group-iam-overview.png
screenshots/role-assignments.png
screenshots/access-check.png
```

## Security Notes

Do not expose sensitive information in screenshots.

Before uploading screenshots to GitHub, hide or blur:

- Email addresses
- Subscription IDs
- Tenant IDs
- Object IDs
- Personal account details

## Lessons Learned

This section will be updated after the lab is completed.

Planned reflection points:

- What I learned about Azure RBAC
- Why least privilege matters in cloud security
- Why Owner access should be limited
- How role scope affects security risk
- How access reviews support audit readiness
- How RBAC connects to GRC and compliance work

## Portfolio Summary

This lab demonstrates Azure identity and access management knowledge by reviewing RBAC role assignments, identifying high-risk permissions, and documenting least privilege recommendations for cloud security governance.
