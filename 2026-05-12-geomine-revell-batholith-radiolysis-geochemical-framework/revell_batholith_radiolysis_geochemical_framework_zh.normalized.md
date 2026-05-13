# Revell Batholith 结晶岩深地质处置库场址地下水化学演化、放射性辐解产氢及 THMC 安全评价接口综述

生成日期：2026-05-12  
工作流：GeoMine Research / Academic Paper Research Writer / Report Synthesis  
研究边界：本文不评价 Revell Batholith 处置库是否安全，也不替代 NWMO 安全案例、CNSC 监管审查、许可论证或合格专业意见。本文目标是建立可解释的深部地球化学框架，服务于后续 PHREEQC、COMSOL 或 PINN 驱动的长期模拟。

## 摘要

Revell Batholith 位于安大略省西北部 Wabigoon Lake Ojibway Nation-Ignace 区域，是加拿大核废料管理组织 NWMO 选择进入后续场址确认阶段的结晶岩候选处置区域之一。公开资料显示，该场址主体为约 2.71 Ga 的花岗闪长岩-英云闪长岩，钻孔岩心约 95% 为近均一 granitoid host rock，低孔隙度、低渗透率和随深度增强的盐度分层构成长期水文地球化学隔离的核心条件。NWMO 2023 年 Revell 信心报告给出的关键观测包括：浅部约 300 m 以内为淡水 Ca-HCO3 型水；约 600-650 m 以下进入较高盐度 Ca-Na-Cl(-HCO3) 深部水；深部水缺氧、还原，总溶解硫化物低于 0.02 mg/L 检出限；拟议处置深度约 650-800 m，当前讨论值约 750 m。

本文将 Revell Batholith 视为一个低通量、低孔隙、裂隙控制的水-岩-气-微生物系统。围岩中 U、Th、K 衰变释放的 $\alpha$、$\beta$ 和 $\gamma$ 能量可在孔隙水、裂隙水和矿物-水界面产生 H2、H2O2、OH radical、hydrated electron、氧化剂以及由硫化物/硫酸盐体系参与的 S 物种转换。直接针对 Revell Batholith 的 2025 年 JGR Biogeosciences 研究估算，最可能的天然辐解 H2 产率约为 1.6 nmol H2 $\mathrm{m}^{-3}$ rock yr^-1，远低于富 U-Th-K 或高硫化物深部系统，但在百万年尺度和低流速条件下仍可成为可解释的电子供体源项。用 Revell granodiorite-tonalite 平均连通孔隙度 0.45 vol.% 作一阶换算，若忽略扩散、反应和微生物消耗，该源项约对应 0.36 mmol/L/Myr 的孔隙水 H2 浓度增长潜力；若全部转为气相并封闭在同等孔隙体积中，1 Myr 对应气压约 0.0009 MPa，显示围岩天然辐解本身更可能是氧化还原和微生物能量源项，而不是主要气压风险源。该判断依赖 2025 年模型源项、孔隙度、有效水体积和无消耗假设，不能外推为许可结论。

综述结果表明，Revell 的关键科学问题不是单独的 H2 产量，而是 H2、硫酸盐、Fe-S 矿物、低硫化物地下水、微生物代谢、铜容器腐蚀、膨润土缓冲材料和核素迁移之间的耦合路径。H2 可通过维持还原环境、支持甲烷菌/乙酸菌/硫酸盐还原菌、消耗残余氧化剂等方式产生有利影响；也可能在有可利用硫酸盐和微生物生态位时促进硫化物生成，进而影响铜腐蚀。深部盐度升高会降低部分阳离子交换型核素的吸附，但还原状态通常降低 U、Np、Pu、Tc 等氧化还原敏感核素的溶解度和迁移性。后续定量研究需要把 U-Th-K 活度、辐射能量沉积、孔隙/裂隙水体积、H2 G-value、硫酸盐还原速率、硫化物缓冲、Fe(II)/Fe(III) 容量、微生物阈值、膨润土扩散系数和核素 Kd/表面络合参数统一进 THMC 源项模型。

关键词：Revell Batholith；结晶岩；深地质处置库；地下水化学；水辐解；H2；U-Th-K；硫酸盐还原；铜腐蚀；膨润土；核素迁移；THMC

## 1. 研究问题与归一化对象

### 1.1 研究问题

本文围绕三个问题组织综述：

1. Revell Batholith 地下水的主要化学特征、盐度分层、氧化还原状态和水-岩作用路径是什么？
2. 围岩中 U、Th、K 的长期衰变和水辐解可能产生多少 H2，这些 H2 更可能被矿物反应消耗、被微生物利用，还是形成气压风险？
3. 这些过程如何进入深地质处置库的 THMC 安全评价体系，并影响核素释放、迁移和封闭后风险判断？

### 1.2 归一化实体

