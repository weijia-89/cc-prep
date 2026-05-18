#!/usr/bin/env python3
"""Render the ISC2 CC study guide corpus + 10 daily cram pages as solarpunk HTML.

Adapts /Users/wjia/Projects/qa-prep/scripts/render_html.py for the CC cram cadence.
Output: study_guide/daily/{index,day-NN,guide,exams,mocks2,glossary}.html

Usage:
    /Users/wjia/Projects/.venv-pdf/bin/python scripts/render_html.py
"""

from __future__ import annotations

import re
from pathlib import Path
from html import escape as h

from jinja2 import Template
from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.anchors.index import slugify as _default_slug
from mdit_py_plugins.attrs import attrs_plugin

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "study_guide" / "daily"

SG_MD = ROOT / "study_guide" / "CC_Study_Guide.md"
PE_MD = ROOT / "study_guide" / "PRACTICE_EXAMS.md"
PE2_MD = ROOT / "study_guide" / "PRACTICE_EXAMS_2.md"
GLOS_MD = ROOT / "study_guide" / "glossary.md"

DEFAULT_START = "2026-05-18"  # Monday
EXAM_DATE = "2026-05-30"

# === 10-day CC cram curriculum ===
# Weighted: D4 = 3 days, D2 = 2 days, D3 = 1.5 days, D5 = 1.5 days, D1 = 1 day, Mocks/review = 1 day.
# Each citation: (label, gloss). Each link: (label, href).

