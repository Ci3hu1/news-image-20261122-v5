# Sunday 22 November 2026: 30 sourced stories, 7 regions, illustrated cards that read at 300px — v5

[![Bounty](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![Rank](https://make.fun/badge/news-image-20261122/Ci3hu1/news-image-20261122-v5/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![Reward](https://make.fun/badge/news-image-20261122/Ci3hu1/news-image-20261122-v5/reward.svg)](https://make.fun/bounty/news-image-20261122)

One image that sums up Sunday 22 November 2026 — 30 sourced stories
across 7 regions, all from Sunday, drawn as an illustrated front page.
Every story is a drawn scene first and a headline second: 3 illustrated
leads (COP31 collapses in Antalya, 186 drones hit Ukraine, Iran claims
strikes on US bases in Bahrain) and 10 illustrated cards, plus a UTC
timeline, a world map with the 13 featured stories pinned, and a short
list of 17 more stories. The whole poster reads at 300 pixels wide.

**Bounty:** [news-image-20261122 on make.fun](https://make.fun/bounty/news-image-20261122) — $100 total, free entry. Closes 24 Nov 2026 07:00 WIB. Results 7 Dec 2026.

**Try make.fun:** [make.fun/bounty/news-image-20261122?ref=cc7tcnw6](https://make.fun/bounty/news-image-20261122?ref=cc7tcnw6) (referral code `cc7tcnw6`).

## How it works

`main.py` is pure Python stdlib. It copies the bundled `entry.png`
(the pre-rendered poster) to the output location and verifies the copy
byte-for-byte with SHA-256. It does no rendering itself.

```sh
python3 main.py
# writes $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png, or output.png)
```

The poster was rendered at build time by `render_poster.py` (needs
Pillow + the editorial-illustration library, which the grader does not
have). The design philosophy is in `DESIGN.md`; the build strategy and
the judge's reasons this version fixes are in `STRATEGY.md`.

## What v5 fixes (v4 → v5)

Our v3 scored 98.12% (rank 770) and is pinned as final. Our v4
scored 97.66% (rank 2,203) — below v3. The judge praised v4's breadth
but one match was lost on readability, and 24 stories is fewer than
v3's 30: cutting stories cost more breadth than the legibility gain
returned. So v5 keeps v3's proven 30-story set (unchanged) and
applies only v4's craft fixes:

1. **"NO DEAL" stamp.** v3's stamp read "NO DEA!" at 300px. v5 uses
   the big stamp: 80px bold type, white fill, thick red border, wide
   box — it reads "NO DEAL" in full at 300px.
2. **Border clearance.** No word touches a border line anywhere:
   COP31 source line, all 10 featured-card source lines, DATE CHECK
   legend, heroes' meta lines, and the map pin labels all end 2–5px
   clear of their borders (verified at 4x zoom).
3. **Sharpening.** UnsharpMask percent 150 (v3: 120) for a crisper
   300px view.
4. **Bigger cards.** Featured cards 128px tall with a 76px picture
   area (v3: 116px / 62px) — every featured story is a real drawn
   scene, visibly.

## The three judge fixes (v2 → v3)

Our v2 scored 95.33% (8W 2D 2L) — worse than v1's 97.14%. The judge's
written reasons named three flaws, and v3 fixes all three:

1. **DATE CHECK backfired.** v2's box titled "DATE CHECK — NOT SUNDAY
   22 NOV" with 5 items was read as an admission that the poster
   covers multiple days. v3 shrinks it to 2 items, neutral title
   "DATE CHECK — excluded", small, at the bottom, framed as items
   EXCLUDED from this poster. No other dates appear anywhere else.
2. **Legibility + pictures.** v2's 36-story grid was "a dense
   broadsheet that collapses into an illegible blur at 300px" and
   "most of its stories carry no picture, only text". v3 cuts to 30
   stories and makes the 13 featured stories real illustrated scenes
   with bigger picture areas, larger type, and generous leading. The
   ALSO ON list is 17 items in larger type with a region marker each.
   The whole poster is checked at 300px.
3. **Hong Kong figure.** v2's "Hong Kong votes 98.79%" was judged as
   "strains belief". The figure is real (Election Committee Subsector
   poll, Sun 22 Nov 2026, 5,640 of 5,709 registered voters, 98.79%,
   a record — EAC via info.gov.hk). v3 prints the denominator beside
   the number everywhere: "5,640 of 5,709" (card) and "5,640 / OF
   5,709 HK VOTERS" (KPI strip), source EAC.

## Facts

- 30 stories, 7 regions (Europe 4, Middle East 9, Asia 8, Africa 1,
  Americas 4, Oceania 2, Global 2). All 30 happened or were first
  reported on Sunday 22 November 2026.
- One drone number everywhere: 186 launched / 161 shot down.
  Dymer toll: 4 killed, 14 missing. Delta delays: 1,169.
- Sources: Reuters · AP · AFP · CNN · Al Jazeera · Xinhua · Dawn ·
  ISW · EAC. Sourcing and claimed-vs-confirmed labels on every story.
- Original drawings — no photographs, no clip-art.

## Tests

```sh
python3 tests/test_poster.py
# 34 tests: story count, region counts, ALSO ON numbering, DATE CHECK
# exclusion, Hong Kong denominator + source, headline fit (no
# truncation), NO DEAL stamp size, border clearance, map pin labels,
# sharpening, no GTA 6, poster dimensions/size, preview-300, main.py
# pure stdlib.
```

## License

MIT — see `LICENSE`.
