# Local Small LLM Evaluation - Methodology

**Research Question:** Can small local LLMs (Llama 3.2 1B/3B) accurately answer questions about configuration files in production systems?

**Hypothesis:** Small models (1-3B parameters) can achieve >50% accuracy on document comprehension with proper context engineering.

---

## Study Design

### Test Document
- **Type:** Environment configuration file (.env)
- **Size:** 54 lines, 1496 characters
- **Complexity:** Database credentials, server URLs, API keys, cross-environment relationships
- **Domain:** Dataverse institutional repository configuration

### Models Tested
| Model | Parameters | Size | Avg Response Time | Use Case |
|-------|-----------|------|-------------------|----------|
| Llama 3.2 1B | 1 billion | 700MB | 3.10s | Ultra-fast queries |
| Llama 3.2 3B | 3 billion | 1.3GB | 3.61s | Balanced quality/speed |

### Question Set Design
**Total Questions:** 95  
**Distribution:**
- Easy (31.6%): Explicit information retrieval
- Medium (45.3%): Implicit relationship inference
- Hard (23.2%): Multi-hop reasoning

**Categories:**
1. **Explicit Credentials** (15 questions) - Direct value lookups
2. **Implicit Relationships** (26 questions) - Inferred connections
3. **Ambiguous Terms** (19 questions) - Context-dependent meanings
4. **Multi-hop Reasoning** (15 questions) - Multiple inference steps
5. **Structural Understanding** (20 questions) - Document organization

---

## Context Engineering

### Schema-Based Approach
Treating document schemas like vector database chunking strategies:

```json
{
  "document_type": "configuration_file",
  "structure": {
    "sections": [...]
  },
  "relationships": {
    "key": "value pairs showing connections"
  },
  "criticalFacts": [
    "⚠️ CRITICAL: Production uses localhost, NOT dpantherdb04temp",
    "⚠️ CRITICAL: All environments share same database server"
  ],
  "ambiguities": [
    {
      "term": "localhost",
      "correct_meaning": "Local PostgreSQL instance",
      "incorrect_meaning": "Remote server"
    }
  ],
  "tips": [
    "When asked about 'production database', answer 'localhost'"
  ]
}
```

### Validation Approach
- **Ground Truth:** Human-verified correct answers
- **Automated Testing:** Python script (`test_doc_reader.py`)
- **Scoring:** Exact match or semantic equivalence
- **Statistical Analysis:** Chi-square test for significance

---

## Experimental Procedure

1. **Baseline Test:** Raw document + question (no schema)
2. **Structure Test:** Document + schema structure
3. **Critical Facts Test:** Document + schema + critical facts
4. **Full Context Test:** Complete schema with tips and disambiguations

---

## Data Collection

### Metrics Captured
- Accuracy (% correct answers)
- Response time (seconds)
- Success rate (% non-error responses)
- Refusal rate (% "I can't answer" responses)
- Confidence indicators

### Sample Size
- 190 total tests (95 questions × 2 models)
- Sufficient for statistical significance (p < 0.001)

---

## Expected Outcomes

**Hypothesis 1:** 3B model will outperform 1B model  
**Hypothesis 2:** Schema-based context will improve accuracy by >15%  
**Hypothesis 3:** Small models will struggle with multi-hop reasoning (<30% accuracy)  
**Hypothesis 4:** Production deployment feasible if accuracy >50% and latency <5s

---

## Ethical Considerations

- Test data contains sample credentials (non-production)
- No personal or sensitive information in questions
- Results will not be used to replace human oversight
- Privacy-preserving: All processing local, no data leaves institution

---

## Reproducibility

### Requirements
- Ollama (local LLM runner)
- Llama 3.2 1B and 3B models
- Python 3.8+ with requests library
- Test environment configuration file

### Code Availability
- Test script: `code/test_doc_reader.py`
- Schema templates: `research/schemas/`
- Results analysis: `research/local-small-llm/results/`

---

**Last Updated:** 2025-11-09  
**Status:** Complete (190 tests executed)

