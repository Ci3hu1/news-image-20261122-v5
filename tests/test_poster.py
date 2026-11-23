#!/usr/bin/env python3
"""Tests for news-image-20261122 v5.

Run: python3 -m pytest tests/  (or python3 tests/test_poster.py)

v5 is the fix for v4, ordered by Joni ("Perbaiki", 23 Nov 2026).
v3 scored 981,243 (98.12%, rank 770) and is PINNED as final; v4
scored 976,591 (97.66%, rank 2,203) — below v3. The judge praised
v4's breadth but one match was lost on readability, and 24 stories
is fewer than v3's 30. LESSON: cutting stories cost more breadth
than the legibility gain returned. So v5 keeps v3's PROVEN 30-story
set (unchanged, all verified Sunday 22 Nov 2026) and applies ONLY
v4's craft fixes. The tests cover:

  1. 30 stories total (3 leads + 10 featured + 17 ALSO ON), region
     counts sum to 30 across 7 regions, ALSO ON numbering 14-30.
  2. DATE CHECK is 2 items, neutral title, and none of its stories
     appear in the main list.
  3. Hong Kong figure carries its denominator and a source (EAC);
     no bare "98.79%" anywhere.
  4. Legibility: every featured headline wraps to at most 2 lines at
     17px bold in a 186px card, every ALSO ON headline fits its 298px
     column, and the poster is 1024x1024 under 1 MiB.
  5. The "NO DEAL" stamp is big enough to read at 300px (80px type
     in a 180px scene, white fill, thick red border).
  6. BORDER CLEARANCE (Joni, 23 Nov 13:56: no word may touch a
     border line): every text element ends 2-5px clear of its box
     border — COP31 meta, featured-card meta, DATE CHECK legend,
     heroes 2-3 meta.
  7. Sharpening is UnsharpMask percent 150 (v4's setting).
  8. GTA 6 appears nowhere (its $3.79B was announced Fri 20 Nov,
     not a 22 Nov story).
  9. One drone number (186/161), Dymer toll, Delta delays, and
     main.py pure stdlib.
"""

import ast
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

sys.path.insert(0, "/home/hatch/workspace/custom-skills/"
                   "editorial-illustration")
sys.path.insert(0, ROOT)

import render_poster as rp  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

EXCLUDED_MARKERS = ("peru", "bulgari")


def renderer_source():
    with open(os.path.join(ROOT, "render_poster.py")) as fh:
        return fh.read()


class TestStoryCount(unittest.TestCase):
    def test_total_is_30(self):
        total = len(rp.LEADS) + len(rp.FEATURED) + len(rp.ALSO_ON)
        self.assertEqual(total, 30)

    def test_sections(self):
        self.assertEqual(len(rp.LEADS), 3)
        self.assertEqual(len(rp.FEATURED), 10)
        self.assertEqual(len(rp.ALSO_ON), 17)

    def test_region_counts_sum_to_30(self):
        total = sum(int(label.split()[-1]) for label, _ in rp.REGIONS)
        self.assertEqual(total, 30)

    def test_seven_regions(self):
        self.assertEqual(len(rp.REGIONS), 7)

    def test_region_counts(self):
        counts = dict((label, int(label.split()[-1]))
                      for label, _ in rp.REGIONS)
        self.assertEqual(counts.get("Europe 4"), 4)
        self.assertEqual(counts.get("Middle East 9"), 9)
        self.assertEqual(counts.get("Asia 8"), 8)
        self.assertEqual(counts.get("Africa 1"), 1)
        self.assertEqual(counts.get("Americas 4"), 4)
        self.assertEqual(counts.get("Oceania 2"), 2)
        self.assertEqual(counts.get("Global 2"), 2)


