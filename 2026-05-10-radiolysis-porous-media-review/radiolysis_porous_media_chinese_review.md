# 多孔介质中水辐解、电子迁移与 G 值变化：简要文献综述与控制方程推导

日期：2026-05-10  
主题：Radiolysis in porous media；water radiolysis；electric-field-driven electron separation；G-value modification  
说明：本文为学术性技术综述和机理推导，不构成特定工程系统的安全评估或辐射化学设计结论。具体体系仍需结合辐射类型、LET、剂量率、孔径分布、矿物表面化学、pH、离子强度、温度和实验 G 值标定。

## 1. 问题背景

水辐解是指水分子在电离辐射作用下产生一系列短寿命自由基、溶剂化电子和长寿命分子产物的过程。典型初级产物包括：

```text
e_aq^-, •OH, H•, H3O+, OH^-, H2, H2O2
```

在 bulk water 中，辐解产物首先在纳米尺度的 spur 或 track 中产生，随后经历扩散、复合、反应和逃逸。经典辐射化学通常用 G 值描述产额：

```text
G_i = 每 100 eV 吸收能量产生或净生成的第 i 种分子数
```

在多孔介质中，问题变得更复杂。孔壁、电双层、表面电荷、孔径限制、矿物表面反应、孔隙水结构变化和局部电场都会影响初级产物的复合和逃逸。因此，多孔介质中的辐解不能简单看作 bulk water 的缩小版本。

本文特别关注一个关键问题：

> 辐解产生的电子 `e_aq^-` 是带电粒子。若多孔介质中存在内建电场或外加电场，电子会发生定向迁移，从而改变其与 `H3O+`、`•OH`、`H•` 等初级产物的复合概率。这种电场诱导的空间分离会如何改变长寿命产物的 G 值？

## 2. 简要文献综述

### 2.1 Bulk water radiolysis

水辐解的经典研究已经建立了较完整的反应网络。辐射能量沉积后，水在飞秒至皮秒尺度产生激发态、离子化态和低能电子；随后电子溶剂化，形成 `e_aq^-`。在纳秒至微秒尺度，`e_aq^-`、`•OH`、`H•` 等短寿命物种发生扩散和反应，最终形成较长寿命产物，例如 `H2`、`H2O2`、`O2`、`HO2•/O2•^-` 等。

Buxton 等人整理了大量水相自由基反应速率常数。Le Caër 的综述则系统总结了水辐解、氧化物界面、核废料和材料腐蚀相关的辐射化学过程。

bulk water 中的重要认识是：

- 低 LET 辐射中，spurs 稀疏，更多自由基逃逸，`e_aq^-` 和 `•OH` 的逃逸产额较高。
- 高 LET 辐射中，track 内局部浓度高，复合反应更强，`H2` 和 `H2O2` 等分子产物更容易增加。
- 初级产物的最终 G 值不是单纯的生成量，而是生成、复合、扩散、反应和边界损失共同决定的净产额。

### 2.2 Confined water 与 porous media radiolysis

多孔介质中水辐解的研究集中在 silica nanopores、oxide/water interface、clay/cement pore water、核废料环境和辐射催化体系。已有研究表明：

- 孔隙限制会改变自由基扩散和复合几率。
- 固体表面可以捕获电子或自由基，也可以催化 `H2` 或 `H2O2` 生成。
- 氧化物、硅胶、黏土、金属氧化物等界面可改变初级产额。
- 孔径达到纳米尺度时，孔壁电荷和电双层会使孔内电场达到足以影响电子迁移的程度。

Rotureau 等研究了受限水中分子氢的生成；Foley 等关注受限水中 `•OH` 的形成和反应性；Ouerdane 等通过模拟讨论多孔 silica 中水辐解及电子捕获/水捕获对产额的影响。总体上，多孔介质既可能提高某些长寿命产物的 G 值，也可能由于表面淬灭而降低水相可测产额。

### 2.3 Onsager geminate recombination 与电场效应

