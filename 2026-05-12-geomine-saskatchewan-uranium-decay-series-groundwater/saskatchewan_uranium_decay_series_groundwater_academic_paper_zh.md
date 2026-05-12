# 加拿大萨省铀矿区地下水中 U-Ra-Rn-Po-Pb 系列核素的分布、迁移与剂量贡献：一项水文地球化学综述框架研究

生成日期：2026-05-12  
工作流：GeoMine Research / Academic writing Skill / PDF math export ready  
文章类型：综述论文 / 概念模型论文  
研究边界：本文不评价任何矿山、社区饮用水或尾矿设施是否安全，不替代 CNSC、Health Canada、Saskatchewan 监管要求、矿山许可证监测、合格专业意见或场地调查。本文目标是建立一个可解释、可量化、可扩展到 PHREEQC 和剂量模型的水文地球化学框架。

## 摘要

在铀矿区或富铀地质背景区，地下水放射性风险不能只用总铀浓度判断。$^{238}\mathrm{U}$ 和 $^{234}\mathrm{U}$ 的迁移主要受氧化还原条件、碳酸盐络合和 pH 控制；$^{226}\mathrm{Ra}$ 和 $^{228}\mathrm{Ra}$ 作为二价碱土金属，更受 Ba/Sr/Ca 竞争、硫酸盐和碳酸盐共沉淀、离子强度、黏土及 Fe-Mn 氧化物吸附控制；$^{222}\mathrm{Rn}$ 是挥发性惰性气体，更多反映含 Ra 裂隙表面、岩性、裂隙连通性、停留时间和逸散条件；$^{210}\mathrm{Pb}$ 与 $^{210}\mathrm{Po}$ 则具有强颗粒反应性和较高摄入剂量权重，适合用于长期沉积、管网尺度累积和慢性暴露评价。因此，U 高不必然意味着 Ra、Rn、Po、Pb 高，Ra 或 Rn 异常也不一定直接对应高 U 浓度。

本文围绕 Saskatchewan northern Athabasca Basin 铀矿区，综述 U-Ra-Rn-Po-Pb 系列核素在地下水、井水、矿区排水、尾矿影响水和区域环境监测中的地球化学行为。2025 年瑞典井水研究测定 $^{210}\mathrm{Po}$、$^{210}\mathrm{Pb}$、$^{226}\mathrm{Ra}$、$^{228}\mathrm{Ra}$、$^{238}\mathrm{U}$ 和 $^{234}\mathrm{U}$，显示天然放射性核素分布高度可变，并给出摄入指示剂量贡献顺序 $^{210}\mathrm{Pb} > ^{228}\mathrm{Ra} > ^{210}\mathrm{Po} > ^{226}\mathrm{Ra} > ^{234}\mathrm{U} > ^{238}\mathrm{U}$。这一外部井水案例说明，铀系衰变链核素的风险权重可以与铀质量浓度显著脱耦。

本文提出一个从铀源项、衰变链生成、地下水迁移、地球化学截留到人体剂量贡献的综合解释模型。对萨省铀矿区而言，Athabasca Basin 的高品位不整合型铀矿、砂岩-基底断裂系统、尾矿地球化学、矿区水处理和社区环境监测共同构成研究背景；但公开数据对全套 U-Ra-Rn-Po-Pb 地下水同位素链的覆盖仍不均衡。后续研究应同时测定 U 同位素、Ra 同位素、Rn、Pb/Po、Ba/Sr、SO$_4^{2-}$、DIC、Fe/Mn、DOC、Cl、TDS、Eh-pH、碱度、稳定同位素和地下水年龄指标，并用 PHREEQC 进行铀碳酸盐络合、Ra-Ba-Sr 硫酸盐共沉淀、Pb/Po 表面络合和 Rn 裂隙释放模拟。

关键词：Saskatchewan；Athabasca Basin；铀矿；地下水；$^{226}\mathrm{Ra}$；$^{222}\mathrm{Rn}$；$^{210}\mathrm{Pb}$；$^{210}\mathrm{Po}$；剂量贡献；PHREEQC；GeoMine Research

## 1. 引言

铀矿区地下水评价常以总铀、溶解铀或 U(VI) 迁移为起点，但饮用水和环境剂量并不只由铀决定。铀衰变链中的 Ra、Rn、Pb、Po 具有不同半衰期、化学形态、吸附能力、挥发性、共沉淀行为和生物剂量系数。Health Canada 2025 年发布的现行饮用水放射性参数指南将 $^{210}\mathrm{Pb}$、$^{226}\mathrm{Ra}$ 和 $^{228}\mathrm{Ra}$ 列为加拿大饮用水中最重要的自然放射性核素 MAC 对象，并给出 gross alpha 0.5 Bq/L、gross beta 1 Bq/L 的初筛值。该指南还明确说明，铀主要按化学毒性而非放射性 MAC 管理，且 radon 在饮用水中不设 MAC，原因是吸入空气中 radon 更适合直接用空气测量管理。

这意味着铀矿区地下水研究需要从单一元素浓度转向衰变链系统。若只用 U 判断风险，会遗漏三类问题：

