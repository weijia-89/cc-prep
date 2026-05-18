# ISC2 CC Study Guide - cram edition

**Target exam date:** May 30, 2026. Built May 17, 2026 for a 13-day cram.

**Prelim quiz scores (set the weighting):**

| Domain | Score | Weight in this guide |
|---|---|---|
| 1 Security Principles | 87% (26/30) | Light review |
| 2 BC/DR/IR | 60% (6/10) | Heavy |
| 3 Access Control | 75% (15/20) | Moderate |
| 4 Network Security | 55% (11/20) | **Heaviest** |
| 5 Security Operations | 75% (15/20) | Moderate |

**Source corpus body-read:** ISC2 CC Exam Outline (canon), NIST SP 800-12r1 (Intro to Infosec), NIST SP 800-34r1 (Contingency Planning), NIST SP 800-41r1 (Firewalls), NIST SP 800-61r3 (IR, April 2025, replaces r2), NIST SP 800-63B (Authentication), NIST SP 800-77r1 (IPsec VPNs), NIST SP 800-115 (Security Testing), NIST SP 800-53r5 (Controls), OWASP Top 10:2025.

**Style note:** every initialism is defined on first use in body text. See `glossary.md` for the consolidated reference.

---

## Part 1 - Security Principles (Domain 1, ISC2 weight ~26%)

> **Memory anchors (palace Room 1: Foyer, Domain 1).** Pick a foyer or entryway you know intimately. List 5-6 distinct loci in order: door, mat, hooks or coat rack, mirror, side table, shelf, or whatever your foyer actually has. For each Domain 1 anchor below, choose your own image to place at one locus; vivid and personal beats clever. Capture each choice as a gutter note.
>
> - **CIA + AAA** (Confidentiality / Integrity / Availability; Authentication / Authorization / Accounting)
> - **PASA** (ethics canon order: Protect society / Act honorably / Service to principals / Advance the profession; earlier canons win when they conflict)
> - **ATMA** (risk treatments: Avoid / Transfer / Mitigate / Accept)
> - **5 authentication factors** (Know / Have / Are / Where / Do; MFA requires factors from two different categories)
> - **SLE x ARO = ALE** (risk math: single-loss x annual rate = annual loss)
> - **RPS-PGB** (policy hierarchy: Regulation / Policy / Standard / Procedure / Guideline / Baseline; top three mandatory, bottom three recommended)
>
> See Appendix D.2 for the elicitation framework.

Wei is at 87% on the prelim. This part is a vocabulary refresh, not a re-teach. Hit the named concepts ISC2 will quiz.

### 1.1 Information assurance - the CIA triad plus

**Confidentiality.** Information is not disclosed to unauthorized parties. Achieved by encryption, access controls, classification, and need-to-know.

**Integrity.** Information is not modified by unauthorized parties, intentionally or accidentally. Achieved by hashing, digital signatures, version control, change management.

**Availability.** Information and systems are accessible to authorized users when needed. Achieved by redundancy, capacity planning, backups, BC/DR (business continuity / disaster recovery) plans.

**Authentication.** Verifying that an identity claim is true. Five factors:

1. Something you know (password, PIN)
2. Something you have (hardware token, smart card, phone)
3. Something you are (biometric - fingerprint, iris, face)
4. Somewhere you are (IP geolocation, GPS)
5. Something you do (typing rhythm, gait)

**MFA (multi-factor authentication)** requires two or more factors from *different* categories. Two passwords are not MFA. Password plus SMS code is MFA (something you know plus something you have).

**Non-repudiation.** A party cannot later deny having performed an action. Achieved by digital signatures plus audit logging. Symmetric encryption alone does not provide non-repudiation because both parties share the same key.

**Privacy.** Individual's right to control disclosure of personal information. Distinct from confidentiality: confidentiality is a control, privacy is the right that control protects. Regulated by GDPR (General Data Protection Regulation, EU), CCPA (California Consumer Privacy Act), HIPAA (Health Insurance Portability and Accountability Act).

### 1.2 Risk management

> **Anchor reminder (Room 1 locus).** Pick one image that captures **ATMA risk treatments** (Avoid / Transfer / Mitigate / Accept). Place it at a Foyer locus; capture as gutter note.

**Risk = threat × vulnerability × impact.** ISC2 will quiz this as a relationship, not a literal multiplication.

**Risk treatment options (four):**

| Treatment | What it means | Example |
|---|---|---|
| **Avoid** | Eliminate the activity that creates risk | Stop accepting credit cards |
| **Transfer** | Shift risk to a third party | Buy cyber insurance, outsource to SaaS |
| **Mitigate** | Reduce likelihood or impact | Deploy MFA, patch the vuln |
| **Accept** | Acknowledge and live with the risk | Document and move on (requires sign-off) |

**Inherent vs residual risk.** Inherent = before controls. Residual = after controls. Residual risk must be at or below the organization's **risk tolerance** (also called risk appetite).

**Risk identification → assessment → treatment.** The three steps ISC2 names. Assessment can be qualitative (high/med/low ranking) or quantitative (annualized loss expectancy ALE = single-loss expectancy SLE × annualized rate of occurrence ARO).

### 1.3 Security controls

> **Anchor reminder (Room 1 locus).** Pick one image that captures **default deny** as the safe baseline (default allow is the trap). Place it at a Foyer locus; capture as gutter note.

ISC2 names three categories:

**Technical (logical) controls.** Software, hardware, encryption, firewalls, IDS/IPS (intrusion detection / prevention systems), access control lists, MFA tokens.

**Administrative (managerial) controls.** Policies, procedures, training, background checks, separation of duties, hiring practices.

**Physical controls.** Locks, fences, badges, guards, mantraps, surveillance cameras (CCTV - closed-circuit television), bollards, biometric scanners at the door.

**Control functions (also tested):**

- **Preventive** (stops an incident - locks, encryption)
- **Detective** (identifies an incident - IDS, logs, alarms)
- **Corrective** (fixes after an incident - patching, restore from backup)
- **Deterrent** (discourages a threat - warning signs, visible cameras)
- **Compensating** (alternative when primary control infeasible - extra logging when MFA not possible)
- **Recovery** (restores operations - backups, failover sites)

### 1.4 ISC2 Code of Ethics

> **Anchor reminder (Room 1 locus).** Pick one image that captures **PASA canon order** (Protect society first, Act honorably, Service to principals, Advance the profession last; earlier canons win when they conflict). Place it at a Foyer locus; capture as gutter note.

Four canons. Order matters; ISC2 expects them in this order.

1. **Protect** society, the common good, necessary public trust and confidence, and the infrastructure.
2. **Act** honorably, honestly, justly, responsibly, and legally.
3. **Provide** diligent and competent service to principals.
4. **Advance** and protect the profession.

Preamble: "Safety and welfare of society and the common good, duty to our principals, and to each other, requires that we adhere, and be seen to adhere, to the highest ethical standards of behavior."

If canons conflict, **earlier canon wins.** Protecting society beats serving the principal.

### 1.5 Governance - the policy hierarchy

> **Anchor reminder (Room 1 locus).** Pick one image that captures **RPS-PGB policy hierarchy** (Regulation / Policy / Standard / Procedure / Guideline / Baseline; top three mandatory, bottom three recommended). Place it at a Foyer locus; capture as gutter note.

| Element | Force | Example |
|---|---|---|
| **Regulation / law** | Mandatory, external | HIPAA, GDPR, SOX (Sarbanes-Oxley) |
| **Policy** | Mandatory, internal, high-level | "All laptops shall encrypt data at rest" |
| **Standard** | Mandatory, internal, specific | "AES-256 in XTS mode for full-disk encryption" |
| **Procedure** | Mandatory, internal, step-by-step | "Run `cryptsetup` with these flags" |
| **Guideline** | Recommended, not mandatory | "Consider rotating disk encryption keys annually" |
| **Baseline** | Minimum acceptable configuration | "All Linux servers must meet CIS Level 1 benchmark" |

Memory anchor: **R-P-S-P-G-B** is the hierarchy. Regulations are external; policy/standards/procedures are mandatory internal; guidelines are recommended only.

---

## Part 2 - Business Continuity, Disaster Recovery, Incident Response (Domain 2, ISC2 weight ~10%)

> **Memory anchors (palace Room 2: Living Room, Domain 2).** Pick a living room you know. List 5 distinct loci in walkthrough order: couch, TV, fireplace, coffee table, bookshelf, or whatever your room actually has. For each Domain 2 anchor below, choose your own image to place at one locus; vivid and personal beats clever. Capture each choice as a gutter note.
>
> - **PDCP** (NIST 800-61 r2 IR phases: Preparation / Detection-and-Analysis / Containment-Eradication-Recovery / Post-Incident; short-term-isolate and long-term-rebuild both sit inside phase 3)
> - **RPO / RTO / MTD / WRT** (recovery numbers: data tolerance / downtime tolerance / outer limit / verification gap; RTO + WRT must be less than or equal to MTD)
> - **HWCR** (recovery sites in ascending cost: Hot ready immediately / Warm hours to ramp / Cold days / Reciprocal mutual)
> - **CTSPF** (BCP test ladder in ascending rigor: Checklist / Tabletop / Simulation / Parallel / Full Cutover)
> - **Order of volatility** (collect RAM before disk before archives)
>
> See Appendix D.2 for the elicitation framework.

Wei is at 60%. **Heavy emphasis** here. Three distinct concepts that ISC2 tests as separate but related.

### 2.1 The three plans, distinguished

