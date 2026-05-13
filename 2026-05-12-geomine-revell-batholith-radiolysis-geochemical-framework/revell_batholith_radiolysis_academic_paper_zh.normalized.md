# Revell Batholith 结晶岩地下水化学演化与天然辐解产氢的 THMC 安全评价接口：一项综述性概念框架研究

生成日期：2026-05-12  
文章类型：综述论文 / 概念模型论文  
研究边界：本文不评价处置库是否安全，不替代 NWMO 安全案例、CNSC 监管审查、许可申请或合格专业意见。本文只建立可解释、可量化、可进入后续模拟的地球化学框架。

## 摘要

Revell Batholith 是加拿大安大略省西北部 Wabigoon Lake Ojibway Nation-Ignace 区域的太古代花岗质结晶岩体，也是加拿大深地质处置库场址研究中的关键结晶岩系统。公开 NWMO 与独立 Geoscientific Review Group 资料显示，Revell Site 主体由约 $2.71\ \mathrm{Ga}$ 的 biotite granodiorite-tonalite 组成，六口深钻孔岩心约 $95\%$ 为近均一 granitoid host rock，并表现出低孔隙度、低渗透率、离散裂隙控制和地下水盐度随深度增加的典型 Canadian Shield 特征。场址水化学可概念化为浅部 Ca-HCO$_3$ 淡水、过渡混合水和深部 Ca-Na-Cl(-HCO$_3$) 还原盐水三个端元。公开资料指示深部 hydrogeochemical zone 约在 $600$-$650\ \mathrm{m}$ 以下形成，缺氧、还原，total dissolved sulphide 低于 $0.02\ \mathrm{mg\ L^{-1}}$ 检出限，noble gas 数据指示深部水龄超过 $1\ \mathrm{Ma}$。

本文综述 Revell Batholith 地下水化学演化、U-Th-K 放射性衰变驱动的水辐解产 H$_2$ 过程，以及 H$_2$、硫酸盐、微生物、铜容器、膨润土和核素迁移之间的 THMC 耦合路径。直接针对 Revell Batholith 的 Higgins et al. (2025) 估算，最可能的天然辐解 H$_2$ 产率约为 $1.6\ \mathrm{nmol\ m^{-3}_{rock}\ yr^{-1}}$。结合 Revell granodiorite-tonalite 平均连通孔隙度 $\phi_c \approx 0.0045$，在无扩散、无反应、无微生物消耗的保守保留假设下，该源项在 $1\ \mathrm{Myr}$ 中相当于约 $0.36\ \mathrm{mmol\ L^{-1}}$ 的孔隙水 H$_2$ 浓度增长潜力；若全部转化为封闭气相，对应压力约 $0.0009\ \mathrm{MPa}$，远小于处置深度静水压力。因此，Revell host-rock 天然辐解 H$_2$ 更合理地被视为长期氧化还原和微生物能量源项，而不是主要气体压力风险源。本文提出后续 PHREEQC、COMSOL 和 PINN 模型所需的参数体系，包括 U-Th-K 空间分布、能量沉积分配、H$_2$/oxidant G-value、孔隙水体积、硫酸盐还原速率、硫化物通量、Eh-pH 边界、膨润土扩散系数和核素分配参数。

关键词：Revell Batholith；结晶岩；地下水化学；水辐解；H$_2$；U-Th-K；硫酸盐还原；铜腐蚀；膨润土；核素迁移；THMC

## 1. 引言

低孔隙度、低渗透率的花岗质结晶岩在深地质处置库研究中具有双重角色：一方面，它通过低地下水通量、长停留时间和扩散控制限制核素迁移；另一方面，它也是一个长期水-岩-气-微生物反应系统。含 U、Th、K 矿物的放射性衰变会在孔隙水和矿物-水界面沉积能量，产生 H$_2$、H$_2$O$_2$、hydrated electron、OH radical 以及其他氧化还原活性物种。这些物种虽然产率低，但可在百万年至千万年尺度影响深部氧化还原状态、微生物代谢、硫循环、金属容器腐蚀、膨润土缓冲材料稳定性和核素迁移。

