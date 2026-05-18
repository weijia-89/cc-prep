# ISC2 CC Practice Exams - Mocks 3 and 4

Two more 100-question mocks. These are weighted toward Wei's weak domains (Domain 4 Network Security at 55% prelim, Domain 2 BC/DR/IR at 60% prelim). Distribution: D1 10, D2 25, D3 15, D4 35, D5 15.

**How to use:** 2 hours per mock. Score yourself with the key at the end. These mocks are harder by intent (more Domain 4 depth questions). 65+ here is roughly equivalent to 70+ on Mocks 1-2.

---

## Mock 3 (100 questions, weighted toward weak domains)

### Domain 1: Security Principles (Q1-10) - light review

**1.** A non-repudiation control prevents:
A. Unauthorized access
B. A party from denying they performed an action
C. Data leakage
D. Network attacks

**2.** Which property is most directly compromised by an unauthorized data modification?
A. Confidentiality
B. Integrity
C. Availability
D. Privacy

**3.** Adding a UPS (Uninterruptible Power Supply) addresses:
A. Confidentiality
B. Integrity
C. Availability
D. Authentication

**4.** Risk transfer is best illustrated by:
A. Deploying MFA
B. Buying cyber insurance
C. Eliminating the risky activity
D. Documenting an accepted risk

**5.** Which is most directly an administrative control?
A. Encryption
B. Locked server room
C. Mandatory security training
D. Antivirus software

**6.** The ISC2 Code of Ethics canon order is:
A. Provide service, Protect society, Act honorably, Advance the profession
B. Protect society, Act honorably, Provide service, Advance the profession
C. Act honorably, Protect society, Advance the profession, Provide service
D. Advance the profession, Provide service, Act honorably, Protect society

**7.** Which factor describes facial recognition?
A. Something you know
B. Something you have
C. Something you are
D. Something you do

**8.** A control whose primary purpose is to alert on a security event is:
A. Preventive
B. Detective
C. Corrective
D. Compensating

**9.** Quantitative risk analysis uses:
A. High/Medium/Low ratings
B. SLE, ARO, ALE calculations
C. Color-coded risk matrices
D. Subjective expert opinion only

**10.** A baseline configuration is:
A. The recommended optional setup
B. The minimum acceptable configuration for a system
C. An external regulation
D. A peer-reviewed standard

### Domain 2: BC, DR, IR (Q11-35) - HEAVY weight

**11.** A Business Impact Analysis primarily identifies:
A. All known vulnerabilities
B. Mission-essential functions and their recovery priorities
C. Network segments to firewall
D. Acceptable Use Policy violations

**12.** RPO of 4 hours means:
A. The system must be back up within 4 hours
B. Backups must capture changes at intervals no longer than 4 hours
C. The work recovery time is 4 hours
D. Maximum downtime is 4 hours

**13.** RTO is independent of:
A. Disaster severity
B. Cost
C. RPO (they measure different things)
D. Business criticality

**14.** Which recovery objective addresses tolerable data loss?
A. RTO
B. RPO
C. MTD
D. WRT

**15.** Which is true about a cold site?
A. Fast to activate, expensive
B. Slow to activate (weeks), cheapest
C. Pre-loaded with current data
D. Identical to a hot site

**16.** A "structured walk-through" of a BCP is:
A. A checklist review
B. A tabletop exercise
C. A full cutover
D. A parallel test

**17.** Per NIST SP 800-61 r2, the IR phase 3 includes:
A. Preparation and Detection
B. Containment, Eradication, and Recovery
C. Lessons Learned only
D. Detection and Analysis only

**18.** A signal that an attack might occur but has not happened is a:
A. Indicator
B. Precursor
C. False positive
D. Containment trigger

**19.** A signal that an attack has occurred or is in progress is a:
A. Indicator
B. Precursor
C. False positive
D. Tabletop

**20.** Lessons learned, evidence retention, and playbook updates happen in:
A. Preparation
B. Detection and Analysis
C. Containment, Eradication, Recovery
D. Post-Incident Activity

**21.** Chain of custody documentation typically includes:
A. Who collected, when, how, where stored, who accessed
B. The attacker's identity
C. The CVSS score of the exploited vuln
D. The patch level of the system

**22.** Order of volatility says to collect FIRST:
A. Disk image
B. Network captures
C. RAM and CPU caches
D. Archived backups

**23.** A coordinating IR team:
A. Responds directly to all incidents
B. Advises distributed responders without direct response
C. Replaces the SOC
D. Is the same as an outsourced model