| Plan | Scope | Trigger | Time horizon |
|---|---|---|---|
| **BCP (business continuity plan)** | Keep critical business functions running during a disruption | Any disruption | Hours to weeks |
| **DRP (disaster recovery plan)** | Restore IT systems after a disaster | Major disaster | Hours to months |
| **IRP (incident response plan)** | Respond to a security incident | Security incident detected | Minutes to days |

**BCP is broader than DRP.** BCP covers people, processes, facilities, IT. DRP is the IT subset of BCP. Both feed off the **BIA (Business Impact Analysis)**.

### 2.2 The BIA (Business Impact Analysis)

Per NIST SP 800-34r1, the BIA is the foundation. Three steps:

1. **Determine business processes and recovery criticality.** Identify mission-essential functions (MEFs). Rank processes by criticality.
2. **Identify resource requirements.** What people, systems, facilities, vendors does each MEF depend on?
3. **Identify system resource recovery priorities.** Order in which systems must come back online.

The BIA produces the **recovery objectives** that drive BCP/DRP design.

### 2.3 Recovery objectives - the four numbers ISC2 tests

> **Anchor reminder (Room 2 locus).** Pick one image that captures the **RPO vs RTO** trap (RPO = data tolerance, RTO = time tolerance; memorize the letter). Place it at a Living Room locus; capture as gutter note.

| Term | Question it answers | Example |
|---|---|---|
| **RPO (Recovery Point Objective)** | How much data can we afford to lose? | RPO of 1 hour means backups must be ≤1 hour old |
| **RTO (Recovery Time Objective)** | How long can we be down? | RTO of 4 hours means system must be back in 4 hours |
| **MTD (Maximum Tolerable Downtime)** | Absolute outer limit before business fails | MTD of 24 hours - past this, the business does not recover |
| **WRT (Work Recovery Time)** | Time after RTO to verify, restore data, resume work | WRT of 1 hour means after the 4-hour RTO, 1 more hour to validate |

**Relationship:** RTO + WRT ≤ MTD. The system must be technically up (RTO), then verified and loaded with current data (WRT), all within the absolute MTD.

**RPO is about data loss; RTO is about downtime.** Memory anchor: **P**oint = data **P**oint in time before failure; **T**ime = downtime.

### 2.4 Recovery sites - the four options

> **Anchor reminder (Room 2 locus).** Pick one image that captures the **HWCR site ladder** (Hot fast and expensive / Warm middle / Cold slow and cheap / Reciprocal mutual). Place it at a Living Room locus; capture as gutter note.

| Site type | Setup time | Cost | What's there |
|---|---|---|---|
| **Hot site** | Hours | Highest | Fully equipped, current data, ready to switch over |
| **Warm site** | 1-3 days | Medium-high | Hardware present, data needs restoring |
| **Cold site** | Weeks | Lowest | Empty space with power and network only |
| **Reciprocal agreement** | Variable | Low cash, high trust | Use another org's facility under mutual agreement |
| **Cloud / mobile** | Hours to days | Variable | Cloud failover, mobile data center |

Trade-off: hot site = fast recovery, high cost. Cold site = slow recovery, low cost.

### 2.5 BCP/DRP testing - five test types in increasing rigor

1. **Checklist (review)** - read through the plan, verify completeness. Lowest cost, lowest realism.
2. **Tabletop (structured walk-through)** - team walks through a scenario verbally. Discussion-based.
3. **Simulation** - simulated disaster, team responds, no real switchover.
4. **Parallel** - failover systems brought up alongside primary; both run, primary stays live.
5. **Full interruption (cutover)** - primary actually goes down; failover takes over. Highest cost, highest realism, highest risk.

Memory anchor: **C-T-S-P-F**. Start with checklist, end with full cutover only when confident.

### 2.6 Incident response lifecycle

> **Anchor reminder (Room 2 locus).** Pick one image that captures **PDCP IR phases** (Preparation / Detection-and-Analysis / Containment-Eradication-Recovery / Post-Incident; short-term-isolate and long-term-rebuild both sit inside phase 3). Place it at a Living Room locus; capture as gutter note.

**ISC2 currently teaches the SP 800-61r2 lifecycle** (four phases, the canonical model). NIST published SP 800-61r3 in April 2025 reframing IR around the CSF (Cybersecurity Framework) 2.0 six Functions, but the CC exam still tests the four-phase model.

**SP 800-61r2 four phases (memorize):**

1. **Preparation** - staffing, training, tooling, communications plans, hardening. Done before any incident.
2. **Detection and Analysis** - identify that something is happening; classify severity. Distinguishes **precursors** (signs an incident might occur) from **indicators** (signs an incident has occurred).
3. **Containment, Eradication, and Recovery** - stop the bleeding, remove the threat, restore service. Containment can be **short-term** (isolate) or **long-term** (rebuild).
4. **Post-Incident Activity** - lessons learned, update playbooks, evidence retention.

**Mnemonic:** **P** **DA** **CER** **PI**. Or just remember: Prep → Detect → Contain → Post.

**SP 800-61r3 (CSF 2.0 alignment, newer):** the same activities are mapped to CSF 2.0's six Functions - Govern, Identify, Protect, Detect, Respond, Recover. Govern/Identify/Protect = the old Preparation phase. Detect = old Detection. Respond = old Containment/Eradication. Recover = old Recovery + Post-Incident. The CC exam outline references the older r2 model; know it.

### 2.7 IR team models and members

**Team models (per SP 800-61):**

- **Central team** - one team for the whole org. Best for small orgs.
- **Distributed teams** - multiple teams by geography or business unit, coordinated by a central function.
- **Coordinating team** - central team that doesn't respond directly but advises distributed responders.

**Staffing models:**

- **Employees** - in-house, highest familiarity, highest cost.
- **Partially outsourced** - in-house plus a retainer with an IR firm.
- **Fully outsourced** - third-party MSSP (Managed Security Service Provider) handles everything.

**Roles:** Incident handler (lead), forensic analyst, malware analyst, communications lead, legal counsel, HR liaison, executive sponsor.

### 2.8 Evidence handling - chain of custody

> **Anchor reminder (Room 2 locus).** Pick one image that captures the **order of volatility** (RAM first, then disk, then archives). Place it at a Living Room locus; capture as gutter note.

When evidence may be used legally, **chain of custody** must be maintained: who collected it, when, how, where it was stored, who accessed it. Break the chain → evidence inadmissible.

**Order of volatility** - collect most-volatile evidence first:

1. CPU registers, cache
2. RAM (memory)
3. Network state, running processes
4. Disk
5. Remote logs, archival media

Image disks **before** rebooting, or you lose RAM.

---

## Part 3 - Access Control Concepts (Domain 3, ISC2 weight ~22%)

> **Memory anchors (palace Room 3: Bedroom, Domain 3).** Pick a bedroom you know. List 5 distinct loci in order: bed posts, closet, dresser, window, nightstand, or whatever your bedroom actually has. For each Domain 3 anchor below, choose your own image to place at one locus; vivid and personal beats clever. Capture each choice as a gutter note.
>
> - **DMRA** (access control models: DAC owner-decides / MAC system-enforces-labels / RBAC role-tied / ABAC attribute-tied; do not confuse Mandatory Access Control with Media Access Control)
> - **AAL levels** (NIST 800-63B assurance: AAL1 single-factor / AAL2 multi-factor / AAL3 hardware-cryptographic)
> - **Biometric errors** (FRR Type 1 false-reject is annoying / FAR Type 2 false-accept is dangerous / CER crossover where the two rates meet)
> - **Physical controls** (mantrap preventive / bollards anti-ramming / floodlight deterrent)
> - **IAAA + identity protocols** (Identification / Authentication / Authorization / Accounting; Kerberos for intranet ticket-based, SAML for federated SSO via XML, OAuth for authorization delegation)
>
> See Appendix D.2 for the elicitation framework.

Wei is at 75%. Moderate weight.

### 3.1 Physical access controls

**Layered defense (defense in depth physical):** perimeter → building → floor → room → cabinet → device.

**Common physical controls ISC2 names:**

- **Badge systems** - RFID (radio-frequency identification), proximity, smart card. Lost badges must be revocable.
- **Gate entry** - vehicle gates, turnstiles.
- **CCTV (closed-circuit television)** - surveillance, recording, monitoring.
- **Alarm systems** - motion, glass-break, door-contact sensors.
- **Logs** - sign-in books, badge-reader logs, visitor records.
- **Security guards** - human judgment, last line of detection.
- **Environmental design (CPTED - Crime Prevention Through Environmental Design)** - lighting, sight lines, fencing, landscaping that discourages intrusion.
- **Mantraps** - two-door vestibule, only one door opens at a time. Defeats tailgating (one person follows another through a door).
- **Bollards** - vehicle barriers, prevent ramming.
- **Biometric scanners at the door** - fingerprint, iris, hand geometry.

**Authorized vs unauthorized personnel.** Visitor badges visually distinct from employee badges. Escort policies for visitors. Termination triggers immediate badge revocation.

### 3.2 Logical access controls

**Principle of least privilege.** Users get only the access they need for their job, nothing more. Reduces blast radius of credential theft.

**Separation of duties (SoD).** No single person can complete a sensitive transaction alone. Prevents fraud. Example: developer cannot deploy to production; QA approves the deploy.

**Need-to-know.** Access requires both clearance level *and* a job reason. Distinct from clearance: a Top Secret clearance does not grant access to all Top Secret material - only the material the person needs to know.

### 3.3 Access control models - the four ISC2 tests

> **Anchor reminder (Room 3 locus).** Pick one image that captures **DMRA models** (DAC owner / MAC labels / RBAC role / ABAC attributes); separately pick one image that disambiguates Mandatory Access Control from Media Access Control. Place each at a Bedroom locus; capture both as gutter notes.

