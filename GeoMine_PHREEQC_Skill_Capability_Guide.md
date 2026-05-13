# GeoMine Research 插件：PHREEQC Skill 能力说明文档

> 文档名称：GeoMine PHREEQC Skill Capability Guide  
> 适用插件：GeoMine Research / OpenMine.VIP Research Workflow  
> 插件版本：`geo-mining-research` v0.2.0  
> 核心模块：`phreeqc-modeling-skill`  
> 相关模块：`thmc-modeling/phreeqc-coupling-skill`、`geomine-paper-pdf-export-skill`  
> 生成日期：2026-05-13  
> 文档用途：总结当前 GeoMine Research 插件中 PHREEQC skill 的功能、架构、内置内容、运行边界和典型使用案例。

---

## 1. 总体定位

`phreeqc-modeling-skill` 是 GeoMine Research 插件中面向地下水地球化学建模的专用 skill。它的目标不是把 PHREEQC 当成一个“自动给结论”的黑盒，而是把科研问题、地下水化学数据、矿物学背景、反应假设和论文写作要求整理为一个可复现的 PHREEQC Modeling Package。

它支持的典型研究对象包括：

- 地下水主要离子、碳酸盐、硫酸盐和盐度控制；
- 铀、镭、氡、铅、钋等核素或 U 系列元素迁移；
- 铀矿区地下水、尾矿渗滤液、酸性矿山排水和水岩反应；
- 形态分布、矿物饱和指数、批反应、反应路径、吸附、离子交换、气相、逆向建模和一维反应运移；
- THMC 或 HC/THC/HMC 研究中需要 PHREEQC 承担化学反应模块的场景。

其核心输出是一个从“数据审计”到“PHREEQC 输入文件”再到“selected output、解释计划和论文方法段落”的完整研究链条。

---

## 2. 当前架构

当前 PHREEQC 能力由两个层级组成。

### 2.1 主 skill：`phreeqc-modeling-skill`

路径：

```text
plugins/Code/geo-mining-research/skills/phreeqc-modeling-skill/
```

职责：

- 判断用户问题适合哪类 PHREEQC 模型；
- 审计水化学、矿物、边界条件、红氧、吸附、动力学和 transport 数据；
- 推荐 PHREEQC 数据库；
- 规划 PHREEQC keyword；
- 生成 `.phr` 输入片段；
- 设计 `SELECTED_OUTPUT` 和 `USER_PUNCH`；
- 提供运行命令、manifest、输出解析和论文方法写作模板；
- 明确区分“实测数据、假设、占位符、数据库选择、计算结果和未验证解释”。

### 2.2 耦合 skill：`thmc-modeling/phreeqc-coupling-skill`

路径：

```text
plugins/Code/geo-mining-research/skills/thmc-modeling/phreeqc-coupling-skill/
```

职责：

- 在 THMC Modeling Package 中把水化学、矿物组合、红氧假设、吸附概念和反应网络转换为 PHREEQC-ready artifact；
- 若 `geomine_thmc` MCP 可用，则调用 `query_water_chemistry_samples`、`query_mineral_assemblages`、`build_phreeqc_input`，必要时调用 `run_phreeqc_job`；
- 若 MCP 不可用，则进入 Core Mode，本地生成未执行的 PHREEQC draft blocks；
- 明确标注 live、mock 或 local-only 模式，避免把 mock run 误写成真实计算结果。

### 2.3 与 GeoMine 插件总体关系

```text
GeoMine Research Router
  ↓
PHREEQC Modeling Skill
  ├─ 数据审计与 schema 校验
  ├─ 模型类型分类
  ├─ 数据库选择
  ├─ PHREEQC keyword 规划
  ├─ .phr 输入生成
  ├─ selected output 设计
  ├─ 本地 PHREEQC 运行清单
  ├─ selected output 解析
  ├─ 图表与论文解释
  └─ PDF/论文导出工作流

THMC Groundwater Router
  ↓
PHREEQC Coupling Skill
  ├─ 化学反应模块
  ├─ PhreeqcRM coupling plan
  ├─ transport solver 接口说明
  └─ THMC Modeling Package 汇总
```

