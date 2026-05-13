# GeoMine Research 插件：THMC Skill Family 说明文档

> 文档名称：GeoMine THMC Skill Family Guide  
> 适用插件：GeoMine Research / OpenMine.VIP Research Workflow  
> 模块名称：`thmc-modeling`  
> 版本建议：v0.1.0  
> 文档用途：说明 THMC skill family 的构造过程、内部工作流、输出包结构和典型使用示例。

---

## 1. 模块定位

`thmc-modeling` 是 GeoMine Research 插件中的高级科研建模 skill family，用于支持 **热—水—力—化学耦合过程** 下的地下水化学、反应输运、矿区环境、核素迁移、尾矿渗滤液、酸性矿山排水、深地处置、地热流体和长期环境风险研究。

它不是一个单一求解器，也不是简单生成 COMSOL、PHREEQC 或 PFLOTRAN 输入文件的工具，而是一个面向科研论文和工程研究的 **THMC Modeling Package 生成工作流**。

它的核心目标是：

```text
从科研问题出发
  ↓
自动判断 THMC 过程类型
  ↓
建立概念模型
  ↓
识别 T/H/M/C 耦合关系
  ↓
组织控制方程
  ↓
设计地球化学反应网络
  ↓
选择数值实现路线
  ↓
设计校准、验证和不确定性分析
  ↓
输出论文级 THMC Modeling Package
```

---

## 2. THMC 的含义

THMC 代表：

| 缩写 | 英文 | 中文含义 | 在地下水化学中的作用 |
|---|---|---|---|
| T | Thermal | 热过程 | 控制温度场、热传导、热对流、反应速率、溶解度、黏度和密度 |
| H | Hydrological | 水文过程 | 控制地下水流动、压力、水头、渗流、对流输运、弥散和扩散 |
| M | Mechanical | 力学过程 | 控制应力、变形、裂隙开度、孔隙率、渗透率和损伤演化 |
| C | Chemical | 化学过程 | 控制水岩反应、络合、吸附、离子交换、氧化还原、矿物溶解沉淀和核素衰变 |

对于地下水化学建模，最常见的耦合形式包括：

```text
HC     = 地下水流动 + 化学反应输运
THC    = 热场 + 地下水流动 + 化学反应输运
HMC    = 地下水流动 + 力学变形 + 化学反馈
THMC   = 完整热—水—力—化学耦合
```

实际建模时，不应默认使用最复杂的 THMC。`thmc-modeling` skill family 的重要职责之一，就是根据科研问题自动判断是否真的需要完整 THMC，还是采用 HC、THC 或 THM 即可。

---

## 3. 在 GeoMine Research 插件中的位置

建议目录结构如下：

```text
geo-mining-research/
  skills/
    thmc-modeling/
      thmc-groundwater-router-skill/
        SKILL.md
      conceptual-thmc-model-skill/
        SKILL.md
      thmc-coupling-matrix-skill/
        SKILL.md
      governing-equations-skill/
        SKILL.md
      hydro-transport-skill/
        SKILL.md
      geochemical-reaction-network-skill/
        SKILL.md
      thermal-gradient-heat-transport-skill/
        SKILL.md
      mechanical-damage-permeability-skill/
        SKILL.md
      solver-selection-skill/
        SKILL.md
      phreeqc-coupling-skill/
        SKILL.md
      comsol-thmc-setup-skill/
        SKILL.md
      ogs-phreeqc-setup-skill/
        SKILL.md
      pflotran-reactive-transport-skill/
        SKILL.md
      calibration-validation-skill/
        SKILL.md
      uncertainty-sensitivity-skill/
        SKILL.md
      thmc-paper-figure-skill/
        SKILL.md
      thmc-report-synthesis-skill/
        SKILL.md
      templates/
        thmc-modeling-package-template.md
        thmc-coupling-matrix-template.md
        thmc-parameter-table-template.md
        thmc-json-model-spec.schema.json
      references/
        thmc-process-taxonomy.md
        groundwater-reactive-transport-basics.md
        uranium-series-reaction-network.md
        acid-mine-drainage-reaction-network.md
        tailings-seepage-reaction-network.md
        bentonite-buffer-thmc.md
        solver-selection-guide.md
      scripts/
        validate_thmc_model_spec.py
        generate_coupling_matrix.py
        generate_parameter_table.py
```