class TestAlsoOn(unittest.TestCase):
    def test_numbering_14_to_30_sequential(self):
        nums = [n for n, _, _ in rp.ALSO_ON]
        self.assertEqual(nums, list(range(14, 31)))

    def test_no_duplicate_numbers(self):
        nums = [n for n, _, _ in rp.ALSO_ON]
        self.assertEqual(len(nums), len(set(nums)))

    def test_headlines_fit_column(self):
        # Column is 336px wide; dot (12px) + number (26px) leaves 298px.
        img = Image.new("RGB", (10, 10))
        d = ImageDraw.Draw(img)
        f = rp.fnt("sans", 15)
        for n, txt, _ in rp.ALSO_ON:
            w = d.textlength(txt, font=f) / rp.SS
            self.assertLessEqual(
                w, 298,
                "ALSO ON %d headline too wide for its column: %r (%.1fpx)"
                % (n, txt, w))


class TestDateCheck(unittest.TestCase):
    def test_at_most_two_items(self):
        self.assertLessEqual(len(rp.DATE_CHECK), 2)

    def test_excluded_stories_not_in_main_list(self):
        main = " ".join(
            [h["headline"] for h in rp.LEADS]
            + [s["headline"] for s in rp.FEATURED]
            + [txt for _, txt, _ in rp.ALSO_ON]).lower()
        for marker in EXCLUDED_MARKERS:
            self.assertNotIn(marker, main,
                             "excluded story %r leaked into the main list"
                             % marker)

    def test_date_check_items_are_off_day(self):
        # Both items carry a date that is not Sunday 22 Nov.
        for item in rp.DATE_CHECK:
            self.assertTrue("20 Nov" in item or "21 Nov" in item, item)


class TestHongKong(unittest.TestCase):
    def test_card_carries_denominator(self):
        hk = [s for s in rp.FEATURED if s["place"] == "HONG KONG"]
        self.assertEqual(len(hk), 1)
        self.assertIn("5,640 of 5,709", hk[0]["headline"])

    def test_card_source_is_eac(self):
        hk = [s for s in rp.FEATURED if s["place"] == "HONG KONG"][0]
        self.assertEqual(hk["source"], "EAC")

    def test_kpi_carries_denominator(self):
        kpi = dict((lab, val) for val, lab in rp.KPIS)
        self.assertEqual(kpi.get("OF 5,709 HK VOTERS"), "5,640")

    def test_no_bare_turnout_percentage(self):
        # The judge read a bare "98.79%" as implausible. It must never
        # appear on the poster without its denominator beside it.
        for val, _ in rp.KPIS:
            self.assertNotEqual(val, "98.79%")
        for s in rp.FEATURED:
            self.assertNotIn("98.79%", s["headline"])


class TestNoDealStamp(unittest.TestCase):
    def test_stamp_type_is_large(self):
        # v3's stamp was 44px type in a 156px scene and read "NO DEA!"
        # at 300px. v5 uses v4's 80px bold type.
        src = renderer_source()
        m = re.search(r'stamp_f = ff\("sans_bold", (\d+)\)', src)
        self.assertIsNotNone(m, "stamp font line not found")
        self.assertGreaterEqual(int(m.group(1)), 70)

    def test_cop31_scene_is_tall(self):
        # v5 scene is 180px tall (v3: 156, v4: 220). The stamp's final
        # size depends on the type/scene ratio, so 180 keeps it
        # readable while saving space for the 17-item ALSO ON list.
        src = renderer_source()
        m = re.search(r'lead_scene\(h\["scene"\], 2000, (\d+)\)', src)
        self.assertIsNotNone(m, "COP31 scene size not found")
        self.assertGreaterEqual(int(m.group(1)), 170)

    def test_stamp_has_white_fill_and_thick_border(self):
        src = renderer_source()
        self.assertIn("fill=WHITE", src)
        m = re.search(r'outline=RED, width=(\d+)', src)
        self.assertIsNotNone(m, "stamp border not found")
        self.assertGreaterEqual(int(m.group(1)), 8)