Onsager 理论描述了电离后正负电荷对的 geminate recombination。若电子与其正电荷母体距离较近，则 Coulomb 吸引会增加复合概率；若电场或热扩散使两者分离，则电子逃逸概率增加。

在多孔介质中，孔壁电荷、电双层、外加电势或辐射诱导电荷积累都可能产生局部电场。因此，`e_aq^-` 的漂移不再可以忽略。该漂移会影响：

- `e_aq^- + H3O+ -> H• + H2O`
- `e_aq^- + •OH -> OH^-`
- `e_aq^- + H• + H2O -> H2 + OH^-`
- 电子被孔壁、缺陷位点、金属离子或半导体表面捕获

这些过程最终会影响 `H2`、`H2O2` 和其它长寿命 redox products 的 G 值。

## 3. 初级水辐解反应

水辐解的初级过程可概括为：

```text
H2O --radiation--> e_aq^- + •OH + H• + H3O+ + OH^- + H2 + H2O2
```

其中：

- `e_aq^-` 是强还原性物种。
- `•OH` 是强氧化性自由基。
- `H•` 既可作为还原性自由基，也可与其它自由基生成 `H2`。
- `H2` 和 `H2O2` 是较长寿命分子产物。

在早期 spur 中，产物的局部浓度非常高，因此二级反应速度极快。典型速率常数为 `10^9 - 10^10 M^-1 s^-1` 量级。

## 4. 多孔介质中的通用输运-反应方程

设多孔介质孔隙率为 `ε`，曲折度为 `τ`，孔隙水中第 `i` 个物种浓度为 `c_i`。其控制方程可写为：

```text
∂(ε c_i)/∂t = -∇·N_i + ε S_i^rad + ε Σ_j ν_ij R_j - a_s J_i,s
```

其中：

- `N_i`：物种 `i` 的通量。
- `S_i^rad`：辐解源项。
- `ν_ij`：第 `j` 个反应中物种 `i` 的化学计量数。
- `R_j`：第 `j` 个反应速率。
- `a_s`：单位孔隙体积的固液界面面积。
- `J_i,s`：物种 `i` 在孔壁表面的吸附、捕获、催化或淬灭通量。

若考虑扩散、迁移和对流，则：

```text
N_i = -ε D_i/τ ∇c_i - ε z_i u_i F c_i ∇Φ + ε c_i v
```

其中：

- `D_i`：水相扩散系数。
- `D_i/τ`：有效扩散系数。
- `z_i`：电荷数。
- `u_i`：迁移率。
- `F`：Faraday 常数。
- `Φ`：电势。
- `v`：孔隙水速度。

利用 Einstein 关系：

```text
u_i = D_i/(RT)
```

可写成 Nernst-Planck 形式：

```text
N_i = -ε D_eff,i [∇c_i + (z_i F/RT)c_i ∇Φ] + ε c_i v
```

其中：

```text
D_eff,i = D_i/τ
```

若体系中无明显对流，则 `v ≈ 0`，通量主要由扩散和电迁移控制。

## 5. 电势方程：Poisson 方程

电场由电势给出：

```text
E = -∇Φ
```

孔隙水中的电势满足 Poisson 方程：

```text
-∇·(ε_m ∇Φ) = F ε Σ_i z_i c_i + ρ_fixed
```

其中：

- `ε_m`：介质有效介电常数。
- `ρ_fixed`：孔壁固定电荷或表面电荷等效体电荷密度。

在许多多孔介质中，孔壁带电会形成电双层。若孔径接近 Debye length，电双层可能重叠，使整个孔内都处于非零电场环境。此时 `e_aq^-` 的迁移不能忽略。

## 6. 辐解源项与 G 值换算

G 值定义为每 `100 eV` 吸收能量产生的分子数。若吸收剂量率为 `Ddot_w`，水密度为 `ρ_w`，则单位体积单位时间吸收能量为：

```text
ρ_w Ddot_w       [J m^-3 s^-1]
```

每 `100 eV` 的能量为：

```text
100 eV = 100 × 1.602 × 10^-19 J = 1.602 × 10^-17 J
```

