# 利用核辐射、多孔半导体与粘土材料提升电解水制氢效能的可能性：理论推导、研究路径与产业化判断

日期：2026-05-10  
研究主题：Radiolysis-assisted electrolysis；porous semiconductor/clay media；water splitting；G-value engineering；radiocatalytic hydrogen production  
研究边界：本文为研究构想、理论推导和产业可行性分析，不构成核设施设计、安全许可、投资建议或工程放大结论。涉及放射源、电解槽、氢气安全、核材料、辐射防护、工业许可时，必须由持证核安全、化工安全、电化学工程和监管合规团队复核。

## 1. 结论先行

从严格能量守恒和辐射化学 G 值出发，我的判断是：

1. **直接用核辐射水辐解来替代现代电解水制氢，难以在总能效上大幅超过常规电解。**  
   低 LET γ/电子辐解水中 `G(H2)` 约为 `0.45 molecule / 100 eV` 量级，对应把 1 kg H2 仅靠辐解产生，需要约 `10.7 GJ` 的吸收辐射能；现代电解槽通常约 `180 MJ/kg H2` 量级。差距约一个数量级以上。

2. **如果辐射能本身是废辐射，例如核废料、乏燃料、放射性材料衰变热/γ 场，否则会被屏蔽耗散，那么辐解-电解耦合可以作为能量回收或副产氢路线研究。**  
   但它应被称为“废辐射化学能回收”或“radiation-assisted electrolysis”，不是低成本主流绿氢替代路线。

3. **多孔半导体/粘土体系的真正价值，不在于粘土本身“神奇地产氢”，而在于它可能同时提供：**
   - 高比表面积；
   - 纳米孔限域；
   - 表面电荷和电双层电场；
   - 离子交换和吸附；
   - 半导体颗粒或氧化物催化剂的分散载体；
   - 促进 `e_aq^-`、电子-空穴对和自由基的空间分离。

4. **粘土材料必须谨慎定义。**  
   纯 kaolinite、montmorillonite 等层状硅铝酸盐通常更接近宽带隙绝缘/弱导电材料，而不是高迁移率半导体。所谓“粘土半导体”更现实的路线是：粘土作为载体，负载或原位生长 TiO2、ZrO2、Fe2O3、MoS2、g-C3N4、NiFe oxyhydroxide、NiMo、Pt/Ni 等真正承担光/辐射催化和电催化功能的活性相。

5. **最有研究价值的方向是：辐射辅助的多孔半导体电解槽，而不是自然辐射驱动的产氢装置。**  
   自然放射性矿物或粘土中的辐射功率密度极低，工业产氢几乎不可行；实验室必须使用强 γ 源、电子束、反应堆/乏燃料辐射场或其它高通量辐射源。

最终判断：

```text
可以作为科学研究和特殊场景技术路线；
不应被宣传为短期内大幅超越常规电解槽的通用工业制氢方法；
若有价值，价值来自“废辐射能回收 + 半导体载流子分离 + 电解槽偏压降低 + 孔壁选择性催化”的耦合。
```

## 2. 资料收集与证据基础

### 2.1 水辐解与固液界面

Le Caër 的综述指出，水在电离辐射下产生：

```text
e_aq^-, H•, •OH, H3O+, H2, H2O2
```

并且 `H2` 产率会被氧化物/水界面显著改变。该综述还列出典型逃逸产额：低 LET γ/电子辐射下，中性 pH 附近 `H2` 逃逸产额约为 `0.047 µmol/J`，换算为约 `0.45 molecule / 100 eV`。同时，氧化物表面可以通过能量转移、激子、电子/空穴和表面反应改变 `H2` 产率。

### 2.2 半导体水分解

半导体光催化/光电化学水分解已有成熟理论基础。核心要求是：

- 半导体能吸收能量产生电子-空穴对；
- 导带电势足够负，可驱动 `H+/H2` 或 `H2O/H2` 还原；
- 价带电势足够正，可驱动 `H2O/O2` 氧化；
- 电子和空穴必须在复合前被分离并传输到反应位点；
- 表面催化剂必须降低 HER/OER 过电位。