Revell Batholith 为研究这一问题提供了清晰场景。该场址公开资料显示其主体岩性近均一，孔隙度低，深部水化学分层明显，且拟议处置深度位于深部还原 hydrogeochemical zone。与富铀矿体、热液系统或高硫化物岩体不同，Revell host rock 的 U-Th-K 平均含量偏低，因此天然辐解 H$_2$ 的安全意义不在于绝对气体生成量，而在于它如何作为低通量系统中的电子供体和 redox buffer 进入 THMC 模型。

## 2. 研究问题与假设

本文提出三个研究问题：

1. Revell Batholith 地下水的主要化学特征、盐度分层、氧化还原状态和水-岩作用路径是什么？
2. 围岩 U、Th、K 衰变在长期尺度上可能产生多少 H$_2$，这些 H$_2$ 更可能被矿物反应消耗、被微生物利用，还是形成气体压力风险？
3. H$_2$、硫酸盐还原、微生物活动、铜腐蚀、膨润土演化和核素迁移如何进入处置库 THMC 安全评价体系？

对应假设为：

- H1：Revell 地下水可被解释为浅部补给淡水、过渡混合水和深部还原盐水的三端元系统。
- H2：由于 Revell granitoid host rock 平均 U-Th-K 含量较低，天然 host-rock radiolysis 的 H$_2$ 源项较小，主要影响 redox 和 microbial energy budget，而非主导 gas pressure。
- H3：H$_2$ 对长期安全评价具有双重作用：它可维持还原环境，也可在有 sulfate 和活性 sulfate-reducing bacteria 的条件下促进 sulfide formation，进而影响铜腐蚀。
- H4：Revell 安全评价中的关键不确定性不是 H$_2$ 是否存在，而是 H$_2$ 生成、扩散、矿物消耗和微生物利用之间的相对速率。

## 3. 文献综述

### 3.1 Revell 场址地质与水文地球化学

NWMO 2023 Confidence in Safety - Revell Site 报告显示，Revell Batholith 约 $40\ \mathrm{km}$ 长、$15\ \mathrm{km}$ 宽，在场址区域潜在 host rock 厚度约 $2.5$-$3.0\ \mathrm{km}$。六口深钻孔最大深度约 $1000\ \mathrm{m}$，岩心约 $95\%$ 为 granodiorite-tonalite。主体矿物组成为 $44$-$52\%$ plagioclase、$38$-$40\%$ quartz、$4$-$9\%$ biotite、$1$-$6\%$ K-feldspar 及少量副矿物。

公开资料显示，Revell 水化学随深度呈系统变化。约 $300\ \mathrm{m}$ 以内为淡水条件，约 $600$-$650\ \mathrm{m}$ 以下进入较高盐度 Ca-Na-Cl(-HCO$_3$) 深部水。深部水缺氧、还原，并且 total dissolved sulphide 低于 $0.02\ \mathrm{mg\ L^{-1}}$。这为铜容器腐蚀和核素迁移模型提供了重要背景。

### 3.2 Canadian Shield 深部结晶岩地下水类比

NWMO 2017 crystalline rock postclosure safety assessment 给出了假想 Canadian Shield crystalline setting 的参考水 CR-10：TDS 约 $11.3\ \mathrm{g\ L^{-1}}$，pH 7.0，Eh $-200\ \mathrm{mV}$，主要为 Ca-Na-Cl 型水，SO$_4^{2-}$ 约 $1000\ \mathrm{mg\ L^{-1}}$。该水样不能直接等同 Revell 现场水，但可作为 PHREEQC 和敏感性分析的初始类比。

Boumaiza et al. (2024) 对 Canadian Shield crystalline-rock groundwater 的化学与同位素特征进行了综述，支持将深部盐水解释为长期水-岩作用、扩散保留、古水混合和构造-水文边界共同作用的结果。2024 GRG 报告也指出，Revell 深部盐度来源需要更广泛讨论，不能只采用单一解释。

### 3.3 水辐解 H$_2$ 与深部微生物

Dzaugis et al. (2015, 2016) 提供了近 radionuclide-containing solids 与海底玄武岩含水层中的水辐解定量模型，说明 H$_2$ 产率需要同时考虑 radionuclide abundance、porewater volume、energy deposition 和 G-value。Sherwood Lollar et al. (2014) 和 Li et al. (2016) 则表明，Precambrian crystalline rocks 中的 radiolytic H$_2$ 和 sulfur cycling 可支持长期深部微生物生态。

