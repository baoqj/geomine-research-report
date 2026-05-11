# 铀—钍—钾放射性衰变驱动的深部 H2 生成：以 Revell Batholith 与 Athabasca Basin 基底岩为例

日期：2026-05-11  
研究框架：GeoMine Research / deep geochemistry / natural hydrogen / water radiolysis / crystalline basement / nuclear waste repository geochemistry  
研究对象：Revell Batholith, northwestern Ontario；Athabasca Basin crystalline basement, Saskatchewan-Alberta  
核心问题：U-Th-K 衰变如何通过水辐解生成 H2；孔隙、裂隙、矿物表面、地下水、硫化物和热演化如何控制 H2 的产生、保存、消耗和风险。  
边界说明：本报告是科研调研与理论论证，不是天然氢资源量评价、核废料处置库安全审查、工程设计或投资建议。

## 1. 执行摘要

本课题的核心判断是：

```text
在低孔低渗结晶岩中，U-Th-K 衰变导致的水辐解确实可以长期产生 H2；
但对 Revell Batholith 这类低孔隙率、硫化物含量低、流体连通性弱的岩体而言，
产率更接近深部微生物能量源和核废料库气体/氧化还原安全项，
而不是可商业开发的天然氢资源。
```

2025 年 Higgins, Song, Warr and Sherwood Lollar 在 *Journal of Geophysical Research: Biogeosciences* 发表的 Revell Batholith 研究给出一个关键数值：Revell 最可能的辐解 H2 生成速率约为：

```text
P_H2,Revell ≈ 1.6 nmol m^-3 rock yr^-1
```

这个数值的意义不在于“产量大”，而在于它建立了一个可量化框架：即使不能直接取样生物量、气体和流体，也可以利用 U-Th-K、孔隙度、硫化物、水-岩几何、辐射能量沉积和 Monte Carlo 不确定性估算 H2 与 sulfate 的潜在生成能力。

把这个结果换算到资源尺度：

```text
1 km3 rock = 10^9 m3 rock
1.6 nmol m^-3 yr^-1 × 10^9 m3 = 1.6 mol H2 yr^-1
≈ 3.2 g H2 yr^-1 per km3 rock
```

所以，对 Revell 这种端元环境，辐解 H2 的经济意义很弱；但对深部生物圈和核废料处置库，长期、低通量、原位产生的 H2 与氧化剂非常重要。

Athabasca Basin 基底岩的意义不同。Athabasca 是全球最富铀的地质省之一，已有研究证明盆地内存在 basin-scale U-rich brines，流体包裹体中 U 可达 `0.6-26.8 ppm`，矿床流体可更高；2025 年公开的 eastern Athabasca felsic intrusive 数据显示多数放射性生热值落在 `1.6-3.5 µW m^-3` 的花岗岩/上地壳平均范围，但伟晶质样品可高于邻近花岗岩。由此可提出一个新的研究假说：

```text
Athabasca 基底的辐解 H2 潜力不是由平均岩石 U-Th-K 决定，
而由“富放射性附件矿物/伟晶质-花岗质体 + 微裂隙水 + 硫化物/石墨还原带 + 长驻留地下水”
共同控制。
```

本报告提出一个理论创新指标：**Radiolytic Hydrogen System Index, RHSI**。它把传统的 U-Th-K 生热项，扩展为五个相乘/相除的控制量：

```text
RHSI = Source(U,Th,K)
       × Interface(fracture aperture, surface area, alpha range)
       × WaterResidence(residence time, connectivity)
       × Retention(seal, solubility, pressure)
       / Sink(microbial sulfate reduction, methanogenesis, Fe/S redox consumption, leakage)
```

这个指标比“找高 U 花岗岩”更合理，因为辐解 H2 的成藏或生态意义必须同时满足：

1. 有放射性能量源；
2. 这部分能量真正沉积到水中；
3. H2 不被快速扩散、冲刷、微生物或矿物反应消耗；
4. 有足够长的封存时间；
5. sulfate 等电子受体不能完全把 H2 消耗掉。

## 2. 研究问题和证据车道

本研究按 GeoMine evidence lanes 分为：

| Evidence lane | 核心问题 | 证据来源 |
|---|---|---|
| AOI / 地质背景 | Revell 与 Athabasca 是否可比 | NWMO Revell 资料、Revell 地球物理论文、Athabasca 公开地质 |
| 放射性源项 | U-Th-K 如何决定辐射能量源 | U-Th-K 生热公式、Athabasca heat production 数据 |
| 水辐解化学 | H2 与 H2O2/自由基如何形成 | Le Caer 2011、Dzaugis et al. 2016、Briggs et al. 2025 |
| 孔隙-裂隙几何 | 低孔低渗为何不等于高产 H2 | Revell 2025 Monte Carlo、fracture-width model |
| 硫循环 | sulfate 如何与 H2 同源或竞争 | Li et al. 2016、Kidd Creek、Higgins et al. 2025 |
| 地下水与核素迁移 | 盐水、Eh-pH、U 价态和核素迁移 | Revell groundwater, Athabasca U-rich brines |
| 热长期演化 | 温度、热梯度、反应速率与水岩平衡 | radiogenic heat, Arrhenius, fracture residence |
| 工程/生态意义 | H2 是能源、微生物食物还是气体风险 | DGR gas pressure, deep biosphere, natural H2 exploration |

## 3. 资料调研结果

### 3.1 Revell Batholith 的研究地位

