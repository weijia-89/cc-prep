# ISC2 CC Glossary, defined on first use

Every initialism and field-specific term in the study guide, alphabetized. Per palamedes rule, each is also defined inline on first use in `CC_Study_Guide.md`. This file is the consolidated reference.

## A

- **AAA (Authentication, Authorization, Accounting):** the three pillars of access control. Sometimes IAAA when Identification is broken out.
- **AAL (Authenticator Assurance Level):** NIST SP 800-63B scale: AAL1 single-factor, AAL2 multi-factor, AAL3 hardware-cryptographic.
- **ABAC (Attribute-Based Access Control):** access decisions based on attributes of user, resource, and environment.
- **ACL (Access Control List):** ordered list of allow/deny rules tied to a resource.
- **AES (Advanced Encryption Standard):** symmetric block cipher, 128/192/256-bit keys. Industry standard.
- **AH (Authentication Header):** IPsec protocol providing authentication and integrity without encryption.
- **ALE (Annualized Loss Expectancy):** SLE × ARO. Expected loss per year from a given risk.
- **AP (Access Point):** WiFi base station.
- **ARO (Annualized Rate of Occurrence):** how often a risk event happens per year.
- **ARP (Address Resolution Protocol):** maps IP addresses to MAC addresses at OSI Layer 2.
- **AUP (Acceptable Use Policy):** rules for how users may use organization systems.

## B

- **BCP (Business Continuity Plan):** how the business keeps operating during a disruption.
- **BIA (Business Impact Analysis):** foundation document identifying mission-essential functions and recovery priorities.
- **BYOD (Bring Your Own Device):** policy allowing personal devices to access corporate resources.

## C

- **C2 (Command and Control):** the channel a botnet uses to receive instructions from its operator.
- **CA (Certificate Authority):** issues and signs X.509 certificates in a PKI.
- **CASB (Cloud Access Security Broker):** policy enforcement point between users and cloud apps.
- **CBC (Cipher Block Chaining):** symmetric encryption mode where each block XORs with the previous ciphertext.
- **CCPA (California Consumer Privacy Act):** California state privacy law.
- **CCTV (Closed-Circuit Television):** surveillance camera system.
- **CER (Crossover Error Rate):** point where FRR equals FAR in a biometric. Lower is better.
- **CIA triad:** Confidentiality, Integrity, Availability. The three foundational security properties.
- **CIS (Center for Internet Security):** publisher of the CIS Controls and CIS Benchmarks.
- **CRL (Certificate Revocation List):** signed list of certificates a CA has revoked.
- **CSF (Cybersecurity Framework):** NIST framework. CSF 2.0 has six Functions: Govern, Identify, Protect, Detect, Respond, Recover.
- **CTR (Counter mode):** symmetric encryption mode treating the cipher as a keystream generator.
- **CVE (Common Vulnerabilities and Exposures):** unique identifier for each publicly known vulnerability.
- **CVSS (Common Vulnerability Scoring System):** 0-10 severity score for a vulnerability.

## D

- **DAC (Discretionary Access Control):** the data owner decides who gets access.
- **DDoS (Distributed Denial of Service):** denial of service attack from many compromised hosts.
- **DES (Data Encryption Standard):** legacy symmetric cipher, broken, not for use.
- **DH (Diffie-Hellman):** key exchange protocol, not encryption.
- **DHCP (Dynamic Host Configuration Protocol):** assigns IP addresses to hosts on a network.
- **DISA STIG (Defense Information Systems Agency Security Technical Implementation Guide):** US government hardening guidelines.
- **DLP (Data Loss Prevention):** technology that detects and blocks sensitive data leaving the org.
- **DMZ (Demilitarized Zone):** subnet between the internet and the internal network, hosting public-facing services.
- **DNS (Domain Name System):** translates hostnames to IP addresses. Port 53.
- **DoS (Denial of Service):** attack that makes a system unavailable to legitimate users.
- **DRP (Disaster Recovery Plan):** how IT systems are restored after a disaster. Subset of BCP.
- **DSA (Digital Signature Algorithm):** asymmetric algorithm for signatures.

## E

- **ECB (Electronic Code Book):** symmetric encryption mode, insecure for multi-block plaintexts.
- **ECC (Elliptic Curve Cryptography):** asymmetric crypto with smaller keys than RSA for equivalent strength.
- **EDR (Endpoint Detection and Response):** modern endpoint security with behavioral analytics.
- **ESP (Encapsulating Security Payload):** IPsec protocol providing encryption plus authentication.

## F

- **FaaS (Function as a Service):** cloud model where the provider runs ephemeral functions on demand.
- **FAR (False Acceptance Rate):** biometric error: impostor accepted as legitimate user. Type 2 error.
- **FIDO2 (Fast Identity Online v2):** standard for hardware-key passwordless authentication.
- **FRR (False Rejection Rate):** biometric error: legitimate user denied. Type 1 error.
- **FTP (File Transfer Protocol):** ports 20 and 21. Cleartext; use SFTP or FTPS instead.