| Model | Who decides access | Example |
|---|---|---|
| **DAC (Discretionary Access Control)** | The data owner decides | Linux file permissions; Windows NTFS ACLs (access control lists). Owner can grant access at their discretion. |
| **MAC (Mandatory Access Control)** | System enforces based on labels | Military classification. Labels (Top Secret, Secret, Confidential) + clearance levels. User cannot override. |
| **RBAC (Role-Based Access Control)** | Access tied to job role | "Accountants" role gets access to accounting system. Most common in enterprise. |
| **ABAC (Attribute-Based Access Control)** | Access based on attributes of user, resource, environment | "Allow access if department=Finance AND device=corporate-managed AND time=business-hours" |

**MAC ≠ MAC.** Mandatory Access Control (security model) is different from Media Access Control (network hardware address). ISC2 questions sometimes hinge on which MAC is meant.

**Rule-Based Access Control** is sometimes listed separately - access decisions follow a set of rules independent of identity. Firewalls use rule-based.

### 3.4 IAAA (Identification, Authentication, Authorization, Accounting)

**Identification** - claiming an identity (username).
**Authentication** - proving the claim (password, token, biometric).
**Authorization** - what the authenticated identity is allowed to do.
**Accounting (auditing)** - recording what was done.

Sometimes called **AAA** when identification is folded into authentication.

### 3.5 Authentication factors and MFA depth

> **Anchor reminder (Room 3 locus).** Pick one image that captures the **5 authentication factors** (Know / Have / Are / Where / Do) and the rule that MFA requires factors from two different categories. Place it at a Bedroom locus; capture as gutter note.

Recap from 1.1:

- Something you know - password, PIN, security questions.
- Something you have - hardware token (RSA SecurID), smart card, phone (push notification, SMS code), FIDO2/WebAuthn key.
- Something you are - fingerprint, iris, face, voice, retina, palm vein.
- Somewhere you are - IP geolocation, GPS.
- Something you do - typing rhythm, gait, signature dynamics.

**Type 1 errors (false rejection)** - legitimate user denied. Annoying.
**Type 2 errors (false acceptance)** - impostor accepted. Dangerous.

**FRR (False Rejection Rate)** vs **FAR (False Acceptance Rate)**. **CER (Crossover Error Rate)** is where FRR = FAR; lower CER = better biometric system.

Per NIST SP 800-63B, **AAL (Authenticator Assurance Levels):**

- **AAL1** - single-factor (password alone). Lowest.
- **AAL2** - multi-factor, at least 2 factors.
- **AAL3** - multi-factor, hardware-based cryptographic authenticator required.

### 3.6 SSO (Single Sign-On) and federation

**SSO** - one login grants access to multiple applications. Reduces password fatigue and re-prompting.

**Federation** - SSO across organizational boundaries via trust relationships. Standards: SAML (Security Assertion Markup Language), OAuth 2.0, OpenID Connect (OIDC), Kerberos (for intranet).

**Risk of SSO:** if the SSO credential is compromised, attacker gets all linked applications. Mitigate with MFA on the SSO login.

---

## Part 4 - Network Security (Domain 4, ISC2 weight ~24%) - DEPTH PASS

> **Memory anchors (palace Room 4: Kitchen, Domain 4 - YOUR WEAKEST, MAKE THIS VIVID).** Pick a kitchen you know. List 5 distinct loci in order: pantry shelves, fridge door, stove burners, spice rack, attack-jars shelf, or whatever your kitchen actually has. For each Domain 4 anchor below, choose your own image to place at one locus; vivid and personal beats clever. Capture each choice as a gutter note.
>
> - **OSI 7 layers** (top to bottom: Application / Presentation / Session / Transport / Network / Data Link / Physical; mnemonic "All People Seem To Need Data Processing")
> - **IPsec** (AH authentication header / ESP encryption-plus-auth / IKE key exchange; Transport mode wraps payload only, Tunnel mode wraps the entire original packet plus a new IP header)
> - **Firewall types** (ascending sophistication: packet filter sees headers / stateful tracks connections / application-proxy reads protocol semantics / NGFW combines all plus IPS plus threat intel)
> - **Private IP ranges** (Class A 10.0.0.0/8 / Class B 172.16.0.0/12 / Class C 192.168.0.0/16 / APIPA 169.254.0.0/16 link-local-only)
> - **Named attacks** (ARP spoofing / DNS poisoning / MITM / evil twin; ISC2 outline 4.2 expects each by name)
> - **Port chunks** (file/shell 20-23, mail 25/110/143, web 80/443, names 53/67/123, Microsoft 135/445/3389, directory 389/636, management 161/162)
>
> See Appendix D.2 for the elicitation framework.

Wei is at 55%. **Maximum depth.** This is where the cram time goes.

### 4.1 OSI vs TCP/IP models - know both

**OSI (Open Systems Interconnection) - 7 layers, top to bottom:**

| # | Layer | What it does | Examples |
|---|---|---|---|
| 7 | Application | User-facing protocols | HTTP, FTP, SMTP, DNS |
| 6 | Presentation | Encoding, encryption, translation | TLS, JPEG, ASCII |
| 5 | Session | Establish/maintain/teardown sessions | NetBIOS, RPC, PPTP |
| 4 | Transport | End-to-end delivery, ports | TCP, UDP |
| 3 | Network | Routing, IP addressing | IP, ICMP, IPsec |
| 2 | Data Link | Frames, MAC addresses | Ethernet, ARP, switches |
| 1 | Physical | Bits on the wire | Cables, hubs, repeaters |

**Mnemonic top-to-bottom:** **All People Seem To Need Data Processing.**
**Bottom-to-top:** **Please Do Not Throw Sausage Pizza Away.**

**TCP/IP (DoD model) - 4 layers:**

| # | Layer | Maps to OSI | Examples |
|---|---|---|---|
| 4 | Application | OSI 5-6-7 | HTTP, FTP, DNS |
| 3 | Transport | OSI 4 | TCP, UDP |
| 2 | Internet | OSI 3 | IP, ICMP |
| 1 | Network Access | OSI 1-2 | Ethernet, WiFi |

ISC2 tests OSI more than TCP/IP, but expects familiarity with both.

### 4.2 IPv4 vs IPv6

**IPv4:** 32-bit addresses (4.3 billion total), written as dotted decimal `192.168.1.1`. Address exhaustion drove IPv6 adoption.

**IPv6:** 128-bit addresses (3.4 × 10^38), written as 8 groups of 4 hex digits `2001:0db8:85a3::8a2e:0370:7334`. Built-in IPsec support. No NAT needed at scale (every device gets a public address).

**Private (RFC 1918) IPv4 ranges (memorize):**

- `10.0.0.0/8` - Class A private
- `172.16.0.0/12` - Class B private
- `192.168.0.0/16` - Class C private

**Loopback:** `127.0.0.1` (IPv4), `::1` (IPv6).

### 4.3 Ports and protocols - memorize the common ones

| Port | Protocol | Use |
|---|---|---|
| 20, 21 | FTP | File Transfer Protocol (data, control) |
| 22 | SSH / SFTP | Secure Shell, Secure FTP |
| 23 | Telnet | Cleartext remote shell (insecure) |
| 25 | SMTP | Simple Mail Transfer Protocol |
| 53 | DNS | Domain Name System |
| 67, 68 | DHCP | Dynamic Host Configuration Protocol (server, client) |
| 69 | TFTP | Trivial FTP (no auth) |
| 80 | HTTP | HyperText Transfer Protocol |
| 110 | POP3 | Post Office Protocol v3 |
| 119 | NNTP | Network News Transfer Protocol |
| 123 | NTP | Network Time Protocol |
| 137-139 | NetBIOS | Windows networking |
| 143 | IMAP | Internet Message Access Protocol |
| 161, 162 | SNMP | Simple Network Management Protocol (agent, trap) |
| 389 | LDAP | Lightweight Directory Access Protocol |
| 443 | HTTPS | HTTP over TLS |
| 445 | SMB | Server Message Block (Windows file sharing) |
| 465, 587 | SMTPS | SMTP over TLS |
| 514 | Syslog | Logging |
| 636 | LDAPS | LDAP over TLS |
| 989, 990 | FTPS | FTP over TLS |
| 993 | IMAPS | IMAP over TLS |
| 995 | POP3S | POP3 over TLS |
| 1433 | MS SQL | Microsoft SQL Server |
| 1521 | Oracle | Oracle database |
| 3306 | MySQL | MySQL database |
| 3389 | RDP | Remote Desktop Protocol |
| 5432 | PostgreSQL | PostgreSQL database |

**Memory pattern:** the secure-TLS variant typically increments the cleartext port (HTTP 80 → HTTPS 443, but the pattern is not always +363). Memorize the ones above.

**TCP vs UDP:**

- **TCP (Transmission Control Protocol)** - connection-oriented, reliable, three-way handshake (SYN → SYN/ACK → ACK), in-order delivery, retransmission. Slower.
- **UDP (User Datagram Protocol)** - connectionless, best-effort, no handshake, faster. Used for DNS, VoIP, streaming.

**ICMP (Internet Control Message Protocol)** - diagnostics. `ping` uses ICMP echo request/reply. Often blocked at firewalls; can be abused for reconnaissance.

### 4.4 Network threats and attacks - ISC2 named list

**Malware family:**