γ 射线或电子束不是光子带隙吸收意义上的普通光，但它可以在半导体和水中产生高能电子、二次电子、电子-空穴对、激子和缺陷态。因此可以把它看成一种“高能激发源”，其问题是热化损失和辐射损伤很大。

### 2.3 粘土基材料

粘土矿物在光催化和电化学材料中常被用作：

- 吸附/离子交换材料；
- 纳米片或管状载体；
- TiO2、ZnO、g-C3N4、MoS2 等半导体的分散支撑；
- 调控界面电荷和孔结构的基底；
- 改善催化剂回收和稳定性的载体。

因此，粘土材料在本问题中的合理定位不是“粘土本身就是高效半导体”，而是“粘土-半导体-电催化剂复合多孔结构”。

### 2.4 当前电解氢产业背景

IEA Global Hydrogen Review 2024 显示，低排放氢仍处于早期扩张阶段，电解槽产能增长很快，但项目 FID、成本和需求落地仍面临挑战。现代电解槽的核心竞争指标是电耗、寿命、资本成本、动态响应和系统安全，而不是单纯追求新奇能量源。

这意味着：任何“辐射辅助电解”路线若要产业化，必须回答两个问题：

```text
是否降低总能耗？
是否降低总成本和风险？
```

只降低电表读数而增加更昂贵的辐射源、屏蔽、许可和维护成本，不能算真正提升效能。

## 3. 常规电解水的热力学基准

水分解反应为：

```text
H2O(l) -> H2(g) + 1/2 O2(g)
```

标准 Gibbs 自由能：

```text
ΔG° ≈ 237.1 kJ/mol H2
```

标准焓变：

```text
ΔH° ≈ 285.8 kJ/mol H2
```

因为生成 1 mol H2 需要 2 mol 电子，所以可逆电压为：

```text
E_rev = ΔG° / (2F)
```

代入：

```text
E_rev ≈ 237100 / (2 × 96485) ≈ 1.229 V
```

热中性电压为：

```text
E_th = ΔH° / (2F)
```

代入：

```text
E_th ≈ 285800 / (2 × 96485) ≈ 1.48 V
```

实际电解槽电压为：

```text
V_cell = E_rev + η_anode + η_cathode + iR + η_mass
```

其中：

- `η_anode`：析氧反应 OER 过电位；
- `η_cathode`：析氢反应 HER 过电位；
- `iR`：欧姆损耗；
- `η_mass`：传质损失。

现代电解槽若以约 `50 kWh/kg H2` 估算：

```text
50 kWh/kg = 180 MJ/kg H2
```

这相当于以 HHV `142 MJ/kg H2` 计，系统效率约：

```text
η_HHV ≈ 142 / 180 ≈ 79%
```

实际系统根据工况、压缩、辅助设备和寿命不同会更低，但这个数量级说明：现代电解水已经接近热力学极限，任何新路线要“大幅提升”，必须非常谨慎地做能量账。

## 4. 水辐解产氢的能量账

### 4.1 G 值到摩尔产率的换算

G 值定义为：

```text
G = molecules / 100 eV
```

`100 eV` 的能量为：

```text
100 eV = 100 × 1.602 × 10^-19 J = 1.602 × 10^-17 J
```

每焦耳产生的摩尔数为：

```text
r_mol/J = G / [(1.602 × 10^-17) N_A]
```

其中：

```text
N_A = 6.022 × 10^23 mol^-1
```

所以：

```text
r_mol/J = 1.036 × 10^-7 G
```

若 `G(H2) = 0.45 molecule / 100 eV`，则：

```text
r_H2 = 1.036 × 10^-7 × 0.45
     ≈ 4.66 × 10^-8 mol/J
```

### 4.2 生产 1 kg H2 需要多少辐射能

1 kg H2 约为：

```text
n_H2 = 1000 g / 2 g mol^-1 = 500 mol
```

所需吸收辐射能为：

```text
E_rad = n_H2 / (1.036 × 10^-7 G)
```

对于 bulk water γ 辐解：

```text
G = 0.45
```

得到：

```text
E_rad ≈ 500 / (1.036 × 10^-7 × 0.45)
      ≈ 1.07 × 10^10 J
      ≈ 10.7 GJ/kg H2
```