对 Revell 最直接的约束来自 Higgins et al. (2025)，该研究估算低孔隙、低渗透 crystalline rocks 中天然 H$_2$ 和 sulfate 的 radiolytic production，并给出 Revell Batholith 最可能 H$_2$ 产率约 $1.6\ \mathrm{nmol\ m^{-3}_{rock}\ yr^{-1}}$。

## 4. 理论框架与模型公式

### 4.1 辐解源项

物种 $i$ 的辐解源项可写为：

$$
S_i^{\mathrm{rad}} = G_i \dot{E}_{\mathrm{abs}}
$$

其中 $S_i^{\mathrm{rad}}$ 为物种 $i$ 的生成率，单位 $\mathrm{mol\ m^{-3}\ yr^{-1}}$；$G_i$ 为辐解产额，单位 $\mathrm{mol\ J^{-1}}$；$\dot{E}_{\mathrm{abs}}$ 为水相或矿物-水界面的吸收能量率，单位 $\mathrm{J\ m^{-3}\ yr^{-1}}$。

U-Th-K 衰变能量进入水相的比例可表示为：

$$
\dot{E}_{\mathrm{abs,w}}
=
\rho_r \sum_j C_j A_j E_j f_{j,w}
$$

其中 $\rho_r$ 为岩石密度，$C_j$ 为元素或核素浓度，$A_j$ 为单位质量活度，$E_j$ 为每次衰变或衰变链有效能量，$f_{j,w}$ 为进入孔隙水或矿物-水界面的能量分配比例。对 Revell 而言，$f_{j,w}$ 是关键不确定性，因为 U 和 Th 可能集中于 zircon、apatite、monazite 等副矿物，$\alpha$ 射程、晶粒包裹关系和孔隙水接触面积都会影响实际产额。

### 4.2 H$_2$ 质量守恒

H$_2$ 在裂隙-基质系统中的守恒方程可写为：

$$
\frac{\partial(\phi S_w C_{H_2})}{\partial t}
=
\nabla \cdot (\phi S_w D_e \nabla C_{H_2})
- \nabla \cdot (\mathbf{q} C_{H_2})
+ S_{H_2}^{\mathrm{rad}}
+ S_{H_2}^{\mathrm{corr}}
- R_{\mathrm{bio}}
- R_{\mathrm{min}}
- R_{\mathrm{gas}}
$$

其中 $\phi$ 为有效孔隙度，$S_w$ 为水饱和度，$C_{H_2}$ 为溶解 H$_2$ 浓度，$D_e$ 为有效扩散系数，$\mathbf{q}$ 为 Darcy flux，$S_{H_2}^{\mathrm{corr}}$ 为工程近场腐蚀或废物相关 H$_2$ 源项，$R_{\mathrm{bio}}$、$R_{\mathrm{min}}$ 和 $R_{\mathrm{gas}}$ 分别为微生物耗氢、矿物耗氢和气液相转移。

### 4.3 硫酸盐还原

H$_2$ 驱动的 sulfate reduction 可用 Monod 型表达式近似：

$$
R_{\mathrm{SRB}}
=
k_{\mathrm{SRB}} X
\frac{C_{H_2}}{K_{H_2}+C_{H_2}}
\frac{C_{SO_4}}{K_{SO_4}+C_{SO_4}}
f(T,pH,a_w)
$$

该式不能直接给出处置库近场速率，因为高膨润土干密度、低水活度、小孔径、高盐度和温度演化会强烈限制微生物活性。其作用是明确后续实验和模型需要测定的参数。

## 5. 方法学框架

本文采用证据 lane 组织方法：

1. 场址地质与结构：NWMO Revell 场址报告、IG_BH04 WP10、GRG 2024。
2. 地下水端元与盐度分层：Revell 公开水化学描述、NWMO CR-10 类比、Canadian Shield groundwater review。
3. 辐解源项：Revell U-Th-K gamma-ray spectrometer 结果、Higgins et al. 2025、Dzaugis 等辐解模型。
4. 微生物与硫循环：Precambrian crystalline rock 深部生物圈文献。
5. 工程屏障接口：铜容器、膨润土、硫化物通量和核素迁移的 THMC 过程。

本文所有数值估算均为概念模型级别，不作为许可、安全或工程设计参数。

