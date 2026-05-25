# GeoMine Research 报告索引

默认显示英文版：[README.md](./README.md)。本文件为中文版本。

本目录汇总 GeoMine Research 生成的地球科学、矿产勘查、水文地球化学、放射化学、THMC 建模、PHREEQC/PFLOTRAN 工作流设计和研究方法文档。多数日期目录都是自包含研究包，包含 Markdown 论文、PDF 导出、provenance 记录、机器可读摘要、数据表、图件和本地脚本。

研究边界：这些材料用于科研探索、筛选、工作流设计和方法论论证，不构成投资建议、法律意见、Qualified Person 意见、NI 43-101 技术报告、资源量/储量估算、采矿可行性研究、环境许可、核安全结论或经现场验证的场地评价。矿权状态、监管结论、水质、辐射剂量、工程安全和披露决策必须由官方系统和合格专业人员复核。

## 当前目录概况

- 18 个日期化研究包，下方按由新到旧排列。
- 5 份顶层 skill 能力或方法论文档。
- 主要交付物类型：Markdown 论文、PDF 导出、图表包、provenance 记录、JSON/CSV 数据产品、PHREEQC/PFLOTRAN 模型产物和本地分析脚本。
- 相比旧版 README，本次补充索引了 2026-05-12、2026-05-13、2026-05-14 的所有新增研究包，以及 THMC、PHREEQC、PFLOTRAN、Material Behavior Modeling 和地球化学论文架构方法文档。

## 目录规范

- 日期前缀目录为研究包：`YYYY-MM-DD-topic-slug/`。
- 成熟研究包通常应包含包级 `README.md`、一篇或多篇主论文、可用 PDF 导出、使用工具或公开数据时的 `mcp_provenance.md`，以及必要的 `data/`、`figures/`、`models/` 或 `scripts/`。
- `.normalized.md` 或 `.normalized.pdf` 一般表示为了数学公式、化学符号、Mermaid 或图件渲染而生成的导出规范化版本。
- 顶层 `GeoMine_*.md` 是能力说明或方法论文档，不是单个研究项目论文。

## 研究项目与文章列表

### 2026-05-14

#### [野火与极端降雨驱动的放射性核素再迁移](./2026-05-14-wildfire-rainfall-radionuclide-remobilization/)

- 主论文：
  - [Wildfire_Extreme_Rainfall_Radionuclide_Remobilization_Athabasca.zh.md](./2026-05-14-wildfire-rainfall-radionuclide-remobilization/Wildfire_Extreme_Rainfall_Radionuclide_Remobilization_Athabasca.zh.md)
  - [Wildfire_Postfire_Water_Chemistry_Long_Term_Risk_Phase2.zh.md](./2026-05-14-wildfire-rainfall-radionuclide-remobilization/Wildfire_Postfire_Water_Chemistry_Long_Term_Risk_Phase2.zh.md)
- PDF：包含第一阶段和第二阶段的 normalized PDF。
- 支撑文件：[figure_package.md](./2026-05-14-wildfire-rainfall-radionuclide-remobilization/figure_package.md)、[mcp_provenance.md](./2026-05-14-wildfire-rainfall-radionuclide-remobilization/mcp_provenance.md)、`data/`、`figures/`、`models/`、`scripts/`。
- 重点：围绕 Athabasca 铀矿区，构建野火、极端降雨、第一冲刷水化学、沉积物二次源、PHREEQC 敏感性和放射性核素再迁移的公开数据研究框架。
- 边界：仅用于科研筛选和研究设计，不是剂量评价、场地合规判断或监管结论。

### 2026-05-13

#### [PFLOTRAN 尾矿铀系放射性核素反应运移论文](./2026-05-13-geomine-pflotran-tailings-uranium-radionuclide/)