每焦耳对应的摩尔数换算为：

```text
1 / [(1.602 × 10^-17) N_A] ≈ 1.036 × 10^-7 mol J^-1
```

因此，辐解源项为：

```text
S_i^rad = 1.036 × 10^-7 ρ_w Ddot_w G_i
```

单位为：

```text
mol m^-3 s^-1
```

该式说明：`G_i` 不只是实验报告中的经验量，也可直接进入连续介质反应-输运方程。

## 7. 主要复合与积分反应网络

初级产物在早期主要通过以下反应被消耗或转化：

```text
e_aq^- + e_aq^- + 2H2O -> H2 + 2OH^-
```

```text
e_aq^- + H• + H2O -> H2 + OH^-
```

```text
H• + H• -> H2
```

```text
e_aq^- + •OH -> OH^-
```

```text
e_aq^- + H3O+ -> H• + H2O
```

```text
•OH + •OH -> H2O2
```

```text
•OH + H• -> H2O
```

```text
H3O+ + OH^- -> 2H2O
```

如果存在溶解氧，还需加入：

```text
e_aq^- + O2 -> O2•^-
```

```text
H• + O2 -> HO2•
```

这些反应会竞争消耗 `e_aq^-`、`•OH` 和 `H•`。最终长寿命产物 `H2` 与 `H2O2` 的产率取决于这些反应的相对速率、空间分布和边界损失。

## 8. 简化动力学推导

以 `e_aq^-` 为例，其浓度方程可写为：

```text
∂(ε c_e)/∂t =
∇·[ε D_eff,e ∇c_e + ε (F D_eff,e/RT)c_e ∇Φ]
+ ε S_e^rad
- ε k_eOH c_e c_OH
- ε k_eH c_e c_H
- ε k_eH3O c_e c_H3O
- 2ε k_ee c_e^2
- a_s J_e,s
```

注意电子电荷数 `z = -1`，因此电迁移项方向与正离子相反。若写成漂移速度：

```text
v_d,e = μ_e E
```

其中：

```text
μ_e = D_e F / RT
```

则电场使电子在 spur 中产生定向位移。对于 `•OH`：

```text
∂(ε c_OH)/∂t =
∇·(ε D_eff,OH ∇c_OH)
+ ε S_OH^rad
- ε k_eOH c_e c_OH
- 2ε k_OHOH c_OH^2
- ε k_OHH c_OH c_H
- a_s J_OH,s
```

对于 `H2O2`：

```text
∂(ε c_H2O2)/∂t =
∇·(ε D_eff,H2O2 ∇c_H2O2)
+ ε S_H2O2^rad
+ ε k_OHOH c_OH^2
- ε R_loss,H2O2
- a_s J_H2O2,s
```

对于 `H2`：

```text
∂(ε c_H2)/∂t =
∇·(ε D_eff,H2 ∇c_H2)
+ ε S_H2^rad
+ ε k_HH c_H^2
+ ε k_eH c_e c_H
+ ε k_ee c_e^2
- a_s J_H2,s
```

这些式子表明：电场通过改变 `c_e` 的空间分布，间接改变 `H2` 和 `H2O2` 的净生成。

## 9. 电场对电子逃逸的无量纲判据

判断电场是否重要，可比较电迁移能与热能。定义特征长度 `ℓ`，例如 spur 尺度或孔径尺度。无量纲电场强度为：

```text
Pe_E = |z| F E ℓ / RT
```

其中 `Pe_E` 类似电迁移 Péclet 数。若：

```text
Pe_E << 1
```

则热扩散主导，电场影响较弱。若：

```text
Pe_E ≳ 1
```

则电迁移可显著改变带电物种分布。

在 25 °C 下：

```text
RT/F ≈ 25.7 mV
```

若 `ℓ = 10 nm`，则使 `Pe_E ≈ 1` 的电场约为：

```text
E ≈ 25.7 mV / 10 nm ≈ 2.6 × 10^6 V/m
```

即：

```text
E ≈ 2.6 MV/m
```