1. $^{226}\mathrm{Ra}$ 或 $^{228}\mathrm{Ra}$ 可能在低 U 水中升高，因为 Ra 的迁移受 Ba/Sr、SO$_4^{2-}$、离子强度和吸附-解吸控制。
2. $^{222}\mathrm{Rn}$ 可由含 Ra 裂隙表面直接释放到流动地下水中，因此 Rn 异常可以是裂隙和岩性信号，而非溶解 U 信号。
3. $^{210}\mathrm{Pb}$ 和 $^{210}\mathrm{Po}$ 的剂量权重和颗粒反应性使其在长期饮用水、沉积物、管网和生物累积评价中具有独立意义。

本文以 Saskatchewan northern Athabasca Basin 铀矿区为场景，建立一个可用于综述、监测设计和反应迁移模拟的框架，而不是直接判断任何具体水源是否安全。

## 2. 研究问题与假设

本文回答三个问题：

1. 萨省铀矿区地下水中 $^{238}\mathrm{U}$、$^{234}\mathrm{U}$、$^{226}\mathrm{Ra}$、$^{228}\mathrm{Ra}$、$^{222}\mathrm{Rn}$、$^{210}\mathrm{Pb}$、$^{210}\mathrm{Po}$ 的典型赋存状态和空间差异如何解释？
2. Eh-pH、碳酸盐络合、硫酸盐、Ba/Sr 共沉淀、离子强度、Fe-Mn 氧化物吸附、裂隙发育和地下水停留时间如何控制这些核素的迁移？
3. 不同核素如何贡献饮用水摄入、矿区排水、尾矿渗滤液、吸入 radon 和长期沉积暴露的剂量评价？

对应假设为：

- H1：U、Ra、Rn、Pb、Po 之间的相关性在自然地下水中通常不稳定，相关性强弱取决于水化学端元和水-岩接触条件。
- H2：氧化型碳酸盐水更利于 U(VI) 迁移；高离子强度、Ba 缺乏或硫酸盐-重晶石体系失衡条件更可能提高 Ra 活度。
- H3：Rn 更适合作为含 Ra 裂隙表面、岩性、流动路径和停留时间的示踪指标，不宜简单等同为溶解 U 的代理。
- H4：Po/Pb 因高剂量系数、颗粒反应性和沉积累积潜力，应在长期风险框架中与 U、Ra、Rn 同时纳入。

## 3. 研究区与数据边界

### 3.1 Saskatchewan Athabasca Basin 铀矿区

Athabasca Basin 位于加拿大北部 Saskatchewan 和 Alberta，是全球最重要的高品位不整合型铀矿省之一。公开 GSC Athabasca Basin Uranium Geochemistry Database 说明，该数据库汇编了 Saskatchewan Geological Survey 数据文件和 2000-2010 年矿产评估报告中的钻芯地球化学数据，用于支持不整合型铀矿相关研究。CNSC 对 Cigar Lake 等萨省铀矿设施的 IEMP 页面说明，Cigar Lake 位于 northern Saskatchewan 的 Athabasca Basin，并要求铀矿和铀磨厂许可证持有人通过环境保护项目监测和控制核物质及有害物质释放。

Athabasca Basin 铀矿地质和环境水文地球化学有四个与本文直接相关的特点：

1. 铀源项局部极强，但地下水中的 U、Ra、Rn、Pb、Po 不会按简单衰变平衡同步迁移。
2. 砂岩、断裂、不整合面、基底岩和覆盖沉积物构成多尺度水流路径。
3. 矿区、尾矿和处理水系统会改变 SO$_4^{2-}$、Ba、Sr、Ca、Fe/Mn、pH、Eh、TDS 和胶体条件。
4. 社区环境监测多关注水、鱼、浆果、沉积物和区域累积影响；地下水全套衰变链同位素监测则需要单独设计。

### 3.2 GeoMine MCP 调用边界

本次 GeoMine Research 使用 AOI 和数据发现工具进行 source planning，但未获得可直接下载的实时地下水监测表。AOI 正规化结果为文本型 "Athabasca Basin uranium mining districts, northern Saskatchewan, Canada"，没有权威边界几何；Saskatchewan mineral data、Canada geodata 和 CDoGS survey 检索返回的是候选数据源或规划 URL，而非可分析的现场水化学数据。因此，本文将这些 MCP 结果作为数据源路线和 provenance 记录，不把它们当作实测浓度证据。

## 4. 文献综述

### 4.1 瑞典 2025 井水研究的启示

Piñero-García et al. 2025 在 *Ecotoxicology and Environmental Safety* 发表的开放获取论文系统分析瑞典井水中 $^{210}\mathrm{Po}$、$^{210}\mathrm{Pb}$、$^{226}\mathrm{Ra}$、$^{228}\mathrm{Ra}$、$^{238}\mathrm{U}$ 和 $^{234}\mathrm{U}$。该研究报告井水中 $^{238}\mathrm{U}$ decay series 存在同位素不平衡，天然放射性核素分布高度可变，摄入指示剂量主要贡献顺序为：

$$
^{210}\mathrm{Pb} > ^{228}\mathrm{Ra} > ^{210}\mathrm{Po} > ^{226}\mathrm{Ra} > ^{234}\mathrm{U} > ^{238}\mathrm{U}
$$

这对萨省研究的意义不是把瑞典浓度外推到加拿大，而是提供方法学参照：井水和裂隙水风险评价应按核素链和剂量系数组织，而不是只按 U 浓度排序。

### 4.2 加拿大饮用水放射性参数框架