## 6. 机制分析

### 6.1 地下水化学演化

Revell 水化学演化可解释为：

$$
\mathrm{meteoric\ Ca-HCO_3\ water}
\rightarrow
\mathrm{transition\ mixed\ water}
\rightarrow
\mathrm{deep\ reducing\ Ca-Na-Cl(-HCO_3)\ water}
$$

浅部补给水通过裂隙系统进入岩体后，O$_2$ 被有机质、Fe(II) minerals、sulfides 和微生物消耗。随着深度增加，裂隙连通性降低，扩散和长时间水-岩作用增强，Ca、Na、Cl、Sr、Br 等离子逐渐富集，形成深部还原盐水。深部 noble gas 指示老水，说明深部系统与现代补给之间连接弱。

### 6.2 辐解产 H$_2$

IG_BH04 WP10 报告给出的 biotite granodiorite-tonalite 平均 K、U、Th 分别为 $0.28\%$、$0.53\ \mathrm{ppm}$ 和 $1.24\ \mathrm{ppm}$。这些值支持低 radiolytic source term。用 Higgins et al. (2025) 的 Revell 源项：

$$
S_{H_2}^{\mathrm{rad}}
\approx
1.6\ \mathrm{nmol\ m^{-3}_{rock}\ yr^{-1}}
$$

并取连通孔隙度 $\phi_c=0.0045$，则 $1\ \mathrm{Myr}$ 内无消耗孔隙水浓度增长潜力为：

$$
C_{H_2}^{1\ \mathrm{Myr}}
\approx
\frac{1.6 \times 10^{-9}\ \mathrm{mol\ m^{-3}_{rock}\ yr^{-1}}
\times 10^6\ \mathrm{yr}}
{0.0045\ \mathrm{m^3_{water}\ m^{-3}_{rock}}}
\approx
0.36\ \mathrm{mmol\ L^{-1}}
$$

若全部形成封闭气相，则：

$$
P_{H_2}
\approx
\frac{nRT}{V_p}
=
\frac{1.6\times10^{-3}\ \mathrm{mol}
\times 8.314\ \mathrm{J\ mol^{-1}\ K^{-1}}
\times 293\ \mathrm{K}}
{0.0045\ \mathrm{m^3}}
\approx
0.0009\ \mathrm{MPa}
$$

因此 host-rock natural radiolysis 在 Revell 场址更应作为长期 H$_2$ redox source term，而不是主要 free gas pressure source。

### 6.3 H$_2$、微生物与硫循环

H$_2$ 是深部微生物常见电子供体，可支持 methanogenesis、acetogenesis、iron reduction 和 sulfate reduction。其有利作用是维持还原环境，降低 O$_2$、H$_2$O$_2$ 和其他氧化剂的影响；潜在不利作用是当 sulfate 与活性 SRB 存在时产生 HS$^-$ 或 H$_2$S，增加铜腐蚀通量。

Revell 公开资料中 total dissolved sulphide 低于 $0.02\ \mathrm{mg\ L^{-1}}$，岩石中硫化物和硫酸盐矿物不丰富。这降低了 sulfide corrosion source term 的初始风险，但不能排除长期 sulfate reduction 作为敏感性场景，因为 sulfate 可来自地下水、膨润土孔隙水、局部硫化物氧化或辐解硫循环。

## 7. THMC 安全评价接口

Revell geochemical framework 可进入 THMC 模型的路径如下：

| THMC 模块 | 关键过程 | 输出指标 |
|---|---|---|
| Thermal | used fuel decay heat、反应速率、气体溶解度、膨润土水分迁移 | temperature field、diffusion coefficients |
| Hydrological | 低孔隙基质、DFN 裂隙、盐度密度耦合、深浅水端元混合 | Darcy flux、matrix diffusion、travel time |
| Mechanical | 原位应力、EDZ、HFFIs、裂隙孔径变化 | transmissivity change、gas pathway |
| Chemical | U-Th-K 辐解、Fe-S-C redox、sulfide corrosion、核素 speciation | Eh-pH、HS flux、Kd/speciation |
| Biological | H$_2$ 利用、sulfate reduction、methanogenesis、O$_2$ 消耗 | microbial rate、sulfide generation |

## 8. 讨论

### 8.1 为什么 H$_2$ 不能只按产率判断