---

## 3. 功能能力

### 3.1 模型类型识别

当前 skill 支持以下 PHREEQC 模型类型：

| 类型 | 用途 |
|---|---|
| `speciation` | 水溶液形态分布，例如 U(VI)-carbonate、Ra2+、SO4 络合 |
| `saturation_index` | 计算 calcite、barite、gypsum、uraninite 等矿物饱和指数 |
| `batch_reaction` | 模拟酸碱滴定、矿物加入、尾矿水混合和中和反应 |
| `equilibrium_phases` | 与指定矿物相达到平衡或测试溶解度控制 |
| `kinetic_reactions` | 使用 `RATES` / `KINETICS` 表达有文献支持的速率律 |
| `surface_complexation` | 吸附/表面络合，前提是有兼容的表面常数和位点密度 |
| `ion_exchange` | 阳离子交换或 Ra/Ba/Sr 竞争交换，前提是有 CEC 或位点容量 |
| `gas_phase` | CO2、O2、H2S、CH4、H2、Rn 等气相边界或平衡 |
| `one_dimensional_transport` | 一维对流、弥散、扩散和反应运移 |
| `inverse_modeling` | 根据初末端水和候选矿物相反演质量转移 |
| `PhreeqcRM_coupling_plan` | 设计 PHREEQC 与 transport/THMC solver 的耦合方案 |

设计原则是“用能回答问题的最小模型”。如果 speciation 与 saturation index 已能回答研究问题，不默认升级到 transport 或 THMC。

### 3.2 输入数据审计

skill 在生成 PHREEQC 输入之前会检查：

- 样品 ID、位置、深度、采样日期；
- pH、温度、pe/Eh、电导率、密度；
- alkalinity 的单位和基准，例如 `as CaCO3` 或 `as HCO3`；
- Ca、Mg、Na、K、Cl、SO4、HCO3/CO3 等主要离子；
- Fe、Mn、Al、U、Ra、Rn、Pb、Po、Ba、Sr 等目标元素；
- 检出限、QA/QC flag、charge balance；
- 矿物相、表面位点、交换容量、动力学常数、transport 边界条件；
- 哪些是实测数据，哪些是文献常数、模型假设或占位符。

缺失数据不会被自动编造，而是以显式占位符保留，例如：

```text
<pH_field_or_lab>
<temperature_C>
<alkalinity_value_and_basis>
<Eh_mV_or_pe>
<U_concentration_and_units>
<rate_constant_source>
```

### 3.3 数据库选择

当前 skill 内置数据库选择指南，强调数据库选择本身是科学假设。

| 数据库 | 建议用途 | 主要限制 |
|---|---|---|
| `phreeqc.dat` | 主要离子、碳酸盐体系、简单饱和指数 | 微量金属和核素覆盖有限 |
| `wateq4f.dat` | 天然水、WATEQ 风格形态分析、部分 trace elements | 需检查目标物种和矿物相 |
| `llnl.dat` | 覆盖较广，适合探索性 trace/radionuclide modeling | 数据库大，内部一致性需审计 |
| `minteq.dat` / `minteq.v4.dat` | 环境 trace metal、吸附和表面络合 | 表面模型和常数必须匹配 |
| `pitzer.dat` | 高盐水、蒸发浓缩和 Pitzer 活度模型 | 只适用于数据库支持的离子相互作用 |
| `sit.dat` | 盐水中的 SIT specific-ion-interaction 模型 | 覆盖可能不足 |

规则：不随意合并数据库。如果缺少物种、矿物或常数，应报告缺口并给出可审计的扩展路径。

### 3.4 PHREEQC keyword 规划

当前 skill 可以把研究问题映射到 PHREEQC keyword：

