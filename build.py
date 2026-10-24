#!/usr/bin/env python3
"""Builds the BCCHC website.

  dist/     production files for GitHub Pages (clean URLs that match the old Google Site)
  preview/  the same pages with relative .html links, for the claude.ai preview
"""
import json, os, shutil, html
from pages import PAGES, SITE

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://www.blackcanyonhealth.com"
FONTS = "https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..800&family=Source+Sans+3:wght@400;600;700&display=swap"


def link(slug, mode, depth):
    """URL for an internal page. slug '' = home. '#x' anchors allowed after slug."""
    anchor = ""
    if "#" in slug:
        slug, anchor = slug.split("#", 1)
        anchor = "#" + anchor
    if mode == "dist":
        return path_for(slug) + anchor
    prefix = "../" * depth
    return prefix + (slug + ".html" if slug else "index.html") + anchor


DIRS = {"locations"}  # slugs that also have child pages: served as folder/index.html


def path_for(slug):
    if not slug:
        return "/"
    return "/" + slug + ("/" if slug in DIRS else "")


def asset(name, mode, depth):
    return "/assets/" + name if mode == "dist" else "../" * depth + "assets/" + name


def render(page, mode):
    slug = page["slug"]
    depth = slug.count("/")
    L = lambda s: link(s, mode, depth)
    A = lambda n: asset(n, mode, depth)
    L.asset = A
    body = page["body"](L, A)
    canonical = DOMAIN + path_for(slug)
    ld = page.get("jsonld")
    ld_html = ""
    if ld:
        ld_html = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False, indent=1) + "</script>"
    robots = '<meta name="robots" content="noindex">' if page.get("noindex") else ""
    head = f"""<title>{html.escape(page['title'])}</title>
<meta name="description" content="{html.escape(page['description'])}">
<link rel="canonical" href="{canonical}">
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Black Canyon Community Health Center">
<meta property="og:title" content="{html.escape(page['title'])}">
<meta property="og:description" content="{html.escape(page['description'])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/assets/og-image.png">
<meta name="theme-color" content="#15213d">
<link rel="icon" href="{A('favicon-48.png')}" type="image/png" sizes="48x48">
<link rel="apple-touch-icon" href="{A('apple-touch-icon.png')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{A('site.css')}">
{ld_html}"""
    content = SITE["chrome"](L, A, page, body)
    full = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
</head>
<body>
{content}
<script src="{A('site.js')}" defer></script>
</body>
</html>
"""
    # Preview home page: the artifact host adds its own skeleton, so emit head bits + body only.
    preview_head = head.replace(f"<title>{html.escape(page['title'])}</title>", "<title>BCCHC New Website</title>", 1)
    bare = f"""{preview_head}
<meta name="claude:viewport-fit-sides" content="cover">
{content}
<script src="{A('site.js')}" defer></script>
"""
    return full, bare


def redirect(to, mode, depth):
    target = link(to, mode, depth)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Black Canyon Community Health Center</title>
<link rel="canonical" href="{DOMAIN}{'/' + to if to else '/'}"><meta http-equiv="refresh" content="0; url={target}">
<meta name="robots" content="noindex"></head><body><p><a href="{target}">Continue to Black Canyon Community Health Center</a></p></body></html>
"""


def main():
    for mode in ("dist", "preview"):
        out = os.path.join(ROOT, "docs" if mode == "dist" else "preview")
        shutil.rmtree(out, ignore_errors=True)
        os.makedirs(os.path.join(out, "assets"))
        for f in ("site.css", "site.js", "favicon-48.png", "favicon.png", "apple-touch-icon.png", "logo-white.png", "logo-navy.png", "og-image.png", "notice-of-privacy-practices.pdf"):
            src = os.path.join(ROOT, "src", f)
            if os.path.exists(src):
                shutil.copy(src, os.path.join(out, "assets", f))
        shutil.copytree(os.path.join(ROOT, "src", "img"), os.path.join(out, "assets", "img"))
        for page in PAGES:
            full, bare = render(page, mode)
            name = (page["slug"] or "index") + ".html"
            if mode == "dist" and page["slug"] in DIRS:
                name = page["slug"] + "/index.html"
            path = os.path.join(out, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            text = bare if (mode == "preview" and page["slug"] == "") else full
            with open(path, "w") as fh:
                fh.write(text)
        for old, new in SITE["redirects"].items():
            path = os.path.join(out, old + ".html")
            with open(path, "w") as fh:
                fh.write(redirect(new, mode, old.count("/")))
        if mode == "dist":
            with open(os.path.join(out, "CNAME"), "w") as fh:
                fh.write("www.blackcanyonhealth.com\n")
            with open(os.path.join(out, "robots.txt"), "w") as fh:
                fh.write(f"User-agent: *\nAllow: /\nDisallow: /employees\n\nSitemap: {DOMAIN}/sitemap.xml\n")
            urls = "".join(
                f"  <url><loc>{DOMAIN}{path_for(p['slug'])}</loc><lastmod>{SITE['updated']}</lastmod></url>\n"
                for p in PAGES if not p.get("noindex") and p["slug"] != "404")
            with open(os.path.join(out, "sitemap.xml"), "w") as fh:
                fh.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
            open(os.path.join(out, ".nojekyll"), "w").close()
    print("built", len(PAGES), "pages")


if __name__ == "__main__":
    main()
