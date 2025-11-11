# Agentic-AI-Research-Roadmap
**Agentic-AI Engineering Framework to Build Reliable AI Agents**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17561541.svg)](https://doi.org/10.5281/zenodo.17561541)
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)
![Made with: GPT-5 · Claude 4.5 · Cursor](https://img.shields.io/badge/Made%20with-GPT--5%20·%20Claude%204.5%20·%20Cursor-blue)

**Author:** Dr. Boyuan (Keven) Guan  
**Affiliation:** FIU Library & GIS Center  
**First Public Release:** November 8, 2025  
**Version:** 1.1.0  
**DOI:** [10.5281/zenodo.17561541](https://doi.org/10.5281/zenodo.17561541)

---

## Mission

**This repository explores how large-language-model agents can evolve through documented, reproducible, and production-grade workflows.** The goal is to make intelligent systems learn from real-world experience as human engineers do.

**New here?** Start with **[START HERE](docs/START_HERE.md)** for quick onboarding! 🚀

## Overview

This repository documents and open-sources the foundation of the **Agentic-AI Engineering Framework**, a systematic methodology that transforms AI from theoretical reasoning to practical, production-ready systems.

While Large Language Models (LLMs) are powerful theorists, **Agents are practitioners** — operating in real environments, performing concrete tasks, and learning through trial and feedback.

## The Core Framework

Our framework implements a closed learning loop:

> **Context → Documentation → Indexing → RAG → Fine-Tuning**

Where each stage strengthens the next:
- **Context** captures the working environment and raw artifacts
- **Documentation** turns experience into reusable knowledge
- **Indexing** organizes knowledge for retrieval and reasoning
- **RAG** (Retrieval-Augmented Generation) connects AI reasoning to verified data
- **Fine-Tuning** distills accumulated experience into domain-specialized models

This transforms one-off AI experiments into **continuous, evidence-based AI systems**.

## Key Insight

**"LLM is the theorist, Agent is the practitioner."**

To bring AI from conversation to production, we must systematize how agents:
- Accumulate knowledge from real tasks
- Document their decision-making processes
- Evolve through structured feedback loops
- Persist context across interactions

## Framework Foundations

The Agentic-AI Engineering Framework addresses a critical research gap: **the engineering lifecycle of production-grade agentic systems**. While most research focuses on agent capabilities (reasoning, planning, learning), our framework tackles the complementary problem of building agents that are maintainable, evolvable, accountable, and scalable.

**Core Documents:**
- **[Framework Foundations](docs/framework-foundations.md)** — Theoretical underpinnings and key questions
- **[Research Problems & Positioning](docs/research-problems-and-positioning.md)** — Academic landscape and how our framework addresses known gaps
- **[Dual-Helix Clarification](docs/dual-helix-clarification.md)** — Engineering strand (this repo) vs. Governance strand (co-agenticOS)
- **[Agentic Collaboration Guide](docs/agentic-collaboration-guide.md)** — Complete methodology for working at AI-augmented velocity

## Research Vision

Establish a **repeatable, scalable, and evaluable Agentic-AI engineering framework** that integrates LLM reasoning with traditional software engineering discipline, enabling sustainable AI engineering where AI systems:
- Not only respond but **operate**
- Not only answer but **record**
- Not only reason but **evolve**

## Repository Structure

```
Agentic-AI-Research-Roadmap/
├── README.md                              # This file — Start here!
├── CONTRIBUTING.md                        # How to contribute (v2.0 - Agentic Collaboration)
├── CONTRIBUTORS.md                        # Recognition and attribution
├── LICENSE                                # CC BY-NC 4.0
├── CITATION.cff                           # Zenodo citation metadata
├── DUAL_REPO_STRATEGY.md                  # GitHub (public) + GitLab (full) strategy
│
├── docs/                                  # 📚 Core Documentation
│   ├── START_HERE.md                      # ⭐ Quick onboarding (read this first!)
│   ├── Agentic-AI-Research-Roadmap.md     # Complete research roadmap
│   ├── Research-Timeline-2025-2027.md     # Milestones and deliverables
│   │
│   ├── Framework Core (WHAT + WHY + HOW)
│   ├── framework-foundations.md           # Theoretical underpinnings (F1-F7)
│   ├── research-problems-and-positioning.md # Academic landscape and positioning
│   ├── dual-helix-clarification.md        # Engineering vs. Governance strands
│   ├── agentic-collaboration-guide.md     # Complete methodology (11K words!)
│   │
│   ├── case-studies/                      # 🔬 Production Validations
│   │   ├── README.md                      # Case study template and guide
│   │   └── dataverse-diva.md              # Digital libraries (Stage 2, 3+ months)
│   │
│   └── Supporting Documentation
│       ├── getting-started.md
│       ├── co-agenticOS-integration-guide.md
│       ├── DISCUSSION_TEMPLATE.md
│       └── ZENODO_INTEGRATION.md
│
├── figures/                               # 📊 Diagram Specifications
│   ├── dual-helix-diagram-spec.md         # Engineering + Governance strands
│   ├── memory-hierarchy-analogy-diagram.md # Computer architecture analogy
│   └── private/                           # 🔒 NOT in Git (DIVA figures)
│
├── .github/                               # GitHub Configuration
│   └── PULL_REQUEST_TEMPLATE.md           # Case study submission checklist
│
├── meta/                                  # 🗂️ Project Metadata
│   ├── directory-index.yaml               # Directory structure and purpose
│   ├── search-manifest.json               # Document collections for RAG/search
│   └── README.md                          # Metadata documentation
│
├── .cursor/                               # 🤖 AI Collaboration Rules
│   └── rules.md                           # Canonical references and editing policy
│
├── archives/                              # 📦 Historical Materials
│   ├── EDITORIAL_REVIEW_SUMMARY.md
│   └── inputRAW/dataverse-diva/           # DIVA extraction (9 detailed docs)
│
├── drafts/                                # 📝 Pre-Publication Materials
│   ├── public/                            # ✅ Shareable outlines and roadmaps
│   └── private/                           # 🔒 NOT in Git (full drafts, sensitive)
│
├── experiments/                           # 🧪 Experimental Code & Studies
│   └── private/                           # 🔒 NOT in Git (DIVA experiments)
│
└── temp/                                  # 🗃️ Working Documents & Summaries
    └── [Session summaries and documentation]
```

## Experimental Domains

We are validating this framework across multiple domains:

| Domain | Use Case | Expected Outcome |
|--------|----------|------------------|
| **GIS / Environmental Data** | Automatic buoy data annotation, anomaly detection (EnviStor) | Validate RAG for spatiotemporal reasoning |
| **Digital Libraries** | Metadata repair, catalog enrichment (Dataverse) | Improve retrieval precision |
| **Education** | AI teaching assistants, research support | Demonstrate adaptive learning |
| **IT Operations** | Log analysis, system self-healing | Evaluate feedback loops |
| **Industry Applications** | Multi-agent coordination systems | Measure operational reliability |

## Engineering Framework

Based on the **Agentic-Dev Workflow**:

```
Plan → Implement → Verify → Document → Summarize → Iterate
```

**Core Elements:**
- `.cursor/rules.md` — Context-aware AI editing policy
- `decision_log/` — Persistent design rationale
- `daily/` — Auto-summaries of activity and changes
- **CI/CD + Changesets** — Continuous integration with changelog tracking
- **Documentation Site** — Public transparency and collaboration

## How to Contribute

**Want to contribute?** We welcome case studies, research collaborations, and community engagement!

**Quick Links:**
- 📖 **[CONTRIBUTING.md](CONTRIBUTING.md)** — Contribution pathways and process
- 🤝 **[Case Studies Guide](docs/case-studies/README.md)** — Submit your framework validation
- 🎯 **[Agentic Collaboration Guide](docs/agentic-collaboration-guide.md)** — Learn the high-velocity methodology
- 🌟 **[CONTRIBUTORS.md](CONTRIBUTORS.md)** — See who's involved and how you'll be credited

**New to the framework?** Start with **[START HERE](docs/START_HERE.md)** for a guided onboarding!

---

## Collaboration

We welcome collaborations with:
- **Academic Institutions** — Research validation and datasets
- **Industry Partners** — Real-world deployment and feedback
- **Open Source Community** — Tools, benchmarks, and standards

**Current Partners:**
- FIU Library & GIS Center (lead)
- FIU Computer Science Department
- FIU Division of IT
- Pelican, OSG, and other research infrastructure partners

## Agentic-AI Ecosystem

This framework is implemented and validated through a connected ecosystem of projects:

### Core Components

| Repository | Role | Description |
|------------|------|-------------|
| **[Agentic-AI-Research-Roadmap](https://github.com/Keven1894/Agentic-AI-Research-Roadmap)** | 🎓 Theory & Methodology | Framework definition, research roadmap, and academic foundation |
| **[co-agenticOS](https://github.com/Keven1894/co-agenticOS)** | 🧠 Execution & Governance | Runtime system for agent behavior rules, coordination protocols, and operational standards |

### Implementation Layer (Planned)

- **EnviStor Agentic Case** - Environmental data management validation
- **Dataverse Agentic Case** - Digital library metadata curation
- **Multi-Agent Coordination** - System orchestration examples

### Relationship

```
[Agentic-AI Framework]  → defines what agents should do and how they learn
         ↓
[co-agenticOS]         → implements how agents behave and cooperate at runtime
         ↓
[Domain Applications]  → validates framework in real-world scenarios
```

**For implementation details and operational guidelines, see [co-agenticOS](https://github.com/Keven1894/co-agenticOS).**

## Publications & Roadmap

**Stage 1 (2025 Q4):** Framework workshop paper  
**Stage 2 (2026 Q1-Q3):** Domain-specific case studies  
**Stage 3 (2026 Q4):** Integrative system paper  
**Stage 4 (2027):** Monograph and curriculum development

See [Research Timeline](docs/Research-Timeline-2025-2027.md) for detailed milestones.

### 🔒 Privacy & IP Protection

⚠️ **Note**: This project uses a **dual-repository strategy** to balance open science with IP protection.

**This Repository (GitHub - Public)**
- Framework methodology and conceptual materials
- High-level documentation and guides
- All `private/` folders are excluded via `.gitignore`

**Full Repository (GitLab - Private)**
- Complete research materials including experimental data
- Detailed DIVA case study with metrics and analysis
- All `private/` folders with sensitive content

**Protected Content** (GitLab only):
- `drafts/private/` - Full paper drafts with experimental data
- `experiments/private/dataverse-diva/` - Complete DIVA experiments
- `figures/private/dataverse-diva/` - All DIVA figures and charts

For details, see [`DUAL_REPO_STRATEGY.md`](DUAL_REPO_STRATEGY.md).

## Expected Outcomes

| Type | Description |
|------|-------------|
| **Software** | Open-source Agentic-Dev Workflow template and toolkit |
| **Publications** | Peer-reviewed papers at PEARC, JCDL, ICSE, AI-Engineering venues |
| **Education** | Agentic-AI course modules and tutorials |
| **Datasets** | Curated agent-interaction logs for research use |
| **Industry Pilots** | Operational agents in production systems |

## Citation

If you reference this framework or methodology, please cite:

```bibtex
@software{guan2025agenticai,
  author = {Guan, Boyuan (Keven)},
  title = {Agentic-AI Lab: Engineering the Next Generation of Intelligent Systems},
  year = {2025},
  publisher = {Zenodo},
  version = {1.1.0},
  doi = {10.5281/zenodo.17561541},
  url = {https://doi.org/10.5281/zenodo.17561541}
}
```

## Contact

**Dr. Boyuan (Keven) Guan**  
Lead Developer & Research Engineer  
FIU Library & GIS Center  
📧 bguan@fiu.edu  
🌐 https://dataversedev.fiu.edu/ai/

---

## License

© 2025 Dr. Boyuan (Keven) Guan, FIU Library & GIS Center

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit
- **NonCommercial** — You may not use the material for commercial purposes

---

*This repository is a living research project. Contributions, collaborations, and feedback are welcome.*

**Last Updated:** November 11, 2025

