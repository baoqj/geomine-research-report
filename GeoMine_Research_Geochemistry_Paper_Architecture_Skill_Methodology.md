# GeoMine Research 地球化学学术论文架构设计 Skill 方法论文档

**文档用途**：用于将地球化学专业论文写作方法论封装为 Codex / GeoMine Research 插件中的论文架构设计 Skill。该 Skill 的目标不是简单生成调研报告或综述文章，而是帮助研究者根据具体课题类型，自动选择合适的学术论文架构、数据方法、图表体系、论证路径和写作规范，生成接近博士/博士后水平的地球化学论文草稿、研究计划、方法章节或完整论文框架。

**适用对象**：

- GeoMine Research 插件开发者；
- 地球化学、矿床学、环境地球化学、核废料处置、地下水地球化学、反应运移模拟方向研究者；
- 使用 Codex / AI Agent / Skill 进行地学论文写作、数据分析和科研报告生成的团队；
- OpenMine.VIP、GeoMine、MiningReg 等矿业与地球科学 AI 系统。

---

## 1. Skill 的定位

### 1.1 Skill 名称建议

建议 Skill 名称：

```text
academic-geochemistry-paper-architect
```

或：

```text
geomine-paper-architecture
```

也可以作为 GeoMine Research 插件中的子 Skill：

```text
GeoMine Research / Skills / Academic Paper Architect
```

### 1.2 Skill 的核心目标

该 Skill 的核心目标是：

> 将地球化学专业论文写作从“资料汇总型输出”提升为“问题驱动、数据约束、方法透明、机制解释、图表论证、结论有边界”的学术论文生成流程。

它应帮助 Codex 在写作前先判断：

1. 课题属于哪一类地球化学论文；
2. 该类论文通常需要哪些章节；
3. 需要哪些数据；
4. 需要哪些图表；
5. 需要哪些地球化学指标或模型；
6. 如何建立假设；
7. 如何从数据推导机制；
8. 如何讨论替代解释和不确定性；
9. 如何把结论控制在合理边界内；
10. 如何输出符合期刊规范的论文结构。

---

## 2. 地球化学论文写作的核心理念

### 2.1 论文不是报告

地球化学论文不是简单的：

- 文献整理；
- 数据罗列；
- 图表展示；
- 区域背景描述；
- 泛泛而谈的研究意义。

博士/博士后水平的地球化学论文必须回答一个明确的科学问题。

一个合格的地球化学论文应当具备以下逻辑：

```text
科学问题 → 可检验假设 → 数据设计 → 方法选择 → 结果呈现 → 机制解释 → 替代解释排除 → 不确定性评估 → 学术意义或工程意义
```

### 2.2 论文的中心不是“我有什么数据”，而是“我要回答什么问题”

错误思路：

```text
我收集了很多地球化学数据，所以我要写一篇论文。
```

正确思路：

```text
某个地球过程尚未被充分解释，因此我需要收集和处理特定类型的地球化学数据，用来检验某些假设。
```

例如：

```text
问题：Athabasca Basin 周缘地下水中 U 的迁移是受原岩丰度控制，还是受氧化性地下水和碳酸络合控制？

假设：如果 U 迁移主要受碳酸络合控制，则地下水 U 浓度应与 HCO3-、Eh、pH 和 U(VI)-carbonate complexes 形态存在一致关系，并且 PHREEQC 计算应显示 U(VI)-carbonate 络合物占主导。
```

---

## 3. Skill 工作流总览

该 Skill 在 GeoMine Research 中应采用以下工作流。

```text
Input research topic
        ↓
Topic classification
        ↓
Paper type selection
        ↓
Research question extraction
        ↓
Hypothesis generation
        ↓
Data requirement planning
        ↓
Method and model selection
        ↓
Figure and table architecture
        ↓
Paper outline generation
        ↓
Section-level writing guide
        ↓
Citation and reference requirements
        ↓
Uncertainty, limitation and boundary control
        ↓
Final academic paper scaffold
```

---

## 4. 地球化学论文的典型类型

GeoMine Research 插件必须能够判断研究课题属于哪一种论文类型。不同类型的论文有不同的基础架构、数据需求、图表体系和论证方法。

下面列出常见且重要的地球化学论文类型。

---

### 4.1 Data Paper / Database Paper：地球化学数据库论文

#### 定义

以数据汇编、数据结构、数据质量控制、数据公开和可复用性为核心贡献的论文。

#### 典型问题

- 如何构建一个区域或全球尺度的岩石地球化学数据库？
- 如何整合主量元素、微量元素、同位素、年龄和空间信息？
- 如何清洗、标准化和公开数据？
- 该数据库可支持哪些地球科学问题？

#### 典型章节

1. Abstract
2. Introduction
3. Existing databases / initiatives
4. Data sources
5. Database structure
6. Data processing and quality control
7. Data statistics
8. Computed properties
9. Data availability
10. Limitations and future improvements
11. Conclusions

#### 核心数据

- 样品编号；
- 坐标；
- 岩性；
- 主量元素；
- 微量元素；
- 同位素；
- 年龄；
- 数据来源；
- 分析方法；
- 质量标记；
- 计算指标。