DAYS = [
    # --- Week 1 (May 18-22): heavy on Domain 4 first, then Domain 2 ---
    dict(w=1, d=1, title="Domain 4 Network Security part 1: OSI, TCP/IP, ports",
        subtitle="<strong>Acronyms used today:</strong> ISC2 (International Information System Security Certification Consortium), CC (Certified in Cybersecurity), OSI (Open Systems Interconnection), TCP/IP (Transmission Control Protocol / Internet Protocol), NIST SP (National Institute of Standards and Technology Special Publication), IPv4/IPv6 (Internet Protocol version 4 / version 6).",
        focus="You are at 55 percent on Network Security. Frontload it. Today: memorize the OSI 7 layers top-to-bottom (Application, Presentation, Session, Transport, Network, Data Link, Physical) and the top-20 common ports. Use the mnemonic All People Seem To Need Data Processing. Skim NIST SP 800-41 sections 2.1.1-2.1.3 for packet-filter vs stateful vs application firewalls. Tonight: walk Room 4 (Kitchen, Domain 4) slowly; this room is your weakest.",
        citations=[
            ("ISC2 CC Outline 4.1", "OSI and TCP/IP models, IPv4 vs IPv6, ports are all named explicitly"),
            ("NIST SP 800-41 r1 sec 2.1.1", "packet filtering is the most basic firewall technology; modern firewalls layer it under stateful inspection"),
            ("Roediger and Karpicke 2006", "spaced retrieval beats massed re-reading for delayed recall"),
        ],
        links=[("Study Guide Part 4", "guide.html#part-4-network-security-domain-4-isc2-weight-24-depth-pass"),
               ("Glossary: ports and protocols", "glossary.html"),
               ("Memory palace walkthrough", "guide.html#d2-the-cc-memory-palace")]),

    dict(w=1, d=2, title="Domain 4 part 2: TLS, IPsec, VPN, network threats",
        subtitle="<strong>Acronyms used today:</strong> ISC2 CC (Certified in Cybersecurity, by the International Information System Security Certification Consortium), TLS (Transport Layer Security), IPsec (Internet Protocol Security), VPN (Virtual Private Network), AH (Authentication Header), ESP (Encapsulating Security Payload), DoS/DDoS (Denial of Service / Distributed DoS), MITM (man-in-the-middle), ARP (Address Resolution Protocol), DNS (Domain Name System), NIST SP (National Institute of Standards and Technology Special Publication).",
        focus="Today: IPsec Transport vs Tunnel modes (payload only vs entire packet plus new IP header), AH vs ESP (auth-only vs encryption-plus-auth), and the named attack vocabulary (DoS/DDoS, MITM, ARP/DNS spoofing, evil twin, side-channel). Practice naming each: virus needs a host, worm self-propagates, Trojan hides in legitimate-looking software. Tonight: walk Room 4 again, focusing on the fridge (IPsec) and stove burners (firewalls).",
        citations=[
            ("ISC2 CC Outline 4.2", "network threats and attacks list is canonical; memorize each by name"),
            ("NIST SP 800-77 r1", "IPsec VPN modes and protocols; transport vs tunnel is the most-tested distinction"),
            ("Bjork 1994", "the desirable-difficulties principle: harder retrieval produces stronger encoding"),
        ],
        links=[("Study Guide 4.4 Network threats", "guide.html#44-network-threats-and-attacks-isc2-named-list"),
               ("Study Guide 4.8 VPNs", "guide.html#48-vpns-virtual-private-networks"),
               ("Memory palace walkthrough", "guide.html#d2-the-cc-memory-palace")]),

    dict(w=1, d=3, title="Domain 4 part 3 plus Mock 1 (full 100 questions, 2 hours)",
        subtitle="<strong>Acronyms used today:</strong> ISC2 CC (Certified in Cybersecurity, by the International Information System Security Certification Consortium), DMZ (demilitarized zone), VLAN (Virtual Local Area Network), NAC (Network Access Control), NIST SP (National Institute of Standards and Technology Special Publication).",
        focus="Morning: read Study Guide 4.6 firewalls and 4.7 architectures (DMZ, VLAN, subnet, micro-segmentation, zero trust, NAC). Afternoon: take Mock 1 timed at 2 hours. Score yourself. Anything below 65 means re-study that domain tomorrow morning before continuing. Tonight: full 5-room walk; Mock 1 will show which loci are weakest, reinforce those tomorrow.",
        citations=[
            ("ISC2 CC Outline 4.3", "network security infrastructure including on-premises, design, and cloud"),
            ("NIST SP 800-41 r1 sec 3", "DMZ architecture requires two firewalls or two interfaces on one firewall"),
            ("Karpicke and Blunt 2011", "practice testing is more effective than concept mapping for long-term retention"),
        ],
        links=[("Mock Exam 1", "exams.html#mock-1-100-questions-isc2-weighted"),
               ("Study Guide 4.6 Firewalls", "guide.html#46-firewalls-types-and-where-they-sit"),
               ("Memory palace walkthrough", "guide.html#d2-the-cc-memory-palace")]),

    dict(w=1, d=4, title="Domain 2 Incident Response: NIST SP 800-61 4-phase lifecycle",
        subtitle="<strong>Acronyms used today:</strong> ISC2 CC (Certified in Cybersecurity, by the International Information System Security Certification Consortium), IR (Incident Response), NIST SP (National Institute of Standards and Technology Special Publication), CSF (Cybersecurity Framework), RAM (Random Access Memory).",
        focus="You are at 60 percent on this domain. Today: memorize the 4 IR phases verbatim (Preparation, Detection and Analysis, Containment Eradication and Recovery, Post-Incident Activity). Know the distinction: precursor (sign incident might occur) vs indicator (sign incident has occurred). Order of volatility: RAM before disk before archives. Chain of custody preserves admissibility. Tonight: walk Room 2 (Living Room, Domain 2); verify couch cushion order matches NIST 800-61 IR phases.",
        citations=[
            ("ISC2 CC Outline 2.3", "incident response purpose, importance, and components are exam-tested"),
            ("NIST SP 800-61 r2", "the canonical 4-phase model the CC exam references; r3 was published April 2025 but the exam outline points at r2"),
            ("NIST SP 800-61 r3", "newer reframing maps the activities to CSF 2.0 Functions Govern Identify Protect Detect Respond Recover"),
        ],
        links=[("Study Guide 2.6 IR lifecycle", "guide.html#26-incident-response-lifecycle"),
               ("Study Guide 2.8 Evidence handling", "guide.html#28-evidence-handling-chain-of-custody"),
               ("Memory palace walkthrough", "guide.html#d2-the-cc-memory-palace")]),

    dict(w=1, d=5, title="Domain 2 BC plus DR: RPO RTO MTD WRT, recovery sites, plus Mock 2",
        subtitle="<strong>Acronyms used today:</strong> ISC2 CC (Certified in Cybersecurity, by the International Information System Security Certification Consortium), BC (Business Continuity), DR (Disaster Recovery), BCP/DRP/IRP (BC Plan / DR Plan / Incident Response Plan), RPO (Recovery Point Objective: data-loss tolerance), RTO (Recovery Time Objective: downtime tolerance), MTD (Maximum Tolerable Downtime), WRT (Work Recovery Time), BIA (Business Impact Analysis), NIST SP (National Institute of Standards and Technology Special Publication).",
        focus="Morning: BCP plus DRP vs IRP scope distinctions, the four recovery objectives (RPO data, RTO downtime, MTD outer limit, WRT post-RTO verification), and the recovery site ladder (hot fast and expensive, warm middle, cold slow and cheap, reciprocal mutual). BCP test types: Checklist, Tabletop, Simulation, Parallel, Full Cutover. Afternoon: Mock 2 timed. Tonight: walk Room 2 again, fireplace and coffee table.",
        citations=[
            ("ISC2 CC Outline 2.1 and 2.2", "BC and DR purpose importance and components"),
            ("NIST SP 800-34 r1 sec 3", "BIA is the foundation: determine processes, identify resources, set recovery priorities"),
            ("Roediger 2006 testing effect", "two mocks in one week beats one mock plus more reading"),
        ],
        links=[("Mock Exam 2", "exams.html#mock-2-100-questions-isc2-weighted-different-angles"),
               ("Study Guide 2.3 Recovery objectives", "guide.html#23-recovery-objectives-the-four-numbers-isc2-tests"),
               ("Study Guide 2.4 Recovery sites", "guide.html#24-recovery-sites-the-four-options"),
               ("Memory palace walkthrough", "guide.html#d2-the-cc-memory-palace")]),

    # --- Week 2 (May 25-29): Domain 3, then Domain 5, then Domain 1 + final mocks ---
    dict(w=2, d=1, title="Domain 3 Access Control: DAC, MAC, RBAC, ABAC, AAA, MFA",
        subtitle="<strong>Acronyms used today:</strong> ISC2 CC (Certified in Cybersecurity, by the International Information System Security Certification Consortium), DAC (Discretionary Access Control), MAC (Mandatory Access Control here; also Media Access Control in networking), RBAC (Role-Based Access Control), ABAC (Attribute-Based Access Control), AAA (Authentication, Authorization, Accounting), MFA (Multi-Factor Authentication), FRR (False Reject Rate, biometric Type 1), FAR (False Accept Rate, biometric Type 2), AAL (Authenticator Assurance Level), NIST SP (National Institute of Standards and Technology Special Publication).",
        focus="Read the access control models table until you can produce each from memory. DAC = owner decides. MAC = system enforces labels. RBAC = role tied. ABAC = attributes. Memorize the 5 authentication factors (know, have, are, where, do) and that MFA needs different categories, not just multiple factors. Drill Type 1 (FRR) vs Type 2 (FAR) biometric errors. Tonight: walk Room 3 (Bedroom, Domain 3); bed posts hold DMRA models, closet shelves hold AAL levels.",
        citations=[
            ("ISC2 CC Outline 3.1 and 3.2", "physical and logical access controls both tested explicitly"),
            ("NIST SP 800-63B sec 4", "AAL1 single-factor, AAL2 multi-factor, AAL3 hardware-cryptographic"),
            ("Bjork interleaving", "mix access-control vocab with network terms today; transfer improves"),
        ],
        links=[("Study Guide Part 3", "guide.html#part-3-access-control-concepts-domain-3-isc2-weight-22"),
               ("Glossary AAA AAL ABAC", "glossary.html#a"),
               ("Memory palace walkthrough", "guide.html#d2-the-cc-memory-palace")]),

    dict(w=2, d=2, title="Domain 3 wrap plus Domain 5 part 1: encryption, hashing, PKI",
        subtitle="<strong>Acronyms used today:</strong> ISC2 CC (Certified in Cybersecurity, by the International Information System Security Certification Consortium), SSO (Single Sign-On), SAML (Security Assertion Markup Language), OAuth (Open Authorization), OIDC (OpenID Connect), AES (Advanced Encryption Standard), RSA (Rivest-Shamir-Adleman), ECC (Elliptic Curve Cryptography), SHA (Secure Hash Algorithm), PKI (Public Key Infrastructure).",
        focus="Morning: finish Domain 3 (SSO and federation via SAML, OAuth, OIDC, Kerberos). Afternoon: Domain 5 encryption (AES symmetric, RSA and ECC asymmetric, SHA-2/SHA-3/bcrypt hashing). Memorize the use patterns: confidentiality = recipient public key, authenticity = sender private key, hybrid = asymmetric exchanges symmetric. Non-repudiation requires asymmetric. Tonight: walk Rooms 3 and 5.",
        citations=[
            ("ISC2 CC Outline 5.1", "encryption including symmetric asymmetric and hashing tested explicitly"),
            ("Study Guide Appendix B miss-pattern 4", "symmetric does NOT provide non-repudiation; shared keys cannot prove sender"),
            ("Study Guide Appendix B miss-pattern 1", "Mandatory Access Control vs Media Access Control: read questions carefully"),
        ],
        links=[("Study Guide 5.2 Encryption", "guide.html#52-encryption-symmetric-asymmetric-hashing"),
               ("Study Guide 3.6 SSO and federation", "guide.html#36-sso-single-sign-on-and-federation"),
               ("Memory palace walkthrough", "guide.html#d2-the-cc-memory-palace")]),

    dict(w=2, d=3, title="Domain 5 part 2: data lifecycle, logging, hardening, policies, plus Mock 3",
        subtitle="<strong>Acronyms used today:</strong> ISC2 CC (Certified in Cybersecurity, by the International Information System Security Certification Consortium), NIST SP (National Institute of Standards and Technology Special Publication), SIEM (Security Information and Event Management), SOAR (Security Orchestration, Automation and Response), SOC (Security Operations Center), CIS (Center for Internet Security), DISA STIG (Defense Information Systems Agency Security Technical Implementation Guide), AES (Advanced Encryption Standard).",
        focus="Morning: data classification, labeling, retention, destruction (Clear, Purge, Destroy per NIST SP 800-88). SIEM aggregates, SOAR automates, SOC operates. CIS Benchmarks and DISA STIGs for hardening. Current NIST 800-63B password guidance: length over complexity, no forced rotation, check breach corpora. Afternoon: Mock 3 (weighted toward your weak Domains 2 and 4). Score yourself. Tonight: walk Room 5 (Bathroom, Domain 5); sink toothbrushes hold data states, medicine cabinet holds AES modes.",
        citations=[
            ("ISC2 CC Outline 5.1 through 5.4", "data security, hardening, policies, awareness training all on the exam"),
            ("NIST SP 800-88", "data sanitization terms Clear Purge Destroy in ascending strength"),
            ("Practice Exams 2", "Mock 3 is weighted toward Domain 4 (35 questions) and Domain 2 (25 questions)"),
        ],
        links=[("Mock Exam 3", "mocks2.html#mock-3-100-questions-weighted-toward-weak-domains"),
               ("Study Guide 5.3 Data lifecycle", "guide.html#53-data-handling-lifecycle"),
               ("Memory palace walkthrough", "guide.html#d2-the-cc-memory-palace")]),

    dict(w=2, d=4, title="Domain 1 light review plus glossary memorization plus Mock 4",
        subtitle='<strong>Acronyms used today:</strong> ISC2 CC (Certified in Cybersecurity, by the International Information System Security Certification Consortium). Glossary memorization day: see <a href="glossary.html">glossary</a> for the full initialism list.',
        focus="Morning: speed-read Part 1 (you are at 87 percent already). Memorize the ISC2 Code of Ethics canon order (Protect society first, Act honorably, Provide service, Advance the profession last). Drill the policy hierarchy: Regulation, Policy, Standard, Procedure, Guideline, Baseline. Risk treatment: Avoid, Transfer, Mitigate, Accept. Afternoon: Mock 4 (also weighted toward weak domains). Final score check. Tonight: walk Room 1 (Foyer, Domain 1).",
        citations=[
            ("ISC2 CC Outline 1.4", "ISC2 Code of Ethics canons are tested in order; earlier canons win when they conflict"),
            ("Study Guide Appendix B miss-pattern 9", "the canon order is the #9 high-frequency miss pattern"),
            ("Practice Exams 2", "Mock 4 is the final cram simulation"),
        ],
        links=[("Mock Exam 4", "mocks2.html#mock-4-100-questions-weighted-toward-weak-domains-final-cram"),
               ("Study Guide Part 1", "guide.html#part-1-security-principles-domain-1-isc2-weight-26"),
               ("Glossary all initialisms", "glossary.html"),
               ("Memory palace walkthrough", "guide.html#d2-the-cc-memory-palace")]),

    dict(w=2, d=5, title="Final review: targeted re-study of weakest mock domain plus exam logistics",
        subtitle="<strong>Acronyms used today:</strong> ISC2 CC (Certified in Cybersecurity, by the International Information System Security Certification Consortium).",
        focus="Look at your four mock scores. The domain where you scored lowest gets the final day. Re-read that part of the Study Guide, drill the 15 high-frequency miss patterns in Appendix B, and read Appendix C (day-of-exam reminders) twice. Tonight: pack ID, confirm test-center location, plan transportation, set alarm, then a full 5-room palace walk before bed. No new material after 8 PM. Sleep consolidates everything before tomorrow's exam.",
        citations=[
            ("Study Guide Appendix B", "15 high-frequency miss patterns drilled here will catch the most common careless errors"),
            ("Study Guide Appendix C", "100 questions in 120 minutes = 1.2 min per question; pass at 700/1000"),
            ("Walker 2017", "sleep consolidation: 6-8 hours the night before exam outperforms last-minute cram"),
        ],
        links=[("Study Guide Appendix B miss patterns", "guide.html#appendix-b-high-frequency-miss-patterns"),
               ("Study Guide Appendix C day-of reminders", "guide.html#appendix-c-day-of-exam-reminders"),
               ("Memory palace walkthrough", "guide.html#d2-the-cc-memory-palace")]),
]