**24.** Which IR staffing model uses an MSSP for full incident handling?
A. Employees only
B. Partially outsourced (in-house plus retainer)
C. Fully outsourced
D. Central team only

**25.** WRT (Work Recovery Time) is the time:
A. Before RTO
B. After RTO to verify data and resume work
C. Equivalent to RPO
D. The same as MTD

**26.** A hot site is preferred when:
A. RTO is hours and budget is large
B. RTO is weeks
C. The system is non-critical
D. The org has no DR program

**27.** A reciprocal agreement means:
A. Buying insurance
B. Two organizations agree to host each other in a disaster
C. A formal contract with a recovery vendor
D. A government-mandated arrangement

**28.** Which is the LOWEST-rigor BCP test?
A. Checklist
B. Tabletop
C. Simulation
D. Parallel

**29.** Full interruption (cutover) testing is:
A. The cheapest test
B. The most realistic and the highest risk
C. Not actually a test
D. Required quarterly

**30.** During eradication, the response team:
A. Removes the threat from systems (malware cleanup, account disabling)
B. Restores systems from backup
C. Conducts the post-mortem
D. Notifies law enforcement

**31.** Incident prioritization typically considers:
A. Time since last patch
B. Functional impact, information impact, recoverability
C. Number of users in the org
D. The day of the week

**32.** A "kill chain" model in IR refers to:
A. The sequence of attacker steps from recon to action
B. The sequence of firewall rules
C. The OSI model
D. The NIST CSF

**33.** NIST SP 800-61 r3 (April 2025) reorganizes IR around:
A. The OSI model
B. CSF 2.0's six Functions
C. ISO 27001 controls
D. The OWASP Top 10

**34.** Which event is BEST classified as an incident (not just an event)?
A. A user enters a wrong password
B. A confirmed unauthorized data exfiltration
C. A scheduled patch reboot
D. A backup job completion

**35.** Containment short-term vs long-term:
A. Short-term = isolate now; long-term = rebuild systems
B. Short-term = first 24h; long-term = after
C. Are the same
D. Both apply only after eradication

### Domain 3: Access Control Concepts (Q36-50)

**36.** A user receives the role "Marketing Analyst" and inherits access to marketing tools. This is:
A. DAC
B. MAC
C. RBAC
D. ABAC

**37.** Mandatory Access Control enforces:
A. Owner discretion
B. System-enforced security labels regardless of owner
C. Role memberships
D. Attribute-based rules

**38.** A FIDO2 hardware key is:
A. Something you know
B. Something you have, providing AAL3-capable authentication
C. Something you are
D. A type of password

**39.** A physical badge that opens specific doors based on assigned permissions implements:
A. Physical RBAC
B. MAC
C. ABAC
D. DAC

**40.** Two passwords from the same factor category are:
A. Multi-factor authentication
B. Multi-step but single-factor authentication
C. Stronger than MFA
D. Required for AAL2

**41.** A Type 2 biometric error is:
A. False rejection (legitimate user denied)
B. False acceptance (impostor accepted)
C. Crossover error
D. Enrollment error

**42.** The Crossover Error Rate (CER) is:
A. Where FAR and FRR are equal
B. The maximum FAR allowed
C. The minimum FRR allowed
D. The same as Type 1 error

**43.** Privileged Access Management (PAM) typically includes:
A. Session recording, just-in-time access, password vaulting for elevated accounts
B. End-user password resets only
C. Network packet inspection
D. WiFi management

**44.** Separation of duties is most directly intended to prevent:
A. Phishing
B. Single-insider fraud
C. Network attacks
D. Tailgating

**45.** Kerberos is primarily used for:
A. Intranet authentication using a Key Distribution Center
B. Internet authentication via federated tokens
C. Encryption of data at rest
D. Disk hashing

**46.** OAuth 2.0 provides:
A. Authentication only
B. Authorization delegation (often paired with OIDC for authentication)
C. Encryption
D. Network access control

**47.** A "need-to-know" principle:
A. Replaces RBAC
B. Adds a job-reason requirement on top of clearance
C. Is the same as least privilege
D. Applies only to physical access

**48.** Account lifecycle management starts with:
A. Onboarding/provisioning
B. Termination
C. Authentication
D. Logging

**49.** When an employee changes roles, access:
A. Remains the same automatically
B. Should be reviewed and adjusted to the new role's needs only
C. Doubles
D. Is deleted

**50.** A clean-desk policy is part of:
A. Physical access control awareness
B. Network security
C. Encryption standards
D. Patch management

