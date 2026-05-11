# Patterson Lake Corridor：面向未 Claim / 近期失效地块的铀-金-关键矿物潜力筛选报告

日期：2026-05-11  
研究类型：GeoMine Research / AOI screening / claim-gap due diligence / commodity-potential review  
AOI：加拿大 Saskatchewan 省西南 Athabasca Basin 边缘，Patterson Lake Corridor，筛选框 `-109.90,57.25,-108.45,58.15`（EPSG:4326）  
重点矿种：铀为主，兼顾金、Ni-Cu-Co、REE-Th、Mo-V-Pb 等伴生或邻近关键矿物  
输出边界：本报告是公开数据和第一轮空间筛选，不是 NI 43-101 技术报告、QP 意见、法律矿权意见、资源量/储量估算、开采可行性或投资建议。矿权状态必须在 Saskatchewan MARS 当日复核。

## 1. 结论摘要

**最重要的判断：Patterson Lake Corridor 的“地质最优地段”和“现在可能无 Claim 的地段”高度不重合。**

从地球化学、构造、地球物理、钻孔和矿床模型看，最可能继续产生新热点的是：

1. `JR Zone - Broach/Tetra - Minto - Smart Lake` 北西延展区；
2. `Hook Lake / Spitfire - Bow - Harpoon` 结构走廊；
3. `Triple R - Arrow` 已开发级矿床两侧的二级剪切带、交叉断裂和 mafic/ultramafic 接触带；
4. `Black Lake / Broach / Smart Lake` 一带的 U-REE-Th-Ni-Cu-Co 多金属异常组合。

但这些强证据区大多已经被 F3 Uranium、NexGen、Paladin/Fission、Cameco/Orano/Purepoint、Orano、F4、Stallion 等公司控制。若目标是“没被 claim 的地块”，不能只按地质最优排序；必须先做 tenure subtraction，再谈矿化潜力。

本次官方图层下载和网格筛选显示：

- AOI 内下载到 `521` 个 active mineral disposition features；
- 下载到 `26` 个 lapsed mineral disposition features；
- 下载到 `1,635` 个官方钻孔点；
- 下载到 `96` 个 Mineral Deposits Index 点；
- 下载到 `53` 个 Government Rock Samples 点；
- 完全无 active disposition bbox 交集的网格主要在 AOI 南部、东南部和东北外围，地质证据较弱；
- 具有 lapsed 证据的候选区主要落在 `PNR / Cache Lake` 一带，但这些 lapsed feature 与 active disposition bbox 有重叠，不能直接视为可 staking 空地。

**因此，我的排序结论是：**

| 优先级 | 区域 | 是否可能 open | 主矿种 | 判断 |
|---|---|---:|---|---|
| 1 | `JR-Broach-Smart Lake`，约 `-109.55, 57.82-57.88` | 低，核心多为 active | U + REE/Th + Ni-Cu-Co + 少量 Au | 地质最强，适合并购/JV/邻区边界监控，不是直接 staking 首选 |
| 2 | `Hook Lake-Spitfire-Bow`，约 `-109.25 to -109.15, 57.65-57.72` | 低 | U | 典型 PLC 高品位铀模式，适合监控 claim 边界和公司交易 |
| 3 | `Triple R-Arrow flanks`，约 `-109.36 to -109.25, 57.62-57.68` | 很低 | U + Au/Cu/Ag accessory | 开发级矿床邻区，最强但矿权和竞争压力最高 |
| 4 | `PNR / Cache Lake lapsed cluster`，约 `-108.85 to -108.55, 57.37-57.45` | 需要 MARS 精确确认 | REE-Th + Ni-Cu-Co，局部 U 弱 | 最值得做 claim-gap 精查的“过期/可能空档”方向，但不是核心铀靶 |
| 5 | `PLC-234 open grid`，中心约 `-109.05, 58.025` | 本次网格无 active bbox 交集 | 早期 U/结构探索 | 成本低但证据弱，适合廉价 grassroots 侦查 |
| 6 | `PLC-001 open grid`，中心约 `-109.85, 57.275` | 本次网格无 active bbox 交集 | 早期 U/基底结构探索 | 距主矿床远，作为低成本外围选项 |
| 7 | `PLC-026/027 open grids`，中心约 `-108.85/-108.75, 57.325` | 本次网格无 active bbox 交集 | 岩石样/REE-Th/基底金属潜力 | 与核心 PLC 距离远，铀潜力较低，关键矿物备选 |

