# mohmuz14.github.io

Personal portfolio site for **Mohammed Muzeeb Shaik** — AI Engineer & GenAI Specialist.
Static HTML/CSS/JS, published with GitHub Pages at <https://mohmuz14.github.io>.

## Layout

```
index.html            single-page site (hero, about, experience, education,
                      certifications, projects, skills, achievements, contact)
projects/*.html       one detail page per project, opened in a VenoBox iframe
assets/css/           style.css (site) and project.css (detail pages)
assets/js/main.js     nav, filtering, counters, typed hero text
assets/img/           WebP imagery, grouped by section
assets/vendor/        third-party libraries, pruned to what is actually loaded
scripts/check_site.py pre-publish checks
```

## Run locally

```bash
python -m http.server 8765
```

Then open <http://localhost:8765>.

## Checks

```bash
python scripts/check_site.py
```

Runs in CI on every push and pull request. It fails the build on:

- broken internal links or missing images
- unfilled `TODO:` placeholders in `projects/*.html`
- images over 400 KB, or total image weight over 3 MB
- a phone number reappearing in any page
- `LICENSE` being reintroduced (see `COPYRIGHT.md`)

## Images

Source images are WebP, resized on import: projects 900 px wide, certificates
1600 px, education 1200 px, backgrounds 1920 px. Keep new images inside the
400 KB budget or CI will flag them.

## Licence

Original content is **all rights reserved** — see [COPYRIGHT.md](COPYRIGHT.md).
Bundled third-party libraries under `assets/vendor/` keep their own licences.