#### 典型图表

- 数据库关系结构图；
- 样品空间分布图；
- 年龄分布图；
- 元素分析数量直方图；
- 岩性分类饼图；
- 数据来源统计表；
- 字段说明表；
- QA/QC 流程图。

#### 适合 GeoMine 的场景

- 建立 Saskatchewan 铀矿区地球化学数据库；
- 整合加拿大各省矿产地球化学数据；
- 建立矿业法规与地球化学数据联合数据库；
- 建立地下水核素迁移样品数据库；
- 建立全岩地球化学 + GIS + 矿权信息数据库。

---

### 4.2 Regional Geochemical Characterization Paper：区域地球化学特征论文

#### 定义

描述并解释某一区域岩石、土壤、沉积物或地下水的地球化学组成、空间分布和地质控制因素。

#### 典型问题

- 某区域岩石或土壤的元素背景值是多少？
- 元素异常与岩性、构造、成矿带之间有什么关系？
- 区域地球化学分区是否反映不同地质单元？
- 某些元素组合是否可作为找矿指标？

#### 典型章节

1. Introduction
2. Geological setting
3. Sampling and analytical methods
4. Data quality control
5. Major and trace element geochemistry
6. Spatial geochemical patterns
7. Geochemical associations and anomaly interpretation
8. Geological controls
9. Implications for exploration or environmental assessment
10. Conclusions

#### 核心数据

- 岩石/土壤/沉积物样品；
- 主量元素；
- 微量元素；
- 稀土元素；
- GIS 坐标；
- 岩性与地层单元；
- 构造线、断裂、岩体边界；
- 矿点或矿床位置。

#### 典型图表

- 样点分布图；
- 元素空间异常图；
- 元素相关矩阵；
- PCA 图；
- cluster dendrogram；
- boxplot by lithology；
- spider diagram；
- REE 配分图；
- 异常阈值统计表。

---

### 4.3 Mineral Exploration Geochemistry Paper：矿产勘查地球化学论文

#### 定义

以找矿预测、异常识别、矿化机制或矿床靶区评价为目标的地球化学论文。

#### 典型问题

- 哪些元素组合最能指示矿化？
- 地球化学异常是否与已知矿床一致？
- 新的潜在靶区在哪里？
- 元素异常是成矿作用导致，还是岩性背景或风化作用造成？
- 多源数据能否提高找矿预测能力？

#### 典型章节

1. Introduction
2. Regional geology and metallogenic setting
3. Deposit model
4. Sampling and analytical methods
5. Geochemical data processing
6. Anomaly detection
7. Multivariate analysis
8. Spatial prediction and target ranking
9. Discussion: ore-forming processes and exploration implications
10. Conclusions

#### 核心方法

- 背景值与异常阈值计算；
- robust statistics；
- percentile threshold；
- fractal / concentration-area model；
- PCA / factor analysis；
- random forest / XGBoost；
- weights-of-evidence；
- GIS overlay；
- prospectivity mapping。

#### 典型图表

- 成矿地质图；
- 多元素异常图；
- 元素组合热图；
- 靶区评分图；
- ROC curve；
- feature importance；
- 矿化模型示意图。

#### GeoMine 场景

- Saskatchewan 铀矿靶区筛选；
- Ontario 金矿勘查地球化学异常识别；
- 稀土、锂、镍、铜、钾盐等关键矿产靶区评价；
- 地球化学 + 地球物理 + 矿权数据综合选地。

---

### 4.4 Petrogenesis Paper：岩石成因论文

#### 定义

通过全岩地球化学、矿物化学、同位素和年龄学解释岩石来源、岩浆演化、部分熔融、分离结晶、地壳混染或构造背景的论文。

#### 典型问题

- 岩浆来自地幔、地壳，还是混合源区？
- 岩浆经历了哪些分异或混染过程？
- 岩石形成于俯冲带、裂谷、板内或造山环境？
- 岩石与区域构造演化或成矿作用有什么关系？

#### 典型章节

1. Introduction
2. Geological background
3. Petrography
4. Analytical methods
5. Geochronology
6. Major and trace elements
7. Isotope geochemistry
8. Petrogenesis
9. Tectonic implications
10. Conclusions

#### 核心数据

- 岩相学；
- 主量元素；
- 微量元素；
- REE；
- Sr-Nd-Hf-Pb 同位素；
- U-Pb 年龄；
- 矿物化学。

#### 典型图表

- TAS diagram；
- Harker diagrams；
- chondrite-normalized REE diagram；
- primitive mantle-normalized spider diagram；
- Sr-Nd isotope plots；
- εHf(t) vs age；
- tectonic discrimination diagrams；
- petrogenetic model cartoon。

---

### 4.5 Isotope Geochemistry Paper：同位素地球化学论文

#### 定义

以同位素系统为核心证据，解释源区、年龄、流体来源、迁移路径、成矿过程或地球演化过程的论文。

#### 典型问题

- Sr-Nd-Hf-Pb 同位素揭示了什么源区？
- U-Pb 年龄约束了什么地质事件？
- C-O-S 同位素显示流体来自岩浆、变质、沉积还是大气水？
- U 系、Ra 系或 Pb 同位素能否约束放射性核素迁移？