在 GeoMine Research 总体插件中，它与以下模块连接：

```text
GeoMine Research Router
  ├─ GIS / Geodata Discovery
  ├─ Geochemistry
  ├─ Mineral Exploration
  ├─ Canadian Compliance
  ├─ Academic Figure Package
  └─ THMC Groundwater Chemistry Modeling
```

当用户问题涉及地下水化学、反应输运、核素迁移、热梯度、裂隙渗流、尾矿渗滤液、酸性矿山排水、深地处置、地热流体或长期环境风险时，总 router 应自动转入 `thmc-modeling` skill family。

---

## 4. 构造过程总览

构造 `thmc-modeling` skill family 可分为 7 个阶段。

### 阶段 1：定义科研问题分类体系

首先要让 router 能判断用户问题属于哪一类 THMC 研究。

建议分类：

```text
acid_mine_drainage
uranium_mine_groundwater
radionuclide_transport
tailings_seepage
nuclear_waste_repository
bentonite_buffer_evolution
geothermal_fluid_rock_interaction
co2_storage_reactive_transport
fractured_rock_contaminant_transport
mining_heat_pollution
long_term_groundwater_risk
```

每种问题对应不同的化学反应网络、耦合强度和软件路线。

---

### 阶段 2：定义 THMC 耦合层级

不是所有问题都需要完整 THMC。应先判断模型复杂度。

| 模型层级 | 启用过程 | 适用场景 |
|---|---|---|
| H | 地下水流动 | 只关心水头、流向、补给排泄 |
| HC | 地下水 + 化学输运 | 常规污染物迁移、水岩反应、地下水化学演化 |
| THC | 热 + 水 + 化学 | 地热、热污染、核废料热源、温度控制反应速率 |
| HM | 水 + 力 | 孔压、有效应力、裂隙开闭、沉降 |
| HMC | 水 + 力 + 化学 | 矿物沉淀/溶解导致渗透率变化、裂隙化学堵塞 |
| THMC | 热 + 水 + 力 + 化学 | 深地处置、长期核素迁移、高温水岩反应、强反馈系统 |

router 的判断原则：

```text
如果只有地下水化学和溶质迁移 → HC
如果温度显著影响反应或流体性质 → THC
如果应力、裂隙开度、孔隙率、渗透率会演化 → HMC 或 THMC
如果热源、地下水流动、变形和化学反馈同时重要 → THMC
```

---

### 阶段 3：设计子 skill 职责

每个子 skill 应只负责一个清晰任务。

| Skill | 职责 |
|---|---|
| `thmc-groundwater-router-skill` | 识别研究问题、判断耦合层级、选择下游 skills、组织最终输出 |
| `conceptual-thmc-model-skill` | 建立研究域、边界、地层、裂隙、反应区和观测点的概念模型 |
| `thmc-coupling-matrix-skill` | 生成 T/H/M/C 之间的耦合矩阵和反馈路径 |
| `governing-equations-skill` | 输出热、水、力、化学控制方程及变量说明 |
| `hydro-transport-skill` | 设计地下水流动、对流、弥散、扩散、基质扩散模型 |
| `geochemical-reaction-network-skill` | 设计水岩反应、络合、吸附、离子交换、氧化还原、矿物反应和核素衰变网络 |
| `thermal-gradient-heat-transport-skill` | 处理热传导、热对流、温度依赖参数和热边界条件 |
| `mechanical-damage-permeability-skill` | 处理应力、变形、裂隙开度、孔隙率和渗透率反馈 |
| `solver-selection-skill` | 推荐 PHREEQC、COMSOL、OpenGeoSys、PFLOTRAN、Python、PINN 等路线 |
| `phreeqc-coupling-skill` | 生成 PHREEQC 反应网络和耦合思路 |
| `comsol-thmc-setup-skill` | 生成 COMSOL 多物理场设置方案 |
| `ogs-phreeqc-setup-skill` | 生成 OpenGeoSys + PHREEQC 设置方案 |
| `pflotran-reactive-transport-skill` | 生成 PFLOTRAN 反应输运设置方案 |
| `calibration-validation-skill` | 设计校准目标、验证数据和 benchmark |
| `uncertainty-sensitivity-skill` | 设计参数敏感性、不确定性和长期预测分析 |
| `thmc-paper-figure-skill` | 生成 THMC 论文图版计划 |
| `thmc-report-synthesis-skill` | 汇总完整 THMC Modeling Package |