- 主论文：[PFLOTRAN_Tailings_Uranium_Radionuclide_Paper.zh.md](./2026-05-13-geomine-pflotran-tailings-uranium-radionuclide/PFLOTRAN_Tailings_Uranium_Radionuclide_Paper.zh.md)
- 建模包：[PFLOTRAN_Modeling_Package.md](./2026-05-13-geomine-pflotran-tailings-uranium-radionuclide/PFLOTRAN_Modeling_Package.md)
- 图表包：[PFLOTRAN_Tailings_Uranium_Figure_Package.md](./2026-05-13-geomine-pflotran-tailings-uranium-radionuclide/PFLOTRAN_Tailings_Uranium_Figure_Package.md)
- 支撑文件：PFLOTRAN 输入模板、运行清单、验证 JSON、CSV 筛查表和 PNG/SVG 图件。
- 重点：面向铀尾矿渗漏的 PFLOTRAN 式反应运移研究包，覆盖硫酸盐、pH 缓冲、阻滞、敏感性排序和论文级图件生成。

#### [PHREEQC U-Ra-SO4-CO3 地下水工作流](./2026-05-13-geomine-phreeqc-u-ra-so4-co3-groundwater/)

- 主论文：[u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.md](./2026-05-13-geomine-phreeqc-u-ra-so4-co3-groundwater/u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.md)
- PDF：包含原始 PDF 和 normalized PDF。
- 支撑文件：`models/phreeqc/`、[workflow_manifest.json](./2026-05-13-geomine-phreeqc-u-ra-so4-co3-groundwater/workflow_manifest.json)、[datasets_evidence.json](./2026-05-13-geomine-phreeqc-u-ra-so4-co3-groundwater/datasets_evidence.json)、图件、脚本和 provenance。
- 重点：基于 PHREEQC 的铀、镭、硫酸盐、碳酸盐体系形态、饱和指数、地球化学控制和地下水迁移风险筛查流程。
- 边界：在缺少真实监测水化学时，使用占位或合成端元演示科研链条。

#### [裂隙岩体中放射性核素吸附、基质扩散和胶体迁移 THMC](./2026-05-13-geomine-fractured-rock-radionuclide-colloid-thmc/)

- 主论文：[Fractured_Rock_Radionuclide_Sorption_Diffusion_Colloid_THMC_Model.zh.md](./2026-05-13-geomine-fractured-rock-radionuclide-colloid-thmc/Fractured_Rock_Radionuclide_Sorption_Diffusion_Colloid_THMC_Model.zh.md)
- PDF：包含原始 PDF 和 normalized PDF。
- 支撑文件：参数/来源 CSV、筛查结果、summary JSON、SVG 图件、脚本和 provenance。
- 重点：在裂隙结晶岩中对核素迁移、吸附、基质扩散、胶体结合和情景排序进行概念 THMC 筛查。

#### [DGR 铜容器-膨润土-结晶岩 THMC 模型](./2026-05-13-geomine-dgr-copper-bentonite-thmc/)

- 主论文：[DGR_Copper_Bentonite_Crystalline_Rock_THMC_Model.zh.md](./2026-05-13-geomine-dgr-copper-bentonite-thmc/DGR_Copper_Bentonite_Crystalline_Rock_THMC_Model.zh.md)
- PDF：包含原始 PDF 和 normalized PDF。
- 支撑文件：THMC 参数/来源表、筛查输出、SVG 图件、脚本和 provenance。
- 重点：铜容器、膨润土缓冲层、结晶围岩、地下水入渗、热衰减、盐度、膨胀/渗透率、硫化物腐蚀、氢气生成和核素扩散。

#### [尾矿渗滤进入浅层地下水的 THMC 论文](./2026-05-13-geomine-tailings-seepage-thmc-groundwater/)

- 主论文：[Tailings_Seepage_THMC_Groundwater_Paper.zh.md](./2026-05-13-geomine-tailings-seepage-thmc-groundwater/Tailings_Seepage_THMC_Groundwater_Paper.zh.md)
- PDF：[Tailings_Seepage_THMC_Groundwater_Paper.pdf](./2026-05-13-geomine-tailings-seepage-thmc-groundwater/Tailings_Seepage_THMC_Groundwater_Paper.pdf)
- 支撑文件：包级 README 和 MCP provenance。
- 重点：硫化物尾矿氧化、酸生成、碳酸盐中和、二次矿物沉淀、金属阻滞、季节性地下水运动和 THMC 模型选择。

### 2026-05-12