Health Canada 2025 指南建立了两级评价逻辑。首先用 gross alpha 0.5 Bq/L 和 gross beta 1 Bq/L 作为筛查；若超出筛查值，再对特定核素进行分析。现行 MAC 为：

| 核素 | 当前 MAC 或参考值 | 解释 |
|---|---:|---|
| $^{210}\mathrm{Pb}$ | 2 Bq/L | 当前 MAC，基于 1 mSv/y 参考水平 |
| $^{226}\mathrm{Ra}$ | 5 Bq/L | 当前 MAC，U 衰变链 |
| $^{228}\mathrm{Ra}$ | 2 Bq/L | 当前 MAC，Th 衰变链 |
| $^{210}\mathrm{Po}$ | 1 Bq/L | Appendix C 情景参考浓度，不是常规 MAC |
| $^{222}\mathrm{Rn}$ | 2000 Bq/L | Appendix C 摄入参考浓度；主要管理路径为空气 radon |
| 总铀 | 0.02 mg/L | 化学毒性 MAC，不纳入放射性求和公式 |

指南还说明，如果多个 MAC 核素同时检出，应满足：

$$
\sum_i \frac{C_i}{\mathrm{MAC}_i} \leq 1
$$

其中 $C_i$ 是检出核素活度浓度。对本研究而言，这一公式应扩展为场景剂量框架，而不是只作为合规判断工具。

### 4.3 Saskatchewan 监测与尾矿地球化学背景

CNSC Cigar Lake IEMP 2024 结果显示，其采样计划关注 radioactive nuclear and hazardous substances，样品包括 surface water、fish、Labrador tea leaves 和 blueberries；surface water 放射性水平和 hazardous contaminants 低于相关背景或指南，并用 0.1 mSv/y screening level 作为保守比较。EARMP 则是 Saskatchewan 政府、CNSC、Cameco、Orano 组成的 industry-government partnership，目标之一是监测 Athabasca 区域 uranium mining and milling operations 下游水、沉积物、鱼、浆果和野生动物等介质的长期变化。

这些公开资料支持两点：一是萨省铀矿区已有较成熟的区域环境监测体系；二是公开监测常以 surface water、food pathways、country foods 和累积效应为主，未必提供井水或深部地下水中 U-Ra-Rn-Po-Pb 全链核素的同步数据。因此，研究框架需要补上地下水衰变链机制层。

Athabasca Basin 尾矿地球化学综述指出，该区铀矿石以 uraninite 和 pitchblende 为主，伴生 quartz、aluminosilicates、sulfide、arsenide minerals，并含 As、Se、Mo、Ni、$^{226}\mathrm{Ra}$ 等 elements of concern；尾矿常富集这些组分，长期行为取决于尾矿矿物、处理工艺、水化学和 hydrosphere 连接。

### 4.4 U-Ra-Rn-Po-Pb 脱耦的水文地球化学机制

USGS 对 groundwater radionuclides 的综述指出，U 在氧化形态下溶解度较高，在还原形态下溶解度较低，因此受 redox、pH 和 bicarbonate 控制；Rn 是 dissolved gas，虽然由 U decay 产生，但 groundwater 中 U 与 Rn 不一定同时升高；Ra 的迁移控制因素与 U 不同，高 U 和高 Ra 很少稳定重合。

USGS 对 $^{210}\mathrm{Pb}$ 和 $^{210}\mathrm{Po}$ 的 public-supply groundwater 研究进一步显示，$^{210}\mathrm{Pb}$ 可由 $^{222}\mathrm{Rn}$ decay 及 short-lived progeny 的 alpha recoil 释放，酸性水、Fe-Mn oxyhydroxide 溶解、Pb-carbonate complexing 等条件可促进 Pb 迁移；$^{210}\mathrm{Po}$ 在高 pH、还原和阳离子交换相关水化学环境中可增强迁移，而低至中性 pH 下更容易被吸附。

## 5. 理论框架与模型公式

### 5.1 衰变链与活度

本文关注的主链为：

$$
^{238}\mathrm{U}
\rightarrow
^{234}\mathrm{U}
\rightarrow
^{230}\mathrm{Th}
\rightarrow
^{226}\mathrm{Ra}
\rightarrow
^{222}\mathrm{Rn}
\rightarrow
^{210}\mathrm{Pb}
\rightarrow
^{210}\mathrm{Po}
\rightarrow
^{206}\mathrm{Pb}
$$

同时，$^{228}\mathrm{Ra}$ 属于 $^{232}\mathrm{Th}$ 衰变链，不是 $^{238}\mathrm{U}$ 的直接子体；但它与 $^{226}\mathrm{Ra}$ 具有相同元素化学行为，因此常与 Ra 风险共同评价。

任一核素 $i$ 的活度为：

$$
A_i = \lambda_i N_i
$$

其中 $A_i$ 为活度，$\lambda_i$ 为衰变常数，$N_i$ 为原子数。地下水中是否达到 secular equilibrium 取决于半衰期、母体供应、反冲释放、吸附、沉淀、扩散、流动和采样时间，而不能仅由矿石 U 含量推断。

### 5.2 反应迁移方程

溶解态核素 $i$ 的一维或三维反应迁移可抽象为：

$$
\frac{\partial(\theta C_i)}{\partial t}
=
\nabla \cdot (\theta D_{e,i}\nabla C_i)
- \nabla \cdot (\mathbf{q} C_i)
+ S_i^{\mathrm{decay}}
+ S_i^{\mathrm{recoil}}
- \lambda_i \theta C_i
- R_i^{\mathrm{sorp}}
- R_i^{\mathrm{precip}}
+ R_i^{\mathrm{desorp}}
$$