如果目标是“开采成本最低、回报最快”，我的判断不是直接去找外围空地，而是：

1. **第一选择：监控强证据 active claims 的 good-standing 风险、work-waiting 状态、边界 sliver 和 re-opening lands。**  
   这类机会一旦出现，比外围空地价值高很多。

2. **第二选择：围绕 lapsed cluster 做精确 polygon subtraction。**  
   重点是 CAT Strategic Metals lapsed ids `MC00013968`, `MC00013970`, `MC00014519`, `MC00014557`, `MC00013808` 等附近区域。但现有公开 lapsed layer 不提供 lapse date，本报告不能确认它们是否属于最近 1-2 年过期，也不能确认是否已被重新 staking。

3. **第三选择：接受低确定性，拿外围 open grids 做低成本 geophysics-first 项目。**  
   这类地块不应按“马上开矿”估值，而应按“低成本买一个可验证的结构/地球物理假说”估值。

## 2. 使用的数据和来源

### 2.1 GeoMine MCP 使用情况

已调用 GeoMine MCP：

- `normalize_aoi`：标准化 Patterson Lake Corridor AOI；
- `search_saskatchewan_mineral_data`：确认 Saskatchewan GeoAtlas / public geoscience data 为候选来源；
- `search_cdogs_surveys`：确认 CDoGS 可作为地球化学数据源，但当前 MCP 版本不执行实时空间查询；
- `search_canada_geodata`：确认 Open Canada / Geo.ca 和 CDoGS 的数据发现路径；
- `summarize_dataset_provenance`：记录 Saskatchewan tenure 与 mineral exploration 图层元数据；
- `calculate_infrastructure_distance`：当前 MCP 版本仅返回所需输入，未执行真实距离计算。

MCP 的限制是：当前 GeoMine MCP 版本对 Saskatchewan GeoAtlas、CDoGS 的实时数据查询尚未实现，因此本报告对矿权和矿产点数据采用 Saskatchewan ArcGIS REST 官方图层直接下载。

### 2.2 官方 GIS 图层

1. Saskatchewan Mineral Tenure Crown Dispositions  
   URL: `https://gis.saskatchewan.ca/arcgis/rest/services/Economy/P_Mineral_Tenure_Crown_Dispositions/MapServer`  
   使用图层：
   - `Mineral Dispositions (0)`
   - `Mineral Dispositions - Lapsed (3)`

2. Saskatchewan Mineral Exploration  
   URL: `https://gis.saskatchewan.ca/arcgis/rest/services/Economy/Mineral_Exploration/MapServer`  
   使用图层：
   - `Drillholes (3)`
   - `Government Rock Samples (4)`
   - `Mineral Deposits Index (5)`

3. Saskatchewan MARS  
   URL: `https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/mineral-tenure/mineral-administration-registry-saskatchewan-mars`  
   MARS 是 Saskatchewan 的电子矿权登记系统，取代传统 ground-staking，并以 GIS parcel 方式管理 mineral dispositions。报告中的 open-ground 结论必须以 MARS 当日结果为准。

### 2.3 学术和公司技术来源

关键证据来源包括：

- Card, C. 2021, *The Patterson Lake corridor of Saskatchewan, Canada...*, Geochemistry: Exploration, Environment, Analysis, DOI `10.1144/geochem2020-007`。
- Hillacre, Ansdell and McEwan 2021, *Geology, Structural Analysis, and Paragenesis of the Arrow Uranium Deposit...*, Economic Geology。
- Powell et al. 2019, GSC Open File 8549, *Quantifying fertile alteration in the Patterson Lake corridor...*, DOI `10.4095/313671`。
- Powell et al. 2022, *Mineralogy and K-Ar geochronology of clay alteration associated with uranium mineralization in the Patterson Lake Corridor*。
- Boulanger, Kiss and Tschirhart 2019, GSC Open File 8533/8534, Patterson Lake airborne gravity / first vertical derivative maps。
- NexGen Rook I Project page and feasibility disclosures。
- Paladin/Fission PLS Project update, 2025-08-27。
- F3 Uranium PLN/JR Zone project disclosures and NI 43-101 technical report announcement。
- Purepoint Hook Lake project summary.

