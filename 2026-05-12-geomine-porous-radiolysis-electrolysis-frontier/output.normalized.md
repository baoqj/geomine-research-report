# 多孔介质水辐解增强制氢的机理边界与工程可行性

发布日期：2026-05-12  
研究框架：GeoMine Research / radiation chemistry / porous-media geochemistry / hydrogen engineering  
引用格式：正文采用 APA author-year 体例；参考文献列于文末。  
研究边界：本文为科研开题与机理论证，不构成核设施设计、辐射源设计、核废料处置安全审查、工业投资建议或工程放大结论。

## 摘要

本文重新开题讨论一个跨学科问题：能否利用核辐射、多孔半导体与粘土材料，提高水分解制氢效能。报告参考本地文献综合文件 `plugins/report/Sci-Bot_ 关于多孔介质中的辐射分解.pdf` 的思路，但将其扩展为辐射化学、孔隙限域、界面能带、电场分离、电化学与氢能工程的统一模型。核心判断是：多孔介质确实可以使若干辐解产物的表观 G 值高于本体水，尤其是 $e_{\mathrm{aq}}^-$、$H_2$ 与 $H_2O_2$；增强机制包括氧化物向孔隙水的电子/激子能量转移、纳米孔隔室效应、界面电双层与内建电场导致的电子-空穴分离，以及反向复合反应被几何隔离抑制。受限水中的 $G(H_2)$ 可由本体低 LET 水辐解的约 $0.047\,\mu\mathrm{mol}\,\mathrm{J}^{-1}$ 增至水饱和纳米孔中的约 $(3.0 \pm 0.5)\times 10^{-7} \mathrm{mol}\,\mathrm{J}^{-1}$，即约 6-7 倍；在少量吸附水层中，文献报告的表观产率可进一步升高，但该数值不代表工业水流量下的连续能效。

从能量守恒看，若辐射能需要用电力主动制造，辐解水不是常规电解水的高效替代路线。本体水 $G(H_2) = 0.45 \mathrm{molecule} / 100\,\mathrm{eV}$ 对应约 $2978\,\mathrm{kWh}\,\mathrm{kg}^{-1} H_2$ 的吸收辐射能；即使取水饱和多孔硅的 $G(H_2) \sim 2.9 \mathrm{molecule} / 100\,\mathrm{eV}$，仍需约 $462\,\mathrm{kWh}\,\mathrm{kg}^{-1} H_2$ 的吸收辐射能，显著高于现代电解槽约 $50\,\mathrm{kWh}\,\mathrm{kg}^{-1} H_2$ 的工程量级。只有在极薄吸附水层、废辐射场或核废料近场等“辐射能本来就会被屏蔽耗散”的场景下，辐解-电解耦合才可能作为能量回收、腐蚀控制、气体安全、地下水长期演化或特殊氢气副产技术路线继续研究。粘土材料的合理定位不是单独作为高效半导体，而是作为高比表面积、强电双层、离子交换、限域水和半导体/电催化活性相的复合载体。

## 关键词

水辐解；多孔介质；G 值；溶剂化电子；纳米孔；界面电场；粘土矿物；半导体；核废料处置；天然氢；电解水；能量守恒

## 1. 研究问题与核心判断

本文围绕六个研究问题展开：

| 编号 | 研究问题 | 本文判断 |
|---|---|---|
| RQ1 | 多孔介质是否会改变水辐解 G 值？ | 会。改变幅度取决于孔径、含水量、固体相能带、表面电荷、剂量率、pH、溶解氧和金属/氧化物表面。 |
| RQ2 | 为什么多孔介质中 $e_{\mathrm{aq}}^-$、$H_2$、$H_2O_2$ 可升高？ | 主要来自电子从固体相进入水相、纳米孔隔室降低复合、$H_2 + •OH$ 等反向反应受抑制，以及 $•OH + •OH$ 生成 $H_2O_2$ 的氧化端配对增强。 |
| RQ3 | 电场一定会提高自由基或 H2 产额吗？ | 不一定。电场可提高电子逃逸和电荷分离，但若电子被金属、缺陷、溶解氧或金属离子捕获，$H_2$ 产率可能下降，$•OH$ 或腐蚀性氧化剂反而升高。 |
| RQ4 | 多孔半导体/粘土能否显著提升电解水工业效率？ | 作为主能源路线不成立；作为辐射辅助、电极界面调控、废辐射能回收或核废料近场化学控制方向值得研究。 |
| RQ5 | 何时可以说“多孔介质优于本体水”？ | 只在同一吸收能量口径、同一剂量率、同一含水量、同一气液收集条件下比较。表观 G 值不能直接等同于系统总效率。 |
| RQ6 | 对地球化学和核废料处置有何意义？ | 意义很大。多孔岩石、膨润土、氧化物、金属容器和地下水界面会改变 $H_2$、$H_2O_2$、`O2`、还原性电子和氧化性自由基，从而影响微生物能量、腐蚀、气体压力、U/Tc/Se/I 等核素迁移和长期氧化还原状态。 |

核心判断可以压缩为一句话：

```text
多孔介质能够提高局部或表观辐解产额，但不能绕过能量守恒；它的科研价值主要在 G 值调控、界面反应、废辐射回收和长期地下水-核废料化学，而不是短期替代常规电解水制氢。
```

## 2. 方法、证据车道与 provenance

### 2.1 研究方法

本报告采用 GeoMine evidence lanes 的结构化方法，但研究对象是概念 AOI，而非单一矿权或地理多边形。概念 AOI 定义为：

```text
多孔介质中的水辐解系统，包括加拿大地盾结晶岩裂隙水、膨润土/粘土工程屏障、氧化物/半导体纳米孔、金属容器界面、核废料处置库地下水和深部地质氢气系统。
```

研究方法包括：

- 文献综述：优先采用辐射化学、孔隙水、纳米孔、氧化物界面、深部地球化学和氢能工程的同行评议文献。
- 机理推导：从 G 值定义、吸收剂量、Nernst-Planck 输运、Poisson 电势、Onsager 复合、表面通量和能带关系推导控制方程。
- 定量核算：统一换算 $\mu\mathrm{mol}\,\mathrm{J}^{-1}$、$\mathrm{molecule} / 100\,\mathrm{eV}$、$\mathrm{kWh}\,\mathrm{kg}^{-1} H_2$、$\mathrm{kg} H_2 \mathrm{yr}^{-1}\,\mathrm{MW}_{\mathrm{abs}}^{-1}$。
- 工程筛选：将自然放射性、废辐射、电子束/γ 源、核废料近场和电解槽辅助路线分开评价。
- 边界条件审查：明确剂量率、孔径、pH、含氧状态、材料电导率和表面类型对结论的限制。

### 2.2 证据矩阵