| 项目 | 归一化结果 |
|---|---|
| AOI | Revell Batholith / Revell Site, WLON-Ignace area, northwestern Ontario, Canada |
| 地质省/构造背景 | Canadian Shield, Wabigoon Subprovince, Superior Province |
| 主体岩性 | biotite granodiorite-tonalite；少量 felsic dykes 与 mafic sheets，后者在 2024 GRG 文件中被进一步解释为 metamorphosed lamprophyre dykes |
| 场址尺度 | NWMO 2023 报告称 Revell Site 约 19 km2，位于 batholith 北部 |
| 深度尺度 | 拟议处置深度区间约 650-800 m；当前讨论值约 750 m |
| 地下水系统 | 浅部补给淡水、过渡混合水、深部盐水/卤水端元 |
| 关键反应组分 | H2、H2O2、O2/oxidants、SO4^2-、HS-/H2S、Fe(II)/Fe(III)、U/Th/K、Cl/Br、Ca/Na/HCO3 |
| 证据边界 | 公开 NWMO/CNSC/学术文献；未取得 NWMO 未公开原始 hydrogeochemical database |

GeoMine MCP 归一化结果保留了场址名称和默认 EPSG:4326，但没有执行权威地理编码、边界提取或空间过滤；GeoMine 当前 CDoGS/Canada geodata 工具只能生成检索计划，不能声称已实时抓取地球化学数据库。因此本文的场址事实来自公开 NWMO/CNSC/学术资料，而不是 MCP 实时数据。

## 2. 证据等级与资料来源

| 证据 lane | 主要资料 | 本文使用方式 | 证据等级 | 关键限制 |
|---|---|---|---|---|
| Revell 场址地质、水文地球化学 | NWMO 2023 Confidence in Safety - Revell Site；NWMO IG_BH04 WP10；2024 GRG report | 建立场址端元、深度分层、U-Th-K 初值和不确定性 | 高 | 公开报告为汇总性资料；原始水化学全量数据未公开 |
| 通用结晶岩处置库安全评价 | NWMO 2017 crystalline rock postclosure safety assessment | 建立 Canadian Shield 类比、CR-10 参考水、微生物/胶体/吸附边界 | 中-高 | 2017 文件为假想 crystalline setting，不能直接等同 Revell |
| 监管安全案例框架 | CNSC REGDOC-2.11.1 Vol. III v2 | 界定 safety case、FEP、模型和不确定性接口 | 高 | 监管指南不是 Revell 场址参数库 |
| Revell 辐解 H2 / sulfate | Higgins et al., 2025, JGR Biogeosciences | 作为 Revell 直接源项约束 | 高 | 模型仍依赖 U-Th-K、反应产率、孔隙结构和能量沉积假设 |
| 深部辐解与微生物生态 | Dzaugis et al. 2015/2016；Sherwood Lollar et al. 2014；Li et al. 2016；Boumaiza et al. 2024 | 建立一般机制与类比边界 | 中-高 | 来自海底玄武岩、South African/Kidd Creek/Fennoscandian/Canadian Shield 类比，需场址校准 |
| 铜-膨润土-硫化物耦合 | NWMO barrier reports；SKB/NWMO 类比；Harper et al. 2024 | 建立腐蚀和微生物源项路径 | 中 | 具体腐蚀速率需 Revell 地下水、膨润土密度、温度和微生物活性约束 |

## 3. Revell Batholith 地下水化学框架

### 3.1 岩性、孔隙和裂隙控制

NWMO 2023 报告显示 Revell Batholith 约 40 km 长、15 km 宽，在场址处估计厚度约 2.5-3.0 km，主体岩性为约 2.71 Ga 的 granodiorite-tonalite。六口深钻孔最大深度约 1000 m，约 95% 岩心为 granodiorite-tonalite。平均模型矿物组成为 44-52% plagioclase、38-40% quartz、4-9% biotite、1-6% K-feldspar 及少量副矿物。

对长期地球化学最重要的不是平均岩性本身，而是低孔隙基质与离散裂隙网络之间的分工：

- 基质：Revell granodiorite-tonalite 平均连通孔隙度约 0.45 vol.%、总孔隙度约 1.32 vol.%；amphibolite sheets 平均连通孔隙度约 0.15 vol.%、总孔隙度约 1.79 vol.%。
- 裂隙：IG_BH04 等报告显示 fracture sets、structural units 与 high fracture frequency intervals 控制潜在导水路径；2024 GRG 特别要求进一步说明 DFN 模型假设和不确定性。
- 传输：NWMO 2023 报告称，在约 750 m 深度，Revell EPM rock mass transmissivity 的中值约在 10^-13 到 10^-10 m2/s 范围，表明低地下水速度；但 fracture zones 和 HFFIs 仍是端元混合、溶质迁移和不确定性的关键。

### 3.2 水化学端元

公开资料支持将 Revell 地下水划分为三个可建模端元：