Revell Batholith 位于加拿大 Ontario 西北部，NWMO 已将其选为加拿大乏燃料深地质处置库的场址。NWMO 官方页面说明，该库将位于 Revell Batholith 这一 Ontario 西北部结晶岩体中，位于 Wabigoon Lake Ojibway Nation 领土和 Ignace 附近。

Briggs et al. 2025 在核废料容器辐解腐蚀模型中引用 Revell 场址条件：处置库预计位于 `650-800 m` 深度的结晶岩中，处置深度地下水预计为缺氧、盐性、Ca-Na-Cl 型，Cl- 约 `0.1 mol/L`。这些条件非常适合研究：

- 低渗结晶岩中水和辐射能量的接触；
- 氯盐水对辐解反应网络的影响；
- H2、O2、H2O2 在水-气界面的分配；
- 铜容器、膨润土、岩石表面与辐解产物之间的反应。

Revell 不是“天然氢矿”的典型靶区，而是一个约束良好的低孔低渗端元：

```text
低孔隙度
低渗透率
结晶岩
盐性缺氧地下水
低硫化物
核废料库安全背景
```

### 3.2 2025 Revell radiolysis 论文的关键结论

Higgins et al. 2025 的论文题目是 *Natural H2 and Sulfate Production via Radiolysis in Low Porosity and Permeability Crystalline Rocks*。其研究重点：

- 用 Monte Carlo 方法估算 Revell Batholith 中辐解生成 H2 和 sulfate 的能力；
- 与 Kidd Creek 这一更破碎、硫化物更丰富的 Canadian Shield 深部环境对比；
- 评估低孔低渗结晶岩对深部生物圈、天然 H2 探索和 DGR 的意义。

关键结果：

```text
Revell most probable H2 production:
1.6 nmol m^-3 rock yr^-1

Revell sulfate production:
比 Kidd Creek 低 10^2-10^6 倍

主要控制因素：
H2 低是因为低孔隙率；
sulfate 低是因为硫化物含量低。
```

这个结果给出一个重要科学边界：

```text
放射性元素多并不自动等于天然 H2 资源；
水-岩接触几何、孔隙连通性和保存条件同样关键。
```

### 3.3 Athabasca Basin 基底的可比性

Athabasca Basin 与 Revell 的可比性来自：

- 都是加拿大地盾背景；
- 都包含古老结晶基底；
- 都有低渗裂隙水/盐水系统的研究意义；
- 都涉及 U-Th-K 的天然放射性源项；
- 都与核材料、铀矿、长期地下水反应有关。

但 Athabasca 与 Revell 的关键差异也很明显：

| 对比项 | Revell Batholith | Athabasca Basin basement |
|---|---|---|
| 主要意义 | 核废料库低孔低渗端元 | 高品位铀矿省、U-rich fluid system |
| U 系统 | 普通花岗质/花岗闪长质背景 | 局部强烈 U 富集、U-rich brines、铀矿化 |
| 硫化物/石墨 | 相对低 | 局部 graphitic/sulphidic shear zones |
| 裂隙/结构 | DGR 需避开高渗结构 | 铀矿常由 reactivated structures 控制 |
| H2 经济潜力 | 很低 | 局部可作为天然 H2 热点假说，但未证实 |
| 研究价值 | 安全边界、背景辐解 | 辐解 H2 + U 迁移 + 深部生物圈 + 矿化系统耦合 |

Athabasca 2019 年流体包裹体研究显示，远离矿化的盆地岩石中也广泛存在 U-rich diagenetic brines，包裹体 U 浓度 `0.6-26.8 ppm`，平均约 `6.8 ppm U`，超过多数天然地质流体两个数量级以上。这说明 Athabasca 是一个 U 被长期迁移和重分配过的水-岩系统。

2025 年 Mendeley Data / GSC Open File 相关数据进一步显示 eastern Athabasca felsic intrusive 的 radiogenic heat production 多数落在 `1.6-3.5 µW m^-3`，与全球花岗岩和上地壳平均值相当，但 pegmatitic samples 相对邻近花岗岩升高。这意味着：

```text
Athabasca 的辐解 H2 热点不一定是大面积高生热背景；
更可能是局部伟晶质、富 U-Th 附件矿物、铀矿化裂隙和微孔水共同形成的微尺度热点。
```

## 4. 理论基础：从 U-Th-K 到 H2 的方程链

### 4.1 放射性衰变源项

对任一放射性核素 `j`：

```text
N_j = m_j N_A / M_j
λ_j = ln(2) / t_1/2,j
A_j = λ_j N_j
```

其中：

- `N_j` 是原子数；
- `m_j` 是该核素质量；
- `N_A` 是阿伏伽德罗常数；
- `M_j` 是摩尔质量；
- `λ_j` 是衰变常数；
- `A_j` 是活度，单位 decays s^-1。

单位岩石体积内的衰变能量源为：

```text
Q_rad = Σ_j A_j E_j
```

其中 `E_j` 是每次衰变最终沉积到介质中的能量。对天然结晶岩，主要核素链为：

```text
238U decay series
235U decay series
232Th decay series
40K
```

实际地热学中常用 Rybach 型经验公式直接从 U-Th-K 估算放射性生热：

```text
A_RHP(µW m^-3)
  = 10^-5 ρ (9.52 C_U + 2.56 C_Th + 3.48 C_K)
```

其中：

- `ρ` 为岩石密度，kg m^-3；
- `C_U` 为 U 浓度，ppm；
- `C_Th` 为 Th 浓度，ppm；
- `C_K` 为 K 浓度，wt.%；
- `A_RHP` 是体积放射性生热率。

