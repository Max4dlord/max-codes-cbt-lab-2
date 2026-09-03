#!/usr/bin/env python3
"""Textbook math notation pass for EEE 202.
Replaces programming-style notation (underscores, florin-f, middots, carets)
with textbook Unicode (real subscripts/superscripts, ×, clean fractions).
Applies to build_eee202.py and splice_eee202.py, then audits for leftovers."""
import re
import sys

FILES = ["scripts/build_eee202.py", "scripts/splice_eee202.py"]

# (old, new) — ordered, longest first where they overlap
PAIRS = [
    # --- symbol renames: programming underscore subscripts -> Unicode subscripts
    ("A_max", "Aₘ"), ("V_max", "Vₘ"), ("I_max", "Iₘ"),
    ("V_rms", "Vᵣₘₛ"), ("I_rms", "Iᵣₘₛ"), ("V_avg", "Vₐᵥₑ"),
    ("X_L", "Xₗ"), ("X_C", "XC"),
    ("R_m", "Rₘ"), ("I_m", "Iₘ"), ("R_shunt", "Rₛₕ"), ("R_sh", "Rₛₕ"),
    ("R_total", "Rₜ"),
    ("V_th", "Vₜₕ"), ("Z_th", "Zₜₕ"), ("Z_load", "Zₗ"),
    ("I_N", "Iₙ"), ("Z_N", "Zₙ"),
    ("I_fsd", "Iꜰₛᵈ"),  # fallback; hand-edited afterwards where needed
    ("μ_r", "μᵣ"),
    # --- florin f -> plain f, subscript zero
    ("ƒ₀", "f₀"), ("2πƒ", "2πf"), ("ƒ = 1/T", "f = 1/T"),
    ("2πƒL = 1/(2πƒC)", "2πfL = 1/(2πfC)"),
    # --- caret exponent -> superscript
    ("e^(−t)", "e⁻ᵗ"),
    ("Aₘ e⁻ᵗ", "Aₘ × e⁻ᵗ"),
    ("sin(t)/2πf", "sin(t)/(2πf)"),
    # --- multiplication dots/concatenation -> ×
    ("q·v·B·sin", "q × v × B × sin"),
    ("q v B sin", "q × v × B × sin"),
    ("qvB sin", "q × v × B × sin"),
    ("qvB cos", "q × v × B × cos"),
    ("qvB", "q × v × B"),
    ("mB sin θ", "m × B × sin θ"),
    ("B·I·l·sin", "B × I × l × sin"),
    ("BIl sin", "B × I × l × sin"),
    ("Φ = B·A", "Φ = B × A"), ("Φ = BA", "Φ = B × A"), ("B·A", "B × A"),
    ("μ₀·n·I", "μ₀ × n × I"), ("μ₀ n I", "μ₀ × n × I"), ("μ₀nI", "μ₀ × n × I"),
    ("E = N·(dΦ/dt)", "E = N × (dΦ/dt)"), ("E = N (dΦ/dt)", "E = N × (dΦ/dt)"),
    ("E = N·(ΔΦ/Δt)", "E = N × (ΔΦ/Δt)"), ("E = N (ΔΦ/Δt)", "E = N × (ΔΦ/Δt)"),
    ("E = B·l·v", "E = B × l × v"), ("E = B l v", "E = B × l × v"), ("E = Blv", "E = B × l × v"),
    ("V₁I₁ = V₂I₂", "V₁ × I₁ = V₂ × I₂"), ("V₁I₁", "V₁ × I₁"),
    ("Z₁Z₂/(Z₁+Z₂)", "Z₁ × Z₂ / (Z₁ + Z₂)"), ("Z₁Z₂/(Z₁ + Z₂)", "Z₁ × Z₂ / (Z₁ + Z₂)"),
    ("Aₘ·sin", "Aₘ sin"), ("A_max·sin", "Aₘ sin"), ("*sin(2π", " sin(2π"),
    # --- spacing around arithmetic
    ("0.707 Vₘ", "0.707 × Vₘ"), ("0.637 Vₘ", "0.637 × Vₘ"),
    ("1.414 Vᵣₘₛ", "1.414 × Vᵣₘₛ"),
    ("100 kHz/50", "100 kHz / 50"),
    ("0.1/0.999", "0.1 / 0.999"), ("12/0.75", "12 / 0.75"), ("0.02/5", "0.02 / 5"),
    ("20/20", "20 / 20"),
    ("I = 20/(10 + 10)", "I = 20 / (10 + 10)"),
    ("Vₜₕ/(Zₜₕ", "Vₜₕ / (Zₜₕ"),
    # --- instruments worked solutions: name the quantities in words
    ("Formula: R_total = V/I_fsd; multiplier = R_total − R_m.",
     "Formula: total resistance Rₜ = V / I, where I is the full-scale deflection current; multiplier = Rₜ − Rₘ."),
    ("Step 1: R_total = 10 V/100 µA = 10/(1 × 10⁻⁴) = 100 kΩ.",
     "Step 1: Rₜ = 10 / (1 × 10⁻⁴) = 100 kΩ."),
    ("Step 1: R_total = 5/(50 × 10⁻⁶) = 100 kΩ.",
     "Step 1: Rₜ = 5 / (5 × 10⁻⁵) = 100 kΩ."),
    ("Formula: Iₘ Rₘ = (I − Iₘ) Rₛₕ.", "Formula: Iₘ × Rₘ = (I − Iₘ) × Rₛₕ."),
    ("Step 2: Rₛₕ = (0.001 × 100)/0.999", "Step 2: Rₛₕ = (0.001 × 100) / 0.999"),
    # --- solenoid substitutions: juxtaposed parentheses -> explicit ×
    ("(4π × 10⁻⁷)(1000)(1600)", "(4π × 10⁻⁷) × 1000 × 1600"),
    ("(4π × 10⁻⁷)(160)(1700)", "(4π × 10⁻⁷) × 160 × 1700"),
    ("(4π × 10⁻⁷)(58.33)(800)", "(4π × 10⁻⁷) × 58.33 × 800"),
    ("(4π × 10⁻⁷)(500)(4)", "(4π × 10⁻⁷) × 500 × 4"),
    ("= 4π × 1.6 × 10⁻³... compute 12.566 × 10⁻⁴ × 1600 = 2.0106 T ≈ 2.01 T",
     "= 2.0106 T ≈ 2.01 T"),
    # --- study-mode formula sheets
    ("EXTENDING RANGES: voltmeter multiplier R = (V/I_fsd) − R_m; ammeter shunt R_sh = (I_m·R_m)/(I − I_m).",
     "EXTENDING RANGES: voltmeter — total resistance Rₜ = V / (full-scale deflection current), multiplier = Rₜ − Rₘ; ammeter — shunt Rₛₕ = (Iₘ × Rₘ) / (I − Iₘ)."),
]

def apply_pairs(text):
    for old, new in PAIRS:
        if old in text:
            text = text.replace(old, new)
    return text

def audit(name, text):
    """Print lines containing banned tokens, with context."""
    banned = ["_", "ƒ", "·", "*", "^", "qvB", "V_max", "X_L", "X_C", "R_m",
              "I_fsd", "R_total", "Z_load", "V_th", "Z_th", "I_N ", "R_sh",
              "e^(", "μF", "μA"]
    issues = []
    for i, line in enumerate(text.split("\n"), 1):
        for b in banned:
            if b in line and not line.strip().startswith(("#", "//")):
                issues.append((i, b, line.strip()[:110]))
                break
    print(f"--- {name}: {len(issues)} flagged lines ---")
    for i, b, s in issues[:40]:
        print(f"  L{i} [{b}] {s}")

def main():
    for f in FILES:
        text = open(f).read()
        text = apply_pairs(text)
        open(f, "w").write(text)
        print(f"patched {f}")
    # audit
    for f in FILES:
        audit(f, open(f).read())

if __name__ == "__main__":
    main()