---

### 阶段 4：定义标准输出包

所有 THMC 任务最终都应输出一个标准化的 **THMC Modeling Package**。

它不是单纯报告，而是一个可继续开发为代码、论文、图版和数值模型的结构化包。

---

### 阶段 5：准备反应网络参考库

THMC 地下水化学模型的难点在 C，即化学反应网络。

建议内置以下参考文件：

```text
references/
  uranium-series-reaction-network.md
  acid-mine-drainage-reaction-network.md
  tailings-seepage-reaction-network.md
  bentonite-buffer-thmc.md
  geothermal-water-rock-reaction-network.md
  carbonate-buffering-system.md
  sorption-surface-complexation-basics.md
  redox-reaction-basics.md
```

这些文件帮助 skill 在没有外部数据库时，也能生成合理的反应网络草案。

---

### 阶段 6：准备输出模板

建议模板包括：

```text
templates/
  thmc-modeling-package-template.md
  thmc-coupling-matrix-template.md
  thmc-parameter-table-template.md
  thmc-reaction-network-template.md
  thmc-solver-selection-template.md
  thmc-validation-plan-template.md
  thmc-json-model-spec.schema.json
```

---

### 阶段 7：建立自动调用规则

GeoMine Research 总 router 应加入以下规则：

```text
If the user asks about groundwater chemistry, reactive transport, radionuclide migration,
acid mine drainage, tailings seepage, thermal gradients, fractured rock groundwater,
bentonite buffer evolution, geothermal water-rock interaction, porosity-permeability feedback,
or long-term subsurface environmental risk, route the task to thmc-groundwater-router-skill.
```

THMC router 再决定调用哪些子 skill。

---

## 5. THMC Modeling Package 输出结构

标准输出包如下：

```markdown
# THMC Groundwater Chemistry Modeling Package

## 1. Research Objective

## 2. Scenario Classification

## 3. Required Coupling Level

## 4. Conceptual Model

## 5. THMC Coupling Matrix

## 6. Model Domain and Geometry

## 7. Primary Variables

## 8. Governing Equations

## 9. Boundary and Initial Conditions

## 10. Geochemical Reaction Network

## 11. Parameters and Data Requirements

## 12. Solver / Software Recommendation

## 13. Implementation Plan

## 14. Calibration and Validation Plan

## 15. Sensitivity and Uncertainty Plan

## 16. Expected Outputs

## 17. Publication Figure Plan

## 18. Limitations and Assumptions

## 19. Machine-readable JSON Model Spec
```

---

## 6. THMC Modeling Package 各部分说明

### 6.1 Research Objective

说明研究目标，例如：

```text
评估铀矿区裂隙花岗岩地下水中 U-Ra-Rn-Pb-Po 系列核素在 100 年尺度内的迁移行为及剂量贡献。
```

该部分应明确：

```text
- 研究对象
- 研究尺度
- 时间尺度
- 目标变量
- 风险或科学问题
```

---

### 6.2 Scenario Classification

自动分类，例如：

```json
{
  "scenario": "radionuclide_transport",
  "sub_scenario": "uranium_mine_groundwater",
  "domain": "fractured_crystalline_rock",
  "time_scale": "long_term",
  "risk_focus": "drinking_water_and_environmental_dose"
}
```

---

### 6.3 Required Coupling Level

判断需要 HC、THC、HMC 还是 THMC。

示例：

```text
Recommended coupling level: THC, with optional M feedback.

Reason:
- Groundwater flow and chemical reaction transport are essential.
- Temperature affects reaction kinetics, equilibrium constants, viscosity, and diffusion.
- Mechanical deformation may be secondary unless fracture aperture or permeability evolution is significant.
```

---

### 6.4 Conceptual Model

概念模型应包括：

```text
- 地质介质
- 地下水路径
- 热源或温度梯度
- 裂隙和孔隙结构
- 化学反应区
- 污染源或核素源项
- 观测井或采样点
- 关键边界条件
```

示例：