## 3. 成矿理论：为什么 Patterson Lake Corridor 重要

### 3.1 核心模型

Patterson Lake Corridor 的意义不只是发现了高品位铀矿，而是改变了 Athabasca 铀矿勘探的空间偏好。传统模型强调盆地内部、不整合面附近和东部成熟区，而 PLC 证明：

- 西南盆地边缘；
- 基底内；
- 远离典型东部矿集区；
- 由深部高应变带和反复活化断裂控制；
- 在 graphitic / sulphidic shear zones、quartz flooding、clay alteration 和 cross structure 叠加处；

也可以形成高品位铀矿。

简化成矿逻辑如下：

```text
深部 crustal-scale / high-strain basement structure
    -> ductile shear / brittle reactivation / Riedel-style fault linkage
    -> graphitic and sulphidic reducing zones
    -> basin-derived oxidized U-bearing brines or mixed basinal-basement fluids
    -> pressure-temperature-redox change and fluid mixing
    -> uraninite precipitation
    -> later remobilization and local high-grade enrichment
```

### 3.2 可用于找下一个热点的证据组合

我把可用证据分成 8 条 evidence lanes：

| Evidence lane | 正向证据 | 负向/风险证据 |
|---|---|---|
| 构造 | NE-SW conductor / shear corridor，交叉断裂，Riedel-style geometry | 单一线性 conductor 无交叉结构 |
| 地球物理 | EM conductor、resistivity low、gravity gradient / mafic-ultramafic contact、magnetic disruption | 只有磁异常但无导电/蚀变证据 |
| 岩性 | orthogneiss、pegmatite、mafic-ultramafic intrusive、graphite/sulphide shear | 均一花岗质片麻岩且无还原带 |
| 蚀变 | illite、kaolinite、chlorite、tourmaline、hematite、quartz flooding、clay crystallinity vector | 弱蚀变、无 clay maturity vector |
| 地球化学 | U + B + Pb + Mo + Ni + Co + Cu + V + As；局部 Au/Ag | 单点 U 异常无结构控制 |
| 钻孔 | gamma / CPS / U3O8 assay，basement-hosted intervals，alteration halo | 只有浅部弱异常、无复测 |
| 矿权 | lapsed / re-opening / active good-standing risk / boundary gap | active tenure 完整覆盖 |
| 开发 | Highway 955、水/电/营地/未来处理厂 proximity | 湖下、水文复杂、监管长周期 |

## 4. 空间筛选方法

### 4.1 AOI 和网格

本次使用的筛选框：

```text
lon_min = -109.90
lon_max = -108.45
lat_min = 57.25
lat_max = 58.15
CRS = EPSG:4326
```

建立 `0.1° × 0.05°` 的初筛网格，共 `270` 个网格单元。每个网格记录：

- active disposition bbox intersection count；
- lapsed disposition bbox intersection count；
- lapsed disposition ids；
- Mineral Deposits Index 点数量；
- uranium / gold / REE-Th / base-metal 指示数量；
- drillhole count；
- government rock sample count；
- 到 `Triple R`, `Arrow`, `Spitfire`, `JR Zone`, `Smart Lake` 的最近距离；
- 综合 score。

输出文件：

- `data/processed/patterson_lake_corridor_claim_gap_grid.csv`
- `data/processed/patterson_lake_corridor_top_grid_cells.geojson`
- `data/processed/patterson_lake_corridor_screen_summary.json`

### 4.2 评分公式

评分是 exploration-screening index，不是资源量或经济估值：

```text
score =
  40 * I(active_count = 0)
  + min(8 * lapsed_count, 24)
  + min(15 * uranium_MDI_count, 30)
  + min(8 * gold_MDI_count, 16)
  + min(5 * REE_Th_MDI_count, 15)
  + min(4 * base_metal_MDI_count, 16)
  + min(8 * ln(1 + drillhole_count), 24)
  + min(2 * rock_sample_count, 8)
  + proximity_bonus
  - 60 * I(active_count > 0)
```

其中：

```text
proximity_bonus =
  16, if nearest_anchor <= 10 km
  12, if nearest_anchor <= 20 km
   6, if nearest_anchor <= 35 km
   0, otherwise
```

注意：这里使用 active/lapsed feature 的 bbox overlap，而不是精确 polygon overlay。因此：

