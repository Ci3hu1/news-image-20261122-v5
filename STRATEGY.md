# STRATEGY — news-image-20261122 v5

## Where we stand

- v1: 971,449 (97.14%), rank 3,741/12,530, 10W 2D 0L.
- v2: 953,261 (95.33%), 8W 2D 2L — WORSE than v1.
- v3: 981,243 (98.12%), 12W 0D 0L, rank 770/13,174 — BEST, PINNED as final.
- v4: 976,591 (97.66%), 12W 0D 0L, rank 2,203 — BELOW v3 by 4,652.
- Top-10 cutoff ~990,650. v5 must beat v3 by ~9,400 to reach the top 10.
- v5 is submission #5 of max 5 (last slot). Entries close 24 Nov 07:00 WIB.

## What the judge actually said (v4)

Read from `GET /api/submissions/01a20739-68a2-7739-995f-7446455a26aa`,
`scores[0].judge.heat.matches[].calls[].reason`. v4 won 12 of 12
calls on breadth and dating — "24 stories across 7 regions", "UTC
timeline, source attributions, explicit date-check box" — but one
call was lost to a cleaner opponent on readability: the judge's later
criteria (craft/legibility) reversed a match v4 was winning on
breadth. And 24 stories is fewer than v3's 30, so v4 gave up breadth
(the judge's criterion 2) for a cleanliness gain that did not pay.

## The v5 strategy — v3's breadth + v4's craft, no cuts

**Fix 1 — restore the 30-story breadth.** v5 uses v3's EXACT 30-story
set (3 leads + 10 featured + 17 ALSO ON, all verified Sunday 22 Nov
2026, all 7 regions). No story is cut, swapped, or added. The judge
rewards breadth after the date; 30 stories beat 24. The v4-only
stories (BepiColombo, Poland missiles, DNI/Nvidia probe) are NOT in
v5 — they were v4's viral picks, but v3's set already won 12/12
matches on breadth, and changing the set would trade a proven winner
for an unproven one.

**Fix 2 — keep v4's "NO DEAL" stamp.** v3's stamp read "NO DEA!" at
300px. v5 uses v4's stamp: 80px bold type, white fill, thick red
border, wide box, inside a 180px scene (v4: 220px — the stamp's final
size depends on the type/scene ratio, so 180 keeps it readable while
saving 20px for the ALSO ON list). Verified at 300px: "NO DEAL" reads
in full.

**Fix 3 — border clearance everywhere (Joni's rule).** No word may
touch a border line. COP31 meta ends 5px clear of its box; featured
meta 3px clear; DATE CHECK legend 4px clear; heroes 2-3 meta 2px
clear. Enforced by test (TestBorderClearance) and verified visually
at 4x zoom. The map pin labels were also fixed: the 46px-tall map
pushed 5 northern pins' labels above the box top and onto the "WHERE
IT HAPPENED" label, and pins 3/13 overlapped each other — all
retuned (TestMapPins) so every label sits inside the box with >=2px
clearance and no two labels overlap.

**Fix 4 — keep v4's sharpening and bigger cards.** UnsharpMask
percent 150 (v3: 120) after the LANCZOS downscale. Featured cards
128px tall with a 76px picture area (v3: 116px / 62px).

## What v5 keeps (judge-praised in v3)

- Explicit date "Sunday 22 November 2026" prominently (Criterion 1).
- Broad coverage across 7 regions (Criterion 2) — 30 stories.
- Sourcing + claimed-vs-confirmed labels on every story.
- UTC timeline + world map + big COP31 lead story.
- Header "ALL FROM SUNDAY" is true — all 30 main-list stories are
  Sunday 22 Nov only.
- DATE CHECK shrunk to 2 items, neutral title "DATE CHECK —
  excluded", framed as excluded.
- Hong Kong figure with denominator ("5,640 of 5,709", source EAC).
- One consistent drone number (186 launched / 161 shot down); Dymer
  toll "4 killed, 14 missing"; Delta delays "1,169" consistent.

## Layout budget

The taller hero scene and cards cost 24px. v5 pays by tightening
the map (46px, was 70) and the DATE CHECK box (78px, was 110). The
ALSO ON list keeps v3's 17 items at 16px leading; the footer stays
at y=1012. Every section gap is 6-8px.

## Design

Design philosophy in DESIGN.md ("Illustrated Front Page"): every story
a drawn scene first and a headline second; cream paper, navy ink, one
red accent; strict grid, generous breathing room, nothing overlaps.
Infographic-generator principles applied to the layout (card anatomy,
typography hierarchy, section patterns); canvas-design principles
applied as art direction (visual hierarchy, craftsmanship, precision,
breathing room). The canvas-design "minimal text" stance does NOT apply
here — a news poster is text-heavy by nature.

## Risks

- The judge may still prefer a cleaner 6-story poster over a
  30-story one. v5's answer is the same as v3's: the 13 pictured
  stories ARE the clean composition the judge praised, and the
  17-item list is short, large, and airy rather than a wall of text —
  plus the stamp, the borders, and the sharpening are now fixed.
- The DATE CHECK box, however small, is still a box with other dates
  in it. v3 proved the shrunken, neutrally-titled version is praised,
  not penalised — keep it.
- v3 is PINNED as final. If v5 scores below v3, v3 stays final and
  nothing is lost. If v5 scores above v3, v5 becomes the latest and
  stands as final automatically (Force_Last) — no re-pin needed.
- This is the LAST submission slot (5 of 5). There is no v6.