#### 典型章节

1. Introduction
2. Geological setting
3. Samples and analytical methods
4. Isotope results
5. Age interpretation or source tracing
6. Mixing models
7. Geological implications
8. Conclusions

#### 典型图表

- Concordia diagram；
- weighted mean age plot；
- εNd(t) vs age；
- εHf(t) vs age；
- Pb isotope diagrams；
- δ13C vs δ18O；
- sulfur isotope histogram；
- isotope mixing model。

---

### 4.6 Hydrogeochemistry Paper：地下水地球化学论文

#### 定义

研究地下水化学组成、水-岩反应、氧化还原、污染迁移、矿物饱和状态和水化学演化路径的论文。

#### 典型问题

- 地下水化学类型是什么？
- 水-岩反应如何控制离子组成？
- U、As、Ra、Pb 等污染物如何迁移？
- pH、Eh、HCO3-、SO4 2-、Cl-、Fe/Mn 如何影响元素形态？
- 地下水是否达到某些矿物饱和状态？

#### 典型章节

1. Introduction
2. Hydrogeological setting
3. Sampling and analytical methods
4. Water chemistry classification
5. Speciation and saturation modelling
6. Redox and mineral controls
7. Contaminant mobility
8. Conceptual hydrogeochemical model
9. Environmental implications
10. Conclusions

#### 核心方法

- Piper diagram；
- Gibbs diagram；
- Stiff diagram；
- ion balance error；
- PHREEQC speciation；
- saturation index；
- Eh-pH diagrams；
- inverse modelling；
- reaction path modelling。

#### GeoMine 场景

- 铀矿区地下水中 U、Ra、As 迁移；
- 核废料处置场地地下水长期演化；
- 尾矿库渗滤液污染；
- 酸性矿山排水；
- 冰川、冻土或深部裂隙水化学。

---

### 4.7 Environmental Geochemistry Paper：环境地球化学论文

#### 定义

研究元素污染、重金属迁移、生态风险、沉积物或土壤污染来源识别的论文。

#### 典型问题

- 土壤或沉积物中重金属是否超标？
- 污染来源是自然背景、矿业活动、工业排放还是交通源？
- 污染物是否具有生物可利用性？
- 风险等级如何？

#### 核心方法

- enrichment factor；
- geoaccumulation index；
- pollution load index；
- potential ecological risk index；
- positive matrix factorization；
- sequential extraction；
- spatial interpolation；
- human health risk assessment。

#### 典型图表

- 污染元素空间分布图；
- 风险指数图；
- 源解析图；
- boxplot；
- PCA biplot；
- 风险分级表。

---

### 4.8 Reactive Transport Modelling Paper：反应运移模拟论文

#### 定义

使用 PHREEQC、PFLOTRAN、OpenGeoSys、COMSOL 或自建模型，研究水-岩反应、溶质迁移、矿物沉淀/溶解和长期演化过程。

#### 典型问题

- 地下水中 U、Ra、As 或其他元素如何随时间迁移？
- 哪些矿物反应控制污染物释放或固定？
- 氧化还原前沿如何推进？
- 多孔介质中扩散、对流、反应如何耦合？
- 长周期核素迁移是否会影响地下水安全？

#### 典型章节

1. Introduction
2. Geological and hydrogeological setting
3. Conceptual model
4. Governing equations
5. Geochemical reaction network
6. Numerical implementation
7. Boundary and initial conditions
8. Model calibration and validation
9. Results
10. Sensitivity analysis
11. Implications and limitations
12. Conclusions

#### 核心内容

- 控制方程；
- 反应网络；
- 边界条件；
- 初始条件；
- 物种数据库；
- 矿物相；
- 孔隙率、渗透率、扩散系数；
- 温度、pH、Eh；
- 敏感性分析。

#### 典型图表

- 概念模型图；
- 网格图；
- 浓度剖面图；
- breakthrough curve；
- 饱和指数随时间变化；
- pH/Eh 演化图；
- 敏感性 tornado plot。

---

### 4.9 Experimental Geochemistry Paper：实验地球化学论文

#### 定义

通过实验室控制条件研究矿物反应、元素分配、吸附/解吸、溶解/沉淀、同位素分馏或辐解反应的论文。

#### 典型问题

- 某矿物在特定 pH/Eh 条件下如何吸附 U 或 As？
- 温度、压力、盐度如何影响元素分配？
- 多孔介质中的水辐解 G 值如何随孔径、电场、材料表面变化？
- 氧化物或金属表面如何改变自由基产额？

#### 典型章节

1. Introduction
2. Experimental design
3. Materials
4. Analytical methods
5. Results
6. Kinetic or thermodynamic modelling
7. Mechanistic interpretation
8. Comparison with natural systems
9. Conclusions

#### 典型图表

- 实验装置图；
- 变量设计表；
- 反应时间曲线；
- kinetic fitting；
- adsorption isotherm；
- speciation diagram；
- uncertainty plot。

---

### 4.10 Radiolysis / Nuclear Geochemistry Paper：辐射化学与核地球化学论文

#### 定义