assert len(DAYS) == 10, f"expected 10 days, got {len(DAYS)}"


# === User notes (read daily_notes.md, bake into HTML at build time) ===

DAILY_NOTES_MD = ROOT / "study_guide" / "daily_notes.md"

_NOTES_OPEN_RE = re.compile(r"^\s*<!--\s*user-notes:([a-z0-9-]+)\s*-->\s*$")
_NOTES_CLOSE_RE = re.compile(r"^\s*<!--\s*/user-notes:([a-z0-9-]+)\s*-->\s*$")
_NOTE_LINE_RE = re.compile(
    r"^\*(?P<text>.*)\*\{\.user-note\s+#(?P<id>note-[a-z0-9-]+-\d+)\}\s*$"
)


def _unescape_attrs(text: str) -> str:
    """Inverse of notes_server.escape_attrs_text. Single-pass left-to-right
    so \\\\* does not double-decode."""
    out = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text):
            nxt = text[i + 1]
            if nxt in ("\\", "*", "{", "}"):
                out.append(nxt)
                i += 2
                continue
        out.append(ch)
        i += 1
    return "".join(out)


def parse_daily_notes() -> dict:
    """Read daily_notes.md and return {anchor: [(note_id, text), ...]} mapping.
    Returns empty dict if file missing. Notes preserve their source order."""
    if not DAILY_NOTES_MD.exists():
        return {}
    lines = DAILY_NOTES_MD.read_text(encoding="utf-8").splitlines()
    notes: dict = {}
    current_anchor = None
    for line in lines:
        m_open = _NOTES_OPEN_RE.match(line)
        if m_open:
            current_anchor = m_open.group(1)
            notes.setdefault(current_anchor, [])
            continue
        m_close = _NOTES_CLOSE_RE.match(line)
        if m_close:
            current_anchor = None
            continue
        if current_anchor is None:
            continue
        m_note = _NOTE_LINE_RE.match(line)
        if m_note:
            notes[current_anchor].append(
                (m_note.group("id"), _unescape_attrs(m_note.group("text")))
            )
    return notes