- **Virus** - needs a host file; spreads when host runs.
- **Worm** - self-propagating across networks. No host file needed.
- **Trojan** - appears legitimate, hides malicious payload.
- **Ransomware** - encrypts data, demands payment. Often delivered as Trojan.
- **Rootkit** - burrows into the OS at deep privilege, hides itself.
- **Spyware** - exfiltrates information silently.
- **Logic bomb** - triggers on a condition (date, event).
- **Bot / botnet** - compromised hosts controlled by C2 (command and control).

**Network attacks:**

- **DoS (Denial of Service)** - overwhelm a target so legitimate users cannot use it.
- **DDoS (Distributed Denial of Service)** - DoS from many compromised hosts (a botnet). Harder to block.
- **MITM (Man in the Middle)** - attacker intercepts and possibly modifies traffic between two parties. ARP spoofing, rogue WiFi access points, BGP hijack.
- **Replay attack** - capture a valid authentication, replay it later. Defeated by nonces, timestamps.
- **DNS poisoning** - corrupt DNS cache so victims resolve a name to attacker's IP.
- **ARP spoofing** - send fake ARP (Address Resolution Protocol) replies, so victim sends traffic to attacker.
- **Side-channel attack** - extract info from physical characteristics (timing, power consumption, electromagnetic emanations) rather than breaking the algorithm.
- **Zero-day** - exploits a vulnerability not yet patched (vendor has had zero days to fix).
- **Social engineering** - phishing, spear phishing (targeted), whaling (executives), vishing (voice), smishing (SMS), pretexting, baiting.
- **Insider threat** - malicious or negligent employee, contractor, partner.
- **Supply chain attack** - compromise a vendor to reach the target. SolarWinds 2020.

**Wireless-specific:**

- **Evil twin** - rogue WiFi AP impersonating a legitimate one.
- **Wardriving** - searching for unprotected WiFi.
- **WEP / WPA / WPA2 / WPA3** - WiFi security protocols. WEP is broken. WPA2 (AES-CCMP) is the practical floor. WPA3 is current.

### 4.5 Detection and prevention - IDS, IPS, HIDS, NIDS

**IDS (Intrusion Detection System)** - monitors and alerts. Passive (out-of-band).
**IPS (Intrusion Prevention System)** - monitors and blocks. Active (in-line).

**By location:**

- **HIDS (Host-based)** - runs on individual hosts. Sees host activity (file changes, process behavior). Cannot see traffic to other hosts.
- **NIDS (Network-based)** - sits on the network. Sees traffic in transit. Cannot decrypt TLS unless given keys.

**By detection method:**

- **Signature-based** - pattern match against known threats. Cannot catch zero-days.
- **Anomaly-based** - baseline normal behavior, alert on deviations. Catches unknown threats but generates false positives.
- **Heuristic / behavioral** - rules about suspicious behavior. Middle ground.

**Antivirus / antimalware** - usually signature + heuristic on a host. Modern variants (EDR - Endpoint Detection and Response) add behavioral analytics + threat hunting.

### 4.6 Firewalls - types and where they sit

> **Anchor reminder (Room 4 locus).** Pick one image that captures the **stateful versus application firewall** distinction (stateful tracks connections; application reads protocol semantics). Place it at a Kitchen locus; capture as gutter note.

Per NIST SP 800-41r1:

**Firewall types (memorize the order from simplest to most capable):**

1. **Packet filter (stateless)** - examines individual packets against rules (source/dest IP, port, protocol). No memory of prior packets. Cheapest, fastest, dumbest. Most basic feature; usually layered with others.
2. **Stateful inspection** - tracks connections in a **state table**. Knows that a return packet belongs to an outgoing session you initiated. Industry baseline.
3. **Application-layer firewall (a.k.a. deep packet inspection)** - understands application protocols (HTTP, SMTP, DNS). Can block specific commands, detect protocol violations.
4. **Application-proxy gateway** - terminates the connection on the firewall, opens a new connection to the destination. Two separate connections, never a direct one. Strongest isolation.
5. **WAF (Web Application Firewall)** - specialized application-layer firewall for HTTP/HTTPS. Blocks SQL injection, XSS (cross-site scripting), other web attacks. Sits in front of web apps.
6. **NGFW (Next-Generation Firewall)** - combines stateful + app-aware + IPS + threat intel + user identity in one box. Common today.
7. **UTM (Unified Threat Management)** - NGFW plus antivirus, anti-spam, content filtering, VPN. Combines many functions for small/midsize orgs.
8. **Host-based / personal firewall** - runs on a single host (Windows Defender Firewall, iptables). Protects the host, not the network.

**Default deny.** Best-practice rule: block everything by default, explicitly allow only what's needed. Implicit deny at the end of every rule chain.

### 4.7 Network architectures and segmentation

> **Anchor reminder (Room 4 locus).** Pick one image that captures the **DMZ requires two firewalls** rule (or two interfaces on one firewall: one between internet and DMZ, one between DMZ and internal). Place it at a Kitchen locus; capture as gutter note.

**DMZ (Demilitarized Zone, also called perimeter network).** A subnet between the internet and the internal network. Hosts public-facing services (web, mail) so a compromise of those services does not directly expose the internal network. Two firewalls: one between internet and DMZ, one between DMZ and internal.

**VLAN (Virtual Local Area Network).** Logical segmentation of switch ports into separate broadcast domains. Layer 2. Separates traffic without separate physical switches.

**Subnetting.** Layer 3 segmentation. Each subnet is its own broadcast domain; routers move traffic between subnets.

**Micro-segmentation.** Fine-grained segmentation often at the host or workload level. Enforced by host-based firewalls or software-defined networking (SDN). Common in cloud and zero-trust architectures.

**Zero trust.** "Never trust, always verify." No implicit trust based on network location. Every request authenticated and authorized. NIST SP 800-207 is the canonical reference.

**Defense in depth.** Multiple layers of controls so that no single failure compromises the system. Physical + perimeter + network + host + application + data layers.

**NAC (Network Access Control).** Verifies a device's posture (patches, AV running, config) before granting network access. Quarantines non-compliant devices.

### 4.8 VPNs (Virtual Private Networks)

> **Anchor reminder (Room 4 locus).** Pick one image that captures **IPsec Transport vs Tunnel** (Transport wraps payload only; Tunnel wraps the entire packet plus a new IP header). Place it at a Kitchen locus; capture as gutter note.

**Purpose:** encrypted tunnel across an untrusted network (the internet).

**Architectures:**

- **Site-to-site (gateway-to-gateway)** - connects two networks. Branch office to HQ.
- **Remote access (host-to-gateway)** - connects a user device to a network. Employee laptop to corporate LAN.

**Protocols:**

- **IPsec (Internet Protocol Security)** - operates at Layer 3 (network). Two modes: **transport** (encrypts payload only) and **tunnel** (encrypts entire packet, adds new IP header). Authentication via **AH (Authentication Header)** or confidentiality+auth via **ESP (Encapsulating Security Payload)**. Key exchange via **IKE (Internet Key Exchange)**. Canonical for site-to-site.
- **TLS / SSL VPN** - operates at Layer 7 (application). Uses HTTPS port 443, easier through firewalls. Canonical for remote access via browser.
- **SSH tunneling** - port forwarding over SSH. Ad hoc.
- **WireGuard** - modern, simpler than IPsec, growing adoption.

**Older / weaker:** PPTP (broken), L2TP (needs IPsec for encryption).

### 4.9 Cloud service and deployment models

**Service models (the XaaS stack):**

| Model | Provider manages | Customer manages | Example |
|---|---|---|---|
| **IaaS (Infrastructure as a Service)** | Hardware, hypervisor, networking | OS, runtime, apps, data | AWS EC2, Azure VMs |
| **PaaS (Platform as a Service)** | Hardware + OS + runtime | Apps, data | Heroku, App Engine |
| **SaaS (Software as a Service)** | Everything | Configuration, data only | Salesforce, Gmail, Workday |
| **FaaS (Function as a Service)** | Everything except your function code | Function code | AWS Lambda |

**Shared responsibility:** the more "as-a-Service" you go, the more the provider handles. Security responsibility shifts but never fully transfers.

**Deployment models:**

- **Public cloud** - multi-tenant, provider-owned (AWS, GCP, Azure).
- **Private cloud** - single-tenant, self-hosted or vendor-hosted but dedicated.
- **Community cloud** - shared by orgs with common concerns (government, healthcare).
- **Hybrid cloud** - mix of public and private with orchestration between them.

**Cloud terms ISC2 names:**

- **SLA (Service Level Agreement)** - contractual uptime, support response, recovery commitments.
- **MSP (Managed Service Provider)** - third party managing IT services on the customer's behalf.
- **MSSP (Managed Security Service Provider)** - MSP focused on security.
- **CASB (Cloud Access Security Broker)** - policy enforcement point between users and cloud apps.
- **MOU (Memorandum of Understanding) / MOA (Memorandum of Agreement)** - formal but non-binding agreements between organizations.

### 4.10 On-premises infrastructure considerations

ISC2 explicitly tests these (Domain 4.3):

- **Power** - UPS (uninterruptible power supply) for short outages, generators for long. PDU (power distribution unit) for rack-level.
- **HVAC (Heating, Ventilation, Air Conditioning)** - data centers need cooling. Hot aisle / cold aisle layouts. Humidity matters (too dry = static; too humid = condensation).
- **Fire suppression** - water sprinklers damage equipment. Better: gas-based (FM-200, Inergen) or **clean agents** for data centers. Pre-action sprinkler systems delay water release.
- **Data center / closet** - locked, monitored, raised floor, fire suppression, environmental sensors.
- **Redundancy** - N+1 (one extra), 2N (full duplicate), 2N+1. RAID (Redundant Array of Inexpensive Disks) for storage redundancy.
- **MOU/MOA** - agreements with backup vendors, ISPs, cloud providers.

