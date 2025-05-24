# Open Web Application Security Project

1. Broken Access Control

🔴 Issue: Users can access unauthorized data or perform actions beyond their permissions.
✅ Example:

    A normal user can access an admin panel by navigating to /admin directly.
    An API allows a user to modify another user's data by changing the user_id in a request.

🔧 Fix: Implement role-based access control (RBAC) and validate permissions at the server level.
2. Cryptographic Failures (formerly "Sensitive Data Exposure")

🔴 Issue: Poor encryption or unencrypted data leads to sensitive information leaks.
✅ Example:

    Storing passwords in plain text instead of hashing them.
    Using HTTP instead of HTTPS, exposing sensitive data during transmission.

🔧 Fix: Use strong encryption algorithms (e.g., AES-256, bcrypt) and enforce HTTPS.
3. Injection (SQL, NoSQL, OS, LDAP, etc.)

🔴 Issue: Untrusted input is executed as a command or query.
✅ Example:

    SQL Injection:

    SELECT * FROM users WHERE username = 'admin' OR '1'='1';

    This returns all users, allowing attackers to bypass authentication.

🔧 Fix: Use prepared statements and ORMs to prevent injections.
4. Insecure Design

🔴 Issue: Poor security considerations in application architecture.
✅ Example:

    A banking app doesn't enforce transaction limits, allowing unlimited withdrawals.
    A social media site lacks protection against Cross-Site Request Forgery (CSRF) attacks.

🔧 Fix: Implement threat modeling, security reviews, and secure coding practices.
5. Security Misconfiguration

🔴 Issue: Default settings or unnecessary features expose vulnerabilities.
✅ Example:

    Default credentials (admin/admin) left unchanged.
    Debug mode enabled in production, exposing sensitive logs.

🔧 Fix: Harden configurations, disable unused features, and follow the principle of least privilege.
6. Vulnerable and Outdated Components

🔴 Issue: Using old versions of frameworks, libraries, or plugins.
✅ Example:

    Running an outdated version of Apache Struts with known vulnerabilities.
    Using an old jQuery version vulnerable to XSS attacks.

🔧 Fix: Regularly update dependencies and monitor for security advisories.
7. Identification and Authentication Failures

🔴 Issue: Weak authentication methods allow attackers to impersonate users.
✅ Example:

    Weak passwords like "password123" allowed.
    No rate limiting on login attempts, enabling brute-force attacks.

🔧 Fix: Use multi-factor authentication (MFA) and strong password policies.
8. Software and Data Integrity Failures

🔴 Issue: Unverified updates or malicious modifications to software/data.
✅ Example:

    A web app loads JavaScript from an untrusted CDN that gets compromised.
    An update mechanism lacks integrity checks, allowing supply chain attacks.

🔧 Fix: Use code signing, integrity checks, and only trusted update sources.
9. Security Logging and Monitoring Failures

🔴 Issue: Lack of proper logging and monitoring leads to undetected attacks.
✅ Example:

    No logs for failed login attempts, making brute-force attacks invisible.
    No alerts when an admin account logs in from an unusual location.

🔧 Fix: Implement centralized logging, alerting, and real-time monitoring.
10. Server-Side Request Forgery (SSRF)

🔴 Issue: An attacker tricks a server into making requests on their behalf.
✅ Example:

    A web application allows users to fetch a URL but doesn’t validate it:

    curl http://internal-company.com/admin

    This lets an attacker access internal resources.

🔧 Fix: Restrict outbound requests, validate URLs, and block internal IP addresses.
Final Thoughts

    Understand the risks in the OWASP Top 10.
    Use security best practices (input validation, encryption, RBAC, logging).
    Regularly scan and test your applications for vulnerabilities.

Would you like more details on any specific issue? 🚀