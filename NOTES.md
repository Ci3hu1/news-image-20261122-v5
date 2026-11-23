# NOTES — news-image-20261122 v5 (the fix for v4)

**Status:** BUILT, NOT SUBMITTED. Entry commit
`6571508ff6e42f8d4ebe7bdbd062acc034b47601` (repo
https://github.com/Ci3hu1/news-image-20261122-v5, main, public,
created 2026-11-23T07:32:13Z — after the competition opened).
Bundle + kit check PENDING — the builder session's usage rows flush
only after the builder turn ends; the parent re-runs bundle + check
after the rows flush. Do NOT submit before the kit check returns
ok=true failed=[]. Do NOT submit without Joni's 'Setuju' on the
exact entry.

## What v5 is

The fix for v4, ordered by Joni ("Perbaiki", 23 Nov 2026 ~14:28).
v3 scored 981,243 (98.12%, 12W 0D 0L, rank 770/13,174) and is PINNED
as final (submission 01a20709). v4 scored 976,591 (97.66%, 12W 0D 0L,
rank 2,203) — BELOW v3 by 4,652. The judge praised v4's breadth but
one match was lost on readability, and 24 stories < v3's 30. LESSON:
cutting stories cost more breadth than the legibility gain returned.

v5 = v3's proven 30-story set (UNCHANGED — same 3 leads, same 10
featured, same 17 ALSO ON, all verified Sunday 22 Nov 2026) + v4's
craft fixes only (NO DEAL stamp, border clearance, sharpening
percent 150, bigger cards). This is submission #5 of max 5 (last
slot). Entries close 24 Nov 2026 07:00 WIB. Results 7 Dec 2026.

## The v5 changes (vs v3)

1. **"NO DEAL" stamp fixed (from v4).** 80px bold type, white fill,
   thick red border, wide box, inside a 180px COP31 scene (v3: 44px
   type in a 156px scene, read "NO DEA!" at 300px). Verified at
   300px: "NO DEAL" reads in full.
2. **Border clearance (Joni, 23 Nov 13:56).** COP31 meta ends 5px
   clear of its box (v3: touched); featured-card meta 3px clear;
   DATE CHECK legend 4px clear; heroes 2-3 meta 2px clear. Enforced
   by TestBorderClearance; verified visually at 4x zoom.
3. **Map pin labels fixed.** The 46px-tall map pushed 5 northern
   pins' labels (2, 5, 9, 10, 11) above the box top and onto the
   "WHERE IT HAPPENED — STORIES 1–13 PINNED" label, and pins 3/13
   (Bahrain/Riyadh) overlapped each other (4.9px apart). Their
   offsets were retuned (pin 2 dy -30→-8, pin 5 -28→-3, pin 9
   -28→-18, pin 10 -26→-15, pin 11 -26→-17, pin 13 dx 44→-44) so
   every label sits inside the box with >=2px clearance and no two
   labels overlap. Enforced by TestMapPins; verified visually at 4x
   zoom. (These were pre-existing v3 defects, worse in v5 because
   the map is shorter.)
4. **Sharpening percent 150 (from v4; v3: 120).** Enforced by test.
5. **Bigger cards (from v4).** Featured cards 128px tall with a 76px
   picture area (v3: 116px / 62px).
6. **Layout budget.** The taller hero scene (180 vs 156) and cards
   (128 vs 116) cost 24px; paid by tightening the map (46px, was 70)
   and the DATE CHECK box (78px, was 110). ALSO ON keeps v3's 17
   items at 16px leading; footer stays at y=1012.

## Verification

- Tests: 34/34 pass (v3's 21 + NO DEAL stamp 3 + border clearance
  4 + map pins 2 + sharpening 1 + no-GTA-6 1 + preview-300 1 +
  region-counts 1).
- Render: entry.png 558,056 bytes, sha256
  345d6e2e4301be20df66cbe3c484265485b972e2f74055cb1e8f5713526553ca
  (1024x1024, under 1 MiB). preview-300.png rendered.
- Grader conditions: main.py run as uid 65534 on a read-only repo
  copy produces byte-identical output (sha256 matches the bundled
  entry.png).
- Visual check (full poster + 2x crops + 4x zooms): NO DEAL reads
  clearly; no word touches a border anywhere (COP31 meta, all 10
  featured meta lines, DATE CHECK legend, heroes 2-3 meta, map pin
  labels); all 30 stories present; Hong Kong denominator printed;
  300px preview reads as a clean front page (date, stamp, COP31
  headline, cards all discernible).
- main.py: pure stdlib (enforced by test), fresh write for v5.
- No GTA 6 anywhere (enforced by test).

## Kit / bundle

- Fresh kit downloaded 23 Nov 2026 (~14:30 WIB):
  ~/workspace/tools/makefun/news-image-20261122-kit/ (level 37;
  site reports level 38 — same note as v4, submit still accepted).
- Kit init run in the empty repo BEFORE copying files (creates
  .makefun/freshness.json, drand round 34205260, anchor 542ac227).
  LICENSE from init (MIT, SPDX line present).
- Bundle: ~/workspace/tools/makefun/bundles/ni22-v5-bundle.tar.gz
  (PENDING — parent re-runs after usage rows flush).
- Kit check: PENDING (parent re-runs after bundle).

## Submission (PENDING — needs Joni's "Setuju")

- Title: "Sunday 22 November 2026: 30 sourced stories, 7 regions, illustrated cards that read at 300px — v5"
- v3 stays PINNED as final: if v5 scores below v3, v3 stands and
  nothing is lost. If v5 scores above v3, v5 becomes the latest and
  stands as final automatically (Force_Last).
- Claim code: save ONLY in
  ~/.config/makefun/news-image-20261122-v5-submission.json (0600).

## Bundle + kit check (parent, 23 Nov ~14:44 WIB)
- Entry commit: 6571508ff6e42f8d4ebe7bdbd062acc034b47601
- Bundle: ~/workspace/tools/makefun/bundles/ni22-v5-bundle.tar.gz (2,030,478 B, sha256 0d799048c6f823a6072a44605517ca4a2273371a1167d0932e661232815be9f7)
- Kit check: ok=true, failed=[] (2 intake items deferred to server, hand-verified: repo public, owner Ci3hu1, created 07:32:13Z after open, commit in repo; uncommitted change is only __pycache__/)
- Usage: 1 row attached (builder session 247eb252)
- NOT submitted — awaiting Joni's "Setuju". This is submission #5 of max 5 (last slot).