其中 $\theta$ 为含水孔隙度，$D_{e,i}$ 为有效扩散系数，$\mathbf{q}$ 为 Darcy flux，$S_i^{\mathrm{decay}}$ 为衰变生成项，$S_i^{\mathrm{recoil}}$ 为 alpha recoil 或裂隙表面释放项，$R_i^{\mathrm{sorp}}$、$R_i^{\mathrm{precip}}$ 和 $R_i^{\mathrm{desorp}}$ 分别代表吸附、沉淀和解吸过程。

### 5.3 吸附与迟滞

线性分配近似下，迁移迟滞因子为：

$$
R_i = 1 + \frac{\rho_b K_{d,i}}{\theta}
$$

其中 $\rho_b$ 为 bulk density，$K_{d,i}$ 为表观分配系数。该式适合作为初筛，但对 Ra、Pb、Po 不应长期依赖单一 $K_d$，因为它们的迁移受 pH、离子强度、Fe-Mn 氧化物、硫酸盐、碳酸盐、Ba/Sr、DOC 和胶体显著影响。

### 5.4 铀碳酸盐络合

氧化水中 U(VI) 常以 uranyl-carbonate complexes 迁移：

$$
\mathrm{UO_2^{2+}} + n\mathrm{CO_3^{2-}}
\rightleftharpoons
\mathrm{UO_2(CO_3)_n^{2-2n}}
$$

当 DIC 和 pH 升高时，U(VI)-carbonate complexing 可显著增加 U 溶解度；在还原条件下，U(IV) 以低溶解度相存在，迁移性通常下降。因此，U 高水样多反映氧化碳酸盐条件，而不是必然反映高 Ra 或高 Rn。

### 5.5 Ra-Ba-Sr 硫酸盐共沉淀

Ra 与 Ba、Sr、Ca 同属碱土金属，常通过 barite 或 Sr/Ba sulfate solid solution 被截留。可用 saturation index 表示沉淀趋势：

$$
SI_{\mathrm{barite}} = \log_{10}\left(\frac{IAP_{\mathrm{BaSO_4}}}{K_{sp,\mathrm{barite}}}\right)
$$

当 $SI_{\mathrm{barite}}>0$ 且 Ba 与 SO$_4^{2-}$ 充足时，Ra 更可能进入 $(\mathrm{Ba},\mathrm{Ra})\mathrm{SO_4}$；但在高离子强度、Ba 供应不足、竞争阳离子增强或 barite 溶解条件下，Ra 活度可升高。2025 年 crystalline rock 实验研究表明，在低总体盐度、或高 SO$_4$ 和 Ba 条件下，Ra 可被共沉淀和吸附强烈移除；这一结果直接支持在 PHREEQC 中同时模拟 sorption 和 coprecipitation。

### 5.6 Rn 裂隙释放

Rn 不是典型溶解金属，而是惰性气体。含 Ra 裂隙表面的 decay 可以把 $^{222}\mathrm{Rn}$ 直接释放到流动水中。概念质量平衡为：

$$
\frac{dC_{\mathrm{Rn}}}{dt}
=
E_{\mathrm{Rn}}\lambda_{\mathrm{Ra}}A_{\mathrm{Ra,solid}}
- \lambda_{\mathrm{Rn}}C_{\mathrm{Rn}}
- k_{\mathrm{deg}}C_{\mathrm{Rn}}
- \mathbf{v}\cdot\nabla C_{\mathrm{Rn}}
$$

其中 $E_{\mathrm{Rn}}$ 为 emanation efficiency，$A_{\mathrm{Ra,solid}}$ 为裂隙附近固相 Ra 活度，$k_{\mathrm{deg}}$ 为脱气或逸散系数。USGS fractured-rock 模型提出，$^{226}\mathrm{Ra}$ 可从岩石基质扩散到水力裂隙并在风化产物表面吸附，随后其子体 $^{222}\mathrm{Rn}$ 直接进入地下水。

### 5.7 摄入剂量与多核素求和

饮水摄入年有效剂量可表示为：

$$
E_{\mathrm{ing}}
=
\sum_i C_i^A I_w t e_i
$$

其中 $C_i^A$ 为核素活度浓度，单位 Bq/L；$I_w$ 为饮水摄入量，单位 L/day；$t$ 为暴露天数，单位 day/year；$e_i$ 为摄入剂量系数，单位 Sv/Bq。用于 Canadian drinking-water screening 时，还应采用 Health Canada 当前参考水平、消费率和核素 MAC；用于矿区或社区暴露评价时，应按目标人群、饮水来源、country food、Rn inhalation、尾矿沉积和长期沉积路径建立情景。

## 6. 机制分析

### 6.1 U：氧化碳酸盐水中的高迁移性

U 的迁移性最强条件通常是氧化、碳酸盐丰富、pH 中性至弱碱性。此时 U(VI) 形成 uranyl-carbonate complexes，过滤样中的溶解 U 可显著升高。还原条件下 U(IV) 更容易沉淀或被还原矿物截留。因而 U 浓度更多指示 Eh-pH-DIC 条件和含 U 矿物风化，不应自动转换为 Ra、Rn、Pb、Po 风险。