例：取普通花岗质岩石：

```text
ρ = 2700 kg m^-3
C_U = 4 ppm
C_Th = 15 ppm
C_K = 4 wt.%

A_RHP = 10^-5 × 2700 × (9.52×4 + 2.56×15 + 3.48×4)
      = 2.44 µW m^-3
```

这个值与 eastern Athabasca felsic intrusive `1.6-3.5 µW m^-3` 的公开数据范围相容。

### 4.2 从生热到水中吸收剂量

放射性生热并不等于水辐解能量。许多能量沉积在矿物晶格中而不是水中。定义：

```text
f_w = absorbed radiation energy fraction in water
```

则单位岩石体积内水吸收功率为：

```text
P_abs,w = A_RHP × f_w
```

`f_w` 不是常数，而由以下因素控制：

- 孔隙度 `φ`；
- 裂隙宽度 `b`；
- 水-岩界面面积 `a_s`；
- alpha、beta、gamma 的射程；
- U-Th-K 在矿物中的空间分布；
- 放射性附件矿物是否靠近裂隙水；
- 裂隙水是否连通。

alpha 粒子射程通常只有几十微米，但 LET 高、H2 产额高；gamma 穿透强，但 LET 低。因此：

```text
alpha radiation controls near-interface hotspots;
gamma radiation controls more distributed low-LET background;
beta contributes intermediate behavior.
```

### 4.3 辐解产氢 G 值换算

G 值定义为每 `100 eV` 吸收能量生成或消耗的分子数。

```text
100 eV = 1.602 × 10^-17 J
```

如果 `G_H2` 的单位是 `molecules / 100 eV`，则每焦耳生成 H2 的摩尔数为：

```text
Y_H2 = G_H2 / [(1.602×10^-17) N_A]
     = 1.036×10^-7 G_H2 mol J^-1
```

Le Caer 2011 总结的纯水逃逸产额显示：

- 低 LET gamma/electron，中性 pH，`H2 ≈ 0.047 µmol J^-1`，约 `G(H2) ≈ 0.45`；
- 高 LET alpha，低 pH 条件下，`H2 ≈ 0.163 µmol J^-1`，约 `G(H2) ≈ 1.57`。

因此，单位岩石体积的辐解 H2 源项可以写为：

```text
P_H2,rad
  = 1.036×10^-7 × G_H2 × P_abs,w × seconds_per_year
  = 1.036×10^-7 × G_H2 × A_RHP × f_w × 31,557,600
```

若 `A_RHP` 用 `W m^-3`，则 `P_H2,rad` 的单位是：

```text
mol H2 m^-3 rock yr^-1
```

### 4.4 量级检验

取 `A_RHP = 2.44 µW m^-3`，`G_H2 = 1.0`。

若低孔低渗岩体中只有 `f_w = 0.0002` 的能量有效沉积到水中：

```text
P_abs,w = 2.44×10^-6 × 0.0002
        = 4.88×10^-10 W m^-3

P_H2 = 1.036×10^-7 × 1.0 × 4.88×10^-10 × 31,557,600
     = 1.59×10^-9 mol m^-3 yr^-1
     = 1.59 nmol m^-3 yr^-1
```

这与 Revell 2025 的 `1.6 nmol m^-3 rock yr^-1` 同阶。这个反推很重要：Revell 的低产率不是因为 U-Th-K 完全没有能量，而是因为：

```text
可被水接收并转化为 H2 的能量比例极小。
```

若在 Athabasca 某些局部伟晶质/富 U 裂隙中，取：

```text
A_RHP = 5.4 µW m^-3
f_w = 0.005
G_H2 = 1.2
```

则：

```text
P_H2 ≈ 1.07×10^-7 mol m^-3 yr^-1
     ≈ 107 nmol m^-3 yr^-1
```

这比 Revell 高约两个数量级，但仍然是非常低的体积通量。它对深部生态可能重要，对工业天然氢资源则只有在长期封存、区域聚集和低消耗条件下才可能有意义。

## 5. 孔隙、裂隙和表面积：为什么“低孔隙率”有双重作用

低孔隙率对 H2 有两个相反影响。

### 5.1 对产氢是不利的

水是反应物。若孔隙度极低，单位岩石体积内可被辐解的水少：

```text
water volume = φ V_rock
```

且只有靠近放射性矿物和裂隙壁的水能有效接收 alpha/beta 能量。低孔隙率通常意味着：

```text
small V_water
low connected surface
low f_w
low P_H2 per rock volume
```

这解释了 Revell 的低 H2 通量。

### 5.2 对保存可能是有利的

低孔低渗又可能提高 H2 保存：

- 扩散慢；
- 地下水流速低；
- 与浅层大气/氧化水交换少；
- residence time 可达百万年以上；
- noble gas 和盐水可记录古老流体系统。

因此，H2 的控制不是简单的孔隙度单调关系，而是一个“中间最优”问题：

```text
过低孔隙度：
  水少，产氢少。

过高孔隙度/高渗透率：
  水多，但 H2 易被冲走和稀释。

微裂隙发育但宏观低渗：
  水-岩界面大，局部产氢强，保存时间长。
```

这就是本报告提出的第一个理论观点：

> 辐解天然氢的最优介质不是最高孔隙度岩石，也不是完全致密岩石，而是“微裂隙-高界面面积-低宏观渗透率”的中间状态。

### 5.3 裂隙宽度的数学表达

对平行板裂隙，裂隙宽度为 `b`，水-岩界面面积与水体积比近似：