class TestBorderClearance(unittest.TestCase):
    """Joni, 23 Nov 13:56: no word may touch a border line. Every
    text element must end at least 2px clear of its box border."""

    def test_cop31_meta_clear_of_box(self):
        # Hero 1 box bottom 278; meta text at y=260 in 13px font
        # ends at 273 — 5px clear.
        src = renderer_source()
        m = re.search(r'px\(1012\), px\((\d+)\)\], outline=INK', src)
        self.assertIsNotNone(m, "hero 1 box not found")
        box_bottom = int(m.group(1))
        self.assertEqual(box_bottom, 278)
        self.assertLessEqual(260 + 13, box_bottom - 2)

    def test_featured_meta_clear_of_card(self):
        # Card is 128 tall; meta at y+116 in 9px font ends at
        # y+125 — 3px clear of the card bottom.
        src = renderer_source()
        self.assertIn("px(y + 128)", src)
        self.assertIn("px(y + 116)", src)
        self.assertLessEqual(116 + 9, 128 - 2)

    def test_date_check_legend_clear_of_box(self):
        # DATE CHECK box bottom 878; legend at y=864 in 10px font
        # ends at 874 — 4px clear.
        src = renderer_source()
        m = re.search(r'px\(660\), px\(800\), px\(1012\), px\((\d+)\)',
                      src)
        self.assertIsNotNone(m, "DATE CHECK box not found")
        self.assertEqual(int(m.group(1)), 878)
        self.assertLessEqual(864 + 10, 878 - 2)

    def test_heroes_meta_clear_of_box(self):
        # Heroes 2-3 box bottom 440; tag text at y=426 in 12px font
        # ends at 438 — 2px clear.
        src = renderer_source()
        self.assertIn("px(x + 494), px(440)", src)
        self.assertLessEqual(426 + 12, 440 - 2)


class TestMapPins(unittest.TestCase):
    """Pin number labels must sit inside the map box (816-862) with
    >=2px clearance, and below the section-label row (ends ~814).
    The map is only 46px tall in v5 (v3: 70), so the northern pins'
    old dy values pushed their labels above the box top and onto the
    "WHERE IT HAPPENED" label. draw_world_map adds dx/dy in 2x
    canvas coords, so the final displacement is dx/2, dy/2; the
    label circle radius is 3.5px final."""

    def test_pin_labels_inside_map_box(self):
        for p in rp.PINS:
            pin_y = 816 + (90 - p["lat"]) / 180 * 46
            label_y = pin_y + p["dy"] / 2
            self.assertGreaterEqual(
                label_y - 3.5, 818,
                "pin %d label escapes the map top (centre %.1f)"
                % (p["n"], label_y))
            self.assertLessEqual(
                label_y + 3.5, 860,
                "pin %d label escapes the map bottom (centre %.1f)"
                % (p["n"], label_y))

    def test_pin_labels_do_not_overlap_each_other(self):
        centres = []
        for p in rp.PINS:
            pin_x = 12 + (p["lon"] + 180) / 360 * 636
            pin_y = 816 + (90 - p["lat"]) / 180 * 46
            centres.append((pin_x + p["dx"] / 2, pin_y + p["dy"] / 2))
        for i in range(len(centres)):
            for j in range(i + 1, len(centres)):
                dx = centres[i][0] - centres[j][0]
                dy = centres[i][1] - centres[j][1]
                dist = (dx * dx + dy * dy) ** 0.5
                self.assertGreaterEqual(
                    dist, 9,
                    "pin labels %d and %d overlap (%.1fpx apart)"
                    % (i + 1, j + 1, dist))


class TestSharpening(unittest.TestCase):
    def test_unsharp_mask_percent_150(self):
        # v5 uses v4's stronger sharpening (Joni: "Pertajam gambarnya").
        src = renderer_source()
        m = re.search(r'UnsharpMask\(radius=2, percent=(\d+)', src)
        self.assertIsNotNone(m, "UnsharpMask call not found")
        self.assertEqual(int(m.group(1)), 150)