与现代电解槽约 `180 MJ/kg H2` 相比：

```text
10.7 GJ / 0.18 GJ ≈ 59
```

也就是说，若把辐射能作为需要付出的能量，普通水辐解制氢比现代电解水低效约几十倍。

### 4.3 理论上需要多高的 G 值才能接近电解槽

若希望达到：

```text
E_input = 180 MJ/kg H2
```

则需要：

```text
500 = 1.036 × 10^-7 G × 1.8 × 10^8
```

解得：

```text
G_required ≈ 26.8 molecules / 100 eV
```

这意味着：要仅靠辐解在能量上接近现代电解槽，`G(H2)` 需要从 `0.45` 提高到约 `27`，即提高约 `60` 倍。

这不是普通孔隙限域、电场分离或粘土表面效应能够轻易达到的数量级。

## 5. 热力学上限

生成 1 个 H2 分子的 Gibbs 自由能约为：

```text
ΔG_per molecule ≈ 237.1 kJ/mol / N_A
```

换算成 eV：

```text
ΔG_per molecule ≈ 2.46 eV / H2
```

若 `100 eV` 的吸收能全部转化为 H2 的 Gibbs 化学能，则理论最大：

```text
G_max,Gibbs = 100 / 2.46 ≈ 40.6 molecules / 100 eV
```

若按 HHV：

```text
ΔH_per molecule ≈ 2.96 eV / H2
```

则：

```text
G_max,HHV = 100 / 2.96 ≈ 33.8 molecules / 100 eV
```

所以 `G_required ≈ 26.8` 已经接近热力学上限的相当大比例。考虑高能辐射热化、散射、缺陷形成、声子损失、复合、表面淬灭和气液分离损失，实际达到这个值非常困难。

因此：

```text
用辐解路线大幅超过现代电解槽，不符合当前物理和工程判断；
最多可能在特殊场景下降低外加电能，或利用废辐射做部分化学能回收。
```

## 6. 辐射辅助电解的控制方程

设多孔电极孔隙率为 `ε`，孔隙水中物种 `i` 的浓度为 `c_i`。控制方程为：

```text
∂(ε c_i)/∂t = -∇·N_i + ε S_i^rad + ε Σ_j ν_ij R_j - a_s J_i,s
```

通量为 Nernst-Planck 形式：

```text
N_i = -ε D_eff,i [∇c_i + (z_i F/RT)c_i ∇Φ] + ε c_i v
```

其中：

```text
D_eff,i = D_i / τ
```

电势满足：

```text
-∇·(ε_m ∇Φ) = F ε Σ_i z_i c_i + ρ_fixed
```

辐解源项：

```text
S_i^rad = 1.036 × 10^-7 ρ_w Ddot_w G_i
```

对于 `H2`，若同时存在电解和辐解贡献：

```text
r_H2,total = I_F/(2F) + ∫_V S_H2^rad dV + r_H2,surf
```

其中：

- `I_F`：真正用于 Faradaic 产氢的电流；
- `∫ S_H2^rad dV`：体相辐解直接产氢；
- `r_H2,surf`：半导体/孔壁表面由辐射激发载流子产生的氢。

系统能效必须写为：

```text
η_total = ṅ_H2 ΔH_H2 / (P_el + P_rad,absorbed + P_aux)
```

如果只计算电耗：

```text
η_electric = ṅ_H2 ΔH_H2 / P_el
```

会产生误导。因为辐射能不是免费消失的，除非它本来就是必须被屏蔽和耗散的废辐射。

## 7. 辐射如何降低外加电解功

常规电解槽：

```text
V_cell = E_rev + η_anode + η_cathode + iR + η_mass
```

若多孔半导体在辐射下产生可收集电子-空穴对，并形成辐射诱导光电压/放射电压 `V_rad`，则等效可写成：

```text
V_cell,external = E_rev + η_anode + η_cathode + iR + η_mass - V_rad
```

但这不是免费降低能耗，因为：

```text
P_rad -> electron-hole pairs -> separated carriers -> chemical work
```