```text
a_s / V_w ≈ 2 / b
```

若 alpha 粒子有效射程为 `R_α`，则能与 alpha 能量耦合的水体比例可近似为：

```text
χ_α ≈ min(1, 2R_α / b)
```

因此对 alpha 主导的局部辐解：

```text
P_H2,α per water volume ∝ (2/b) × U_near_surface × G_α
```

裂隙越窄，单位水体积接收的界面辐射越高。Dzaugis et al. 2016 在玄武岩裂隙体系中也指出，微裂隙相对于厘米级裂隙可以显著提高按水体积归一的 H2 生成。

## 6. 化学反应网络：H2、H2O2、sulfate 和核素迁移

### 6.1 水辐解的一阶产物

水受电离辐射后：

```text
H2O --radiation--> e_aq^- + H• + •OH + H3O+ + OH^- + H2 + H2O2
```

关键还原性物种：

```text
e_aq^-
H•
H2
```

关键氧化性物种：

```text
•OH
H2O2
O2  secondary
```

这意味着辐解不是单向“还原 H2 生成”，而是同时创造还原剂与氧化剂。深部环境中它相当于一个持续工作的微型 redox battery。

### 6.2 H2 生成路径

主要 H2 形成反应可简化为：

```text
H• + H• -> H2
e_aq^- + H• + H2O -> H2 + OH^-
e_aq^- + e_aq^- + 2H2O -> H2 + 2OH^-
```

但这些反应要与复合和矿物表面捕获竞争：

```text
e_aq^- + •OH -> OH^-
H• + •OH -> H2O
e_aq^- + Fe(III) -> Fe(II)
H2O2 + Fe(II) -> Fe(III) + •OH + OH^-
```

### 6.3 硫化物氧化生成 sulfate

Li et al. 2016 在 Canadian Shield Kidd Creek 深部裂隙水中提出，辐解氧化剂可氧化 Archaean host rocks 中的硫化物，从而为深部微生物提供 sulfate。简化 pyrite 氧化式：

```text
FeS2 + 7H2O2 -> Fe2+ + 2SO4^2- + 2H+ + 6H2O
```

若用 radiolysis oxidants 代表：

```text
FeS2 + radiolytic oxidants(•OH, H2O2)
  -> SO4^2- + Fe2+/Fe3+ + acidity
```

这使系统出现一个关键耦合：

```text
radiolysis -> H2 electron donor
radiolysis + sulfide -> sulfate electron acceptor
H2 + sulfate -> microbial sulfate reduction
```

微生物硫酸盐还原可表示为：

```text
SO4^2- + 4H2 + H+ -> HS^- + 4H2O
```

所以，硫化物既能通过辐解氧化生成 sulfate，又能使 sulfate-reducing microbes 消耗 H2。其结果取决于 sulfate 生成和 H2 消耗之间的平衡。

### 6.4 对核素迁移的影响

U 在地下水中的迁移高度依赖 Eh-pH 和配位环境。

还原条件：

```text
U(IV) -> uraninite/coffinite-like phases
low solubility
immobile
```

氧化-碳酸盐条件：

```text
U(VI) -> UO2^2+ / uranyl carbonate complexes
mobile
```

氯盐水中还要考虑：

- chloride radiolysis；
- Ca-Na-Cl brine ionic strength；
- U(VI)-carbonate / Ca-uranyl-carbonate complexes；
- colloids；
- clay/bentonite adsorption；
- Fe(II)/Fe(III) redox buffering；
- sulfide/sulfate cycling。

辐解对核素迁移有双重作用：

```text
H2, e_aq^-, Fe(II), HS^- 可能促进 U(VI) 还原固定；
•OH, H2O2, O2 可能促进 U(IV) 或 sulfide 氧化，增强局部迁移。
```

在 Revell DGR 场景下，近场 used-fuel gamma 源项和天然 U-Th-K 背景源项必须区分：

```text
天然 U-Th-K：低剂量、长期、区域背景；
used fuel γ-field：早期较强、随 Cs-137 等衰变降低、近场控制。
```

## 7. 统一反应-迁移方程

### 7.1 H2 质量守恒

对裂隙-孔隙介质：

```text
∂(φ C_H2)/∂t
  = ∇ · (φ D_eff,H2 ∇C_H2)
    - ∇ · (q C_H2)
    + S_H2,rad
    + S_H2,serp
    + S_H2,mech
    - R_H2,microbe
    - R_H2,abiotic
    - R_H2,leak
    - R_H2,gas_partition
```

其中：

- `φ`：有效孔隙度；
- `C_H2`：溶解 H2 浓度；
- `D_eff,H2 = D_H2 / τ`：有效扩散系数；
- `q`：Darcy flux；
- `S_H2,rad`：辐解源项；
- `S_H2,serp`：蛇纹石化等水岩反应源项；
- `S_H2,mech`：断裂机械自由基产氢；
- `R_H2,microbe`：微生物消耗；
- `R_H2,abiotic`：矿物/氧化剂消耗；
- `R_H2,leak`：迁移泄漏；
- `R_H2,gas_partition`：气相析出/溶解项。

本报告重点是：

```text
S_H2,rad = 1.036×10^-7 × G_H2 × A_RHP × f_w
```

若使用年为单位，还需乘以 `31,557,600 s yr^-1`。

### 7.2 sulfate 质量守恒

```text
∂(φ C_SO4)/∂t
  = ∇ · (φ D_eff,SO4 ∇C_SO4)
    - ∇ · (q C_SO4)
    + S_SO4,rad-sulfide
    + S_SO4,external
    - R_SO4,MSR
    - R_SO4,precipitation
```