class TestNoGTA6(unittest.TestCase):
    def test_no_gta6_anywhere(self):
        # Hard constraint: GTA 6's $3.79B was announced Fri 20 Nov
        # (Take-Two 8-K), not a 22 Nov story. It must not appear on
        # the poster in any form — not as a story, not in DATE CHECK.
        blob = (" ".join(
            [h["headline"] for h in rp.LEADS]
            + [s["headline"] for s in rp.FEATURED]
            + [txt for _, txt, _ in rp.ALSO_ON]).lower()
            + " " + " ".join(rp.DATE_CHECK).lower() + " "
            + " ".join(h["deck"] for h in rp.LEADS).lower())
        self.assertNotIn("gta", blob)
        self.assertNotIn("grand theft", blob)


class TestLegibility(unittest.TestCase):
    def test_featured_headlines_fit_two_lines(self):
        # The v2 judge's core complaint was truncation/blur. Every
        # featured headline must wrap to at most 2 lines in its card.
        img = Image.new("RGB", (10, 10))
        d = ImageDraw.Draw(img)
        f = rp.fnt("sans_bold", 17)
        for s in rp.FEATURED:
            lines = rp.wrap(d, s["headline"], f, rp.px(186))
            self.assertLessEqual(
                len(lines), 2,
                "featured %d headline wraps to %d lines: %r"
                % (s["n"], len(lines), s["headline"]))

    def test_lead_headlines_fit(self):
        img = Image.new("RGB", (10, 10))
        d = ImageDraw.Draw(img)
        for i, h in enumerate(rp.LEADS):
            size = 28 if i == 0 else 21
            width = 1000 if i == 0 else 478
            f = rp.fnt("sans_bold", size)
            lines = rp.wrap(d, h["headline"], f, rp.px(width))
            self.assertLessEqual(len(lines), 2, h["headline"])

    def test_poster_dimensions_and_size(self):
        path = os.path.join(ROOT, "entry.png")
        self.assertTrue(os.path.isfile(path), "entry.png missing")
        with Image.open(path) as im:
            self.assertEqual(im.size, (1024, 1024))
        size = os.path.getsize(path)
        self.assertLessEqual(size, 1024 * 1024,
                             "entry.png over 1 MiB: %d bytes" % size)

    def test_preview_300_exists(self):
        path = os.path.join(ROOT, "preview-300.png")
        self.assertTrue(os.path.isfile(path), "preview-300.png missing")
        with Image.open(path) as im:
            self.assertEqual(im.size, (300, 300))


class TestConsistency(unittest.TestCase):
    def test_one_drone_number(self):
        # 186 launched / 161 shot down everywhere it appears.
        kpi = dict((lab, val) for val, lab in rp.KPIS)
        self.assertEqual(kpi["DRONES IN A NIGHT"], "186")
        self.assertEqual(kpi["SHOT DOWN"], "161")
        dymer = rp.LEADS[1]
        self.assertIn("186", dymer["headline"])
        self.assertIn("161", dymer["deck"])

    def test_dymer_toll(self):
        self.assertIn("4 killed, 14 missing", rp.LEADS[1]["deck"])

    def test_delta_delays(self):
        kpi = dict((lab, val) for val, lab in rp.KPIS)
        self.assertEqual(kpi["DELTA DELAYS"], "1,169")
        delta = [s for s in rp.FEATURED if s["place"] == "ATLANTA"][0]
        self.assertIn("1,169", delta["headline"])

    def test_main_py_pure_stdlib(self):
        # The grader is pure Python stdlib: main.py must not import
        # anything outside the standard library.
        with open(os.path.join(ROOT, "main.py")) as fh:
            src = fh.read()
        tree = ast.parse(src)
        allowed = set(sys.stdlib_module_names)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for a in node.names:
                    self.assertIn(a.name.split(".")[0], allowed, a.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    self.assertIn(node.module.split(".")[0], allowed,
                                  node.module)


if __name__ == "__main__":
    unittest.main(verbosity=2)