### 6.2 Ra：不受 redox 直接控制的二价离子

Ra 的核心特征是不像 U 那样强烈受价态控制，而像 Ba/Sr/Ca 一样作为二价碱土金属迁移。影响 Ra 的关键变量包括：

- Ba/Sr/Ca 竞争和 carrier element 供应。
- SO$_4^{2-}$ 和 CO$_3^{2-}$ 控制的低溶解度共沉淀。
- 高离子强度降低部分表面吸附、增强阳离子交换竞争。
- Fe-Mn 氧化物、黏土和有机质表面吸附。
- alpha recoil 和母体 Th/U 矿物分布。
- 地下水停留时间和流动路径。

因此，Ra 高水样可能出现在 U 不高的还原、高盐、Ba 缺乏或吸附位点受竞争的地下水中。

### 6.3 Rn：裂隙和岩性的短半衰期信号

$^{222}\mathrm{Rn}$ 半衰期约 3.82 d，适合反映近场生成和短尺度迁移。高 Rn 可能由含 Ra 裂隙表面、granite/felsic crystalline rocks、断裂密度、水岩接触面积、低脱气封闭条件和适中停留时间共同造成。由于 Rn 易逸散，采样和保存方法会显著影响结果。Rn 对健康风险的主路径通常是 outgassing 后吸入，因此矿区饮用水框架需要同时连接水样浓度和建筑室内空气 radon，而不是只按摄入剂量评价。

### 6.4 Pb/Po：颗粒反应性、沉积累积和剂量权重

$^{210}\mathrm{Pb}$ 与 $^{210}\mathrm{Po}$ 是 radon decay 后段子体，常与颗粒、有机质、Fe-Mn 氧化物、硫化物和管网沉积物发生强相互作用。USGS 研究显示，Pb-210 可由 Rn decay 的 alpha recoil 释放，并在酸性地下水或 Fe-Mn oxyhydroxide 溶解条件下增强迁移；Po-210 在高 pH、还原、Na/Cl 高和阳离子交换相关条件下可更易迁移。对萨省铀矿环境而言，Po/Pb 的意义在于：

1. 饮用水摄入剂量系数较高，低浓度也可能有剂量意义。
2. 它们可在沉积物、Fe-Mn precipitates、尾矿界面和生物介质中累积。
3. 它们可解释 U 或 Ra 不显著但长期 alpha/beta 或食物链指标异常的情景。

## 7. 水化学端元分类

本文建议把萨省铀矿区地下水和矿区水样初步分成五类端元：

| 端元 | 典型水化学 | 主要核素行为 |
|---|---|---|
| 氧化碳酸盐型 | 高 DIC、Eh 较高、pH 中性至弱碱性 | U(VI) 迁移增强，Ra 不一定同步升高 |
| 还原型 | 低 Eh、Fe/Mn 还原、可能有 DOC 或硫化物 | U 受还原截留，Ra/Pb/Po 可因吸附位点变化而变化 |
| 高硫酸盐型 | SO$_4^{2-}$ 高，可能受矿区水或尾矿影响 | 若 Ba 充足，Ra 可被 barite 共沉淀；若 Ba 受限，Ra 控制变弱 |
| 高盐度型 | TDS、Cl、Na/Ca 高，离子强度大 | 阳离子交换竞争增强，Ra 吸附可能下降 |
| 裂隙 Rn 型 | Rn 高、短停留时间或含 Ra 裂隙表面 | Rn 与 U 可脱耦，采样保存关键 |

这一分类用于解释过程，不是固定水质类别。实际应用中应结合 PCA、聚类、主离子图、Cl-Br、SO$_4$/Ba、$^{234}\mathrm{U}/^{238}\mathrm{U}$、$^{226}\mathrm{Ra}/^{238}\mathrm{U}$、$^{222}\mathrm{Rn}/^{226}\mathrm{Ra}$ 和 groundwater age tracer 共同判断。

## 8. 监测与模拟方法

### 8.1 采样设计

建议同时采集以下样品和参数：

| 类别 | 参数 |
|---|---|
| 放射性核素 | $^{238}\mathrm{U}$、$^{234}\mathrm{U}$、$^{226}\mathrm{Ra}$、$^{228}\mathrm{Ra}$、$^{222}\mathrm{Rn}$、$^{210}\mathrm{Pb}$、$^{210}\mathrm{Po}$、gross alpha、gross beta |
| 主量离子 | Ca、Mg、Na、K、Cl、SO$_4^{2-}$、HCO$_3^-$、alkalinity、TDS |
| 共沉淀控制 | Ba、Sr、SO$_4^{2-}$、Ca、barite/celestite saturation indices |
| 表面吸附控制 | Fe、Mn、Al、Si、DOC、颗粒物、浊度、胶体 |
| 现场参数 | pH、Eh、DO、temperature、specific conductance、flow cell 稳定指标 |
| 水文指标 | 水位、抽水流量、裂隙深度、screen interval、停留时间、稳定同位素 |
| 暴露路径 | 饮用水使用、处理方式、室内 radon、沉积物、鱼和 country foods |

Rn 样品必须避免扰动、气泡和开口放置；Po/Pb 应区分 filtered 与 unfiltered 样，以识别溶解态、胶体态和颗粒态贡献。

### 8.2 PHREEQC 反应路径

PHREEQC 模型至少应包括：