### Domain 4: Network Security (Q51-85) - HEAVIEST weight

**51.** OSI Layer 7 is:
A. Physical
B. Application
C. Network
D. Transport

**52.** TCP three-way handshake is:
A. ACK -> SYN -> ACK
B. SYN -> SYN/ACK -> ACK
C. SYN -> ACK -> FIN
D. SYN -> ACK -> SYN

**53.** UDP is preferred over TCP for:
A. File transfer requiring guaranteed delivery
B. Real-time audio and video where latency matters more than reliability
C. Database transactions
D. SSH sessions

**54.** A stateless packet filter examines:
A. The application payload
B. Individual packet headers in isolation
C. Connection state from a state table
D. User identity

**55.** A stateful firewall tracks:
A. Application-layer commands
B. Connection state across packets in a state table
C. User group memberships
D. Vulnerability scan results

**56.** An application-proxy firewall:
A. Allows direct connections through
B. Terminates the connection, then opens a separate connection to destination
C. Operates at Layer 2
D. Replaces the need for IDS

**57.** A WAF specifically protects against:
A. Network-layer DoS
B. Application-layer attacks like SQL injection and XSS
C. WiFi key cracking
D. Side-channel attacks

**58.** An NGFW typically combines:
A. Stateful inspection, application awareness, IPS, threat intel, user identity
B. Only stateful inspection
C. Only application-layer inspection
D. Only host-based protection

**59.** A DMZ is best placed:
A. Inside the most-protected internal network
B. Between the internet and the internal network as an intermediate zone
C. On the public internet directly
D. Inside a VPN tunnel

**60.** A VLAN segments traffic at:
A. Layer 1
B. Layer 2 (Data Link)
C. Layer 3 (Network)
D. Layer 7

**61.** Micro-segmentation is most associated with:
A. Legacy perimeter security
B. Zero-trust and cloud architectures
C. Public WiFi
D. Modem connections

**62.** Zero trust security says:
A. Trust the internal network by default
B. Never trust, always verify regardless of network location
C. Trust only encrypted traffic
D. Trust authenticated users for 24 hours

**63.** A host-based personal firewall:
A. Replaces network firewalls
B. Protects only the host it runs on
C. Cannot block any traffic
D. Operates at Layer 1

**64.** Default-deny ruleset means:
A. All traffic is denied unless explicitly allowed
B. All traffic is allowed unless explicitly denied
C. Inbound is allowed, outbound is denied
D. Outbound is allowed, inbound is denied

**65.** IPsec Tunnel Mode:
A. Encrypts only the payload, keeps original headers
B. Encrypts the entire original packet and adds new IP headers
C. Operates at OSI Layer 7
D. Is the same as TLS

**66.** IPsec Transport Mode:
A. Encrypts only the payload, original IP header remains
B. Encrypts the entire packet
C. Is used only for site-to-site VPNs
D. Adds an outer IP header

**67.** AH (Authentication Header) provides:
A. Encryption only
B. Authentication and integrity, no encryption
C. Key exchange
D. Compression

**68.** ESP (Encapsulating Security Payload) provides:
A. Authentication only
B. Encryption and authentication
C. Compression only
D. Routing

**69.** IKE (Internet Key Exchange) is used to:
A. Encrypt data
B. Negotiate keys for IPsec
C. Hash passwords
D. Authenticate users

**70.** A TLS VPN typically uses:
A. UDP 4500
B. TCP 443 (HTTPS), often easier through restrictive firewalls
C. ESP protocol
D. AH only

**71.** WireGuard is:
A. A legacy VPN protocol
B. A modern VPN with smaller codebase and simpler key management than IPsec
C. A WiFi protocol
D. An antivirus product

**72.** WPA3 introduces:
A. WEP-equivalent encryption
B. Stronger handshake (SAE/Dragonfly), forward secrecy, protection against offline dictionary attacks
C. Lower security than WPA2
D. Mandatory cloud authentication

**73.** An evil twin attack:
A. Decrypts WPA3 traffic
B. Creates a rogue AP impersonating a legitimate SSID to capture credentials
C. Performs SQL injection
D. Is a type of DDoS

**74.** A wardriving attack involves:
A. Driving cars autonomously
B. Searching for unprotected or weakly protected WiFi networks
C. Stealing vehicles via Bluetooth
D. Modifying GPS

**75.** ARP spoofing operates at:
A. Layer 1
B. Layer 2 (sending fake ARP replies)
C. Layer 3
D. Layer 7

**76.** DNS poisoning corrupts:
A. The TCP stack
B. The DNS cache so victims resolve names to attacker IPs
C. The ARP table
D. The routing table