```text
The model domain is represented as a fractured granitic bedrock system with a weathered upper zone, a connected fracture network, and a low-permeability rock matrix. Groundwater flows from recharge areas toward discharge zones. Uranium-series radionuclides are released from mineralized zones or mine-affected groundwater, transported along fractures, retarded by adsorption on Fe/Mn oxides and clay minerals, and transformed by radioactive decay-chain ingrowth.
```

---

### 6.5 THMC Coupling Matrix

示例矩阵：

| From / To | T | H | M | C |
|---|---|---|---|---|
| T | — | 温度影响水密度、黏度和热对流 | 热膨胀影响应力 | 温度影响平衡常数和反应速率 |
| H | 对流携带热量 | — | 孔压影响有效应力 | 地下水输运溶质和反应物 |
| M | 变形热通常可忽略 | 应力改变裂隙开度、孔隙率和渗透率 | — | 矿物沉淀/溶解影响岩体刚度 |
| C | 反应热通常次要 | 沉淀/溶解改变孔隙率和渗透率 | 化学弱化或胶结影响力学性质 | — |

---

### 6.6 Primary Variables

| Field | Primary Variables | Notes |
|---|---|---|
| Thermal | `T` | temperature |
| Hydrological | `p`, `h`, `q`, `S_w` | pressure, hydraulic head, Darcy flux, saturation |
| Mechanical | `u`, `σ`, `ε` | displacement, stress, strain |
| Chemical | `C_i`, `a_i`, `SI`, `V_m` | concentration, activity, saturation index, mineral volume |

---

### 6.7 Governing Equations

文档应根据耦合级别输出不同方程。

#### 地下水流动

```text
∂(ρφ)/∂t + ∇·(ρq) = Q
q = -(k/μ)(∇p - ρg)
```

#### 溶质输运

```text
∂(φC_i)/∂t + ∇·(qC_i - φD∇C_i) = R_i
```

#### 热输运

```text
(ρC_p)_eff ∂T/∂t + ρ_w C_w q·∇T = ∇·(λ_eff ∇T) + Q_T
```

#### 力学平衡

```text
∇·σ + f = 0
σ' = σ - αpI
```

#### 化学源汇项

```text
R_i = R_i^{eq} + R_i^{kinetic} + R_i^{sorption} + R_i^{decay}
```

---

### 6.8 Geochemical Reaction Network

应输出反应网络表。

| Category | Components |
|---|---|
| Master species | H, O, C, Ca, Mg, Na, K, Cl, S, Fe, Mn, U, Ra, Pb, Po, Rn |
| Aqueous complexes | carbonate complexes, sulfate complexes, hydroxide complexes |
| Minerals | calcite, dolomite, gypsum, barite, uraninite, goethite, ferrihydrite, clay minerals, quartz |
| Surface reactions | adsorption on Fe/Mn oxides, clay surfaces, organic matter if relevant |
| Redox reactions | U(VI)/U(IV), Fe(III)/Fe(II), Mn(IV)/Mn(II) |
| Kinetic reactions | pyrite oxidation, silicate dissolution, mineral precipitation |
| Decay chain | U → Ra → Rn → Pb → Po |

---

### 6.9 Parameters and Data Requirements

| Parameter Group | Required Data | Source Type |
|---|---|---|
| Hydraulic | hydraulic conductivity, porosity, dispersivity, storage | field tests, literature, calibration |
| Thermal | thermal conductivity, heat capacity, temperature gradient | lab data, borehole data |
| Mechanical | Young's modulus, Poisson ratio, Biot coefficient, fracture stiffness | rock mechanics tests |
| Chemical | major ions, trace metals, pH, Eh, alkalinity, mineralogy | water chemistry, XRD, lab analysis |
| Reaction | equilibrium constants, kinetic rates, sorption coefficients | thermodynamic database, experiments |
| Geometry | fracture network, layers, boundary geometry | GIS, boreholes, geologic sections |

---

### 6.10 Solver / Software Recommendation