H$_2$ 的长期意义取决于源项、库容、传输和消耗四者的相对大小。Revell host-rock 源项较低，但孔隙水体积也很小，因此浓度效应不能忽略。反过来，低源项意味着若考虑微生物利用、矿物反应和裂隙扩散，H$_2$ 很可能被系统缓冲，而不形成显著气压。

### 8.2 对铜容器腐蚀的双重含义

低硫化物、缺氧、还原深部地下水有利于铜容器耐久性。H$_2$ 可帮助消耗氧化剂，但也可能为 sulfate reduction 提供电子供体。因此后续安全评价应关注 $J_{HS^-}^{Cu}$，即到达铜表面的硫化物通量，而不是仅关注 bulk groundwater sulfide concentration。

### 8.3 对核素迁移的影响

还原环境通常降低 U、Np、Pu、Tc 等氧化还原敏感核素的溶解度；但高盐度会降低某些阳离子交换型核素如 Cs、Sr 的吸附。H$_2$ 通过改变 redox state、microbial metabolism、DIC/organic ligands 和 colloids 间接影响核素迁移。后续 PHREEQC 模型需同时处理 carbonate、chloride、sulfate、pH、pe 和 surface complexation。

## 9. 关键参数与后续工作

| 参数 | 符号 | 公开初值或状态 | 后续需求 |
|---|---|---:|---|
| U 浓度 | $C_U$ | IG_BH04 平均 $0.53\ \mathrm{ppm}$ | 全钻孔、岩性、副矿物尺度分布 |
| Th 浓度 | $C_{Th}$ | IG_BH04 平均 $1.24\ \mathrm{ppm}$ | 同上 |
| K 浓度 | $C_K$ | IG_BH04 平均 $0.28\%$ | 同上 |
| 连通孔隙度 | $\phi_c$ | granodiorite-tonalite 平均 $0.45\%$ | 深度/岩性分布 |
| H$_2$ 源项 | $S_{H_2}^{rad}$ | $1.6\ \mathrm{nmol\ m^{-3}_{rock}\ yr^{-1}}$ | 不确定性分布和 dose partition |
| 深部硫化物 | $C_{HS^-}$ | $<0.02\ \mathrm{mg\ L^{-1}}$ | 更低检出限和长期监测 |
| 硫酸盐还原 | $R_{\mathrm{SRB}}$ | 未公开定量 | 原位/实验速率、微生物组数据 |
| 核素吸附 | $K_d$ 或 SCM 参数 | 需元素化 | Revell rock、fracture coating、salinity sensitivity |

后续模型建议：

1. PHREEQC：建立 shallow、transition、deep 三端元，做 Eh-pH、Cl-Br、Fe-S-C 和核素 speciation。
2. COMSOL：建立 fracture-matrix dual continuum，耦合 H$_2$ 扩散、sulfate reduction、sulfide flux 和 gas-liquid partition。
3. PINN：作为 PHREEQC/COMSOL 情景集的 surrogate，用于参数敏感性和不确定性传播，不替代热力学和质量守恒约束。

## 10. 局限性

本文受以下限制约束：

- 未取得 NWMO 原始 hydrogeochemical database，Revell 场址水化学以公开汇总报告为主。
- H$_2$ 源项采用 Higgins et al. (2025) 的公开模型结果，未重新计算完整衰变链和能量沉积分配。
- CR-10 仅作为 Canadian Shield crystalline reference water 类比，不作为 Revell 现场水样。
- 微生物动力学和 sulfate reduction rate 缺乏 Revell site-specific 数据。
- 本文不评价处置库是否安全，不生成工程设计参数或许可结论。

## 11. 结论

Revell Batholith 可被理解为低孔隙度、低渗透率、裂隙控制、深部还原盐水占优的结晶岩地球化学系统。公开资料支持 shallow Ca-HCO$_3$ freshwater、transition mixed water 和 deep Ca-Na-Cl(-HCO$_3$) reducing saline water 的三端元概念模型。围岩 U-Th-K 含量较低，使天然 host-rock radiolysis H$_2$ 产率较小；在现有公开估算下，它更可能作为长期 redox/microbial source term，而不是主要 gas pressure source。H$_2$ 的长期安全意义具有双重性：它有助于维持还原环境，也可能在 sulfate 和 SRB 存在时驱动 sulfide generation。后续 THMC 安全评价应把 H$_2$ 源项、矿物缓冲、微生物反应、铜腐蚀、膨润土扩散和核素迁移统一到质量守恒和不确定性传播框架中。