**77.** A SYN flood attack exploits:
A. Application-layer logic
B. The TCP three-way handshake by sending many SYNs and ignoring the responses
C. UDP connections
D. ICMP

**78.** A reflection/amplification DDoS attack uses:
A. The OSI Layer 1
B. Protocols like DNS or NTP with spoofed source addresses to amplify traffic toward a victim
C. Encrypted tunnels
D. Local hosts only

**79.** A NIDS sees:
A. Only encrypted traffic
B. Network traffic in transit, but cannot decrypt TLS without keys
C. Only local host events
D. Application-source code

**80.** A HIDS sees:
A. Network traffic between hosts
B. Activity on the host it runs on (file changes, process behavior, logs)
C. Wireless RF only
D. Cloud-provider traffic only

**81.** A signature-based IDS:
A. Catches new (zero-day) threats easily
B. Requires known patterns; cannot catch threats without signatures
C. Uses statistical baselining
D. Cannot generate alerts

**82.** An anomaly-based IDS:
A. Uses known signatures only
B. Baselines normal behavior and alerts on deviations
C. Cannot generate false positives
D. Operates only on encrypted traffic

**83.** NAC (Network Access Control) verifies:
A. The destination IP only
B. Device posture (patches, AV, config) before granting network access
C. The user's role in HR
D. The MFA factor count

**84.** SaaS shifts the most security responsibility to:
A. The customer
B. The cloud provider
C. The CASB
D. The end user

**85.** A CASB sits:
A. On the host
B. Between users and cloud services to enforce policy
C. Inside the firewall
D. On the WAN

### Domain 5: Security Operations (Q86-100)

**86.** Data in transit is protected by:
A. Full-disk encryption
B. TLS or VPN
C. Hashing
D. ACLs only

**87.** Which is symmetric?
A. RSA
B. AES
C. ECC
D. DSA

**88.** Which provides non-repudiation?
A. AES-GCM
B. SHA-256
C. Digital signature using the sender's private key
D. HMAC

**89.** PKI uses asymmetric cryptography to:
A. Encrypt bulk data
B. Establish trust and exchange keys, often paired with symmetric for bulk encryption
C. Hash passwords
D. Replace TLS

**90.** A CRL is:
A. A list of revoked certificates published by the CA
B. A real-time revocation check
C. A list of trusted CAs
D. A certificate signing request

**91.** OCSP differs from CRL in that:
A. OCSP is a real-time revocation check; CRL is a list
B. They are identical
C. CRL is real-time
D. OCSP is offline only

**92.** Data destruction levels (NIST SP 800-88) from weakest to strongest:
A. Destroy, Purge, Clear
B. Clear, Purge, Destroy
C. Purge, Clear, Destroy
D. Destroy, Clear, Purge

**93.** Degaussing primarily:
A. Encrypts a disk
B. Reduces magnetic media to a state where data recovery is infeasible
C. Refurbishes media for reuse
D. Backs up data

**94.** SIEM, SOAR, SOC are best characterized as:
A. The same thing
B. SIEM = platform that aggregates logs; SOAR = automation on top; SOC = team that runs them
C. All hardware appliances
D. All open-source tools

**95.** A CVSS score of 9.8 indicates:
A. A low-severity vulnerability
B. A critical-severity vulnerability
C. A patched vulnerability
D. A false positive

**96.** A zero-day vulnerability is:
A. One that is patched on Day 0
B. One the vendor has had zero days to patch
C. One discovered by automated scanners
D. One that exists for 24 hours only

**97.** Current NIST password guidance prefers:
A. Mandatory 90-day rotation
B. Long passphrases, no forced rotation, breach-corpus checks, MFA
C. Complex character classes plus rotation
D. Security questions

**98.** A BYOD policy should require:
A. MDM enrollment, ability to remotely wipe corporate data, separation from personal data
B. Surrender of personal devices
C. No use of personal devices anywhere
D. Annual device replacement

**99.** Change management requires:
A. Skipping testing for speed
B. Documentation, approval, testing, rollback procedures
C. Encryption of every change
D. Manager veto only

**100.** The most common initial-access vector remains:
A. Zero-day exploit
B. Supply-chain compromise
C. Phishing and other social engineering
D. Physical break-in

---

### Mock 3 Answer Key