研究电离辐射作用下水、矿物、孔隙介质、地下水或核素体系中的化学反应、自由基生成、氧化还原演化和核素迁移。

#### 典型问题

- 多孔介质如何改变水辐解 G 值？
- e_aq^-、•OH、H2、H2O2 如何随孔径、材料和电场变化？
- 辐解是否改变地下水 Eh？
- 放射性核素迁移是否受辐解产物控制？
- 金属表面是否捕获电子并改变自由基产额？

#### 典型章节

1. Introduction
2. Background on water radiolysis
3. Porous media and surface effects
4. Reaction network
5. Governing equations
6. Experimental or modelling methods
7. G-value results
8. Mechanistic interpretation
9. Implications for nuclear waste disposal or geochemical evolution
10. Limitations
11. Conclusions

#### 核心图表

- 辐解反应网络图；
- G-value comparison table；
- 本体水 vs 多孔介质对照表；
- 孔径影响图；
- 电场影响图；
- surface band alignment schematic；
- Eh-pH evolution diagram；
- reaction pathway diagram。

---

### 4.11 Geochemical Modelling and Machine Learning Paper：地球化学建模与机器学习论文

#### 定义

使用统计模型、机器学习或 AI 方法从地球化学数据中识别模式、预测岩性、预测成矿靶区或重建地质过程。

#### 典型问题

- 能否用全岩地球化学预测岩性或原岩？
- 能否从多元素组合中识别成矿异常？
- 能否用机器学习进行矿产远景预测？
- AI 模型是否能辅助地球化学数据清洗和解释？

#### 典型章节

1. Introduction
2. Data sources
3. Feature engineering
4. Model architecture
5. Training and validation
6. Results
7. Geological interpretation
8. Model explainability
9. Limitations and transferability
10. Conclusions

#### 核心方法

- random forest；
- gradient boosting；
- SVM；
- neural networks；
- Bayesian classifier；
- clustering；
- PCA / UMAP / t-SNE；
- SHAP values；
- spatial cross-validation。

---

### 4.12 Review / Perspective Paper：综述或观点论文

#### 定义

系统梳理某一领域研究进展、方法争议、知识空白和未来方向的论文。

#### 典型问题

- 某类矿床地球化学指标研究进展如何？
- 放射性核素迁移模型有哪些局限？
- 多孔介质水辐解研究未来方向是什么？
- AI 如何改变矿业地球化学研究？

#### 典型章节

1. Introduction
2. Scope and literature selection
3. Thematic review sections
4. Methodological comparison
5. Knowledge gaps
6. Future research directions
7. Conclusions

#### 注意

综述论文不能只是文献摘要。必须有：

- 分类框架；
- 争议梳理；
- 方法评价；
- 未来问题；
- 作者自己的判断。

---

### 4.13 Technical Note / Methods Paper：方法论文

#### 定义

提出一种新的数据处理方法、计算流程、模型耦合方法、数据库结构或软件工具。

#### 典型问题

- 如何自动清洗地球化学数据？
- 如何将 PHREEQC 与 GIS 或 RAG 系统集成？
- 如何构建可复现的地球化学分析 Notebook？
- 如何设计地球化学数据 QA/QC pipeline？

#### 典型章节

1. Introduction
2. Method design
3. Implementation
4. Validation dataset
5. Case study
6. Performance and limitations
7. Code and data availability
8. Conclusions

---

## 5. 论文类型自动判断规则

GeoMine Research 插件可根据用户课题关键词自动判断论文类型。

### 5.1 规则示例

```yaml
if topic contains [database, compilation, dataset, global, csv, SQL, data structure]:
  paper_type: Data Paper

if topic contains [uranium, groundwater, PHREEQC, speciation, saturation index, pH, Eh]:
  paper_type: Hydrogeochemistry / Reactive Transport Modelling

if topic contains [mineral exploration, anomaly, target, prospectivity, claim, GIS, geophysics]:
  paper_type: Mineral Exploration Geochemistry

if topic contains [zircon, Hf, Nd, Sr, Pb, crustal growth, lithosphere, Archean]:
  paper_type: Isotope Geochemistry / Crustal Evolution Paper

if topic contains [radiolysis, G-value, porous media, radicals, e_aq, H2, H2O2]:
  paper_type: Radiolysis / Nuclear Geochemistry Paper

if topic contains [machine learning, prediction, classifier, random forest, AI]:
  paper_type: Geochemical Modelling and Machine Learning Paper

if topic contains [review, progress, future directions, literature]:
  paper_type: Review / Perspective Paper
```

### 5.2 混合类型判断

许多高水平论文不是单一类型，而是混合类型。

例如：

```text
题目：Using PHREEQC and whole-rock geochemistry to evaluate uranium mobility in fractured crystalline basement groundwater.
```

可判定为：

```text
Primary type: Hydrogeochemistry Paper
Secondary type: Reactive Transport Modelling Paper
Tertiary type: Environmental / Nuclear Geochemistry Paper
```

论文架构应组合三类结构：

- 地下水化学结果；
- PHREEQC 形态与饱和指数模拟；
- 核素迁移与长期安全讨论。

---

## 6. 标准地球化学论文架构模板