- 若 `active_count = 0`，说明该格网没有 active bbox 交集，作为 open-ground 线索较可靠；
- 若 `active_count > 0`，该格网不能说 open，但可能仍存在边界 sliver 或 partial parcel 空档；
- lapsed feature 不带 lapse date，不能判断是否最近 1-2 年过期。

## 5. 重点候选区解释

### 5.1 JR-Broach-Smart Lake 北西延展区：地质最强，但不是 open-ground 首选

代表格网：

- `PLC-169`：中心约 `-109.55, 57.825`；
- `PLC-184`：中心约 `-109.55, 57.875`。

官方 MDI / 钻孔证据：

- `5991: JR Zone Uranium Mineralization`；
- `5850: Drill holes PLN14-018 & PLN14-019`，U + Co + Cu + Ni + P + Th；
- `4761: Drill hole BR2-6`，U + REE + Th；
- `4769: Drill hole BR-21`，U + Au + Ni + REE + Th；
- 多个 BR / PLN / GL 系列钻孔显示 REE-Th-Ni-Cu-Co 组合；
- 距 JR Zone 最近约 1.6-5.3 km。

地质解释：

这一带位于 JR Zone 与 Broach/Minto/Smart Lake 周边，是典型的“已发现高品位铀矿 + 未完全闭合结构走向 + 多金属地球化学”的组合。其关键不在单个 U 点，而在：

```text
A1/B1-like shear continuation
  + cross-fault / offset structure
  + U + Ni + Co + Cu + REE + Th + Au pathfinders
  + drill-proven basement alteration
  + Highway 955 access
```

这类证据在 PLC 模型中非常强。

矿权结论：

本次网格显示 active disposition bbox intersection 很高，不适合直接当作“无 claim 地块”。如果要进入，路径是：

- 并购 F3 或其非核心资产；
- 与 F3 / F4 / nearby juniors 做 JV；
- 监控边界、work-waiting、good-standing、re-opening；
- 找 active claim 外缘的 exact polygon gap，而不是按格网粗略判断。

开采难度和成本：

- 若发现高品位铀矿，技术路线大概率是地下矿或局部浅部地下开发；
- 放射性矿山许可、尾矿、地下水、通风、辐射防护成本高；
- 但高品位可显著降低单位 operating cost；
- 若未来 Rook I / PLS 形成区域基础设施，卫星矿床或 JV feed 的商业价值会提高。

产量展望：

对 open-ground 新地块不能给资源量或产量。可用 analog 只说明上限潜力：JR/Arrow/Triple R 证明该带可以形成高品位矿体，但新地块需要至少 5-10 年钻探和许可才可能讨论产量。

### 5.2 Hook Lake - Spitfire - Bow：高品位铀模型清晰，但矿权压力高

代表区：

- `PLC-127`：中心约 `-109.25, 57.675`，Arrow 附近；
- `PLC-128`：中心约 `-109.15, 57.675`，Spitfire/Bow 附近；
- `PLC-143`：中心约 `-109.15, 57.725`，Hook Lake/Spitfire 北侧。

证据：

- `5678: Spitfire Zone`；
- `5959: Bow Target Area`；
- `5958: Drill hole RK-15-69`；
- `5332: Arrow Deposit`；
- Purepoint Hook Lake 公开资料显示该项目包含 Spitfire 高品位发现，且不整合面深度约 0-350 m；三条结构 corridor 由多个 EM conductor 构成，钻孔确认与 prospective graphitic shear zones 有关。

地质解释：

Spitfire / Bow 一带是 PLC 模型的标准样本：

```text
graphitic shear conductor
  + shallow to moderate Athabasca unconformity depth
  + basement structural reactivation
  + high-grade U intercepts
  + gravity high / mafic-ultramafic contact hypothesis
```

这类目标非常适合继续找二级 parallel conductor、offset conductor、cross-structure intersection。

矿权结论：

核心多在 Purepoint/Cameco/Orano JV、NexGen 或邻近 active tenure 中。若出现空档，优先级很高；但目前不能把它作为 open-ground。

开采难度：

- 比深部 basin-hosted 目标有优势，因为部分 unconformity depth 较浅；
- 但仍然面临 Athabasca 铀矿共同难题：水文、冻结/注浆、辐射防护、尾矿、CNSC 许可、Indigenous consultation；
- 若未来 Rook I / PLS 建成，区域服务能力会改善。