def render_user_notes_html(anchor: str, notes_by_anchor: dict) -> str:
    """Render baked-in user notes for one anchor as a stream of <aside>
    elements. Returns empty string if no notes for this anchor.

    Each aside carries data-note-id and data-anchor so the inline JS can
    wire edit/delete affordances to the right markdown line via the BE.
    """
    bucket = notes_by_anchor.get(anchor, [])
    if not bucket:
        return ""
    parts = []
    for note_id, text in bucket:
        parts.append(
            f'<aside class="user-note" data-note-id="{h(note_id)}" '
            f'data-anchor="{h(anchor)}" data-source="baked">{h(text)}</aside>'
        )
    return "".join(parts)


# === Markdown rendering ===

def _collapse_dashes(s: str) -> str:
    """Slug function for anchors_plugin: default slugger then collapse multi-dashes.

    The default slugger converts ' - ' (em-dash-fix output) into '---' triples.
    Collapsing them to single '-' produces slugs like 'part-4-network-security'
    instead of 'part-4---network-security', matching the href scheme used in DAYS.
    Also collapses dots in section numbers: '2.3' -> '23' (via default slugger),
    which is why DAYS hrefs use '23-recovery-objectives' not '2-3-recovery-...'.
    """
    return re.sub(r"-+", "-", _default_slug(s)).strip("-")