| Software Route | Best Use Case | Strength | Limitation |
|---|---|---|---|
| PHREEQC | 批反应、1D 反应输运、反应网络验证 | 地球化学能力强 | THM 能力弱 |
| COMSOL + PHREEQC | 多物理场、复杂几何、工程模型 | UI 强、多物理场耦合灵活 | 授权和耦合复杂 |
| OpenGeoSys + PHREEQC | 开源 THMC、地质介质、论文可复现 | 科研友好、适合 THMC | 学习成本较高 |
| PFLOTRAN | 大尺度反应输运、高性能计算 | HPC 能力强 | 前处理和可视化门槛较高 |
| Python + PHREEQC | 原型、自动化、参数扫描 | 灵活、适合 AI workflow | 不适合复杂 3D THMC |
| PINN / PyTorch | 代理模型、反演、长期预测 | 可结合 AI | 必须用物理模型验证 |

---

### 6.11 Implementation Plan

示例：

```text
Phase 1: Build geochemical reaction network in PHREEQC.
Phase 2: Validate batch reaction and 1D transport behavior.
Phase 3: Build 2D hydro-transport domain in OGS or COMSOL.
Phase 4: Couple temperature-dependent reaction rates and transport parameters.
Phase 5: Add porosity-permeability feedback if mineral volume change is significant.
Phase 6: Calibrate against water chemistry and hydraulic observations.
Phase 7: Run long-term prediction and sensitivity analysis.
```

---

### 6.12 Calibration and Validation Plan

Calibration targets:

```text
- hydraulic head
- groundwater flow direction
- temperature profile
- pH
- Eh
- EC / TDS
- major ions
- trace metals
- radionuclide concentrations
- saturation indices
- mineralogical changes
```

Validation methods:

```text
- independent sampling wells
- historical monitoring data
- laboratory column experiments
- benchmark cases
- mass balance checks
- sensitivity consistency checks
```

---

### 6.13 Sensitivity and Uncertainty Plan

Key sensitivity parameters:

```text
- hydraulic conductivity
- fracture aperture
- porosity
- dispersivity
- diffusion coefficient
- temperature gradient
- reaction rate constants
- sorption coefficients
- mineral surface area
- source-term concentration
```

Recommended methods:

```text
- one-at-a-time sensitivity analysis
- Latin Hypercube Sampling
- Monte Carlo simulation
- Sobol sensitivity indices
- scenario comparison
```

---

### 6.14 Publication Figure Plan

建议自动输出论文图版计划：

```text
Figure 1. Conceptual THMC model of the groundwater system
Figure 2. THMC coupling matrix and feedback pathways
Figure 3. Model domain, boundary conditions, and monitoring locations
Figure 4. Geochemical reaction network
Figure 5. Calibration results for hydraulic head and water chemistry
Figure 6. Spatial distribution of pH, Eh, temperature, and key species
Figure 7. Porosity/permeability evolution under reaction feedback
Figure 8. Long-term prediction and uncertainty envelope
```

该部分应自动调用或对接 `academic-figure-design-skill`。

---

### 6.15 Machine-readable JSON Model Spec

示例：

```json
{
  "model_type": "THC_with_optional_M_feedback",
  "scenario": "uranium_mine_groundwater",
  "domain": {
    "geometry": "2D fractured bedrock cross-section",
    "scale": "field",
    "time_scale": "100 years"
  },
  "enabled_processes": {
    "thermal": true,
    "hydrological": true,
    "mechanical": "optional",
    "chemical": true
  },
  "primary_variables": {
    "thermal": ["T"],
    "hydrological": ["p", "h", "q"],
    "mechanical": ["u", "sigma", "epsilon"],
    "chemical": ["C_i", "SI", "mineral_volume"]
  },
  "reaction_network": {
    "master_species": ["H", "O", "C", "Ca", "Mg", "Na", "K", "Cl", "S", "Fe", "Mn", "U", "Ra", "Pb", "Po", "Rn"],
    "minerals": ["calcite", "dolomite", "gypsum", "barite", "uraninite", "goethite", "ferrihydrite", "quartz"],
    "processes": ["carbonate_complexation", "surface_adsorption", "redox_transformation", "mineral_precipitation", "radioactive_decay"]
  },
  "recommended_solver": "OpenGeoSys + PHREEQC",
  "fallback_solver": "Python + PHREEQC prototype",
  "validation_targets": ["head", "temperature", "pH", "Eh", "major_ions", "radionuclides"],
  "limitations": [
    "Requires site-specific mineralogy and water chemistry",
    "Mechanical feedback should be included only if fracture aperture evolution is significant",
    "Reaction rates and sorption parameters require calibration or laboratory constraints"
  ]
}
```

---