以下为通用模板。Skill 应根据论文类型自动调整各章节。

```markdown
# Title

## Abstract
- Background
- Knowledge gap
- Data and methods
- Key results
- Interpretation
- Broader implications

## Keywords

## 1. Introduction
### 1.1 Scientific background
### 1.2 Previous work
### 1.3 Knowledge gap
### 1.4 Research questions
### 1.5 Hypotheses and objectives

## 2. Geological / Hydrogeological / Geochemical Setting
### 2.1 Regional geology
### 2.2 Stratigraphy and lithology
### 2.3 Structural framework
### 2.4 Mineralization or environmental context
### 2.5 Previous geochemical studies

## 3. Materials and Methods
### 3.1 Sampling strategy or data sources
### 3.2 Analytical methods
### 3.3 Database structure
### 3.4 Data cleaning and quality control
### 3.5 Normalization and derived indices
### 3.6 Statistical methods
### 3.7 Geochemical modelling methods
### 3.8 Uncertainty treatment

## 4. Results
### 4.1 Sample distribution and metadata
### 4.2 Major element geochemistry
### 4.3 Trace element geochemistry
### 4.4 Rare earth element patterns
### 4.5 Isotope results
### 4.6 Spatial patterns
### 4.7 Temporal patterns
### 4.8 Modelling results

## 5. Discussion
### 5.1 Data reliability and representativeness
### 5.2 Source characteristics
### 5.3 Alteration and mobility
### 5.4 Redox and fluid controls
### 5.5 Mineral reaction mechanisms
### 5.6 Tectonic / metallogenic / environmental implications
### 5.7 Alternative explanations
### 5.8 Sensitivity and uncertainty
### 5.9 Conceptual model

## 6. Implications
### 6.1 Scientific implications
### 6.2 Exploration implications
### 6.3 Environmental or nuclear waste implications
### 6.4 Methodological implications

## 7. Limitations

## 8. Conclusions

## Data and Code Availability

## Author Contributions

## Competing Interests

## Acknowledgements

## References

## Supplementary Materials
```

---

## 7. 各章节写作要求

### 7.1 Abstract

摘要必须具备完整逻辑链。

推荐结构：

```text
[背景] X is important because ...
[问题] However, Y remains poorly constrained because ...
[方法] Here we use ... to test ...
[结果] We find that ...
[解释] These results indicate ...
[意义] This implies ...
```

不要写成：

```text
本文介绍了某区域地质背景，分析了元素特征，并提出了一些建议。
```

这种摘要太弱。

---

### 7.2 Introduction

Introduction 的任务是建立问题张力。

必须包括：

1. 为什么这个问题重要；
2. 前人做了什么；
3. 前人方法有什么限制；
4. 本文提出什么新数据、新方法或新解释；
5. 本文要检验什么假设。

推荐句式：

```text
Although previous studies have shown ..., the extent to which ... remains uncertain.
This uncertainty arises because ...
Here, we address this gap by ...
We test the hypothesis that ...
```

---

### 7.3 Geological Setting

必须服务于后文解释，不能写成百科式背景。

应包括：

- 区域构造位置；
- 主要地层和岩性；
- 岩浆或变质事件；
- 断裂和流体通道；
- 成矿或污染背景；
- 已有地球化学研究。

写作原则：

```text
只写与研究问题相关的地质背景。
```

---

### 7.4 Materials and Methods

这是论文可信度的核心。

必须说明：

- 样品从哪里来；
- 采样标准是什么；
- 分析方法是什么；
- 仪器和检测限是什么；
- 数据如何清洗；
- 异常值如何处理；
- 缺失值如何处理；
- 是否归一化；
- 是否进行岩性分类；
- 使用什么软件；
- 使用什么版本；
- 使用什么数据库；
- 如何处理不确定性。

---

### 7.5 Results

Results 只报告观察结果，不应过早解释。

错误写法：

```text
U 含量升高，说明氧化性地下水促进了铀迁移。
```

更规范写法：

```text
U concentrations range from X to Y, with the highest values observed in samples collected along the fracture zone. U shows a positive correlation with HCO3- and Eh, whereas no clear relationship is observed with total dissolved Fe.
```

解释应放到 Discussion。

---

### 7.6 Discussion

Discussion 是论文价值最高的部分。

必须完成：

1. 解释结果；
2. 对比前人；
3. 讨论机制；
4. 排除替代解释；
5. 说明边界条件；
6. 提出概念模型。

推荐结构：

```text
Observation → Mechanism → Evidence → Alternative explanation → Boundary condition → Implication
```

---

### 7.7 Conclusions

结论应为 4–6 条，每条对应一个主要发现。

结论中不要引入新数据，不要夸大意义。

推荐格式：

```text
1. The compiled dataset shows that ...
2. Major and trace element patterns indicate ...
3. PHREEQC modelling suggests that ...
4. These results imply that ...
5. The interpretation is limited by ...
```

---

## 8. 数据获取与处理方法论

### 8.1 数据获取

GeoMine Research 应支持从以下来源读取数据：