1. U(VI)-carbonate aqueous complexes。
2. U(IV) 还原沉淀或表面络合边界。
3. BaSO$_4$、SrSO$_4$、RaSO$_4$ 或 $(\mathrm{Ba},\mathrm{Ra})\mathrm{SO_4}$ 的共沉淀近似。
4. Pb-carbonate 和 Pb adsorption。
5. Po adsorption 到 Fe-Mn oxides、有机质或硫化物表面。
6. Rn 的生成-衰变-逸散单独质量平衡。
7. 多核素剂量求和和情景消费率。

### 8.3 统计与解释流程

建议采用下列解释序列：

1. 先按 water type 分类，不直接做 U-Ra 全样本线性相关。
2. 对每类水分别计算 $^{234}\mathrm{U}/^{238}\mathrm{U}$、$^{226}\mathrm{Ra}/^{238}\mathrm{U}$、$^{222}\mathrm{Rn}/^{226}\mathrm{Ra}$、$^{210}\mathrm{Po}/^{210}\mathrm{Pb}$。
3. 用 Ba/Sr/SO$_4$ 判断 Ra 是否受共沉淀或 carrier limitation 控制。
4. 用 Fe/Mn/DOC/颗粒态比例判断 Pb/Po 是否受表面和颗粒控制。
5. 将浓度分布转换为 dose fraction，而不是只报告浓度排名。

## 9. 证据矩阵

| 命题 | 支持证据 | 对萨省研究的含义 |
|---|---|---|
| U 高不一定 Ra 高 | USGS 指出 U 与 Ra 迁移控制因素不同，高 U 和高 Ra 很少稳定重合；Ra 受 Ba/Sr/SO$_4$、离子强度和吸附控制 | 萨省监测不能只测 U，需要同步测 Ra-226/Ra-228 和主量离子 |
| Ra 可能由 barite/celestite 共沉淀控制 | Grundl and Cape 用 PHREEQC 解释 sandstone aquifer 中 Ra 受 barite coprecipitation 控制；2025 crystalline rock 实验显示低盐或高 SO$_4$/Ba 下 Ra 可被强移除 | PHREEQC 模型必须加入 Ba/Sr/SO$_4$，否则 Ra 解释会失真 |
| Rn 与 U 可脱耦 | USGS 说明 Rn 为气体，受 U 影响但不按 U 的 redox geochemistry 同步变化；fractured-rock 模型强调裂隙表面 Ra 对 Rn 释放的重要性 | Rn 应作为裂隙-岩性-停留时间指标，采样需专门设计 |
| Pb/Po 有独立剂量意义 | 2025 瑞典井水研究中 Pb-210 和 Po-210 对指示剂量贡献高；USGS 研究强调 Pb/Po 的 geochemical mobility 条件 | 饮用水和长期风险不能省略 Pb-210/Po-210 |
| 加拿大指南优先关注 Pb-210、Ra-226、Ra-228 | Health Canada 2025 指南设立三者 MAC，并把 Po-210/Rn-222列为情景参考浓度 | 加拿大语境下应区分 MAC、参考值、gross alpha/beta 和 uranium chemical MAC |
| 萨省公开监测体系强，但地下水链式数据仍需专题化 | CNSC IEMP 和 EARMP 覆盖水、鱼、浆果、沉积物等区域介质；公开页面不等同于深部地下水全链核素数据库 | 本课题应定位为补充机制框架和监测方案设计 |

## 10. 剂量贡献框架

### 10.1 饮用水摄入

饮用水摄入评价不应只比较质量浓度，还应转换为活度浓度和 dose fraction：

$$
F_i = \frac{C_i}{G_i}
$$

其中 $G_i$ 可取 Health Canada MAC 或情景参考浓度。若采用 current Canadian framework，则 $^{210}\mathrm{Pb}$、$^{226}\mathrm{Ra}$、$^{228}\mathrm{Ra}$ 是常规 MAC 核素；$^{210}\mathrm{Po}$ 和 $^{222}\mathrm{Rn}$ 是 unique scenario 的参考核素；总 U 主要按 0.02 mg/L chemical MAC 管理。

### 10.2 Rn 吸入

Radon 的主要健康路径是吸入。水中 Rn 对室内空气的贡献取决于出水位置、通风、热水使用、搅动、点源处理和建筑条件。Health Canada 明确建议通过空气 radon 测量管理 inhalation risk，而不是由水中 Rn 简单外推室内空气风险。因此，矿区或井水研究若发现高 $^{222}\mathrm{Rn}$，应同步设计室内空气 radon 测量。

### 10.3 沉积和食物链

Po/Pb 因颗粒反应性强，可能在沉积物、Fe-Mn precipitates、水生生物和管网沉积物中累积。CNSC Cigar Lake IEMP 将 fish、Labrador tea、berries 等介质纳入 sampling plan，并对 Po-210 in fish 与 regional background 进行比较，说明 food pathway 在北部 Saskatchewan 语境中具有实际评价意义。

## 11. 综合概念模型

本文提出如下反应路径图：

$$
\mathrm{U\ source\ minerals}
\rightarrow
\mathrm{decay\ chain\ generation}
\rightarrow
\mathrm{fracture\ and\ porewater\ release}
\rightarrow
\mathrm{aqueous\ speciation}
\rightarrow
\mathrm{sorption/coprecipitation/degassing}
\rightarrow
\mathrm{drinking\ water,\ air,\ sediment,\ food\ dose}
$$