def render_markdown(md_text: str) -> str:
    md = MarkdownIt("gfm-like", {"html": True, "linkify": False, "typographer": False})
    md = md.enable("table").enable("strikethrough")
    try:
        md = md.use(attrs_plugin)
    except Exception:
        pass
    md = md.use(anchors_plugin, min_level=1, max_level=4, slug_func=_collapse_dashes)
    return md.render(md_text)


# === Templates ===

PAGE_TMPL = Template("""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{ title }}</title>
<link rel="stylesheet" href="style.css">
<script src="notes.js" defer></script>
</head>
<body>
<main>
{{ body|safe }}
</main>
</body>
</html>
""")


def render_day_page(idx: int, notes_by_anchor: dict | None = None) -> str:
    d = DAYS[idx]
    n = idx + 1
    notes_by_anchor = notes_by_anchor or {}
    anchor_focus = f"day-{n}-focus"
    anchor_cites = f"day-{n}-citations"
    anchor_links = f"day-{n}-links"

    cites_html = "".join(
        f'<aside class="margin-note"><strong>{h(label)}</strong>: {gloss}</aside>'
        for (label, gloss) in d["citations"]
    )
    if d["links"]:
        links_list_html = "<ul>" + "".join(
            f'<li><a href="{h(href)}">{h(label)}</a></li>'
            for (label, href) in d["links"]
        ) + "</ul>"
    else:
        links_list_html = '<p><em>No external links today. Drill from memory.</em></p>'

    focus_notes_html = render_user_notes_html(anchor_focus, notes_by_anchor)
    cites_notes_html = render_user_notes_html(anchor_cites, notes_by_anchor)
    links_notes_html = render_user_notes_html(anchor_links, notes_by_anchor)

    prev_href = f"day-{n-1:02d}.html" if n > 1 else "index.html"
    next_href = f"day-{n+1:02d}.html" if n < 10 else "index.html"
    prev_label = f"&larr; Day {n-1}" if n > 1 else "&larr; Index"
    next_label = f"Day {n+1} &rarr;" if n < 10 else "Index &rarr;"

    body = f"""
<header class="hero">
  <div class="hero__category">ISC2 CC cram - week {d['w']} - day {d['d']}</div>
  <h1 class="hero__title">{h(d['title'])}</h1>
  {f'<p class="hero__subtitle">{d["subtitle"]}</p>' if d.get('subtitle') else ''}
  <div class="hero__meta">
    <span><strong>Day {n}</strong> of 10</span>
    <span><strong>Week {d['w']}</strong> of 2</span>
    <span>Exam {EXAM_DATE}</span>
  </div>
</header>

<div class="focus" data-notable-anchor="{anchor_focus}">
  <span class="focus__label">Today's focus</span>
  <p>{h(d['focus'])}</p>
</div>
{focus_notes_html}

<span class="notable-anchor" data-notable-anchor="{anchor_cites}" aria-hidden="true"></span>
{cites_html}
{cites_notes_html}

<h2 id="{anchor_links}" data-notable-anchor="{anchor_links}">Links</h2>
{links_list_html}
{links_notes_html}

<nav class="daynav">
  <a href="{prev_href}">{prev_label}</a>
  <span class="daynav__meta">CC cram - {DEFAULT_START} start - exam {EXAM_DATE}</span>
  <a href="{next_href}">{next_label}</a>
</nav>
"""
    return PAGE_TMPL.render(title=f"Day {n}: {d['title']}", body=body)