| Evidence lane | 主要证据 | 结论用途 | provenance 与限制 |
|---|---|---|---|
| 本体水辐解基准 | 低 LET γ/电子在 pH 3-11 下 $G(e_{aq}^{-}) \sim 0.28\,\mu\mathrm{mol}\,\mathrm{J}^{-1}$、$G(•OH) \sim 0.28\,\mu\mathrm{mol}\,\mathrm{J}^{-1}$、$G(H_2) \sim 0.047\,\mu\mathrm{mol}\,\mathrm{J}^{-1}$、$G(H_2O_2) \sim 0.073\,\mu\mathrm{mol}\,\mathrm{J}^{-1}$ (Le Caër, 2011) | 建立本体水对照组 | 取自综述表格；不同 LET、pH、温度和溶质会改变数值。 |
| 纳米孔/硅氧化物 | 多孔硅、controlled pore glass 和 MCM-41 中 $H_2$ 产率高于本体水，且反向 $H_2 + •OH$ 反应被抑制 (Rotureau et al., 2005; Foley et al., 2007) | 解释多孔介质 $H_2/H_2O_2$ 增强 | 需要核对吸收能量口径是水相还是固体+水整体。 |
| Monte Carlo 模拟 | 多孔 silica 中低能电子可跨界面进入水，相对导带边 `Delta U` 控制电子收集，孔径小于约 100 nm 时 $e_{\mathrm{aq}}^-$ 增强明显 (Ouerdane et al., 2010) | 解释 $e_{\mathrm{aq}}^-$ 增强和电子收集 | 模拟关注 ps 前的物理化学阶段，需与后续反应-扩散耦合。 |
| 纳米管/粘土类材料 | imogolite 类铝硅酸盐纳米管存在曲率诱导电荷分离，电子向外、空穴向内迁移 (Pignié et al., 2021) | 连接粘土/纳米孔与内建电场 | imogolite 是特殊纳米管，不应直接外推到普通膨润土或高岭石。 |
| 金属表面 | 不锈钢、Hastelloy、金等表面会改变 $•OH$ 和 $e_{\mathrm{aq}}^-$，金属可捕获预溶剂化电子并增强局部氧化剂 (Le Caër et al., 2014) | 解释容器腐蚀和电子损失 | 表面状态、氧化膜、粗糙度和杂质对结果敏感。 |
| 深部地球化学 | U-Th-K 衰变可长期产生 radiolytic H2，H2 可供给深部微生物或改变地下水氧化还原状态 (Lin et al., 2005; Blair et al., 2007; Dzaugis et al., 2016; Higgins et al., 2025) | 服务天然氢、核废料库和地下水长期演化 | 地质通量通常很低，资源意义与安全意义必须分开。 |
| 氢能工程 | 2025 年 IEA 报告显示低排放氢仍受成本、FID、需求和基础设施约束；全球水电解装机仍处于早期扩张阶段 (IEA, 2025) | 约束产业化判断 | 成本随地区、电价、政策和供应链变化，本文只作框架模型。 |

## 3. 文献综述

### 3.1 本体水辐解的经典框架

水辐解不是单一反应，而是由物理阶段、物理化学阶段和化学阶段组成的多尺度过程。电离辐射首先在飞秒尺度沉积能量，产生电离水、激发水和低能电子；随后电子热化与溶剂化，形成 $e_{\mathrm{aq}}^-$；最后在皮秒至微秒尺度，自由基扩散、复合、被溶质捕获或转化为 $H_2$、$H_2O_2$ 等较长寿命产物 (Le Caër, 2011)。

本体水的低 LET 基准值可写为：

| 物种 | 典型逃逸产额 $G_i$ in $\mu\mathrm{mol}\,\mathrm{J}^{-1}$ | 换算为 $\mathrm{molecule} / 100\,\mathrm{eV}$ | 主要角色 |
|---|---:|---:|---|
| $e_{\mathrm{aq}}^-$ | 0.28 | 2.70 | 强还原剂，决定还原端化学 |
| $•OH$ | 0.28 | 2.70 | 强氧化剂，决定腐蚀和有机氧化 |
| $H•$ | 0.06 | 0.58 | H2 前体和还原性自由基 |
| $H_2$ | 0.047 | 0.45 | 长寿命还原性分子产物 |
| $H_2O_2$ | 0.073 | 0.70 | 长寿命氧化剂，腐蚀关键物种 |

这些值不是常数，而是随 LET、pH、温度、盐度、溶解氧、自由基捕获剂和气液边界变化 (Le Caër, 2011; Buxton et al., 1988)。

### 3.2 多孔 silica 与受限水

Rotureau 等对 controlled pore glass 和 MCM-41 中的受限水进行了实验研究，发现水饱和纳米孔中 $G(H_2)$ 可达到约 $(3.0 \pm 0.5)\times 10^{-7} \mathrm{mol}\,\mathrm{J}^{-1}$，按总吸收能量计约为本体水 $H_2$ 产额的 6-7 倍 (Rotureau et al., 2005)。该研究还指出，羟基自由基捕获剂并不显著改变 $H_2$ 产率，说明受限孔隙中 $H_2 + •OH \to H_2O + H•$ 这类反向链反应被几何隔离削弱。

Foley 等进一步研究 hydrated nanoporous glasses 中的 $H_2O_2$，发现低剂量率 γ 辐照下 $H_2O_2$ 同样增强，且与 $H_2$ 一样体现 silica 向受限水的能量转移；但在 10 MeV 高剂量率电子束下，能量转移被削弱，$H_2O_2$ 产率接近本体水 (Foley et al., 2007)。这说明剂量率不是细节变量，而是控制“界面能量转移是否有效”的关键条件。

### 3.3 电子收集、导带边与 Monte Carlo 模拟

Ouerdane 等用 event-by-event Monte Carlo 模拟研究 silica 圆柱孔中的水辐解，指出固体和水的相对导带边控制低能电子跨界面转移。由于水相相对于 silica 可作为低能电子收集相，孔径较小时固体中产生的电子可进入水相并溶剂化，从而提高 $e_{\mathrm{aq}}^-$ 初级产额 (Ouerdane et al., 2010)。这一路径与传统“水吸收能量后直接辐解”不同，它本质上是：

```text
solid absorbs radiation -> electronic excitation / low-energy electrons -> interface transfer -> water traps electrons -> e_aq^- increases
```

因此，在多孔体系中讨论 G 值时必须明确吸收能量口径。如果把固体和水的总吸收能量作为分母，增强值是系统表观 G 值；如果只把水相吸收能量作为分母，得到的数值会更高，但工程含义不同。

### 3.4 粘土与纳米管材料

普通粘土矿物如膨润土、蒙脱石和高岭石通常不是高迁移率半导体。它们更常见的功能是吸附、离子交换、形成电双层、保持孔隙水、提供纳米限域和分散负载活性相。imogolite 这类铝硅酸盐纳米管则是重要例外：其高曲率结构可产生内建极化和电子-空穴分离。Pignié 等的 pulse radiolysis 实验证明，铝硅酸盐纳米管中电子倾向于向外表面迁移，空穴向内表面迁移，从而影响水分子、准自由电子、溶剂化电子和 $H_2$ 的形成 (Pignié et al., 2021)。

这给粘土路线提供了一个严谨定位：

```text
粘土不是高效“辐射电解水半导体”的默认答案；
粘土-氧化物-半导体-电催化剂复合孔道，才是合理研究对象。
```

### 3.5 金属表面与核废料容器化学

金属表面对辐解的作用与氧化物不同。金属的费米能级、表面氧化膜、粗糙度和缺陷位点可捕获预溶剂化电子，使水相 $e_{\mathrm{aq}}^-$ 降低；同时，金属或金属氧化膜可活化 $H_2O_2$，增强 $•OH$ 或其他氧化性中间体 (Le Caër et al., 2014)。这对核废料处置库和反应堆腐蚀很关键，因为金属容器附近的辐解化学可能表现为：

```text
还原端电子被金属短路或捕获；
氧化端 H2O2 / •OH 局部增强；
腐蚀速率和钝化膜稳定性改变。
```

### 3.6 深部地质氢气与核废料处置