```
1.B  2.B  3.C  4.B  5.C  6.B  7.C  8.B  9.B  10.B
11.B 12.B 13.C 14.B 15.B 16.B 17.B 18.B 19.A 20.D
21.A 22.C 23.B 24.C 25.B 26.A 27.B 28.A 29.B 30.A
31.B 32.A 33.B 34.B 35.A 36.C 37.B 38.B 39.A 40.B
41.B 42.A 43.A 44.B 45.A 46.B 47.B 48.A 49.B 50.A
51.B 52.B 53.B 54.B 55.B 56.B 57.B 58.A 59.B 60.B
61.B 62.B 63.B 64.A 65.B 66.A 67.B 68.B 69.B 70.B
71.B 72.B 73.B 74.B 75.B 76.B 77.B 78.B 79.B 80.B
81.B 82.B 83.B 84.B 85.B 86.B 87.B 88.C 89.B 90.A
91.A 92.B 93.B 94.B 95.B 96.B 97.B 98.A 99.B 100.C
```

---

## Mock 4 (100 questions, weighted toward weak domains, final cram)

### Domain 1: Security Principles (Q1-10)

**1.** Which is BEST evidence of integrity?
A. Encryption at rest
B. Hash comparison
C. Multi-factor authentication
D. Backup retention

**2.** A risk register lists:
A. Active incidents only
B. Identified risks with treatment plans
C. Approved vendors
D. Vulnerabilities only

**3.** A "data owner" role primarily:
A. Manages backups
B. Has accountability for classifying and protecting a dataset
C. Operates the firewall
D. Conducts audits

**4.** The ISC2 first canon prioritizes:
A. The client's interests
B. Society and the common good
C. Personal advancement
D. Profitability

**5.** Risk mitigation is best described as:
A. Eliminating the activity
B. Reducing likelihood or impact via controls
C. Transferring to insurance
D. Accepting and documenting

**6.** Which is a deterrent control specifically?
A. A locked server room
B. A "no trespassing" sign
C. An IDS alert
D. A daily backup

**7.** Defense in depth is:
A. A single strong control
B. Multiple layered controls so one failure does not breach the system
C. Encrypting everything at maximum strength
D. Hiring more analysts

**8.** A "data custodian" role primarily:
A. Decides who can access the data
B. Operates the systems where the data resides, per the owner's policy
C. Replaces the data owner
D. Conducts external audits

**9.** Risk avoidance is appropriate when:
A. The risk is small and manageable
B. The risk is so severe that ceasing the activity is the best option
C. Insurance is cheap
D. The org is risk-tolerant

**10.** A "compensating control" is used when:
A. The primary control is infeasible, requiring an alternative
B. There is no risk
C. Auditors require redundancy
D. Encryption fails

### Domain 2: BC, DR, IR (Q11-35) - HEAVY

**11.** RTO measures:
A. Acceptable data loss
B. Acceptable system downtime
C. Maximum total outage tolerance
D. Recovery cost

**12.** RPO measures:
A. Acceptable data loss
B. Acceptable system downtime
C. Backup duration
D. Site activation time

**13.** A BIA identifies critical processes BEFORE:
A. RTO and RPO are set
B. After RTO is set
C. Independently of recovery objectives
D. Only during incidents

**14.** Order of recovery in a disaster typically:
A. Restore the most critical mission functions first
B. Restore everything simultaneously
C. Restore alphabetically by system name
D. Restore the cheapest systems first

**15.** A warm site has:
A. Hardware and network in place but needs data restored
B. Only empty space
C. Current data and is ready to switch over in hours
D. Identical capacity to production

**16.** "Failback" refers to:
A. Switching from primary to recovery site
B. Returning operations from the recovery site to the restored primary
C. Failing a BCP test
D. Restoring a backup that failed

**17.** A simulation BCP test:
A. Walks through a scenario with discussion only
B. Has the response team act out a simulated disaster without real switchover
C. Switches over to the recovery site for real
D. Reads the plan aloud

**18.** A parallel test:
A. Brings up the failover alongside the primary; both run, primary stays live
B. Only does a checklist
C. Is identical to full cutover
D. Cannot be conducted in production

**19.** The IR preparation phase includes:
A. Containment of active threats
B. Staffing, training, tooling, communications plans
C. Forensic analysis
D. Eradication

**20.** An "indicator of compromise" (IoC) is:
A. A sign an incident may occur
B. A sign an incident has occurred or is in progress
C. The first phase of IR
D. A regulation

**21.** First action when malware is detected on a production server:
A. Power off the server immediately
B. Determine scope and contain (likely isolate from network) while preserving evidence
C. Restore from backup immediately
D. Notify all employees

