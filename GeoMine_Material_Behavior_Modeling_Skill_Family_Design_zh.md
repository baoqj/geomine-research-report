# GeoMine Material Behavior Modeling Skill Family 设计说明

发布日期：2026-05-15  
适用范围：GeoMine Research 插件的论文选题、定方向、模型包设计与期刊论文写作前置路由。

## 1. 设计目的

现有 GeoMine Research 已能生成较完整的研究框架、白皮书型论文和 THMC 概念模型，但在 `natural-analogues-dgr-canada` 这类题目上，若缺少原始实验数据、场址专属数据和正式数值求解验证，论文容易停留在宏观综述与方法框架层面。

本 skill family 的目标是在论文选题和定方向阶段就强制进入一条更接近期刊工程论文的逻辑链：

```text
材料机制 -> 本构模型 -> 实验标定 -> FEM / 现场模拟 -> 现场对比或验证 -> 结果与结论
```

它不负责伪造数据或替代求解器运行；它负责判断论文能否成为正式的机制型、工程型、数值模拟型论文，并把缺失数据、参数、实验、求解和验证环节明确列出来。

## 2. Skill Family 架构

源码位置：

```text
plugins/Code/geo-mining-research/skills/material-behavior-modeling/
```

核心子技能：

| Skill | 作用 |
|---|---|
| `material-behavior-router-skill` | 在 GeoMine 路由阶段识别材料行为、本构、实验、FEM、现场验证和 DGR natural analogue 论文需求。 |
| `natural-analogue-dgr-material-scope-skill` | 专门把 Canadian DGR / natural analogue 题目从宏观综述转成材料模型论文方向，并判断 analogue 证据能否支撑模型、参数、边界或验证。 |
| `constitutive-model-development-skill` | 设计本构模型、状态变量、历史变量、方程、参数表、适用范围和 FEM 实现要求。 |
| `laboratory-calibration-skill` | 设计实验矩阵、参数-实验映射、拟合目标函数、QA/QC、不确定性与标定图表。 |
| `fem-simulation-design-skill` | 设计有限元/数值模拟的几何、网格、边界条件、材料区、接口、收敛和结果图。 |
| `field-validation-skill` | 设计现场数据清单、模型输出与观测映射、误差指标、验证/反分析边界和现场对比图。 |
| `material-paper-synthesis-skill` | 汇总成 Material Behavior Modeling Paper Package，并约束论文结构、图表、结论边界和下游写作。 |

辅助资源：

- `references/dgr-natural-analogue-material-model.md`
- `references/material-paper-taxonomy.md`
- `references/constitutive-model-patterns.md`
- `references/laboratory-calibration-rules.md`
- `references/fem-simulation-workflow.md`
- `references/field-validation-and-figures.md`
- `templates/material-behavior-paper-package-template.md`
- `templates/natural-analogue-dgr-topic-gate-template.md`
- `scripts/build_material_paper_plan.py`

## 3. 触发条件

GeoMine Research 在以下场景应优先路由到该 family：

- 用户要求论文不再只是 framework / white paper，而要机制型、工程型、数值模拟型。
- 题目出现：constitutive model、laboratory calibration、FEM、finite element、field simulation、field validation、back-analysis、swelling、creep、plasticity、damage、fracture aperture、stress-dependent permeability。
- DGR 题目出现：natural analogue、Canadian DGR、Revell、deep geological repository、bentonite buffer、crystalline-rock repository、excavation damaged zone、copper-bentonite interface、packer test、borehole monitoring。
- 用户要求论文结构包含 Abstract、Keywords、Introduction、Constitutive model development、Laboratory calibration、Field simulations、Results、Conclusions、References。

## 4. natural-analogues-dgr-canada 的选题闸门

`natural-analogue-dgr-material-scope-skill` 是这次新增的关键前置 skill。它把 natural analogue 证据分配到具体模型角色：

| Analogue 证据 | 可接受角色 | 不能直接声称 |
|---|---|---|
| 文献机制 | 假设与过程选择 | 已标定参数 |
| 可比实验数据 | 参数先验或标定输入 | 加拿大场址现场验证 |
| 钻孔或 packer 记录 | 水力边界或对比目标 | 完整安全案例 |
| 监测时间序列 | 反分析或独立验证 | 盲预测，除非从标定中留出 |
| 地下水化学 | 反应网络约束 | 力学验证 |
| 岩芯力学试验 | 围岩参数约束 | 裂隙网络尺度渗透率证明 |