其中：

```text
R_SO4,MSR ≈ k_MSR C_SO4 C_H2^n f(T, pH, salinity)
```

高盐、低孔、低 sulfate 的 Revell 环境可能使 `R_SO4,MSR` 很低；Kidd Creek 硫化物更丰富、裂隙更开放，则 sulfate-supported habitability 更强。

### 7.3 H2 气体压力风险

若 H2 溶解达到饱和并产生自由气体，相态分配受 Henry 定律控制：

```text
C_H2,aq = H_H2(T, salinity) × P_H2
```

当净生成超过溶解、扩散和消耗能力：

```text
∫(S_H2,total - R_H2,total) dt > C_H2,saturation × φV
```

系统可能形成气相 H2，导致：

- 局部气压升高；
- 有效渗透率变化；
- 对密封材料或缓冲材料产生气体迁移压力；
- 对核废料库 safety case 构成气体源项。

但对 Revell 天然背景 U-Th-K 来说，`1.6 nmol m^-3 yr^-1` 级别的源项极小。真正需要重点模拟的是：

```text
天然背景源项 + 处置库近场 γ 辐解源项 + 容器腐蚀产氢 + 微生物/矿物消耗
```

## 8. Revell 与 Athabasca 的定量比较

### 8.1 Revell：低孔低渗端元

Revell 的关键控制逻辑：

```text
普通到中等 U-Th-K 生热
× 极低孔隙率
× 低裂隙水体积
× 低硫化物
× 低 sulfate co-production
= 极低 H2 和 sulfate 生成
```

按 2025 论文：

```text
H2 ≈ 1.6 nmol m^-3 rock yr^-1
```

解释：

- 对微生物：只可能支持很低水平生物活动；
- 对天然 H2 资源：几乎没有经济意义；
- 对 DGR：仍需纳入长期气体和氧化还原背景项，因为时间尺度可达 `10^5-10^6 yr`；
- 对方法学：是 Monte Carlo radiolysis-source 模型的优秀 benchmark。

### 8.2 Athabasca：局部热点端元

Athabasca 不应直接套用 Revell 的低产率，因为它包含：

- U-rich basin brines；
- 高品位铀矿；
- U-bearing monazite、uraninite、zircon、apatite、xenotime 等附件矿物；
- graphitic/sulphidic shear zones；
- 伟晶质/花岗质富 K-U-Th 岩体；
- 断裂控制的深部盐水循环；
- 局部热-构造边界。

但也不能简单认为 Athabasca 会形成可采 H2。决定因素是：

```text
是否存在可与富 U/Th/K 矿物长期接触的裂隙水；
H2 是否能避开 sulfate reduction、methanogenesis、Fe/S redox sinks；
是否有区域 sealing 和 trap；
是否存在可观的气体聚集或高流量泉/井。
```

### 8.3 计算场景表

本报告建立了一个初步情景表，保存在：

```text
data/processed/radiolytic_h2_scenario_table.csv
```

主要场景：

| 场景 | H2 产率 | 解释 |
|---|---:|---|
| Revell 2025 most probable | `1.6 nmol m^-3 yr^-1` | 公开论文结果，低孔低渗 |
| 普通上地壳花岗岩 | `~1.3 nmol m^-3 yr^-1` | Revell-like 低 water-energy interception |
| Athabasca 平均 felsic intrusive | `~8 nmol m^-3 yr^-1` | 假设更好微裂隙接触 |
| Athabasca 伟晶质/富放射性样品 | `~107 nmol m^-3 yr^-1` | 局部热点情景 |
| U 矿化微裂隙 halo | `~1630 nmol m^-3 yr^-1` | 概念热点，不代表 bulk rock |

这些数值是源项量级，不是储量。它们说明：

```text
H2 source term can vary by >1000× locally,
but economic accumulation still requires migration + trapping + low sink.
```

## 9. 理论创新：RHSI 和两个平衡指标

### 9.1 Radiolytic Hydrogen System Index

提出：

```text
RHSI =
  [A_RHP × f_w × G_H2]
  × [τ_res / τ_diff]
  × [C_sat / C_background]
  / [1 + Da_sink]
```

其中：

```text
A_RHP = radiogenic heat production
f_w = fraction of decay energy deposited in water
G_H2 = radiolytic H2 yield
τ_res = groundwater residence time
τ_diff = diffusion/leakage time scale
C_sat = H2 saturation concentration at P-T-salinity
C_background = measured or expected H2 background
Da_sink = sink Damköhler number
```

其中：

```text
Da_sink = k_sink τ_res
```

若：

```text
Da_sink >> 1
```

说明 H2 生成后快速被微生物、硫酸盐、铁氧化物或其它氧化剂消耗，不易积累。

若：

```text
Da_sink << 1
```

说明保存潜力较好。

这个指标把天然氢评价从“源岩是否富 U”推进为“完整系统是否允许 H2 积累”。

### 9.2 H2-sulfate redox balance number

对 sulfate reduction：

```text
SO4^2- + 4H2 + H+ -> HS^- + 4H2O
```

定义：

```text
B_RS = 4 P_SO4 / P_H2
```

若：

```text
B_RS << 1
```

H2 过剩，sulfate 不足，可能有 H2 积累或转向 methanogenesis。

若：

```text
B_RS ≈ 1
```

H2 与 sulfate 近似配平，适合 sulfate-reducing biosphere。

若：