## 7. Skill 内部自动调用流程

### 7.1 总调用逻辑

```text
User Prompt
  ↓
GeoMine Research Router
  ↓
Detect THMC-related keywords and scientific intent
  ↓
thmc-groundwater-router-skill
  ↓
Classify scenario and coupling level
  ↓
Call required THMC family skills
  ↓
Collect partial outputs
  ↓
thmc-report-synthesis-skill
  ↓
Generate THMC Modeling Package
```

---

### 7.2 THMC Router 的判断规则

触发 THMC family 的关键词包括：

```text
地下水化学
反应输运
水岩反应
核素迁移
酸性矿山排水
尾矿渗滤液
热梯度
地热
热污染
裂隙渗流
孔隙率变化
渗透率演化
矿物沉淀
矿物溶解
吸附/解吸
氧化还原
PHREEQC
COMSOL
OpenGeoSys
PFLOTRAN
PINN
THMC
THC
HMC
```

耦合判断规则：

```text
If the question only involves water flow and solute transport → HC.
If temperature affects reaction, density, viscosity, or diffusion → THC.
If stress or deformation changes fracture aperture, porosity, or permeability → HM/HMC.
If all T, H, M, and C feedbacks are active or relevant → THMC.
```

---

### 7.3 自动调用示例

用户输入：

```text
我要建立一个铀矿区地下水中 U-Ra-Rn-Pb-Po 系列核素迁移的 THMC 模型，考虑热梯度、水岩反应、裂隙流和长期风险。
```

Router 判断：

```json
{
  "scenario": "radionuclide_transport",
  "sub_scenario": "uranium_mine_groundwater",
  "recommended_coupling": "THC_with_optional_M",
  "required_skills": [
    "conceptual-thmc-model-skill",
    "thmc-coupling-matrix-skill",
    "governing-equations-skill",
    "hydro-transport-skill",
    "geochemical-reaction-network-skill",
    "thermal-gradient-heat-transport-skill",
    "mechanical-damage-permeability-skill",
    "solver-selection-skill",
    "calibration-validation-skill",
    "thmc-paper-figure-skill",
    "thmc-report-synthesis-skill"
  ]
}
```

---

## 8. 使用示例

## 示例 1：铀矿区核素迁移 THMC 模型

### 用户 Prompt

```text
Use GeoMine Research THMC Modeling.

Task:
Build a THMC Modeling Package for uranium-series radionuclide migration in fractured granitic groundwater near a uranium mining area.

Focus:
- U, Ra, Rn, Pb, Po decay-series migration
- groundwater flow in fractures and porous matrix
- redox and carbonate control
- adsorption/desorption on mineral surfaces
- temperature gradient and long-term reaction effects
- porosity/permeability feedback if mineral precipitation or dissolution is significant

Return:
1. conceptual THMC model
2. coupling matrix
3. governing equations
4. geochemical reaction network
5. parameter table
6. recommended solver route
7. validation plan
8. expected outputs and figures
9. paper-ready methods description
10. model limitations
11. machine-readable JSON model spec
```

### 预期输出摘要

```text
Recommended coupling level: THC with optional mechanical feedback.

The essential processes are groundwater flow, reactive transport, carbonate complexation, redox transformation, adsorption/desorption, radioactive decay-chain ingrowth, and temperature-dependent reaction/transport parameters. Mechanical coupling should be included only if fracture aperture evolution or mineral precipitation/dissolution significantly changes permeability.
```

---

## 示例 2：酸性矿山排水反应输运模型

### 用户 Prompt

```text
Use GeoMine Research THMC Modeling.

Task:
Design a reactive transport model for acid mine drainage generated from sulfide-bearing waste rock.

Include:
- pyrite oxidation
- oxygen diffusion
- sulfate and acidity generation
- carbonate neutralization
- Fe/Al hydroxide precipitation
- heavy metal mobilization
- groundwater seepage path
- seasonal temperature variation

Please generate a THMC Modeling Package and recommend a solver route.
```

### 自动判断

```json
{
  "scenario": "acid_mine_drainage",
  "recommended_coupling": "THC",
  "reason": [
    "Hydrological transport controls acid and metal migration",
    "Chemical reactions are dominant",
    "Temperature affects pyrite oxidation and reaction kinetics",
    "Mechanical coupling is not necessary unless waste-rock settlement or permeability evolution is included"
  ]
}
```

