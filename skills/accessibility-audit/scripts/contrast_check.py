#!/usr/bin/env python3
"""
Contrast ratio calculator for WCAG 2.1 accessibility audits.

Usage:
    python contrast_check.py "#1a1a1a" "#ffffff"
    python contrast_check.py "rgb(26,26,26)" "rgb(255,255,255)"
    python contrast_check.py --batch pairs.json

Batch JSON format:
    [
        {"fg": "#1a1a1a", "bg": "#ffffff", "label": "Body text"},
        {"fg": "#7d94a2", "bg": "#1e2a31", "label": "Muted text dark"}
    ]
"""

import sys
import json
import re
import argparse


def parse_color(color_str: str) -> tuple[int, int, int]:
    """Parse hex or rgb() color string to (r, g, b) tuple."""
    color_str = color_str.strip()

    # Hex: #rgb or #rrggbb
    hex_match = re.match(r'^#([0-9a-fA-F]{3,6})$', color_str)
    if hex_match:
        hex_val = hex_match.group(1)
        if len(hex_val) == 3:
            hex_val = ''.join(c * 2 for c in hex_val)
        r = int(hex_val[0:2], 16)
        g = int(hex_val[2:4], 16)
        b = int(hex_val[4:6], 16)
        return (r, g, b)

    # rgb(r, g, b)
    rgb_match = re.match(r'^rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$', color_str)
    if rgb_match:
        return (int(rgb_match.group(1)), int(rgb_match.group(2)), int(rgb_match.group(3)))

    raise ValueError(f"Unrecognized color format: {color_str!r}. Use #rrggbb or rgb(r,g,b).")


def relative_luminance(r: int, g: int, b: int) -> float:
    """Calculate relative luminance per WCAG 2.x formula."""
    def linearize(c: int) -> float:
        srgb = c / 255.0
        return srgb / 12.92 if srgb <= 0.04045 else ((srgb + 0.055) / 1.055) ** 2.4

    return 0.2126 * linearize(r) + 0.7152 * linearize(g) + 0.0722 * linearize(b)


def contrast_ratio(color1: str, color2: str) -> float:
    """Calculate WCAG contrast ratio between two colors."""
    rgb1 = parse_color(color1)
    rgb2 = parse_color(color2)
    l1 = relative_luminance(*rgb1)
    l2 = relative_luminance(*rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def grade(ratio: float) -> dict:
    """Return WCAG pass/fail grades for a given contrast ratio."""
    return {
        "AA_normal":  ratio >= 4.5,   # < 18pt / < 14pt bold
        "AA_large":   ratio >= 3.0,   # >= 18pt or >= 14pt bold
        "AA_ui":      ratio >= 3.0,   # UI components, focus indicators
        "AAA_normal": ratio >= 7.0,
        "AAA_large":  ratio >= 4.5,
    }


def format_result(label: str, fg: str, bg: str, ratio: float, grades: dict) -> str:
    """Format a single contrast check result."""
    lines = []
    ratio_str = f"{ratio:.2f}:1"

    aa_normal = "✓ PASS" if grades["AA_normal"] else "✗ FAIL"
    aa_large  = "✓ PASS" if grades["AA_large"]  else "✗ FAIL"
    aa_ui     = "✓ PASS" if grades["AA_ui"]     else "✗ FAIL"
    aaa_norm  = "✓ PASS" if grades["AAA_normal"] else "✗ FAIL"

    if label:
        lines.append(f"\n{label}")
        lines.append(f"  {fg} on {bg}")
    else:
        lines.append(f"\n{fg} on {bg}")

    lines.append(f"  Contrast ratio: {ratio_str}")
    lines.append(f"  AA  normal text (4.5:1): {aa_normal}")
    lines.append(f"  AA  large text  (3.0:1): {aa_large}")
    lines.append(f"  AA  UI / focus  (3.0:1): {aa_ui}")
    lines.append(f"  AAA normal text (7.0:1): {aaa_norm}")

    return "\n".join(lines)


def check_pair(fg: str, bg: str, label: str = "") -> None:
    ratio = contrast_ratio(fg, bg)
    grades = grade(ratio)
    print(format_result(label, fg, bg, ratio, grades))


def main():
    parser = argparse.ArgumentParser(description="WCAG contrast ratio checker")
    parser.add_argument("fg", nargs="?", help="Foreground color (#hex or rgb())")
    parser.add_argument("bg", nargs="?", help="Background color (#hex or rgb())")
    parser.add_argument("--batch", metavar="FILE", help="JSON file with [{fg, bg, label}]")
    args = parser.parse_args()

    if args.batch:
        with open(args.batch) as f:
            pairs = json.load(f)
        print(f"Checking {len(pairs)} color pair(s):\n{'─' * 40}")
        all_pass = True
        for pair in pairs:
            ratio = contrast_ratio(pair["fg"], pair["bg"])
            grades = grade(ratio)
            label = pair.get("label", "")
            print(format_result(label, pair["fg"], pair["bg"], ratio, grades))
            if not grades["AA_normal"]:
                all_pass = False
        print(f"\n{'─' * 40}")
        print("Overall AA (normal text):", "✓ All pass" if all_pass else "✗ Some failures")

    elif args.fg and args.bg:
        check_pair(args.fg, args.bg)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