| 端元 | 深度范围 | 主控过程 | 化学特征 | 建模用途 |
|---|---:|---|---|---|
| 浅部补给水 | <约 300 m | meteoric recharge、浅部裂隙流、碳酸盐缓冲、微生物耗氧 | Fresh Ca-HCO3 型，低 Cl，较可能保留氧化信号 | 近地表边界、水文补给、未来气候扰动 |
| 过渡混合水 | 约 300-650 m | 裂隙连通性降低、扩散增强、离子交换、水岩反应、端元混合 | Cl 随深度升高，Ca-Na-HCO3-Cl 过渡，Eh 下降 | 盐度界面、红氧边界、模型校准带 |
| 深部盐水/老水 | >约 600-650 m | 长停留时间、扩散控制、有限补给、矿物缓冲 | Ca-Na-Cl(-HCO3)；缺氧、还原；深部 He/noble gas 显示 >1 Ma 水龄；硫化物低 | 处置深度背景水、腐蚀/核素迁移边界条件 |

NWMO 2023 报告强调，深部 zone 与浅部 zone 主要离子化学和同位素组成不同，没有直接连接；现有 noble gas 数据指示深部水龄超过 1 Ma。2024 GRG 则指出，Revell 深部盐度来源仍需更广泛讨论，不能只用单一机制解释。可并列考虑的盐度来源包括：

1. 长期水-岩作用与低通量环境下的溶质积累。
2. 扩散控制导致的深部保留和浅部冲刷分异。
3. 古海水、蒸发卤水、冰冻浓缩水或热液盐水的历史混合。
4. 由 fracture zones/HFFIs 引导的局部端元混合。

### 3.3 Eh-pH 与主量离子路径

Revell 公开资料给出的是趋势而非完整水化学表。为了后续建模，可使用两层证据：

第一层是 Revell site-specific observations：

- 浅部淡水条件约延伸至 300 m。
- 600-650 m 以下进入较高盐度深部 hydrogeochemical zone。
- 深部 zone 未见溶解氧，呈还原状态。
- 所有已采集地下水样的 total dissolved sulphide 低于 0.02 mg/L 检出限。
- 深部水中 Cl 随深度持续升高，反映盐度分层和低流速。

第二层是 NWMO 2017 crystalline reference case 的可比边界：

- 假想 Canadian Shield 处置深度参考水 CR-10 为 Ca-Na-Cl 型，TDS 约 11.3 g/L，pH 7.0，Eh -200 mV，SO4 约 1000 mg/L，Cl 约 6100 mg/L，Fe 约 1 mg/L。
- CR-10 不是 Revell 现场水样，但可作为初始 PHREEQC 参考水或敏感性下限/中位场景。

建议建立如下 geochemical reaction path：

```text
meteoric Ca-HCO3 recharge
  -> O2 consumption by organics, Fe(II)-minerals, sulfides and microbes
  -> calcite dissolution/precipitation + plagioclase hydrolysis + ion exchange
  -> Na/Ca/Cl enrichment and pH buffering
  -> transition-zone mixing with old Ca-Na-Cl water
  -> deep reducing Ca-Na-Cl(-HCO3) water with low sulfide and long residence time
```

### 3.4 Cl-Br、SO4、Fe-S 和 U-series 指标

后续数据整理应优先收集以下指标：

- Cl、Br、Na、Ca、Sr、Li、B、I：区分 evaporated seawater、shield brine、rock-water interaction、diffusion/mixing。
- SO4、HS-/H2S、Fe(II)、Fe(total)、S(-II)/S(VI)：约束硫酸盐还原和铜腐蚀源项。
- H2、CH4、CO2、N2、He、Ne、Ar、Kr、Xe：约束水龄、气体来源和微生物代谢。
- U、Th、K、Ra、Rn、alpha/beta/gamma dose：约束 radiolytic source term。
- pH、pe/Eh、alkalinity、DIC、DOC、acetate、formate：约束微生物可利用碳和电子受体。
- δ18O、δ2H、87Sr/86Sr、δ34S-SO4/HS、δ13C-DIC/CH4、U-series disequilibrium：识别端元、停留时间和水-岩反应路径。

## 4. U-Th-K 放射性衰变与水辐解产 H2 框架

### 4.1 Revell U-Th-K 初始约束

NWMO IG_BH04 WP10 报告基于 158 个手持 gamma-ray spectrometer 点测结果给出 biotite granodiorite-tonalite 的现场放射性元素范围：

| 元素 | 范围 | 平均值 | 解释 |
|---|---:|---:|---|
| K | 0-0.8% | 0.28% | 与 K-feldspar 相对低丰度一致 |
| U | 0-5.9 ppm | 0.53 ppm | 低 U host rock；局部副矿物仍可能造成微尺度热点 |
| Th | 0-3.5 ppm | 1.24 ppm | 低 Th host rock；需与 zircon/monazite/apatite 等副矿物分布结合 |

这些值较低，意味着 host-rock radiolysis 的体积平均源项不会很大。但在低孔隙度体系中，少量能量输入可被分配到很小的水体积中；因此需区分“每 m3 岩石产率很低”和“每 L 孔隙水浓度影响可积累”两个尺度。