### 5.3 Triple R - Arrow flank：开发级锚定区，但 claim-gap 机会最低

代表区：

- Triple R：官方 MDI 点约 `-109.3619, 57.6403`；
- Arrow：官方 MDI 点约 `-109.2496, 57.6730`；
- `PLC-111`, `PLC-112`, `PLC-127` 等网格。

证据：

- Paladin 2025 PLS update：PLS / Triple R 的 LOM production `90.9 Mlb U3O8`，平均年产 `9.1 Mlb U3O8`，LOM cash operating cost 约 `US$11.7/lb U3O8`，AISC 约 `US$15.2/lb U3O8`，FEED pre-production capital 约 `US$1.226B`，首次产铀目标 `2031`。
- NexGen Rook I：Rook I / Arrow 为加拿大最大开发阶段铀项目之一；2026-03-05 CNSC 批准 EA 并签发 Licence to Prepare Site and Construct；NI 43-101 FS 设想约 11 年矿山寿命和 `233.6 Mlb` recovered yellowcake；Probable reserves `239.6 Mlb U3O8 @ 2.37% U3O8`。

地质解释：

这些矿床本身已经证明 corridor fertility。找下一个热点时，不应只贴着矿体外圈找，而应找：

- 与主 conductor 平行的 second-order shear；
- conductor 被 transverse fault offset 的位置；
- gravity-gradient / mafic-ultramafic contact；
- resistivity low 与 EM conductor 不完全重合处；
- clay alteration halo 在 drill core 或 spectral 数据中向外延展的方向。

矿权结论：

直接 staking 概率最低。更现实的商业路线是：

- 购买邻近小公司股权；
- 参与 property option；
- 监控边界空档；
- 从 assessment report 中找被历史 drilling 低估的 weak anomaly。

### 5.4 PNR / Cache Lake lapsed cluster：最值得做 MARS 精查的“可能过期地块”

代表格网：

- `PLC-041`：中心约 `-108.85, 57.375`；
- `PLC-042`：中心约 `-108.75, 57.375`；
- `PLC-058`：中心约 `-108.65, 57.425`。

本次 lapsed layer 相关 ids：

- `MC00013968`
- `MC00013970`
- `MC00014519`
- `MC00014557`
- `MC00013808`
- 以及附近 CAT Strategic Metals 相关 lapsed records。

证据：

- `PLC-058` 含 5 个 lapsed bbox intersections；
- 附近 MDI 包括 `5668: Drill hole PN14004`，REE + Th；
- 邻近还有 `PN14001`, `PN14003`, `PN14007`, `PN15003/15004` 等 REE-Th-Ni-Cu-Co-Mo-V 指示；
- 该区政府 rock sample 数量较多。

解释：

这不是最正宗的 PLC 高品位铀靶区，但有三个优点：

1. 有 lapsed-layer 证据，适合做 claim-gap；
2. 关键矿物组合较多，可能不是单一铀项目；
3. 地表/浅部样品和早期钻孔较多，初步验证成本低于深部铀靶。

风险：

- active bbox intersections 存在，说明可能已被重新覆盖，或只有边界空档；
- lapsed layer 不提供 lapse date，不能确认是否最近 1-2 年；
- REE-Th 异常常与放射性矿物、磷酸盐或重矿物有关，未必形成可采矿体；
- 若矿种含 U/Th，仍会带来放射性监管和环境基线成本。

建议：

这是本报告最适合立即做“full tenure subtraction”的区域。下一步不是上钻，而是：

```text
1. 用 MARS 当日 polygon / parcel 下载；
2. 对 active, lapsed, re-opening layers 做 exact difference；
3. 将 open polygons 与 PN/PNR 系列 drillholes、rock samples、SMDI points 叠加；
4. 若存在连续 open polygon，再做地表放射性、便携式 XRF、重矿物、湖/土壤 geochem；
5. 确认是否有可建立 claim block 的面积和连通性。
```

### 5.5 外围 open grids：低成本但低确定性

本次完全无 active bbox intersection 的候选包括：

