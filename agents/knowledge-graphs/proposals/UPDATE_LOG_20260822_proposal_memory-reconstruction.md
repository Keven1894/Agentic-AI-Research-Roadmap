# UPDATE_LOG: Proposal — Memory Reconstruction

**Date**: 2026-08-22
**Author (agent)**: envita-builder
**Slug**: memory-reconstruction
**Proposed node type**: knowledge
**Target graph**: builder-knowledge

---

## Justification (the "why")

The framework's premise is that the host is a carrier, not the agent; it follows that no part of the agent may live only in the carrier. Working state was the last part still host-bound, so an agent could recall the organization's accepted design but not what it did yesterday. This node records the design that closes that gap: identity is derived from the VCS remote on each host rather than transferred between hosts, which makes support cost linear in hosts instead of quadratic in host pairs and removes any dependency on an editor's private store.

## Source context

Authored 2026-08-22 alongside the shipped implementation in agentloom-runtime (docs/memory/memory-reconstruction.md, docs/memory/layer-0-session-memory.md, module agentloom_runtime.session).

## Proposed node

```json
{
  "id": "knowledge:builder:memory-reconstruction",
  "type": "architecture",
  "data": {
    "title": "Memory Reconstruction",
    "description": "The framework's premise is that the host is a carrier, not the agent; it follows that no part of the agent may live only in the carrier. Working state was the last part still host-bound, so an agent could recall the organization's accepted design but not what it did yesterday. This node records the design that closes that gap: identity is derived from the VCS remote on each host rather than transferred between hosts, which makes support cost linear in hosts instead of quadratic in host pairs and removes any dependency on an editor's private store.",
    "category": "builder-proposed",
    "path": "docs/builder/architecture/memory-reconstruction.md",
    "tags": [
      "builder",
      "proposed"
    ]
  },
  "relationships": {
    "parent": "knowledge:builder:root",
    "children": []
  }
}
```

## Reviewer notes

_(none)_