U、Th、K 的天然衰变可以在深部地下水中持续产生 radiolytic H2。Lin 等在深部地质环境中研究 radiolytic H2 的产率和同位素特征，指出 H2 可作为深部生物圈能量源 (Lin et al., 2005)。Blair 等将该思想扩展到深海沉积物，比较 U-Th-K、孔隙度和沉积物呼吸强度，认为在有机碳贫乏环境中辐解 H2 的相对重要性上升 (Blair et al., 2007)。Dzaugis 等研究 subseafloor basaltic aquifer，强调孔隙结构、岩石组成和放射性元素对 H2 通量的控制 (Dzaugis et al., 2016)。Higgins 等在 Revell Batholith 低孔低渗结晶岩中使用 Monte Carlo 框架估算 H2 和 sulfate 产生，说明低孔隙率会显著限制 H2 生产，即使长期安全意义仍然重要 (Higgins et al., 2025)。

## 4. 反应机理：从初级产物到长寿命产物

### 4.1 初级过程

水辐解可概括为：

$$
\mathrm{H_2O}
\xrightarrow{\mathrm{ionizing\ radiation}}
e_{aq}^{-} + \mathrm{\cdot OH} + \mathrm{H\cdot}
+ \mathrm{H_3O^{+}} + \mathrm{OH^{-}}
+ \mathrm{H_2} + \mathrm{H_2O_2}
$$

其中：

- $e_{\mathrm{aq}}^-$：溶剂化电子，标准还原电势很负，是强还原性物种。
- $•OH$：羟基自由基，是强氧化性物种。
- $H•$：氢原子自由基，可参与 $H_2$ 生成。
- $H_2$：还原性长寿命分子产物。
- $H_2O_2$：氧化性长寿命分子产物，控制腐蚀和氧化还原演化。

### 4.2 主要二级反应网络

| 反应 | 作用 | 对 $H_2$ / $H_2O_2$ 的影响 |
|---|---|---|
| $e_{\mathrm{aq}}^- + e_{\mathrm{aq}}^- + 2H2O \to H_2 + 2OH^-$ | 还原端复合产氢 | 增加 $H_2$ |
| $e_{\mathrm{aq}}^- + H• + H_2O \to H_2 + OH^-$ | 电子与氢自由基产氢 | 增加 $H_2$ |
| $H• + H• \to H_2$ | 氢自由基复合 | 增加 $H_2$ |
| $•OH + •OH \to H_2O_2$ | 氧化端自由基复合 | 增加 $H_2O_2$ |
| $e_{\mathrm{aq}}^- + •OH \to OH^-$ | 还原端和氧化端互相湮灭 | 降低自由基逃逸产额 |
| $e_{\mathrm{aq}}^- + H3O+ \to H• + H_2O$ | 酸性条件下电子转化 | 降低 $e_{\mathrm{aq}}^-$，增加 $H•$ |
| $H_2 + •OH \to H_2O + H•$ | 反向链反应 | 消耗 $H_2$ |
| $H_2O_2 + e_{\mathrm{aq}}^- \to •OH + OH^-$ | 过氧化氢还原活化 | 可增加 $•OH$ |
| $H_2O_2 + metal surface \to •OH / O2 / surface oxides$ | 金属表面催化 | 增强腐蚀性氧化剂或消耗 $H_2O_2$ |

本体水中，辐解产物在同一 spur 或 track 中空间距离近，复合概率高。多孔介质中，孔壁和孔喉可把初级产物分配到不同隔室，使某些反向反应失效或变慢。这是 $H_2$ 与 $H_2O_2$ 同时升高的关键。

## 5. G 值定义、换算与源项

### 5.1 G 值定义

令 $G_i^{(100\mathrm{eV})}$ 表示每吸收 $100\,\mathrm{eV}$ 能量产生的第 `i` 个物种分子数：

$$
G_i^{(100\mathrm{eV})}
=
\frac{N_i}{E_{\mathrm{abs}}/(100\ \mathrm{eV})}
$$

其中：

- $N_i$：第 `i` 个物种的分子数，单位 $\mathrm{molecule}$。
- $E_{\mathrm{abs}}$：体系吸收的辐射能，单位 $\mathrm{eV}$ 或 $\mathrm{J}$。
- $100\,\mathrm{eV} = 1.602176634\times 10^{-17} J$。

若用摩尔产率 $Y_i$ 表示：

$$
Y_i
=
G_i^{(100\mathrm{eV})}
\frac{1}{(100\mathrm{eV})N_A}
=
1.03643\times 10^{-7} G_i^{(100\mathrm{eV})}
\quad [\mathrm{mol\ \mathrm{J}^{-1}}]
$$

其中 $N_A = 6.02214076\times 10^{23} \mathrm{mol}^{-1}$。

若文献用 $\mu\mathrm{mol}\,\mathrm{J}^{-1}$ 表示：

$$
G_i^{(100\mathrm{eV})}
=
9.64853\ G_i^{(\mu \mathrm{mol}\ \mathrm{J}^{-1})}
$$

### 5.2 吸收剂量率到源项

若孔隙水密度为 $\rho_w$，孔隙水吸收剂量率为 $\dot{D}_w$，则单位孔隙水体积内的辐解源项为：

$$
S_i^{\mathrm{rad}}
=
\rho_w \dot{D}_w
\left(1.03643\times 10^{-7}\right)
G_i^{(100\mathrm{eV})}
$$

其中：

- $S_i^{\mathrm{rad}}$：第 `i` 个物种的辐解生成源项，单位 $\mathrm{mol}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}$。
- $\rho_w$：孔隙水密度，单位 $\mathrm{kg}\,\mathrm{m}^{-3}$。
- $\dot{D}_w$：孔隙水吸收剂量率，单位 $\mathrm{Gy}\,\mathrm{s}^{-1} = \mathrm{J}\,\mathrm{kg}^{-1}\,\mathrm{s}^{-1}$。
- $G_i^{(100\mathrm{eV})}$：每 $100\,\mathrm{eV}$ 的分子产额。

对多孔介质，若辐射能主要吸收在固体相而产物在水相形成，应拆分为：

$$
S_i^{\mathrm{rad}}
=
\rho_w \dot{D}_w \alpha_i^w
+ \rho_s \dot{D}_s \eta_{s \to w,i}
$$

其中：

- $\rho_s$：固体密度，单位 $\mathrm{kg}\,\mathrm{m}^{-3}$。
- $\dot{D}_s$：固体相吸收剂量率，单位 $\mathrm{Gy}\,\mathrm{s}^{-1}$。
- $\alpha_i^w = 1.03643\times 10^{-7} G_{i,w}^{(100\mathrm{eV})}$。
- $\eta_{s \to w,i}$：固体相吸收能转移并最终在水相形成物种 `i` 的有效摩尔产率，单位 $\mathrm{mol}\,\mathrm{J}^{-1}$。

该式是多孔介质辐解的关键：增强的 G 值常常来自固体相吸收能向水相化学产物的转移。

## 6. 多孔介质中的反应-输运-电场方程

### 6.1 Nernst-Planck 反应输运方程

对孔隙水中物种 `i`，定义：

- $\epsilon$：孔隙率。
- $\tau$：曲折度。
- `c_i`：物种 `i` 的浓度，单位 $\mathrm{mol}\,\mathrm{m}^{-3}$。
- $D_i$：自由水扩散系数，单位 $\mathrm{m}^{2}\,\mathrm{s}^{-1}$。
- $D_{eff,i} = \epsilon D_i / \tau$：有效扩散系数。
- `z_i`：电荷数。
- $\mathrm{F}$：Faraday 常数。
- `R`：气体常数。
- `T`：温度，单位 $\mathrm{K}$。
- $\Phi$：电势，单位 $\mathrm{V}$。
- `a_s`：单位孔隙体积固液界面面积，单位 $\mathrm{m}^{2}\,\mathrm{m}^{-3}$。
- $J_{i,s}$：表面捕获、吸附或催化通量，单位 $\mathrm{mol}\,\mathrm{m}^{-2}\,\mathrm{s}^{-1}$。

