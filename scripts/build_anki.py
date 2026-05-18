#!/usr/bin/env python3
"""Build ISC2 CC Anki deck (.apkg) of weak/unknown terms only.

Curation principle: skip terms a Staff QA engineer at a mid/large web company
(Mailchimp R&A) already knows from daily work. Focus on CC-specific definitions
that the exam tests and that aren't day-job vocabulary.

Output: /Users/wjia/Projects/cc-prep/anki/cc_glossary.apkg
"""

import genanki
import pathlib
import random

# Stable IDs so re-runs update the same deck/model rather than duplicating.
MODEL_ID = 1716014523
DECK_ID = 1716014524

OUT = pathlib.Path("/Users/wjia/Projects/cc-prep/anki/cc_glossary.apkg")
OUT.parent.mkdir(parents=True, exist_ok=True)

# Card format: (front_term, back_definition, [tags...])
# Tags: domain (D1-D5), category (acl, ir, bc, net, crypto, risk, pki, ethics)

CARDS = [
    # ---- Domain 1: Security Principles ----
    ("AAA model",
     "Authentication, Authorization, Accounting. The three pillars of access control. "
     "Sometimes IAAA when Identification is broken out as a separate first step.",
     ["D1", "acl"]),
    ("Non-repudiation",
     "A party cannot later deny having performed an action. Provided by digital signatures "
     "using the sender's private key (not by symmetric encryption or hashing alone).",
     ["D1", "crypto"]),
    ("Risk treatment options (4)",
     "Avoid (stop the activity), Transfer (insurance/contract), Mitigate (add controls), "
     "Accept (formally document and sign-off).",
     ["D1", "risk"]),
    ("SLE (Single Loss Expectancy)",
     "Dollar loss from one occurrence of a risk event. SLE = AssetValue x ExposureFactor.",
     ["D1", "risk"]),
    ("ARO (Annualized Rate of Occurrence)",
     "How many times per year a risk event is expected to happen.",
     ["D1", "risk"]),
    ("ALE (Annualized Loss Expectancy)",
     "Expected dollar loss per year from a given risk. ALE = SLE x ARO. The key quantitative "
     "risk metric the CC exam tests.",
     ["D1", "risk"]),
    ("Risk appetite vs residual risk",
     "Appetite = how much risk the org is willing to accept. Residual = what remains after "
     "controls are applied. Treatment of residual: accept (if <=appetite) or add more controls.",
     ["D1", "risk"]),
    ("Quantitative vs qualitative risk",
     "Quantitative uses dollar amounts (SLE x ARO = ALE). Qualitative uses High/Medium/Low "
     "ratings or expert opinion. Most orgs use both.",
     ["D1", "risk"]),
    ("Control categories (3) by type",
     "Administrative (policies, training), Technical (firewalls, encryption), Physical "
     "(locks, mantraps).",
     ["D1"]),
    ("Control functions (6+)",
     "Preventive (stop), Detective (alert), Corrective (fix), Recovery (restore), "
     "Deterrent (discourage), Compensating (alternative when primary infeasible).",
     ["D1"]),
    ("Deterrent vs Preventive control",
     "Deterrent discourages (warning sign, visible camera). Preventive blocks (locked door, "
     "MFA). A visible camera can be both.",
     ["D1"]),
    ("ISC2 Code of Ethics canon order",
     "1. Protect society, the common good, and infrastructure. 2. Act honorably, honestly, "
     "justly, responsibly, legally. 3. Provide diligent and competent service to principals. "
     "4. Advance and protect the profession. Earlier canons win when conflicts arise.",
     ["D1", "ethics"]),
    ("Policy hierarchy (top to bottom)",
     "Regulation (external mandatory) > Policy (internal mandatory broad) > Standard "
     "(internal mandatory specific) > Procedure (step-by-step) > Guideline (recommended). "
     "Baseline = minimum acceptable config.",
     ["D1"]),
    ("Authentication factors (5)",
     "Know (password), Have (token), Are (biometric), Where (location), Do (behavior/typing). "
     "MFA needs factors from DIFFERENT categories, not just multiple of one.",
     ["D1", "acl"]),

    # ---- Domain 2: BC, DR, IR ----
    ("BCP vs DRP vs IRP",
     "BCP = how business keeps operating (broadest). DRP = how IT systems are restored "
     "(subset of BCP). IRP = how security incidents are handled (narrowest, security-specific).",
     ["D2", "bc"]),
    ("BIA (Business Impact Analysis)",
     "The foundation document for BCP. Identifies mission-essential functions, dependencies, "
     "and sets recovery priorities. Done BEFORE setting RPO/RTO.",
     ["D2", "bc"]),
    ("RPO (Recovery Point Objective)",
     "How much DATA LOSS is tolerable. Drives backup frequency. RPO of 4hr means backups "
     "must capture every 4 hours or less.",
     ["D2", "bc"]),
    ("RTO (Recovery Time Objective)",
     "How long DOWNTIME is tolerable before systems must be back. Drives recovery-site "
     "choice and DR investment.",
     ["D2", "bc"]),
    ("MTD (Maximum Tolerable Downtime)",
     "Absolute outer limit before the business fails to recover. RTO + WRT <= MTD always.",
     ["D2", "bc"]),
    ("WRT (Work Recovery Time)",
     "Time AFTER RTO to verify data, reload, and resume actual work. Often forgotten when "
     "people quote only RTO.",
     ["D2", "bc"]),
    ("Hot site",
     "Fully equipped recovery facility with current data. Switchover in hours. Most expensive.",
     ["D2", "bc"]),
    ("Warm site",
     "Hardware and network in place but needs data restored from backup. Switchover in "
     "days. Middle cost.",
     ["D2", "bc"]),
    ("Cold site",
     "Empty space with power and network only. Weeks to activate. Cheapest.",
     ["D2", "bc"]),
    ("Reciprocal agreement",
     "Two organizations agree to host each other in a disaster. Cheap but rarely tested, "
     "may have insufficient capacity. Not a vendor contract.",
     ["D2", "bc"]),
    ("BCP test types (5, weakest to strongest)",
     "1. Checklist (read plan). 2. Tabletop (discussion). 3. Simulation (act it out, no "
     "switchover). 4. Parallel (failover runs alongside primary). 5. Full Interruption "
     "(actual cutover, highest risk and realism).",
     ["D2", "bc"]),
    ("NIST SP 800-61 IR phases (4)",
     "1. Preparation. 2. Detection and Analysis. 3. Containment, Eradication, and Recovery. "
     "4. Post-Incident Activity (lessons learned).",
     ["D2", "ir"]),
    ("Precursor vs Indicator",
     "Precursor = sign an incident MIGHT occur (e.g. recon scan). Indicator = sign an "
     "incident HAS occurred or is in progress (e.g. AV alert, anomaly).",
     ["D2", "ir"]),
    ("Order of volatility (collect first)",
     "RAM and CPU caches > network state and connections > running processes > disk image "
     "> archived backups. Most volatile FIRST.",
     ["D2", "ir"]),
    ("Chain of custody",
     "Documentation of who collected evidence, when, how, where stored, who accessed. "
     "Required for evidence admissibility in court. Failure = evidence ruled inadmissible.",
     ["D2", "ir"]),
    ("IR team models (3)",
     "Central (one team handles all). Distributed (teams in each business unit). "
     "Coordinating (central team advises distributed teams without direct response).",
     ["D2", "ir"]),
    ("Containment short-term vs long-term",
     "Short-term = isolate now (yank network cable, disable account). Long-term = rebuild "
     "systems from clean images, deploy permanent fixes before declaring resolved.",
     ["D2", "ir"]),
    ("CSF 2.0 Functions (6)",
     "Govern (NEW in 2.0), Identify, Protect, Detect, Respond, Recover. NIST SP 800-61 r3 "
     "(April 2025) reorganizes IR around these.",
     ["D2", "ir"]),

    # ---- Domain 3: Access Control ----
    ("DAC (Discretionary Access Control)",
     "The data owner decides who gets access. Example: Linux file permissions, Windows ACLs. "
     "Most common in commercial enterprises.",
     ["D3", "acl"]),
    ("MAC (Mandatory Access Control)",
     "System enforces access via security LABELS (Top Secret, Secret, Confidential). Owner "
     "cannot override. Common in military/government. Distinct from Media Access Control.",
     ["D3", "acl"]),
    ("RBAC (Role-Based Access Control)",
     "Access tied to job role (Marketing Analyst, DBA). User gets role, role gets permissions. "
     "Efficient when roles are stable and many users share each.",
     ["D3", "acl"]),
    ("ABAC (Attribute-Based Access Control)",
     "Dynamic policy combining user attributes, resource attributes, and environment "
     "attributes. Example: 'Allow if dept=Finance AND time=business-hours AND device=managed'.",
     ["D3", "acl"]),
    ("AAL1 / AAL2 / AAL3",
     "NIST SP 800-63B Authenticator Assurance Levels. AAL1 = single-factor (password). "
     "AAL2 = multi-factor. AAL3 = MFA with hardware-cryptographic authenticator (FIDO2 key).",
     ["D3", "acl"]),
    ("FRR (False Rejection Rate)",
     "Biometric Type 1 error: legitimate user is DENIED. Annoying but not a breach.",
     ["D3", "acl"]),
    ("FAR (False Acceptance Rate)",
     "Biometric Type 2 error: impostor is ACCEPTED. The dangerous error. Lower is better.",
     ["D3", "acl"]),
    ("CER (Crossover Error Rate)",
     "Point where FRR equals FAR. Lower CER = better biometric. The standard comparison metric.",
     ["D3", "acl"]),
    ("Least privilege",
     "Users get only the access NEEDED for their job, nothing more. Violated by privilege "
     "creep when role changes don't trigger access cleanup.",
     ["D3", "acl"]),
    ("SoD (Separation of Duties)",
     "No single person can complete a sensitive transaction alone. Example: developer cannot "
     "deploy to prod; deployer cannot edit code. Prevents single-insider fraud.",
     ["D3", "acl"]),
    ("Need-to-know",
     "Required IN ADDITION to clearance level. Clearance lets you SEE the level; need-to-know "
     "lets you see the SPECIFIC item. Both required.",
     ["D3", "acl"]),
    ("Privilege creep",
     "Users accumulate excess permissions over role changes if access isn't cleaned up at "
     "each transition. Mitigated by periodic access reviews.",
     ["D3", "acl"]),
    ("PAM (Privileged Access Management)",
     "Specialized controls for elevated accounts: password vaulting, session recording, "
     "just-in-time elevation. Distinct from regular IAM.",
     ["D3", "acl"]),
    ("Just-in-Time access",
     "Temporary privilege elevation only for the duration of a task, then automatically "
     "reverts. Reduces standing privilege.",
     ["D3", "acl"]),
    ("Mantrap",
     "Physical control: two doors in series, only one opens at a time. Defeats tailgating. "
     "Preventive physical control.",
     ["D3", "phys"]),
    ("Bollard",
     "Short vertical post preventing vehicle ramming attacks on buildings. Physical "
     "preventive control.",
     ["D3", "phys"]),
    ("Tailgating vs piggybacking",
     "Tailgating = unauthorized person follows authorized through a controlled door without "
     "consent. Piggybacking = same, but authorized person knowingly allows it.",
     ["D3", "phys"]),

    # ---- Domain 4: Network Security ----
    ("OSI 7 layers (top down)",
     "Application, Presentation, Session, Transport, Network, Data Link, Physical. "
     "Mnemonic top-down: All People Seem To Need Data Processing.",
     ["D4", "net"]),
    ("TCP 3-way handshake",
     "SYN -> SYN/ACK -> ACK. Establishes connection state. SYN flood attack exploits this "
     "by sending many SYNs and ignoring the responses.",
     ["D4", "net"]),
    ("Private IPv4 ranges (3)",
     "Class A: 10.0.0.0/8. Class B: 172.16.0.0/12. Class C: 192.168.0.0/16. "
     "(169.254.0.0/16 is APIPA, not private.) Non-routable on public internet.",
     ["D4", "net"]),
    ("IPsec AH vs ESP",
     "AH (Authentication Header) = integrity and auth only, NO encryption. ESP "
     "(Encapsulating Security Payload) = encryption PLUS auth. Use ESP for confidentiality.",
     ["D4", "net"]),
    ("IPsec Transport vs Tunnel mode",
     "Transport = encrypts payload only, original IP header kept (host-to-host). Tunnel = "
     "encrypts ENTIRE original packet and adds new IP header (site-to-site VPN).",
     ["D4", "net"]),
    ("IKE (Internet Key Exchange)",
     "IPsec key negotiation protocol. Phase 1 establishes IKE SA, Phase 2 establishes "
     "IPsec SAs. UDP 500/4500.",
     ["D4", "net"]),
    ("WAF (Web Application Firewall)",
     "Application-layer firewall for HTTP/HTTPS. Protects against SQLi, XSS, business "
     "logic abuse at Layer 7. Complements but doesn't replace network firewalls.",
     ["D4", "net"]),
    ("NGFW (Next-Generation Firewall)",
     "Stateful inspection + application awareness + IPS + threat intel + user identity. "
     "Modern firewall in one box.",
     ["D4", "net"]),
    ("DMZ (Demilitarized Zone)",
     "Subnet between internet and internal network hosting public-facing services (web, "
     "mail). Requires two firewalls OR two interfaces on one firewall.",
     ["D4", "net"]),
    ("VLAN",
     "Virtual LAN. Layer 2 logical segmentation of switch ports. Hosts in different VLANs "
     "cannot communicate without going through Layer 3 routing.",
     ["D4", "net"]),
    ("Micro-segmentation",
     "Fine-grained segmentation per workload (often per VM or container) rather than per "
     "subnet. Associated with zero-trust and cloud architectures.",
     ["D4", "net"]),
    ("Zero trust",
     "'Never trust, always verify' regardless of network location. No implicit trust for "
     "internal traffic. NIST SP 800-207.",
     ["D4", "net"]),
    ("NAC (Network Access Control)",
     "Verifies device POSTURE (patches, AV, config) before granting network access. "
     "Distinct from authentication; NAC is about device health.",
     ["D4", "net"]),
    ("CASB (Cloud Access Security Broker)",
     "Policy enforcement point between users and cloud services. Provides visibility, "
     "compliance, DLP, threat protection across SaaS apps.",
     ["D4", "net"]),
    ("HIDS vs NIDS",
     "HIDS = Host-based IDS, watches activity on one host (file changes, process behavior). "
     "NIDS = Network-based IDS, watches network traffic on a segment.",
     ["D4", "net"]),
    ("Signature vs Anomaly IDS",
     "Signature = matches known patterns (catches known threats, misses zero-days). "
     "Anomaly = baselines normal then alerts on deviations (catches novel attacks, higher "
     "false-positive rate).",
     ["D4", "net"]),
    ("IDS vs IPS",
     "IDS detects and alerts (out of band, passive). IPS detects and BLOCKS (in-line, "
     "active). IPS adds risk of false positives blocking legit traffic.",
     ["D4", "net"]),
    ("WEP / WPA / WPA2 / WPA3",
     "WEP = broken, never use. WPA = transitional, weak. WPA2 = AES-CCMP, current minimum. "
     "WPA3 = SAE/Dragonfly handshake, forward secrecy, defeats offline dictionary attacks.",
     ["D4", "net"]),
    ("Evil twin attack",
     "Rogue access point impersonating a legitimate SSID to capture credentials or perform "
     "MITM. Defeated by certificate-based WiFi auth or VPN.",
     ["D4", "net"]),
    ("ARP spoofing",
     "Attacker sends fake ARP replies to associate their MAC with another host's IP. Layer 2 "
     "MITM technique. Defeated by static ARP, port security, or DHCP snooping.",
     ["D4", "net"]),
    ("DNS poisoning / cache poisoning",
     "Corrupts DNS resolver cache so victims resolve hostnames to attacker IPs. Mitigated by "
     "DNSSEC.",
     ["D4", "net"]),
    ("Side-channel attack",
     "Extracts information from physical observation (timing, power consumption, "
     "electromagnetic emissions, acoustics) rather than algorithmic weaknesses.",
     ["D4", "net"]),
    ("Worm vs Virus vs Trojan",
     "Virus needs a host file and user action to spread. Worm self-propagates without a host. "
     "Trojan appears legitimate but hides malicious payload, no self-propagation.",
     ["D4", "net"]),
    ("Logic bomb",
     "Malicious code that triggers on a condition (date, event, user action). Often planted "
     "by insiders.",
     ["D4", "net"]),
    ("C2 (Command and Control)",
     "Channel a botnet or APT uses to receive instructions from operator. Detection target "
     "for egress monitoring and DNS analytics.",
     ["D4", "net"]),

    # ---- Domain 5: Security Operations ----
    ("Symmetric vs Asymmetric",
     "Symmetric = same key for encrypt and decrypt (AES, ChaCha20). Fast, key-distribution "
     "problem. Asymmetric = key PAIR, public/private (RSA, ECC). Slow, solves key distribution. "
     "Asymmetric provides non-repudiation; symmetric cannot.",
     ["D5", "crypto"]),
    ("AES modes: ECB / CBC / CTR / GCM",
     "ECB = insecure for multi-block (patterns leak). CBC = chained, needs IV. CTR = counter, "
     "parallelizable. GCM = authenticated encryption, confidentiality + integrity in one pass. "
     "Prefer GCM.",
     ["D5", "crypto"]),
    ("Hashing properties",
     "One-way (cannot reverse), deterministic (same input -> same output), collision-resistant. "
     "Use SHA-256/SHA-3 for general, bcrypt/Argon2 for passwords. Never MD5 or SHA-1.",
     ["D5", "crypto"]),
    ("Salt vs Pepper",
     "Salt = per-password random value stored WITH the hash. Defeats rainbow tables. "
     "Pepper = secret value NOT stored with the hash, added to all passwords. Defense in depth.",
     ["D5", "crypto"]),
    ("Digital signature flow",
     "Sender hashes message, encrypts hash with their PRIVATE key. Receiver decrypts with "
     "sender's PUBLIC key, hashes the message themselves, compares. Provides integrity, "
     "authenticity, non-repudiation.",
     ["D5", "crypto"]),
    ("PKI components",
     "CA (Certificate Authority issues certs), RA (Registration Authority verifies identity), "
     "Certificate (binds public key to identity), CRL (revocation list), OCSP (real-time "
     "revocation check).",
     ["D5", "pki"]),
    ("CRL vs OCSP",
     "CRL = signed list of revoked certs published by CA, downloaded periodically. "
     "OCSP = real-time query to check one cert's status. OCSP stapling = server prefetches "
     "OCSP response, attaches to TLS handshake.",
     ["D5", "pki"]),
    ("Data states (3)",
     "At rest (stored on disk, protect with FDE), In transit (moving over network, protect "
     "with TLS/IPsec/VPN), In use (in memory being processed, hardest to protect; TEE/SGX).",
     ["D5", "crypto"]),
    ("NIST 800-88 data sanitization (3)",
     "Clear = logical (overwrite, reformat). Purge = stronger (degauss, multi-pass overwrite "
     "or cryptographic erase). Destroy = physical (shred, incinerate, pulverize). Strength "
     "increases left to right.",
     ["D5"]),
    ("Degaussing",
     "Application of strong magnetic field to magnetic media (HDDs, tapes) to render data "
     "unrecoverable. Does NOT work on SSDs. NIST 800-88 Purge method for magnetic media.",
     ["D5"]),
    ("SIEM vs SOAR vs SOC",
     "SIEM = platform aggregating logs and correlating alerts. SOAR = automation playbooks "
     "on top of SIEM. SOC = the human team operating both. Distinct from SoC (System on Chip).",
     ["D5"]),
    ("CVE vs CVSS",
     "CVE = unique identifier for one specific vulnerability (CVE-2024-12345). "
     "CVSS = 0-10 severity score for that vulnerability (9.8 = critical).",
     ["D5"]),
    ("EDR vs XDR",
     "EDR = Endpoint Detection and Response, behavioral analytics on endpoints. XDR = "
     "Extended D&R, correlates across endpoints, network, cloud, email.",
     ["D5"]),
    ("DLP (Data Loss Prevention)",
     "Detects and blocks sensitive data from leaving the organization. Endpoint DLP, "
     "network DLP, cloud DLP. Requires data classification to work effectively.",
     ["D5"]),
    ("Current NIST 800-63B password guidance",
     "LENGTH over complexity (8+ minimum, longer better). NO forced periodic rotation "
     "(rotate only on compromise). Check against breach corpora. Allow all printable chars. "
     "Don't use 'security questions'.",
     ["D5"]),

    # ---- Cross-domain: NIST publications Wei should know by number ----
    ("NIST SP 800-12",
     "An Introduction to Information Security. Foundational concepts. Domain 1 reference.",
     ["nist"]),
    ("NIST SP 800-34",
     "Contingency Planning Guide for Federal Information Systems. BIA, BCP, DRP framework. "
     "Domain 2.",
     ["nist", "D2"]),
    ("NIST SP 800-41",
     "Guidelines on Firewalls and Firewall Policy. Packet filter / stateful / app firewall "
     "types and DMZ architectures. Domain 4.",
     ["nist", "D4"]),
    ("NIST SP 800-53",
     "Security and Privacy Controls catalog. The control families (AC, AU, CM, IR, etc.). "
     "Foundation of US federal security.",
     ["nist"]),
    ("NIST SP 800-61",
     "Computer Security Incident Handling Guide. The 4-phase IR lifecycle the CC exam tests. "
     "r2 is canonical; r3 (April 2025) reframes around CSF 2.0.",
     ["nist", "D2", "ir"]),
    ("NIST SP 800-63B",
     "Digital Identity Guidelines: Authentication. AAL1/2/3 levels, password guidance.",
     ["nist", "D3", "acl"]),
    ("NIST SP 800-77",
     "Guide to IPsec VPNs. Transport vs tunnel, AH vs ESP, IKE.",
     ["nist", "D4"]),
    ("NIST SP 800-88",
     "Guidelines for Media Sanitization. Clear / Purge / Destroy levels.",
     ["nist", "D5"]),
    ("NIST SP 800-115",
     "Technical Guide to Information Security Testing and Assessment. Pen-test methodology.",
     ["nist"]),
    ("NIST SP 800-207",
     "Zero Trust Architecture. The canonical zero-trust reference.",
     ["nist", "D4"]),

    # ---- Less-common but exam-tested odds and ends ----
    ("MOU vs MOA vs SLA",
     "MOU (Memorandum of Understanding) = informal agreement of intent. MOA (Memorandum of "
     "Agreement) = formal but often non-binding. SLA = service-level commitments with "
     "metrics. ISA (Interconnection Security Agreement) = technical security expectations.",
     ["D1"]),
    ("Type 1 vs Type 2 hypervisor",
     "Type 1 (bare metal) runs directly on hardware (ESXi, Hyper-V, KVM). Type 2 (hosted) "
     "runs on top of an OS (VMware Workstation, VirtualBox). Type 1 more secure.",
     ["D4"]),
    ("Cloud responsibility (shared)",
     "IaaS: customer responsible for OS+, provider for hardware/hypervisor. PaaS: customer "
     "for app+data, provider for runtime+OS+infra. SaaS: customer for data+identity, provider "
     "for everything else.",
     ["D4"]),
    ("RAID levels",
     "RAID 0 = stripe (speed, no redundancy). RAID 1 = mirror (redundancy, half capacity). "
     "RAID 5 = stripe + parity (one disk failure). RAID 6 = stripe + 2 parity (two disk "
     "failures). RAID 10 = mirror + stripe (best perf + redundancy).",
     ["D2"]),
    ("UPS vs Generator",
     "UPS = battery, seconds to minutes of bridge power. Generator = fuel-powered, hours to "
     "days. UPS bridges the gap until generator starts. Both needed for sustained outages.",
     ["D2"]),
    ("Clean-desk policy",
     "Users clear sensitive material from desks when away. Mitigates visual data exposure, "
     "shoulder surfing, and after-hours snooping.",
     ["D5"]),
    ("Smishing / Vishing / Whaling / Spear phishing",
     "Smishing = SMS phishing. Vishing = voice phishing. Whaling = phishing targeting "
     "executives. Spear phishing = phishing targeting a specific individual.",
     ["D5"]),
    ("Pretexting",
     "Social engineering using a fabricated scenario to extract information. 'I'm from IT, "
     "I need your password to reset the system.' Often pairs with phishing.",
     ["D5"]),
]