---

## Part 5 - Security Operations (Domain 5, ISC2 weight ~18%)

> **Memory anchors (palace Room 5: Bathroom, Domain 5).** Pick a bathroom you know. List 5 distinct loci in order: sink, medicine cabinet, bathtub, mirror, shower curtain, or whatever your bathroom actually has. For each Domain 5 anchor below, choose your own image to place at one locus; vivid and personal beats clever. Capture each choice as a gutter note.
>
> - **Data states** (at rest stored / in transit moving / in use processing in memory; protections rise from full-disk encryption through TLS/VPN/IPsec to TEE or homomorphic encryption, hardest at in-use)
> - **AES modes** (ECB insecure for multi-block / CBC chains with IV / CTR counter-based / GCM authenticated encryption in one pass)
> - **CPD sanitization** (NIST 800-88 ascending strength: Clear logical overwrite / Purge degauss or crypto-erase / Destroy physical shred)
> - **PKI flow** (CA signs certificates / RA verifies identity / certificate binds public key to identity / CRL or OCSP checks revocation)
> - **Phishing types** (smishing SMS / vishing voice / whaling executives / spear phishing one named target)
> - **SIEM / SOAR / SOC** (aggregates logs / automates response / is the team; do not confuse SOC with System-on-Chip)
>
> See Appendix D.2 for the elicitation framework.

Wei is at 75%. Moderate weight.

### 5.1 Data security

**Data states:**

- **At rest** - stored on disk, in databases, in backups. Protect with encryption (full-disk, file-level, database-level).
- **In transit** - moving over a network. Protect with TLS, IPsec, VPN.
- **In use** - actively being processed in memory. Hardest to protect; emerging techniques: TEE (trusted execution environment), homomorphic encryption.

### 5.2 Encryption - symmetric, asymmetric, hashing

> **Anchor reminder (Room 5 locus).** Pick one image that captures the **symmetric does not provide non-repudiation** rule (shared keys cannot prove who sent; only asymmetric digital signatures do). Place it at a Bathroom locus; capture as gutter note.

**Symmetric encryption.** One shared secret key for both encrypt and decrypt. Fast. Problem: how to share the key securely.

Common algorithms:
- **AES (Advanced Encryption Standard)** - 128, 192, 256-bit keys. Industry standard.
- **3DES (Triple DES)** - deprecated.
- **DES** - broken, do not use.
- **ChaCha20** - modern alternative to AES.

Modes: **ECB** (insecure for >1 block, leaks patterns), **CBC**, **CTR**, **GCM** (authenticated encryption, preferred).

**Asymmetric (public key) encryption.** Pair of keys: public (share) and private (keep secret). Solves the key distribution problem. Slow.

Common algorithms:
- **RSA** - based on factoring large primes. 2048-bit or 3072-bit minimum.
- **ECC (Elliptic Curve Cryptography)** - smaller keys, same strength. 256-bit ECC ≈ 3072-bit RSA.
- **Diffie-Hellman (DH)** - key exchange, not encryption. Establishes a shared secret over a public channel.
- **DSA / ECDSA** - digital signatures.

**Use patterns:**
- Encrypt with **recipient's public key** → only their private key decrypts (confidentiality).
- Sign with **your private key** → anyone with your public key can verify (authenticity, non-repudiation).
- Hybrid: use asymmetric to exchange a symmetric key, then symmetric for bulk data. This is how TLS works.

**Hashing.** One-way function: input → fixed-size digest. Cannot reverse. Used for integrity, password storage, digital signatures.

Algorithms:
- **MD5** - broken, do not use.
- **SHA-1** - deprecated, collisions found.
- **SHA-2 family** - SHA-256, SHA-384, SHA-512. Current standard.
- **SHA-3** - newer, different design (Keccak).
- **bcrypt / scrypt / Argon2** - password hashing (slow on purpose, salted, memory-hard).

**Salt + pepper.** Salt = random per-password value stored alongside the hash; defeats rainbow tables. Pepper = secret value not stored with the hash; adds another layer.

**HMAC (Hash-based Message Authentication Code).** Combines a hash with a secret key. Integrity + authenticity.

**Digital signature.** Sign hash of message with private key. Verifier hashes message, decrypts signature with public key, compares. Provides integrity, authenticity, non-repudiation.

**PKI (Public Key Infrastructure).** System to manage public keys. Components:

- **CA (Certificate Authority)** - issues and signs certificates.
- **RA (Registration Authority)** - verifies identity before CA issues.
- **Certificate** - binds a public key to an identity. X.509 standard.
- **CRL (Certificate Revocation List)** - list of revoked certs.
- **OCSP (Online Certificate Status Protocol)** - real-time revocation check.

### 5.3 Data handling lifecycle

**Classification.** Label data by sensitivity. Common scheme: Public, Internal, Confidential, Restricted. Government: Unclassified, Confidential, Secret, Top Secret.

**Labeling.** Mark data with its classification (header, watermark, metadata).

**Handling.** Rules per classification: who can access, how it must be stored, how it can be transmitted.

**Retention.** How long data must be kept. Legal/regulatory drivers (HIPAA, SOX, GDPR right to erasure).

**Destruction.** How data is disposed of:

- **Clearing** - overwrite with patterns. Sufficient for most uses; recoverable with effort.
- **Purging** - degaussing, more thorough overwriting. Recovery infeasible.
- **Destruction** - physical (shredding, incineration, pulverization). Required for highest sensitivity.

**Data sanitization** terms from NIST SP 800-88: Clear, Purge, Destroy.

### 5.4 Logging and monitoring

**What to log:** authentications (success and failure), authorizations, system events, security tool alerts, network flows, application events.

**Log management lifecycle:** generate → transmit → store → analyze → archive → dispose.

**SIEM (Security Information and Event Management).** Collects logs from many sources, correlates events, alerts on patterns. Splunk, Elastic SIEM, QRadar.

**SOAR (Security Orchestration, Automation, and Response).** Automates response playbooks on top of SIEM alerts.

**SOC (Security Operations Center).** Team that monitors SIEM, triages alerts, performs IR.

**NTP synchronization** matters: logs from different systems must share a time reference to be correlatable.

### 5.5 System hardening

**Configuration management** baseline:

- Disable unnecessary services and ports.
- Remove default accounts and passwords.
- Apply CIS Benchmarks or DISA STIGs (Security Technical Implementation Guides).
- Enable host-based firewall.
- Enable disk encryption.
- Apply patches.

**Patching:**

- **Vulnerability** - a weakness.
- **Exploit** - code that takes advantage of a vulnerability.
- **Patch** - vendor's fix.
- **CVE (Common Vulnerabilities and Exposures)** - unique ID for each known vulnerability.
- **CVSS (Common Vulnerability Scoring System)** - 0-10 severity score.
- **Patch Tuesday** - Microsoft's monthly patch release (second Tuesday).
- **Zero-day** - vulnerability not yet patched.

**Patch management process:** identify → test → deploy → verify → document. Test patches in a non-production environment first; production patches need change-management approval.

### 5.6 Best-practice security policies

ISC2 names these explicitly (Domain 5.3):

- **Data handling policy** - classification, labeling, retention, destruction, transmission rules.
- **Password policy** - length, complexity, age, history, lockout. Per NIST SP 800-63B (current guidance): length matters more than complexity; do not force periodic rotation; allow paste; check against breach corpora; lockout/throttle on guesses.
- **AUP (Acceptable Use Policy)** - what users may and may not do with org systems. Signed by all employees.
- **BYOD (Bring Your Own Device) policy** - rules for personal devices accessing org resources. MDM (Mobile Device Management), wipe on loss, separation of personal and corporate data.
- **Change management policy** - documentation, approval, testing, rollback procedures. Prevents unauthorized changes that introduce vulnerabilities.
- **Privacy policy** - how the org collects, uses, shares personal information.

### 5.7 Security awareness training

**Purpose:** humans are the weakest link. Training reduces social engineering success rate.

**Topics:**

- **Social engineering** - phishing, vishing, smishing, pretexting, tailgating.
- **Password protection** - no sharing, no writing down, no reuse, use a password manager.
- **Clean desk** - don't leave sensitive material visible when away from desk.
- **Incident reporting** - how to report a suspected incident.
- **Acceptable use** - AUP reminders.

**Cadence:** annual training mandatory; quarterly phishing simulations; new-hire training within first week.

---

## Appendix A - Quick-reference numbers and tables

### CIA triad expanded

| Property | Threat | Control |
|---|---|---|
| Confidentiality | Disclosure | Encryption, access control |
| Integrity | Alteration | Hashing, digital signatures, version control |
| Availability | Destruction, DoS | Redundancy, backups, BC/DR |

### NIST SP 800-61 r2 IR phases (canonical for CC exam)

1. Preparation
2. Detection and Analysis
3. Containment, Eradication, Recovery
4. Post-Incident Activity

### NIST CSF 2.0 six Functions (SP 800-61r3, newer reference)

Govern, Identify, Protect, Detect, Respond, Recover.

### Recovery objective relationship

`RTO + WRT ≤ MTD`. RPO is independent (data loss tolerance).

### BCP test ladder (lowest to highest realism)

Checklist → Tabletop → Simulation → Parallel → Full Cutover.

### Access control models

DAC (owner decides), MAC (system enforces labels), RBAC (role determines), ABAC (attributes determine), Rule-Based (rules independent of identity).

### OSI 7 layers (top-down)

Application, Presentation, Session, Transport, Network, Data Link, Physical.