def render_index() -> str:
    """Router: auto-detects today's weekday index and redirects, or shows TOC."""
    grid = "".join(
        f'<a href="day-{i+1:02d}.html" data-idx="{i}">'
        f'D{i+1}<small>W{d["w"]} - D{d["d"]}</small></a>'
        for i, d in enumerate(DAYS)
    )
    body = f"""
<div id="server-banner" class="callout callout--info server-banner" hidden>
  <span class="callout__label">Notes backend</span>
  <p id="server-banner-msg">Checking backend...</p>
  <div class="server-banner__cmd">
    <code id="server-banner-cmd">python3 scripts/notes_server.py</code>
    <button type="button" class="server-banner__copy" data-copy-target="server-banner-cmd">copy</button>
  </div>
  <p class="server-banner__detail">Run from cc-prep root. Then open <code>http://localhost:8765/</code> for full add/edit/delete. Without the backend, notes save to your browser only and can be exported as markdown below.</p>
</div>

<header class="hero">
  <div class="hero__category">ISC2 CC cram program</div>
  <h1 class="hero__title">2 weeks, Mon-Fri, 10 study days</h1>
  <p class="hero__subtitle">Open this page each weekday morning. The router below sends you to today's lesson. Exam date {EXAM_DATE}. Weighted toward Domain 4 Network Security (your weakest at 55 percent prelim). ISC2 CC = Certified in Cybersecurity, by the International Information System Security Certification Consortium; full acronym list in the <a href="glossary.html">glossary</a>.</p>
  <div class="hero__meta">
    <span><strong>Start</strong> {DEFAULT_START}</span>
    <span><strong>Exam</strong> {EXAM_DATE}</span>
    <span><strong>Cadence</strong> weekdays only</span>
  </div>
</header>

<div id="router-status"></div>

<h2>All 10 days</h2>
<div class="toc">{grid}</div>

<h2>Corpus</h2>
<ul>
  <li><a href="guide.html">CC Study Guide</a> - 5 domains + appendices, weighted to your prelim scores</li>
  <li><a href="exams.html">Practice Exams Mocks 1-2</a> - ISC2-weighted, 100 questions each</li>
  <li><a href="mocks2.html">Practice Exams Mocks 3-4</a> - weighted toward Domain 4 and Domain 2</li>
  <li><a href="glossary.html">Glossary</a> - every initialism defined</li>
</ul>

<h2 id="notes-tools">Notes tools</h2>
<p id="notes-tools-summary" class="hero__subtitle">Loading...</p>
<div class="notes-tools">
  <button type="button" id="notes-export" disabled>Export browser notes as markdown</button>
  <label class="notes-tools__import">
    Import notes from markdown
    <input type="file" id="notes-import" accept=".md,text/markdown,text/plain">
  </label>
  <button type="button" id="notes-clear-ls" disabled>Clear all browser notes</button>
</div>
<p class="server-banner__detail"><strong>Export</strong> downloads your browser-stored notes as a single <code>daily_notes_export.md</code> file. <strong>Import</strong> parses the same format and merges into your browser store (or posts to the backend when it is running). Both operations preserve note IDs so a round-trip through the backend keeps the markdown clean.</p>

<script>
const START = "{DEFAULT_START}";
function todayIdx() {{
  const [y, m, d] = START.split("-").map(Number);
  const start = new Date(y, m-1, d); start.setHours(0,0,0,0);
  const today = new Date(); today.setHours(0,0,0,0);
  if (today < start) return -1;
  let n = 0;
  const cur = new Date(start);
  while (cur < today) {{
    cur.setDate(cur.getDate() + 1);
    const dow = cur.getDay();
    if (dow !== 0 && dow !== 6) n++;
  }}
  const dow = today.getDay();
  if (dow === 0 || dow === 6) return -2;
  return n;
}}
const idx = todayIdx();
const status = document.getElementById("router-status");
if (idx === -1) {{
  status.innerHTML = '<div class="callout callout--info"><span class="callout__label">Cram not started</span><p>Program start date is ' + START + '. Bookmark this page. <a href="day-01.html">Preview Day 1 (Domain 4 part 1)</a>.</p></div>';
}} else if (idx === -2) {{
  status.innerHTML = '<div class="callout callout--ok"><span class="callout__label">Rest day</span><p>Saturday or Sunday. Light Anki only. Use the TOC below to jump to any day or take an extra mock.</p></div>';
}} else if (idx >= 10) {{
  status.innerHTML = '<div class="callout callout--ok"><span class="callout__label">Cram complete - exam imminent</span><p>10 study days done. Final review Day 10. <a href="day-10.html">Re-read Day 10</a> | Exam date {EXAM_DATE}.</p></div>';
}} else {{
  const todayLink = document.querySelector('.toc a[data-idx="' + idx + '"]');
  if (todayLink) todayLink.classList.add('today');
  status.innerHTML = '<div class="callout callout--info"><span class="callout__label">Today is day ' + (idx+1) + '</span><p>Redirecting in 3 seconds... <a href="day-' + String(idx+1).padStart(2,"0") + '.html">Go now</a> | <a href="#" onclick="event.preventDefault();document.getElementById(\\'router-status\\').style.display=\\'none\\';">Stay on index</a></p></div>';
  setTimeout(function() {{
    if (document.getElementById("router-status").style.display !== "none") {{
      location.href = 'day-' + String(idx+1).padStart(2,"0") + '.html';
    }}
  }}, 3000);
}}
</script>
"""
    return PAGE_TMPL.render(title="ISC2 CC cram program", body=body)