### 4.2 辐解反应链

水辐解可简化为以下初级和次级过程：

```text
H2O + ionizing radiation
  -> e_aq^- + OH. + H. + H2 + H2O2 + HO2. + H3O+

e_aq^- + H. / radical recombination
  -> H2

OH. + OH.
  -> H2O2

H2O2 + Fe(II) / sulfide / mineral surfaces
  -> oxidant consumption + Fe(III)/S oxidation

H2 + SO4^2- + microbes
  -> HS-/H2S + HCO3- / biomass

H2 + CO2 + methanogens / acetogens
  -> CH4 or acetate
```

关键点是：bulk water radiolysis 的 G-value 不能直接套用到低孔隙结晶岩。孔隙限制、矿物表面 scavenging、$\alpha$ recoil range、$\gamma$ penetration、electron-hole separation、double layer、pH、salinity 和 LET 都会改变 H2、H2O2 和 radicals 的有效产率。对 Revell 这样的低孔隙度 granodiorite-tonalite，辐解更接近“矿物-水界面和微孔隙中的能量沉积问题”，而不是无限均一水体问题。

### 4.3 一阶源项估算

Higgins et al. (2025) 针对 Revell Batholith 低孔隙-低渗结晶岩估算的最可能天然 H2 产率约为：

$$
S_{H_2}^{\mathrm{rad}} \approx 1.6 \ \mathrm{nmol \ m^{-3}_{rock} \ \mathrm{yr}^{-1}}
$$

用 Revell granodiorite-tonalite 平均连通孔隙度 0.45 vol.% 作一阶换算：

$$
C_{H_2,pore}^{1 Myr}
\approx
\frac{1.6 \times 10^{-9} \ \mathrm{mol \ m^{-3}_{rock} \ \mathrm{yr}^{-1}} \times 10^{6} \ \mathrm{yr}}
{0.0045 \ \mathrm{m^{3}_{water} \ m^{-3}_{rock}}}
\approx 0.36 \ \mathrm{mmol \ L^{-1}}
$$

这个值是“无扩散、无气液分配、无矿物反应、无微生物消耗”的上限式保留估算。它与 Canadian Shield / Fennoscandian Shield 深部地下水中微摩尔到毫摩尔级 H2 报道范围在量级上可比较，但不能直接说明 Revell 现场浓度，因为实际浓度受流动、扩散、气体逸散、微生物利用和矿物耗氢共同控制。

若进一步将 1 Myr 内每 m3 岩石产生的 H2 全部作为气相封闭在 0.45 vol.% 孔隙体积中，并用理想气体估算：

$$
P_{H_2}^{1 Myr}
\approx
\frac{nRT}{V_p}
=
\frac{1.6 \times 10^{-3} \ \mathrm{mol} \times 8.314 \ \mathrm{J \ \mathrm{mol}^{-1}\,\mathrm{K}^{-1}} \times 293 \ \mathrm{K}}
{0.0045 \ \mathrm{\mathrm{m}^{3}}}
\approx 8.7 \times 10^{2} \ \mathrm{Pa}
\approx 0.0009 \ \mathrm{MPa}
$$

与 750 m 深度约数 MPa 级静水压力相比，这个一阶气压值很小。因此，在当前公开源项范围内，host-rock U-Th-K 辐解 H2 更应被视为长期氧化还原/微生物能量源项，而不是主要 gas pressure driver。气压风险若要进入 safety case，应同时包括废物容器腐蚀、钢材反应、废物辐解、封闭孔隙气体、微生物甲烷和工程封闭结构内的局部封闭条件。

### 4.4 H2 的三个去向

| 去向 | 过程 | 对 Revell 的初步判断 | 需要的量化参数 |
|---|---|---|---|
| 矿物反应消耗 | Fe(III) reduction、氧化剂还原、硫酸盐/硫化物循环、表面吸附/扩散 | 主体 granitoid 低硫；Fe-bearing biotite/chlorite/alteration minerals 可参与缓冲 | Fe(II)/Fe(III) 容量、sulfide/sulfate、surface area、rate constants |
| 微生物利用 | methanogenesis、acetogenesis、sulfate reduction、iron reduction | 深部 H2 可支持低能量生态；但 Revell 深部 sulfate、DOC、biomass 和 bentonite porewater 活性需实测 | cell counts、qPCR/metagenomics、SO4 reduction rate、H2 threshold、acetate/formate |
| 气体积累 | 溶解度饱和后形成 free gas，相对渗透率改变、局部 overpressure | Host-rock natural radiolysis 源项偏小；气压风险需与工程近场气体源项合并评估 | H2 solubility、Henry constant under salinity/pressure、gas entry pressure、relative permeability |

## 5. H2、SO4、微生物与铜-膨润土-核素迁移耦合

### 5.1 有利路径