```text
B_RS >> 1
```

sulfate/oxidant 过剩，H2 难保存。

Revell 的 sulfate 产量被估计为远低于 Kidd Creek，因此其 `B_RS` 可能偏低，但 H2 源项本身也很低；Kidd Creek 则是 H2 与 sulfate redox cycling 的强端元。

### 9.3 Radiolytic uranium mobility feedback

对 Athabasca，可提出第二个创新假说：

> 富 U 基底不仅是铀矿化的结果，也会在后期长期产生辐解 redox halo，改变局部 U、Fe、S、C 的价态和迁移性。

概念路径：

```text
U-rich mineralization / U-bearing accessory minerals
  -> alpha/gamma radiolysis of microfracture water
  -> H2 + H2O2 + •OH
  -> sulfide oxidation to sulfate
  -> Fe(II)/Fe(III) cycling
  -> U(VI)/U(IV) local redox cycling
  -> secondary uranium remobilization or immobilization halos
```

这对铀矿勘探和核废料库都有意义：

- 对勘探：可寻找 radiolytic redox halo 的矿物学和同位素指纹；
- 对核废料库：可评估长期辐解对 U、Ra、Rn、I、Se、Tc 等核素迁移的影响；
- 对天然 H2：可识别 H2 生成、sulfate 生成和 H2 消耗的空间耦合。

## 10. 可检验预测

本报告的理论不是任意猜想，可形成如下可检验预测。

### 10.1 Revell 预测

1. 深部 fracture water 中 H2 应为低浓度或低通量，除非与容器腐蚀/工程源项叠加。
2. sulfate 生成应受硫化物含量限制，整体低于 Kidd Creek。
3. H2 与 radiogenic noble gases 不一定强相关，因为低孔低渗下气体释放和流体连通受限。
4. 若存在 H2 局部异常，应与微裂隙密度、U/Th/K 富集矿物和界面面积更相关，而不是 bulk granite average。
5. Cl- radiolysis 和 bentonite/copper interactions 在 DGR 近场比天然背景 U-Th-K 更重要。

### 10.2 Athabasca 预测

1. U-rich pegmatite、monazite/apatite/xenotime-bearing orthogneiss 和 uraninite-bearing shear zones 的 fracture waters 应有更高 H2 背景或更强 H2 generation potential。
2. Graphitic/sulphidic shear zones 中 sulfate、S isotopes、Fe redox 和 H2 可能形成耦合异常。
3. 高 gamma logs 不一定对应高 H2；只有与 connected microfracture water 和 low flushing 同时出现才会增强 H2 保存。
4. U-rich brines 的古流体路径可能同时是 U 迁移通道和长期 radiolytic redox reaction zones。
5. 若 H2 长期被 sulfate reduction 消耗，应出现 δ34S、Δ33S、δD-H2、CH4 isotopologues、dissolved inorganic carbon 等生物/非生物耦合指纹。

## 11. 实验和数据方案

### 11.1 岩石和水样分析

对 Revell 与 Athabasca 基底岩，应建立统一分析包：

岩石：

- U, Th, K：ICP-MS / ICP-OES / gamma spectrometry；
- 全岩主微量；
- 矿物学：XRD, SEM-EDS, EPMA；
- 放射性附件矿物：zircon, monazite, apatite, xenotime, uraninite；
- sulfide abundance：pyrite, pyrrhotite, chalcopyrite；
- porosity/permeability：He pycnometry, MICP, micro-CT；
- fracture aperture distribution；
- gamma log / spectral gamma；
- density, thermal conductivity。

地下水：

- H2, CH4, He, Ne, Ar, N2, CO2；
- Cl, Br, SO4, sulfide, Fe(II)/Fe(III)；
- pH, Eh, alkalinity, salinity；
- U, Ra, Rn, Sr, Ba, Ca, Na, Mg；
- δD-H2, δ13C-CH4, clumped isotopes；
- δ34S, δ18O-SO4, Δ33S, Δ36S；
- noble gas residence ages；
- ^14C, ^36Cl, ^129I where applicable。

### 11.2 实验室辐解实验

设计：

```text
core powder / fracture chip / intact microfracture core
+ synthetic Revell brine or Athabasca brine
+ controlled gamma or alpha source
+ anoxic sealed reactor
+ variable temperature, salinity, pH, sulfide abundance
```

测量：

- H2 generation rate；
- H2O2；
- sulfate；
- Fe(II)/Fe(III)；
- U redox/speciation；
- gas-liquid partition；
- isotope fractionation；
- microbial sterile vs non-sterile contrast。

重点实验矩阵：

| 变量 | 水平 | 目的 |
|---|---|---|
| U-Th-K | low / average / pegmatitic / mineralized | 源项响应 |
| 裂隙宽度 | 1 µm / 10 µm / 100 µm / 1 mm | interface geometry |
| 水化程度 | dry / adsorbed water / saturated | 水体积控制 |
| 硫化物 | absent / pyrite / pyrrhotite / mixed sulfides | sulfate co-production |
| 盐度 | dilute / 0.1 M Cl / high brine | chloride radiolysis |
| 温度 | 25 / 60 / 90 / 120 °C | 地热长期反应 |
| 微生物 | sterile / inoculated / inhibitor | H2 sink |

### 11.3 建模方案

建立三层模型：

1. **微尺度 Monte Carlo radiation transport**  
   模拟 alpha/beta/gamma 能量沉积到矿物、水和界面的比例。

