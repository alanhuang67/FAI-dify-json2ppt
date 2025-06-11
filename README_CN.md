# JSON 到 PPTX Dify 插件

## 简介

Presented by Fantasy AI Studio!

`fai-dify-json2ppt` 是一个基于 python-pptx 开发的 Dify 插件，旨在帮助用户将结构化的 JSON 数据转换为精美的 PowerPoint 演示文稿（PPTX 文件）。通过简单的 JSON 定义，您可以快速生成多页的、包含标题和内容的投影片。

## 功能特性

*   **JSON 格式优势:** 相比 Markdown，JSON 格式能够精确控制演示文稿的布局和格式，确保生成专业、美观的投影片。
*   **模板灵活性:** 插件提供两个内置模板：`default.pptx` (默认使用) 和 `FAI.pptx`。您也可以使用自己的自定义 PPTX 模板以保持品牌一致性。
*   **自定义模板支持:** 将 PPTX 模板文件放置在插件的 `templates` 目录中，并在插件节点配置中指定模板名称。

**重要提示:**
*   JSON 格式必须严格正确 - 任何语法错误都会导致演示文稿生成失败。
*   布局名称和占位符键名必须与模板结构完全匹配。
*   文本内容中的换行需要使用 `\\n` 转义。如果不需要文本框顶部出现空行，请避免在文本内容开头使用 `\\n`。
*   列表项中支持 Markdown 格式（如 `**加粗**`）。
*   为避免列表中产生不必要的 PPT 空行，请确保起始中括号 `[` 与第一个列表项在同一行，结束中括号 `]` 与最后一个列表项在同一行。
*   自定义模板需要放置在插件的 `templates` 目录中，并在插件节点设置中指定使用。

## 安装与部署

1.  **访问 Dify 应用市场:** 进入您工作区的 Dify 应用市场。
2.  **查找插件:** 搜索 "JSON to PPTX" 或 "fai-dify-json2ppt"。
3.  **安装:** 点击"安装"按钮将插件添加到您的工作区。
4.  **配置:** 插件将自动配置并可在您的应用中直接使用。

注意：本插件正在申请加入 Dify Marketplace。在此期间，您可以通过以下方式下载并使用最新版本：
1. 从 releases 页面下载 .difypkg 文件
2. 在 .env 文件中设置 FORCE_VERIFYING_SIGNATURE=false
3. 通过 Dify 的插件管理界面进行本地安装

## JSON 示例

以下是完整的 JSON 格式示例，展示了所有支持的投影片布局及其定义方式：

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

## 联系方式: alan.huang67@gmail.com