H2 在深部结晶岩中通常是电子供体。它可能通过以下路径维持处置环境的还原性：

- 促进残余 O2、H2O2 和其他氧化剂被还原，降低氧化型核素的稳定性。
- 支持 methanogens 和 acetogens，消耗 CO2/DIC 并生成 CH4 或 acetate。
- 通过微生物或矿物反应维持低 Eh，增强 U(IV)、Pu(III/IV)、Np(IV)、Tc(IV) 等还原态的低溶解度。
- 在 fracture water 与 porewater 之间形成可扩散的还原当量。

### 5.2 不利或需约束路径

H2 也可能进入不利路径：

- 若 sulfate 供应充足并存在活跃 sulfate-reducing bacteria，H2 可驱动 SO4^2- 还原为 HS-/H2S。
- HS-/H2S 是铜腐蚀的重要腐蚀剂，低浓度长期通量也需要进入容器寿命模型。
- 微生物代谢可能改变 pH、DIC、organic ligands 和 colloids，影响核素络合和迁移。
- H2 或 CH4 局部气体形成可能降低饱和度、改变有效扩散系数和 hydraulic properties，尤其是在工程近场而非完整远场岩体中。

对 Revell 而言，NWMO 2023 报告指出 groundwater total dissolved sulphide 低于 0.02 mg/L 检出限，岩石中硫化物/硫酸盐矿物不丰富，这有助于降低铜腐蚀源项。但该结论不能替代长期硫酸盐还原速率测试，因为 sulfate 可由地下水、膨润土孔隙水、微生物、局部硫化物氧化或辐解反应提供。

### 5.3 膨润土缓冲材料接口

膨润土在 THMC 中同时是水力屏障、扩散介质、阳离子交换介质和微生物生态限制介质。H2 和 radiolysis 相关组分影响膨润土的关键路径包括：

1. 深部盐水进入膨润土后，Na/Ca 交换改变 swelling pressure 和 porewater chemistry。
2. H2 扩散进入膨润土，可作为微生物电子供体；但高干密度、低水活度和小孔径会抑制微生物活性。
3. sulfate 或 sulfide 在膨润土内扩散到铜表面，形成 corrosion flux。
4. H2O2/OH radical 等氧化剂若在近场产生，可短期影响 Fe/S/U redox speciation；远场 host-rock 源项通常较低。
5. 膨润土胶体释放受 salinity 控制；低盐水入侵更可能提升 colloid stability，高盐深部水一般抑制膨润土胶体迁移。

### 5.4 核素迁移接口

H2 和盐度对核素迁移有方向相反的影响：

- 还原性增强通常降低 U、Np、Pu、Tc 等氧化还原敏感元素的溶解度和扩散通量。
- 高 Cl、Ca、Na、ionic strength 可能降低 Cs、Sr 等阳离子交换型核素的 Kd。
- Carbonate、sulfate、chloride 和 organic ligands 可增强某些核素络合，需 PHREEQC speciation。
- Colloids 在高盐下通常较少稳定，但工程扰动、pH 变化和膨润土侵蚀可产生局部异常。

## 6. THMC 反应路径图

```text
Thermal
  used fuel decay heat
  -> rock and bentonite temperature rise
  -> reaction rates, diffusion coefficients, gas solubility, bentonite water redistribution

Hydrological
  low matrix porosity + DFN-controlled fractures
  -> shallow fresh water / transition water / deep saline water stratification
  -> slow porewater diffusion and limited advective transport at repository depth

Mechanical
  in-situ stress + excavation damage zone + HFFIs
  -> fracture aperture and transmissivity changes
  -> localized mixing, gas pathways, radionuclide transport heterogeneity

Chemical
  U-Th-K decay + water radiolysis
  -> H2 + oxidants + sulfur redox perturbations
  -> Fe-S-C redox buffering, sulfate reduction, copper corrosion flux, radionuclide speciation

Biological
  H2 + DIC/DOC + sulfate/Fe(III)
  -> methanogenesis / acetogenesis / sulfate reduction / iron reduction
  -> O2 consumption, sulfide generation, pH/DIC/ligand changes

Safety-assessment outputs
  container lifetime
  bentonite swelling and diffusivity
  radionuclide source term
  geosphere travel time
  dose/risk indicators under normal and disturbed scenarios
```

## 7. 方程注册表

### 7.1 辐解 G-value 到源项

$$
S_i^{\mathrm{rad}} = G_i \, \dot{E}_{abs}
$$

| 符号 | 含义 | 单位 |
|---|---|---|
| $S_i^rad$ | 物种 i 的辐解生成率 | $\mathrm{mol}\,\mathrm{m}^{-3}\,\mathrm{yr}^{-1}$ |
| $G_i$ | 物种 i 的辐解产额，若以 molecules/100 eV 给出需换算为 mol/J | $\mathrm{mol}\,\mathrm{J}^{-1}$ |
| $E_{\mathrm{abs}}$ dot | 水或矿物-水界面吸收的辐射能量率 | $\mathrm{J}\,\mathrm{m}^{-3}\,\mathrm{yr}^{-1}$ |