纳米孔中的电双层电场可达到 `10^6 - 10^8 V/m`，因此该效应在多孔介质中是现实可行的。

## 10. 电子漂移距离估算

以溶剂化电子扩散系数为：

```text
D_e ≈ 5 × 10^-9 m^2/s
```

则：

```text
μ_e = D_e F / RT
```

在 25 °C 下：

```text
μ_e ≈ 1.9 × 10^-7 m^2 V^-1 s^-1
```

若孔内电场为：

```text
E = 10^7 V/m
```

则电子漂移速度为：

```text
v_d,e = μ_e E ≈ 1.9 m/s
```

电子在时间 `t` 内的漂移距离为：

```text
L_d = μ_e E t
```

当：

```text
t = 1 ns
```

时：

```text
L_d ≈ 1.9 nm
```

当：

```text
t = 10 ns
```

时：

```text
L_d ≈ 19 nm
```

这与 spur 尺度和纳米孔尺度相当。因此，孔内电场可以在早期复合发生之前，将电子从其正电荷母体或 `•OH` 附近拉开。

## 11. 电场如何改变 G 值

### 11.1 对 `G(e_aq^-)` 的影响

电场使电子远离 `H3O+`、`•OH` 和其它正电荷/氧化性物种，从而降低以下反应概率：

```text
e_aq^- + H3O+ -> H• + H2O
```

```text
e_aq^- + •OH -> OH^-
```

因此，电子逃逸产额通常增加：

```text
G_escape(e_aq^-) ↑
```

这是最稳健的判断。

### 11.2 对 `G(•OH)` 的影响

若电子被电场带走，则 `e_aq^- + •OH` 复合减少，`•OH` 的逃逸概率增加：

```text
G_escape(•OH) ↑
```

但若孔壁强烈吸附或淬灭 `•OH`，则水相可测 `•OH` 产额可能降低。因此：

```text
inert pore wall: G(•OH escape) ↑
reactive pore wall: aqueous G(•OH) may ↓
```

### 11.3 对 `G(H2O2)` 的影响

`H2O2` 的主要生成路径之一是：

```text
•OH + •OH -> H2O2
```

电场减少 `e_aq^- + •OH` 后，更多 `•OH` 可存活并二聚生成 `H2O2`。因此，在惰性孔壁中：

```text
G(H2O2) ↑
```

但若孔壁分解或吸附 `H2O2`，例如过渡金属氧化物表面催化分解，则：

```text
measured aqueous G(H2O2) ↓
```

所以 `H2O2` 的方向依赖于孔壁表面化学。

### 11.4 对 `G(H2)` 的影响

`H2` 可由以下路径生成：

```text
H• + H• -> H2
```

```text
e_aq^- + H• + H2O -> H2 + OH^-
```

```text
e_aq^- + e_aq^- + 2H2O -> H2 + 2OH^-
```

电场对 `H2` 的影响不一定单调。

若电子被迁移到可催化质子还原或水还原的表面，则：

```text
G(H2) ↑
```

但若电子被孔壁缺陷、矿物表面或金属离子捕获，并未转化为 `H2`，则：

```text
G(H2) ↓ 或不变
```

因此，`H2` 的 G 值最依赖材料表面性质。

## 12. 多孔介质与 bulk water 的差异

### 12.1 多孔介质可能增强辐解表现的原因

多孔介质可能提高某些长寿命产物的表观 G 值，原因包括：

- 电双层电场促进电子和氧化性自由基空间分离。
- 孔壁可捕获电子并催化 `H2`。
- 固体相吸收辐射后产生的低能电子可能注入孔隙水。
- 纳米孔限制扩散，使特定反应路径更集中。
- 孔内局部 pH、离子强度和电势可改变反应速率。

### 12.2 多孔介质可能降低辐解表现的原因

多孔介质也可能降低水相可测产物：

- 孔壁淬灭 `e_aq^-`、`•OH` 或 `H•`。
- `H2O2` 被金属氧化物表面分解。
- 电子被缺陷态捕获，形成非生产性陷阱。
- 孔隙曲折度降低扩散，使产物更容易与表面反应。
- 孔径过小导致水结构改变，初级产物溶剂化和迁移行为不同于 bulk water。

