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

## Outstanding

- `assets/img/certification/azure.webp` is referenced but missing; the Azure
  certificate image needs to be supplied.
- All ten `projects/*.html` pages carry `TODO:` placeholders awaiting real
  Problem / Approach / Results copy from the site owner. Do not invent this
  content.