控制方程为：

$$
\frac{\partial(\epsilon c_i)}{\partial t}
=
-\nabla \cdot \mathbf{N}_i
+ \epsilon S_i^{\mathrm{rad}}
+ \epsilon \sum_j \nu_{ij} R_j
- a_s J_{i,s}
$$

通量为：

$$
\mathbf{N}_i
=
-D_{eff,i}\nabla c_i
-D_{eff,i}\frac{z_i F}{RT}c_i\nabla \Phi
+ \epsilon c_i \mathbf{v}
$$

其中 `mathbf{v}` 是孔隙水速度。对密闭核废料库近场或低渗结晶岩，许多微尺度模型可令 $mathbf{v} \sim 0$，此时扩散和电迁移占主导。

### 6.2 电势与电双层

电场为：

$$
\mathbf{E} = -\nabla \Phi
$$

孔隙水中电势满足 Poisson 方程：

$$
-\nabla \cdot (\epsilon_e \nabla \Phi)
=
F\sum_i z_i c_i + \rho_f
$$

其中：

- $\epsilon_e$：有效介电常数，单位 $\mathrm{F}\,\mathrm{m}^{-1}$。
- $\rho_f$：孔壁固定电荷等效体电荷密度，单位 $\mathrm{C}\,\mathrm{m}^{-3}$。

Debye 长度为：

$$
\lambda_D
=
\left(
\frac{\epsilon_r \epsilon_0 RT}
{2F^{2} I}
\right)^{1/2}
$$

其中 `I` 是离子强度。若孔径 `d_p` 与 `2 lambda_D` 同量级，电双层重叠，整个孔内都处于显著电势梯度中。低离子强度纳米孔和干湿交替的吸附水层最容易出现这种状态；高盐地下水会强烈屏蔽外加电场。

### 6.3 表面边界通量

孔壁对电子、自由基和分子产物的影响可写为：

$$
J_{i,s}
=
k_{i,s} c_i
- k_{des,i}\Gamma_i
+ J_{i,s}^{\mathrm{cat}}
+ J_{i,s}^{\mathrm{ET}}
$$

其中：

- $k_{i,s}$：物种 `i` 的表面捕获速率常数，单位 $\mathrm{m}\,\mathrm{s}^{-1}$。
- $\Gamma_i$：表面吸附量，单位 $\mathrm{mol}\,\mathrm{m}^{-2}$。
- $k_{des,i}$：解吸速率常数，单位 $\mathrm{s}^{-1}$。
- $J_{i,s}^{\mathrm{cat}}$：表面催化反应通量。
- $J_{i,s}^{\mathrm{ET}}$：界面电子转移通量。

金属表面的 $J_{e,s}$ 通常较大，会降低水相可测 $e_{\mathrm{aq}}^-$；氧化物和半导体表面可能既提供电子转移，也可能捕获电子或空穴。

## 7. 电场、Onsager 复合与孔隙限域

### 7.1 Onsager 半径

带相反电荷的电子-阳离子对在水中受到 Coulomb 吸引。Onsager 半径定义为 Coulomb 能等于热能的距离：

$$
r_O
=
\frac{e^{2}}{4\pi\epsilon_0\epsilon_r k_B T}
$$

其中：

- `e`：元电荷。
- $\epsilon_0$：真空介电常数。
- $\epsilon_r$：水的相对介电常数。
- `k_B`：Boltzmann 常数。
- `T`：温度。

在 25 C 的水中，`r_O` 约为 `0.7 nm`。若初始电子-阳离子分离距离小于或接近该尺度，geminate recombination 很强；若外场、界面势或孔道几何使电子越过该尺度，逃逸产额提高。

### 7.2 外场或内建场的无量纲判据

外场对电子分离的影响可用下式估算：

$$
\Psi_E
=
\frac{eE\ell}{k_B T}
$$

其中：

- `E`：局部电场强度，单位 $\mathrm{V}\,\mathrm{m}^{-1}$。
- `ell`：电子与母体阳离子或空穴之间的有效分离距离，单位 $\mathrm{m}$。
- $\Psi_E$：场驱动分离能与热能之比。

判断规则：

```text
Psi_E << 1：电场对复合几率影响弱；
Psi_E ~ 1：电场开始显著改变逃逸概率；
Psi_E >> 1：漂移分离可与扩散/复合竞争。
```

在 25 C 下，$k_B T/e \sim 25.85 mV$。因此：

| `E` in $\mathrm{V}\,\mathrm{m}^{-1}$ | $ell = 1 nm$ | $ell = 5 nm$ | $ell = 10 nm$ | 解释 |
|---:|---:|---:|---:|---|
| `1 x 10^5` | `0.004 kBT` | `0.019 kBT` | `0.039 kBT` | 普通宏观外场，对纳米电子分离弱。 |
| `1 x 10^6` | `0.039 kBT` | `0.19 kBT` | `0.39 kBT` | 可有轻微影响，但高电导水中易被屏蔽。 |
| `1 x 10^7` | `0.39 kBT` | `1.93 kBT` | `3.87 kBT` | 纳米孔电双层或强内建场可显著降低复合。 |
| `1 x 10^8` | `3.87 kBT` | `19.3 kBT` | `38.7 kBT` | 强界面场，可能主导早期电荷分离。 |

这说明“外加电场提高 G 值”只在局部场足够强、离子强度足够低、电子未被表面短路捕获且反应时间尺度匹配时成立。

### 7.3 孔隙隔室效应

设孔径为 `d_p`，有效扩散系数为 $D_{\mathrm{eff}}$，则孔内扩散时间尺度：

$$
\tau_{diff}
=
\frac{d_p^{2}}{D_{eff}}
$$

若自由基寿命 $\tau_r$ 小于跨孔扩散时间 $\tau_{\mathrm{diff}}$，则自由基主要在本孔内反应；若 $\tau_r$ 大于孔喉交换时间，才可能跨孔反应。可定义一个复合 Damkohler 数：

$$
Da_{rec}
=
k_{rec} c_{rad} \tau_{diff}
$$

其中 `k_rec` 为二级复合速率常数，`c_rad` 为局部自由基浓度。纳米孔中局部浓度高会提高复合，但隔室分离又会降低与反向反应物相遇的概率。最终方向取决于：

```text
同一孔内的初级密度
孔与孔之间的连通性
水层厚度
孔壁对电子/自由基的捕获
H2 是否快速逸出或留在水相
```

这也是为什么多孔介质不是简单地“复合更多”或“复合更少”，而是形成新的空间选择性。

## 8. 能带结构、半导体与粘土复合体系

### 8.1 氧化物-水界面的电子转移

在固体-水复合体系中，电子是否进入水相可用相对能带边描述。令：

- $V_0^s$：固体相低能电子或导带底相对真空能级的位置。
- $V_0^w$：水相相应能级位置。
- $\Delta U = V_0^s - V_0^w$。

若：

$$
\Delta U > 0
$$

则电子从固体进入水相在能量上更有利，水可作为电子收集相。电子跨界面需要满足垂直动能与势垒条件：

$$
\frac{p_\perp^{2}}{2m^*}
\ge
E_b
$$

其中：

- `p_perp`：电子动量垂直界面分量。
- $m^*$：有效质量。
- $E_b$：界面势垒或有效反射能垒。

一旦电子进入水相并通过振动态耗散能量，就可能被水溶剂化，形成 $e_{\mathrm{aq}}^-$。这一路径解释了 silica 纳米孔中 $e_{\mathrm{aq}}^-$ 增强的模拟结果 (Ouerdane et al., 2010)。