## 13. 综合判断

### 13.1 G 值如何变化

在存在强孔内电场、且孔壁不强烈淬灭自由基的情况下，预期趋势为：

| 物种或产物 | G 值趋势 | 判断 |
|---|---|---|
| `e_aq^-` escape | 增加 | 电场促进电子逃逸，减少 geminate recombination。 |
| `•OH` escape | 通常增加 | 电子远离后，`e_aq^- + •OH` 减少。 |
| `H2O2` | 惰性孔中增加；活性孔壁中可能降低 | 取决于 `•OH` 是否能二聚，以及孔壁是否分解 `H2O2`。 |
| `H2` | 不确定 | 若表面催化电子转化为氢则增加；若表面只是非生产性捕获电子则降低。 |
| 氧化/还原空间分离 | 增加 | 这是最稳定的趋势。 |

### 13.2 多孔介质辐解相对 bulk water 的表现

多孔介质中的辐解不是简单地“更强”或“更弱”，而是：

```text
more heterogeneous
more surface-controlled
more field-sensitive
more selective
```

若孔壁惰性、孔内电场强、电子迁移后能被有效转化为目标产物，则多孔介质可优于 bulk water。

若孔壁是强自由基/电子 sink，则多孔介质中水相可测 G 值可能低于 bulk water。

因此可概括为：

```text
Porous media + strong internal electric field:
    G_escape(e_aq^-) ↑
    redox separation ↑
    G(H2O2) often ↑ in inert pores
    G(H2) depends on surface catalytic conversion
    aqueous final products may ↓ if pore walls are strong sinks
```

## 14. 结论

电场对多孔介质水辐解的核心作用，是在纳秒尺度内促进带电初级产物，尤其是 `e_aq^-`，与其 geminate partner 和氧化性自由基发生空间分离。由于早期复合反应速率极快，哪怕数纳米至数十纳米的电子漂移，也可能显著改变初级产物逃逸概率。

最可靠的物理判断是：

```text
电场增强电子逃逸；
电子逃逸增强氧化/还原分离；
氧化/还原分离改变 H2、H2O2 等长寿命产物的净 G 值。
```

具体到最终产物：

- `G(e_aq^- escape)` 大概率增加。
- `G(•OH escape)` 在惰性孔中倾向增加。
- `G(H2O2)` 在惰性孔中倾向增加，但在强催化分解表面上可能降低。
- `G(H2)` 方向不确定，取决于电子是否被有效转化为氢，而不是被非生产性捕获。

因此，多孔介质辐解相对 bulk water 的优势不在于简单增加所有 G 值，而在于通过孔结构、表面化学和电场调控，选择性地改变辐解反应路径。

## 15. 参考文献与资料

- Le Caër, S. Water Radiolysis: Influence of Oxide Surfaces on H2 Production under Ionizing Radiation. *Water*, 2011. <https://www.mdpi.com/2073-4441/3/1/235>
- Buxton, G. V. et al. Critical Review of Rate Constants for Reactions of Hydrated Electrons, Hydrogen Atoms and Hydroxyl Radicals in Aqueous Solution. *Journal of Physical and Chemical Reference Data*, 1988.
- Rotureau, P. et al. Radiolysis of confined water: molecular hydrogen formation. *Chemical Physics Letters*, 2005. <https://pubmed.ncbi.nlm.nih.gov/15968699/>
- Foley, S. et al. Radiolysis of confined water: production and reactivity of hydroxyl radicals. *Chemical Physics Letters*, 2004.
- Ouerdane, H. et al. Radiolysis of Water Confined in Porous Silica: A Simulation Study. *Journal of Physical Chemistry C*, 2010. <https://pubs.acs.org/doi/10.1021/jp103127j>
- Onsager, L. Initial Recombination of Ions. *Physical Review*, 1938. <https://journals.aps.org/pr/abstract/10.1103/PhysRev.54.554>
