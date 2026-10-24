# -*- coding: utf-8 -*-
"""All page content for blackcanyonhealth.com. Edit here, then run `python3 build.py`.

Each page: slug (URL path, matches the old Google Site), title (<60-65 chars ideal),
description (meta description, ~150-160 chars), body(L, A) -> HTML, optional jsonld, noindex.
L(slug) makes an internal link; A(name) makes an asset link.
"""

DOMAIN = "https://www.blackcanyonhealth.com"
ORG = "Black Canyon Community Health Center"

PORTAL = "https://16465.portal.athenahealth.com/"
PAY = "https://payment.patient.athenahealth.com/statement/?src=statement"
SCHED_BC = "https://consumer.scheduling.athena.io/?locationId=16465-1"
SCHED_SV = "https://consumer.scheduling.athena.io/?locationId=16465-8"
FACEBOOK = "https://www.facebook.com/BlackCanyonHealth"
SURVEY = "https://docs.google.com/forms/d/e/1FAIpQLSeckBkbXVhekv_V6cz2Pm2KBFnefNyv4R45QDTOwrEKDfEwCQ/viewform"
MERCH = "https://black-canyon-comm-health.printify.me/products"
EMAIL = "feedback@blackcanyonhealth.com"
FAX = "(623) 374-5576"

CLINICS = {
    "black-canyon": {
        "name": "Black Canyon City", "full": "Black Canyon City Clinic",
        "street": "19251 E. Oasis Drive", "city": "Black Canyon City", "zip": "85324",
        "phone": "(623) 374-0200", "tel": "+16233740200", "sched": SCHED_BC,
        "geo": (34.0599427, -112.1478393),
        "maps": "https://www.google.com/maps/search/?api=1&query=Black+Canyon+Community+Health+Center+19251+E+Oasis+Dr+Black+Canyon+City+AZ+85324",
        "hours": [("Monday", 1, 8, 17), ("Tuesday", 2, 9, 19), ("Wednesday", 3, 8, 17), ("Thursday", 4, 9, 19), ("Friday", 5, 8, 15)],
        "nearby": "Black Canyon City, Rock Springs, Bumble Bee, Cordes Lakes, New River and Anthem",
    },
    "spring-valley": {
        "name": "Spring Valley (Mayer)", "full": "Spring Valley Clinic",
        "street": "17301 E. Spring Valley Road, Suite G", "city": "Mayer", "zip": "86333",
        "phone": "(928) 404-8004", "tel": "+19284048004", "sched": SCHED_SV,
        "geo": None,
        "maps": "https://www.google.com/maps/search/?api=1&query=17301+E+Spring+Valley+Rd+Suite+G+Mayer+AZ+86333",
        "hours": [("Monday", 1, 8, 17), ("Tuesday", 2, 8, 17), ("Wednesday", 3, 8, 19), ("Thursday", 4, 8, 17), ("Friday", 5, 8, 15)],
        "nearby": "Mayer, Spring Valley, Cordes Lakes, Dewey-Humboldt and Prescott Valley",
    },
    "camp-verde": {
        "name": "Camp Verde", "full": "Camp Verde Clinic",
        "street": "385 S. Main Street", "city": "Camp Verde", "zip": "86322",
        "maps": "https://www.google.com/maps/search/?api=1&query=385+S+Main+St+Camp+Verde+AZ+86322",
        "nearby": "Camp Verde, Cottonwood, Rimrock, Lake Montezuma and the Verde Valley",
    },
}

DAY_CODES = {1: "Mo", 2: "Tu", 3: "We", 4: "Th", 5: "Fr"}


def t12(h):
    return f"{h % 12 or 12}:00 {'PM' if h >= 12 else 'AM'}"


def hours_short(h):
    return f"{h % 12 or 12}{'pm' if h >= 12 else 'am'}"


