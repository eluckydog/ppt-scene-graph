# PPT Scene Graph

PowerPoint 视觉场景图 —— 让 AI 看懂幻灯片布局。

---

## 这是什么？

PPT Scene Graph 从 PowerPoint 文件中提取结构化视觉信息，让 AI 能够：

- **解析** 幻灯片布局为元素树
- **理解** 空间关系（左/右/上/下/重叠）
- **识别** 布局模式（单列/双列/网格）
- **精确操作** 特定元素

不再把 PPT 当作不透明的二进制文件，这个库暴露了人类能看到但机器 traditionally 无法访问的视觉结构。

---

## 核心概念：视觉场景图

```python
from ppt_scene_graph import parse_slide

slide = parse_slide("presentation.pptx", slide_idx=0)

# 你得到的是：
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

## 安装

```bash
pip install python-pptx
# 然后将 ppt_scene_graph/ 复制到你的项目中
```

---

## 快速开始

```python
from ppt_scene_graph.pipeline import beautify, evaluate

# 使用主题美化现有 PPT
beautify("input.pptx", theme="projection", output_path="output.pptx")

# 评估 PPT 质量
evaluate("presentation.pptx")
```

---

## 设计哲学

这是基础设施代码。它能工作。你怎么用是你的事。

---

## 许可证

MIT

---

## 致谢

基于 [python-pptx](https://github.com/scanny/python-pptx)（Steve Canny 开发）构建。