### 8.2 半导体水分解判据

半导体参与水分解需满足：

$$
E_C < E(H^+/H_2)
$$

和：

$$
E_V > E(O_2/H_2O)
$$

这里使用电化学能级惯例时，需要明确相对 NHE、真空能级或材料能带图的符号方向。文字含义是：

- 导带电子必须具有足够还原能力驱动 HER。
- 价带空穴必须具有足够氧化能力驱动 OER 或水/羟基氧化。
- 电子和空穴必须在复合前被分离并到达反应位点。
- 表面催化剂必须降低 HER/OER 过电位。

电离辐射与光催化不同。γ 射线和电子束不会只按带隙选择性吸收，而会产生大量二次电子、空穴、激子和缺陷。因此它更接近“高能无选择激发源”。这带来两个后果：

```text
优势：可穿透不透明多孔材料，在固体和水中同时产生载流子。
劣势：热化损失和辐射损伤大，能量选择性差，必须严格计算总能效。
```

### 8.3 粘土材料的合理定位

粘土在该研究方向中的作用应分为四类：

| 角色 | 材料例子 | 作用 | 风险 |
|---|---|---|---|
| 限域水载体 | 膨润土、蒙脱石、高岭石 | 提供层间水、微孔、表面电荷和电双层 | 吸附水量低，真实孔道不均一。 |
| 离子交换/缓冲材料 | Na/Ca-蒙脱石、膨润土 | 控制 pH、离子强度、金属离子捕获 | 高盐时电场被屏蔽，杂质捕获自由基。 |
| 半导体载体 | 粘土负载 TiO2、ZrO2、Fe2O3、g-C3N4、MoS2 | 分散活性相、提高界面面积 | 粘土本体不等于半导体；复合界面需表征。 |
| 核废料工程屏障 | 膨润土缓冲层 | 控制地下水、胶体、核素迁移和气体扩散 | 辐解产物、腐蚀气体和微生物会反馈影响长期性能。 |

因此，建议的材料路线不是“粘土半导体电解槽”，而是：

```text
clay scaffold + oxide/semiconductor nanophase + HER/OER cocatalyst
+ controlled pore water + radiation/electric-field coupling
```

## 9. 为什么 $e_{\mathrm{aq}}^-$、$H_2$、$H_2O_2$ 在多孔介质中可升高

### 9.1 $e_{\mathrm{aq}}^-$ 升高

$e_{\mathrm{aq}}^-$ 升高的必要条件是生成电子后没有快速复合或被不可逆捕获。多孔介质提供三条增强路径：

1. 固体相吸收辐射后产生低能电子，电子跨氧化物-水界面进入水相。
2. 孔壁电荷或纳米管内建极化使电子与空穴空间分离。
3. 小孔径使电子进入不同孔室，降低与初始阳离子或 $•OH$ 的相遇概率。

抑制条件也必须同时写清：

- 金属表面可捕获预溶剂化电子。
- 溶解氧会快速捕获 $e_{\mathrm{aq}}^-$，生成 `O2•^-`。
- 高离子强度会缩短 Debye 长度，削弱外加电场在孔内的有效作用。
- Fe(III)、U(VI)、Cu(II)、NO3^- 等电子受体会竞争消耗 $e_{\mathrm{aq}}^-$。

### 9.2 $H_2$ 升高

$H_2$ 的增加来自四类贡献：

$$
e_{aq}^{-}+e_{aq}^{-}+2H_2O \to H_2+2OH^{-}
$$

$$
e_{aq}^{-}+H\cdot+H_2O \to H_2+OH^{-}
$$

$$
H\cdot+H\cdot \to H_2
$$

$$
e_{pre}^{-}+H_2O \to H\cdot + OH^{-}
\quad \mathrm{followed\ by\ H_2\ formation}
$$

其中 `e_pre^-` 表示预溶剂化电子或准自由电子。多孔介质使 $H_2$ 升高的关键不只是产氢路径增强，还包括反向消耗路径变弱：

$$
H_2 + \cdot OH \to H_2O + H\cdot
$$

当 $H_2$ 与 $•OH$ 被不同孔室、不同水层或不同表面位点隔开时，该链反应不再像本体水中那样有效。

### 9.3 $H_2O_2$ 升高

$H_2O_2$ 可视为氧化端的长寿命配对产物：

$$
\cdot OH + \cdot OH \to H_2O_2
$$

若孔隙环境使 $•OH$ 更倾向于在局部孔室内两两反应，而不是被 $H_2$、$e_{\mathrm{aq}}^-$ 或有机物消耗，则 $H_2O_2$ 增加。Foley 等的 hydrated nanoporous glasses 结果支持 $H_2O_2$ 是 $H_2$ 的氧化 counterpart 这一观点 (Foley et al., 2007)。

但金属表面会改变这一结论。金属或金属氧化膜可催化：

$$
H_2O_2 + surface \to \cdot OH + OH^{-} + surface^{+}
$$

或：

$$
H_2O_2 \to H_2O + \frac{1}{2}O_2
$$

因此，金属孔道中观测到的 $•OH$ 增强并不等同于 $H_2O_2$ 必然积累，它可能意味着 $H_2O_2$ 被活化为更强腐蚀性自由基。

## 10. 本体水 vs 多孔介质对照

| 对比项 | 本体水 | 多孔介质水 | 对 G 值的含义 |
|---|---|---|---|
| 能量沉积 | 主要在水相 | 水相和固体相共同吸收 | 固体向水相的能量转移可提高表观 G 值。 |
| 初级物种空间分布 | 同一 spur/track 内扩散复合 | 被孔壁、孔喉和水层分割 | 反向复合和链反应可被抑制。 |
| $e_{\mathrm{aq}}^-$ | 由水中电离电子溶剂化形成 | 还可由固体低能电子跨界面贡献 | $e_{\mathrm{aq}}^-$ 可升高，尤其在小孔径氧化物中。 |
| $H_2$ | 低 LET 下产率较低，且可被 $•OH$ 链反应消耗 | $H_2$ 与 $•OH$ 隔室化，反向反应弱 | $G(H_2)$ 可显著高于本体水。 |
| $H_2O_2$ | 由 $•OH$ 复合形成，也会被还原端消耗 | 氧化端局部化，且固体能量转移可增强 | $G(H_2O_2)$ 可升高，但金属表面可分解或活化。 |
| 电场 | 主要为 track 内 Coulomb 场 | 叠加电双层、内建极化、外加场 | 可降低 geminate recombination，前提是未被屏蔽或短路。 |
| 金属表面 | 无固体捕获边界 | 电子可被金属捕获，$H_2O_2$ 可被活化 | $e_{\mathrm{aq}}^-$ 可能下降，$•OH$ 可能上升。 |
| 工程解释 | 可作为基准反应网络 | 必须加入孔径、表面、能带和传质 | 不能把多孔增强直接外推为工业效率提升。 |

### 10.1 典型 G 值与能量指标