只有在 `P_rad` 是废辐射时，外部电能减少才有系统意义。

辐射对应的等效电流为：

```text
I_rad = 2F r_H2,rad
```

代入：

```text
r_H2,rad = 1.036 × 10^-7 G P_rad
```

得：

```text
I_rad / P_rad = 2F × 1.036 × 10^-7 G
              ≈ 0.0200 G A/W
```

若 `G = 0.45`：

```text
I_rad / P_rad ≈ 0.009 A/W
```

在 `V_cell ≈ 2 V` 下，相当于每 1 W 吸收辐射最多抵消约：

```text
P_el,saved ≈ 2 × 0.009 = 0.018 W
```

也就是约 `1.8%` 的电功等效回收。

若通过半导体/表面催化把有效 `G` 提高到 `5`：

```text
I_rad / P_rad ≈ 0.10 A/W
P_el,saved ≈ 0.20 W per W radiation
```

这在废辐射利用中可能有研究价值，但若辐射能本身需要专门生产，则总能效仍不占优。

## 8. 半导体辐射催化的理论上限

高能辐射在半导体中产生电子-空穴对。设产生一个可用电子-空穴对的平均能量为 `W_s`，单位 eV/pair。辐射吸收功率为 `P_abs`，则载流子生成率为：

```text
R_eh = P_abs / (W_s × 1.602 × 10^-19)
```

若载流子分离效率为 `η_sep`，法拉第效率为 `η_F`，每生成 1 个 H2 需要 2 个电子，则：

```text
R_H2 = η_sep η_F R_eh / 2
```

换算成 G 值：

```text
G_H2,semi = 100 η_sep η_F / (2 W_s)
```

即：

```text
G_H2,semi = 50 η_sep η_F / W_s
```

若：

```text
W_s = 10 eV/pair
η_sep η_F = 1
```

则：

```text
G_H2,semi = 5 molecules / 100 eV
```

若极理想地：

```text
W_s = 3 eV/pair
η_sep η_F = 1
```

则：

```text
G_H2,semi ≈ 16.7 molecules / 100 eV
```

这已经远高于 bulk water radiolysis 的 `0.45`，但仍低于接近现代电解槽所需的 `~27`。实际材料中 `η_sep η_F` 很难等于 1，辐射损伤、缺陷复合、声子热化和界面损失会进一步降低。

因此，半导体辐射催化可以显著提升辐解产氢 G 值，但从总能效上击败电解槽仍然困难。

## 9. 粘土材料在该体系中的合理角色

### 9.1 粘土不能被简单当作高效半导体

常见粘土矿物如 kaolinite、montmorillonite、illite、halloysite 主要是硅铝酸盐层状结构。它们的优势是：

- 高比表面积；
- 层间空间；
- 离子交换；
- 表面电荷；
- 吸附水和阳离子；
- 化学和机械稳定性；
- 成本低。

但它们的弱点也明显：

- 电子迁移率低；
- 导电性差；
- 宽带隙；
- 载流子收集困难；
- 天然杂质不可控。

因此，若要构建高效体系，粘土更适合作为：

```text
porous scaffold + ion-exchange host + semiconductor/catalyst support
```

而不是单独作为主半导体。

### 9.2 可设计的粘土复合体系

可行材料路线：

```text
clay / TiO2 / Pt 或 NiMo
clay / ZrO2 / Ni
clay / Fe2O3 / NiFeOOH
clay / g-C3N4 / MoS2
clay / MnOx / NiFeOOH
clay / conductive carbon / semiconductor / catalyst
```

其中：

- 粘土提供孔结构和界面电荷；
- 半导体吸收辐射并产生电子-空穴对；
- 导电网络收集电子；
- HER catalyst 降低析氢过电位；
- OER catalyst 或牺牲氧化路径消耗空穴；
- 膜分离 H2/O2，防止爆炸混合。

## 10. 自然辐射能否迁移到实验室并工业化

### 10.1 自然条件下的辐射功率太低

天然铀的比活度约 `25.4 kBq/g`。即使按天然铀衰变链达到长期平衡估算，1 吨天然铀的衰变热也只是约 `0.1 W` 量级。