## G

- **GCM (Galois/Counter Mode):** authenticated encryption mode. Confidentiality plus integrity in one pass.
- **GDPR (General Data Protection Regulation):** EU privacy regulation.

## H

- **HIDS (Host-based Intrusion Detection System):** IDS that runs on individual hosts.
- **HIPAA (Health Insurance Portability and Accountability Act):** US healthcare privacy and security law.
- **HMAC (Hash-based Message Authentication Code):** integrity plus authenticity, hash combined with secret key.
- **HTTP (Hypertext Transfer Protocol):** port 80. Cleartext.
- **HTTPS (HTTP Secure):** HTTP over TLS. Port 443.
- **HVAC (Heating, Ventilation, Air Conditioning):** data center environmental control.

## I

- **IaaS (Infrastructure as a Service):** cloud model providing virtual machines, storage, networking.
- **IAM (Identity and Access Management):** the discipline of managing identities and their access rights.
- **ICMP (Internet Control Message Protocol):** network diagnostics. `ping` uses ICMP.
- **IDS (Intrusion Detection System):** monitors for malicious activity; alerts but does not block.
- **IGMP (Internet Group Management Protocol):** multicast group management at OSI Layer 3.
- **IKE (Internet Key Exchange):** IPsec key negotiation protocol.
- **IMAP (Internet Message Access Protocol):** email retrieval. Port 143; IMAPS port 993.
- **IoT (Internet of Things):** networked embedded devices (cameras, thermostats, sensors).
- **IP (Internet Protocol):** OSI Layer 3 addressing and routing.
- **IPS (Intrusion Prevention System):** IDS that also blocks. Inline.
- **IPsec (Internet Protocol Security):** Layer 3 encryption and authentication suite. Transport and tunnel modes.
- **IRP (Incident Response Plan):** how the org responds to a security incident.

## K

- **Kerberos:** intranet authentication protocol using a Key Distribution Center.

## L

- **LATCH:** unrelated to CC (car seat term). Not on the exam.
- **LDAP (Lightweight Directory Access Protocol):** directory service for users and resources. Port 389; LDAPS port 636.

## M

- **MAC (Mandatory Access Control):** system enforces access based on labels (Top Secret, Secret, etc.). Distinct from Media Access Control.
- **MAC address (Media Access Control address):** OSI Layer 2 hardware identifier. Distinct from Mandatory Access Control.
- **MD5 (Message Digest 5):** legacy hash, broken, do not use.
- **MDM (Mobile Device Management):** central control of mobile devices accessing corporate resources.
- **MFA (Multi-Factor Authentication):** two or more factors from different categories.
- **MITM (Man in the Middle):** attacker intercepts and may modify traffic between two parties.
- **MOA (Memorandum of Agreement):** formal but non-binding inter-organizational agreement.
- **MOU (Memorandum of Understanding):** similar to MOA, less specific.
- **MSP (Managed Service Provider):** third party managing IT services.
- **MSSP (Managed Security Service Provider):** MSP focused on security.
- **MTD (Maximum Tolerable Downtime):** absolute outer downtime limit before the business fails.

## N

- **NAC (Network Access Control):** verifies device posture before granting network access.
- **NAT (Network Address Translation):** rewrites IP addresses on packets; allows many private addresses to share one public address.
- **NetBIOS (Network Basic Input/Output System):** Windows networking, ports 137-139.
- **NGFW (Next-Generation Firewall):** stateful firewall plus app awareness, IPS, threat intel, identity.
- **NIDS (Network-based Intrusion Detection System):** IDS that watches network traffic.
- **NIST (National Institute of Standards and Technology):** US federal agency publishing security standards.
- **Non-repudiation:** a party cannot later deny having performed an action.
- **NTP (Network Time Protocol):** time synchronization. Port 123.

## O

- **OCSP (Online Certificate Status Protocol):** real-time certificate revocation check.
- **OIDC (OpenID Connect):** identity layer on top of OAuth 2.0.
- **OSI (Open Systems Interconnection):** 7-layer networking reference model.
- **OWASP (Open Worldwide Application Security Project):** publisher of the Top 10 web app risks and other security guides.

## P

- **PaaS (Platform as a Service):** cloud model providing runtime, OS, and infrastructure.
- **PDU (Power Distribution Unit):** rack-level power distribution.
- **PII (Personally Identifiable Information):** information that can identify an individual.
- **PKI (Public Key Infrastructure):** system to manage public keys via CAs and certificates.
- **POP3 (Post Office Protocol v3):** legacy email retrieval. Port 110; POP3S port 995.
- **PPTP (Point-to-Point Tunneling Protocol):** legacy VPN protocol, broken, do not use.