#### [Saskatchewan 铀衰变系地下水学术论文](./2026-05-12-geomine-saskatchewan-uranium-decay-series-groundwater/)

- 主论文：[saskatchewan_uranium_decay_series_groundwater_academic_paper_zh.md](./2026-05-12-geomine-saskatchewan-uranium-decay-series-groundwater/saskatchewan_uranium_decay_series_groundwater_academic_paper_zh.md)
- PDF：包含原始 PDF 和 normalized PDF。
- 支撑文件：包级 README 和 datasets evidence JSON。
- 重点：铀衰变系地下水地球化学、核素迁移、数据源证据和学术论文式综合。

#### [Revell Batholith 辐解地球化学框架](./2026-05-12-geomine-revell-batholith-radiolysis-geochemical-framework/)

- 主论文：
  - [revell_batholith_radiolysis_geochemical_framework_zh.md](./2026-05-12-geomine-revell-batholith-radiolysis-geochemical-framework/revell_batholith_radiolysis_geochemical_framework_zh.md)
  - [revell_batholith_radiolysis_academic_paper_zh.md](./2026-05-12-geomine-revell-batholith-radiolysis-geochemical-framework/revell_batholith_radiolysis_academic_paper_zh.md)
- PDF：两篇文章均包含原始 PDF 和 normalized PDF。
- 支撑文件：[datasets_evidence.json](./2026-05-12-geomine-revell-batholith-radiolysis-geochemical-framework/datasets_evidence.json)
- 重点：Revell Batholith 深部地下水化学、天然辐解产氢、硫酸盐/微生物氧化还原耦合和结晶岩 DGR 安全研究的 THMC 接口。

#### [多孔介质辐解-电解前沿研究](./2026-05-12-geomine-porous-radiolysis-electrolysis-frontier/)

- 主论文：[porous_media_radiolysis_electrolysis_research_report_zh.md](./2026-05-12-geomine-porous-radiolysis-electrolysis-frontier/porous_media_radiolysis_electrolysis_research_report_zh.md)
- PDF：包含原始、normalized 和导出测试 PDF。
- 支撑文件：[mcp_provenance.md](./2026-05-12-geomine-porous-radiolysis-electrolysis-frontier/mcp_provenance.md)、normalized Markdown 和数学转换支持文件。
- 重点：多孔介质水辐解、辐射辅助电解、载流子分离、G 值边界、工程可行性、地球化学和核废料相关性。

### 2026-05-11

#### [Revell Batholith 与 Athabasca 基底中的辐解天然氢](./2026-05-11-geomine-radiolytic-natural-hydrogen-revell-athabasca/)

- 主论文：[radiolytic_natural_hydrogen_revell_athabasca_research_report_zh.md](./2026-05-11-geomine-radiolytic-natural-hydrogen-revell-athabasca/radiolytic_natural_hydrogen_revell_athabasca_research_report_zh.md)
- PDF：[radiolytic_natural_hydrogen_revell_athabasca_research_report_zh.pdf](./2026-05-11-geomine-radiolytic-natural-hydrogen-revell-athabasca/radiolytic_natural_hydrogen_revell_athabasca_research_report_zh.pdf)
- 支撑文件：evidence matrix 和 machine-readable summary。
- 重点：U-Th-K 衰变、深部水辐解、H2 生成、氧化还原晕、硫酸盐平衡和核素迁移反馈。

#### [Patterson Lake Corridor 矿权空档筛选](./2026-05-11-geomine-patterson-lake-corridor-claim-gap/)

- 主论文：[patterson_lake_corridor_claim_gap_research_report_zh.md](./2026-05-11-geomine-patterson-lake-corridor-claim-gap/patterson_lake_corridor_claim_gap_research_report_zh.md)
- PDF：[patterson_lake_corridor_claim_gap_research_report_zh.pdf](./2026-05-11-geomine-patterson-lake-corridor-claim-gap/patterson_lake_corridor_claim_gap_research_report_zh.pdf)
- 支撑文件：evidence matrix、machine-readable summary、数据表和筛查脚本。
- 重点：基于官方矿权、地质、矿产点和勘探证据，对 Saskatchewan Patterson Lake Corridor 的铀、金和关键矿物 claim-gap 进行筛选。