2. **孔隙-裂隙反应迁移模型**  
   解 H2、H2O2、SO4、Fe、U、microbial sink 的耦合 PDE。

3. **区域尺度保存模型**  
   以断裂网络、地下水流、盖层和 solubility/trapping 评估 H2 是否能积累。

## 12. 对天然氢资源的判断

### 12.1 Revell

Revell 的辐解 H2 源项过低，且低孔低渗使商业采集没有现实意义。其价值是：

- DGR background gas and redox term；
- low-habitability endmember；
- Monte Carlo framework benchmark；
- crystalline rock safety case。

结论：

```text
Revell 不应作为天然 H2 勘探靶区；
应作为低孔低渗结晶岩辐解-硫循环-核废料安全的定量基准。
```

### 12.2 Athabasca Basin basement

Athabasca 有更强的局部源项条件，但商业天然 H2 仍未成立。其潜在价值排序：

1. 深部微生物生态和地球化学研究；
2. 铀矿成矿后期 redox halo 和 U 迁移研究；
3. 放射性源项与地下水长期反应；
4. 核废料库 analog；
5. 作为天然 H2 勘探的理论端元，而非直接资源靶区。

若要找天然 H2 异常，优先筛选：

```text
U-Th-K high heat production
+ connected microfractures
+ old saline groundwater
+ low hydraulic flushing
+ low microbial/sulfate sink
+ gas trap or sealed fracture compartment
```

而不是只找：

```text
highest uranium grade
```

因为最高铀矿化区往往伴随强烈结构、流体和硫化物体系，H2 可能被快速消耗或泄漏。

## 13. 对核废料处置库的判断

DGR 中 H2 可来自多源：

```text
natural U-Th-K radiolysis
used-fuel gamma radiolysis
container corrosion
steel/bentonite/water reaction
microbial processes
```

天然 U-Th-K 背景源项通常较低，但不可忽略，因为时间尺度长。安全评估更关心：

- H2 与 O2/H2O2 对容器腐蚀的影响；
- gas pressure 是否改变 buffer 和 fracture flow；
- sulfate reduction 是否产生 sulfide 腐蚀风险；
- chloride radiolysis 是否改变 oxidant chemistry；
- bentonite 是否吸附、催化或缓冲 radiolysis products；
- U/Ra/Rn/I/Se/Tc 等核素是否因 redox 改变迁移性。

本报告建议 DGR 模型中引入：

```text
background radiolytic redox source term
+ near-field engineered source term
+ microbially mediated H2-sulfate sink
+ gas phase emergence threshold
```

而不是只把 H2 看成单独气体问题。

## 14. 最有建设性的观点

### 14.1 观点一：辐解 H2 是“系统属性”，不是“岩石属性”

传统思路容易问：

```text
这块岩石 U-Th-K 高不高？
```

更正确的问题是：

```text
U-Th-K 释放的能量有多少沉积到水中？
H2 生成后是否能在水-岩系统中保存？
是否被 sulfate, Fe(III), CO2 或微生物快速消耗？
是否有封闭断裂或 trap 让低通量长期积累？
```

### 14.2 观点二：Athabasca 可作为“辐解红氧化带”天然实验室

Athabasca 的传统研究重点是铀矿成矿。新的课题可改写为：

```text
高品位 U 省在成矿后数亿至十亿年尺度上，
是否持续通过辐解改变地下水、硫循环、H2、CH4 和 U 迁移？
```

这把铀矿省从“静态矿体”变成“长期 redox reactor”。

### 14.3 观点三：sulfide 对 H2 是双刃剑

硫化物越多：

- radiolytic oxidants 可生成更多 sulfate；
- sulfate-reducing microbes 有更多电子受体；
- H2 更可能被消耗；
- 但深部生物圈更可能维持。

所以：

```text
高硫化物 = 高 habitability 潜力
高硫化物 ≠ 高 H2 保存潜力
```

Revell 低硫化物导致 sulfate-supported habitability 低；Kidd Creek 高硫化物使 sulfate cycling 强；Athabasca graphitic/sulphidic shear zones 可能处于中间到强端元。

### 14.4 观点四：天然氢勘探应引入“低通量长期积分”思维

即时产率很低不代表 geologic cumulative inventory 一定为零。

累积量：

```text
M_H2,cum = ∫ P_H2,net dt
```

若：

```text
P_H2,net = 1.6 nmol m^-3 yr^-1
V = 1 km3
t = 1 Ga
```

则：

```text
n_H2 = 1.6×10^-9 × 10^9 × 10^9
     = 1.6×10^9 mol
m_H2 ≈ 3.2×10^6 kg
     ≈ 3,200 tonnes
```

这只是理论总产量，现实中会被泄漏和消耗显著削弱。它说明 Revell 类低通量体系对能源意义仍弱；但若局部源项提高 `100-1000×`，又有封闭 trap，则天然 H2 研究才可能进入资源讨论。

## 15. 数据缺口

本报告仍有以下缺口：

1. 未提取 Higgins et al. 2025 全文 supplementary Monte Carlo input distributions；
2. Revell borehole U-Th-K、硫化物、孔隙度、微裂隙宽度、地下水 H2/SO4 原始表未被解析；
3. Athabasca 基底样品的 U-Th-K 与 fracture water H2 数据未形成统一数据库；
4. CDoGS 在当前 GeoMine MCP 版本中只完成数据源规划，未执行实时空间查询；
5. 没有将 gamma logs 与 fracture aperture / water inflow intervals 联合建模；
6. 未建立气体相态和 pressure evolution 的完整 numerical model；
7. 未加入 microbial kinetic parameters 的温度-盐度-营养限制；
8. 未区分天然背景辐解与核废料近场 gamma 源项的时空叠加；
9. 未做 U-series disequilibrium、Rn escape、He accumulation 的联合反演。