| 场景 | $G(H_2)$ in $\mu\mathrm{mol}\,\mathrm{J}^{-1}$ | $G(H_2)$ in $\mathrm{molecule} / 100\,\mathrm{eV}$ | 吸收辐射能 $\mathrm{kWh}\,\mathrm{kg}^{-1} H_2$ | 说明 |
|---|---:|---:|---:|---|
| 本体低 LET 水辐解 | 0.047 | 0.45 | 2978 | 远高于电解槽电耗，不适合作主产氢路线。 |
| 水饱和纳米孔 silica | 0.30 | 2.9 | 462 | 产额约 6-7 倍，但仍高于常规电解约 50 kWh/kg。 |
| 强增强假设值 | 0.62 | 6.0 | 223 | 仍高于电解工程基准。 |
| 高性能辐解目标 | 2.07 | 20.0 | 67 | 接近但仍高于现代电解，且材料/剂量率要求苛刻。 |
| 与 50 kWh/kg 持平阈值 | 2.78 | 26.8 | 50 | 若主动制造辐射，至少需达到该量级才有能量竞争性。 |
| 少量吸附水层文献端元 | 3.0 | 28.9 | 46 | 可能接近电解能耗，但水量极低、通量和工程放大受限。 |

上表只计算吸收辐射能，没有计入产生辐射源所需电力、屏蔽、冷却、气体分离、辐射损伤、许可和运维成本。若辐射由电子加速器主动产生，总电耗还需除以加速器和耦合效率。

## 11. 总效率与能量守恒

### 11.1 热力学上限

水分解：

$$
H_2O(l) \to H_2(g) + \frac{1}{2}O_2(g)
$$

标准 Gibbs 自由能：

$$
\Delta G^\circ \approx 237.1\ \mathrm{kJ}\ \mathrm{mol}^{-1}\ H_2
$$

标准焓变：

$$
\Delta H^\circ \approx 285.8\ \mathrm{kJ}\ \mathrm{mol}^{-1}\ H_2
$$

若 $100\,\mathrm{eV}$ 全部以 Gibbs 自由能形式转为 $H_2$，理论最大 G 值为：

$$
G_{\Delta G,max}
=
\frac{100\mathrm{eV}}{\Delta G^\circ/N_A}
\approx 40.7\ \mathrm{molecule}/100\mathrm{eV}
$$

若按 HHV 焓值计：

$$
G_{\Delta H,max}
\approx 33.8\ \mathrm{molecule}/100\mathrm{eV}
$$

因此：

- 本体水 $G(H_2) \sim 0.45$，Gibbs 能效率约 $0.45 / 40.7 = 1.1%$。
- 水饱和多孔 silica $G(H_2) \sim 2.9$，Gibbs 能效率约 `7.1%`。
- 少量吸附水层 $G(H_2) \sim 28.9$，表观 Gibbs 能效率可达约 `71%`，但这通常是极低含水量、强界面能量转移和特定实验口径下的结果，不能直接代表连续流工业水电解。

### 11.2 产业化能量账

若吸收辐射功率为 $P_{\mathrm{abs}}$，则产氢质量流率：

$$
\dot{m}_{H_2}
=
P_{abs}
\left(1.03643\times 10^{-7}G_{H_2}^{(100\mathrm{eV})}\right)
M_{H_2}
$$

其中 $M_{H_2} = 2.01588\times 10^{-3} \mathrm{kg}\,\mathrm{mol}^{-1}$。

以 $P_{\mathrm{abs}} = 1 \mathrm{MW}$ 连续吸收为例：

| $G(H_2)$ in $\mathrm{molecule} / 100\,\mathrm{eV}$ | 年产氢量 $\mathrm{kg}\,\mathrm{yr}^{-1}\,\mathrm{MW}_{\mathrm{abs}}^{-1}$ | 若主动辐射且耦合效率 $\eta_{\mathrm{rad}}=0.5$、电价 `$50/MWh`，仅辐射电费 `$ kg^-1` |
|---:|---:|---:|
| 0.45 | 2,965 | 298 |
| 2.9 | 19,108 | 46 |
| 6.0 | 39,533 | 22 |
| 10.0 | 65,889 | 13 |
| 20.0 | 131,777 | 6.7 |
| 28.9 | 190,418 | 4.6 |

这说明：

```text
若辐射由电力主动制造，绝大多数可实证的多孔介质 G 值仍无法与电解槽竞争；
若辐射为废辐射或必须屏蔽的近场能量，经济逻辑才可能转为“副产回收”和“安全控制”。
```

### 11.3 与电解水耦合时的正确效率指标

辐射辅助电解不能只比较电解槽端电压，还要比较系统总能耗：

$$
\eta_{system}
=
\frac{\dot{n}_{H_2}\Delta G^\circ}
{P_{electric} + P_{rad,input} + P_{aux}}
$$

其中：

- $P_{\mathrm{electric}}$：电解槽电功率。
- $P_{\mathrm{rad},\mathrm{input}}$：产生、引导或维持辐射源的外部功率；若为废辐射，可在边际成本模型中设为近零，但仍需计入安全系统成本。
- $P_{\mathrm{aux}}$：泵、冷却、屏蔽、气体分离、监测和控制系统功率。

如果只看：

$$
V_{cell} = E_{rev} + \eta_{anode} + \eta_{cathode} + iR + \eta_{mass}
$$

而不计 $P_{\mathrm{rad},\mathrm{input}}$，会把辐射能误认为免费能量，得到虚假的效率提升。

## 12. 何种条件下 G 值增强判断成立

| 条件 | 有利于 G 值增强 | 不利或反向条件 |
|---|---|---|
| 辐射类型 | 低 LET γ/电子可产生较高逃逸自由基；固体能量转移可贡献电子 | 高 LET 或极高剂量率会增强轨迹内复合，或造成激子湮灭和缺陷损伤。 |
| 剂量率 | 低到中等剂量率有利于界面能量转移保持有效 | 10 MeV 高剂量率电子束端元中，silica 到水的能量转移可被抑制。 |
| 孔径 | `2-100 nm` 氧化物孔道利于电子收集和隔室化；`<2 nm` 层间水可能强限域 | 孔太大则接近本体水；孔太小则水活度低、扩散差、通量低。 |
| 材料 | SiO2、ZrO2、TiO2、Al2O3、imogolite 和复合半导体可提供能带/界面效应 | 金属表面可能捕获电子，缺陷和杂质可能淬灭自由基。 |
| 电导率/离子强度 | 低离子强度有利于电双层重叠和局部电场 | 高盐地下水中 Debye 长度短，外场被屏蔽。 |
| pH | 中性到弱碱条件保留 $e_{\mathrm{aq}}^-$；酸性可把 $e_{\mathrm{aq}}^-$ 转为 $H•$ | 强酸、强碱都改变反应网络；pH 需与电极腐蚀和材料稳定性匹配。 |
| 含氧状态 | 缺氧有利于 $e_{\mathrm{aq}}^-$ 存活和 $H_2$ 形成 | `O2` 快速捕获电子，转向 $O2•^- / HO2•$ 路径。 |
| 含水量 | 单层/少层吸附水可出现高表观 G 值 | 工业产氢需要高水通量，少层水端元难以放大。 |
| 外加电场 | 局部 $E >= 10^{7} \mathrm{V}\,\mathrm{m}^{-1}$ 且 $ell \sim 5-10 nm$ 时可显著分离电荷 | 宏观电场在高电导水中容易被屏蔽，且金属电极可短路电子。 |

## 13. 核废料处置、地下水辐解与核素环境化学

### 13.1 核废料处置

在深地质处置库中，辐解产物不是“产氢资源”这么简单，而是安全项：

- $H_2$ 可增加气体压力，影响膨润土缓冲层和裂隙水运移。
- $H_2$ 也可作为还原剂，促进还原性微生物代谢或影响金属腐蚀。
- $H_2O_2$ 与 $•OH$ 可增强容器腐蚀和燃料表面氧化。
- `O2`、`HO2•`、`O2•^-` 可改变近场 Eh。
- 金属容器表面可能捕获电子，使氧化端化学占优。

因此，核废料处置中的关键问题不是追求最高 $G(H_2)$，而是建立：