**22.** Memory should be captured BEFORE:
A. Disk imaging
B. Powering down (to preserve volatile data)
C. The incident is contained
D. Lessons learned

**23.** Chain of custody documentation primarily preserves:
A. System uptime
B. Admissibility of evidence in legal proceedings
C. Backup integrity
D. Patch level

**24.** An IR team that handles incidents directly across the org from one location is:
A. Central team
B. Distributed team
C. Coordinating team
D. Outsourced team

**25.** "Containment short-term" might mean:
A. Isolating the affected host from the network
B. Rebuilding all affected systems
C. The forensics phase
D. Lessons learned only

**26.** "Eradication" means:
A. Restoring backups
B. Removing the threat (malware, malicious accounts, persistence mechanisms)
C. Communicating with executives
D. Closing the incident ticket

**27.** Lessons learned should produce:
A. A finger-pointing report
B. Process and playbook improvements, training updates
C. Termination of responsible employees
D. A media release

**28.** A "containment long-term" decision might be:
A. Rebuilding compromised systems from clean images
B. Calling law enforcement
C. Closing all tickets
D. Sending an all-hands email

**29.** A coordinating IR team typically:
A. Responds directly to incidents on the ground
B. Advises and coordinates distributed responders without direct action
C. Is the same as a central team
D. Outsources everything

**30.** An incident's "functional impact" measures:
A. Business operations affected
B. CVSS score
C. Patch level
D. Network segment count

**31.** An incident's "information impact" measures:
A. The sensitivity and volume of data affected
B. The CIA triad of network packets
C. The number of users
D. The patch level

**32.** "Recoverability effort" categorizes:
A. The estimated work required to restore
B. The patch level
C. The user impact
D. The CVE number

**33.** A "tabletop" exercise primarily:
A. Tests the team's ability to discuss and walk through a scenario
B. Performs a real cutover
C. Replaces a checklist
D. Generates compliance reports

**34.** An MOU between two organizations is:
A. A binding legal contract
B. A formal but generally non-binding agreement of intent
C. The same as a SLA
D. A type of insurance

**35.** A failure to maintain chain of custody can result in:
A. Faster recovery
B. Evidence being ruled inadmissible
C. Lower legal cost
D. Better lessons learned

### Domain 3: Access Control Concepts (Q36-50)

**36.** Which model is most common in commercial enterprises?
A. MAC
B. DAC
C. RBAC
D. ABAC

**37.** "Owner" in DAC refers to:
A. The data owner who decides who else gets access
B. The system administrator
C. The user with the most privilege
D. The auditor

**38.** ABAC's flexibility comes from:
A. Static role mappings
B. Combining user, resource, and environment attributes in dynamic policy
C. Single attribute per user
D. Mandatory labels

**39.** A "discretionary" model puts decisions in the hands of:
A. The system
B. The owner
C. The auditor
D. The user

**40.** Physical "tailgating" can be defeated by:
A. Encryption
B. Mantraps and security training
C. Strong passwords
D. NAC

**41.** "AAL3" requires:
A. Single-factor authentication
B. Multi-factor with a hardware-cryptographic authenticator
C. Biometric only
D. Smart card only

**42.** A False Acceptance Rate (FAR):
A. Is a Type 1 error
B. Is a Type 2 error
C. Means a legitimate user was denied
D. Is unimportant

**43.** "Just-in-time" privilege elevation:
A. Permanently elevates the user
B. Temporarily elevates for the duration of a task, then reverts
C. Replaces RBAC
D. Is a backup procedure

**44.** Separation of duties typically:
A. Reduces one person's ability to commit fraud
B. Eliminates the need for monitoring
C. Doubles operational cost without benefit
D. Replaces least privilege

**45.** A typical SSO with MFA flow:
A. User authenticates once with MFA at the SSO; subsequent app access uses tokens
B. User authenticates with MFA at every app
C. User skips MFA entirely
D. The SSO has no MFA

**46.** Federation differs from SSO in that federation:
A. Is internal SSO only
B. Crosses organizational trust boundaries via standards like SAML and OIDC
C. Replaces passwords
D. Is the same as SSO

**47.** A "smart card with PIN" is:
A. Single-factor (something you have)
B. Multi-factor (something you have plus something you know)
C. Three-factor
D. Single-step

**48.** Privilege creep means:
A. Privileges escalate during attacks
B. Users accumulate excess privileges over role changes if not cleaned up
C. The org adds new privileges over time
D. Privileges decrease

**49.** A least-privilege review should be done:
A. Once at hire
B. Periodically (e.g., quarterly) and at every role change
C. Only on termination
D. Never