不同核素对应的主控路径如下：

| 核素 | 主控源项 | 主控迁移机制 | 主控剂量路径 |
|---|---|---|---|
| $^{238}\mathrm{U}$, $^{234}\mathrm{U}$ | U minerals、oxidation | U(VI)-carbonate complexing、redox | 化学毒性优先，放射性次要 |
| $^{226}\mathrm{Ra}$ | U chain、alpha recoil、solid Ra | Ra$^{2+}$ adsorption、barite coprecipitation、ion exchange | 饮水摄入、bone-seeking dose |
| $^{228}\mathrm{Ra}$ | Th chain | 与 Ra-226 类似，但源项来自 Th-rich phases | 饮水摄入，当前 Canadian MAC 核素 |
| $^{222}\mathrm{Rn}$ | Ra-226 decay near fractures | 溶解气体、短半衰期、逸散 | 室内空气吸入为主 |
| $^{210}\mathrm{Pb}$ | Rn decay、alpha recoil | Pb-carbonate、Fe-Mn oxide sorption、颗粒态 | 饮水摄入、沉积累积、管网释放 |
| $^{210}\mathrm{Po}$ | Pb-210 decay、surface cycling | pH/redox/speciation、有机质和 Fe-Mn 表面 | 饮水摄入、食物链、长期沉积 |

## 12. 后续可量化参数

| 参数 | 符号 | 单位 | 优先级 |
|---|---|---|---|
| 核素活度浓度 | $C_i^A$ | Bq/L | 高 |
| 总 U 质量浓度 | $C_U$ | mg/L | 高 |
| U 同位素比 | $^{234}\mathrm{U}/^{238}\mathrm{U}$ | activity ratio | 高 |
| Ra-U 活度比 | $^{226}\mathrm{Ra}/^{238}\mathrm{U}$ | activity ratio | 高 |
| Rn-Ra 比 | $^{222}\mathrm{Rn}/^{226}\mathrm{Ra}$ | activity ratio | 高 |
| Ba/Sr/Ca | $C_{\mathrm{Ba}},C_{\mathrm{Sr}},C_{\mathrm{Ca}}$ | mg/L | 高 |
| 硫酸盐 | $C_{SO_4}$ | mg/L | 高 |
| 碱度和 DIC | Alk, DIC | mg/L as CaCO$_3$, mol/L | 高 |
| Eh-pH | Eh, pH | mV, unitless | 高 |
| Fe/Mn/DOC | $C_{\mathrm{Fe}},C_{\mathrm{Mn}},C_{\mathrm{DOC}}$ | mg/L | 高 |
| 分配系数 | $K_{d,i}$ | L/kg | 中 |
| 表面络合常数 | $K_{\mathrm{surf}}$ | variable | 中 |
| Rn 逸散系数 | $k_{\mathrm{deg}}$ | day$^{-1}$ | 中 |
| 地下水年龄 | $\tau_w$ | yr | 中 |
| 饮水摄入量 | $I_w$ | L/day | 高 |
| 剂量系数 | $e_i$ | Sv/Bq | 高 |

## 13. 讨论

### 13.1 为什么不能只用 U 浓度筛选

U 是源项，但不是所有剂量路径的决定变量。U(VI) 在氧化碳酸盐水中可以高迁移，而 Ra 在这些水中可能因 BaSO$_4$ 共沉淀或吸附而降低。相反，在某些还原、高盐或离子交换环境中，U 可能低而 Ra 较高。Rn 又因挥发性、短半衰期和裂隙表面生成而与 U 进一步脱耦。Po/Pb 的颗粒反应性和剂量系数则使其风险意义不能由 U 或 Ra 简单替代。

### 13.2 监测方案的实际含义

铀矿区基线调查应把 radioactivity screening、uranium chemical monitoring 和 decay-series radionuclide monitoring 分开设计。最小组合建议为 gross alpha/beta、total U、U isotopes、Ra-226/Ra-228、Rn-222、Pb-210/Po-210、主量离子、Ba/Sr、Fe/Mn、DOC、Eh-pH、alkalinity 和 TDS。若样品用于剂量评价，还应明确过滤状态、采样深度、井结构、处理方式和实际饮用水使用。

### 13.3 对尾矿库和矿区排水的意义

尾矿和矿区处理水中 SO$_4^{2-}$、Ba、Sr、Fe/Mn、pH、Eh 和 TDS 的变化会重塑 Ra、Pb、Po 的迁移。比如硫酸盐提高不一定导致 Ra 提高；如果 Ba 充足，barite 共沉淀反而会降低溶解 Ra。Fe-Mn 沉淀可截留 Pb/Po，但还原溶解或管网扰动又可能释放。风险评价应关注状态转变，而不是单次浓度。

## 14. 局限性

1. 本文主要基于公开文献和监管资料，没有访问矿山许可证下的完整地下水监测数据库。
2. 2025 瑞典井水研究用于方法学参照，不能外推为 Saskatchewan 浓度或风险水平。
3. Health Canada 2025 指南的 1 mSv/y reference level 与 CNSC IEMP 某些筛查语境中的 0.1 mSv/y conservatism 并不完全相同，跨报告比较必须注明版本和目的。
4. Ra、Pb、Po 的 $K_d$ 和 surface complexation 参数具有强场地依赖性，不能用单一默认值替代实验或场地反演。
5. Rn 水-气转移需要现场采样和室内空气测量，不宜仅靠地下水浓度推算吸入剂量。