若以 `G(H2) = 0.45` 估算：

```text
r_H2 = 1.036 × 10^-7 × 0.45 × 0.1
     ≈ 4.66 × 10^-9 mol/s
```

一年为：

```text
n_year ≈ 4.66 × 10^-9 × 3.15 × 10^7
       ≈ 0.147 mol/year
```

对应 H2 质量：

```text
m_H2 ≈ 0.147 × 2 g
     ≈ 0.29 g/year
```

这还是 1 吨天然铀本身，不是 1 吨普通矿石。若矿石品位为 1% U，则每吨矿石的 H2 产量约为毫克级/年。

所以：

```text
自然辐射可以解释地质环境中的长期辐解化学；
但不能直接作为工业产氢能源。
```

### 10.2 实验室可模拟，但必须使用强辐射源

实验室中可以使用：

- `60Co` γ 源；
- `137Cs` γ 源；
- 电子束；
- X 射线源；
- α/β 放射性薄膜源；
- 反应堆辐照孔道；
- 乏燃料或高放废物附近的受控辐射场。

这些源可以把自然界极低剂量率过程压缩到可测时间尺度。

但这意味着工业化路线本质上不是“自然粘土辐射电解”，而是：

```text
强辐射源 + 多孔半导体电解反应器 + 氢氧分离 + 辐射安全系统
```

## 11. 可能的工业化流程设计

### 11.1 概念流程 A：废辐射辅助电解槽

适用场景：

- 核设施已有强 γ 场；
- 辐射本来必须被屏蔽；
- 目标是回收一小部分辐射能为 H2 或 H2O2。

流程：

```text
核废料/γ源
    ↓ γ radiation
屏蔽窗口 / 辐照通道
    ↓
多孔半导体-粘土复合电极流通槽
    ↓
AEM/PEM 膜分离
    ↓
Cathode: H2
Anode: O2 或 H2O2/氧化产物
```

关键设计：

- 辐射源和电解液物理隔离，防止污染；
- 半导体电极必须导电，不能只是粉体悬浮；
- H2/O2 必须膜分离；
- 辐照区需气泡管理；
- H2 浓度必须低于爆炸风险或连续移除。

### 11.2 概念流程 B：辐射-电场协同多孔电极

在多孔半导体电极内部施加电场：

```text
E = -∇Φ
```

作用：

- 拉开 `e_aq^-` 与 `H3O+ / •OH`；
- 分离半导体中的电子-空穴对；
- 使电子向 HER 位点迁移；
- 使空穴向 OER 位点或牺牲氧化位点迁移。

目标不是让辐射独立产氢，而是降低：

```text
η_cathode + η_anode + recombination loss
```

### 11.3 概念流程 C：辐射诱导 H2O2 / H2 联产

若体系很难实现高效整体水分解，可以考虑更现实的中间路线：

- 阴极侧强化 H2；
- 阳极/氧化侧选择性生成 H2O2；
- 或将 `H2O2` 作为高价值化学品回收。

原因是多孔介质中 `•OH` 逃逸和二聚可能增强：

```text
•OH + •OH -> H2O2
```

这种路线可能比单纯追求 H2 更容易找到经济性，但也需要避免 H2O2 分解和安全风险。

## 12. 实验验证路线

### 12.1 第一阶段：基础 G 值测定

变量：

- bulk water；
- clay suspension；
- clay pellet；
- clay/TiO2；
- clay/ZrO2；
- clay/Fe2O3；
- clay/semiconductor/HER catalyst。

测量：

- `G(H2)`：GC-TCD 或 MS；
- `G(H2O2)`：UV-vis、titanium sulfate 或 Amplex Red；
- `e_aq^-`：瞬态吸收或 scavenger method；
- `•OH`：EPR spin trapping；
- radiation dose：Fricke dosimeter / alanine / calorimetry；
- surface charge：zeta potential；
- band structure：UV-vis DRS、Mott-Schottky、UPS/XPS；
- conductivity：EIS。

### 12.2 第二阶段：外加电场效应

设计平行板或微流控多孔电极：

```text
E = 10^5 - 10^7 V/m
```

测量不同电场下：