**50.** Logging access decisions contributes to the "A" in AAA standing for:
A. Authorization
B. Accounting
C. Authentication
D. Availability

### Domain 4: Network Security (Q51-85) - HEAVIEST

**51.** The OSI Transport Layer handles:
A. Routing across networks
B. End-to-end delivery and ports (TCP, UDP)
C. Application data
D. Bits on the wire

**52.** Port 22 is used by:
A. Telnet
B. SSH and SFTP
C. FTP
D. HTTP

**53.** Port 25 is used by:
A. SMTP
B. POP3
C. IMAP
D. DNS

**54.** Port 53 is used by:
A. DNS
B. DHCP
C. HTTPS
D. SSH

**55.** Port 3389 is used by:
A. RDP (Remote Desktop Protocol)
B. SSH
C. Telnet
D. FTP

**56.** A common port for SMB (Server Message Block) is:
A. 21
B. 80
C. 445
D. 53

**57.** ICMP is used by:
A. Web browsers
B. The `ping` utility for echo request/reply
C. Email clients
D. File transfer

**58.** Class A private IPv4 range is:
A. 10.0.0.0/8
B. 172.16.0.0/12
C. 192.168.0.0/16
D. 169.254.0.0/16

**59.** Class B private IPv4 range is:
A. 10.0.0.0/8
B. 172.16.0.0/12
C. 192.168.0.0/16
D. 169.254.0.0/16

**60.** Class C private IPv4 range is:
A. 10.0.0.0/8
B. 172.16.0.0/12
C. 192.168.0.0/16
D. 169.254.0.0/16

**61.** IPv4 loopback:
A. 192.168.0.1
B. 127.0.0.1
C. 10.0.0.1
D. 0.0.0.0

**62.** IPv6 loopback:
A. ::1
B. ::0
C. fe80::1
D. 127.0.0.1

**63.** IPv6 address length is:
A. 32 bits
B. 64 bits
C. 128 bits
D. 256 bits

**64.** A "private" IPv4 address:
A. Is routable on the public internet
B. Is non-routable on the public internet and used inside organizations
C. Is the same as a loopback
D. Is reserved for multicast

**65.** TCP is connection-oriented and provides:
A. Best-effort delivery
B. Reliable, ordered delivery with retransmission
C. Stateless service
D. Multicast

**66.** UDP provides:
A. Connection-oriented service
B. Connectionless, best-effort service
C. Guaranteed delivery
D. Encrypted transport

**67.** A worm differs from a virus in that:
A. A worm needs a host file
B. A worm self-propagates without needing a host
C. They are the same
D. A worm is benign

**68.** Ransomware typically:
A. Steals data only
B. Encrypts data and demands payment for decryption
C. Floods networks
D. Performs reconnaissance

**69.** A Trojan:
A. Appears legitimate, hides malicious payload
B. Self-propagates like a worm
C. Is the same as a logic bomb
D. Cannot be installed by a user

**70.** A logic bomb:
A. Triggers on a condition like a date or event
B. Is the same as a worm
C. Is benign
D. Self-propagates

**71.** A botnet's C2 channel is:
A. The command-and-control link between bots and operator
B. A type of firewall
C. A network segmentation tool
D. A backup protocol

**72.** Phishing's voice variant is:
A. Smishing
B. Vishing
C. Whaling
D. Pretexting

**73.** SMS-based phishing is:
A. Smishing
B. Vishing
C. Whaling
D. Spear phishing

**74.** Targeted phishing aimed at a specific person is:
A. Spear phishing
B. Whaling
C. Smishing
D. Pretexting

**75.** "Whaling" targets:
A. Random users
B. High-value targets like executives
C. Mobile users only
D. Foreign citizens

**76.** Pretexting involves:
A. Creating a fabricated scenario to extract information
B. Sending random emails
C. Crashing systems
D. Hacking WiFi

**77.** A supply-chain attack compromises:
A. A target's direct systems
B. A trusted vendor or component to reach downstream targets
C. Shipping vehicles
D. Stock prices

**78.** Default WiFi security on most modern devices is:
A. WEP
B. WPA
C. WPA2 with AES-CCMP
D. Open (no encryption)

**79.** A "rogue access point" is:
A. An unauthorized AP, potentially impersonating a legitimate SSID
B. A misconfigured printer
C. A backup router
D. A wired switch

**80.** A side-channel attack might use:
A. SQL injection
B. Timing analysis or power-consumption measurement
C. Brute-force credentials
D. Buffer overflow