| 研究目标 | 常用 keyword |
|---|---|
| 形态分析 / 饱和指数 | `SOLUTION`、`SELECTED_OUTPUT`、可选 `USER_PUNCH` |
| 水岩反应 / 批反应 | `SOLUTION`、`REACTION`、`EQUILIBRIUM_PHASES` |
| 矿物平衡 | `EQUILIBRIUM_PHASES` |
| 动力学反应 | `RATES`、`KINETICS`、`INCREMENTAL_REACTIONS` |
| 表面络合 | `SURFACE`、必要时 `SURFACE_MASTER_SPECIES`、`SURFACE_SPECIES` |
| 离子交换 | `EXCHANGE`、必要时 `EXCHANGE_MASTER_SPECIES`、`EXCHANGE_SPECIES` |
| 气相 | `GAS_PHASE` |
| 一维运移 | `TRANSPORT`、`SOLUTION` zones、可叠加 `KINETICS` / `SURFACE` / `EXCHANGE` |
| 反演 | `INVERSE_MODELING` |
| PhreeqcRM | 数据库、cell chemistry、selected output mapping、state variables、coupling interval |

### 3.5 输入文件生成

skill 生成 `.phr` 时遵循以下规则：

- 每个可运行草稿包含 `TITLE`、`SOLUTION` 和 `END`；
- 所有模型都包含 `SELECTED_OUTPUT`，便于后续解析和绘图；
- 数据库选择放在 run manifest 和运行说明中，不写死在 `.phr` 内；
- 使用 PHREEQC 注释标记假设和占位符；
- `-charge` 只在明确需要并说明时使用；
- 红氧、alkalinity basis、矿物量、气相边界、吸附容量和 transport 边界条件必须显式说明。

### 3.6 selected output 与解析

默认 selected output 包括：

- pH、pe、temperature、alkalinity；
- ionic strength、charge balance、percent error、water；
- 主要离子和目标元素 totals；
- 目标矿物 saturation indices；
- 必要的 molalities 或 activities；
- 自定义 derived columns 可通过 `USER_PUNCH` 实现。

当前脚本还支持把 selected output 解析为 JSON 或 CSV，便于 Python 可视化、相关性分析、热图和论文表格生成。

### 3.7 运行清单与可复现性

skill 提供 `make_phreeqc_run_manifest.py`，记录：

- 研究目标；
- 模型类型；
- 输入文件、输出文件、selected output；
- 数据库路径；
- PHREEQC executable；
- 文件 checksum；
- run manifest JSON 路径。

本地运行命令格式：

```bash
phreeqc input.phr output.out database.dat
```

当前环境中已验证过的 macOS wrapper 路径为：

```bash
~/.local/bin/phreeqc input.phr output.out ~/.local/phreeqc/phreeqc-3.5.0-14000/database/phreeqc.dat
```

---

## 4. 内置文件内容

### 4.1 参考文档

| 文件 | 内容 |
|---|---|
| `references/groundwater-chemistry-data-schema.md` | 地下水化学表字段、必填项、推荐项和缺失值处理 |
| `references/phreeqc-database-selection.md` | 数据库选择规则和报告语言 |
| `references/phreeqc-keywords.md` | PHREEQC keyword 与研究问题映射 |
| `references/phreeqc-paper-methods-writing.md` | 论文方法、结果和 caveat 写作规则 |
| `references/uranium-radionuclide-reaction-patterns.md` | 铀、镭、氡和核素迁移建模模式 |
| `references/tailings-seepage-reaction-patterns.md` | 尾矿渗滤液、混合、缓冲和衰减模式 |
| `references/acid-mine-drainage-reaction-patterns.md` | AMD、硫化物氧化、金属迁移和中和模式 |

### 4.2 模板