```text
G_eff(H2), G_eff(H2O2), Faradaic efficiency, radical lifetime
```

判断电场是否通过降低复合提高有效产额。

### 12.3 第三阶段：半导体载流子收集

用三电极体系测：

- 辐照开关下的 photocurrent/radiocurrent；
- open-circuit radiovoltage；
- 电流-电压曲线；
- EIS；
- 气体产物法拉第效率。

判据：

```text
若 radiation-on 时在同一产氢速率下 V_cell 明显下降，
且 P_rad 是废辐射，
则有工程意义。
```

### 12.4 第四阶段：连续流反应器

目标：

- 证明 100-1000 小时稳定；
- 氢氧安全分离；
- 无显著催化剂粉化/淋失；
- 无严重辐射损伤；
- 总能效账可闭合。

## 13. 产业化评价指标

必须报告以下指标：

```text
G_eff(H2) = H2 molecules / 100 eV absorbed
```

```text
η_total = ṅ_H2 ΔH_H2 / (P_el + P_rad,absorbed + P_aux)
```

```text
η_waste-radiation = ṅ_H2 ΔH_H2 / P_el
```

其中 `η_waste-radiation` 只能在辐射源本来必须被耗散时使用，不能作为通用能效。

还要报告：

- Faradaic efficiency；
- radiation utilization efficiency；
- catalyst durability；
- gas crossover；
- H2/O2/H2O2 selectivity；
- absorbed dose distribution；
- shielding mass；
- regulatory cost；
- lifecycle cost per kg H2。

## 14. 主要技术风险

| 风险 | 解释 |
|---|---|
| 总能效不占优 | 辐射水解 G 值太低，半导体也有热化损失。 |
| 辐射源成本和许可 | γ 源、电子束或核废料利用涉及严格监管。 |
| H2/O2 混合爆炸 | 辐射会同时产生氧化/还原产物，必须膜分离。 |
| 材料辐射损伤 | 半导体缺陷、粘土结构变化、催化剂失活。 |
| 表面淬灭 | 孔壁可能捕获电子/自由基，降低有效产物。 |
| 副产物控制 | H2O2、O2、HO2•、O2•^-、溶出金属离子可能影响稳定性。 |
| 公众接受度 | “核辐射制氢”需要极强安全叙事和透明监管。 |

## 15. 研究者的科学畅想，但受约束

一个值得探索的未来体系是：

```text
放射源 / 废辐射场
    ↓
多孔粘土-半导体复合膜
    ↓
内建电场 + 外加低偏压
    ↓
电子向 HER cathode 迁移
空穴向 OER / H2O2 anode 迁移
    ↓
H2 与 O2/H2O2 分离收集
```

材料结构可以是：

```text
conductive substrate
    ↓
clay nanosheet scaffold
    ↓
TiO2 / ZrO2 / Fe2O3 semiconductor domains
    ↓
NiMo / Pt / MoS2 HER sites
    ↓
NiFeOOH / MnOx OER or peroxide sites
```

理论上，若实现：

```text
η_sep η_F 高
W_s 低
surface recombination 低
radiation damage 低
gas separation 高
```

则有效 G 值可从 bulk water 的 `~0.45` 提高到 `1-5`，甚至在理想半导体载流子收集情况下更高。但要接近现代电解槽总能效，需要 `G ≈ 27`，这是非常高的门槛。

所以科学畅想的合理目标不是：

```text
取代绿电电解水
```

而是：

```text
利用废辐射进行部分化学能回收；
在核设施附近生产少量 H2/H2O2；
发展辐射-电化学耦合传感和特殊化学合成；
探索多孔电场对辐解路径的基础科学。
```

## 16. 产业化路线图

### 阶段 0：理论筛选

目标：

- 计算 `G_required`；
- 建立 PNP + Butler-Volmer + radiolysis reaction model；
- 筛选材料 bandgap、导电性、表面能级和辐射稳定性。

Go / No-Go：

```text
若预测 G_eff(H2) < 1 且无废辐射场，不建议继续产业化。
```

### 阶段 1：克级材料和小型辐照

目标：