**81.** A buffer overflow primarily targets:
A. Network layer
B. Application layer (memory corruption in software)
C. Data link layer
D. Physical layer

**82.** A SOC (Security Operations Center) typically operates:
A. 9-5 on weekdays only
B. 24/7 with monitoring shifts
C. Only during incidents
D. Quarterly

**83.** A SIEM correlation rule like "10 failed logins followed by 1 success" might indicate:
A. A normal user behavior
B. A credential stuffing or brute-force attack
C. A DDoS
D. A patching event

**84.** A NIDS placed in-line that drops malicious packets is actually a:
A. NIPS (Network Intrusion Prevention System)
B. HIDS
C. SIEM
D. Firewall

**85.** Egress filtering blocks:
A. Inbound malicious traffic
B. Outbound traffic that should not leave (e.g., spoofed source addresses, blocked protocols)
C. Encrypted traffic
D. UDP only

### Domain 5: Security Operations (Q86-100)

**86.** Data states are:
A. Hot, warm, cold
B. At rest, in transit, in use
C. Public, private, secret
D. Active, archived

**87.** Symmetric encryption uses:
A. One key for both encrypt and decrypt
B. A key pair
C. No keys
D. Hash functions

**88.** Asymmetric encryption uses:
A. One shared key
B. A public/private key pair
C. Three keys
D. No keys

**89.** Hashing is:
A. Reversible
B. One-way; cannot be reversed
C. The same as encryption
D. Required for symmetric ciphers

**90.** A salt added to a password hash:
A. Encrypts it
B. Adds per-password random data to defeat rainbow tables
C. Is the same as a pepper
D. Makes hashing reversible

**91.** A digital certificate (X.509) binds:
A. A public key to an identity, signed by a CA
B. A username to an IP address
C. A file hash to a backup
D. A MAC address to an IP

**92.** Public Key Infrastructure components include:
A. CA, RA, CRL/OCSP, certificates
B. Firewall, IDS, SIEM, SOAR
C. RAM, disk, CPU, network
D. RTO, RPO, MTD, WRT

**93.** Data classification "Confidential" typically:
A. Is publishable
B. Requires restricted access and protection appropriate to sensitivity
C. Can be emailed without protection
D. Is the lowest sensitivity

**94.** "Purge" data sanitization includes:
A. Re-formatting
B. Degaussing or thorough overwrite making recovery infeasible
C. Physical destruction
D. Encryption

**95.** "Destroy" data sanitization includes:
A. Encryption only
B. Physical destruction (shredding, incineration, pulverization)
C. Overwriting once
D. Re-formatting

**96.** A SIEM's primary job is to:
A. Replace firewalls
B. Aggregate, correlate, and alert on log events from many sources
C. Encrypt logs
D. Block traffic

**97.** A CVE record provides:
A. A unique ID for a vulnerability with description
B. A severity score
C. The patch
D. The exploit code

**98.** CVSS is:
A. A vulnerability ID system
B. A 0-10 severity scoring system for vulnerabilities
C. A backup standard
D. A network protocol

**99.** Patch management process:
A. Skip testing for speed
B. Identify, test in non-production, deploy, verify, document
C. Apply only on Patch Tuesday
D. Auto-apply without verification

**100.** A "clean-desk" policy mitigates:
A. Phishing
B. Visual data exposure when users are away
C. Network attacks
D. Insider threats only

---

### Mock 4 Answer Key

```
1.B  2.B  3.B  4.B  5.B  6.B  7.B  8.B  9.B  10.A
11.B 12.A 13.A 14.A 15.A 16.B 17.B 18.A 19.B 20.B
21.B 22.B 23.B 24.A 25.A 26.B 27.B 28.A 29.B 30.A
31.A 32.A 33.A 34.B 35.B 36.C 37.A 38.B 39.B 40.B
41.B 42.B 43.B 44.A 45.A 46.B 47.B 48.B 49.B 50.B
51.B 52.B 53.A 54.A 55.A 56.C 57.B 58.A 59.B 60.C
61.B 62.A 63.C 64.B 65.B 66.B 67.B 68.B 69.A 70.A
71.A 72.B 73.A 74.A 75.B 76.A 77.B 78.C 79.A 80.B
81.B 82.B 83.B 84.A 85.B 86.B 87.A 88.B 89.B 90.B
91.A 92.A 93.B 94.B 95.B 96.B 97.A 98.B 99.B 100.B
```

---

End of Mocks 3-4. With Mocks 1-4 you have 400 ISC2 CC-style questions across the 5 domains.