| 模板 | 用途 |
|---|---|
| `templates/phreeqc-modeling-package-template.md` | 标准 PHREEQC Modeling Package 结构 |
| `templates/solution-template.phr` | `SOLUTION` 输入模板 |
| `templates/selected-output-template.phr` | `SELECTED_OUTPUT` 输出模板 |
| `templates/equilibrium-phases-template.phr` | 矿物平衡相模板 |
| `templates/kinetics-template.phr` | `RATES` / `KINETICS` 动力学模板 |
| `templates/surface-complexation-template.phr` | 表面络合模板 |
| `templates/exchange-template.phr` | 离子交换模板 |
| `templates/transport-1d-template.phr` | 一维运移模板 |
| `templates/paper-methods-template.md` | PHREEQC 论文方法段落模板 |

### 4.3 脚本

| 脚本 | 能力 |
|---|---|
| `scripts/validate_water_chemistry_table.py` | 审计 CSV/TSV/JSON 地下水化学表，检查推荐字段和缺失项 |
| `scripts/build_solution_block.py` | 从水化学表生成 `SOLUTION` block |
| `scripts/generate_selected_output.py` | 生成 `SELECTED_OUTPUT` 片段 |
| `scripts/make_phreeqc_run_manifest.py` | 生成 PHREEQC run manifest 和 checksum |
| `scripts/parse_selected_output.py` | 将 PHREEQC selected output 转为 JSON 或 CSV |

### 4.4 内置示例

| 示例 | 说明 |
|---|---|
| `examples/phreeqc-uranium-groundwater.md` | 铀地下水形态分布与饱和指数筛选 |
| `examples/phreeqc-tailings-seepage.md` | 尾矿水、背景地下水与混合渗滤情景 |
| `examples/phreeqc-acid-mine-drainage.md` | 酸性矿山排水中和、金属迁移与矿物饱和指数 |

---

## 5. 标准科研工作流

当前 PHREEQC skill 支持如下完整科研链条：

```text
1. 研究问题定义
   ↓
2. 模型类型分类
   ↓
3. 数据采集与表结构审计
   ↓
4. 实测数据 / 假设 / 占位符分离
   ↓
5. PHREEQC 数据库选择
   ↓
6. keyword plan
   ↓
7. .phr 输入文件生成
   ↓
8. selected output 设计
   ↓
9. 本地 PHREEQC 运行或未执行 draft 标记
   ↓
10. selected output 解析
   ↓
11. 图表、相关性分析和机制解释
   ↓
12. 论文方法、结果、限制和 provenance 生成
   ↓
13. Markdown / normalized Markdown / HTML / PDF 论文产物
```

这一流程特别适合“先构建可复用科研测试链条，再逐步替换为真实观测数据”的场景。

---

## 6. 使用案例

### 6.1 铀矿区 U-Ra-SO4-CO3 地下水体系

本仓库已有一个完整案例：

```text
report/2026-05-13-geomine-phreeqc-u-ra-so4-co3-groundwater/
```

研究主题：

```text
铀矿区地下水中 U-Ra-SO4-CO3 体系的地球化学控制机制
```

已生成内容：

- `data/synthetic_groundwater_endmembers.csv`：13 个合成端元与混合水样；
- `models/phreeqc/u_ra_so4_co3_screening.phr`：PHREEQC 输入文件；
- `models/phreeqc/u_ra_so4_co3_screening.out`：PHREEQC 输出文件；
- `models/phreeqc/selected_output.tsv`：selected output；
- `data/screening_results.csv`：输入数据、PHREEQC 输出和机制评分整合表；
- `figures/*.svg`：二维相关性图、散点图、机制分数和饱和指数热图；
- `u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.md`：中文论文；
- `u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.pdf`：论文 PDF；
- `u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.normalized.pdf`：normalized Markdown 对应 PDF。

该案例已完成本地 PHREEQC 运行：

```text
PHREEQC executable: /Users/aibao/.local/bin/phreeqc
Database: /Users/aibao/.local/phreeqc/phreeqc-3.5.0-14000/database/llnl.dat
Sample count: 13
Run status: completed
```

科学解释边界：

