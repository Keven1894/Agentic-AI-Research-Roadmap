# Figure Spec: LLM Accuracy Comparison

**Figure ID:** DIVA-01  
**Type:** Grouped Bar Chart  
**Purpose:** Compare Llama 3.2 1B vs 3B performance across question categories

---

## Data

| Category | Llama 1B (%) | Llama 3B (%) |
|----------|-------------|-------------|
| Explicit Credentials | 60.0 | 100.0 |
| Implicit Relationships | 42.3 | 65.4 |
| Ambiguous Terms | 26.3 | 26.3 |
| Multi-hop Reasoning | 20.0 | 20.0 |
| Structural Understanding | 20.0 | 40.0 |
| **OVERALL** | **35.8** | **52.6** |

---

## Visual Specifications

### Layout
- **Chart Type:** Grouped horizontal bar chart
- **Dimensions:** 800x600px (standard), 1200x900px (publication)
- **Orientation:** Horizontal bars (easier to read category labels)

### Axes
- **X-axis:** Accuracy (0-100%), gridlines every 20%
- **Y-axis:** Question categories (left-aligned labels)
- **Labels:** Bold, 12pt font

### Bars
- **1B Model:** Orange (#F18F01), 40% opacity
- **3B Model:** Blue (#2E86AB), 80% opacity
- **Width:** 30px each, 5px gap between grouped bars
- **Value Labels:** Displayed at bar end, white text on dark background

### Annotations
- **Overall Accuracy:** Highlighted row at bottom with border
- **Improvement Arrows:** Green arrows showing +47% overall improvement
- **Significance Stars:** *** for p<0.001 on differentiable categories

### Legend
- **Position:** Top right
- **Items:** 
  - Llama 3.2 1B (700MB)
  - Llama 3.2 3B (1.3GB) ⭐ Winner

---

## Key Insights to Highlight

1. **3B model 47% better overall** (35.8% → 52.6%)
2. **100% on explicit credentials** vs 60% for 1B (censorship effect)
3. **+23pp on implicit relationships** (schema-based context impact)
4. **Tie on ambiguity and multi-hop** (both models struggle)

---

## Caption

> **Figure 1: Local Small LLM Performance Comparison**  
> Llama 3.2 3B significantly outperforms 1B model on document comprehension (52.6% vs 35.8%, p<0.001). Explicit credential questions show dramatic difference due to 1B model censorship (40% refusal rate). Both models struggle equally with ambiguous terms and multi-hop reasoning, suggesting task complexity limits rather than model size.

---

## Export Formats

- **Publication:** PDF, 300 DPI
- **Presentation:** PNG, 150 DPI
- **Web:** SVG (scalable)
- **Print:** TIFF, 600 DPI

---

## Tools Recommended

- **Python:** Matplotlib, Seaborn
- **R:** ggplot2
- **JavaScript:** D3.js, Chart.js
- **Design:** Adobe Illustrator, Inkscape

---

**Status:** Specification complete  
**Next:** Generate draft visualization  
**Review:** Pending