### Common ports (top 20 to memorize)

22 SSH, 25 SMTP, 53 DNS, 80 HTTP, 110 POP3, 123 NTP, 143 IMAP, 389 LDAP, 443 HTTPS, 445 SMB, 636 LDAPS, 993 IMAPS, 995 POP3S, 3389 RDP, 21 FTP, 23 Telnet, 67/68 DHCP, 161 SNMP, 514 Syslog, 1433 MSSQL.

### Firewall types (simple to complex)

Packet filter → Stateful → Application-layer → Application-proxy → WAF → NGFW → UTM → Host-based.

### Cloud XaaS responsibility shift

IaaS (most customer) → PaaS → SaaS → FaaS (least customer).

### Encryption use patterns

- Confidentiality only → recipient's public key encrypts.
- Authenticity only → sender signs with own private key.
- Both → sign then encrypt.
- Bulk data → hybrid (asymmetric exchanges symmetric key).

### Hashing algorithms safe / unsafe

Safe: SHA-256, SHA-3, bcrypt, scrypt, Argon2. Avoid: MD5, SHA-1.

### Data destruction

Clear (overwrite) → Purge (degauss, advanced overwrite) → Destroy (physical).

---

## Appendix B - High-frequency miss patterns

These are the concepts that consistently trip CC candidates. Drill these.

1. **MAC** - Mandatory Access Control vs Media Access Control. Read the question twice.
2. **MFA categories** - two passwords are not MFA. Must be two *different* categories.
3. **RPO vs RTO** - RPO = data, RTO = time. Memorize the letter.
4. **Symmetric does not provide non-repudiation** - only asymmetric (digital signature) does, because shared keys cannot prove who sent.
5. **DAC vs MAC** - discretionary = owner decides; mandatory = system enforces.
6. **Stateful firewalls vs application firewalls** - stateful tracks connections; application reads protocol semantics.
7. **DMZ requires two firewalls** (or two interfaces on one firewall) - one between internet and DMZ, one between DMZ and internal.
8. **IPsec modes** - transport (payload only) vs tunnel (entire packet).
9. **ISC2 Code of Ethics** - protect society is canon 1; advance the profession is canon 4. If they conflict, earlier wins.
10. **Policy hierarchy** - policies are mandatory, guidelines are not.
11. **Hot site = fast + expensive; cold site = slow + cheap.** Warm site is in between.
12. **Containment in IR** - short-term (isolate) vs long-term (rebuild). Both happen in phase 3.
13. **Order of volatility** - collect RAM before powering down.
14. **Risk treatment options** - Avoid, Transfer, Mitigate, Accept. Four options, memorize.
15. **Default deny** is best practice; default allow is unsafe.

---

## Appendix C - Day-of-exam reminders

- Read every question twice. ISC2 likes "BEST" and "MOST" answers; multiple options may be technically correct.
- If two answers seem equally good, pick the one that's more specific or more aligned with ISC2 doctrine (NIST canon).
- 100 questions, 2 hours = 1.2 minutes per question. Mark and skip if stuck.
- 700/1000 to pass. You can miss ~25 questions and still pass.
- Bring photo ID. Arrive 30 minutes early. No notes, no phone in the testing room.

---

## Appendix D - Memory and recall techniques (palamedes-graded)

This appendix is built on a palamedes research pass against two recent peer-reviewed sources (one 2025 systematic review and meta-analysis on the method of loci, one 2025 state-of-the-art review on retrieval practice). Effect sizes and methodological caveats are tagged.

**Headline:** four techniques carry most of the load for a 13-day cram on heterogeneous rote-plus-application content: retrieval practice, spaced repetition, method of loci, and dual coding. Three more (interleaving, generation effect, sleep consolidation) compound the gains. Mnemonics and a memory palace handle the rote bedrock (port numbers, OSI layers, IR phase order, recovery-site ladder). Practice questions handle application-level transfer.

### D.1 Evidence summary (load-bearing claims tagged)

**Retrieval practice / testing effect** `[T1-verified, read:body]`
Recall from memory bolsters long-term retention more than re-reading the same material. The 2025 review of retrieval practice in the health professions traces the modern resurgence to Roediger and Karpicke 2006 and confirms two decades of converging evidence (Serra et al. 2025). The mechanism is the act of pulling information out of memory, not the act of being tested. **Practical form for CC: do the four mocks, score yourself, restudy the missed domain. The mocks are the primary intervention.**

**Transfer-appropriate processing** `[T1-verified, read:body]`
Retrieval practice is most beneficial when the practice FORM matches the test FORM (Morris et al. 1977, cited in Serra et al. 2025). The CC exam is 100 multiple-choice questions. Practice multiple-choice questions transfers better than flashcard recall transfers. **Practical: prioritize the mocks over the Anki deck if you have to pick one.** The Anki deck is supplementary; the mocks are the main course.

**Spaced repetition** `[T2-verified, read:abstract]` (Ebbinghaus 1885 + modern meta-analyses)
Reviewing material across spaced intervals beats massed review of the same total duration. Anki implements this automatically via the SM-2 algorithm. **Practical for CC cram: 15-25 minutes of Anki every weekday. Trust the algorithm; do not skip "easy" days.**

**Method of Loci (memory palace)** `[T1-verified, read:body]`
A mnemonic where to-be-remembered items are visualized at specific points along a familiar mental route. The 2025 systematic review and meta-analysis (Ondrej et al. 2025, British Journal of Psychology) reports moderate-to-large effect sizes for immediate serial recall vs rehearsal (d = 0.42 to 0.88, weighted across 13 included experiments). **Caveat:** overall GRADE rating is "very low to low" due to methodological issues across the included studies (publication bias, small samples, inconsistent implementation). The cognitive mechanisms are well-supported (dual coding, self-reference, spatial binding, elaborative processing); the magnitude estimates are uncertain. Practical capacity: about 2 items per locus before interference. **Use for ordered lists where ORDER MATTERS: OSI 7 layers top-down, NIST 800-61 IR phases in sequence, BCP test types ladder weakest-to-strongest.** Do not use for unordered conceptual material; the spatial scaffolding wastes effort.

**Dual coding** `[T2-verified, read:body]` (Paivio 1971; mechanism confirmed in MoL meta-analysis)
Encoding information in BOTH verbal and visual channels produces stronger memory traces than either alone. The method of loci is partly effective because it forces dual coding. **Practical for CC: when you see a new term, take 5 seconds to picture it as an image. AAL3 = a glowing hardware key. DMZ = a literal demilitarized buffer zone with sandbags.**

**Elaborative interrogation** `[T2-cited]` (Pressley et al. 1992)
Asking "why is this true?" or "how does this work?" during encoding deepens processing. **Practical: for each new CC fact, ask one why. Why does AH not encrypt? Because it provides integrity and authenticity without confidentiality, which lets ISPs and middleboxes still see the traffic for routing.**

**Interleaving** `[T2-cited]` (Rohrer and Taylor 2007; Bjork 1994)
Mixing categories during practice produces worse immediate performance but substantially better long-term transfer than blocked practice. **Practical: when you do Anki, do NOT filter to one tag. Let the deck shuffle across all five domains. When you re-study, jump between domains rather than re-reading one domain end-to-end.**

**Generation effect** `[T2-cited]` (Slamecka and Graf 1978)
Generating an answer yourself before checking it strengthens encoding more than reading the answer first. **Practical: for every mock question, commit to an answer in your head before looking at the options. Then read the options. The act of generating the wrong answer is itself a learning event.**

**Chunking** `[T2-cited]` (Miller 1956; revised down to ~4 by Cowan 2001)
Working memory holds 3 to 4 chunks of information at a time. Group items into chunks before trying to memorize them. **Practical: don't memorize 20 port numbers as 20 facts. Chunk them: file transfer (20, 21, 22, 23 + 80 web), mail (25, 110, 143), name services (53, 67, 123), Microsoft (135, 445, 3389), security (443, 636), management (161, 162).**

**Sleep consolidation** `[T2-cited]` (Walker 2017 + 2020s replications)
Memory consolidates during sleep, particularly during slow-wave and REM phases. Six to eight hours the night before an exam outperforms last-minute cramming on test-day performance. **Practical: lights out by 11pm the night before Mock 1, and the night before the exam. No new material after dinner on Friday May 29.**

### D.2 The CC memory palace

A memory palace works best when the route is HIGHLY familiar AND the imagery is yours. The 2-3x encoding advantage of Method of Loci over rote memorization comes from self-generated, vivid, personally-relevant imagery. Dictated imagery from someone else's brain is somebody else's pointer system; mapping it to yours is double work.

**Build your own, in five steps:**

1. **Pick five rooms you can walk through eyes-closed.** Your apartment is ideal. Childhood home, a familiar gym, or a frequent commute route work too. Each room holds one ISC2 domain in outline order; the Part-level blockquotes at the top of each Part name which room maps to which domain.
2. **List 5-8 distinct loci per room in walkthrough order.** Door, mat, table, shelf, window, whatever your actual room contains. The route is the index; order matters.
3. **For each Domain anchor, pick your own image to place at one locus.** The five Part-level blockquotes (one at the top of each Part 1 through 5) list the anchors for that Domain. Vivid and personal beats clever.
4. **Capture each choice as a gutter note on the daily page.** The note system anchors your imagery to the source section. Next time you re-read the section, your own image surfaces alongside.
5. **Walk the palace every night for the first three days, then twice a week.** First three walks are slow; verify each locus. Nights 4 through 10, the walk should take under three minutes.

**Why this works:**