- 合成水样用于 skill 验证，不是 Athabasca 实测数据；
- PHREEQC selected output 是筛选计算，不是场地验证；
- Ra-226 activity 被换算为元素 Ra 质量输入用于 workflow 测试；
- 真实场地解释前必须重新审计数据库覆盖、矿物相、红氧状态、吸附和共沉淀常数。

### 6.2 铀地下水形态与饱和指数筛选

适用问题：

- 氧化富碳酸盐地下水中 U 是否主要以 uranyl-carbonate 络合物迁移；
- 还原条件下 U 是否受 uraninite 或 coffinite 饱和控制；
- calcite、gypsum、barite、ferrihydrite 等矿物是否对水化学有控制作用。

典型模型：

```text
model types: speciation + saturation_index
database: llnl.dat or checked phreeqc.dat/wateq4f.dat
keywords: SOLUTION + SELECTED_OUTPUT
```

典型 selected output：

```phreeqc
-totals U Ca Mg Na K Cl S(6)
-saturation_indices Calcite Gypsum Ferrihydrite Uraninite Schoepite
-molalities UO2+2 UO2CO3 UO2(CO3)2-2 UO2(CO3)3-4
```

### 6.3 尾矿渗滤液混合与衰减假设

适用问题：

- 尾矿孔隙水进入背景地下水后，pH、SO4、Fe、Mn 和 trace metals 如何变化；
- 混合比例是否会导致 gypsum、calcite、Fe oxyhydroxides 或 jarosite-family phases 接近饱和；
- 金属衰减是矿物沉淀、吸附还是简单稀释造成的假设。

典型模型：

```text
model types: speciation + saturation_index + batch_reaction
optional: inverse_modeling / one_dimensional_transport
keywords: SOLUTION 1 + SOLUTION 2 + MIX + SELECTED_OUTPUT
```

关键边界：

- 混合比例未知时只能作为 scenario placeholder；
- 没有 seepage flux、矿物丰度、吸附容量和下游监测数据时，不能声称衰减能力已经验证。

### 6.4 酸性矿山排水中和模拟

适用问题：

- AMD 水体中 Fe、Al、Mn、SO4 和 trace metals 的形态与饱和指数；
- calcite、dolomite 或 alkalinity addition 对 pH 和金属沉淀的情景影响；
- pyrite oxidation 或中和动力学是否可建模。

典型模型：

```text
model types: speciation + saturation_index + batch_reaction
optional: kinetic_reactions
keywords: SOLUTION + REACTION + SELECTED_OUTPUT + optional EQUILIBRIUM_PHASES
```

关键边界：

- 不能编造 pyrite abundance、oxygen flux、rate constant、field seepage rate；
- 动力学模型必须有文献或实验支持的速率律。

### 6.5 THMC / PhreeqcRM 耦合前置设计

适用问题：

- OpenGeoSys、PFLOTRAN 或其他 transport solver 负责 H/T/M，PHREEQC 负责 C；
- 每个 cell 的 solution、矿物、表面、交换位点如何初始化；
- selected output 如何映射回 transport solver；
- coupling interval、state variables 和 restart/versioning 如何设计。

当前状态：

- `phreeqc-modeling-skill` 可以输出 PhreeqcRM coupling plan；
- `phreeqc-coupling-skill` 可以在 MCP 可用时请求构建或运行 PHREEQC artifact；
- 若 MCP 不可用，则只生成 draft block，不声称 live coupled run。

---

## 7. 输出包规范

一个完整的 PHREEQC Modeling Package 应包含：

1. 研究目标；
2. 模型类型分类；
3. 输入数据审计；
4. 数据库推荐；
5. PHREEQC keyword plan；
6. 生成的 `.phr` 输入；
7. 运行说明；
8. selected output 设计；
9. 解释计划；
10. 论文方法草稿；
11. 限制与不确定性；
12. future MCP extension 或 coupling plan。

在 OpenMiner/GeoMine 报告目录中，推荐产物结构为：