### 2026-05-10

#### [NWT 与 Nunavut 矿业市场进入 SWOT](./2026-05-10-geomine-northern-canada-mining-market-entry/)

- 主论文：[nwt_nunavut_mining_market_entry_swot_report.md](./2026-05-10-geomine-northern-canada-mining-market-entry/nwt_nunavut_mining_market_entry_swot_report.md)
- 重点：分析 NWT 和 Nunavut 矿业公司较少的原因、北方项目难点，以及金矿、铀矿和关键矿物机会的进入条件。

#### [NWT 金矿第二阶段矿权扣减](./2026-05-10-geomine-nwt-gold-phase2-tenure-subtraction/)

- 主论文：[nwt_gold_phase2_tenure_subtraction_report.md](./2026-05-10-geomine-nwt-gold-phase2-tenure-subtraction/nwt_gold_phase2_tenure_subtraction_report.md)
- 补充说明：[south_rae_claim_gap_explanation.md](./2026-05-10-geomine-nwt-gold-phase2-tenure-subtraction/south_rae_claim_gap_explanation.md)
- PDF：[nwt_gold_phase2_tenure_subtraction_report.pdf](./2026-05-10-geomine-nwt-gold-phase2-tenure-subtraction/nwt_gold_phase2_tenure_subtraction_report.pdf)
- 重点：active tenure 精确扣减、open-ground 网格排序、异常源追踪和 South Rae/Hearne margin 优先级解释。

#### [NWT 金矿潜力与 claim-gap 筛选](./2026-05-10-geomine-nwt-gold-prospectivity/)

- 主论文：[nwt_gold_prospectivity_report.md](./2026-05-10-geomine-nwt-gold-prospectivity/nwt_gold_prospectivity_report.md)
- PDF：[nwt_gold_prospectivity_report.pdf](./2026-05-10-geomine-nwt-gold-prospectivity/nwt_gold_prospectivity_report.pdf)
- 重点：Northwest Territories 金矿带的矿点、till Au 地球化学、矿权压力、矿床模型和后续窗口。

#### [辐解辅助制氢可行性](./2026-05-10-radiolysis-assisted-hydrogen-production/)

- 主论文：[radiolysis_assisted_hydrogen_industrial_feasibility_report.md](./2026-05-10-radiolysis-assisted-hydrogen-production/radiolysis_assisted_hydrogen_industrial_feasibility_report.md)
- PDF：[radiolysis_assisted_hydrogen_industrial_feasibility_report.pdf](./2026-05-10-radiolysis-assisted-hydrogen-production/radiolysis_assisted_hydrogen_industrial_feasibility_report.pdf)
- 重点：在能量守恒和 G 值约束下，评估核辐射、多孔半导体和粘土复合材料能否提升电解水制氢效率。

#### [多孔介质辐解文献综述](./2026-05-10-radiolysis-porous-media-review/)

- 主论文：[radiolysis_porous_media_chinese_review.md](./2026-05-10-radiolysis-porous-media-review/radiolysis_porous_media_chinese_review.md)
- PDF：[radiolysis_porous_media_chinese_review.pdf](./2026-05-10-radiolysis-porous-media-review/radiolysis_porous_media_chinese_review.pdf)
- 重点：多孔介质中的水辐解、电子迁移、电场效应、反应网络和控制方程推导。

### 2026-05-09

#### [Wollaston Lake East 铀矿潜力筛选](./2026-05-09-geomine-wollaston-lake-east-uranium-screening/)

- 初筛论文：[wollaston_lake_east_uranium_screening_report.md](./2026-05-09-geomine-wollaston-lake-east-uranium-screening/wollaston_lake_east_uranium_screening_report.md)
- 扩展论文：[wollaston_lake_east_expanded_research_report.md](./2026-05-09-geomine-wollaston-lake-east-uranium-screening/wollaston_lake_east_expanded_research_report.md)
- PDF：两篇文章均包含中文 PDF 导出。
- 支撑文件：evidence matrix 和 machine-readable summary。
- 重点：结合导电体、Wollaston 变沉积岩、放射性漂砾、SMDI、钻孔和地球化学证据，对 Athabasca 边缘铀矿潜力进行筛选。

