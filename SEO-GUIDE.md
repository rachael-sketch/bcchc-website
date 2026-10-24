# blackcanyonhealth.com — how this site works

Static site for Black Canyon Community Health Center (BCCHC), hosted on GitHub Pages from the `docs/` folder, custom domain www.blackcanyonhealth.com.

## Editing
- All page text, titles, meta descriptions and structured data live in `pages.py`. Styles: `src/site.css`. Scripts (open-now status, sliding fee estimator): `src/site.js`.
- Clinic hours are in two places and must match: `CLINICS[...]["hours"]` in `pages.py` and `HOURS` in `src/site.js`.
- Sliding fee scale: `FPG` table and the "What you pay" table in `pages.py`, plus the tiers in `src/site.js`. Update when the board approves a new scale (new Federal Poverty Guidelines each January).
- Run `python3 build.py`. It writes `docs/` (the live site) and `preview/` (relative links, for claude.ai previews). Commit both `pages.py`/`src` changes and the rebuilt `docs/`.
- Page URLs match the old Google Site (/services, /locations/black-canyon, …) so existing Google rankings carry over. Don't rename slugs. If a page must move, add the old path to `SITE["redirects"]`.
- Homepage announcement banner: `ANNOUNCEMENT` in `pages.py` (has an end date; set to None when there's nothing to announce).
- Update `SITE["updated"]` (sitemap lastmod) whenever content changes.

## Rules
- Only facts BCCHC has published or Rachael has confirmed. No invented services, insurance plans, stats or reviews.
- Never claim FTCA/PHS deemed status unless HRSA has deemed BCCHC (check with Rachael).
- Keep wording plain, patient-facing, short sentences. Keep the design as is unless Rachael asks.
- Changes go on a branch with a pull request. Rachael approves by merging. Never push to `main` directly.
- `employees` page stays `noindex`.

## Monthly SEO checklist
1. Every page loads (200), no broken internal or external links (athena scheduling, portal, payment).
2. Facts current: providers, hours, phones, Camp Verde status, services (counseling ended Nov 1, 2026), sliding fee scale year, CEO.
3. Each page: unique title (≤ 65 chars ideal), meta description (≤ 160), one H1, image alt text, canonical, valid JSON-LD.
4. sitemap.xml lists every indexable page with current lastmod; robots.txt points to it.
5. Search visibility: search Google for the target terms below, note where BCCHC appears.
6. Suggest 1–3 small content improvements per month that target local searches (e.g., a short FAQ, a service people search for that BCCHC already provides).

Target searches: primary care Black Canyon City AZ · doctor Black Canyon City · family doctor Mayer AZ · clinic Spring Valley AZ · sliding fee clinic Yavapai County · community health center Camp Verde · doctor accepting AHCCCS near Mayer · Medicare wellness visit Black Canyon City.

## Off-site (Rachael or staff)
- Google Search Console: verify the domain and submit https://www.blackcanyonhealth.com/sitemap.xml.
- Google Business Profile for each clinic: correct hours, phone, website link to the matching /locations page, and add Camp Verde when it opens.
