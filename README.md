# JSON to PPTX Dify Plugin

## Introduction

Presented by Fantasy AI Studio!

The `fai-dify-json2ppt` plugin for Dify is designed to convert structured JSON data into elegant PowerPoint presentations (.PPTX files). Built with python-pptx, this tool allows users to rapidly generate multi-slide presentations, complete with titles and and content, by simply defining their slides in a straightforward JSON format.

## Features

*   **JSON Format Advantage:** Unlike Markdown, JSON provides precise control over presentation layout and formatting, ensuring consistent and professional-looking slides.
*   **Template Flexibility:** The plugin provides two built-in templates: `default.pptx` (used by default) and `FAI.pptx`. You can also use your own custom PPTX templates for consistent branding.
*   **Custom Template Support:** Place your PPTX templates in the plugin's `templates` directory and specify the template name in the plugin node configuration.

**Important Notes:**
*   JSON format must be strictly valid - any syntax errors will prevent the presentation from being generated.
*   Layout names and placeholder keys must exactly match your template's structure.
*   Use `\\n` for line breaks within text content. Avoid starting text content with `\\n` if an empty line at the top of the textbox is undesired.
*   Markdown formatting (like `**bold**`) is supported in list items.
*   To prevent unwanted new lines in PPT generated from lists, ensure the opening `[` is on the same line as the first item and the closing `]` is on the same line as the last item.
*   Custom templates should be placed in the plugin's `templates` directory and specified in the plugin node settings.

## Installation and Deployment

1.  **Visit Dify Marketplace:** Go to the Dify Marketplace in your workspace.
2.  **Find the Plugin:** Search for "JSON to PPTX" or "fai-dify-json2ppt".
3.  **Install:** Click the "Install" button to add the plugin to your workspace.
4.  **Configure:** The plugin will be automatically configured and ready to use in your applications.


## JSON EXAMPLE

```json
{
  "slides": [
    {
      "layout": "Title Slide",
      "elements": {
        "Title 1": "项目凤凰：新纪元",
        "Subtitle 2": "2024 年创新与增长"
      }
    },
    {
      "layout": "Title and Content",
      "elements": {
        "Title 1": "执行摘要",
        "Content Placeholder 2": "我们的新倡议，项目凤凰，旨在通过尖端技术和战略伙伴关系彻底改变市场。\\n本演示文稿概述了我们未来一年的愿景、关键策略和预期成果。我们致力于为所有利益相关者提供无与伦比的价值。"
      }
    },
    {
      "layout": "Section Header",
      "elements": {
        "Title 1": "第一章：市场概况",
        "Text Placeholder 2": "理解当前趋势",
        "Section Number 3": "1"
      }
    },
    {
      "layout": "Two Content",
      "elements": {
        "Title 1": "市场分析与机遇",
        "Content Placeholder 2": [
          "**市场趋势：**",
          "- 技术快速普及",
          "- 对可持续解决方案的需求增加",
          "- 向个性化体验转变"
        ],
        "Content Placeholder 3": [
          "**已识别的机遇：**",
          "- 尚未开发的利基市场",
          "- 战略合作伙伴关系以实现扩张",
          "- 利用人工智能提高效率"
        ]
      }
    },
    {
      "layout": "Comparison",
      "elements": {
        "Title 1": "传统方法与凤凰方法",
        "Text Placeholder 2": "传统方法",
        "Content Placeholder 3": [
          "- 大量人工投入",
          "- 可扩展性有限",
          "- 部署周期较慢",
          "- 被动式问题解决"
        ],
        "Text Placeholder 4": "凤凰方法",
        "Content Placeholder 5": [
         "- 自动化流程",
          "- 高度可扩展的架构",
          "- 敏捷快速部署",
          "- 主动式创新"
         ]
      }
    },
    {
      "layout": "Content with Caption",
      "elements": {
        "Title 1": "关键里程碑",
        "Content Placeholder 2": "[插入图表或信息图表的图片占位符]\\n我们的路线图侧重于实现产品开发、市场渗透和客户获取方面的关键里程碑。每个阶段都经过精心规划，以确保最大的影响和可持续增长。",
        "Text Placeholder 3": "图 1：项目时间表与交付成果"
      }
    },
    {
      "layout": "Title Only",
      "elements": {
        "Title 1": "团队与领导"
      }
    },
    {
      "layout": "Blank",
      "elements": {}
    },
    {
      "layout": "End Slide",
      "elements": {
        "Title 1": "期待与您共创辉煌！",
        "Subtitle 2": "Queries & Discussion"
      }
    }
  ]
}
```