| Cell | 中心坐标 | 证据 | 最近锚定矿床 | 解释 |
|---|---:|---|---|---|
| `PLC-234` | `-109.05, 58.025` | drillhole count 2 | JR Zone ~35.4 km | 北东外围，可能是低成本结构/基底探索地，但离核心远 |
| `PLC-001` | `-109.85, 57.275` | drillhole count 2 | Triple R ~50 km | 西南外围，低确定性 |
| `PLC-026` | `-108.85, 57.325` | rock sample count 8 | Spitfire ~45.3 km | 东南外围，关键矿物/基底金属探索多于铀 |
| `PLC-027` | `-108.75, 57.325` | rock sample count 5 | Spitfire ~48.1 km | 同上 |

我的判断：这些 open grids 不应被描述为“下一个 Patterson Lake South”。它们的合理定位是：

- 低成本获取；
- 低成本 airborne/ground geophysics；
- prospecting + lake/soil/till geochem；
- 如果发现 conductor + U pathfinder + alteration，再升级。

## 6. 金矿和多金属综合判断

### 6.1 金矿

AOI 内 MDI 显示多个 gold 相关点，例如：

- `3075: Drill hole BL-08-01`，Gold；
- `3078: Drill hole HOO-03`，Gold + Cu + Ni；
- `4749: Drill hole MR-90-1A`，Gold + Co + Cu + Ni；
- `5513: Drill hole CSE10-02`，Gold；
- `5340: Triple R Deposit`，Uranium + Gold；
- `5332: Arrow Deposit`，Uranium + Copper + Gold + Silver；
- `4769: BR-21`，U + Au + Ni + REE + Th。

但这些 gold evidence 主要是：

- uranium system 的 accessory commodity；
- 基底金属/剪切带中的 isolated drillhole occurrence；
- 或历史点状证据。

目前不足以把 PLC 作为独立金矿带来排序。若要找 gold-only open ground，应转向更明确的 Archean greenstone / orogenic gold belts；在 PLC 内，金的更现实价值是：

```text
Au as by-product / pathfinder / reducing-structure indicator
not primary mine-development thesis
```

### 6.2 Ni-Cu-Co 和 REE-Th

多金属证据在 PNR / Cache Lake、Broach / Smart Lake、CW / PN 系列钻孔中更明显。它们可能对应：

- mafic-ultramafic intrusive；
- hydrothermal alteration；
- phosphate / xenotime / monazite / apatite 类 REE-Th mineralization；
- uranium-related fluid pathway alteration；
- 基底剪切带中的 polymetallic enrichment。

但是 REE-Th-U 项目会有两个问题：

1. 经济上：REE 需要矿物学、选矿和冶金，不是“有 REE 异常就可采”；
2. 合规上：Th/U 放射性可能提高 environmental baseline、tailings 和运输成本。

所以，关键矿物只能作为“副线价值”，不能替代高品位 U 的主线价值。

## 7. 开采难度、成本与回报速度

### 7.1 铀矿开发的成本结构

高品位 Athabasca 铀矿的经济优势是单位 operating cost 可以很低，但前期 capex 和许可成本非常高。

可用 benchmark：

| 项目 | 开发阶段 | 产量/资源 benchmark | 成本 benchmark | 启示 |
|---|---|---:|---:|---|
| PLS / Triple R | FEED / undeveloped | LOM production 90.9 Mlb U3O8，平均 9.1 Mlb/y | cash cost ~US$11.7/lb，AISC ~US$15.2/lb，pre-production capex ~US$1.226B | 高品位能支撑低单位成本，但 capex 超过十亿美元 |
| Rook I / Arrow | 获 CNSC Licence to Prepare Site and Construct | FS 约 233.6 Mlb recovered yellowcake；Probable reserve 239.6 Mlb @ 2.37% U3O8 | 2024 updated capex 约 C$2.2B，OpEx 约 C$13.86/lb | 许可和工程成熟度决定兑现速度 |

这说明：如果新 open ground 只是早期异常，它的“最快回报”不是生产，而是：

```text
claim -> geophysics/geochem -> discovery hole -> resource drilling -> option/JV/M&A
```

不是：

```text
claim -> mine construction -> production
```

### 7.2 回报速度公式

对早期地块，更合理的预期价值公式是：

```text
EV = P_discovery × P_resource × P_transaction × TransactionValue
     - ExplorationCost
     - HoldingCost
     - PermittingAndBaselineCost
```

对生产型项目，才适合用：