适用边界：仅在 $G_i$ 与孔隙/矿物表面条件一致时可直接使用。Revell 应区分 $\alpha$、$\beta$、$\gamma$ 与 mineral-water energy partition。

### 7.2 U-Th-K 能量释放到水相吸收

$$
\dot{E}_{abs,w} =
\rho_r \sum_j C_j A_j E_j f_{j,w}
$$

| 符号 | 含义 | 单位 |
|---|---|---|
| $\rho_r$ | 岩石密度 | $\mathrm{kg}\,\mathrm{m}^{-3}$ |
| $C_j$ | U、Th、K 的质量分数或活度换算浓度 | $\mathrm{kg}\,\mathrm{kg}^{-1}$ |
| $A_j$ | 单位质量元素或核素的活度 | $\mathrm{s}^{-1}\,\mathrm{kg}^{-1}$ |
| $E_j$ | 每次衰变或衰变链有效能量 | J decay^-1 |
| f_j,w | 进入水相/界面的能量分配比例 | dimensionless |

适用边界：f_j,w 是最大不确定性之一，取决于副矿物粒径、孔隙水分布、$\alpha$ range、裂隙表面积和矿物包裹关系。

### 7.3 H2 反应-扩散-流动守恒

$$
\frac{\partial(\phi S_w C_{H_2})}{\partial t}
=
\nabla \cdot (\phi S_w D_e \nabla C_{H_2})
- \nabla \cdot (\mathbf{q} C_{H_2})
+ S_{H_2}^{\mathrm{rad}}
+ S_{H_2}^{\mathrm{corr}}
- R_{bio}
- R_{min}
- R_{gas}
$$

| 符号 | 含义 | 单位 |
|---|---|---|
| $\phi$ | 有效孔隙度 | dimensionless |
| $S_w$ | 含水饱和度 | dimensionless |
| $C_{H_2}$ | 溶解 H2 浓度 | $\mathrm{mol}\,\mathrm{m}^{-3}$ water |
| $D_e$ | 有效扩散系数 | m2 $\mathrm{s}^{-1}$ |
| q | Darcy flux | $\mathrm{m}\,\mathrm{s}^{-1}$ |
| $S_{H_2}^rad$ | host-rock 辐解 H2 源项 | $\mathrm{mol}\,\mathrm{m}^{-3}$ rock $\mathrm{s}^{-1}$ |
| $S_{H_2}^corr$ | 容器/钢材腐蚀等工程源项 | $\mathrm{mol}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}$ |
| $R_{\mathrm{bio}}$ | 微生物耗氢 | $\mathrm{mol}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}$ |
| $R_{\mathrm{min}}$ | 矿物/氧化剂耗氢 | $\mathrm{mol}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}$ |
| $R_{\mathrm{gas}}$ | 气液相转移项 | $\mathrm{mol}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}$ |

### 7.4 硫酸盐还原和硫化物通量

$$
R_{SRB} =
k_{SRB} X
\frac{C_{H_2}}{K_{H_2}+C_{H_2}}
\frac{C_{SO4}}{K_{SO4}+C_{SO4}}
f(T,pH,a_w)
$$

$$
J_{HS^-}^{\mathrm{Cu}} = -D_{HS^-}^{\mathrm{bentonite}} \nabla C_{HS^-}
$$

适用边界：微生物动力学在高压、低孔径、高盐和高膨润土干密度条件下可能受强限制。不能用常规含水层参数直接代替处置库近场参数。

## 8. 可量化参数清单

| 参数 | 推荐符号 | Revell 公开初值/范围 | 后续需求 |
|---|---|---:|---|
| 主岩 U | $C_U$ | IG_BH04 平均 0.53 ppm | 所有钻孔、各岩性、副矿物尺度分布 |
| 主岩 Th | $C_{\mathrm{Th}}$ | IG_BH04 平均 1.24 ppm | 同上 |
| 主岩 K | $C_K$ | IG_BH04 平均 0.28% | 同上 |
| 连通孔隙度 | $\phi_c$ | granodiorite-tonalite 平均 0.45 vol.% | 深度和岩性分布、EDZ 对比 |
| 总孔隙度 | $\phi_t$ | granodiorite-tonalite 平均 1.32 vol.% | 与扩散有效孔隙度区分 |
| 深部水转变深度 | z_saline | 约 600-650 m | 各 borehole Cl/Br/同位素界面 |
| 深部水龄 | $\tau_w$ | noble gas 指示 >1 Ma | 4He、36Cl、81Kr、U-series 联合约束 |
| H2 辐解源项 | $S_{H_2}^rad$ | Higgins et al. 约 1.6 nmol $\mathrm{m}^{-3}$ rock yr^-1 | 不确定性分布、岩性分层和 dose partition |
| 硫化物浓度 | $C_{\mathrm{HS}}$ | 地下水总溶解硫化物 <0.02 mg/L 检出限 | 长期监测、低检出限、微生物培养 |
| 深部水 Eh | Eh | Revell: 还原；CR-10 类比 -200 mV | 现场 Eh、pe-pH speciation、mineral redox buffers |
| 深部水 TDS | TDS | Revell Cl 随深度升高；CR-10 11.3 g/L | 全水化学表、Cl-Br、density coupling |
| sulfate reduction rate | $R_{\mathrm{SRB}}$ | 未公开定量 | tracer incubation、metagenomics、bentonite tests |
| H2 solubility | $K_H$ | 未公开 | Revell salinity, pressure, temperature correction |
| Cu corrosion flux | $J_{\mathrm{corr}}$ | 未公开 | sulfide diffusion + copper surface kinetics |
| 核素 Kd/表面络合 | Kd_i | 需元素化 | Revell rock + fracture coating + salinity/pH sensitivity |