- Self-generated imagery encodes 2-3x stronger than dictated imagery (Roediger 2006; Karpicke and Blunt 2011 testing-effect generalization).
- Spaced retrieval during the walk consolidates the binding (Bjork 1994 desirable difficulties).
- The route serves as both index and retrieval cue: walking activates the cue, the cue retrieves the image, the image retrieves the concept.

**If you cannot generate imagery on day one:** use the pre-built fallback in D.2.1 below as a STARTING point only. Substitute your own imagery within a day or two; the pre-built version exists to break the cold-start, not for long-term encoding.

#### D.2.1 Pre-built rooms (fallback, expect 2-3x weaker encoding)

Use this only if you cannot generate your own imagery. Replace each pre-built image with your own as soon as you find one; the dictated version is a scaffold, not the destination.

The five rooms, in walkthrough order (matching ISC2 domain order):

**Room 1: Front door and foyer = Domain 1 Security Principles**

- **The door itself** has three brass medallions arranged in a triangle: blue Confidentiality on the upper left, gold Integrity on the upper right, green Availability at the bottom. Below them, a small tarnished AAA badge for Authentication, Authorization, Accounting. Visualize ransomware as a giant chain dragging the green Availability medallion off the door.
- **The welcome mat** spells PASA in gold thread: Protect society, Act honorably, Service to principals, Advance the profession. The ISC2 Code of Ethics canon order. Earlier canons win when they conflict; the mat is positioned so you read top-to-bottom in priority order.
- **The coat rack with four hooks** labeled A T M A: Avoid, Transfer, Mitigate, Accept. The four risk treatments. Imagine an insurance contract dangling from the Transfer hook.
- **The hallway mirror** reflects a hand showing five fingers, each a authentication factor: pinky Know (small, a sticky note password), ring Where (jewelry, geo-fenced), middle Do (typing pattern), index Are (pointing at face for biometric), thumb Have (a hardware token gripped). The thumb-and-index pair are the most common combo - "have plus are."
- **The side table** has a calculator showing "SLE x ARO = ALE" and a stack of six papers in priority order top-to-bottom: Regulation, Policy, Standard, Procedure, Guideline, Baseline. The top three are mandatory in most contexts; the bottom three are recommended or implementation-level.

**Room 2: Living room = Domain 2 BC, DR, IR**

- **The couch with four cushions in a row** spells out NIST 800-61 IR phases: Preparation (cushion 1, a pristine first-aid kit), Detection and Analysis (cushion 2, a magnifying glass), Containment Eradication Recovery (cushion 3, a fire extinguisher), Post-Incident Activity (cushion 4, a notebook open to "lessons learned"). Mnemonic if the couch image fades: **P D C P** (Preparation, Detection, Containment, Post).
- **The wall TV** is split into four picture-in-picture quadrants: top-left a hard drive labeled RPO (data loss tolerance), top-right a clock labeled RTO (downtime tolerance), bottom-left a wall safe labeled MTD (absolute outer limit), bottom-right a checkbox labeled WRT (work recovery time, the post-RTO verification gap). The math hangs above: RTO + WRT must be less than or equal to MTD.
- **The fireplace** has four fires of decreasing intensity, left to right: Hot site (roaring fire, ready immediately), Warm site (steady fire, hours to ramp up), Cold site (just embers, days), Reciprocal site (a single matchstick, hope your neighbor agrees to share their fire).
- **The coffee table** has five books stacked weakest test on top: Checklist (a thin paperback), Tabletop (a board-game box), Simulation (a VR headset), Parallel (two identical books side by side), Full Cutover (an axe driven through the bottom book). The stack ascends in rigor and risk.
- **The bookshelf** is the order of volatility: top shelf glowing RAM sticks (volatile, collect first), middle shelf a hard drive (less volatile), bottom shelf a dusty archive tape (least volatile, collect last).

**Room 3: Bedroom = Domain 3 Access Control**

- **The four-poster bed** has each post embodied by a different access model: DAC post (the data owner sitting on it, deciding who can climb in), MAC post (a military soldier in dress uniform enforcing labels), RBAC post (a corporate name badge dangling), ABAC post (a clipboard with attributes - department, time, device posture).
- **The closet has three shelves** holding AAL levels: top shelf a glowing FIDO2 hardware key (AAL3), middle shelf two socks paired together (AAL2 multi-factor), bottom shelf one lonely sock (AAL1 single-factor password). The strength increases as you reach higher.
- **The dresser has three drawers** for biometric errors: top drawer "FRR Type 1" filled with rejected legitimate-customer packages (annoying but safe), bottom drawer "FAR Type 2" with a thief who slipped through (dangerous), middle drawer "CER" holding a perfect balance scale where FRR equals FAR.
- **The window** has metal bars in front (mantrap = preventive physical control), concrete bollards visible outside (defeats vehicle ramming), a motion-activated floodlight (deterrent control).
- **The nightstand** has a smartphone showing three identity-protocol icons: a three-headed dog (Kerberos with KDC for intranet auth), a folded XML document (SAML for federated SSO), a delegation pass card (OAuth for authorization).

**Room 4: Kitchen = Domain 4 Network Security (YOUR WEAKEST, MOST VIVID PALACE)**

- **The seven shelves of the tall pantry, top to bottom**, are the OSI 7 layers Application down to Physical. Top shelf full of red apples and a web browser tab (Application). Next shelf has a Powerpoint slide (Presentation). Next: poker chips spilling out (Session). Next: a delivery truck labeled TCP next to a paper airplane labeled UDP (Transport). Next: a globe with red routing lines drawn across it (Network). Next: bicycle-chain links and a MAC-address label printer (Data Link). Bottom shelf: coiled copper cable and an Ethernet jack (Physical). Mnemonic for verbal reinforcement: **All People Seem To Need Data Processing**.
- **The refrigerator door** has four big magnetic letters and a delivery-truck diorama: A (AH, authentication header, auth only), E (ESP, encapsulating security payload, encryption plus auth), I (IKE, internet key exchange). The diorama shows two delivery boxes: Transport mode (the box is small, just the contents are wrapped, original IP header visible) and Tunnel mode (the box is wrapped inside a larger box with a new shipping label).
- **The four stove burners** are firewall types of ascending sophistication: front-left packet filter (small flame, looks at headers only), front-right stateful (medium flame, with a notepad tracking connections), back-left application-proxy (large flame with a literal chef terminating each connection and starting a new one), back-right NGFW (all four burners merged into one giant flame, app awareness plus IPS plus threat intel).
- **The spice rack** has four bottles of private IP ranges in decreasing size: Class A 10.0.0.0/8 (giant bottle, biggest range), Class B 172.16.0.0/12 (medium bottle), Class C 192.168.0.0/16 (small bottle), and APIPA 169.254.0.0/16 (in a "DO NOT USE" bottle, link-local only).
- **The pantry attack-types shelf** has labeled jars: ARP spoofing jar (fake labels stuck on real cans), DNS poisoning jar (a tainted phonebook), MITM jar (a thief standing between two friends shaking hands), Evil Twin jar (two identical WiFi router models, one wearing a fake mustache).

**Room 5: Bathroom = Domain 5 Security Operations**

- **The sink with three toothbrushes** represents data states: toothbrush in cup labeled "at rest" (stored, protect with full-disk encryption), electric toothbrush mid-stroke labeled "in transit" (moving, protect with TLS/VPN/IPsec), toothbrush actively in someone's mouth labeled "in use" (being processed in memory, hardest to protect; TEE or homomorphic encryption).
- **The medicine cabinet** has four AES-mode bottles arranged left to right: ECB (clear glass, you can see repeating patterns through it, INSECURE for multi-block), CBC (chained bottles with a visible Initialization Vector tag), CTR (a bottle with a counter dial on top), GCM (a bottle with both a counter dial AND a wax authentication seal across the cap - authenticated encryption in one pass).
- **The bathtub has three sponges in a line**, NIST 800-88 sanitization in ascending strength: Clear sponge (light cleaning, logical overwrite), Purge sponge (industrial scrubber + degaussing wand attached), Destroy sponge (a literal hammer breaking ceramic next to a shredder).
- **The mirror** shows the PKI flow in reflection: a Certificate Authority signing a certificate, a Registration Authority verifying identity off to the side, the certificate itself binding a public key to an identity, and two receipts being checked at the door labeled CRL (a printed list) and OCSP (a real-time text-message check).
- **The shower curtain** has four cartoon phishing types: a text-message bubble (smishing), a phone ringing (vishing), a whale wearing a business suit and tie (whaling, targeting executives), a literal spear with one specific name carved on the shaft (spear phishing).

**Daily integration:** walk through the entire palace once per night before sleep, naming each locus and the concept it holds. First three nights, walk slowly and verify each locus. Nights 4 through 10, the walk should take under three minutes total.

### D.3 Domain-by-domain mnemonic quick reference

These are the high-leverage acronyms and acrostics for content that is order-sensitive or list-heavy. Drill these to automaticity.

**Domain 1 Security Principles**
- **CIA** confidentiality integrity availability. Add **N** for non-repudiation, **A** for authentication. CIANA when you need all five.
- **PASA** ISC2 ethics canon order: Protect society, Act honorably, Service to principals, Advance the profession.
- **ATMA** risk treatment: Avoid, Transfer, Mitigate, Accept.
- **Five fingers** authentication factors: Know (pinky), Have (thumb), Are (index), Where (ring), Do (middle).
- **SLE x ARO = ALE** the only quantitative risk equation the exam asks.
- **RPS-PGB** policy hierarchy: Regulation > Policy > Standard / Procedure > Guideline / Baseline.

