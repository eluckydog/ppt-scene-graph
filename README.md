# PPT Scene Graph

Visual Scene Graph for PowerPoint —— Let AI see and understand slide layouts.

---

## What is this?

PPT Scene Graph extracts structured visual information from PowerPoint files, enabling AI agents to:

- **Parse** slide layouts into element trees
- **Understand** spatial relationships (left-of, above, overlaps)
- **Detect** layout patterns (single-column, two-column, grid)
- **Operate** on specific elements programmatically

Instead of treating PPT as opaque binary files, this library exposes the visual structure that humans see but machines traditionally couldn't access.

---

## Core Concept: Visual Scene Graph

```python
from ppt_scene_graph import parse_slide

slide = parse_slide("presentation.pptx", slide_idx=0)

# What you get:
{
    "elements": [
        {"id": "title", "type": "text", "bbox": [0, 0, 4000000, 800000]},
        {"id": "img1", "type": "picture", "bbox": [5000000, 1000000, 3000000, 2000000]}
    ],
    "relations": [
        {"source": "title", "target": "img1", "relation": "left_of"}
    ],
    "layout_pattern": "two_column"
}
```

---

## Installation

```bash
pip install python-pptx
# Then copy ppt_scene_graph/ to your project
```

---

## Quick Start

```python
from ppt_scene_graph.pipeline import beautify, evaluate

# Beautify existing PPT with theme
beautify("input.pptx", theme="projection", output_path="output.pptx")

# Evaluate PPT quality
evaluate("presentation.pptx")
```

---

## Design Philosophy

This is infrastructure code. It works. How you use it is your business.

---

## License

MIT

---

## Acknowledgments

Built on top of [python-pptx](https://github.com/scanny/python-pptx) by Steve Canny.