- 公开论文 supplementary data；
- EarthChem；
- GEOROC；
- PetDB；
- provincial geological surveys；
- Canadian provincial geoatlas；
- USGS / GSC 数据；
- 钻孔报告；
- assessment reports；
- 地下水监测报告；
- PHREEQC 输入输出；
- GIS shapefile / GeoJSON；
- PostGIS / R2 / D1 / CSV / Excel。

### 8.2 数据标准化

必须统一：

- 样品编号；
- 坐标系统；
- 单位；
- 元素名称；
- 氧化物写法；
- 岩石名称；
- 年龄单位；
- 分析方法；
- 引文信息。

### 8.3 QA/QC

必须检查：

- 主量元素总量；
- LOI；
- 检出限；
- 重复样；
- 标准样；
- 空白样；
- 坐标缺失；
- 年龄缺失；
- 岩性不明；
- 单位错误；
- 异常极值。

### 8.4 数据变换

常见处理：

- LOI-free normalization；
- trace element normalization；
- chondrite normalization；
- primitive mantle normalization；
- log transformation；
- centered log-ratio transformation；
- age binning；
- spatial join；
- feature engineering。

---

## 9. 地球化学常用指标和模型

### 9.1 岩石分类与成因指标

- TAS diagram；
- QAPF；
- A/CNK；
- A/NK；
- ASI；
- MALI；
- Fe-number；
- Mg-number；
- CIA；
- WIP；
- Eu/Eu*；
- Ce/Ce*；
- La/Yb；
- Th/U；
- Sr/Y；
- Nb/Ta；
- Zr/Hf。

### 9.2 水化学指标

- charge balance error；
- Piper classification；
- Gibbs diagram；
- saturation index；
- speciation fraction；
- alkalinity；
- carbonate complexation；
- redox couple comparison；
- Eh-pH stability field。

### 9.3 成矿异常指标

- enrichment factor；
- anomaly threshold；
- robust z-score；
- concentration-area fractal model；
- PCA factor loading；
- weights-of-evidence；
- prospectivity score。

### 9.4 辐射化学指标

- G(e_aq^-)
- G(•OH)
- G(H2)
- G(H2O2)
- dose rate；
- LET；
- radical lifetime；
- recombination probability；
- Onsager radius；
- interface electric field；
- electron-hole separation efficiency。

---

## 10. 图表设计规范

GeoMine Research Skill 应在生成论文架构时自动建议图表。

### 10.1 通用图表

- Study area map；
- Geological map；
- Sampling map；
- Data workflow diagram；
- QA/QC flowchart；
- Histogram；
- Boxplot；
- Correlation matrix；
- PCA biplot；
- Spatial heatmap；
- Conceptual model。

### 10.2 岩石地球化学图表

- TAS diagram；
- Harker diagrams；
- REE patterns；
- spider diagrams；
- tectonic discrimination diagrams；
- isotope evolution diagrams；
- age histogram；
- density plot。

### 10.3 地下水地球化学图表

- Piper diagram；
- Stiff diagram；
- Gibbs diagram；
- Eh-pH diagram；
- saturation index plot；
- speciation plot；
- reaction path diagram；
- breakthrough curve。

### 10.4 成矿预测图表

- anomaly map；
- target ranking map；
- multi-layer GIS overlay；
- feature importance；
- ROC / AUC curve；
- prospectivity score table。

### 10.5 辐解与核地球化学图表

- radiolysis reaction network；
- G-value comparison；
- pore-size effect plot；
- dose-rate effect plot；
- electric-field effect plot；
- surface band alignment；
- bulk water vs porous water comparison table。

---

## 11. 引文和参考文献规范

### 11.1 正文引用原则

每个关键判断必须有来源。

必须引用：

- 数据库；
- 分析方法；
- 分类图；
- 公式；
- 前人模型；
- 区域地质资料；
- 软件和代码；
- PHREEQC 数据库；
- 标准化常数；
- 实验参数来源。

### 11.2 推荐格式

根据期刊选择：

- Elsevier / GCA：作者-年份；
- Nature / Science：编号制；
- ACS：编号制或 ACS 格式；
- Earth System Science Data：作者-年份；
- Geochemical Perspectives Letters：作者-年份。

### 11.3 引文密度

高水平论文中，Introduction 和 Methods 的引用密度应较高。Discussion 中每一个与前人对比的判断也应有引用。

---

## 12. 不确定性与局限性

Skill 必须强制生成 Limitations 或 Uncertainty 小节。

常见不确定性包括：

- 空间采样偏差；
- 年龄不确定性；
- 分析误差；
- 数据库来源不一致；
- 岩性分类错误；
- 风化和蚀变影响；
- 检出限影响；
- 重复样合并误差；
- 模型参数不确定；
- PHREEQC 热力学数据库限制；
- 缺少验证样品；
- 机器学习模型过拟合；
- 相关性不等于因果性。

---

## 13. 学术克制原则

GeoMine Research 生成论文时必须避免以下错误。

### 13.1 避免过度外推

错误：

```text
本区域 U 异常证明整个盆地都具有高铀矿化潜力。
```

正确：

```text
The observed U anomaly indicates local enrichment under the sampled geological and hydrogeochemical conditions. Broader extrapolation requires additional spatial coverage and independent geophysical or drilling constraints.
```