因此，`natural-analogues-dgr-canada` 后续不应被定成“加拿大 DGR natural analogue 综合框架”这类泛化题目，而应拆成可验证的模型论文方向，例如：

1. 加拿大 DGR natural analogue 约束下的膨润土缓冲层膨胀-渗透率本构模型。
2. Revell-style 结晶岩裂隙开度-应力-渗透率关系与 borehole packer 反分析。
3. DGR 开挖损伤区损伤-渗透率演化的 FEM 模型与现场对比方案。
4. 铜-膨润土-地下水界面的腐蚀、气体与 THMC 耦合模型。

## 5. 论文输出结构

默认成熟结构：

1. Abstract
2. Keywords
3. Introduction
4. Materials and experimental methods
5. Constitutive model development
6. Laboratory calibration
7. FEM / numerical model setup
8. Field simulations or validation case
9. Results
10. Discussion
11. Conclusions
12. References
13. Appendix / supplementary data

用户要求的紧凑结构也可接受：

- Abstract
- Keywords
- Introduction
- Constitutive model development
- Laboratory calibration
- Field simulations
- Results
- Conclusions
- References

关键要求：所有方程、参数表、实验图、模型图和现场对比图必须服务同一条证据链，不能各自孤立。

## 6. Readiness Level

该 family 使用 readiness gate 防止论文结论越界：

| Level | 含义 |
|---|---|
| `L0_idea` | 只有机制设想和数据需求。 |
| `L1_methods_plan` | 有论文架构、实验/模型计划，但无原始实验或现场验证。 |
| `L2_calibration_ready` | 有实验数据，但参数尚未完整拟合。 |
| `L3_simulation_ready` | 有可用参数，FEM 模型可建立。 |
| `L4_executed_model` | 已有求解输出、收敛和核查记录。 |
| `L5_field_validated` | 独立现场观测支持模型，并有误差指标。 |

若当前只有文献与概念图，论文只能标为 `L1_methods_plan`，不能写成已验证工程模型论文。

## 7. 与 THMC / PHREEQC / PFLOTRAN 的关系

Material Behavior Modeling 不是替代 THMC，而是补上材料行为论文缺失的“实验-本构-有限元-验证”中轴。

- 若研究对象是膨润土膨胀、裂隙闭合、EDZ 损伤、应力相关渗透率：先走 Material Behavior。
- 若涉及地下水化学、腐蚀、硫化物、气体、核素迁移、反应运移：同时路由到 THMC / PHREEQC / PFLOTRAN。
- 若需要 DGR 场址或 analogue 实测数据：先路由到 `dgr-field-data-acquisition-skill`，再决定是否能进入标定或验证。

## 8. 实施状态

本次已把设计落到插件源码层：

- 新增 `natural-analogue-dgr-material-scope-skill`。
- 新增 DGR natural analogue material model reference、example 和 topic-gate template。
- 更新 `material-behavior-router-skill`，让 DGR natural analogue 在选题阶段进入该 family。
- 更新 `research-router-skill`、`geomine-research-router-skill` 和 `academic-paper-research-writer`，确保正式论文写作前先生成 Material Behavior Modeling Paper Package。
- 更新 `build_material_paper_plan.py`，使 natural analogue / Canadian DGR 题目自动分类为 `DGR Natural Analogue Material Model Paper`。
- 更新测试，覆盖 family 结构、资源文件、脚本运行和 DGR natural analogue 题目分类。

## 9. 推荐 Prompt

```text
Use GeoMine Research Material Behavior Modeling to turn natural-analogues-dgr-canada into a journal-style material behavior paper. First run the natural analogue DGR topic gate, then build the constitutive model, laboratory calibration plan, FEM field simulation manifest, validation figure plan, and final paper structure.
```

## 10. 结论

这套 skill family 的价值不是把缺失数据补成结果，而是在选题阶段就阻止论文停留在宏观框架。它把 `natural-analogues-dgr-canada` 明确推向可发表工程论文所需的主链条：可检验机制、可写方程、可标定参数、可复现实验、可执行模型和可对比现场证据。