### 2026-05-08

#### [Cigar Lake 铀矿潜力筛选](./2026-05-08-geomine-cigar-lake-uranium-screening/)

- 主论文：[cigar_lake_uranium_screening_report.md](./2026-05-08-geomine-cigar-lake-uranium-screening/cigar_lake_uranium_screening_report.md)
- PDF：包含英文和中文 PDF。
- 支撑文件：包级 README、machine-readable summary 和 MCP provenance。
- 重点：以高品位 Athabasca 不整合面型铀矿床 Cigar Lake 为对象，梳理矿床模型、生产状态、地球化学、地球物理、基础设施和监管背景。

## Skill 能力与方法论文档

### 2026-05-15

#### [GeoMine Material Behavior Modeling Skill Family 设计说明](./GeoMine_Material_Behavior_Modeling_Skill_Family_Design_zh.md)

- 重点：面向机制型、工程型和数值模拟型 GeoMine 论文，说明设计目的、架构、触发条件、DGR natural analogue 选题闸门、readiness levels、THMC/PHREEQC/PFLOTRAN 衔接和实施状态。

### 2026-05-14

#### [GeoMine Research 地球化学论文架构 Skill 方法论](./GeoMine_Research_Geochemistry_Paper_Architecture_Skill_Methodology.md)

- 重点：把 GeoMine 论文写作从资料汇总型报告提升为问题驱动、数据约束、方法透明、机制解释和结论有边界的地球化学学术论文流程。

### 2026-05-13

#### [GeoMine PFLOTRAN Modeling Skill 说明文档](./GeoMine_PFLOTRAN_Modeling_Skill_Guide_zh.md)

- 重点：PFLOTRAN skill family 的设计目的、架构、能力边界、触发条件、与 THMC 的关联、MCP 设计、本地脚本、使用案例和论文写作价值。

#### [GeoMine PHREEQC Skill 能力说明文档](./GeoMine_PHREEQC_Skill_Capability_Guide.md)

- 重点：PHREEQC skill 的定位、模型类型、输入审计、数据库选择、keyword 规划、selected output、可复现性、案例和限制。

### 2026-05-12

#### [GeoMine THMC Skill Family 说明文档](./GeoMine_THMC_Skill_Family_Guide.md)

- 重点：THMC skill family 的模块定位、耦合层级、子 skill 职责、建模包输出结构、router 行为、反应网络参考、模板和验证要求。

## 推荐阅读路径

- 矿产勘查与矿权筛选：Cigar Lake、Wollaston Lake East、NWT 金矿潜力、NWT 第二阶段矿权扣减、Patterson Lake Corridor。
- 辐解与天然氢：多孔介质辐解综述、辐解辅助制氢、Revell/Athabasca 辐解天然氢、多孔介质辐解-电解前沿、Revell Batholith 地球化学框架。
- 地下水与放射性核素地球化学：Saskatchewan 铀衰变系地下水、PHREEQC U-Ra-SO4-CO3 工作流、野火/降雨驱动的核素再迁移。
- THMC 与反应运移建模：尾矿渗滤 THMC、DGR 铜-膨润土 THMC、裂隙岩核素/胶体 THMC、PFLOTRAN 尾矿铀工作流。
- GeoMine 插件方法论：THMC 指南、PHREEQC 指南、PFLOTRAN 指南、Material Behavior Modeling 设计说明、地球化学论文架构指南。

## 数据与复核边界

- 矿权和 claim 状态具有时效性。staking、并购或披露前必须复核官方省级或地区登记系统。
- 公司披露和历史报告只能作为背景证据，不能替代官方矿权检查、技术报告、QP 审查或现场验证。
- 地球化学异常不是矿化证明，必须结合样品介质、分析方法、检测限、QA/QC、搬运方向、岩性、构造和蚀变背景解释。
- PHREEQC、PFLOTRAN 和 THMC 产物如果没有现场校准，应视为科研工作流和筛选模型。
- 放射性核素、核废料、地下水和氢气相关结论，在工程、监管或安全用途前必须由合格技术团队复核。