```text
辐射源项 -> 孔隙水 G 值 -> 自由基网络 -> 气体压力 -> 腐蚀 -> 核素迁移 -> 长期安全
```

的耦合模型。

### 13.2 地下水长期演化和天然氢

在结晶岩裂隙系统中，U-Th-K 衰变产生的 H2 通量通常很低，但时间尺度可达百万年。其地球化学意义体现在：

- 给深部微生物提供电子供体。
- 与 sulfate、carbonate、Fe(III)、U(VI) 等氧化还原对耦合。
- 影响甲烷生成、硫酸盐还原和铁还原。
- 在低通量、长封存、低有机碳环境中成为重要背景能量。

但对商业天然氢来说，需要满足：

```text
源项足够高
水-岩界面足够大
H2 被保存而非被微生物或矿物消耗
有封闭与富集机制
存在可采流体通道
```

低孔低渗环境如 Revell Batholith 的辐解 H2 更适合作为深部生物圈和核废料库安全模型，而不是天然氢资源模型 (Higgins et al., 2025)。

### 13.3 放射性核素迁移

$e_{\mathrm{aq}}^-$、$H_2$、$H•$、$H_2O_2$ 和 $•OH$ 会影响核素价态：

| 核素/元素 | 氧化还原敏感性 | 多孔辐解影响 |
|---|---|---|
| U | `U(IV)` 难溶，`U(VI)` 易迁移 | 还原端可固定 U，氧化端可促进 U(VI) 形成。 |
| Tc | `Tc(IV)` 难溶，`Tc(VII)` 易迁移 | `H2O2/•OH` 增强会提高迁移风险。 |
| Se | 多价态，迁移性随 Eh-pH 变化 | 需耦合硫/铁/有机质反应。 |
| I | 碘离子和碘酸盐迁移性强 | 氧化环境可改变碘形态和吸附。 |
| Fe/S | 控制地下水 Eh 与微生物代谢 | H2 与 sulfate 同时生成时会形成供体-受体耦合。 |

## 14. 产业化路线筛选与成本模型

### 14.1 LCOH 成本框架

定义辐射辅助制氢的平准化成本：

$$
LCOH
=
\frac{
CRF\ C_{cap}
+ C_{O\&M}
+ C_{electric}
+ C_{rad}
+ C_{shield}
+ C_{license}
+ C_{waste}
+ C_{separation}
}
{M_{H_2,annual}}
$$

其中：

- `CRF`：资本回收因子。
- $C_{\mathrm{cap}}$：反应器、电解槽、辐射源、屏蔽、气体处理和监测系统资本成本。
- $C_{\mathrm{O\&M}}$：运维成本。
- $C_{\mathrm{electric}}$：电解与辅助电力成本。
- $C_{\mathrm{rad}}$：辐射源购置、产生或使用成本。
- $C_{\mathrm{shield}}$：屏蔽和辐射防护成本。
- $C_{\mathrm{license}}$：核安全、放射源、环境和职业安全许可成本。
- $C_{\mathrm{waste}}$：活化材料、污染材料和二次废物处理成本。
- $C_{\mathrm{separation}}$：H2/O2/H2O2/水蒸气/放射性气体的分离净化成本。
- $M_{H_2,\mathrm{annual}}$：年产氢质量。

### 14.2 路线筛选

| 路线 | 技术设想 | 可行性判断 | 主要价值 |
|---|---|---|---|
| 自然放射性矿物直接产氢 | 利用 U-Th-K 天然衰变辐解地下水 | 工业产氢不可行；通量太低 | 深部生物圈、天然氢背景、核素迁移。 |
| 核废料近场副产 H2 回收 | 利用已存在废辐射场生成 H2 | 工程和监管极难；不应以产氢为处置库目标 | 气体安全、腐蚀控制、长期模型验证。 |
| γ 源或电子束主动辐解水 | 建造辐射反应器直接产 H2 | 若辐射需电力制造，能效通常不经济 | 废水处理、灭菌、特殊化学合成副产氢。 |
| 多孔半导体辐射辅助电解 | 辐射产生载流子，电场分离并降低过电位 | TRL 1-3，值得做机制验证 | 研究电子/自由基/电极界面协同。 |
| 粘土-半导体复合电极 | 粘土提供限域和电双层，TiO2/ZrO2/g-C3N4 等提供活性相 | 可做材料开题，但需实证 | 低成本载体、界面水结构调控、核废料屏障模型。 |
| 废辐射能回收 | 利用本来需要屏蔽的辐射能 | 只有在特定核设施边界内可能 | 安全和副产价值，不是普适绿氢路线。 |

### 14.3 工程 go/no-go 指标

建议设定以下门槛：

| 指标 | Go 条件 | No-go 条件 |
|---|---|---|
| $G(H_2)$ | 连续流、实际含水量下 $G(H_2) > 20 \mathrm{molecule}/100\mathrm{eV}$，且可重复 | 仅在少层吸附水粉末中高产，水通量不可放大。 |
| 总能效 | 计入辐射源后低于或接近 $50\,\mathrm{kWh}\,\mathrm{kg}^{-1} H_2$ | 只降低电解槽电压但外部辐射能巨大。 |
| 材料寿命 | >1000 h 辐照-电化学稳定性，活性无显著衰减 | 辐射损伤、孔道堵塞、金属腐蚀、活性相流失。 |
| 安全 | H2/O2 分离、H2O2 控制、辐射屏蔽和许可路径清晰 | 产生混合爆炸气、活化废物或不可接受剂量场。 |
| 成本 | `LCOH` 有明确下降来源 | 成本下降来自忽略辐射源或屏蔽成本。 |

## 15. 建议科研路线

### 15.1 第一阶段：基准实验和模型校准

目标：在统一吸收能量口径下测量本体水、silica、alumina、ZrO2、TiO2、bentonite、imogolite、金属多孔材料中的 $G(e_{aq}^{-})$、$G(•OH)$、$G(H_2)$、$G(H_2O_2)$。

变量矩阵：

- 孔径：`<2 nm` 层间水、`2-10 nm` 介孔、`10-100 nm` 大介孔。
- 含水量：单层水、少层吸附水、毛细凝结水、水饱和孔。
- 辐射：低 LET γ、电子束、必要时 $\alpha$ 模拟。
- 剂量率：低剂量率、连续中等剂量率、高剂量率脉冲。
- 化学：pH 4/7/10，缺氧/空气饱和，低盐/高盐，含 Fe/U/NO3^- 电子受体。
- 电场：无外场、低场、局部强场；同时测量电导率和 Debye 长度。

测量手段：

- pulse radiolysis：$e_{\mathrm{aq}}^-$ 和瞬态自由基。
- EPR spin trapping：$•OH$、$H•$。
- 气相色谱或质谱：$H_2$、`O2`、`CH4`。
- 比色/电化学：$H_2O_2$。
- 原位电化学阻抗：孔道电导、电双层和界面电荷。
- BET、SAXS/SANS、NMR、QENS：孔径、水结构和水动力学。
- XPS/UPS/Mott-Schottky：能带边和表面态。

### 15.2 第二阶段：反应-输运-电场耦合模拟

建立多尺度模型：

```text
Monte Carlo energy deposition
-> primary yields and spatial distribution
-> Nernst-Planck-Poisson transport
-> radical reaction network
-> surface flux and band alignment
-> gas/liquid partition and H2 escape
```

关键拟合参数：

