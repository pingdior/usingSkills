# usingGPT
[分享国外GPT三大金刚：chatGPT\Claude2.0\Bard的使用、比较和常用结构化提示词写法](https://www.bilibili.com/video/BV1CF411r7yC/?spm_id_from=333.999.0.0&vd_source=116dd22e64fc447e82d65ff22f074d1b)

### 例子展示
- chatGPT3.5：非结构：小红书爆款标题；结构（COT）：三个专家：营养、产品需求规格说明书专家、心理洞察伙伴（Younce）,以上例子可以从文件里看到（包括提示词妈妈）。
    - 可以生成提示词的提示词：[Role-Prompt的妈妈.md](https://github.com/pingdior/usingGPT/blob/main/Role-Prompt%E7%9A%84%E5%A6%88%E5%A6%88.md)
    - 可以对结构提示词进行评分的提示词：[Role- 结构提示词的评分专家.md](https://github.com/pingdior/usingGPT/blob/main/Role-%20%E7%BB%93%E6%9E%84%E6%8F%90%E7%A4%BA%E8%AF%8D%E7%9A%84%E8%AF%84%E5%88%86%E4%B8%93%E5%AE%B6.md)
    - 可以通过产品定位、用户故事生成产品需求规格说明书的提示词：[Role- 产品需求规格说明书设计专家.md](https://github.com/pingdior/usingGPT/blob/main/Role-%20%E4%BA%A7%E5%93%81%E9%9C%80%E6%B1%82%E8%A7%84%E6%A0%BC%E8%AF%B4%E6%98%8E%E4%B9%A6%E8%AE%BE%E8%AE%A1%E4%B8%93%E5%AE%B6.md)
    - 可以通过输入个人资料和职位信息，自动生成匹配关键字、高质量的中英文简历：[Role- Resume ExpertV1.0.md](https://github.com/pingdior/usingGPT/blob/main/Role-%20Resume%20ExpertV1.0.md)
- Claude2.0 论文解读，支持10万单词或短语解读，支持PDF、Docx、TXT、CSV、MD、ini 等很多格式
    - 研究的是什么问题，如何研究的和最后得到哪些对行业有贡献的结论。
    - 罗列本文的观点、要点和不足之处
- Bard在线解读论文

小贴士：“西红柿炒钢丝球的做法？”以上三个GPT的智能达不到，结果不正确。poe里头的GPT4是正确的，他是quara公司在chatgpt3.5之上再训练的。

### 定义和各自特点
| 模型 | 优势 | 弱势 |  适用场景 |
| --- |  --- | --- | --- |
| chatGPT-3.5 | - 对话能力<br>- 支持结构化提示词<br>- 支持语言、语调和风格设置<br>- 支持提示词免费商店参考<br>- 交互方便，支持保存聊天频道 | - 训练数据集有偏见<br>- 不是实时联网<br>- 无法支持长文档<br>- 无法支持附件 | - 对话式chatbot eg:营养师 |
| Claude 2.0 | - 支持长文档更快的推理速度<br>- 更好的常识理解<br>- 回答相对更严谨 | - 对话仍有局限<br>- 数学与编程弱项<br>- 不是实时联网 | - 文档理解<br>- 回答比较严谨 eg:附件论文理解 |
| Bard | - 更广泛的知识<br>- 可联网，可实时查询 | - 存在错误信息<br>- 可解释性有限<br>- 无法支持长文档<br>- 无法支持附件 | - 网上搜索<br>- 在线论文解读<br>- 知识问答 eg:线上论文理解 |

这些例子只是GPT工具的一小部分使用方法，在数据处理、代码生成等方面，仍然有不错表现，期待大家更多的挖掘。
另一个方面，大家也可以看到，开发软件产品、特别是知识交流类，有了新的形式来设计最小可测试的产品模型。

### 如何使用：
- 目前国内可以用：我们可以直接在slackAPP上使用claude1.0、notion.ai
- [Claude2.0 网址](https://claude.ai/)
- [Bard](https://bard.google.com/?hl=zh_CN)
- [chatGPT3.5](https://chat.openai.com/)

另外大家可以看到，目前能更好使用GPT，写好提示词是非常重要的事情。目前普通和COT结构化的提示词，提升输出的准确率。

### 如何写好提示词：现在我们可以在提示词商店获取提示词样例来学习和使用
- https://www.aimappro.com/prompts.html
- 需要魔法：
    - chatgpt3.5：https://datafit.ai/
    - https://flowgpt.com/prompt

最后分享下和群友交流的当下初步共识是：普通人结合行业基本知识，合理提示词输入后，可以达到行业60分左右的认知；结合行业知识精细喂养这类辅助工具，可达到80分以上的认知水平和获取行业一般框架，但是更深入的认知，需要更多喂养和期待GPT更智能。