### 反应网络重点

```text
- Pyrite oxidation
- Fe2+/Fe3+ redox cycling
- Sulfate production
- Acid generation
- Carbonate buffering
- Fe/Al hydroxide precipitation
- Heavy metal adsorption/desorption
- Secondary mineral formation
```

---

## 示例 3：尾矿库渗滤液模型

### 用户 Prompt

```text
Use GeoMine Research THMC Modeling to create a model plan for tailings seepage into shallow groundwater.

Scenario:
Sulfide-bearing tailings release sulfate, metals, and acidic seepage. The system has seasonal temperature variation and a shallow groundwater table.

Return a THMC Modeling Package with conceptual model, governing equations, reaction network, parameters, software recommendation, validation plan, and figure plan.
```

### 自动判断

```text
Recommended coupling level: THC or HMC depending on whether tailings consolidation and permeability evolution are important.

If consolidation is ignored, use THC.
If tailings settlement, pore pressure dissipation, and permeability evolution are central, use HMC or THMC.
```

---

## 示例 4：深地处置膨润土缓冲层 THMC 模型

### 用户 Prompt

```text
Use GeoMine Research THMC Modeling.

Task:
Develop a THMC model for bentonite buffer evolution under thermal gradient and groundwater intrusion.

Include:
- heat transfer from waste package
- bentonite swelling
- hydraulic conductivity evolution
- porewater chemistry
- cation exchange
- mineral dissolution/precipitation
- radionuclide diffusion and sorption
- long-term porosity and permeability changes
```

### 自动判断

```text
Recommended coupling level: Full THMC.

Reason:
Thermal gradient, groundwater intrusion, swelling pressure, hydraulic conductivity evolution, mineral reactions, cation exchange, and radionuclide diffusion are strongly coupled.
```

---

## 示例 5：地热流体水岩反应模型

### 用户 Prompt

```text
Use GeoMine Research THMC Modeling to design a model for geothermal fluid-rock interaction in fractured granite.

Include:
- high-temperature groundwater flow
- silica and carbonate scaling
- fracture permeability evolution
- thermal drawdown
- mineral dissolution and precipitation
- long-term injectivity decline
```

### 自动判断

```text
Recommended coupling level: THMC.

Reason:
Thermal drawdown affects fluid properties and reaction kinetics; groundwater flow controls heat and solute transport; mineral precipitation/dissolution changes fracture permeability; permeability evolution affects hydraulic performance.
```

---

## 9. 与 Academic Figure Package 的集成

`thmc-paper-figure-skill` 应自动调用或复用 `academic-figure-design-skill` 的 Figure Package 思路。

建议输出图版包：

```text
THMC Figure Package
  1. Figure Intent
  2. Content Decomposition
  3. Visual Grammar
  4. Layout Plan
  5. Drawing Prompt
  6. Data Plot Script Plan
  7. Caption Draft
  8. Publication Checklist
```

典型图版：

```text
Figure 1. Conceptual THMC model
Figure 2. Coupling matrix
Figure 3. Model geometry and boundary conditions
Figure 4. Reaction network
Figure 5. Calibration and validation results
Figure 6. Spatial concentration / temperature / pH / Eh maps
Figure 7. Porosity-permeability evolution
Figure 8. Long-term risk prediction and uncertainty
```

---

## 10. 与 MCP 的关系

THMC skill family 第一版不应强依赖 MCP。

### v0.1：Skills-only

可完成：

```text
- 科研问题判断
- 耦合层级选择
- 概念模型
- 控制方程
- 反应网络
- 参数表
- 软件路线
- 校准验证方案
- 图版计划
- 论文方法描述
```

### v0.2：本地脚本增强

可增加：

```text
- 生成 PHREEQC 输入文件草案
- 生成参数表 CSV
- 生成耦合矩阵 JSON
- 生成 Matplotlib 图版草图
- 校验 THMC model spec
```

### v0.3：MCP 增强

MCP 可用于：

```text
- 调用 PHREEQC 服务
- 调用 OpenGeoSys / PFLOTRAN 远程任务
- 读取 OpenMine 项目数据库
- 读取 R2/PostGIS 中的水化学、岩性、地质剖面和网格数据
- 保存模型版本和运行记录
```