## 16. 下一步工作计划

### 16.1 数据工作

1. 下载并解析 Higgins et al. 2025 supplementary data；
2. 获取 Revell NWMO borehole geochemistry、fracture log、groundwater chemistry；
3. 下载 Mendeley Athabasca felsic intrusive geochemistry table；
4. 整理 Athabasca uranium geochemistry database；
5. 建立 `sample_id - U - Th - K - density - lithology - porosity - sulfide - gamma_log - fracture_water` 的统一表。

### 16.2 模型工作

1. 复现 Revell Monte Carlo；
2. 构建 Athabasca 基底情景模型；
3. 将 `f_w` 从经验参数变成 micro-CT / fracture aperture 派生参数；
4. 加入 sulfate co-production；
5. 加入 microbial sink；
6. 加入 Henry law 和 gas pressure threshold。

### 16.3 野外和实验

1. Revell：选择不同岩性、不同 fracture density core 做低剂量辐解实验；
2. Athabasca：选择 U-rich pegmatite、graphitic shear、uraninite halo、fresh granite/gneiss 对照；
3. 进行 sterile / non-sterile 对照；
4. 测 H2、H2O2、SO4、Fe、U、Rn、He；
5. 用 sulfur isotopes 和 noble gases 判别长期封闭性。

## 17. 结论

本研究的结论可以压缩成三句话：

```text
Revell Batholith 证明：低孔低渗结晶岩中 U-Th-K 辐解 H2 可以量化，但产率极低，主要意义是深部生物圈和核废料库安全。

Athabasca Basin 基底岩提供更强的局部源项和更复杂的 U-fluid-redox system，适合作为 radiolytic H2 hotspot 和 radiolytic redox halo 的天然实验室。

未来研究不应只追求最高 U-Th-K，而应同时评估 interface geometry、groundwater residence、sulfide/sulfate sink、microbial activity 和 gas retention。
```

最具创新性的研究方向是：

> 建立“放射性源项-微裂隙水-硫化物氧化-sulfate reduction-H2 保存/消耗”的统一反应迁移模型，并用 Revell 作为低孔低渗端元、Athabasca 作为富 U 红氧化端元、Kidd Creek 作为硫化物-深部生物圈强端元进行三端元校准。

这个方向可以同时服务于：

- 天然 H2 科学；
- 铀矿省长期地球化学演化；
- 深部生物圈；
- 核废料处置库气体和 redox safety case；
- 行星宜居性 analog。

## 18. 输出文件

本次研究输出：

- `radiolytic_natural_hydrogen_revell_athabasca_research_report_zh.md`：本报告；
- `evidence_matrix.csv`：证据矩阵；
- `data/processed/radiolytic_h2_scenario_table.csv`：辐解 H2 量级情景表。

## 19. 主要来源

1. Higgins, P. M., Song, M., Warr, O., & Sherwood Lollar, B. 2025. *Natural H2 and Sulfate Production via Radiolysis in Low Porosity and Permeability Crystalline Rocks*. Journal of Geophysical Research: Biogeosciences. DOI: https://doi.org/10.1029/2025JG008863
2. Revell Batholith / NWMO site page: https://www.nwmo.ca/en/site-selection/about-the-site
3. Briggs, S., Behazin, M., & King, F. 2025. *Validation of Water Radiolysis Models Against Experimental Data in Support of the Prediction of the Radiation-Induced Corrosion of Copper-Coated Used Fuel Containers*. https://www.mdpi.com/2624-5558/6/2/14
4. Le Caer, S. 2011. *Water Radiolysis: Influence of Oxide Surfaces on H2 Production under Ionizing Radiation*. https://www.mdpi.com/2073-4441/3/1/235
5. Dzaugis, M. E. et al. 2016. *Radiolytic Hydrogen Production in the Subseafloor Basaltic Aquifer*. https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2016.00076/full
6. Lin, L.-H. et al. 2005. *Radiolytic H2 in continental crust: Nuclear power for deep subsurface microbial communities*. DOI: https://doi.org/10.1029/2004GC000907
7. Li, L. et al. 2016. *Sulfur mass-independent fractionation in subsurface fracture waters indicates a long-standing sulfur cycle in Precambrian rocks*. https://www.nature.com/articles/ncomms13252
8. Chi, G. et al. 2019. *Uranium-rich diagenetic fluids provide the key to unconformity-related uranium mineralization in the Athabasca Basin*. https://www.nature.com/articles/s41598-019-42032-0
9. Powell, J. et al. 2025. *Supplementary data for Age, Geochemistry and Radiogenic Heat Production of Felsic Intrusive Rocks from the Eastern Athabasca Basin, Saskatchewan*. https://data.mendeley.com/datasets/h7n6s6p29y
10. Mushayandebvu, M. et al. 2023. *Subsurface geometry of the Revell Batholith by constrained geophysical modelling, NW Ontario, Canada*. https://www.sciencedirect.com/science/article/pii/S2590197423000101
11. Villamizar, B. J. G. et al. 2023. *Spatial Characterization of Shallow Structures in the Revell Batholith Integrating Seismic Imaging Techniques*. https://link.springer.com/article/10.1007/s00024-023-03382-z
12. Rybach heat-production formula example: https://link.springer.com/article/10.1186/s40517-023-00273-3
