# Figure Spec: Schema-Based Context Impact

**Figure ID:** DIVA-02  
**Type:** Before/After Comparison Chart  
**Purpose:** Visualize +23% accuracy improvement from schema-based context engineering

---

## Data

| Context Type | Accuracy (%) | Improvement |
|-------------|-------------|-------------|
| Raw Document Only | 42.3 | Baseline |
| + Schema Structure | 52.6 | +10pp |
| + Critical Facts | 65.4 | +23pp (total) |

---

## Visual Specifications

### Layout
- **Chart Type:** Stepped area chart or waterfall chart
- **Dimensions:** 1000x600px
- **Style:** Clean, minimal, emphasis on progression

### Elements

**Step 1: Baseline**
- **Height:** 42.3%
- **Color:** Light gray (#CCCCCC)
- **Label:** "Raw Document"
- **Annotation:** "Baseline: No context engineering"

**Step 2: Schema Structure**
- **Height:** 52.6%
- **Color:** Medium blue (#5DADE2)
- **Label:** "+ Schema Structure"
- **Annotation:** "+10pp improvement"
- **Arrow:** Green up-arrow showing gain

**Step 3: Critical Facts**
- **Height:** 65.4%
- **Color:** Dark blue (#2E86AB)
- **Label:** "+ Critical Facts"
- **Annotation:** "+23pp total improvement"
- **Highlight:** Bold border, emphasis box

### Schema Example Box
**Position:** Right side panel

**Content:**
```
Schema Components:
✓ Structure (sections, variables)
✓ Relationships (key connections)
⚠️ CRITICAL FACTS (highlighted)
💡 Disambiguation tips
📋 Answering strategies
```

**Effect:** +23% accuracy

---

## Annotations

### Key Insight Callout
**Position:** Top center
**Content:** "Context engineering as important as model selection"
**Style:** Bold, 14pt, highlighted background

### Statistical Note
**Position:** Bottom
**Content:** "p<0.001, n=95 questions, Llama 3.2 3B model"
**Style:** Small font, gray text

---

## Comparison Table Inset

| Approach | Accuracy | Tokens | Cost |
|----------|----------|--------|------|
| Fine-tuning | ~70%* | Low | High setup |
| RAG (vector) | ~60%* | High | Medium |
| **Schema-based** | **65.4%** | **Medium** | **Low** |

*Estimated from literature

---

## Caption

> **Figure 2: Schema-Based Context Engineering Impact**  
> Progressive accuracy improvement through structured context. Adding schema structure provides +10pp gain; critical facts highlighting adds +13pp more, for +23pp total improvement (42.3% → 65.4%). This demonstrates that context engineering can achieve comparable gains to fine-tuning at fraction of the cost.

---

## Alternative Visualization: Parallel to Vector DB Chunking

### Side-by-Side Comparison

**Left Panel: Vector DB Chunking**
- Chunk size optimization
- Overlap strategy
- Metadata tagging
- Semantic boundaries

**Right Panel: Schema-Based Context**
- Section granularity
- Relationship mapping
- Critical facts highlighting
- Logical grouping

**Connection:** "Similar principles, different application"

---

## Key Messages

1. **Structured context matters** - Not just model size
2. **+23% improvement** - Measurable, reproducible
3. **Cost-effective** - No fine-tuning required
4. **Generalizable** - Applicable to other document types

---

## Export Formats

- **Publication:** PDF, 300 DPI, CMYK
- **Presentation:** PNG with transparent background
- **Web:** SVG for interactivity
- **Poster:** High-res TIFF

---

## Animation Sequence (for presentations)

1. **Frame 1:** Raw document baseline appears
2. **Frame 2:** Schema structure adds, bar grows with +10pp label
3. **Frame 3:** Critical facts highlight, bar reaches 65.4% with +23pp total
4. **Frame 4:** Key insight callout appears
5. **Frame 5:** Comparison table fades in

**Duration:** 10-15 seconds total

---

**Status:** Specification complete  
**Novel Contribution:** First visualization of schema-as-chunking paradigm  
**Impact:** Demonstrates context engineering effectiveness