- $\eta_{s \to w,i}$：固体能量向水相产物转移效率。
- $k_{e,s}$：电子表面捕获速率。
- $k_{OH,s}$：羟基自由基表面淬灭或生成速率。
- $E_{\mathrm{local}}$：孔道局部电场。
- $D_{\mathrm{eff}}$：受限水扩散系数。
- `a_s`：有效固液界面面积。

### 15.3 第三阶段：辐射辅助电解原型

只在第一、二阶段证明 $G(H_2)$、电子寿命和能量效率有实质优势后，才进入电解耦合原型。

原型设计原则：

- 辐射区和电解区可隔离，避免电极被不必要活化或损伤。
- 气体分离优先于产率提升，防止 $H_2/O2$ 混合。
- 采用氧化物/半导体多孔膜，而非直接裸金属孔道。
- 粘土作为支撑和孔水调控层，活性相由可表征半导体和电催化剂承担。
- 用 $system \mathrm{kWh}\,\mathrm{kg}^{-1} H_2$ 而不是单项 G 值作为最终指标。

## 16. 局限性与数据缺口

主要局限性包括：

- 本地 Sci-Bot PDF 是综合性材料，不是原始数据集；其中个别单位表达需要回到原始文献核对。
- 多孔体系的 G 值受吸收能量分母定义影响，水相能量和固体+水总能量不能混用。
- 高表观 G 值常出现在少量吸附水中，其工业水通量与连续收氢效率未被证明。
- 粘土矿物组成复杂，天然样品中的 Fe、Ti、有机质、盐和交换阳离子会强烈影响自由基网络。
- 外加电场在高电导孔隙水中会被屏蔽；真正起作用的是纳米尺度局部电场，而不是宏观电压本身。
- 金属表面可能提高 $•OH$ 和腐蚀风险，不能简单视为电子传输增强材料。
- 核废料处置和辐射源工业应用涉及监管、屏蔽、临界安全、活化废物和职业剂量，不能由材料实验直接外推。

## 17. 结论

1. 多孔介质中水辐解的 G 值可以显著不同于本体水。增强最可信的对象是 $e_{\mathrm{aq}}^-$、$H_2$ 和 $H_2O_2$，机制包括固体-水界面电子转移、纳米孔隔室效应、界面电场电荷分离和反向复合抑制。

2. 电场提高自由基逃逸产额的判断有明确边界。只有当局部电场约达到 $10^{7}-10^{8} \mathrm{V}\,\mathrm{m}^{-1}$、有效分离距离为数纳米、孔隙水离子强度不太高、电子没有被金属或溶解氧捕获时，电场才可能显著降低 geminate recombination。普通宏观外加电压不等于孔内有效电场。

3. 金属表面是双刃剑。它可提供导电通道和催化位点，但也可能捕获预溶剂化电子，降低 $e_{\mathrm{aq}}^-$，并通过 $H_2O_2$ 活化提高 $•OH$，增加腐蚀风险。

4. 粘土材料的合理科研定位是限域水、电双层、离子交换和复合载体。将普通粘土直接描述为高效半导体不严谨；更可行的是粘土负载氧化物/半导体/电催化剂的多孔复合体系。

5. 从工业制氢角度，辐解增强不等于总效率增强。若主动用电制造辐射，已实证的多数 G 值仍无法与现代电解水竞争。若辐射能是废辐射或核废料近场本来存在的能量，则研究重点应转向能量回收、气体安全、腐蚀控制、地下水长期演化和核素迁移。

6. 最值得立项的方向不是“核辐射替代电解槽”，而是“多孔介质中辐解-界面电场-半导体载流子-电化学反应的耦合机理”。该方向服务于地球化学、核废料处置、辐射化学模拟、深部天然氢和地下水长期演化研究，同时保留未来特殊场景氢气副产的工程可能。

## 参考文献

Blair, C. C., D'Hondt, S., Spivack, A. J., & Kingsley, R. H. (2007). Radiolytic hydrogen and microbial respiration in subsurface sediments. *Astrobiology, 7*(6), 951-970. https://doi.org/10.1089/ast.2007.0150

Buxton, G. V., Greenstock, C. L., Helman, W. P., & Ross, A. B. (1988). Critical review of rate constants for reactions of hydrated electrons, hydrogen atoms and hydroxyl radicals in aqueous solution. *Journal of Physical and Chemical Reference Data, 17*(2), 513-886. https://doi.org/10.1063/1.555805

Dzaugis, M. E., Spivack, A. J., Dunlea, A. G., Murray, R. W., & D'Hondt, S. (2016). Radiolytic hydrogen production in the subseafloor basaltic aquifer. *Frontiers in Microbiology, 7*, 76. https://doi.org/10.3389/fmicb.2016.00076

Foley, S., Rotureau, P., Renault, J.-P., & Mialocq, J.-C. (2007). Hydrogen peroxide formation in the radiolysis of hydrated nanoporous glasses: A low and high dose rate study. *Chemical Physics Letters, 450*(1-3), 91-95. https://doi.org/10.1016/j.cplett.2007.10.102

Higgins, P. M., Song, M., Warr, O., & Sherwood Lollar, B. (2025). Natural H2 and sulfate production via radiolysis in low porosity and permeability crystalline rocks. *Journal of Geophysical Research: Biogeosciences, 130*, e2025JG008863. https://doi.org/10.1029/2025JG008863

International Energy Agency. (2025). *Global Hydrogen Review 2025*. IEA. https://www.iea.org/reports/global-hydrogen-review-2025

Le Caër, S. (2011). Water radiolysis: Influence of oxide surfaces on H2 production under ionizing radiation. *Water, 3*(1), 235-253. https://doi.org/10.3390/w3010235

Le Caër, S., Rotureau, P., Vigier, F., Blain, G., Tribet, M., Renault, J.-P., & Mialocq, J.-C. (2014). Radiolysis of water in the vicinity of passive surfaces. *Corrosion Science, 83*, 255-260. https://doi.org/10.1016/j.corsci.2014.02.024

Lin, L.-H., Hall, J., Lippmann-Pipke, J., Ward, J. A., Sherwood Lollar, B., DeFlaun, M., Rothmel, R., Moser, D. P., Gihring, T. M., Mislowack, B., & Onstott, T. C. (2005). Radiolytic H2 in continental crust: Nuclear power for deep subsurface microbial communities. *Geochemistry, Geophysics, Geosystems, 6*, Q07003. https://doi.org/10.1029/2004GC000907

Lin, L.-H., Slater, G. F., Sherwood Lollar, B., Lacrampe-Couloume, G., & Onstott, T. C. (2005). The yield and isotopic composition of radiolytic H2, a potential energy source for the deep subsurface biosphere. *Geochimica et Cosmochimica Acta, 69*(4), 893-903. https://doi.org/10.1016/j.gca.2004.07.032

Ouerdane, H., Gervais, B., Zhou, H., Beuve, M., & Renault, J.-P. (2010). Radiolysis of water confined in porous silica: A simulation study of the physicochemical yields. *The Journal of Physical Chemistry C, 114*(29), 12667-12674. https://doi.org/10.1021/jp103127j

Pignié, M.-C., Shcherbakov, V., Charpentier, T., Moskura, M., Carteret, C., Denisov, S., Mostafavi, M., Thill, A., & Le Caër, S. (2021). Confined water radiolysis in aluminosilicate nanotubes: The importance of charge separation effects. *Nanoscale, 13*, 3092-3105. https://doi.org/10.1039/D0NR08948F

Rotureau, P., Renault, J.-P., Lebeau, B., Patarin, J., & Mialocq, J.-C. (2005). Radiolysis of confined water: Molecular hydrogen formation. *ChemPhysChem, 6*(7), 1316-1323. https://doi.org/10.1002/cphc.200500042

