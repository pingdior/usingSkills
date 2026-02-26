---
id: cceb95cf-bf73-4515-8e8d-5a9615c17a0e
---

# Gen-3 Alpha 提示指南 – Runway

[Read on Omnivore](https://omnivore.app/me/gen-3-alpha-prompting-guide-runway-1942ea3fdc8)  
[Read Original](https://help.runwayml.com/hc/en-us/articles/30586818553107-Gen-3-Alpha-Prompting-Guide)

## Article Excerpt:


### https://help.runwayml.com/hc/en-us/articles/30586818553107-Gen-3-Alpha-Prompting-Guide
## Full Article:
  
[Gen-3 Alpha 具有无限潜力，可以在各种用例](https://runwayml.com/product/use-cases)中将您的艺术构想变为现实。创建传达场景的强大提示是生成符合您概念的[[视频]]的关键。

本文介绍了不同的示例结构、关键字和提示技巧，以帮助您开始使用 Gen-3 Alpha。这些只是示例 - 在将您的想法付诸实践时，不要害怕进行实验。

## 文章重点

* `the camera doesn't move`避免在文本提示中使用否定措辞，例如
* 使用简单直接的提示来描述使用输入图像时所需的**动作**
* 您无需在文本提示中描述输入图像

## 提示基础知识

### 所有提示都应该直接、容易理解，而不是概念性的

在编写提示时，假装您正在向不熟悉您之前的作品和偏好的审美的新合作者描述一个场景会很有帮助。这位新合作者将负责拍摄您描述的场景，因此请确保清晰地传达重要元素。

当简单的描述能够有效地传达场景时，请避免使用过于概念化的语言和措辞。 

❌ 一名男子侵入了主机。

✅ 一名男子在键盘上用力打字。

### 提示应该是描述性的，而不是对话式或命令式的

虽然外部 [[LLM]] 注重自然对话，但 Runway 的[[模型]]则注重视觉细节。在提示中添加对话内容不会给您的结果带来价值，在某些情况下甚至可能对您的结果产生负面影响。

❌ 你能给我制作一段关于两个朋友吃生日蛋糕的视频吗？

✅两个朋友吃生日蛋糕。

使用基于命令的提示可能会产生类似的负面影响，因为它可能不包含足够的细节来创建所需的场景：

❌ 在图片中添加一只狗

✅ 一只狗在镜头外顽皮地跑过田野

### 提示应使用积极的措辞

生成视频模型不支持负面提示或描述_不应_发生的事情的提示。包含负面提示可能会导致相反的情况发生。

❌ 相机不动。没有动作。天空中没有云。

✅ 静态相机。相机保持静止。晴朗的蓝天

## 纯文本提示

纯文本提示在遵循清晰的结构（将场景、主题和摄像机运动的细节分成不同的部分）时最有效。

在您熟悉 Gen-3 Alpha 时，使用以下结构应该有助于提供一致的结果：

[摄像机移动]：[建立场景]。[附加细节]。

使用这种结构，你对站在热带雨林中的女人的提示可能看起来像这样：

Low angle static shot: The camera is angled up at a woman wearing all orange as she stands in a tropical rainforest with colorful flora. The dramatic sky is overcast and gray.

Repeating or reinforcing key ideas in different sections of your [[prompt]] can help increase adherence in the output. For example, you might note that **the camera quickly flies through** the scenes in a **hyperspeed** shot.

Try to keep your prompt focused on what _should_ be in the scene. For example, you would prompt for a **clear sky** rather than a **sky with no clouds**.

## Image + Text Prompting

When using input images, use a **simple** and **direct** text prompt that describes the **movement** you'd like in the output. You **do not** need to describe the contents of the image.

In example, you might try the following prompt if using an input image that features a character:

Subject cheerfully poses, her hands forming a peace sign.

Using a text prompt that significantly differs from the input image may lead to unexpected results. Keep in mind that complex scene transitions may require multiple iterations to achieve the desired output.

## Sample Prompts

### Seamless Transitions

Continuous hyperspeed FPV footage: The camera seamlessly flies through a glacial canyon to a dreamy cloudscape.

### Camera Movement

A glowing ocean at night time with bioluminescent creatures under water. The camera starts with a macro close-up of a glowing jellyfish and then expands to reveal the entire ocean lit up with various glowing colors under a starry sky. Camera Movement: Begin with a macro shot of the jellyfish, then gently pull back and up to showcase the glowing ocean.

### Text Title Cards

A title screen with dynamic movement. The scene starts at a colorful paint-covered wall. Suddenly, black paint pours on the wall to form the word "Runway". The dripping paint is detailed and textured, centered, superb cinematic lighting.

## Prompt Keywords

Keywords can be beneficial to achieve specific styles in your output. Ensuring that keywords are cohesive with your overall prompt will make them more apparent in your output.

In example, including keywords about skin texture wouldn't be beneficial to a wide angle shot where the camera is not closely focused on a face. A wide angle shot might instead benefit from additional details about the environment.

While keeping this cohesiveness in mind, below are different keywords you can experiment with while drafting your prompts.

## Camera Styles

| **Keyword**           | **Output**                                                                                                                                                                                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Low angle             | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sn2iGdiaGDk1BdJHaDqXTmy4jiCwBPfprKGlJGdd9TOE/https://help.runwayml.com/hc/article_attachments/30858367873043)                                                                                                                                                                       |
| High angle            | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sCI2cvbH_j1KXWtq1zP5hANdSKD4HiAd2hTBeqD_yWAg/https://help.runwayml.com/hc/article_attachments/30858367874195)                                                                                                                                                                       |
| Overhead              | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sIxLuQDvokAcYssvc7yoMy5g1qw7_J-rmGweX3q4XzWQ/https://help.runwayml.com/hc/article_attachments/30858337963027)                                                                                                                                                                       |
| FPV                   | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sQAiEm1TQS_ImETrEt-RVBZSoAIScP8rQAq443NMzjxA/https://help.runwayml.com/hc/article_attachments/30858337963795)                                                                                                                                                                       |
| Hand held             | ![](https://proxy-prod.omnivore-image-cache.app/422x254,sAZ1SaDeRIJ98YBlXW7jY0MTATU3mIJF4cSzfSAtOto4/https://help.runwayml.com/hc/article_attachments/30858337965587)                                                                                                                                                                       |
| Wide angle            | ![](https://proxy-prod.omnivore-image-cache.app/422x254,sE-hV-id4Oz1tvjO_Jn4zjvperdhFYPzOsJ70Q6LVuOs/https://help.runwayml.com/hc/article_attachments/30858367878547)                                                                                                                                                                       |
| Close up              | ![](https://proxy-prod.omnivore-image-cache.app/422x254,sqbdv8Kzm9ZkFwHySBC63__GBDGGerMt3mbQpBhS5IlY/https://help.runwayml.com/hc/article_attachments/30858367880339)                                                                                                                                                                       |
| Macro cinematography  | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sZkD2y9vUV29tOozaU84EuPjQzUTMhLHhfakKpFpDpkw/https://help.runwayml.com/hc/article_attachments/30858337968787)                                                                                                                                                                       |
| Over the shoulder     | ![](https://proxy-prod.omnivore-image-cache.app/640x384,s-9xBb36myriZ5C_LhSogkkXhkmqknm6r_vfEWfd3pxk/https://lh7-us.googleusercontent.com/docsz/AD_4nXfneolQiSBAC_6C6Gyy0n1vFVJQvJllODF7kN2x1ZqckEUeX-Po-BQdQXbvQXgwJ_fS3eWynIN1EGn61Rw-8H4H4V8wkvWbLPNHfBnt00qHTmwD7O4T-p853COg0D1l2AF_8FPuEJcFrWpV0aqYJCIN6zc?key=rgGgSZfBNbssGr_ElqRs1A) |
| Tracking              | ![](https://proxy-prod.omnivore-image-cache.app/426x256,s9cHWZW-rei8s1VsWfyAPTFOqYR-O9OimWQGeZ3sqAlw/https://help.runwayml.com/hc/article_attachments/30858367881747)                                                                                                                                                                       |
| Establishing wide     | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sesuUEGhHXC7aDVJ5Y5aXtaD3fy4-AQ014JSp7AkPa3Y/https://help.runwayml.com/hc/article_attachments/30858337971475)                                                                                                                                                                       |
| 50mm lens             | ![](https://proxy-prod.omnivore-image-cache.app/426x256,swI7mOunVTOi_vO8ZtPkqpg5wu9hYKoUsa8_24AMIPng/https://help.runwayml.com/hc/article_attachments/30858337972115)                                                                                                                                                                       |
| SnorriCam             | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sQwp9ArDxfU-CrAutlgTVOgUpxvm_cuRtUjyqhOxh0bs/https://help.runwayml.com/hc/article_attachments/30858367891091)                                                                                                                                                                       |
| Realistic documentary | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sW_GuM8JDE2G0Su8hBtorzz5HiZlkHf-OsdVlmTsI0a4/https://help.runwayml.com/hc/article_attachments/30858337978771)                                                                                                                                                                       |
| Camcorder             | ![](https://proxy-prod.omnivore-image-cache.app/422x254,s-SXvUGTZiOzf0Jaknk_X-BhkthkesydITYOTNt5eH1o/https://help.runwayml.com/hc/article_attachments/30858455121427)                                                                                                                                                                       |

## Lighting Styles

| **Keyword**            | **Output**                                                                                                                                                            |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Diffused lighting      | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sjzRRMCfSKowEhWtnOs9DKauke6P8be1Y_mvs_4zAy88/https://help.runwayml.com/hc/article_attachments/30858441964051) |
| Silhouette             | ![](https://proxy-prod.omnivore-image-cache.app/426x256,siwBia6Q0nBvSTMS811YZEeeUQu9imOq293sEf7nqLo4/https://help.runwayml.com/hc/article_attachments/30858441978131) |
| Lens flare             | ![](https://proxy-prod.omnivore-image-cache.app/422x254,sBeku6NOBdZnci8tlN1YGUlR6eaPIsYQBmTIWQZXsC6o/https://help.runwayml.com/hc/article_attachments/30858441979411) |
| Back lit               | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sM5SUfKDv5gJPCaTPsC4Bo6ljFKn-rr_6BjW035Utz84/https://help.runwayml.com/hc/article_attachments/30858455132179) |
| Side lit               | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sbq-ZgDb9-i_mpg07c_Gx0n5wbywZXiOiiGOBCzsBW1M/https://help.runwayml.com/hc/article_attachments/30858441982739) |
| \[color\] gel lighting | ![](https://proxy-prod.omnivore-image-cache.app/426x256,srtex1w6W_dCHzbOXidmTF6bhOPFNT-b_P0l0fmonwXs/https://help.runwayml.com/hc/article_attachments/30858441984531) |
| Venetian lighting      | ![](https://proxy-prod.omnivore-image-cache.app/426x256,ss2aBVtwGbP78wecE5U7yYKk_mnFCa8-9AI-Fgc_ildg/https://help.runwayml.com/hc/article_attachments/30858441987347) |

## Movement Speeds

## 运动类型

| **关键词** | **输出**                                                                                                                                                                |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 成长      | ![](https://proxy-prod.omnivore-image-cache.app/426x256,szTnLW0V5G013VAjYk-lfxB-op7szcB0T8JpoIZe1BF0/https://help.runwayml.com/hc/article_attachments/30858455141779) |
| 出现      | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sOBzVroezfaPU1tq2lBlF-xQU0qJ-3Wnqo86q8lyygWA/https://help.runwayml.com/hc/article_attachments/30858455142803) |
| 爆炸      | ![](https://proxy-prod.omnivore-image-cache.app/540x304,sY2M5f-zoHc3F3TqDR6DCTh3Cxrxz2qVwZbwYN-nUAb0/https://help.runwayml.com/hc/article_attachments/30858455143571) |
| 上升      | ![](https://proxy-prod.omnivore-image-cache.app/426x256,s6Xsx5sgjO6IxhgOKmEN8fBDceYhBUg7BF7Ix94HtiAw/https://help.runwayml.com/hc/article_attachments/30858441999123) |
| 波动      | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sIX4AeDQz8d0ux1igo2ANLiXVyNQuPLTk0SFeHWcZxqs/https://help.runwayml.com/hc/article_attachments/30858441999891) |
| 扭曲      | ![](https://proxy-prod.omnivore-image-cache.app/540x304,sIH0jTdfpBQ06XBHbKUJw_D1TQK1H3sa4Q-_MIehPKD8/https://help.runwayml.com/hc/article_attachments/30858455145491) |
| 变换      | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sqc1TGvgUMPnNYnkQpqK-HSxhOPInA-CDbIeK9rfoJow/https://help.runwayml.com/hc/article_attachments/30858455146259) |
| 涟漪      | ![](https://proxy-prod.omnivore-image-cache.app/425x239,sZJ0tzqtmg8fasTyIFcpI9-4Cp0FljuojjlkW6mImbTw/https://help.runwayml.com/hc/article_attachments/30858455147155) |
| 破碎      | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sc2b93KU-gRUwJTsn0YdqNu9zxcnUzHf67b919H6-62Y/https://help.runwayml.com/hc/article_attachments/30858455148563) |
| 展开      | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sknpEHr14-o9FIQZly4arQQaPx3j_k49Sf53bfjKgnLk/https://help.runwayml.com/hc/article_attachments/30858442004755) |
| 涡流      | ![](https://proxy-prod.omnivore-image-cache.app/540x304,sS_0zsmVErzFuC53BJoDkQ0FMk5NLXhvrJ4VGuW3st2s/https://help.runwayml.com/hc/article_attachments/30858635846675) |

## 风格与美学

| **关键词**  | **输出**                                                                                                                                                                |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 穆迪       | ![](https://proxy-prod.omnivore-image-cache.app/540x304,sSkqelFv6EZnST3DHV0ujTup2F51Kb8S-dGmA5jZhD5U/https://help.runwayml.com/hc/article_attachments/30858635846931) |
| 电影       | ![](https://proxy-prod.omnivore-image-cache.app/422x254,s5IHHIEZjrvx0tBMcKNSoCiyQBJyKTrE-sb841IGOU4o/https://help.runwayml.com/hc/article_attachments/30858615644819) |
| 彩虹色      | ![](https://proxy-prod.omnivore-image-cache.app/540x304,sMiwouPKIdt02_y1HmjdBeqFlX7QCr8LlBS4_KzrIl2c/https://help.runwayml.com/hc/article_attachments/30858635848083) |
| 家庭录像 VHS | ![](https://proxy-prod.omnivore-image-cache.app/540x304,sQVUlG68z_fSzKFUxnMr0DAZnutgKS6GjtYoDJ8c8_EY/https://help.runwayml.com/hc/article_attachments/30858635848979) |
| 故障核      | ![](https://proxy-prod.omnivore-image-cache.app/600x338,stPr3pqcksgtG6RbllhNotZ9Q6kmyKX-fYN0p7Hm_DGs/https://help.runwayml.com/hc/article_attachments/30858635849363) |

## 文本样式

| **关键词** | **输出**                                                                                                                                                                |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 大胆的     | ![](https://proxy-prod.omnivore-image-cache.app/426x256,sX4xinKJgGJycX9pa5c-J_0jLArNDyOOT16AmCfXV5zg/https://help.runwayml.com/hc/article_attachments/30858615646611) |
| 涂鸦      | ![](https://proxy-prod.omnivore-image-cache.app/540x304,stqPxPrT6DGAN2F_C6y4ZMDaZogBPqAXWDSkf42YEgG4/https://help.runwayml.com/hc/article_attachments/30858615646995) |
| 氖       | ![](https://proxy-prod.omnivore-image-cache.app/540x304,sAdYOYTo2-XXEdKArdhhG67m7QlwW76wiY_cGt8oX1x8/https://help.runwayml.com/hc/article_attachments/30858615647251) |
| 校队      | ![](https://proxy-prod.omnivore-image-cache.app/426x256,s0WmsWfTf7UssyiRI4h5LZD2mr3m9zw_rrdgp_rW3k3w/https://help.runwayml.com/hc/article_attachments/30858635857555) |
| 刺绣      | ![](https://proxy-prod.omnivore-image-cache.app/540x304,sw6CErPHh9CRfelF5T6gQB1YXSDrMpf3RyHkLliVUoEE/https://help.runwayml.com/hc/article_attachments/30858639067027) |

## 括号占位符

为了创建易于重复使用的自定义预设，您还可以将提示的一部分放在括号中，以便一键替换文本。例如：

摄像机无缝飞过[拍摄对象位置]

当保存为预设时，您可以一键替换括号区域并在重复使用它时开始输入文本。 