def render_corpus_page(md_path: Path, title: str, subtitle: str = "",
                       basename: str = "", notes_by_anchor: dict | None = None) -> str:
    md_text = md_path.read_text(encoding="utf-8")
    body_html = render_markdown(md_text)
    body_html = re.sub(r"^\s*<h1[^>]*>.*?</h1>\s*", "", body_html, count=1, flags=re.DOTALL)

    # Bake in user notes anchored at every h2 on the corpus page.
    # Anchor namespace: corpus-<basename>-<slug> so guide/exams/mocks2/glossary
    # don't collide with each other or with day-* anchors.
    notes_by_anchor = notes_by_anchor or {}
    if basename:
        def _anchor_h2(m: re.Match) -> str:
            full = m.group(0)
            id_match = re.search(r'id="([^"]+)"', full)
            if not id_match:
                return full
            anchor = f"corpus-{basename}-{id_match.group(1)}"
            tagged = full.replace(">", f' data-notable-anchor="{anchor}">', 1)
            return tagged + render_user_notes_html(anchor, notes_by_anchor)
        body_html = re.sub(r'<h2[^>]*>.*?</h2>', _anchor_h2, body_html, flags=re.DOTALL)

    hero = f"""
<header class="hero">
  <div class="hero__category">CC cram corpus</div>
  <h1 class="hero__title">{h(title)}</h1>
  {f'<p class="hero__subtitle">{h(subtitle)}</p>' if subtitle else ''}
</header>

<nav class="daynav" style="margin-top:0;border-top:none;padding-top:0;">
  <a href="index.html">&larr; Daily index</a>
  <span class="daynav__meta">{md_path.name}</span>
  <a href="#" onclick="window.scrollTo({{top:0,behavior:'smooth'}});return false;">Top &uarr;</a>
</nav>
"""
    return PAGE_TMPL.render(title=title, body=hero + body_html)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)

    notes_by_anchor = parse_daily_notes()
    note_count = sum(len(v) for v in notes_by_anchor.values())

    for i in range(10):
        out_path = OUT / f"day-{i+1:02d}.html"
        out_path.write_text(render_day_page(i, notes_by_anchor), encoding="utf-8")

    (OUT / "index.html").write_text(render_index(), encoding="utf-8")

    (OUT / "guide.html").write_text(
        render_corpus_page(SG_MD, "CC Study Guide",
            "5 domains plus appendices. Weighted to your prelim scores. Network Security at maximum depth.",
            basename="guide", notes_by_anchor=notes_by_anchor),
        encoding="utf-8")
    (OUT / "exams.html").write_text(
        render_corpus_page(PE_MD, "Practice Exams - Mocks 1 and 2",
            "ISC2-weighted, 100 questions each. Take timed at 2 hours.",
            basename="exams", notes_by_anchor=notes_by_anchor),
        encoding="utf-8")
    (OUT / "mocks2.html").write_text(
        render_corpus_page(PE2_MD, "Practice Exams - Mocks 3 and 4",
            "Weighted toward Domain 4 Network Security and Domain 2 BC/DR/IR (your weak domains).",
            basename="mocks2", notes_by_anchor=notes_by_anchor),
        encoding="utf-8")
    (OUT / "glossary.html").write_text(
        render_corpus_page(GLOS_MD, "ISC2 CC Glossary",
            "Every initialism defined. Drill the alphabet soup.",
            basename="glossary", notes_by_anchor=notes_by_anchor),
        encoding="utf-8")

    print(f"rendered: 10 daily pages + index + 4 corpus pages to {OUT}")
    print(f"  baked-in user notes: {note_count} across {len(notes_by_anchor)} anchors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