## 参考文献

[1] NWMO. Confidence in Safety - Revell Site - 2023 Update. NWMO-TR-2023-07. https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/NWMO-TR-2023-07-Confidence-in-Safety---Revell-Site---2023-Update.ashx

[2] NWMO. Postclosure Safety Assessment of a Used Fuel Repository in Crystalline Rock. NWMO-TR-2017-02. https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/NWMO-TR-2017-02-Postclosure-Safety-Assessment-of-a-Used-Fuel-Repository-in-Crystalline-Rock.ashx

[3] NWMO. 2024 Report of the NWMO Adaptive Phased Management Geoscientific Review Group. https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/2024-Report-of-the-NWMO-Adaptive-Phased-Management-Geoscientific-Review-Group-GRG.ashx

[4] NWMO. WP10 Geological Integration Report for Borehole IG_BH04. APM-REP-01332-0372. https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/APM-REP-01332-0372-WP10---Geological-Integration-Report-for-Borehole-IG_BH04-2022-10.ashx

[5] CNSC. REGDOC-2.11.1, Waste Management, Volume III: Safety Case for the Disposal of Radioactive Waste, Version 2. https://www.cnsc-ccsn.gc.ca/eng/acts-and-regulations/regulatory-documents/published/html/regdoc2-11-1-vol3-ver2/index.cfm

[6] Higgins, P. M., Song, M., Warr, O., and Sherwood Lollar, B. Natural H2 and Sulfate Production via Radiolysis in Low Porosity and Permeability Crystalline Rocks. JGR Biogeosciences, 2025. https://doi.org/10.1029/2025JG008863

[7] Dzaugis, M. E., Spivack, A. J., and D'Hondt, S. A quantitative model of water radiolysis and chemical production rates near radionuclide-containing solids. Radiation Physics and Chemistry, 2015. https://doi.org/10.1016/j.radphyschem.2015.06.011

[8] Dzaugis, M. E., Spivack, A. J., and D'Hondt, S. Radiolytic Hydrogen Production in the Subseafloor Basaltic Aquifer. Frontiers in Microbiology, 2016. https://doi.org/10.3389/fmicb.2016.00076

[9] Sherwood Lollar, B., et al. Hydrogen and the sustainable high-energy low-diversity deep terrestrial biosphere. Nature, 2014. https://doi.org/10.1038/nature14017

[10] Li, L., Wing, B. A., Bui, T. H., et al. Sulfur mass-independent fractionation in subsurface fracture waters indicates a long-standing sulfur cycle in Precambrian rocks. Nature Communications, 2016. https://doi.org/10.1038/ncomms13252

[11] Boumaiza, L., Stotler, R., and Frape, S. A review of the major chemical and isotopic characteristics of groundwater in crystalline rocks of the Canadian Shield. Chemical Geology, 2024. https://doi.org/10.1016/j.chemgeo.2024.122366

## 附录 A：符号与单位

| 符号 | 含义 | 单位 |
|---|---|---|
| $S_i^{\mathrm{rad}}$ | 辐解生成率 | $\mathrm{mol\ m^{-3}\ yr^{-1}}$ |
| $G_i$ | 辐解产额 | $\mathrm{mol\ J^{-1}}$ |
| $\dot{E}_{\mathrm{abs}}$ | 吸收能量率 | $\mathrm{J\ m^{-3}\ yr^{-1}}$ |
| $\rho_r$ | 岩石密度 | $\mathrm{kg\ m^{-3}}$ |
| $\phi$ | 有效孔隙度 | dimensionless |
| $D_e$ | 有效扩散系数 | $\mathrm{m^2\ s^{-1}}$ |
| $\mathbf{q}$ | Darcy flux | $\mathrm{m\ s^{-1}}$ |
| $R_{\mathrm{SRB}}$ | 硫酸盐还原速率 | $\mathrm{mol\ m^{-3}\ s^{-1}}$ |
| $K_d$ | 分配系数 | $\mathrm{m^3\ kg^{-1}}$ 或 $\mathrm{L\ kg^{-1}}$ |