### 13.2 避免把相关性写成因果性

错误：

```text
U 与 HCO3- 相关，所以 HCO3- 导致 U 迁移。
```

正确：

```text
The positive correlation between U and HCO3-, together with speciation modelling showing dominant U(VI)-carbonate complexes, is consistent with carbonate-enhanced U mobility.
```

### 13.3 避免忽略替代解释

任何解释都应讨论可能的替代原因，例如：

- 岩性背景；
- 风化；
- 热液改造；
- 采样偏差；
- 分析误差；
- 后期变质；
- 水文混合。

---

## 14. Skill 输入与输出设计

### 14.1 推荐输入

```yaml
research_topic: string
region: string
paper_goal: string
available_data:
  - whole-rock geochemistry
  - groundwater chemistry
  - isotope data
  - GIS layers
  - PHREEQC outputs
  - mineral occurrence data
  - literature corpus
preferred_journal_style: Elsevier | Nature | ACS | ESSD | GPL | custom
output_language: English | Chinese | bilingual
paper_stage: outline | proposal | draft | revision | final
```

### 14.2 推荐输出

```yaml
paper_type:
  primary: string
  secondary: string
research_questions: list
hypotheses: list
required_data: list
methods: list
figures: list
tables: list
paper_outline: markdown
section_writing_guidance: markdown
citation_requirements: list
uncertainty_checks: list
quality_checklist: list
```

---

## 15. Codex Skill Prompt 模板

下面是可直接交给 Codex 的 Skill 开发 Prompt。

```text
You are developing a GeoMine Research plugin skill named academic-geochemistry-paper-architect.

Goal:
Build a reusable skill that helps researchers design, structure, and draft professional geochemistry research papers. The skill must not generate a generic report. It must identify the paper type, define research questions and hypotheses, plan data requirements, select methods, design figures and tables, and generate a rigorous academic paper architecture.

Core requirements:
1. Classify the research topic into one or more geochemistry paper types:
   - Data Paper / Database Paper
   - Regional Geochemical Characterization Paper
   - Mineral Exploration Geochemistry Paper
   - Petrogenesis Paper
   - Isotope Geochemistry Paper
   - Hydrogeochemistry Paper
   - Environmental Geochemistry Paper
   - Reactive Transport Modelling Paper
   - Experimental Geochemistry Paper
   - Radiolysis / Nuclear Geochemistry Paper
   - Geochemical Modelling and Machine Learning Paper
   - Review / Perspective Paper
   - Technical Note / Methods Paper

2. For each paper type, provide a suitable academic structure, required data, methods, figures, tables, and discussion logic.

3. The skill must follow a research logic:
   Scientific problem → knowledge gap → testable hypotheses → data design → methods → results → mechanism → alternative explanations → uncertainty → implications.

4. The skill must enforce academic writing standards:
   - formal title
   - abstract
   - keywords
   - introduction
   - geological or hydrogeological setting
   - materials and methods
   - results
   - discussion
   - implications
   - limitations
   - conclusions
   - data availability
   - references
   - supplementary materials

5. The skill must require reproducibility:
   - data sources
   - database version
   - sample metadata
   - QA/QC rules
   - normalization methods
   - software and version
   - modelling database
   - code availability

6. The skill must design geochemistry-specific figures:
   - study area map
   - sampling map
   - geological map
   - database structure diagram
   - TAS diagram
   - Harker diagrams
   - REE patterns
   - spider diagrams
   - isotope plots
   - Piper diagram
   - Eh-pH diagram
   - PHREEQC saturation/speciation plots
   - anomaly maps
   - prospectivity maps
   - conceptual model diagrams

7. The skill must enforce uncertainty and limitation analysis:
   - sampling bias
   - analytical uncertainty
   - age uncertainty
   - lithological bias
   - alteration effects
   - detection limits
   - model parameter uncertainty
   - thermodynamic database limitation
   - spatial extrapolation limitation
   - correlation vs causation

8. The skill must support citation style selection:
   - Elsevier author-year
   - Nature numbered
   - ACS
   - Earth System Science Data
   - Geochemical Perspectives Letters

9. The skill must output:
   - detected paper type
   - research questions
   - hypotheses
   - required data checklist
   - method checklist
   - figure plan
   - table plan
   - detailed paper outline
   - section-level writing instructions
   - uncertainty checklist
   - academic quality checklist

Implementation expectations:
- Create a skill folder under the GeoMine Research plugin.
- Include a README.md explaining the skill purpose and usage.
- Include a prompt.md containing the main system prompt for the skill.
- Include schema definitions for input and output.
- Include examples for at least five paper types.
- Include a quality checklist template.
- Include a paper architecture generator function or command.
- Ensure the skill can be called by a research-router agent.
- Ensure the skill can hand off to other skills such as PHREEQC modelling, GIS analysis, geochemical anomaly ranking, literature review, and data visualization.

The final skill should help GeoMine Research produce academic paper structures suitable for geochemistry PhD or postdoctoral research, not generic business reports or superficial literature summaries.
```

---

## 16. Skill 与 GeoMine Research 其他组件的衔接

该 Skill 不应独立工作，而应作为论文架构中枢。

