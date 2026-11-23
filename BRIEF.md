# BRIEF — news-image-20261122 v5 (the fix for v4)

**Competition:** news-image-20261122 — "Sum up 22 November's world news in one image". $100 total (50 paid places), free entry. **Closes 24 Nov 2026 07:00 WIB** (2026-11-24T00:00:00Z). Results 7 Dec 2026. Harness program/v1, bundle-type (transcript bundle via kit CLI, no `record`).

**v3 live:** 981,243 (98.12%), 12W 0D 0L, rank 770/13,174 — BEST, PINNED as final.
**v4 live:** 976,591 (97.66%), 12W 0D 0L, rank 2,203 — BELOW v3 by 4,652.
**v5 is submission #5 of max 5 for this competition (last slot). Day cap taken 4 of 6.**

## Why v5 exists — v4 scored below v3

Read from `GET /api/submissions/01a20739-68a2-7739-995f-7446455a26aa`,
`scores[0].judge.heat.matches[].calls[].reason`. The judge praised
v4's breadth (24 stories / 7 regions) but one match was lost on
readability to a cleaner opponent, and 24 stories is fewer than v3's
30. LESSON: cutting 30 -> 24 stories cost more breadth (the judge's
criterion 2, after the date) than the legibility gain returned.

**v5 = v3's proven 30-story set (unchanged) + v4's craft fixes only:**

1. **"NO DEAL" stamp fixed (v4).** v3's stamp was 44px type inside a
   156px scene and read "NO DEA!" at 300px. v5 uses v4's stamp — 80px
   bold type, white fill, thick red border, wide box — inside a 180px
   scene, so it reads clearly at 300px. (v4 used a 220px scene; v5
   uses 180 — the stamp's final size depends on the type/scene ratio,
   so 180 keeps it readable while saving 20px for the ALSO ON list.)
2. **Border clearance (v4 + Joni, 23 Nov 13:56: no word may touch a
   border line).** Every text element ends 2-5px clear of its box
   border — COP31 source line (5px), all 10 featured-card source
   lines (3px), DATE CHECK legend (4px), heroes 2-3 meta (2px).
   Verified visually at 4x zoom. Map pin labels were also fixed: the
   46px-tall map pushed 5 northern pins' labels above the box top and
   onto the "WHERE IT HAPPENED" label (and pins 3/13 overlapped each
   other) — their offsets were retuned so every label sits inside the
   box with >=2px clearance and no two labels overlap.
3. **Sharpening (v4).** UnsharpMask percent 150 after the LANCZOS
   downscale (v3: 120), for a crisper 300px view.
4. **Bigger cards (v4).** Featured cards 128px tall with a 76px
   picture area (v3: 116px / 62px).

**Kept from v3 (judge-praised):** explicit date "Sunday 22 November
2026" (Criterion 1); broad coverage, 30 stories across 7 regions
(Criterion 2); sourcing + claimed-vs-confirmed labels; UTC timeline +
world map + big COP31 lead; header "ALL FROM SUNDAY" true (all 30
main-list stories are Sunday 22 Nov only); DATE CHECK shrunk to 2
items, neutral title "DATE CHECK — excluded", framed as excluded;
Hong Kong figure with denominator ("5,640 of 5,709", source EAC,
never a bare "98.79%"); one drone number (186 launched / 161 shot
down); Dymer toll "4 killed, 14 missing"; Delta delays "1,169".

**NO GTA 6 on this poster.** GTA 6's $3.79B first-day sales was
announced by Take-Two on FRIDAY 20 NOV 2026 (SEC 8-K filed 20 Nov;
CNN reported 20 Nov). It is NOT a 22 Nov story (enforced by test).

## Story list (30, 7 regions — identical to v3)

- Leads (3): COP31 collapses (Antalya), 186 drones / Dymer, Iran claims
  strikes on US bases in Bahrain.
- Featured (10): Benghazi ship blast, Sparta II towed, Hong Kong EC
  poll (5,640 of 5,709, source EAC), India 720/9 Pant 128, Cikande
  fire, Gaza, Seoul minister quits, Delta ground stop 1,169 late,
  Lahore AQI 538, Riyadh Houthi claim.
- ALSO ON (14–30, 17 items): Bahrain asks UN, Eisenkot–Likud, Bondi
  hero, France squad, Iran double launcher, Iran rationing, Zelenskyy
  Patriots, China spy campaign, Taiwan–Canada, Youth Congress / Meta,
  Pakistan minister Delhi, Trump / China nuclear, Pugh Hormuz swim,
  West Bank settlers, Guatemala arrest, China margin cut, AP Democrats
  258.
- DATE CHECK (excluded, 2 items only): Peru M6.7 quake — Fri 20 Nov;
  Paolo Bulgari dies — 21 Nov. Framed as "Not in this edition".
- Regions: Europe 4, Middle East 9, Asia 8, Africa 1, Americas 4,
  Oceania 2, Global 2 = 30.

## Layout (v5 — paying for the taller hero and cards)

The taller COP31 scene (180 vs v3's 156) and taller cards (128 vs
116) cost 24px of vertical space. v5 pays for it by tightening the
map (46px, was 70) and the DATE CHECK box (78px, was 110) — the
ALSO ON list keeps v3's 17 items at 16px leading, and the footer
stays at y=1012. Every section gap is 6-8px. Full coordinates in
render_poster.py and DESIGN.md.

## Design

Design philosophy in DESIGN.md ("Illustrated Front Page"): every story
a drawn scene first and a headline second; cream paper, navy ink, one
red accent; strict grid, generous breathing room, nothing overlaps;
the whole poster must read at 300px. Infographic-generator principles
applied to the layout (card anatomy, typography hierarchy, section
patterns); canvas-design principles applied as art direction
(visual hierarchy, craftsmanship, precision, breathing room).

## Technical

- Python stdlib ONLY for the graded program (`main.py` copies the
  bundled `entry.png`, SHA-256 verified). Render at build time
  (`render_poster.py`, needs Pillow + editorial-illustration library).
- Test as uid 65534 on a read-only copy; output byte-identical.
- Title: "Sunday 22 November 2026: 30 sourced stories, 7 regions, illustrated cards that read at 300px — v5"
- Do NOT submit without Joni's 'Setuju' on the exact entry.
- v3 is PINNED as final, so a worse v5 costs nothing — but v5 aims to BEAT v3.