- `G(H2)` 比 bulk water 提高至少 3-5 倍；
- H2 法拉第效率可测；
- 材料 100 kGy 后结构稳定。

### 阶段 2：电场耦合微型电解槽

目标：

- radiation-on 状态下，同等 H2 产率所需外加电压下降；
- 气体 crossover 可控；
- H2/O2/H2O2 selectivity 可调。

### 阶段 3：连续流原型

目标：

- 1000 小时运行；
- 稳定 G_eff；
- 总能耗、维护、安全成本可闭合。

### 阶段 4：核设施场景示范

仅适用于：

- 放射源已存在；
- 辐射本来需要屏蔽；
- 许可和安全边界清楚；
- H2 产量虽小但有现场用途。

## 17. 最终判断

### 17.1 是否可能“大幅提升当前电解氢效能”

若把辐射能计入总能耗：

```text
大概率不能。
```

原因是 bulk water `G(H2)` 太低，即使半导体/孔隙/电场提高若干倍，也很难达到与现代电解槽相当的总能效。

若辐射是废辐射，且电解槽本来位于核设施附近：

```text
有可能降低外加电能或回收部分废辐射能。
```

但这更像 niche technology，不是通用绿氢主路线。

### 17.2 粘土半导体工业流程是否可行

作为“粘土本身直接高效电解水”：

```text
不充分。
```

作为“粘土-半导体-电催化剂复合多孔电极”：

```text
值得研究。
```

其关键是把粘土用于孔结构、电荷环境和材料分散，而把真正的载流子生成、传输和电催化交给工程化半导体和催化剂。

### 17.3 最有价值的研究问题

我认为最值得立项的问题是：

```text
在强电场多孔半导体/粘土复合电极中，
辐射产生的电子和空穴是否能被有效分离，
并在低外加偏压下转化为 H2 与 O2/H2O2？
```

如果这个问题的实验答案是肯定的，产业化方向应定位为：

```text
废辐射辅助电化学制氢/制过氧化氢；
核设施副产化学品；
高辐射环境中的能量回收；
多孔介质辐射电化学基础平台。
```

而不是直接宣称替代 PEM/alkaline electrolyzer。

## 18. 参考资料

- Le Caër, S. Water Radiolysis: Influence of Oxide Surfaces on H2 Production under Ionizing Radiation. *Water*, 2011. <https://www.mdpi.com/2073-4441/3/1/235>
- IEA. Global Hydrogen Review 2024: Hydrogen production. <https://www.iea.org/reports/global-hydrogen-review-2024/hydrogen-production>
- Hisatomi, T.; Domen, K. Reaction systems for solar hydrogen production via water splitting with particulate semiconductor photocatalysts. *Nature Catalysis*, 2019. <https://www.nature.com/articles/s41929-019-0242-6>
- Eidsvåg, H. et al. TiO2 as a Photocatalyst for Water Splitting: An Experimental and Theoretical Review. *Molecules*, 2021. <https://www.mdpi.com/1420-3049/26/6/1687>
- Mineral-supported photocatalysts review. *Energies*, 2022. <https://www.mdpi.com/1996-1073/15/15/5607>
- Clay mineral-based photocatalysts review. *Catalysts*, 2024. <https://www.mdpi.com/2073-4344/14/9/575>
- Rotureau, P. et al. Radiolysis of confined water: molecular hydrogen formation. *Chemical Physics Letters*, 2005. <https://pubmed.ncbi.nlm.nih.gov/15968699/>
- Ouerdane, H. et al. Radiolysis of Water Confined in Porous Silica: A Simulation Study. *Journal of Physical Chemistry C*, 2010. <https://pubs.acs.org/doi/10.1021/jp103127j>
- Jung, J. et al. Radiocatalytic H2 production with gamma-irradiation and TiO2 catalysts. <https://pure.korea.ac.kr/en/publications/radiocatalytic-hsub2sub-production-with-gamma-irradiation-and-tio>
- NRC. Natural uranium glossary. <https://www.nrc.gov/reading-rm/basic-ref/glossary/natural-uranium>
- EPA. Radionuclide Basics: Uranium. <https://www.epa.gov/radiation/radionuclide-basics-uranium>