### 16.1 可调用的下游 Skill

```text
academic-geochemistry-paper-architect
    ├── literature-review-synthesizer
    ├── geochem-data-cleaning
    ├── whole-rock-geochemistry-analysis
    ├── groundwater-speciation-phreeqc
    ├── reactive-transport-modeling
    ├── gis-geochemical-mapping
    ├── mineral-prospectivity-ranking
    ├── isotope-geochemistry-interpretation
    ├── radiolysis-geochemistry-modeling
    ├── figure-generation
    └── reference-manager
```

### 16.2 上游 Router 的判断逻辑

Research Router 接收到用户问题后：

1. 判断是否为论文写作任务；
2. 提取研究对象、区域、数据类型、目标期刊；
3. 调用 academic-geochemistry-paper-architect；
4. 生成论文类型和架构；
5. 分派给相应数据分析或建模 Skill；
6. 汇总为论文草稿。

---

## 17. 质量检查清单

GeoMine Research 生成论文前必须通过以下检查。

### 17.1 科学问题检查

- 是否有明确研究问题？
- 是否有知识空白？
- 是否有可检验假设？
- 是否说明为什么该问题重要？

### 17.2 数据检查

- 是否列明数据来源？
- 是否说明样品数量？
- 是否说明分析方法？
- 是否说明 QA/QC？
- 是否处理缺失值和异常值？
- 是否记录坐标和年龄不确定性？

### 17.3 方法检查

- 是否说明公式来源？
- 是否定义所有变量和单位？
- 是否说明软件和版本？
- 是否说明模型参数？
- 是否说明热力学数据库或分类标准？

### 17.4 图表检查

- 是否每张图都服务于论证？
- 是否所有图都在正文引用？
- 是否坐标轴有单位？
- 是否图例清楚？
- 是否图题可独立理解？
- 是否地图有比例尺、投影和数据来源？

### 17.5 讨论检查

- 是否解释机制？
- 是否对比前人？
- 是否讨论替代解释？
- 是否说明边界条件？
- 是否讨论不确定性？

### 17.6 结论检查

- 是否只总结本文结果？
- 是否避免过度外推？
- 是否每条结论都有数据支撑？
- 是否提出合理后续研究方向？

---

## 18. 示例：输入课题与输出架构

### 示例 1：多孔介质水辐解

输入：

```text
研究多孔氧化物和粘土介质中水辐解 G 值变化，以及其对地下水氧化还原演化和核素迁移的影响。
```

输出判断：

```text
Primary type: Radiolysis / Nuclear Geochemistry Paper
Secondary type: Reactive Transport Modelling Paper
Tertiary type: Hydrogeochemistry Paper
```

建议论文架构：

1. Introduction
2. Water radiolysis and porous media background
3. Reaction network and G-value framework
4. Materials / modelling system
5. Governing equations
6. Boundary conditions
7. Results: G-value changes
8. Results: redox and species evolution
9. Discussion: pore confinement, surface effects, electric field
10. Implications for radionuclide migration
11. Limitations
12. Conclusions

---

### 示例 2：萨省铀矿找矿

输入：

```text
基于 Saskatchewan 公开地球化学、地球物理和矿权数据，识别 Athabasca Basin 周缘潜在铀矿靶区。
```

输出判断：

```text
Primary type: Mineral Exploration Geochemistry Paper
Secondary type: Regional Geochemical Characterization Paper
Tertiary type: Geochemical Modelling and Machine Learning Paper
```

建议图表：

- 研究区地质图；
- 铀矿点和断裂分布图；
- U-Th-K 异常图；
- 多元素 PCA 图；
- 地球物理异常叠加图；
- prospectivity ranking map；
- 靶区评分表。

---

### 示例 3：地下水铀迁移

输入：

```text
研究加拿大地盾裂隙地下水中铀的迁移机制，使用水化学数据和 PHREEQC 模拟。
```

输出判断：

```text
Primary type: Hydrogeochemistry Paper
Secondary type: Reactive Transport Modelling Paper
Tertiary type: Nuclear Geochemistry Paper
```

建议方法：

- charge balance check；
- Piper diagram；
- Eh-pH analysis；
- PHREEQC speciation；
- saturation index；
- U(VI)-carbonate complex analysis；
- inverse modelling；
- sensitivity analysis。

---

## 19. 最终原则

GeoMine Research 的论文架构 Skill 必须坚持以下原则：

1. 先判断论文类型，再生成论文结构；
2. 先定义科学问题，再组织数据；
3. 先建立假设，再选择方法；
4. 结果与讨论分离；
5. 每个机制解释都必须有证据链；
6. 每个关键判断都必须有引用；
7. 每个模型都必须有边界条件；
8. 每个结论都必须避免过度外推；
9. 数据和代码应尽可能可复现；
10. 输出必须符合学术论文，而不是咨询报告或商业报告。

---

## 20. 一句话总结

```text
academic-geochemistry-paper-architect Skill 的任务，是把 GeoMine Research 从“地学信息问答工具”提升为“能够按地球化学博士/博士后研究规范设计论文、组织证据链、选择方法、构建图表和控制结论边界的学术研究助手”。
```
