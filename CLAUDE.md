# Working notes for Claude

Static portfolio site — no build step, no package manager. Edit files directly
and serve with `python -m http.server 8765`.

## Before you finish any change

```bash
python scripts/check_site.py
```

This is the same check CI runs. It must pass before anything is pushed.

## Conventions

- **Images**: WebP only. Resize on import (projects 900 px, certificates
  1600 px, education 1200 px, backgrounds 1920 px) and stay under 400 KB.
  Never commit a PNG screenshot straight from a camera or generator.
- **Vendor libraries**: `assets/vendor/` holds only files that are actually
  referenced. Do not restore `.map`, `.eot`, `.svg` or unminified copies.
  Before adding a library, check whether Bootstrap or Boxicons already covers it.
- **Icons**: Boxicons (`bx-*`) and RemixIcon (`ri-*`) only. Do not reintroduce
  IcoFont — it was removed for shipping 1.3 MB to render a single arrow.
- **Project pages**: one file per project in `projects/`, descriptive slug,
  built on the Problem / Approach / Results template with
  `assets/css/project.css`. They render inside a VenoBox iframe, so they are
  standalone documents with no site navigation.
- **Licensing**: content is all-rights-reserved. Do not add a `LICENSE` file;
  CI fails if one appears.
- **Privacy**: no phone numbers in any page — CI enforces this. Email and
  LinkedIn are the intended contact routes.

## Contact form

`#contactForm` posts JSON to whatever URL sits in its `data-endpoint` attribute.
That attribute is currently empty, so the form falls back to opening the
visitor's mail client via `mailto:`. To switch to a real backend (Formspree,
Getform, Basin or similar), put the endpoint URL in `data-endpoint` -- no other
change is needed.

## Outstanding

- `assets/img/certification/azure.webp` is referenced but missing; the Azure
  certificate image needs to be supplied.
- Certificates other than the Claude one have no verification links; add them
  as `.cert-verify` anchors when the owner supplies the URLs.
- Project pages 5-10 (sustainable-ai-agent, movie-recommendation,
  health-risk-prediction, customer-churn, taiwan-aqi, hotel-booking) carry
  descriptive copy written from their titles, not from source material. Pages
  1-4 are grounded in the CV. Replace 5-10 with real detail when available --
  and never add metrics that were not supplied.
- The self-hosted CV at `assets/cv/` contains a phone number. `robots.txt`
  disallows that path so it stays out of search indexes; keep that rule.

## Layout rules

Card grids must stay equal-height. Every grid uses `align-items: stretch`, its
cards are flex columns, and every card image sits in a fixed `aspect-ratio` box
with `object-fit`. Do not size images with inline pixel widths -- that is what
made the Education row look staggered. Never leave two `class` attributes on one
tag; the browser silently ignores the second.