## R

- **RA (Registration Authority):** verifies identity before a CA issues a certificate.
- **RADIUS (Remote Authentication Dial-In User Service):** centralized AAA protocol, common for VPN and WiFi.
- **RAID (Redundant Array of Inexpensive Disks):** storage redundancy. RAID 1 mirror, RAID 5 striped with parity, RAID 6 striped with double parity, RAID 10 mirror plus stripe.
- **RBAC (Role-Based Access Control):** access tied to job role.
- **RDP (Remote Desktop Protocol):** Microsoft remote desktop. Port 3389.
- **RFID (Radio-Frequency Identification):** wireless tag technology used in badges.
- **RPO (Recovery Point Objective):** how much data loss is tolerable.
- **RSA (Rivest-Shamir-Adleman):** asymmetric cipher based on factoring large primes.
- **RTO (Recovery Time Objective):** how long downtime is tolerable before systems must be back.

## S

- **SaaS (Software as a Service):** cloud model where the provider runs the application.
- **SAML (Security Assertion Markup Language):** XML-based federated SSO standard.
- **SCA (Software Composition Analysis):** scanning for vulnerable third-party components.
- **SDN (Software-Defined Networking):** programmable network configuration.
- **SFTP (SSH File Transfer Protocol):** secure file transfer over SSH. Port 22.
- **SHA (Secure Hash Algorithm):** family of hash functions. SHA-256, SHA-384, SHA-512 are current.
- **SIEM (Security Information and Event Management):** log aggregation and correlation platform.
- **SLA (Service Level Agreement):** contractual service commitments.
- **SLE (Single Loss Expectancy):** expected loss from one occurrence of a risk.
- **SMB (Server Message Block):** Windows file sharing. Port 445.
- **SMTP (Simple Mail Transfer Protocol):** email sending. Port 25; SMTPS ports 465 and 587.
- **SNMP (Simple Network Management Protocol):** device monitoring. Ports 161 and 162.
- **SoC (System on a Chip):** integrated circuit combining CPU, memory, and peripherals.
- **SOC (Security Operations Center):** team that runs the SIEM and triages alerts. Distinct from SoC.
- **SOAR (Security Orchestration, Automation, and Response):** automation layer on top of SIEM.
- **SoD (Separation of Duties):** no single person can complete a sensitive transaction alone.
- **SOX (Sarbanes-Oxley Act):** US financial-reporting regulation.
- **SP (Special Publication):** NIST document series, e.g. SP 800-53.
- **SQL (Structured Query Language):** database query language; injection (SQLi) is OWASP A03.
- **SSH (Secure Shell):** encrypted remote shell. Port 22.
- **SSL (Secure Sockets Layer):** legacy name for what is now TLS. Deprecated.
- **SSO (Single Sign-On):** one login grants access to multiple applications.

## T

- **TCP (Transmission Control Protocol):** connection-oriented Layer 4 protocol with three-way handshake.
- **TEE (Trusted Execution Environment):** hardware-isolated environment for sensitive computation.
- **TFTP (Trivial File Transfer Protocol):** UDP-based file transfer with no auth. Port 69.
- **TLS (Transport Layer Security):** current encryption layer for HTTP, SMTP, etc.

## U

- **UDP (User Datagram Protocol):** connectionless Layer 4 protocol. Faster, less reliable than TCP.
- **UPS (Uninterruptible Power Supply):** battery backup for short outages.
- **UTM (Unified Threat Management):** firewall combining many security functions for SMBs.

## V

- **VLAN (Virtual Local Area Network):** Layer 2 logical segmentation of switch ports.
- **VoIP (Voice over IP):** voice telephony over IP networks.
- **VPN (Virtual Private Network):** encrypted tunnel across an untrusted network.

## W

- **WAF (Web Application Firewall):** application-layer firewall for HTTP/HTTPS.
- **WAP (Wireless Access Point):** WiFi base station; also see AP.
- **WebAuthn (Web Authentication):** browser API for FIDO2 hardware-key authentication.
- **WEP (Wired Equivalent Privacy):** broken WiFi encryption. Do not use.
- **WPA / WPA2 / WPA3 (WiFi Protected Access):** successive WiFi security protocols. WPA3 is current.
- **WRT (Work Recovery Time):** post-RTO time to verify and load data before resuming work.

## X

- **XSS (Cross-Site Scripting):** OWASP injection class where attacker scripts execute in victim's browser.
- **XaaS (Anything as a Service):** umbrella for cloud service models.

## Z

- **Zero-day:** vulnerability not yet patched. Attacker has the exploit before the vendor has a fix.
- **Zero trust:** "never trust, always verify." NIST SP 800-207.

End of glossary.