建议原则：

```text
Core Mode = skills-only，必须可用
Enhanced Mode = MCP + solver service，可选增强
```

---

## 11. 验收标准

THMC skill family 完成后，应满足以下标准。

### 11.1 结构验收

```text
- `skills/thmc-modeling/` 存在
- 每个子 skill 都有 `SKILL.md`
- 每个 `SKILL.md` 有明确 name 和 description
- templates 文件存在
- references 文件存在
- 至少有一个 THMC Modeling Package 模板
```

### 11.2 功能验收

```text
- 能自动识别 THMC 相关问题
- 能判断 HC / THC / HMC / THMC 耦合层级
- 能选择下游子 skill
- 能生成完整 THMC Modeling Package
- 能输出概念模型、耦合矩阵、方程、反应网络、参数表、软件路线和验证计划
- 能生成 machine-readable JSON model spec
```

### 11.3 科研质量验收

```text
- 不默认过度复杂化模型
- 能明确假设和限制
- 能区分概念模型、数值模型和工程实现
- 能说明哪些数据需要现场或实验补充
- 不把初步模型描述包装成确定性结论
- 不声称替代水文地质师、地球化学专家或注册工程师判断
```

### 11.4 输出验收

最终输出应至少包含：

```text
Research Objective
Scenario Classification
Required Coupling Level
Conceptual Model
THMC Coupling Matrix
Governing Equations
Boundary and Initial Conditions
Geochemical Reaction Network
Parameters and Data Requirements
Solver Recommendation
Implementation Plan
Calibration and Validation Plan
Sensitivity and Uncertainty Plan
Publication Figure Plan
Limitations and Assumptions
Machine-readable JSON Model Spec
```

---

## 12. 推荐开发顺序

建议按以下顺序开发：

```text
1. thmc-groundwater-router-skill
2. conceptual-thmc-model-skill
3. thmc-coupling-matrix-skill
4. governing-equations-skill
5. geochemical-reaction-network-skill
6. hydro-transport-skill
7. solver-selection-skill
8. calibration-validation-skill
9. thmc-paper-figure-skill
10. thmc-report-synthesis-skill
11. templates and references
12. validation scripts
```

不要一开始就写 COMSOL、OGS 或 PFLOTRAN 复杂实现。第一版最重要的是科研建模逻辑正确、输出结构稳定、能自动判断耦合层级。

---

## 13. 推荐给 Codex 的测试 Prompt

### 测试 1：铀矿地下水

```text
Use GeoMine Research THMC Modeling to build a modeling package for U-Ra-Rn-Pb-Po radionuclide migration in fractured granite groundwater near a uranium mining area.
```

### 测试 2：酸性矿山排水

```text
Use GeoMine Research THMC Modeling to design a reactive transport model for acid mine drainage from sulfide-bearing waste rock.
```

### 测试 3：尾矿库渗滤液

```text
Use GeoMine Research THMC Modeling to create a THC/HMC model plan for tailings seepage into shallow groundwater with seasonal temperature variation.
```

### 测试 4：膨润土缓冲层

```text
Use GeoMine Research THMC Modeling to develop a full THMC model for bentonite buffer evolution under thermal gradient and groundwater intrusion.
```

### 测试 5：模型复杂度判断

```text
For this groundwater chemistry problem, decide whether HC, THC, HMC, or THMC is necessary. Explain why and avoid overcomplicating the model.
```

---

## 14. 总结

`thmc-modeling` skill family 是 GeoMine Research 插件从“矿业信息研究助手”升级为“地球化学与地下水数值建模研究助手”的关键模块。

它的核心价值不是直接替代 COMSOL、OpenGeoSys、PFLOTRAN 或 PHREEQC，而是：

```text
1. 自动理解 THMC 科研问题
2. 判断必要耦合层级
3. 建立概念模型
4. 明确控制方程
5. 组织地球化学反应网络
6. 选择合理求解器路线
7. 设计校准验证方案
8. 输出论文级 THMC Modeling Package
```

一句话定义：

> `thmc-modeling` 是 GeoMine Research 插件中的高级科研建模 skill family，用于把地下水化学、水岩反应、热场、渗流场、力学变形和化学反馈统一组织为可建模、可验证、可发表、可工程化扩展的 THMC Modeling Package。