```text
OperatingMargin_per_lb =
  U3O8_price
  - cash_cost
  - sustaining_cost
  - royalty
  - transport/conversion penalty
  - G&A allocation

ProjectValue ≈ Σ_t [ production_lb_t × OperatingMargin_t / (1+r)^t ]
               - initial_capex
               - closure/environmental liability
```

在 2026 年 5 月附近，公开市场评论显示 U3O8 spot/term 大致在高位区间波动，部分行业评论引用 spot 约 `US$86/lb`、long-term 约 `US$90/lb`。若用 PLS AISC `US$15.2/lb` 做 analog，理论单位 margin 很高；但对新地块不能直接套用，因为新地块没有资源、冶金、采矿方法、许可或处理厂。

### 7.3 不同地块类型的成本难度

| 地块类型 | 勘探成本 | 开发难度 | 回报速度 | 适合策略 |
|---|---:|---:|---:|---|
| 核心 PLC active claims | 高，因需交易/JV | 高但潜力最大 | 中，交易可快于开采 | option/JV/M&A |
| lapsed/possible gap near PNR | 中低 | 未知，偏关键矿物 | 中低，取决于 MARS gap 和样品验证 | 先 title + geochem |
| 外围完全 open grids | 低 | 未知，潜力低 | 低，除非快速发现 conductor/anomaly | 低成本 grassroots |
| 已开发级矿床邻区 | 极高 | 高 | 若并购成功最快，但资本要求大 | 公司层面交易 |

## 8. 推荐的下一步工作计划

### 8.1 第一阶段：矿权精查，1-3 天

目标：把“可能 open”变成“可 staking polygon”。

工作：

1. 在 MARS 中下载或手工导出当日：
   - active mineral dispositions；
   - lapsed mineral dispositions；
   - re-opening lands；
   - deemed partial cells；
   - restricted / withdrawn lands；
   - parcel grid。
2. 在 Saskatchewan projected CRS 中做 exact polygon difference：

```text
OpenCandidate = AOI
                - ActiveMineralDisposition
                - RestrictedLand
                - Water/Surface constraints where applicable
```

3. 对 lapsed ids 做 exact overlap：

```text
LapsedOpen = LapsedDisposition
             - ActiveMineralDisposition
             - RestrictedLand
```

4. 优先复核：
   - CAT lapsed cluster：`MC00013968`, `MC00013970`, `MC00014519`, `MC00014557`, `MC00013808`；
   - active good-standing watchlist 中 2026-2027 日期、`WORKWAITING=Yes` 的 claims，但注意 layer 仍显示 active，不能视为 open；
   - F4 / Stallion / Orano 边界。

### 8.2 第二阶段：证据叠加，1-2 周

对 exact open polygons 叠加：

- MDI uranium/gold/REE/base-metal points；
- government drillholes；
- assessment report drill assays；
- EM conductor plates；
- resistivity inversion；
- magnetic lineaments；
- 2019 airborne gravity first vertical derivative；
- lake sediment / till / soil / boulder U, B, Pb, Ni, Co, Cu, Mo, V, As；
- clay alteration / SWIR vector if有 core。

### 8.3 第三阶段：低成本验证，1-2 个野外季

对真正 open 且证据较强的地块：

1. airborne EM 或购买历史 EM；
2. ground HLEM / moving-loop TEM；
3. DC resistivity / IP；
4. lake sediment、till、boulder prospecting；
5. radon-in-water / radon-in-soil；
6. scintillometer prospecting；
7. pXRF + lab assay；
8. 若 conductor + alteration + U pathfinder 同时成立，再上 3-5 个 scout holes。

## 9. 数据缺口

本报告的主要数据缺口：

1. 未获得 MARS parcel-level 当日 legal title export；
2. lapsed layer 未提供 lapse date，不能确认是否最近 1-2 年失效；
3. active/lapsed 叠加采用 bbox screen，不是 exact polygon overlay；
4. 未下载 assessment reports 的完整 assay table；
5. 未获得 proprietary EM conductor plates 和 resistivity inversion grids；
6. 未做 CDoGS / SGS geochem raw table normalization；
7. 未计算精确 road/power/airport/mill distances；
8. 未做水文、环境、Indigenous consultation、surface access 风险图层；
9. gold/REE/Ni-Cu-Co evidence 多为点状 occurrence，需要矿物学和冶金验证。