## 9. 后续 PHREEQC / COMSOL / PINN 建模建议

### 9.1 PHREEQC

建议先建立三个端元：

1. Shallow Ca-HCO3 water：pH 6-8，低 Cl，含 O2 初始情景。
2. Transition mixed water：用 Cl、Br、Na、Ca 和 alkalinity 混合线校准。
3. Deep Ca-Na-Cl(-HCO3) reducing water：用 Revell 数据优先；缺数据时用 CR-10 作参考敏感性，不作为现场事实。

反应模块：

- plagioclase/K-feldspar/biotite/chlorite/calcite/sulfide dissolution-precipitation。
- Fe(II)/Fe(III)、S(-II)/S(VI)、C(-IV/IV) redox pairs。
- H2、CH4、SO4、HS、H2S、H2O2、O2 的气液和水相反应。
- U、Np、Pu、Tc、I、Cs、Sr 的 speciation 与 Kd/表面络合敏感性。

### 9.2 COMSOL

建议采用 fracture-matrix dual continuum 或 DFN + matrix diffusion：

- 远场：盐度密度耦合流、热扰动、深浅水端元混合。
- 近场：容器-膨润土-裂隙边界，H2/SO4/HS 扩散和腐蚀通量。
- 源项：host-rock radiolysis 与 used-fuel/contact-water radiolysis 分离，不混作一个 H2 source。
- 输出：H2 concentration、gas saturation、HS flux to copper、Eh-pH maps、radionuclide breakthrough curves。

### 9.3 PINN / surrogate modeling

适合训练的状态变量：

```text
u = {C_H2, C_SO4, C_HS, C_Fe2, C_Fe3, pH, Eh, salinity, T, S_gas, C_RN_i}
```

可嵌入物理约束：

- 质量守恒；
- charge balance；
- redox electron balance；
- Henry law / gas-liquid equilibrium；
- diffusion-advection PDE residuals；
- Monod-type microbial kinetics；
- thermodynamic saturation index penalties。

PINN 不应替代物理模型的参数识别。更合适的角色是：在 PHREEQC/COMSOL 生成的高成本情景集上训练代理模型，做不确定性传播和敏感性排序。

## 10. 主要结论

1. Revell Batholith 可解释为低孔隙度、低渗透率、裂隙控制、盐度随深度升高的结晶岩地下水系统。浅部 Ca-HCO3 淡水、过渡混合水和深部 Ca-Na-Cl(-HCO3) 还原盐水是最自然的三端元模型。
2. 公开资料显示，Revell 深部 hydrogeochemical zone 约在 600-650 m 以下形成，拟议处置深度 650-800 m 位于该深部还原 zone 内；深部水缺氧、硫化物低，Cl 随深度升高，noble gas 指示老水。
3. IG_BH04 的 K、U、Th 平均值分别约为 0.28%、0.53 ppm、1.24 ppm，支持低天然辐解源项。Higgins et al. 2025 直接针对 Revell 的 H2 产率约为 1.6 nmol $\mathrm{m}^{-3}$ rock yr^-1。
4. 按 0.45 vol.% 连通孔隙度换算，在无消耗/无扩散保留上限下，host-rock radiolysis 可在 1 Myr 产生约 0.36 mmol/L 级孔隙水 H2 潜力；但相应封闭气压约 0.0009 MPa/Myr，说明天然围岩辐解更像 redox/microbial source term，而非主要 gas pressure risk。
5. H2 的安全意义具有双重性：它可维持还原环境、降低氧化剂并支持深部自养生态；也可能在有 sulfate 和活性 SRB 时生成 sulfide，从而影响铜容器腐蚀。
6. THMC 安全评价中应把 host-rock radiolysis、near-field waste/contact-water radiolysis、container corrosion gas、microbial gas 和 fracture/matrix transport 分开建模，再在统一质量守恒框架下耦合。
7. Revell 后续最关键的数据缺口不是“是否有 H2”，而是 H2 源项、消耗项和迁移项的相对大小：U-Th-K 空间分布、孔隙水体积、dose partition、H2/oxidant G-values、SO4 reduction rate、HS flux、Eh-pH 边界和核素 Kd。

