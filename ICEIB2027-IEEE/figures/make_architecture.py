"""Draw figures/architecture.pdf (Fig. 1, full text width) for the ICEIB 2027 paper.

English redraw of dic3-參考資料/proposal/figures/fig1.mmd. Run from any folder:
    python make_architecture.py
Writes architecture.pdf (for LaTeX) and architecture.png (preview) next to this file.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "STIXGeneral", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "pdf.fonttype": 42,  # embed TrueType fonts (IEEE PDF eXpress rejects Type 3)
    "ps.fonttype": 42,
})

W, H = 7.16, 3.55          # IEEE two-column text width, in inches
FS = 7.0                   # body font size (pt)
INK = "#222222"
MODULE_FILL = "#f2f2f2"
AGENT_FILL = "#ffffff"
GROUP_EDGE = "#555555"

fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")


def box(x0, y0, x1, y1, fill=AGENT_FILL, lw=0.8, ls="-", edge=INK, radius=0.05, z=1):
    ax.add_patch(FancyBboxPatch(
        (x0, y0), x1 - x0, y1 - y0,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        facecolor=fill, edgecolor=edge, linewidth=lw, linestyle=ls, zorder=z))


def num(x, y, n, r=0.075):
    """Circled module number, matching \\ding{172}-\\ding{179} in the text."""
    ax.add_patch(Circle((x, y), r, facecolor=INK, edgecolor=INK, zorder=5))
    ax.text(x, y - 0.005, str(n), color="white", fontsize=FS - 1, fontweight="bold",
            ha="center", va="center", zorder=6)


def module(x0, y0, x1, y1, n, title, body, fill=MODULE_FILL):
    box(x0, y0, x1, y1, fill=fill)
    num(x0 + 0.13, y1 - 0.13, n)
    ax.text(x0 + 0.25, y1 - 0.13, title, fontsize=FS, fontweight="bold",
            ha="left", va="center", color=INK)
    ax.text((x0 + x1) / 2, (y0 + y1 - 0.22) / 2, body, fontsize=FS - 0.5,
            ha="center", va="center", color=INK, linespacing=1.25)


def agent(x0, y0, x1, y1, title, body=None):
    box(x0, y0, x1, y1, z=3)
    cx = (x0 + x1) / 2
    if body:
        ax.text(cx, y1 - 0.1, title, fontsize=FS, fontweight="bold",
                ha="center", va="top", color=INK, zorder=4)
        ax.text(cx, (y0 + y1 - 0.18) / 2, body, fontsize=FS - 0.8,
                ha="center", va="center", color=INK, linespacing=1.2, zorder=4)
    else:
        ax.text(cx, (y0 + y1) / 2, title, fontsize=FS, fontweight="bold",
                ha="center", va="center", color=INK, zorder=4)


def arrow(p, q, both=False, ls="-", rad=0.0, label=None, lpos=0.5, loff=(0, 0.07),
          lha="center"):
    style = "<|-|>" if both else "-|>"
    ax.add_patch(FancyArrowPatch(
        p, q, arrowstyle=style, mutation_scale=7, linewidth=0.8, color=INK,
        linestyle=ls, connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0, zorder=2))
    if label:
        lx = p[0] + (q[0] - p[0]) * lpos + loff[0]
        ly = p[1] + (q[1] - p[1]) * lpos + loff[1]
        ax.text(lx, ly, label, fontsize=FS - 1, fontstyle="italic", ha=lha,
                va="center", color=INK, zorder=4,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.6))


def poly(points, label=None, lxy=None, lha="left"):
    """Elbow connector: straight segments through points, arrowhead at the end."""
    xs, ys = zip(*points[:-1])
    ax.plot(xs, ys, color=INK, linewidth=0.8, zorder=2, solid_capstyle="butt")
    arrow(points[-2], points[-1])
    if label:
        ax.text(*lxy, label, fontsize=FS - 1, fontstyle="italic", ha=lha, va="center",
                color=INK, zorder=4, bbox=dict(facecolor="white", edgecolor="none", pad=0.6))


# ---------------------------------------------------------------- layout (inches)
# Left column: user and input
module(0.05, 2.80, 1.25, 3.50, 1, "User & scenario",
       "Heavy-motorcycle\ntouring riders in Taiwan")
module(0.05, 1.75, 1.25, 2.50, 2, "Query input",
       "Web chat (place names,\nmap picks) + GPX import")

# Center: planner and reasoning
PX0, PY0, PX1, PY1 = 1.45, 1.55, 5.70, 3.50
box(PX0, PY0, PX1, PY1, fill="#fafafa", lw=0.9)
num(PX0 + 0.13, PY1 - 0.13, 3)
ax.text(PX0 + 0.25, PY1 - 0.13, "Planner & reasoning (multi-agent)", fontsize=FS,
        fontweight="bold", ha="left", va="center", color=INK)

agent(1.60, 2.60, 2.65, 3.05, "Orchestrator", "task split, plan draft")
agent(1.60, 1.70, 2.65, 2.15, "Rider memory", "preferences, past plans")

# Specialist agents (dashed group)
box(2.90, 2.33, 5.58, 3.28, fill="none", lw=0.7, ls=(0, (3, 2)), edge=GROUP_EDGE, z=2)
ax.text(5.55, 3.21, "specialist agents", fontsize=FS - 1.2, fontstyle="italic",
        ha="right", va="center", color=GROUP_EDGE)
agent(3.00, 2.55, 3.95, 3.05, "Pace agent", "segment P50/P90,\nETAs")
agent(4.45, 2.72, 5.48, 3.12, "Weather agent", "rain, warnings, dusk")
agent(4.45, 2.40, 5.48, 2.68, "Road & supply agent")

agent(3.00, 1.65, 4.75, 2.12, "Verifier agent",
      "R1 daylight, R2 fuel range, R3 weather,\nR4 road closure, R5 traceable numbers")

# Right column: decision and output
module(5.90, 1.75, 7.11, 2.50, 7, "Decision",
       "departure time, P50/P90\narrivals, fuel stops,\nranked risks")
module(5.90, 2.80, 7.11, 3.50, 8, "Output",
       "chat answer, map\ndashboard (Google Maps),\ntrip plan")

# Bottom band: data, analytics and knowledge
BX0, BY0, BX1, BY1 = 1.45, 0.05, 5.70, 1.30
box(BX0, BY0, BX1, BY1, fill="none", lw=0.7, ls=(0, (3, 2)), edge=GROUP_EDGE)
ax.text(BX1 - 0.05, BY1 - 0.08, "data, analytics & knowledge", fontsize=FS - 1.2,
        fontstyle="italic", ha="right", va="center", color=GROUP_EDGE)
module(1.55, 0.13, 2.85, 1.15, 4, "Data",
       "rider GPX, CWA, TDX,\nterrain (DTM), OSM,\nfuel stations,\nGoogle Routes API")
module(2.97, 0.13, 4.27, 1.15, 5, "Analytics",
       "personal pace model\n(P50/P90), risk rules,\nfuel-range and\ndaylight checks")
module(4.39, 0.13, 5.62, 1.15, 6, "Knowledge",
       "RAG over CWA warnings,\nhighway info, riding\nsafety, motorcycle\nspecs (cited)")

# ---------------------------------------------------------------- arrows
arrow((0.65, 2.80), (0.65, 2.50))                                  # 1 -> 2
poly([(1.25, 2.12), (1.42, 2.12), (1.42, 2.82), (1.60, 2.82)])     # 2 -> orchestrator
arrow((2.125, 2.15), (2.125, 2.60), both=True)                     # orchestrator <-> memory
arrow((2.65, 2.82), (3.00, 2.82))                                  # orchestrator -> pace
arrow((3.95, 2.92), (4.45, 2.92), label="ETAs", lpos=0.5)          # pace -> weather
arrow((3.95, 2.62), (4.45, 2.54))                                  # pace -> road & supply
arrow((4.20, 2.33), (4.20, 2.12))                                  # specialists -> verifier
poly([(3.00, 1.80), (2.80, 1.80), (2.80, 2.70), (2.65, 2.70)],
     label="fail: replan", lxy=(2.76, 2.36), lha="right")           # verifier -> orchestrator
poly([(4.75, 1.88), (5.80, 1.88), (5.80, 2.12), (5.90, 2.12)],
     label="pass", lxy=(5.25, 1.88), lha="center")                 # verifier -> decision
arrow((6.505, 2.50), (6.505, 2.80))                                # decision -> output
arrow((3.575, 1.55), (3.575, 1.30), both=True, label="tool calls, retrieval",
      lpos=0.5, loff=(0.08, 0), lha="left")                       # planner <-> base

out = Path(__file__).resolve().parent
fig.savefig(out / "architecture.pdf")
fig.savefig(out / "architecture.png", dpi=200)
print("wrote", out / "architecture.pdf")