# ----------------------------------------------------------------- icons / art
ICON = {
    "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4.5" width="18" height="16" rx="2"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4M8 14h3"/></svg>',
    "portal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M8 20h8M12 16v4M8.5 10l2 2 4-4"/></svg>',
    "card": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M2.5 10h19M6.5 15h4"/></svg>',
    "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v18M7 21h10M4 7h16M6.5 7 3.5 13a3 3 0 0 0 6 0L6.5 7ZM17.5 7l-3 6a3 3 0 0 0 6 0l-3-6Z"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 3.5h3.2l1.6 4.2-2.1 1.4a11 11 0 0 0 5.2 5.2l1.4-2.1 4.2 1.6V17a2.5 2.5 0 0 1-2.7 2.5A15.5 15.5 0 0 1 2.5 6.2 2.5 2.5 0 0 1 5 3.5Z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    "thermo": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 14.8V5a2 2 0 0 0-4 0v9.8a4 4 0 1 0 4 0Z"/><path d="M12 11v6"/></svg>',
    "pulse": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.4 5.6a5 5 0 0 0-7.1 0L12 6.9l-1.3-1.3a5 5 0 0 0-7.1 7.1L12 21l8.4-8.3a5 5 0 0 0 0-7.1Z"/><path d="M3.5 12h4l1.5-3 3 6 1.5-3h7"/></svg>',
    "clip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h6M9 18h3"/></svg>',
    "child": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M9 10h.01M15 10h.01M8.8 14.2a4.5 4.5 0 0 0 6.4 0M12 3.5c-1.2 1-1.3 2.4 0 3"/></svg>',
    "flower": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="9" r="2.5"/><path d="M12 6.5C12 3 15.5 3 15.5 5.5c2.5 0 2.5 3.5-1 3.5 3.5 0 3.5 3.5 1 3.5 0 2.5-3.5 2.5-3.5-1 0 3.5-3.5 3.5-3.5 1-2.5 0-2.5-3.5 1-3.5-3.5 0-3.5-3.5-1-3.5C8.5 3 12 3 12 6.5ZM12 14v7M12 18c-2 0-3.5-1-4-2.5M12 19c2 0 3.5-1 4-2.5"/></svg>',
    "senior": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7.5 3v5.5c0 4.6-3.2 8.2-7.5 9.5-4.3-1.3-7.5-4.9-7.5-9.5V6L12 3Z"/><path d="M8.8 12l2.2 2.2 4.2-4.4"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}

def saguaro(x, base, s=1.0):
    """A saguaro silhouette standing on y=base at x (in landscape units)."""
    return (f'<g transform="translate({x} {base}) scale({s})">'
            '<rect x="-5" y="-62" width="10" height="62" rx="5"/>'
            '<path d="M-5-30h-8a5 5 0 0 1-5-5v-15a4 4 0 0 1 8 0v12h5z"/>'
            '<path d="M5-38h7v-12a4 4 0 0 1 8 0v15a5 5 0 0 1-5 5H5z"/></g>')


def landscape(ground="var(--paper)", photo=False):
    return (
        '<svg class="landscape" viewBox="0 0 1440 200" preserveAspectRatio="xMidYMax slice" aria-hidden="true">'
        + ('' if photo else '<path d="M0 118 120 98l90 6 50-32h120l40 20 140-8 80-30h120l40 26 140 12 100-30h120l40 26 120-6 120 14v104H0Z" fill="rgba(255,255,255,.06)"/>') +
        '<path d="M0 150c200-22 360-10 520-18 180-10 340 14 520 4 160-8 280 4 400-4v68H0Z" style="fill:var(--band-deep)"/>'
        f'<g style="fill:var(--band-deep)">{saguaro(255, 141, 0.95)}{saguaro(1092, 140, 1.15)}{saguaro(1180, 139, 0.7)}</g>'
        f'<path d="M0 182c240-12 480 8 720-2 240-10 480 8 720-6v26H0Z" style="fill:{ground}"/>'
        '</svg>')


# ----------------------------------------------------------------- shared chrome
NAV = [("services", "Services"), ("locations", "Locations"), ("providers", "Providers"),
       ("about-us", "About")]


def chrome(L, A, page, body):
    cur = page["slug"].split("/")[0]
    nav = "".join(f'<a href="{L(s)}"{" aria-current=\"page\"" if cur == s else ""}>{t}</a>' for s, t in NAV)
    menu = "".join(f'<a href="{L(s)}">{t}</a>' for s, t in [("", "Home")] + NAV + [("patient-portal", "Patient Portal"), ("pay-my-bills", "Pay a Bill"), ("sliding-fee-discount-program", "Sliding Fee Discount"), ("careers", "Careers")])
    bc, sv, cv = CLINICS["black-canyon"], CLINICS["spring-valley"], CLINICS["camp-verde"]
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="utility"><div class="wrap">
  <div class="phones"><span>Black Canyon City <a href="tel:{bc['tel']}">{bc['phone']}</a></span><span>Spring Valley <a href="tel:{sv['tel']}">{sv['phone']}</a></span></div>
  <div class="links"><a href="{L('pay-my-bills')}">Pay a bill</a><a href="{L('careers')}">Careers</a></div>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="brand" href="{L('')}"><img src="{A('logo-white.png')}" alt="{ORG} home" width="520" height="356"></a>
  <nav class="nav" aria-label="Main">{nav}<a href="{L('patient-portal')}"{' aria-current="page"' if cur == 'patient-portal' else ''}>Patient Portal</a><a class="btn btn-sun" href="{L('schedule-appointment')}">Book an appointment</a></nav>
  <details class="menu"><summary>Menu</summary><nav class="menu-panel" aria-label="Mobile">{menu}<a class="btn btn-sun" href="{L('schedule-appointment')}">Book an appointment</a></nav></details>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div class="foot-brand">
      <a class="brand brand-foot" href="{L('')}"><img src="{A('logo-white.png')}" alt="{ORG}" width="520" height="356" loading="lazy"></a>
      <p>A nonprofit community health center caring for rural Yavapai County since 1999. Everyone is welcome, with or without insurance.</p>
      <p class="emergency">In a medical emergency, call 911.</p>
      <div class="member"><span>Proud member of</span><img src="{A('img/arizona-alliance.png')}" alt="Arizona Alliance for Community Health Centers" width="330" height="92"></div>
    </div>
    <div><h2>Clinics</h2><ul>
      <li><a href="{L('locations/black-canyon')}">Black Canyon City</a><br>{bc['street']}<br><a href="tel:{bc['tel']}">{bc['phone']}</a></li>
      <li><a href="{L('locations/spring-valley')}">Spring Valley (Mayer)</a><br>{sv['street']}<br><a href="tel:{sv['tel']}">{sv['phone']}</a></li>
      <li><a href="{L('locations/camp-verde')}">Camp Verde</a> · opening soon</li>
    </ul></div>
    <div><h2>Patients</h2><ul>
      <li><a href="{L('schedule-appointment')}">Book an appointment</a></li>
      <li><a href="{L('patient-portal')}">Patient portal</a></li>
      <li><a href="{L('pay-my-bills')}">Pay a bill</a></li>
      <li><a href="{L('sliding-fee-discount-program')}">Sliding fee discount</a></li>
      <li><a href="{L('services')}">Services</a></li>
      <li><a href="{SURVEY}" rel="noopener">Community survey</a></li>
      <li><a href="{L('notice-of-privacy-practices')}">Privacy notice</a></li>
    </ul></div>
    <div><h2>Organization</h2><ul>
      <li><a href="{L('about-us')}">About us</a></li>
      <li><a href="{L('providers')}">Our providers</a></li>
      <li><a href="{L('careers')}">Careers</a></li>
      <li><a href="{L('employees')}">Employee resources</a></li>
      <li><a href="{FACEBOOK}" rel="noopener">Facebook</a></li>
      <li><a href="{MERCH}" rel="noopener">Merchandise</a></li>
    </ul></div>
  </div>
  <div class="foot-legal">
    <p>Questions or feedback: <a href="mailto:{EMAIL}">{EMAIL}</a> · Fax {FAX}</p>
    <p>{ORG}, Inc. is a 501(c)(3) nonprofit organization and a Federally Qualified Health Center. <a href="{L('nondiscrimination')}">Nondiscrimination notice and language help</a> · <a href="{L('notice-of-privacy-practices')}">Notice of Privacy Practices</a></p>
    <p>© {SITE['year']} {ORG}, Inc.</p>
  </div>
</div></footer>"""


# ----------------------------------------------------------------- structured data
def clinic_ld(key):
    c = CLINICS[key]
    d = {
        "@type": "MedicalClinic",
        "@id": f"{DOMAIN}/locations/{key}#clinic",
        "name": f"{ORG} – {c['full']}",
        "url": f"{DOMAIN}/locations/{key}",
        "address": {"@type": "PostalAddress", "streetAddress": c["street"], "addressLocality": c["city"],
                    "addressRegion": "AZ", "postalCode": c["zip"], "addressCountry": "US"},
        "parentOrganization": {"@id": f"{DOMAIN}/#org"},
        "medicalSpecialty": "PrimaryCare",
        "isAcceptingNewPatients": True,
        "areaServed": c["nearby"],
    }
    if c.get("phone"):
        d["telephone"] = c["tel"]
        d["faxNumber"] = "+16233745576"
        d["openingHoursSpecification"] = [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": day, "opens": f"{o:02d}:00", "closes": f"{cl:02d}:00"}
            for day, _, o, cl in c["hours"]]
    if c.get("geo"):
        d["geo"] = {"@type": "GeoCoordinates", "latitude": c["geo"][0], "longitude": c["geo"][1]}
    if key == "camp-verde":
        d["isAcceptingNewPatients"] = False
        d["description"] = "Opening soon."
    return d


ORG_LD = {
    "@type": ["MedicalOrganization", "NGO"],
    "@id": f"{DOMAIN}/#org",
    "name": ORG,
    "legalName": f"{ORG}, Inc.",
    "url": DOMAIN + "/",
    "logo": DOMAIN + "/assets/logo-navy.png",
    "email": EMAIL,
    "foundingDate": "1999",
    "nonprofitStatus": "Nonprofit501c3",
    "description": "Nonprofit Federally Qualified Health Center providing primary and preventive care in rural Yavapai County, Arizona.",
    "sameAs": [FACEBOOK],
}


def graph(*items):
    return {"@context": "https://schema.org", "@graph": list(items)}


def crumbs_ld(*pairs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + ("/" + s if s else "/") + ("/" if s == "locations" else "")}
        for i, (n, s) in enumerate(pairs)]}


# ----------------------------------------------------------------- page pieces
def page_hero(L, title, lede, crumb=None, ground="var(--paper)"):
    c = ""
    if crumb:
        c = '<p class="crumbs"><a href="' + L('') + '">Home</a>' + "".join(
            f' / <a href="{L(s)}">{n}</a>' if s is not None else f" / {n}" for n, s in crumb) + "</p>"
    return f"""<section class="page-hero has-photo"><img class="hero-photo" src="{L.asset('img/bradshaw-landscape.jpg')}" alt="" width="1140" height="646"><div class="wrap">{c}<h1>{title}</h1>{f'<p class="lede">{lede}</p>' if lede else ''}</div>{landscape(ground, photo=True)}</section>"""


def hours_table(key):
    c = CLINICS[key]
    rows = "".join(f'<tr data-day="{n}"><th scope="row">{d}</th><td>{t12(o)} – {t12(cl)}</td></tr>' for d, n, o, cl in c["hours"])
    rows += '<tr data-day="6"><th scope="row">Saturday</th><td>Closed</td></tr><tr data-day="0"><th scope="row">Sunday</th><td>Closed</td></tr>'
    return f'<table class="hours"><caption class="sr-only">{c["full"]} hours</caption><tbody>{rows}</tbody></table>'


def loc_card(L, key):
    c = CLINICS[key]
    if key == "camp-verde":
        return f"""<article class="loc"><span class="status soon">Opening soon</span><h3><a href="{L('locations/camp-verde')}">Camp Verde</a></h3>
<div class="meta"><span>{c['street']}</span><span>{c['city']}, AZ {c['zip']}</span></div>
<p>Our third clinic, coming to Main Street in Camp Verde. Hours and a phone number will be posted here when we open.</p>
<div class="actions"><a class="btn btn-line" href="{L('locations/camp-verde')}">Learn more</a></div></article>"""
    return f"""<article class="loc"><span class="status" data-status="{key}">Hours below</span><h3><a href="{L('locations/' + key)}">{c['name']}</a></h3>
<div class="meta"><span>{c['street']}</span><span>{c['city']}, AZ {c['zip']}</span><a href="tel:{c['tel']}">{c['phone']}</a></div>
{hours_table(key)}
<div class="actions"><a class="btn btn-sun" href="{c['sched']}" rel="noopener">Book online</a><a class="btn btn-line" href="{c['maps']}" rel="noopener">Directions</a></div></article>"""



HOME_FAQ = [
    ("Are you accepting new patients?", "<p>Yes. Both clinics welcome new patients of all ages. <a href=\"{schedule-appointment}\">Book online</a> or call the clinic closest to you.</p>"),
    ("What insurance do you take?", "<p>We bill Medicare, AHCCCS (Arizona Medicaid) and private insurance. Plans change often, so call your clinic to confirm we're in network with yours.</p>"),
    ("Can I be seen if I don't have insurance?", "<p>Yes. Everyone is welcome, with or without insurance. Our front desk can help you look into AHCCCS and other coverage, and <a href=\"{sliding-fee-discount-program}\">financial assistance</a> is available for patients who qualify.</p>"),
    ("Do you see children?", "<p>Yes. We provide well-child checkups, vaccines and sick visits for kids, so the whole family can see the same clinic.</p>"),
    ("What is a Medicare Annual Wellness Visit?", "<p>It's a yearly visit for people with Medicare to review your health, update your screenings and make a personalized prevention plan. It's different from a sick visit. Ask for one when you book.</p>"),
    ("What should I bring to my first visit?", "<p>A photo ID, your insurance card if you have one, and a list of your medications or the bottles themselves. Please arrive 15 minutes early.</p>"),
    ("Do you offer dental or prenatal care?", "<p>We don't provide these in our clinics, but we refer patients to trusted local partners for dental and obstetric care and help coordinate the referral.</p>"),
]


def faq_html(items, L):
    out = ""
    for q, a in items:
        a = a.replace("{schedule-appointment}", L("schedule-appointment")).replace("{sliding-fee-discount-program}", L("sliding-fee-discount-program"))
        out += f"<details><summary>{q}</summary><div class=\"answer\">{a}</div></details>"
    return out


# Homepage announcement. The banner shows only until "until" (YYYY-MM-DD); the monthly
# agent rebuilds the site, so it drops off on its own. Set to None for no banner.
ANNOUNCEMENT = {
    "until": "2027-01-22",
    "label": "New provider",
    "text": "Please join us in welcoming <strong>Shea Green, PA-C</strong>. Shea brings more than six years of experience in pediatric primary care, pediatric emergency medicine and ENT.",
    "link": ("providers#shea-green", "Meet Shea"),
}


def announcement(L):
    import datetime
    a = ANNOUNCEMENT
    if not a or datetime.date.today().isoformat() > a["until"]:
        return ""
    return f'''<div class="wrap"><aside class="announce" aria-label="Announcement"><span class="announce-label">{a["label"]}</span><p>{a["text"]}</p><a class="announce-link" href="{L(a["link"][0])}">{a["link"][1]} {ICON["arrow"]}</a></aside></div>'''


# Provider headshots: add "Name, Credential": "file-stem" (photo in src/img/) to show a photo
# instead of initials. Kept empty so every card matches until all providers have
# consistent professional photos.
PHOTOS = {}


def avatar(A, name, size=""):
    parts = name.split(",")[0].split()
    if name in PHOTOS:
        return f'<img class="avatar{size}" src="{A("img/" + PHOTOS[name] + ".jpg")}" alt="{name}" width="320" height="320" loading="lazy">'
    return f'<span class="avatar{size}" aria-hidden="true">{parts[0][0]}{parts[-1][0]}</span>'


def team_row(L, A):
    out = ""
    for name, role, _ in PROVIDERS:
        parts = name.split(",")[0].split()
        out += f'<a class="team" href="{L("providers")}">{avatar(A, name)}<span><strong>{name}</strong><span>{role.split(" · ")[0]}</span></span></a>'
    return out


# ----------------------------------------------------------------- pages
def home(L, A):
    bc, sv = CLINICS["black-canyon"], CLINICS["spring-valley"]
    return f"""<section class="hero has-photo"><img class="hero-photo" src="{A('img/bradshaw-landscape.jpg')}" alt="Grassland and mountains in central Arizona" width="1140" height="646" fetchpriority="high"><div class="wrap">
  <div>
    <p class="eyebrow">Nonprofit community health center</p>
    <h1>Primary&nbsp;care for rural central Arizona</h1>
    <p class="lede">Family medicine for every age, close to home, from the I-17 corridor to the Verde Valley. Medicare, AHCCCS, private insurance and uninsured patients are all welcome.</p>
    <div class="hero-ctas"><a class="btn btn-sun" href="{L('schedule-appointment')}">{ICON['cal']}Book an appointment</a><a class="btn btn-ghost" href="{L('locations')}">Find a clinic</a></div>
    <p class="hero-note">Already a patient? <a href="{PORTAL}" rel="noopener">Log in to the patient portal</a> to message your care team or see test results.</p>
  </div>
  <aside class="today" aria-labelledby="today-h">
    <div class="today-head"><h2 id="today-h">Our clinics today</h2><span class="az">Arizona time</span></div>
    <div class="clinic-row"><h3><a href="{L('locations/black-canyon')}">Black Canyon City</a></h3><a class="tel" href="tel:{bc['tel']}">{bc['phone']}</a><span class="status" data-status="black-canyon">Mon–Fri</span><span class="addr">{bc['street']}</span></div>
    <div class="clinic-row"><h3><a href="{L('locations/spring-valley')}">Spring Valley, Mayer</a></h3><a class="tel" href="tel:{sv['tel']}">{sv['phone']}</a><span class="status" data-status="spring-valley">Mon–Fri</span><span class="addr">{sv['street']}</span></div>
    <div class="clinic-row"><h3><a href="{L('locations/camp-verde')}">Camp Verde</a></h3><span class="status soon">Opening soon</span><span class="addr">385 S. Main Street</span></div>
  </aside>
</div>{landscape(photo=True)}</section>

<div class="wrap quick"><nav class="quick-grid" aria-label="Patient tasks">
  <a href="{L('schedule-appointment')}">{ICON['cal']}<strong>Book a visit</strong><span>Online or by phone</span></a>
  <a href="{PORTAL}" rel="noopener">{ICON['portal']}<strong>Patient portal</strong><span>Messages, results, records</span></a>
  <a href="{L('pay-my-bills')}">{ICON['card']}<strong>Pay a bill</strong><span>Secure online payment</span></a>
  <a href="{L('locations')}">{ICON['pin']}<strong>Locations &amp; hours</strong><span>Black Canyon City and Mayer</span></a>
</nav></div>
{announcement(L)}
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">What we do</p><h2>Everyday care for your whole family</h2><p>Our physician, physician assistants and nurse practitioners handle the visits most families need, close to home.</p></div>
  <div class="svc-grid">
    <div class="svc"><span class="chip">{ICON["thermo"]}</span><h3>Sick visits and injuries</h3><p>Care for sore throats, flu, infections, sprains and minor injuries.</p></div>
    <div class="svc"><span class="chip">{ICON["pulse"]}</span><h3>Chronic conditions</h3><p>Ongoing care for diabetes, high blood pressure, high cholesterol, asthma, allergies and heart disease.</p></div>
    <div class="svc"><span class="chip">{ICON["clip"]}</span><h3>Physicals and prevention</h3><p>Annual exams and physicals, immunizations, screenings, weight management and help quitting smoking.</p></div>
    <div class="svc"><span class="chip">{ICON["child"]}</span><h3>Children</h3><p>Well-child checkups, vaccines and care when your child is sick.</p></div>
    <div class="svc"><span class="chip">{ICON["flower"]}</span><h3>Women's health</h3><p>Well-woman exams, gynecological care, family planning and hormone management.</p></div>
    <div class="svc"><span class="chip">{ICON["senior"]}</span><h3>Ages 65+</h3><p>Medicare Annual Wellness Visits, age-specific screenings and help enrolling in Medicare.</p></div>
  </div>
  <p style="margin-top:1.5rem"><a href="{L('services')}">See all services</a></p>
</div></section>

<section class="band alt"><div class="wrap split wide-left">
  <div class="prose">
    <p class="eyebrow">Who we are</p>
    <h2>A nonprofit clinic for the whole community</h2>
    <p>{ORG} is a nonprofit Federally Qualified Health Center. Dr. Randy Hancock opened the clinic in Black Canyon City in 1999 so everyone in the area would have a place to get care, and we've grown with the community ever since.</p>
    <p>Our front desk can help you with insurance questions, AHCCCS enrollment and <a href="{L('sliding-fee-discount-program')}">financial assistance</a>.</p>
    <p><a class="btn btn-line" href="{L('about-us')}">About us</a></p>
  </div>
  <div class="stats" style="grid-template-columns:minmax(0,1fr);margin-top:0">
    <div><strong>1999</strong><span>The year we opened in Black Canyon City</span></div>
    <div><strong>3,100</strong><span>Patients served in 2025, up 14% from 2024</span></div>
    <div><strong>3</strong><span>Clinics, with Camp Verde opening soon</span></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Locations</p><h2>Three clinics in Yavapai County</h2><p>Serving {bc['nearby']}, plus the Mayer area and soon the Verde Valley.</p></div>
  <div class="loc-grid">{loc_card(L, 'black-canyon')}{loc_card(L, 'spring-valley')}{loc_card(L, 'camp-verde')}</div>
</div></section>

<section class="band alt"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Our providers</p><h2>Care from people who know the community</h2><p>A physician, physician assistants and nurse practitioners who care for patients of every age.</p></div>
  <div class="team-row">{team_row(L, A)}</div>
  <p style="margin-top:1.5rem"><a href="{L('providers')}">Meet our providers</a></p>
</div></section>

<section class="band"><div class="wrap split wide-left">
  <div><div class="section-head"><p class="eyebrow">Questions</p><h2>Common questions from new patients</h2></div>
  <div class="faq">{faq_html(HOME_FAQ, L)}</div></div>
  <div class="prose"><h2 style="font-size:var(--s-3)">Ready to come in?</h2><p>Book online any time, or call during clinic hours and our front desk will find a time that works.</p><p><a class="btn btn-sun" href="{L('schedule-appointment')}">{ICON['cal']}Book an appointment</a></p></div>
</div></section>

<section class="band alt"><div class="wrap">
  <div class="callout"><div><h2>New patients are welcome</h2><p>Book online or call the clinic closest to you. Bring a photo ID, your insurance card if you have one, and a list of your medications.</p></div>
  <div class="hero-ctas" style="margin-top:0"><a class="btn btn-sun" href="{L('schedule-appointment')}">Book an appointment</a></div></div>
</div></section>"""


def schedule(L, A):
    cards = ""
    for key in ("black-canyon", "spring-valley"):
        c = CLINICS[key]
        cards += f"""<article class="loc"><span class="status" data-status="{key}">Mon–Fri</span><h2 style="font-size:var(--s-3)">{c['name']}</h2>
<div class="meta"><span>{c['street']}, {c['city']}</span><span>Call <a href="tel:{c['tel']}">{c['phone']}</a></span></div>
<div class="actions"><a class="btn btn-sun" href="{c['sched']}" rel="noopener">{ICON['cal']}Book online at {c['name'].split(' (')[0]}</a></div></article>"""
    return page_hero(L, "Book an appointment", "Pick a clinic to see open times and book online, or call and our front desk will find a time for you.", [("Book an appointment", None)]) + f"""
<section class="band"><div class="wrap">
  <div class="loc-grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr))">{cards}</div>
</div></section>
<section class="band alt"><div class="wrap split">
  <div class="prose"><h2>Before your visit</h2><ul>
    <li>Bring a photo ID and your insurance card, if you have one.</li>
    <li>Bring a list of your medications, or the bottles themselves.</li>
    <li>No insurance? Ask about our <a href="{L('sliding-fee-discount-program')}">sliding fee discount</a> when you check in.</li>
    <li>Please arrive 15 minutes early for your first visit.</li>
  </ul></div>
  <div class="prose"><h2>More options in the portal</h2><p>Current patients can request appointments, message their care team and see upcoming visits in the <a href="{PORTAL}" rel="noopener">patient portal</a>.</p>
  <p class="notice">For a medical emergency, call 911 or go to the nearest emergency room.</p></div>
</div></section>"""


FAQ_PORTAL = [
    ("What is the patient portal?", "<p>The portal is a secure website from athenahealth where you can message your care team, see test results, review your visit summaries and health records, request appointments and pay your bill.</p>"),
    ("How do I create an account?", "<p>Ask our front desk to add your email address to your chart. You'll get an email from athenahealth with a link to set up your account. Follow the link, confirm your identity and create a password.</p>"),
    ("How do I log in?", f'<p>Go to <a href="{PORTAL}" rel="noopener">our patient portal</a> and sign in with the email and password you set up. Bookmark the page so it&#39;s easy to find next time.</p>'),
    ("How do I reset my password?", "<p>On the portal sign-in page, choose the forgot-password link and follow the steps sent to your email.</p>"),
    ("How do I see my test results?", "<p>Sign in and open the test results section. Results appear after your provider has reviewed and released them. If you have questions about a result, send your care team a message.</p>"),
    ("Who do I contact if the portal isn't working?", "<p>Call your clinic: Black Canyon City at (623) 374-0200 or Spring Valley at (928) 404-8004. We can resend your invitation or update your email address.</p>"),
    ("How do I make sure you have my correct contact information?", "<p>Check your profile in the portal, or confirm your address, phone number and email with the front desk at your next visit.</p>"),
    ("Can I download my records to send to another provider?", "<p>Yes. You can view and download your health record summary in the portal. For a full copy of your records, call your clinic and we'll help with a records request.</p>"),
    ("How do I pay my bill?", None),
]


def portal(L, A):
    items = ""
    for q, a in FAQ_PORTAL:
        if a is None:
            a = f'<p>Pay online on our <a href="{L("pay-my-bills")}">Pay a Bill</a> page. Struggling with medical bills? See if you qualify for our <a href="{L("sliding-fee-discount-program")}">income-based sliding fee discount</a>.</p>'
        items += f"<details><summary>{q}</summary><div class=\"answer\">{a}</div></details>"
    return page_hero(L, "Patient portal", "Message your care team, see test results and manage appointments from your phone or computer.", [("Patient portal", None)]) + f"""
<section class="band"><div class="wrap split wide-left">
  <div><h2 style="margin-bottom:1.2rem">Common questions</h2><div class="faq">{items}</div></div>
  <aside class="loc" style="position:sticky;top:110px"><h2 style="font-size:var(--s-3)">Log in or register</h2><p>Our portal is run by athenahealth, our electronic health record provider. Read how we protect your information in our <a href="{L('notice-of-privacy-practices')}">Notice of Privacy Practices</a>.</p>
  <div class="actions"><a class="btn btn-sun" href="{PORTAL}" rel="noopener">{ICON['portal']}Go to the patient portal</a></div></aside>
</div></section>"""


def pay(L, A):
    return page_hero(L, "Pay a bill", "Pay your Black Canyon Community Health Center statement online in a few minutes.", [("Pay a bill", None)]) + f"""
<section class="band"><div class="wrap split">
  <div class="prose">
    <h2>Pay online</h2>
    <ol class="steps">
      <li><span>Have your paper or emailed statement ready. You'll need the details printed on it.</span></li>
      <li><span>Select <strong>Pay my bill</strong> below. Payments are handled securely by athenahealth.</span></li>
      <li><span>Enter your statement details and your card. You'll get a receipt by email.</span></li>
    </ol>
    <p><a class="btn btn-sun" href="{PAY}" rel="noopener">{ICON['card']}Pay my bill</a></p>
    <p>You can also pay in the <a href="{PORTAL}" rel="noopener">patient portal</a> or at the front desk of either clinic.</p>
  </div>
  <div class="prose">
    <h2>Need help with a bill?</h2>
    <p>Questions about a charge or a payment plan? Call the clinic where you were seen: Black Canyon City <a href="tel:+16233740200">(623) 374-0200</a> or Spring Valley <a href="tel:+19284048004">(928) 404-8004</a>.</p>
    <p>If your household income is at or below 200% of the federal poverty guidelines, you may qualify for our <a href="{L('sliding-fee-discount-program')}">sliding fee discount</a>. Our staff can also help you apply for AHCCCS.</p>
    <h3>Insurance</h3>
    <p>We bill Medicare, AHCCCS (Arizona Medicaid) and private insurance. Call your clinic to check that we're in network with your plan.</p>
  </div>
</div></section>"""


def services(L, A):
    groups = [
        ("Everyone", ["Treatment of acute illnesses, such as sore throat or flu, and injuries",
                      "Management of chronic conditions, including high blood pressure, high cholesterol, diabetes, allergies, heart disease and asthma",
                      "Annual exams and physicals", "Care for several related health conditions at once", "Immunizations",
                      "Weight management", "Help quitting smoking"]),
        ("Women", ["Well-woman exams", "Gynecological care", "Family planning", "Hormone management"]),
        ("Children", ["Well-child checkups", "Vaccines", "Sick visits for sore throat, flu and other illnesses"]),
        ("Ages 65+", ["Medicare Annual Wellness Visits", "Help enrolling in Medicare", "Age-specific screenings"]),
        ("Behavioral health", ["Screening for depression and anxiety during primary care visits",
                               "Referrals to counseling and substance use treatment in the community"]),
        ("Help getting care", ["Translation services", "Insurance and eligibility help", "Help enrolling in AHCCCS and other public programs",
                               "Referrals to partner providers for dental and prenatal care, and to specialists",
                               f'Our <a href="{L("sliding-fee-discount-program")}">Sliding Fee Discount Program</a>']),
    ]
    blocks = "".join(f"<div><h2 style=\"font-size:var(--s-3)\">{g}</h2><ul>{''.join(f'<li>{i}</li>' for i in items)}</ul></div>" for g, items in groups)
    return page_hero(L, "Primary care services", "Family medicine for every stage of life at our clinics in Black Canyon City and Mayer.", [("Services", None)]) + f"""
<section class="band"><div class="wrap">
  <div class="service-list">{blocks}</div>
</div></section>
<section class="band alt"><div class="wrap">
  <div class="section-head"><p class="eyebrow">More about our care</p><h2>Primary care that follows you over time</h2></div>
  <div class="service-list">
    <div><h3>A provider who knows you</h3><p>Seeing the same care team visit after visit means fewer repeated questions and care that fits your whole history, not just today's symptom.</p></div>
    <div><h3>Ongoing care for chronic conditions</h3><p>For diabetes, high blood pressure, high cholesterol, asthma and heart disease, we track your numbers, adjust medications and plan regular follow-ups so problems are caught early.</p></div>
    <div><h3>Prevention at every age</h3><p>Well-child checkups and vaccines, well-woman exams, adult physicals and Medicare Annual Wellness Visits keep screenings up to date.</p></div>
    <div><h3>Help with the whole picture</h3><p>Many patients manage more than one condition. We look at how they affect each other and keep your medications and care plan in one place.</p></div>
    <div><h3>Mental health matters too</h3><p>We screen for depression and anxiety as part of primary care and connect you with counseling in the community when you need more support.</p></div>
    <div><h3>Close to home</h3><p>Our clinics serve Black Canyon City, Mayer and nearby rural communities, so you don't have to drive to Phoenix or Prescott for everyday care.</p></div>
  </div>
</div></section>
<section class="band"><div class="wrap"><div class="callout"><div><h2>Not sure if we can help?</h2><p>Call either clinic and ask. If we don't offer a service, we'll help you find a provider who does.</p></div>
<div class="hero-ctas" style="margin-top:0"><a class="btn btn-sun" href="{L('schedule-appointment')}">Book an appointment</a></div></div></div></section>"""


def locations(L, A):
    return page_hero(L, "Clinic locations", "Two clinics open now in Black Canyon City and Mayer, with a third opening soon in Camp Verde.", [("Locations", None)]) + f"""
<section class="band"><div class="wrap"><div class="loc-grid">{loc_card(L, 'black-canyon')}{loc_card(L, 'spring-valley')}{loc_card(L, 'camp-verde')}</div>
<p style="margin-top:1.5rem;color:var(--muted)">All hours are Arizona time. Fax for both clinics: {FAX}.</p></div></section>"""


def location_page(key):
    def body(L, A):
        c = CLINICS[key]
        if key == "camp-verde":
            return page_hero(L, "Camp Verde clinic", "Opening soon at 385 S. Main Street, Camp Verde.", [("Locations", "locations"), ("Camp Verde", None)]) + f"""
<section class="band"><div class="wrap split">
  <div class="prose">
    <h2>Primary care is coming to the Verde Valley</h2>
    <p>{ORG} is opening its third clinic on Main Street in Camp Verde. We'll offer the same family medicine and preventive care available at our other clinics.</p>
    <p>Hours, a phone number and online booking will be posted on this page when the clinic opens. Until then, Camp Verde residents are welcome at either of our current clinics.</p>
    <p><a class="btn btn-line" href="{L('locations')}">See our open clinics</a></p>
  </div>
  <article class="loc"><span class="status soon">Opening soon</span><h3>Camp Verde Clinic</h3><div class="meta"><span>{c['street']}</span><span>{c['city']}, AZ {c['zip']}</span></div>
  <div class="actions"><a class="btn btn-line" href="{c['maps']}" rel="noopener">{ICON['pin']}Map</a></div></article>
</div></section>"""
        other = "spring-valley" if key == "black-canyon" else "black-canyon"
        return page_hero(L, f"{c['full']}", f"Primary care for {c['nearby']}.", [("Locations", "locations"), (c["name"], None)]) + f"""
<section class="band"><div class="wrap split">
  <div class="prose">
    <h2>Visit us</h2>
    <p><strong>{ORG}</strong><br>{c['street']}<br>{c['city']}, AZ {c['zip']}</p>
    <p>Phone <a href="tel:{c['tel']}">{c['phone']}</a><br>Fax {FAX}</p>
    <p class="actions" style="display:flex;flex-wrap:wrap;gap:.6rem"><a class="btn btn-sun" href="{c['sched']}" rel="noopener">{ICON['cal']}Book online</a><a class="btn btn-line" href="{c['maps']}" rel="noopener">{ICON['pin']}Get directions</a></p>
    <h3>Services at this clinic</h3>
    <p>Family medicine for all ages: sick visits, chronic disease care, physicals, immunizations, well-child and well-woman exams, and Medicare wellness visits. <a href="{L('services')}">See all services</a>.</p>
    <p>Patients with or without insurance are welcome. Ask about our <a href="{L('sliding-fee-discount-program')}">sliding fee discount</a>.</p>
  </div>
  <article class="loc"><span class="status" data-status="{key}">Mon–Fri</span><h2 style="font-size:var(--s-3)">Hours</h2>{hours_table(key)}<p style="font-size:.92rem;color:var(--muted)">Arizona time. Closed Saturday, Sunday and major holidays.</p></article>
</div></section>
<section class="band alt"><div class="wrap"><p>Also nearby: our <a href="{L('locations/' + other)}">{CLINICS[other]['full']}</a>.</p></div></section>"""
    return body


PROVIDERS = [
    ("Randy C. Hancock, DO", "Physician · Chief Executive Officer and Chief Medical Officer",
     "Dr. Hancock founded the clinic in Black Canyon City in 1999 to give the community a place to get care regardless of ability to pay. He continues to see patients and leads the health center's medical staff."),
    ("Matthew McElroy, PA-C", "Physician Assistant · Family medicine",
     "Matt earned his bachelor's degree from Tabor College in 2015 and his Master of Science in Physician Assistant Studies from A.T. Still University. He returned to Black Canyon Community Health Center in 2021 and focuses on whole-person, evidence-based family medicine."),
    ("Jodi Palmer, FNP", "Family Nurse Practitioner",
     "Jodi was born and raised in Arizona and has practiced primary care for nearly ten years. She treats every patient as an individual and works with them as a partner toward their best health. She is married with three daughters."),
    ("Isabella Quezada, PA-C", "Physician Assistant · Family medicine",
     "Isabella is an Arizona native. She earned a bachelor's degree in biology from the Grand Canyon University Honors College and a Master of Science in Physician Assistant Studies from A.T. Still University. She provides whole-person care to Black Canyon City and nearby communities."),
    ("Alexa Scanlan, PA-C", "Physician Assistant · Family and emergency medicine",
     "Alexa is a board-certified physician assistant with experience in family and emergency medicine. She believes in relationship-centered primary care and in being a trusted advocate for her patients and their families. She lives in Dewey."),
    ("Shea Green, PA-C", "Physician Assistant · Primary care",
     "Shea is an Arizona native and board-certified physician assistant with more than six years of experience in ENT, pediatric primary care and pediatric emergency medicine. She earned her Master of Physician Assistant Studies from Northern Arizona University and values lasting relationships with patients and families."),
]


def providers(L, A):
    cards = ""
    for name, role, bio in PROVIDERS:
        parts = name.split(",")[0].split()
        initials = parts[0][0] + parts[-1][0]
        slug = name.split(",")[0].lower().replace(".", "").replace(" ", "-")
        cards += f'<article class="provider" id="{slug}">{avatar(A, name, " avatar-lg")}<div><h2 style="font-size:var(--s-3)">{name}</h2><p class="role">{role}</p>{f"<p>{bio}</p>" if bio else ""}</div></article>'
    return page_hero(L, "Our providers", "A physician, physician assistants and nurse practitioners who live and work in the communities they serve.", [("Providers", None)]) + f"""
<section class="band"><div class="wrap"><div class="provider-grid">{cards}</div>
<p style="margin-top:1.75rem">To see a specific provider, <a href="{L('schedule-appointment')}">book online or call your clinic</a>.</p></div></section>"""


FPG = [(1, 15960), (2, 21640), (3, 27320), (4, 33000), (5, 38680), (6, 44360), (7, 50040), (8, 55720)]


def sliding(L, A):
    def m(n):
        return f"${n:,}"
    rows = ""
    for size, base in FPG:
        b = [round(base * p) for p in (1, 1.25, 1.5, 1.75, 2)]
        cells = [f"$0 – {m(b[0])}"] + [f"{m(b[i-1] + 1)} – {m(b[i])}" for i in range(1, 5)]
        rows += f"<tr><th scope=\"row\">{size}</th>{''.join(f'<td>{x}</td>' for x in cells)}</tr>"
    opts = "".join(f'<option value="{n}">{n} {"person" if n == 1 else "people"}</option>' for n in range(1, 13))
    return page_hero(L, "Sliding Fee Discount Program", "If your household income is at or below 200% of the federal poverty guidelines, you pay a reduced, flat fee for your visit.", [("Sliding fee discount", None)]) + f"""
<section class="band"><div class="wrap split wide-left">
  <div class="prose">
    <h2>How it works</h2>
    <p>Our goal is to remove cost as a reason to skip care, especially for patients and families at or below 200% of the Federal Poverty Guidelines. The discount is based only on household size and income. It's available to everyone who qualifies, whether or not you have insurance.</p>
    <ol class="steps">
      <li><span>Pick up a sliding fee application at the front desk of either clinic.</span></li>
      <li><span>Bring it back with proof of household income, such as recent pay stubs, a tax return or a benefits letter.</span></li>
      <li><span>We'll tell you your discount level. You pay that fee at each visit.</span></li>
    </ol>
    <p>Insured patients who qualify never pay more than the sliding fee amount for their visit. Our staff can also help you see if you qualify for AHCCCS.</p>
  </div>
  <form class="calc" id="sfdp-calc" aria-labelledby="calc-h">
    <h2 id="calc-h" style="font-size:var(--s-3)">Estimate your discount</h2>
    <div class="fields">
      <label for="sfdp-size">Household size<select id="sfdp-size">{opts}</select></label>
      <label for="sfdp-income">Yearly household income<input id="sfdp-income" inputmode="numeric" placeholder="$30,000" autocomplete="off"></label>
    </div>
    <div class="calc-result" id="sfdp-result" aria-live="polite"><span class="tier">Enter your household income</span></div>
    <small>An estimate only. Your discount is confirmed when we review your application. Nothing you type here is saved or sent.</small>
  </form>
</div></section>
<section class="band alt"><div class="wrap">
  <div class="section-head"><h2>2026 sliding fee scale</h2><p>Based on the 2026 Federal Poverty Guidelines. Yearly household income by discount level. For households larger than 8, add $5,680 per person to each 100% limit.</p></div>
  <div class="table-scroll"><table class="fee-table"><caption class="sr-only">Income ranges by household size and discount level</caption>
    <thead><tr><th scope="col">Household size</th><th scope="col">A · 0–100%</th><th scope="col">B · 101–125%</th><th scope="col">C · 126–150%</th><th scope="col">D · 151–175%</th><th scope="col">E · 176–200%</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
  <h3 style="margin-top:2rem;margin-bottom:1rem">What you pay</h3>
  <div class="table-scroll"><table class="fee-table"><caption class="sr-only">Nominal fees by discount level</caption>
    <thead><tr><th scope="col">Service</th><th scope="col">A</th><th scope="col">B</th><th scope="col">C</th><th scope="col">D</th><th scope="col">E</th></tr></thead>
    <tbody>
      <tr><th scope="row">Primary care and mental health</th><td>$20</td><td>$25</td><td>$30</td><td>$35</td><td>$40</td></tr>
      <tr><th scope="row">Lab and radiology</th><td>$10</td><td>$10 + 20%</td><td>$10 + 40%</td><td>$10 + 60%</td><td>$10 + 80%</td></tr>
      <tr><th scope="row">Dental (by referral)</th><td>$30</td><td>$45</td><td>$60</td><td>$75</td><td>$90</td></tr>
      <tr><th scope="row">OB/GYN (by referral)</th><td>$20</td><td>$20 + 20%</td><td>$20 + 40%</td><td>$20 + 60%</td><td>$20 + 80%</td></tr>
    </tbody></table></div>
  <p style="margin-top:1rem;color:var(--muted);max-width:75ch">You pay the nominal fee or the full charge, whichever is less. Fees are due at the time of your visit. For dental, OB/GYN and radiology referrals, you pay your discounted amount at our front desk and we pay the outside provider for you. Lab discounts are applied directly by the lab.</p>
</div></section>"""


def careers(L, A):
    reasons = [
        ("pulse", "Mission-driven care", "Join a nonprofit community health center that has cared for rural central Arizona since 1999, for patients with or without insurance."),
        ("senior", "Loan repayment eligibility", "We are a National Health Service Corps-approved site, so eligible clinicians may qualify for NHSC student loan repayment."),
        ("pin", "A growing organization", "We served 3,100 patients in 2025, up 14% from 2024, and are opening a third clinic in Camp Verde."),
        ("cal", "Weekday schedules", "Our clinics are open Monday through Friday, with no weekend clinic hours."),
    ]
    tiles = "".join(f'<div class="svc"><span class="chip">{ICON[i]}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in reasons)
    mail = f"mailto:{EMAIL}?subject=Employment%20inquiry"
    hero = page_hero(L, "Join our team", "We're always planning ahead for providers, medical assistants and front desk staff, even when no position is posted.", [("Careers", None)])
    hero = hero.replace('</p></div><svg class="landscape"', f'</p><div class="hero-ctas" style="margin-top:.6rem"><a class="btn btn-sun" href="{mail}">{ICON["portal"]}Email your resume</a></div></div><svg class="landscape"', 1)
    return hero + f"""
<div class="wrap quick"><div class="apply-card">
  <div class="apply-head"><p class="eyebrow">How to apply</p><h2>Three quick steps</h2></div>
  <ol class="apply-steps">
    <li><strong>Write a short cover letter</strong><span>Tell us which role interests you: provider, medical assistant or front desk.</span></li>
    <li><strong>Attach your resume</strong><span>Include your licenses or certifications if you have them.</span></li>
    <li><strong>Email it to us</strong><span><a href="{mail}">{EMAIL}</a></span></li>
  </ol>
</div></div>
<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Why work with us</p><h2>Meaningful work, close to home</h2><p>Our providers and staff get to know their patients and make a real difference in small communities.</p></div>
  <div class="svc-grid staff-grid">{tiles}</div>
</div></section>"""


def about(L, A):
    return page_hero(L, "About us", "To reduce barriers to care and to inspire hope, health and vitality.", [("About us", None)]) + f"""
<section class="band"><div class="wrap split wide-left">
  <div class="prose">
    <h2>A community clinic that grew with its community</h2>
    <p>{ORG}, Inc. is a 501(c)(3) nonprofit that provides general and preventive health care that is accessible to all. Our mission is to reduce barriers to care and to inspire hope, health and vitality.</p>
    <p>Dr. Randy Hancock, a primary care physician, founded the clinic in 1999 as a small-town practice in Black Canyon City. He wanted everyone in the area to have a place to get care, regardless of their ability to pay.</p>
    <p>We serve rural communities across central Yavapai County, where getting to a doctor can mean a long drive. Our team of a physician, physician assistants and nurse practitioners brings everyday primary care closer to home, and visiting specialists provide some care on site.</p>
    <h3>Our history</h3>
    <ul>
      <li><strong>1999</strong> · Opens as a small-town primary care clinic in Black Canyon City.</li>
      <li><strong>2008</strong> · Becomes a 501(c)(3) nonprofit and a National Health Service Corps-approved site.</li>
      <li><strong>2022</strong> · Recognized as a Federally Qualified Health Center Look-Alike in August.</li>
      <li><strong>2026</strong> · Awarded HRSA Health Center Program funding to open a third clinic in Camp Verde.</li>
    </ul>
  </div>
  <div class="about-side"><figure class="photo-card"><img src="{A('img/clinic-building.jpg')}" alt="Black Canyon Community Health Center clinic building" width="1140" height="646" loading="lazy"></figure>
  <div class="stats" style="grid-template-columns:minmax(0,1fr);margin-top:0">
    <div><strong>3,100</strong><span>Patients served in 2025, up 14% from 2024</span></div>
    <div><strong>13,594</strong><span>Patient visits in 2025</span></div>
    <div><strong>3</strong><span>Clinics, with Camp Verde opening soon</span></div>
  </div></div>
</div></section>
<section class="band alt"><div class="wrap prose">
  <h2>Contact us</h2>
  <p>Questions, compliments or concerns: <a href="mailto:{EMAIL}">{EMAIL}</a>. You can also call <a href="tel:+16233740200">(623) 374-0200</a> or <a href="tel:+19284048004">(928) 404-8004</a>.</p>
  <p>Help us plan for the community's needs by taking our short <a href="{SURVEY}" rel="noopener">community survey</a>.</p>
</div></section>"""


def employees(L, A):
    links = [
        ("Gmail", "Work email and Google Drive. Sign in with your @blackcanyonhealth.com account.", "https://mail.google.com/", "portal"),
        ("athenaOne", "Our electronic health record, scheduling and billing system.", "https://athenanet.athenahealth.com/", "clip"),
        ("Relias", "Required trainings and continuing education.", "https://login.reliaslearning.com/", "senior"),
        ("Paychex Flex", "Pay stubs, time clock and benefits.", "https://myapps.paychex.com/", "card"),
    ]
    tiles = "".join(f'<a class="svc staff-link" href="{u}" rel="noopener"><span class="chip">{ICON[i]}</span><h3>{t}</h3><p>{d}</p></a>' for t, d, u, i in links)
    return page_hero(L, "Employee resources", "For Black Canyon Community Health Center staff.", [("Employee resources", None)]) + f"""
<section class="band"><div class="wrap">
  <div class="section-head"><h2>Staff links</h2></div>
  <div class="svc-grid staff-grid">{tiles}</div>
</div></section>
<section class="band alt"><div class="wrap split">
  <div class="prose">
    <h2>Paychex registration</h2>
    <ol>
      <li>Go to <a href="https://www.paychex.com/login" rel="noopener">Paychex.com/login</a>.</li>
      <li>Click "Paychex Flex."</li>
      <li>Click "New to Paychex Flex? <a href="https://register.flex.paychex.com/" rel="noopener">Sign up</a>."</li>
      <li>Enter your information. Your account will be linked to our business.</li>
    </ol>
    <p>If there is a mismatch of information, you will receive a message to contact your administration. Please contact your site supervisor to verify that your email, SSN and date of birth are correct in our payroll system.</p>
    <p>It may take a few days until you are able to clock in and out, as we will need to enable those location-based permissions.</p>
  </div>
  <div class="prose">
    <h2>Policies and procedures</h2>
    <p>To view our policies, make sure you are logged in to your work email. They are available only to people with an @blackcanyonhealth.com email address.</p>
    <p><a href="https://drive.google.com/drive/folders/1P91TT00x3WzSSuUafIxX7pyxTzqX4Nv5" rel="noopener">BCCHC Policies and Procedures</a> (Clinical, Fiscal and Human Resources)</p>
    <h2>Casual Fridays</h2>
    <p>On Fridays, employees are welcome to wear company-branded t-shirts. This is optional. Shirts can be purchased at cost from our <a href="{MERCH}" rel="noopener">merchandise store</a>.</p>
  </div>
</div></section>"""


def nondiscrimination(L, A):
    return page_hero(L, "Nondiscrimination notice", "Language assistance and accessibility services are available free of charge.", [("Nondiscrimination notice", None)]) + f"""
<section class="band"><div class="wrap prose">
  <p>{ORG}, Inc. complies with applicable federal civil rights laws and does not discriminate on the basis of race, color, national origin, age, disability or sex (including sexual orientation and gender identity). We do not exclude people or treat them differently because of these characteristics.</p>
  <p>We provide free aids and services to people with disabilities to communicate effectively with us, and free language services, including qualified interpreters, to people whose primary language is not English.</p>
  <p>If you need these services, or believe we have failed to provide them or discriminated in another way, contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:+16233740200">(623) 374-0200</a>. You can also file a civil rights complaint with the U.S. Department of Health and Human Services, Office for Civil Rights, at <a href="https://ocrportal.hhs.gov/ocr/portal/lobby.jsf" rel="noopener">ocrportal.hhs.gov</a> or 1-800-368-1019.</p>
  <p lang="es"><strong>Español:</strong> Si habla español, tiene a su disposición servicios gratuitos de asistencia lingüística. Llame al (623) 374-0200.</p>
</div></section>"""


def privacy(L, A):
    def item(t, body):
        return f"<p><strong>{t}</strong> {body}</p>"
    return page_hero(L, "Notice of Privacy Practices", "This notice describes how medical information about you may be used and disclosed and how you can access this information. Please review it carefully.", [("Notice of Privacy Practices", None)]) + f"""
<section class="band"><div class="wrap prose">
  <p class="notice">Effective October 2026. ¿Necesita este aviso en español u otro idioma? Pídalo en la recepción. Le ayudamos sin costo.</p>
  <p>Black Canyon Community Health Center, Inc. (“BCCHC”) is required by law to protect the privacy and security of your protected health information (“PHI”), provide you with this Notice of Privacy Practices, and follow the terms of this notice currently in effect. Protected health information includes information that identifies you and relates to your past, present, or future physical or mental health condition, healthcare services, or payment for healthcare services.</p>
  <h2>How we may use and disclose your health information</h2>
  <p>BCCHC may use and disclose your health information for purposes permitted or required by law, including the following:</p>
  {item("Treatment.", "We may use and share your information with physicians, nurses, pharmacies, laboratories, hospitals, specialists, referral providers, behavioral health providers, and other healthcare professionals involved in your care and treatment.")}
  {item("Payment.", "We may use and disclose your information to bill and collect payment from you, your insurance company, AHCCCS, Medicare, Medicaid, or other third parties responsible for payment of your healthcare services.")}
  {item("Healthcare Operations.", "We may use your information for clinic operations such as quality improvement activities, care coordination, staff training, accreditation, licensing, credentialing, compliance, auditing, and general administrative activities.")}
  {item("Appointment Reminders and Communication.", "We may contact you by phone, voicemail, text message, email, mail, or patient portal regarding:")}
  <ul><li>Appointment reminders</li><li>Test results</li><li>Treatment recommendations</li><li>Referral coordination</li><li>Billing matters</li><li>Healthcare-related services and benefits</li></ul>
  {item("Individuals Involved in Your Care.", "Unless you object, we may disclose relevant information to family members, caregivers, guardians, or other individuals involved in your care or payment for your care.")}
  {item("Business Associates.", "We may share information with third-party service providers who perform services on behalf of BCCHC, including billing companies, electronic health record vendors, consultants, attorneys, accountants, collection agencies, and other business associates as permitted by law.")}
  {item("Public Health and Safety.", "We may disclose information when required for public health activities, disease reporting, abuse or neglect reporting, health oversight activities, FDA reporting, or to prevent a serious threat to health or safety.")}
  {item("Legal Requirements and Law Enforcement.", "We may disclose information when required by federal, state, or local law, court orders, subpoenas, warrants, investigations, or other lawful processes.")}
  {item("Research.", "Certain limited uses and disclosures may occur for research purposes when approved or permitted by law.")}
  {item("Workers’ Compensation.", "We may disclose information as authorized by workers’ compensation laws and similar programs.")}
  {item("Fundraising.", "BCCHC may contact you regarding fundraising activities supporting clinic operations. You may opt out of receiving fundraising communications at any time.")}
  {item("Electronic Communications.", "While BCCHC takes reasonable precautions to protect privacy, electronic communications such as email and text messaging may carry some security risks.")}
  <h2>Your rights regarding your health information</h2>
  <p>You have the right to:</p>
  <ul>
    <li><strong>Request Restrictions.</strong> Request restrictions on certain uses and disclosures of your information. BCCHC is not required to agree to all requested restrictions except as required by law.</li>
    <li><strong>Request Confidential Communications.</strong> Request that we communicate with you by alternative means or at alternative locations.</li>
    <li><strong>Access Your Records.</strong> Inspect and obtain copies of your medical records as permitted by law. Reasonable fees may apply.</li>
    <li><strong>Request Amendments.</strong> Request corrections or amendments to your medical records if you believe information is inaccurate or incomplete.</li>
    <li><strong>Receive an Accounting of Disclosures.</strong> Request a list of certain disclosures made outside of treatment, payment, and healthcare operations.</li>
    <li><strong>Obtain a Copy of This Notice.</strong> Receive a paper or electronic copy of this Notice upon request.</li>
    <li><strong>File a Complaint.</strong> File a complaint if you believe your privacy rights have been violated without fear of retaliation.</li>
  </ul>
  <h2>Complaints and contact information</h2>
  <p>If you have questions regarding this Notice or wish to file a privacy complaint, please contact: Black Canyon Community Health Center, Inc., 19251 E. Oasis Dr., Black Canyon City, AZ 85324. Phone: <a href="tel:+16233740200">(623) 374-0200</a>. Email: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <p>Patients may also file complaints with the U.S. Department of Health and Human Services Office for Civil Rights. Filing a complaint will not affect your care or services.</p>
  <h2>Our responsibilities</h2>
  <p>BCCHC is required by law to:</p>
  <ul><li>Maintain the privacy and security of your protected health information</li><li>Provide you with this Notice of Privacy Practices</li><li>Notify you following a breach of unsecured protected health information when required by law</li><li>Follow the terms of the Notice currently in effect</li></ul>
  <p>BCCHC reserves the right to revise or update this Notice at any time. Revised notices may apply to all protected health information maintained by the clinic and will be made available upon request and posted as required by law.</p>
  <p style="color:var(--muted)">Black Canyon Community Health Center, Inc. · Notice of Privacy Practices · Rev. 10/2026. <a href="{A('notice-of-privacy-practices.pdf')}" download>Download the printable PDF</a>.</p>
</div></section>"""


def not_found(L, A):
    return page_hero(L, "Page not found", "That page may have moved when we updated our website.", None) + f"""
<section class="band"><div class="wrap prose"><p>Try one of these: <a href="{L('')}">Home</a> · <a href="{L('schedule-appointment')}">Book an appointment</a> · <a href="{L('locations')}">Locations</a> · <a href="{L('patient-portal')}">Patient portal</a> · <a href="{L('pay-my-bills')}">Pay a bill</a></p></div></section>"""


# ----------------------------------------------------------------- registry
PAGES = [
    {"slug": "", "body": home,
     "title": "Black Canyon Community Health Center | Primary Care in Yavapai County, AZ",
     "description": "Nonprofit family medicine for rural central Arizona, with clinics in Black Canyon City and Mayer and Camp Verde opening soon. Medicare, AHCCCS, private insurance and uninsured patients welcome.",
     "jsonld": graph(ORG_LD, clinic_ld("black-canyon"), clinic_ld("spring-valley"), clinic_ld("camp-verde"))},
    {"slug": "schedule-appointment", "body": schedule,
     "title": "Book an Appointment | Black Canyon Community Health Center",
     "description": "Book a primary care appointment online at our Black Canyon City or Spring Valley (Mayer) clinic, or call (623) 374-0200 or (928) 404-8004. New patients welcome.",
     "jsonld": graph(crumbs_ld(("Home", ""), ("Book an appointment", "schedule-appointment")))},
    {"slug": "patient-portal", "body": portal,
     "title": "Patient Portal | Black Canyon Community Health Center",
     "description": "Log in to the Black Canyon Community Health Center patient portal to message your care team, see test results, request appointments and pay your bill.",
     "jsonld": graph(crumbs_ld(("Home", ""), ("Patient portal", "patient-portal")))},
    {"slug": "pay-my-bills", "body": pay,
     "title": "Pay a Bill Online | Black Canyon Community Health Center",
     "description": "Pay your Black Canyon Community Health Center statement securely online. Questions about a bill or need a discount? We can help.",
     "jsonld": graph(crumbs_ld(("Home", ""), ("Pay a bill", "pay-my-bills")))},
    {"slug": "services", "body": services,
     "title": "Primary Care Services | Black Canyon Community Health Center",
     "description": "Family medicine in Black Canyon City and Mayer, AZ: sick visits, diabetes and blood pressure care, physicals, vaccines, well-child and well-woman exams, and Medicare wellness visits.",
     "jsonld": graph(crumbs_ld(("Home", ""), ("Services", "services")))},
    {"slug": "locations", "body": locations,
     "title": "Clinic Locations & Hours | Black Canyon Community Health Center",
     "description": "Hours, phone numbers and directions for our clinics in Black Canyon City (19251 E. Oasis Dr.) and Mayer (17301 E. Spring Valley Rd.), plus Camp Verde, opening soon.",
     "jsonld": graph(crumbs_ld(("Home", ""), ("Locations", "locations")))},
    {"slug": "locations/black-canyon", "body": location_page("black-canyon"),
     "title": "Black Canyon City Clinic | Family Doctor in Black Canyon City, AZ",
     "description": "Primary care at 19251 E. Oasis Drive, Black Canyon City, AZ 85324. Open Monday–Friday, evenings until 7 pm Tue & Thu. Call (623) 374-0200 or book online.",
     "jsonld": graph(clinic_ld("black-canyon"), crumbs_ld(("Home", ""), ("Locations", "locations"), ("Black Canyon City", "locations/black-canyon")))},
    {"slug": "locations/spring-valley", "body": location_page("spring-valley"),
     "title": "Spring Valley Clinic | Family Doctor in Mayer, AZ",
     "description": "Primary care at 17301 E. Spring Valley Road, Suite G, Mayer, AZ 86333. Open Monday–Friday, until 7 pm on Wednesdays. Call (928) 404-8004 or book online.",
     "jsonld": graph(clinic_ld("spring-valley"), crumbs_ld(("Home", ""), ("Locations", "locations"), ("Spring Valley", "locations/spring-valley")))},
    {"slug": "locations/camp-verde", "body": location_page("camp-verde"),
     "title": "Camp Verde Clinic (Opening Soon) | Black Canyon Community Health Center",
     "description": "Black Canyon Community Health Center is opening a primary care clinic at 385 S. Main Street, Camp Verde, AZ 86322. Family medicine for every age, for patients with or without insurance.",
     "jsonld": graph(clinic_ld("camp-verde"), crumbs_ld(("Home", ""), ("Locations", "locations"), ("Camp Verde", "locations/camp-verde")))},
    {"slug": "providers", "body": providers,
     "title": "Our Providers | Black Canyon Community Health Center",
     "description": "Meet the physician, physician assistants and nurse practitioners providing primary care at Black Canyon Community Health Center in Black Canyon City and Mayer, AZ.",
     "jsonld": graph(crumbs_ld(("Home", ""), ("Providers", "providers")))},
    {"slug": "sliding-fee-discount-program", "body": sliding,
     "title": "Sliding Fee Discount Program | Affordable Care in Yavapai County",
     "description": "Income-based discounts for patients at or below 200% of the federal poverty guidelines. Primary care visits from $20. See the 2026 scale and estimate your discount.",
     "jsonld": graph(crumbs_ld(("Home", ""), ("Sliding fee discount", "sliding-fee-discount-program"))),
     "noindex": True},
    {"slug": "careers", "body": careers,
     "title": "Careers | Black Canyon Community Health Center",
     "description": "Work in rural Arizona primary care at an NHSC-approved community health center. Providers, medical assistants and front desk staff: send us your resume.",
     "jsonld": graph(crumbs_ld(("Home", ""), ("Careers", "careers")))},
    {"slug": "about-us", "body": about,
     "title": "About Us | Black Canyon Community Health Center",
     "description": "A nonprofit Federally Qualified Health Center founded in 1999 to make primary care accessible to everyone in rural Yavapai County, Arizona.",
     "jsonld": graph(ORG_LD, crumbs_ld(("Home", ""), ("About us", "about-us")))},
    {"slug": "employees", "body": employees, "noindex": True,
     "title": "Employee Resources | Black Canyon Community Health Center",
     "description": "Resources for Black Canyon Community Health Center employees."},
    {"slug": "nondiscrimination", "body": nondiscrimination,
     "title": "Nondiscrimination Notice | Black Canyon Community Health Center",
     "description": "Black Canyon Community Health Center does not discriminate. Free language assistance and accessibility services are available."},
    {"slug": "notice-of-privacy-practices", "body": privacy,
     "title": "Notice of Privacy Practices | Black Canyon Community Health Center",
     "description": "How Black Canyon Community Health Center may use and share your health information, your privacy rights, and how to file a complaint."},
    {"slug": "404", "body": not_found, "noindex": True,
     "title": "Page Not Found | Black Canyon Community Health Center",
     "description": "This page could not be found."},
]

SITE = {
    "chrome": chrome,
    "year": 2026,
    "updated": "2026-10-23",
    # old Google Site paths that no longer have their own page -> new page
    "redirects": {"home": "", "blog": ""},
}