## 11. Peer-review 式自检

| 检查项 | 结果 |
|---|---|
| 研究问题是否具体 | 是，限定为 Revell host-rock hydrogeochemistry/radiolysis/THMC interface |
| 是否过度评价安全性 | 否，明确不作安全结论 |
| 方程是否必要 | 是，用于源项、反应扩散和微生物硫酸盐还原 |
| 单位是否一致 | 一阶 H2 换算已给出 mol、m3、L、MPa 量纲 |
| 替代解释是否考虑 | 是，盐度来源和 H2 去向均列出替代路径 |
| 主要缺口 | 原始水化学表、H2 实测、微生物数据、硫酸盐还原速率、Revell 全钻孔 U-Th-K |
| 发表准备度 | 3/5：框架完整，但正式综述仍需系统下载并逐篇核对 DOI、数据表和引用页码 |

## 12. 参考资料

[R1] NWMO. Confidence in Safety - Revell Site - 2023 Update. NWMO-TR-2023-07. https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/NWMO-TR-2023-07-Confidence-in-Safety---Revell-Site---2023-Update.ashx

[R2] NWMO. Postclosure Safety Assessment of a Used Fuel Repository in Crystalline Rock. NWMO-TR-2017-02. https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/NWMO-TR-2017-02-Postclosure-Safety-Assessment-of-a-Used-Fuel-Repository-in-Crystalline-Rock.ashx

[R3] NWMO. 2024 Report of the NWMO Adaptive Phased Management Geoscientific Review Group. https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/2024-Report-of-the-NWMO-Adaptive-Phased-Management-Geoscientific-Review-Group-GRG.ashx

[R4] NWMO. WP10 Geological Integration Report for Borehole IG_BH04. APM-REP-01332-0372. https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/APM-REP-01332-0372-WP10---Geological-Integration-Report-for-Borehole-IG_BH04-2022-10.ashx

[R5] NWMO. About the Site. https://www.nwmo.ca/en/site-selection/about-the-site

[R6] NWMO. Demonstrating Safety. https://www.nwmo.ca/en/a-safe-approach/demonstrating-safety

[R7] CNSC. REGDOC-2.11.1, Waste Management, Volume III: Safety Case for the Disposal of Radioactive Waste, Version 2. https://www.cnsc-ccsn.gc.ca/eng/acts-and-regulations/regulatory-documents/published/html/regdoc2-11-1-vol3-ver2/index.cfm

[R8] Mushayandebvu, M. F., et al. Subsurface geometry and emplacement history of the Revell Batholith using 3D gravity and magnetic inversion. Applied Computing and Geosciences, 2023. https://doi.org/10.1016/j.acags.2023.100121

[R9] Villamizar, L. F., et al. Integrated geological and geophysical characterization of shallow subsurface structures in the Revell batholith and surrounding greenstone belts. Journal of Applied Geophysics, 2023. https://doi.org/10.1016/j.jappgeo.2022.104938

[R10] Higgins, P. M., Song, M., Warr, O., and Sherwood Lollar, B. Natural H2 and Sulfate Production via Radiolysis in Low Porosity and Permeability Crystalline Rocks. JGR Biogeosciences, 2025. https://doi.org/10.1029/2025JG008863

[R11] Dzaugis, M. E., Spivack, A. J., and D'Hondt, S. A quantitative model of water radiolysis and chemical production rates near radionuclide-containing solids. Radiation Physics and Chemistry, 2015. https://doi.org/10.1016/j.radphyschem.2015.06.011

[R12] Dzaugis, M. E., Spivack, A. J., and D'Hondt, S. Radiolytic Hydrogen Production in the Subseafloor Basaltic Aquifer. Frontiers in Microbiology, 2016. https://doi.org/10.3389/fmicb.2016.00076

[R13] Sherwood Lollar, B., et al. Hydrogen and the sustainable high-energy low-diversity deep terrestrial biosphere. Nature, 2014. https://doi.org/10.1038/nature14017

[R14] Li, L., Wing, B. A., Bui, T. H., et al. Sulfur mass-independent fractionation in subsurface fracture waters indicates a long-standing sulfur cycle in Precambrian rocks. Nature Communications, 2016. https://doi.org/10.1038/ncomms13252

[R15] Boumaiza, L., Stotler, R., and Frape, S. A review of the major chemical and isotopic characteristics of groundwater in crystalline rocks of the Canadian Shield. Chemical Geology, 2024. https://doi.org/10.1016/j.chemgeo.2024.122366

[R16] Harper, R., et al. Microbial growth in compacted bentonites with contrasting geological disposal facility relevant groundwaters. npj Materials Degradation, 2024. https://doi.org/10.1038/s41529-024-00540-z
