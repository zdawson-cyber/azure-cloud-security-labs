# Lab 02 Lessons Learned

## What I Learned

In this lab, I reviewed Azure role-based access control and documented how least privilege applies to cloud environments.

I learned that Azure RBAC is based on three key parts:

- Security principal
- Role assignment
- Scope

The scope of a role assignment matters because permissions assigned at the subscription level can affect more resources than permissions assigned at the resource group or resource level.

## Key Takeaways

- Owner access should be limited because it allows full control, including the ability to assign access to others.
- Contributor access should only be used when a user needs to create, modify, or manage resources.
- Reader access is better for users who only need to review configurations or collect evidence.
- Role assignments should be reviewed regularly to reduce excessive permissions.
- Least privilege supports Zero Trust, GRC, audit readiness, and cloud security governance.

## Security Impact

Improper RBAC assignments can increase the risk of unauthorized changes, accidental deletion, privilege escalation, and poor separation of duties.

Reviewing Azure RBAC helps ensure users only have the access required for their responsibilities.

## Portfolio Reflection

This lab helped me connect Azure identity and access management to real-world cybersecurity work. It also showed how RBAC reviews can support cloud security, GRC, RMF, and compliance efforts.