## 10. 最终判断

如果只问“哪里最可能成为 Patterson Lake Corridor 的下一个热点”，答案是：

```text
JR-Broach-Minto-Smart Lake extension
Hook Lake-Spitfire-Bow-Harpoon corridor
Triple R-Arrow flanking second-order structures
```

如果加上“必须无 claim 或最近过期”，答案就变成：

```text
先做 PNR / Cache Lake lapsed cluster 的 exact MARS subtraction；
再做外围 PLC-234 / PLC-001 / PLC-026 / PLC-027 的低成本 grassroots；
不要把核心强证据 active tenure 区误判为空地。
```

我的实际建议：

1. **立即做 PNR / Cache Lake lapsed cluster 的 full tenure subtraction。**  
   这是最符合“可能过期/可能空档”的区域。

2. **建立 JR-Broach-Smart Lake 与 Hook-Spitfire-Bow 的 claim-expiry watchlist。**  
   这是最符合“地质最强”的区域，但主要靠交易、JV 或边界空档进入。

3. **把外围 open grids 当作低成本期权，不作为主资产叙事。**  
   它们适合便宜拿地和快速地球物理验证，但不应被宣传为等同于 Triple R / Arrow / JR。

4. **金矿只作为辅助价值，不作为 PLC 内的主线。**  
   现有公开证据更支持铀主导、多金属伴生，而非独立金矿开发。

## 11. 本次输出文件

- `patterson_lake_corridor_claim_gap_research_report_zh.md`：本报告；
- `evidence_matrix.csv`：证据矩阵；
- `patterson_claim_gap_grid_screen.mjs`：可复核网格筛选脚本；
- `data/raw/sk_active_mineral_dispositions.geojson`：官方 active tenure 下载；
- `data/raw/sk_lapsed_mineral_dispositions.geojson`：官方 lapsed tenure 下载；
- `data/raw/sk_mineral_exploration_drillholes.geojson`：官方钻孔下载；
- `data/raw/sk_mineral_deposits_index.geojson`：官方 MDI 下载；
- `data/raw/sk_government_rock_samples.geojson`：官方岩石样下载；
- `data/processed/patterson_lake_corridor_claim_gap_grid.csv`：网格筛选表；
- `data/processed/patterson_lake_corridor_top_grid_cells.geojson`：候选格网 GeoJSON；
- `data/processed/patterson_lake_corridor_screen_summary.json`：筛选摘要；
- `data/processed/active_claim_goodstanding_watch.csv`：active claims good-standing watchlist。

## 12. 来源链接

1. Saskatchewan Mineral Tenure Crown Dispositions MapServer: https://gis.saskatchewan.ca/arcgis/rest/services/Economy/P_Mineral_Tenure_Crown_Dispositions/MapServer
2. Saskatchewan Mineral Exploration MapServer: https://gis.saskatchewan.ca/arcgis/rest/services/Economy/Mineral_Exploration/MapServer
3. Saskatchewan MARS: https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/mineral-tenure/mineral-administration-registry-saskatchewan-mars
4. Card 2021 Patterson Lake Corridor abstract: https://hero.epa.gov/reference/8783454/
5. Powell et al. 2019 GSC Open File 8549: https://doi.org/10.4095/313671
6. GSC/AGS/SGS Patterson Lake airborne gravity, OF 8533: https://doi.org/10.4095/313525
7. GSC/AGS/SGS Patterson Lake first vertical derivative gravity, OF 8534: https://doi.org/10.4095/313526
8. NexGen Rook I Project: https://www.nexgenenergy.ca/rook-1-project/default.aspx
9. Paladin PLS Project update, 2025-08-27: https://www.nasdaq.com/press-release/patterson-lake-south-project-update-2025-08-28
10. F3 Uranium PLN / JR Zone NI 43-101 announcement: https://f3uranium.com/f3-files-ni-43-101-technical-report-for-previously-announced-initial-indicated-mineral-resource/
11. F3 Uranium PLN Area: https://f3uranium.com/projects/pln-area/
12. Purepoint Hook Lake Project: https://purepoint.ca/portfolio/hook-lake-project/
13. ANS Nuclear Newswire uranium price note, 2026-05-04: https://www.ans.org/news/2026-05-04/article-8000/uranium-prices-reflect-strong-outlook-raise-supply-questions/