**Domain 2 BC, DR, IR**
- **PDCP** NIST 800-61 r2 IR phases: Preparation, Detection and Analysis, Containment Eradication Recovery, Post-Incident Activity. (SANS uses PICERL: Preparation, Identification, Containment, Eradication, Recovery, Lessons learned. ISC2 references NIST, so use PDCP for the exam.)
- **GIPDRR** NIST CSF 2.0 Functions: Govern (NEW in 2.0), Identify, Protect, Detect, Respond, Recover. ISC2 references 800-61 r3 (April 2025) which maps IR to these.
- **HWCR** recovery sites in descending readiness: Hot, Warm, Cold, Reciprocal (and Mobile if mentioned).
- **CTSPF** BCP test types weakest to strongest: Checklist, Tabletop, Simulation, Parallel, Full Cutover.
- **Order of volatility:** RAM > network state > running processes > disk > archives. The "fast stuff first" rule.
- **RTO + WRT <= MTD** the recovery-objective inequality. RPO is independent; it measures data not time.

**Domain 3 Access Control**
- **DMRA** access control models in increasing flexibility: DAC, MAC, RBAC, ABAC. Or mnemonic sentence: "Dad's Military Rule, Anything's Better Allowed Carefully" - DAC, MAC, RBAC, ABAC.
- **FRR = Type 1 = false rejection** (legitimate user denied, annoying). **FAR = Type 2 = false acceptance** (impostor admitted, dangerous). **CER = crossover**, lower is better.
- **AAA**: Authentication (who you are), Authorization (what you can do), Accounting (what you did). Add **I** for Identification (claiming you are someone) at the front when ISC2 wants IAAA.
- **Need-to-know AND clearance.** Both required. Clearance is the ceiling; need-to-know is the specific item.

**Domain 4 Network Security**
- **APSTNDP** All People Seem To Need Data Processing - OSI layers Application down to Physical.
- **AEI**: AH provides Auth only, ESP provides Encryption + auth, IKE handles Key exchange. Memorize this trio together.
- **Transport vs Tunnel:** Transport keeps the original IP header (host-to-host). Tunnel wraps the entire packet in a new IP header (site-to-site).
- **Common ports chunk groups:**
  - **File-and-shell chunk:** 20/21 FTP data/control, 22 SSH/SFTP, 23 Telnet
  - **Mail chunk:** 25 SMTP, 110 POP3, 143 IMAP (HTTPS-wrapped versions add 100 to each: SMTPS 465 or 587, POP3S 995, IMAPS 993)
  - **Web chunk:** 80 HTTP, 443 HTTPS, 8080 alt-HTTP
  - **Name-service chunk:** 53 DNS, 67/68 DHCP, 123 NTP
  - **Microsoft chunk:** 135 RPC, 137-139 NetBIOS, 445 SMB, 3389 RDP
  - **Directory chunk:** 389 LDAP, 636 LDAPS
  - **Management chunk:** 161 SNMP query, 162 SNMP trap
- **Private IPv4:** 10/8 (Class A), 172.16/12 (Class B), 192.168/16 (Class C). Memorize as "ten - one seventy two dot sixteen - one ninety two dot one sixty eight."
- **WiFi escalation:** WEP (broken), WPA (transitional), WPA2 (AES-CCMP current minimum), WPA3 (SAE / Dragonfly, forward secrecy).

**Domain 5 Security Operations**
- **3 data states:** at Rest, in Transit, in Use. Mnemonic shape: RTU. Different protections at each.
- **ECB CBC CTR GCM** AES modes from least to most preferred: ECB never (patterns leak), CBC needs IV, CTR parallelizable, GCM authenticated.
- **CPD** NIST 800-88 sanitization, weakest to strongest: Clear, Purge, Destroy. Clear = logical overwrite. Purge = degauss or cryptographic erase. Destroy = physical shred or incinerate.
- **PKI components**: CA issues, RA verifies identity, certificate binds key to identity, CRL or OCSP checks revocation. Sequence: identity goes to RA, RA tells CA, CA issues cert, end users check CRL or OCSP.
- **SIEM / SOAR / SOC**: SIEM aggregates logs and correlates (the platform). SOAR automates response playbooks (the orchestration layer). SOC is the human team that runs both (the people). Don't confuse SOC with SoC = System on a Chip.

### D.4 Daily integration schedule (overlay on the 10-day cram)

| Day | Memory work (15-30 min, evening) | New techniques to apply |
|---|---|---|
| 1 (5/18) | Build Kitchen palace (Domain 4). Walk it once before sleep. | Method of loci, dual coding |
| 2 (5/19) | Walk Kitchen palace again. Add the refrigerator IPsec diorama and stove firewalls. | Chunking (group port numbers into 6 chunks) |
| 3 (5/20) | After Mock 1: identify 5 missed concepts, place each at a SPECIFIC locus in your palace where it fits. | Generation effect (commit before checking key) |
| 4 (5/21) | Build Living Room palace (Domain 2). Walk Kitchen + Living Room before sleep. | Elaborative interrogation (why does AH not encrypt?) |
| 5 (5/22) | After Mock 2: same palace-anchoring drill as Day 3. | Interleaving (mix Anki across all tags) |
| 6 (5/25) | Build Bedroom palace (Domain 3). Walk Kitchen, Living, Bedroom. | Sleep target: 8 hours |
| 7 (5/26) | Build Bathroom palace (Domain 5). Now walking all 4 rooms. | Walking takes about 4 minutes total. |
| 8 (5/27) | After Mock 3: re-anchor missed concepts at vacant loci. | Sleep target: 8 hours (cumulative consolidation) |
| 9 (5/28) | Build Foyer palace (Domain 1). All 5 rooms now anchored. | Final mnemonics drill before Mock 4. |
| 10 (5/29) | Walk all 5 rooms before bed. About 4-5 minutes total. Lights out by 10pm. | No new material. |
| 5/30 EXAM | Quick palace walk in your head while waiting in the testing-center lobby. | Test day. |

### D.5 Honest caveats

**The mocks beat the palace.** If you have only 60 minutes one evening, do a mock, not a palace walk. Retrieval practice is `[T1-verified]` with two decades of replication. The method of loci is `[T1-verified]` with effect sizes but a "very low to low" GRADE rating because the included studies have methodological problems. The mechanisms are well-supported; the magnitudes are noisy. Anchor your time accordingly.

**Mnemonics encode pointers, not understanding.** PASA tells you the canon ORDER but does not tell you what conflicts between canons look like in a question. The Kitchen palace tells you OSI Layer 4 is Transport but does not teach you why TCP is connection-oriented and UDP is not. Use the mnemonics as access paths to the underlying material, not as substitutes for it.

**Transfer-appropriate processing applies to you too.** The CC exam is multiple-choice. The mocks ARE the most transfer-appropriate practice. The palace is for the rote bedrock the mocks assume you already know.

**Memory palaces have a known capacity ceiling.** The 2025 MoL meta-analysis reports about 2 items per locus before interference. Your apartment has dozens of loci; you have plenty of room. But do not crowd a single locus with five concepts.

**Sleep matters more than one more re-read.** Walker 2017 + replications: sleep consolidates memory during slow-wave and REM phases. If it is 11pm and you are deciding between one more pass through Domain 4 versus going to bed, go to bed.

### D.6 Sources

`[T1-verified, read:body]` Ondrej J. et al. (2025). "The method of loci in the context of psychological research: A systematic review and meta-analysis." British Journal of Psychology. PMC12514325. https://pmc.ncbi.nlm.nih.gov/articles/PMC12514325/

`[T1-verified, read:body]` Serra M.J., Kaminske A.N., Nebel C., Coppola K.M. (2025). "The Use of Retrieval Practice in the Health Professions: A State-of-the-Art Review." PMC12292765. https://pmc.ncbi.nlm.nih.gov/articles/PMC12292765/

`[T2-cited]` Roediger H.L., Karpicke J.D. (2006). "Test-enhanced learning: Taking memory tests improves long-term retention." Psychological Science 17(3): 249-255. (Foundational; cited in both primary sources read above.)

`[T2-cited]` Morris C.D., Bransford J.D., Franks J.J. (1977). "Levels of processing versus transfer appropriate processing." Journal of Verbal Learning and Verbal Behavior 16: 519-533. (Foundational for transfer-appropriate processing; cited in Serra et al. 2025.)

`[T2-cited]` Paivio A. (1971). Imagery and Verbal Processes. (Dual coding theory; mechanism confirmed in Ondrej et al. 2025.)

`[T2-cited]` Miller G.A. (1956). "The magical number seven, plus or minus two." Psychological Review 63: 81-97. (Working memory capacity; revised down to ~4 by Cowan 2001.)

`[T2-cited]` Bjork R.A. (1994). "Memory and metamemory considerations in the training of human beings." In Metcalfe and Shimamura (eds.) Metacognition. (Desirable difficulties framing; cited in MoL meta-analysis.)

`[T2-cited]` Rohrer D., Taylor K. (2007). "The shuffling of mathematics problems improves learning." Instructional Science 35: 481-498. (Interleaving evidence.)

`[T2-cited]` Slamecka N.J., Graf P. (1978). "The generation effect: Delineation of a phenomenon." Journal of Experimental Psychology: Human Learning and Memory 4(6): 592-604. (Generation effect.)

`[T2-cited]` Walker M. (2017). Why We Sleep. (Sleep consolidation popular synthesis. Replication landscape for memory-consolidation claims is debated but stable for slow-wave sleep + declarative memory consolidation.)

`[priors-only]` Ebbinghaus H. (1885). Über das Gedächtnis. (Foundational forgetting curve. Verifiable but not body-read this session.)

End of study guide.