```text
report/<date>-geomine-<topic>/
  README.md
  mcp_provenance.md
  workflow_manifest.json
  data/
    input_chemistry.csv
    screening_results.csv
  models/
    phreeqc/
      model.phr
      model.out
      selected_output.tsv
      phreeqc.log
  scripts/
    generate_*.py
  figures/
    *.svg
  <paper>.md
  <paper>.normalized.md
  <paper>.html
  <paper>.pdf
  <paper>.normalized.pdf
```

---

## 8. 当前能力边界

PHREEQC skill 的 guardrails 很明确：

- 不发明实测浓度、动力学常数、表面络合常数、热力学数据、矿物量、校准结果或边界条件；
- PHREEQC 输出是地球化学计算，不等于场地验证；
- draft `.phr` 文件不是有效性证明；
- mock run 只验证 workflow 形状，不代表真实计算结果；
- 单一 pe/Eh 可能无法代表复杂红氧非平衡系统；
- 高盐地下水需要评估 Pitzer 或 SIT，而不能默认使用普通 Debye-Huckel 模型；
- 逆向建模结果非唯一；
- transport 输出必须有合理边界、几何、弥散/扩散参数和校准证据；
- 不能把 PHREEQC 结果写成监管合规证明、Qualified Person 意见、资源储量声明或工程设计结论。

---

## 9. 当前成熟度评价

| 能力 | 当前状态 |
|---|---|
| 数据表审计 | 已有 schema 和校验脚本 |
| `SOLUTION` 生成 | 已有脚本和模板 |
| selected output 生成 | 已有脚本和模板 |
| 数据库选择 | 已有参考规则 |
| uranium/radionuclide workflow | 已有示例与完整执行案例 |
| tailings seepage workflow | 已有示例，可作为 THMC 化学模块 |
| AMD workflow | 已有示例和反应模式 |
| 本地 PHREEQC 运行 | 已在 U-Ra-SO4-CO3 案例验证 |
| 输出解析 | 已有 selected output 解析脚本 |
| 图表和论文链条 | 已在 U-Ra-SO4-CO3 案例验证 |
| PhreeqcRM / THMC coupling | 已有 coupling plan 能力，live MCP 依赖环境 |
| live PHREEQC MCP server | 尚未内置；skill 明确要求 local-only 或可用 MCP 模式标注 |

---

## 10. 建议后续增强

短期增强：

- 增加 `run_phreeqc` 本地 wrapper，统一运行、日志、错误解析和 manifest 更新；
- 增加 charge balance 报告和自动 QA/QC 表；
- 增加 PHREEQC selected output 到标准 figure/table 的自动映射；
- 为 U-Ra-SO4-CO3、AMD、tailings seepage 提供更完整的 notebook-style example。

中期增强：

- 建立数据库 coverage checker，自动检查目标物种、矿物和 surface constants 是否存在；
- 增加 `Ra-Ba-Sr-SO4` 共沉淀与 barite/celestite 控制的专用模板；
- 增加 PHREEQC inverse modeling 模板和非唯一性解释报告；
- 增加高盐地下水 `pitzer.dat` / `sit.dat` 选择辅助。

长期增强：

- 实现 live PHREEQC MCP tools：
  - `run_phreeqc`
  - `validate_phreeqc_input`
  - `parse_phreeqc_output`
  - `save_model_version`
  - `query_water_samples`
  - `query_mineralogy`
- 与 OpenGeoSys / PFLOTRAN / PhreeqcRM 工作流建立可执行 coupling artifact；
- 将 provenance、manifest、selected output、figures 和论文 PDF 统一为可检索的 GeoMine Research artifact。

---

## 11. 一句话总结

当前 GeoMine Research 的 PHREEQC skill 已经具备“科研级 PHREEQC 建模包生成能力”：它能从地下水化学数据和研究问题出发，完成数据审计、模型分类、数据库选择、PHREEQC 输入生成、selected output 设计、本地运行与解析、图表/论文解释和 PDF 产物组织；它的主要边界是不会替代真实场地数据、热力学审计、校准验证和专业监管判断。