## 15. 结论

萨省铀矿区地下水放射性风险应被视为 U-Ra-Rn-Po-Pb 衰变链水文地球化学系统，而不是总铀浓度问题。U 的高迁移性通常反映氧化碳酸盐条件；Ra 的迁移取决于 Ba/Sr/SO$_4^{2-}$、离子强度、吸附和共沉淀；Rn 更反映含 Ra 裂隙表面、岩性和地下水流动路径；Pb/Po 则是长期剂量、沉积累积和食物链评价中的关键核素。

最重要的研究结论是：U 高不一定代表 Ra、Rn、Po、Pb 高，Ra 或 Rn 异常也不一定代表高 U。合理的监测和模型应从铀源项、衰变链生成、地下水迁移、地球化学截留和人体剂量贡献五个层次同时展开。该框架可为 Saskatchewan uranium district 的环境基线、矿区排水、尾矿库渗滤、社区井水和长期环境风险研究提供可解释的文献基础，并为 PHREEQC、反应迁移模型和剂量评价模型提供参数清单。

## 16. Peer-review 检查清单

| 检查项 | 状态 |
|---|---|
| 是否区分 $^{228}\mathrm{Ra}$ 与 U-238 chain | 已区分，$^{228}\mathrm{Ra}$ 属 Th-232 chain |
| 是否避免用 U 直接推断 Ra/Rn/Po/Pb | 已避免 |
| 是否说明 Health Canada 当前指南版本 | 已使用 2025-12-05 当前页面 |
| 是否说明 CNSC/EARMP 资料不是深部地下水全链数据库 | 已说明 |
| 是否提供公式和参数清单 | 已提供 |
| 是否避免直接安全评价结论 | 已避免 |

## 参考文献

[1] Piñero-García, F., Thomas, R., Forssell-Aronsson, E., & Isaksson, M. (2025). Comprehensive analysis of naturally occurring radionuclides in well water: Isotopic ratios, mitigation, and dose assessment. *Ecotoxicology and Environmental Safety*, 289, 117480. https://doi.org/10.1016/j.ecoenv.2024.117480

[2] Health Canada. (2025). Guidelines for Canadian drinking water quality: Radiological parameters. Published 2025-12-05. https://www.canada.ca/en/health-canada/services/publications/healthy-living/guidelines-drinking-water-quality-radiological-parameters.html

[3] Canadian Nuclear Safety Commission. Independent Environmental Monitoring Program: Cigar Lake Operation. Page modified 2025-07-28. https://www.cnsc-ccsn.gc.ca/eng/resources/maps-of-nuclear-facilities/iemp/cigar-lake/

[4] Eastern Athabasca Regional Monitoring Program. The Eastern Athabasca Regional Monitoring Program. https://www.earmp.ca/

[5] Wright, D. M., Potter, E. G., & Comeau, J-S. (2014). *Athabasca Basin uranium geochemistry database*. Geological Survey of Canada Open File 7495. https://publications.gc.ca/site/eng/9.958442/publication.html

[6] Robertson, J., Hendry, M. J., Kotzer, T., & Hughes, K. A. (2019). Geochemistry of uranium mill tailings in the Athabasca Basin, Saskatchewan, Canada: A review. *Critical Reviews in Environmental Science and Technology*, 49(14), 1237-1293. https://doi.org/10.1080/10643389.2019.1571352

[7] U.S. Geological Survey. (2019). Radionuclides in Water. https://www.usgs.gov/mission-areas/water-resources/science/radionuclides

[8] Szabo, Z., Stackelberg, P. E., & Cravotta, C. A. (2020). Occurrence and geochemistry of lead-210 and polonium-210 radionuclides in public-drinking-water supplies from principal aquifers of the United States. *Environmental Science & Technology*. https://doi.org/10.1021/acs.est.0c00192

[9] Wood, W. W., Kraemer, T. F., & Shapiro, A. (2004). Radon ($^{222}\mathrm{Rn}$) in ground water of fractured rocks: A diffusion/ion exchange model. *Ground Water*. https://doi.org/10.1111/j.1745-6584.2004.tb02624.x

[10] Grundl, T., & Cape, M. (2006). Geochemical factors controlling radium activity in a sandstone aquifer. *Ground Water*, 44(4), 518-527. https://doi.org/10.1111/j.1745-6584.2006.00162.x

[11] Fabritius, O., Li, X., Sorokina, T., Jakobsson, A.-M., Sojakka, T., & Siitari-Kauppi, M. (2025). Radium and barium sorption and precipitation on crystalline rock; experimental results and modeling development. *Journal of Radioanalytical and Nuclear Chemistry*, 334, 1417-1431. https://doi.org/10.1007/s10967-024-09966-w

[12] Zhang, T., Gregory, K., Hammack, R. W., & Vidic, R. D. (2014). Co-precipitation of radium with barium and strontium sulfate and its impact on the fate of radium during treatment of produced water from unconventional gas extraction. *Environmental Science & Technology*, 48(8), 4596-4603. https://doi.org/10.1021/es405168b

[13] International Atomic Energy Agency. (2023). *The Environmental Behaviour of Uranium*. Technical Reports Series No. 488. https://www.iaea.org/publications/14688/the-environmental-behaviour-of-uranium