def main():
    model = genanki.Model(
        MODEL_ID,
        "CC Glossary",
        fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Tags"}],
        templates=[{
            "name": "Card 1",
            "qfmt": '<div class="front">{{Front}}</div>',
            "afmt": '<div class="front">{{Front}}</div><hr>'
                    '<div class="back">{{Back}}</div>'
                    '<div class="tags">{{Tags}}</div>',
        }],
        css="""
.card { font-family: -apple-system, system-ui, sans-serif; font-size: 18px;
        line-height: 1.5; text-align: left; color: #2a2a2a;
        background: #f7f3e8; padding: 1.5rem; }
.front { font-weight: 700; font-size: 22px; color: #3a5a40; margin-bottom: 0.5rem; }
.back { margin-top: 0.5rem; }
.tags { margin-top: 1rem; font-size: 13px; color: #888; font-style: italic; }
hr { border: 0; border-top: 1px solid #c9b890; margin: 1rem 0; }
""",
    )

    deck = genanki.Deck(DECK_ID, "ISC2 CC - weak/unknown terms")

    for front, back, tags in CARDS:
        note = genanki.Note(model=model, fields=[front, back, " ".join(tags)], tags=tags)
        deck.add_note(note)

    genanki.Package(deck).write_to_file(str(OUT))
    print(f"wrote {OUT}")
    print(f"cards: {len(CARDS)}")
    print(f"tags used: {sorted({t for _, _, ts in CARDS for t in ts})}")


if __name__ == "__main__":
    main()
