# GeoMine Research: 加拿大西北地区金矿潜力与 claim-gap 筛选

报告日期：2026-05-10  
AOI：Northwest Territories, Canada（中文常称“加拿大西北地区”，行政上为 territory，不是省）  
任务目标：用 GeoMine evidence lanes 筛选 NWT 金矿潜力，识别矿物带、伴生矿物、地球化学、钻孔/前期勘探证据，并提出用于寻找暂时未被 claim 的优质地块的下一步工作流。

## 0. 重要结论

本次筛选不能直接给出“已经确认未被 claim 的地块”。原因是矿权开放状态必须以提交 claim 当天的 NWT Mineral Tenure Web Map / Registrar 数据为准，并且还要叠加保护地、土地权益、Indigenous agreement area、地表进入许可和具体 claim staking 规则。本报告能给出的，是基于官方矿点、till 地球化学、矿权图层和公开钻孔资料的“找空档优先窗口”。

按“金矿证据强度 + 矿权压力相对较低 + 可继续验证”的综合排序，优先级如下：

| 排名 | 候选窗口 | 结论 |
|---:|---|---|
| 1 | South Rae / Hearne margin south of MacKay | 最适合先找 claim 空档。155 个官方含金矿点、57 个已钻矿点、2,336 个 till Au ppb 样品，Au ppb p95 为 22、p99 为 82、最高 322 ppb；活动 claim/lease 计数低于 Yellowknife 和 East Slave。 |
| 2 | East Slave Lac de Gras-MacKay-McCrea | 地球化学信号最强。1,550 个 till Au ppb 样品，p95 为 40、p99 为 420、最高 9,420 ppb；但活动 leases 和 claims 很密，可能与 diamond tenure 叠加，适合找边缘空档和 up-ice 源区。 |
| 3 | Central Slave Indin-Colomac-Courageous | 成矿带证据强，含 Colomac、Courageous、Tundra/Salmita 等；适合找二级剪切带、铁建造/BIF 接触带、mafic sill 平行带和项目边缘，不适合把已知项目核心区当空地。 |
| 4 | Yellowknife greenstone belt | 最高等级类比区，Con/Giant/Campbell shear 已验证高品位造山型金矿，但矿权、历史矿山、环境遗留和城市/基础设施约束大；主要用于建立模型，不是第一批大面积找空地对象。 |
| 5 | Great Bear magmatic zone | 纯金证据较弱，但 Au-Bi-Co-Cu-W 多金属系统有潜力；更像多金属/IOCG/侵入相关金目标。 |
| 6 | Mackenzie Mountains / Selwyn NWT | 有 Lened/MONA 等 Au-W-Cu 侵入相关或 skarn 信号，但全区金矿密度低，且活动 claim/permit 也不少；只做特定靶区筛选。 |

## 1. GeoMine 方法与 AOI 标准化

### 1.1 AOI

- 标准化名称：Northwest Territories gold prospectivity screening
- CRS：WGS84 / EPSG:4326
- 范围：territory-scale screening，随后切成 6 个 evidence windows。
- 输入限制：用户没有提供具体 polygon，故所有统计使用宽泛 bbox。bbox 适合战略筛选，不适合法律 staking。

### 1.2 Evidence lanes

本次使用以下 GeoMine evidence lanes：

| Evidence lane | 本次使用的数据 | 用途 |
|---|---|---|
| AOI/CRS normalization | GeoMine MCP `normalize_aoi` | 确认 AOI 为空间概念而非正式 polygon。 |
| Canada geodata discovery | GeoMine MCP `search_canada_geodata` + NTGS/GNWT endpoints | 找官方矿点、till、矿权、地质/地球物理数据源。 |
| CDoGS geochemical lane | CDoGS + NTGS till geochemistry | 识别区域地球化学调查、till Au 和伴生元素调查。 |
| Mineral occurrences | NTGS Mineral Showings 2021 | 统计含金矿点、发育阶段、矿床类型、岩性和构造标签。 |
| Drilling / prior exploration | NTGS showings dev stage + company technical/news disclosure | 识别已钻矿点、先进项目和可参考钻孔。 |
| Tenure / claim pressure | GNWT Mineral Tenure Web Map / Economy_LCC MapServer | 统计候选窗口内活动 claims / leases / prospecting permits。 |
| Deposit model | 造山型金、BIF-hosted gold、mafic sill-hosted gold、intrusion-related/skarn Au-W-Cu-Bi、polymetallic Great Bear systems | 解释为什么某些证据组合有意义。 |

### 1.3 MCP 使用情况

GeoMine MCP 对 NWT 的 Canada geodata / CDoGS 搜索返回的是发现和规划结果，不是完整 live HTTP 抓取。本报告中的数值统计来自之后直接访问的官方 NTGS / GNWT ArcGIS REST、CDoGS 页面和公开公司披露。MCP 结果用于规范 AOI、证据车道和数据源优先级。

## 2. 官方数据源与 provenance

### 2.1 NTGS / GNWT 官方数据

- NTGS Web Applications 页面显示其提供 7 个 Web Apps；其中 Mineral Showings 有 3,108 条记录，References 数据库有 10,166 条 geoscience publications/reports，可检索 assessment reports、open files/reports、theses 等。来源：<https://app.nwtgeoscience.ca/>
- NTGS Open Data Hub：<https://ntgs-open-data-ntgs.hub.arcgis.com/>
- NTGS Mineral Showings 2021 FeatureServer：<https://services3.arcgis.com/GSr8HAQhtEt4sNnv/ArcGIS/rest/services/NWTShowings2021a/FeatureServer/0>
- NT-NU Till Geochemistry FeatureServer：<https://services3.arcgis.com/GSr8HAQhtEt4sNnv/ArcGIS/rest/services/NT_NU_TillGeochemistry/FeatureServer/0>
- Past and Current Producers FeatureServer：<https://services3.arcgis.com/GSr8HAQhtEt4sNnv/ArcGIS/rest/services/Past_Current_Producers/FeatureServer/0>
- Selected Advanced Projects FeatureServer：<https://services3.arcgis.com/GSr8HAQhtEt4sNnv/ArcGIS/rest/services/Selected_Adv_Projects/FeatureServer/0>
- NWT Mineral Tenure Web Map：<https://www.maps.geomatics.gov.nt.ca/Html5Viewer_PROD/index.html?viewer=NWT_MTV>
- GNWT Economy_LCC MapServer mineral tenure layers：<https://www.apps.geomatics.gov.nt.ca/arcgis/rest/services/GNWT/Economy_LCC/MapServer>

矿权层字段包括 `CLAIM_NUM`、`CLAIM_STAT`、`ISSUE_DT`、`ANNIV_DT`、`AREA_HA`、`OWNERS`、`CLAIM_NAME`、`GROUND_OPEN_DATE`、`LAND_CLAIM_AREA`。这些字段支持下一步做真正的 open-ground subtraction。

### 2.2 CDoGS / Canada geochemistry

- CDoGS 是 Canadian Database of Geochemical Surveys，公开界面说明其目标是编目加拿大自 1950s 以来的区域地球化学调查，并尽量提供标准化原始数据。来源：<https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm>
- CDoGS NWT 例子 1：NTS 85C/D/E/F southern NWT 2009 till sampling survey，103 个样点，包含 KIM、MMSIM 和 gold grains，覆盖 Kakisa/Tathlina Lakes 一带。来源：<https://geochem.nrcan.gc.ca/cdogs/content/svy_ext/svy270004_e.ext.htm>
- CDoGS NWT 例子 2：NTS 85N/86C/D/E/F lithogeochemical survey，669 个站点，Great Bear Lake east / Lac La Martre east 一带。来源：<https://geochem.nrcan.gc.ca/cdogs/content/svy_ext/svy210333_e.ext.htm>

### 2.3 公司披露与钻孔资料

这些资料用于“已知矿床与成矿模型验证”，不是用来替代官方矿权核验。

- Gold Terra Campbell Shear：公司页面披露 Phase 1 winter drilling 13 holes / 7,242 m，并称所有孔均 intersect Campbell Shear，支持 Con Mine 以南超过 2 km 的连续性；同页还给出 Yellowknife River Fault Zone、Campbell/Giant shear 与 Con/Giant 历史产金的构造模型。来源：<https://goldterracorp.com/projects/yellowknife-project/campbell-shear-priority-target/>
- Gold Terra 2025-01-10：2025 wedge drilling 从 master hole GTCM24-056 开始，该孔深 3,002 m，用于评估 Robertson shaft 深部 600 m 以下的 Campbell Shear。来源：<https://goldterracorp.com/news/gold-terra-announces-start-of-2025-drilling-progra-9865/>
- Gold Terra 2025-05-26：GTCM25-056A 在 2,680.5-2,703.5 m downhole intersected anomalous Au/Ag；footwall brecciated pyrite-pyrrhotite quartz veins 中有 7.81 g/t Au over 0.5 m。来源：<https://goldterracorp.com/news/gold-terra-confirms-campbell-shear-gold-potential-10145/>
- STLLR Colomac 2024：C24-07 为 1.56 g/t Au over 62.30 m，C24-06 为 1.12 g/t Au over 99.40 m，C24-10 为 0.74 g/t Au over 35.25 m 且含多个窄高品位段；公司描述 Colomac Main 位于约 9 km 长、最宽 155 m 的 differentiated mafic sill 中，伴随 quartz-carbonate veins、minor sulphides 和 coarse/free gold。来源：<https://stllrgold.com/news/stllr-gold-intersects-1-56-g-t-au-over-62-30-m-and-1-12-g-t-au-over-99-40-m-at-the-colomac-main-deposit>
- Seabridge Courageous Lake 2024/2026：Courageous Lake 是 NWT 大型未开发金项目，公司披露 2024 NI 43-101 PFS/PEA、51-54 km prospective greenstone belt、沿带 gold showings and historical drill intercepts；2026-04-27 披露拟 spin-out 为 Valor Gold 并推进 satellite target drilling。来源：<https://www.seabridgegold.com/press-release/seabridge-gold-files-updated-ni-43-101-courageous-lake-technical-report>、<https://www.seabridgegold.com/press-release/seabridge-gold-provides-update-on-courageous-lake-spin-out-information-circular-available-on-sedar-meeting-date-may-22nd-2026>

## 3. 区域成矿背景

### 3.1 NWT 金矿最重要的一阶判断

NWT 的金矿潜力不是均匀分布的。官方 showings 统计显示，1,002 个含金矿点中约 870 个在 Slave geological province，远高于 Bear、Cordilleran、Rae/Churchill 等省份。也就是说，找 NWT 金矿第一优先仍然是 Slave Craton 内的 Archean greenstone belts、主要剪切带、BIF/iron formation、mafic volcanic/intrusive contacts，以及这些构造的覆盖区和边缘区。

### 3.2 主要矿床模型

#### A. Archean orogenic gold

这是 Yellowknife、Con/Giant/Campbell shear、Discovery、Nicholas Lake、Tundra/Salmita、Courageous Lake、Colomac 周边最关键的模型。

判别特征：

- 大型区域剪切带和二级/三级 splays。
- 石英-碳酸盐脉、sericite-carbonate-chlorite alteration。
- pyrite、pyrrhotite、arsenopyrite，局部 stibnite/antimony、lead、silver。
- 主岩：greywacke/turbidite、mafic volcanic、schist、slate、iron formation、gabbro/diorite/mafic sill。
- 地球化学：Au 与 As-Sb-Ag-Pb-Bi-W 局部伴生；在 till 中可表现为 Au grains 或 Au ppb 异常，必须结合冰流方向回溯源区。

#### B. BIF / iron formation associated gold

Central Slave 与 Indin-Courageous 一带官方矿点标签中 iron formation 很突出。铁建造型金矿常与剪切、褶皱 hinge、硫化物替代、magnetite/pyrrhotite 破坏带有关。

判别特征：

- 磁性高带被断裂错断或局部退磁。
- Au 与 pyrite-pyrrhotite-arsenopyrite，局部 Ag/Pb/Zn。
- BIF 与 mafic volcanic / turbidite 接触处出现 quartz-carbonate veins 和剪切蚀变。

#### C. Mafic sill hosted gold, Colomac-style

Colomac Main 是非常有用的模型类比。STLLR 披露其主矿体位于 north-south striking differentiated mafic sill，矿化以 free/coarse gold、quartz-carbonate veins、minor sulphides 为主。找新地块时，应关注：

- 线性 mafic sill 或 differentiated mafic intrusive body。
- sill 内部岩相变化、cross-cutting faults、局部弯曲/扩张段。
- 既有钻孔稀疏的 down-dip/down-plunge 或 strike extension。

#### D. Intrusion-related / skarn Au-W-Cu-Bi

Lened、Mackenzie/Selwyn 和部分 Bear province 多金属点更适合这个模型。

判别特征：

- Au 与 W-Cu-Bi-Mo-As-Sb，scheelite/chalcopyrite/bismuthinite/pyrrhotite。
- reduced intrusion、monzonite/granite/granodiorite、carbonate contact、skarn。
- 金矿潜力可能较局部，不能用 Slave greenstone 的标准直接外推。

#### E. Great Bear magmatic-polymetallic systems

Great Bear magmatic zone 不是本次 pure gold 第一优先，但 NICO 官方 advanced project 的 Co-Au-Cu-Bi-W-Fe 组合说明该省份存在 Au-bearing polymetallic hydrothermal systems。若目标是金叠加 Bi-Co-Cu-W，应关注结构交汇、magmatic-hydrothermal alteration 和红层/IOCG 类似系统。

## 4. 官方矿点证据

### 4.1 全 NWT 含金矿点统计

我从 NTGS Mineral Showings 2021 layer 查询所有 `COMM_ALL` 或 A-E commodity 含 Gold 的记录，共得到 1,002 条。

按地质省：

| Geological province | Gold showings |
|---|---:|
| Slave | 870 |
| Bear | 54 |
| Cordilleran | 31 |
| Churchill - Rae | 25 |
| Churchill | 20 |
| Arctic / Interior / Hudson platforms | 2 |

按发育阶段：

| Development stage | Count | 判断 |
|---|---:|---|
| Reconnaissance | 365 | 早期矿点多，仍有找空档空间。 |
| Local Examination | 282 | 有地表工作，但不少未系统钻探。 |
| Drilled | 267 | 已验证到钻探阶段，是找二级延伸的关键证据。 |
| Advanced Exploration | 46 | 多数核心区很可能已有矿权或历史矿权。 |
| Minor/Past Producer categories | 36+ | 证明成矿系统真实，但通常矿权/环境/基础设施约束更强。 |

按数据库矿床类型：

| Deposit type | Count | 解释 |
|---|---:|---|
| Unclassified | 968 | NTGS showings 的 deposit-type 字段不够细，不能说明真实模型未知；需用构造、岩性、矿物和 drill/assessment reports 解释。 |
| Placer | 15 | 局部，不是本次重点。 |
| Intrusion-related | 12 | 主要在 Cordilleran / Bear / Selwyn 类窗口。 |
| Carbonate-hosted Zn-Pb | 6 | 金多为伴生/异常，不是主金目标。 |

### 4.2 岩性、构造和伴生信息

从 NTGS `CHARAC1-5` 与 `LITHOLOGY1-5` 字段统计，含金矿点最常见证据为：

- Quartz vein：359 条明确标记 quartz vein，另有 84 条 vein。
- Shear：155 条。
- Iron formation：105 条。
- Mafic volcanic：88 条。
- Sedimentary / turbidite / greywacke：sedimentary 120、turbidite 52、greywacke lithology 182。
- Lithology 中 quartz 434、volcanic 175、iron formation 97、schist 92、basalt 55、tuff 50、granite 50。

我的判断：这组统计高度吻合造山型金矿和 BIF/greenstone-hosted gold。对找 claim 空档最有用的不是“矿点数量最大”的城市/矿山核心，而是 quartz vein + shear + iron formation/mafic volcanic/turbidite 组合在矿权边缘或覆盖区重复出现的位置。

### 4.3 代表性官方矿点

| 区域 | NTGS showing examples | 发育阶段 / commodity |
|---|---|---|
| Yellowknife | Con Mine, Giant Mine, Crestaurum, MON Mine, Viking Yellowknife | Past producer / care and maintenance / advanced; Au-Ag, Au-Sb-Pb 等。 |
| Discovery-Nicholas-Ormsby | Nicholas Lake, Discovery Mine, Ormsby Zone | Advanced / past producer / Au-Ag。 |
| Indin-Colomac | Colomac, Lexindin zones, Treasure Island, Indin Zone, Damoti Lake, CATHY-Echo Indin | Past producer / advanced / drilled / Au-Ag。 |
| Tundra-Salmita-Courageous | Tundra Gold Mine, Salmita North/South/New Discovery, Tundra-Fat, Courageous Lake-1/2 | Past producer / advanced / local examination / Au-Ag。 |
| Bear / Great Bear | NICO, Contact Plateau, Terra district | Co-Au-Cu-Bi-W-Fe, Cu-Au, Ag-Cu-U-Co-Ni 等多金属系统。 |
| Cordilleran/Selwyn | Lened, MONA | W-Cu-Au, Au-Ag-Zn-Pb-W；侵入相关/多金属。 |

## 5. 地球化学证据

### 5.1 Till Au 数据处理

NT-NU Till Geochemistry layer 中，NWT `C_ELEMENT = Au` 的记录共有 7,298 行。其中：

- Au ppb 行：6,769 行。
- Au ppm 行：529 行。
- ppb 行统计更适合本次 first-pass ranking：median 5 ppb，p90 10 ppb，p95 15 ppb，p98 40 ppb，p99 110 ppb，最大 9,420 ppb。
- ppm 行存在同一样品 Au ppb 与 ppm 重复记录的情况，很多值集中在 2 或 5 ppm，可能代表不同方法、重分析、限值或数据结构差异；本报告不把 ppm 行直接并入 ranking，避免把重复/限值误当异常。

### 5.2 最关键 Au till 异常

| 样品 | Au ppb | lon | lat | report ID | 初步解释 |
|---|---:|---:|---:|---|---|
| J922072 | 9,420 | -111.52176 | 63.91144 | 083289 | 极强单点异常；需要查原 assessment/open report、采样介质、金粒形态、冰流方向和周边矿权。 |
| J922079 | 790 | -111.56059 | 63.96784 | 083289 | 与 J922072 同报告、同窗口，支持 East Slave / MacKay-Lac de Gras 异常带。 |
| J922062 | 450 | -111.79215 | 63.70649 | 083289 | 同一大窗口内，可能为冰川搬运路径或局部源区。 |
| 921311 | 1,680 | -109.87126 | 63.85189 | 083372 | East Slave 东部强异常，需与 diamond tenure 和 greenstone/structure overlay。 |
| 925042 | 1,170 | -109.81592 | 63.66835 | 083372 | 与 921311 形成区域性关注带。 |
| 922618 | 1,010 | -109.89357 | 64.18746 | 083277 | East Slave 北部/中部异常。 |
| 1274 | 322 | -108.27250 | 62.55130 | 084080 | South Rae / Hearne margin 子窗口核心异常之一。 |
| 736 | 310 | -108.29460 | 62.57930 | 084080 | 与 1274 构成紧凑异常群。 |
| 649 | 236 | -108.26770 | 62.57900 | 084080 | 同报告同窗口；适合做 up-ice tracing。 |
| 1256 | 212 | -108.30620 | 62.55360 | 084080 | South Rae 子窗口。 |

解释逻辑：

- till Au 异常必须按冰流方向回溯，不可直接在样点下方画靶。
- 单点 9,420 ppb 非常强，但仍需验证样品类型、粒度、重分析、QA/QC、是否 nugget effect。
- 多点中等异常比单点极值更适合 claim-gap 筛选，尤其当它与 shear/BIF/mafic volcanic contacts、磁性线性、历史矿点同向排列时。

### 5.3 伴生元素与 pathfinder

NTGS till 数据中 NWT 还有大量 As、Sb、Bi、W、Ag、Cu、Pb、Zn、Mo、Hg、Co、Ni 等元素行。对金矿筛选的实际用法：

- 造山型金：Au + As/Sb/Ag/Pb +/- Bi/W；若 Au 异常旁边 As/Sb 不高，不排除金矿，因为 coarse gold/nugget effect 可单独表现。
- Colomac-style mafic sill：Au + minor sulphides，As/Sb 可弱；更要看 mafic sill、quartz-carbonate vein、fault offsets。
- BIF-hosted：Au + Fe/magnetic high + pyrite/pyrrhotite/arsenopyrite，局部 As/Sb。
- Intrusion-related/skarn：Au + W/Bi/Mo/Cu，尤其在 Lened/Mackenzie/Selwyn。
- Great Bear polymetallic：Au + Bi/Co/Cu/W/Ag/U；更适合多金属 portfolio。

## 6. 钻孔和前期勘探证据

### 6.1 Yellowknife / Campbell Shear

这是 NWT gold model 的最高等级验证区。

证据：

- Gold Terra 披露 Campbell Shear Phase 1 winter drilling：13 holes / 7,242 m，所有孔均 intersect Campbell Shear，并支持 Con Mine 以南超过 2 km 的矿化连续性。
- 2025 年深部 wedge program：master hole GTCM24-056 深 3,002 m，用于从深部 wedge 测试 Campbell Shear。
- GTCM25-056A 在 2,680.5-2,703.5 m downhole intersected anomalous Au/Ag，footwall brecciated pyrite-pyrrhotite quartz veins 中有 7.81 g/t Au over 0.5 m。
- 公司披露 Campbell/Giant/Con shear 系统与 Yellowknife River Fault Zone 有关，成矿带长度远大于历史生产区。

判断：

- Campbell/Con/Giant 是强造山型金矿模型，不是找空地的直接目标。
- 真正可用的启发是：在 NWT 其他 greenstone belts 中，找 regional-scale faults 的 secondary/tertiary splays、sericite-carbonate-chlorite shear、quartz-carbonate veins、pyrite-pyrrhotite-arsenopyrite zone。
- Yellowknife 由于活动 claims 216、leases 232，且有城市/legacy mine 约束，不是第一优先“未 claim 大地块”。

### 6.2 Colomac / Indin belt

证据：

- NTGS official showing：Colomac 为 Au-Ag past producer / care and maintenance；Lexindin、Treasure Island、Indin Zone、Damoti Lake 等周边多点为 advanced/drilled/local examination。
- STLLR 2024 drilling at Colomac Main：
  - C24-06：1.12 g/t Au over 99.40 m；hole detail easting 591926.99, northing 7141518.01, azimuth 298, inclination -77, end depth 402 m。
  - C24-07：1.56 g/t Au over 62.30 m；easting 592059.00, northing 7141951.00, azimuth 270, inclination -78, end depth 415 m。
  - C24-10：0.74 g/t Au over 35.25 m，含多个窄高品位段；easting 591845.00, northing 7141314.00, azimuth 279, inclination -80, end depth 441 m。
- 公司解释 Colomac Main 位于约 9 km 长的 north-south differentiated mafic sill，矿化为 free/coarse gold + quartz-carbonate veining + minor sulphides，并与 cross-cutting faults 有关。

判断：

- Colomac-style 对寻找未 claim 地块的启发非常强：不是只找绿岩带，而是找 mafic sill 的相变、offset fault、parallel sill 和未钻的 down-dip/along-strike segments。
- 但 Central Slave 窗口活动 leases 151、claims 50、permits 4，历史项目区不太可能完全空白；应找项目核心外的二级构造空档。

### 6.3 Courageous Lake / Tundra-Salmita

证据：

- NTGS showing：Tundra Gold Mine、Salmita North/South/New Discovery、Tundra-Fat、Courageous Lake-1/2 等构成 gold-bearing greenstone corridor。
- Seabridge 2024/2026 disclosure：Courageous Lake 是 NWT 大型未开发金项目，技术报告和 2026 spin-out 信息披露显示其沿 51-54 km prospective greenstone belt 分布 gold showings and historical drill intercepts。

判断：

- Courageous Lake 证明 eastern/central Slave greenstone belt 的成矿尺度很大。
- 对新 claim 机会，重点不应在 Courageous 主项目和 known Walsh Lake/satellite 核心，而应看沿带浅钻截获和矿点之间的结构空白、covered greenstone slivers、BIF/mafic contacts。
- 该区技术资料多，但需要下一步下载 NI 43-101 appendices 和 assessment reports 做 drill hole database extraction。

### 6.4 South Rae / Hearne margin

证据：

- 155 个官方含金矿点，57 个已钻，3 个 advanced。
- 2,336 个 till Au ppb 样品，p95 22 ppb、p99 82 ppb、最高 322 ppb。
- 顶级异常样品集中于 report 084080 附近：1274、736、649、1256、1388 等，坐标约 -108.31 至 -108.27、62.55 至 62.58。
- 活动 mineral claims 85、leases 99、prospecting permits 0，低于 Yellowknife 和 East Slave 的矿权压力。

判断：

- 这是本报告最建议优先做 claim-gap GIS subtraction 的窗口。
- 逻辑不是“这里最大矿床已知”，而是“有足够矿化证据 + 地球化学异常 + 已钻/未完全成熟的组合 + 相对较低 tenure pressure”。
- 适合寻找被 till cover、湖泊、低露头率掩盖的 shear/BIF/mafic volcanic targets。

### 6.5 Great Bear 和 Mackenzie/Selwyn

Great Bear：

- 官方 gold showings 26，drilled 6；NICO 为 advanced Co-Au-Cu-Bi-W-Fe。
- 活动 claims 4、leases 1、permits 19。
- 更适合多金属 Au-Bi-Co-Cu-W，不是 first-pass pure-gold best target。

Mackenzie/Selwyn：

- 官方 gold showings 9，drilled 1，advanced 1；Lened 为 W-Cu-Au intrusion-related advanced project。
- 活动 claims 281、leases 21、permits 27，说明该区其他 commodity competition 可能较强。
- 金矿模型更局部，围绕 intrusions / skarn / carbonate contacts 做小靶区，不建议作为 NWT 金矿空地主战场。

## 7. 候选窗口证据矩阵

| Window | Bbox WGS84 | Gold showings / drilled / advanced | Till Au ppb stats | Active tenure count | Score | Claim-gap 判断 |
|---|---|---:|---|---|---:|---|
| South Rae / Hearne margin south of MacKay | -113.0,61.3,-108.0,63.5 | 155 / 57 / 3 | n=2,336; p95=22; p99=82; max=322 | claims 85; leases 99; permits 0 | 78 | 第一优先找空档窗口。 |
| East Slave Lac de Gras-MacKay-McCrea | -112.0,63.2,-107.5,65.2 | 56 / 18 / 6 | n=1,550; p95=40; p99=420; max=9,420 | claims 189; leases 375; permits 0 | 76 | 异常最强，但矿权密；找边缘和 up-ice 源区空档。 |
| Central Slave Indin-Colomac-Courageous | -116.5,63.8,-112.0,65.8 | 227 / 57 / 11 | n=2,916; p95=5; p99=10; max=225 | claims 50; leases 151; permits 4 | 72 | 成矿带强，适合项目边缘和二级结构。 |
| Yellowknife city-greenstone belt | -114.8,61.7,-113.0,63.0 | 286 / 89 / 11 | n=1; max=7.3 | claims 216; leases 232; permits 0 | 66 | 模型区，不是大面积空地优先区。 |
| Great Bear magmatic zone | -123.5,65.0,-116.5,67.8 | 26 / 6 / 0 | no NTGS till Au in bbox | claims 4; leases 1; permits 19 | 54 | 多金属 Au 机会，纯金证据较弱。 |
| Mackenzie Mountains / Selwyn NWT | -130.5,62.0,-123.0,65.5 | 9 / 1 / 1 | no NTGS till Au in bbox | claims 281; leases 21; permits 27 | 45 | 只做特定 Au-W-Cu/skarn 靶区。 |

评分逻辑：地质/成矿带 25%，地球化学 20%，矿点/钻孔/历史生产 20%，claim-gap 可能性 20%，基础设施 10%，数据质量 5%。该评分是 prospectivity screening，不是资源量、储量或投资建议。

## 8. 具体找地逻辑

### 8.1 我会怎么判断一块地值得 claim-gap 跟进

第一步看是否在 Slave Craton greenstone / Rae-Hearne margin 的可成矿岩性内，而不是只看一个 Au 点。

第二步看结构：区域断裂、二级剪切、BIF/mafic volcanic/turbidite contacts、mafic sill 和 cross-fault intersection。对 NWT 这种露头和覆盖条件混合的区域，结构控制比单一元素异常更可靠。

第三步看 geochemistry：till Au ppb 异常要按 survey/report 分组，不同报告之间不能直接拿绝对值硬比。最优先的是同一报告内多点异常、异常沿冰流上游可回溯到合理岩性/结构，并且附近有 Au-As-Sb-Bi-W 或 Au grains/MMSIM 支持。

第四步看 drill evidence：已钻矿点不是为了在老项目上抢地，而是为了验证模型。比如 Colomac 钻孔证明 mafic sill + quartz-carbonate vein + cross-fault 可以形成连续矿化；Campbell Shear 证明深部和 strike extensions 可保存高品位 shoots；Courageous Lake 证明较长 greenstone belt 上多个 showings / historical drill intercepts 可以共同构成 belt-scale opportunity。

第五步看矿权：用活动 claims/leases/permits 先做粗筛，再下载 polygon 做真正 subtraction。没有这一步，不能说“未 claim”。

### 8.2 最值得立即做 GIS claim-gap 的 5 个子靶区

| 子靶区 | 近似中心 | 证据 | 下一步 |
|---|---:|---|---|
| SR-1 South Rae Au till cluster | -108.29, 62.56 | report 084080 多点 Au ppb 210-322；South Rae window 矿点和已钻点密度足够，矿权压力相对较低。 | 下载 active tenure polygons，沿冰流 up-ice 2-10 km buffer，找 mafic volcanic/BIF/shear 交点。 |
| ES-1 MacKay / Lac de Gras west anomaly | -111.52, 63.91 | J922072 Au 9,420 ppb，J922079 790 ppb，J922062 450 ppb；同报告 083289，异常强。 | 先核验是否在 diamond leases/claims 内；若不在，查原报告 QA/QC 与 gold grain morphology。 |
| ES-2 East Slave eastern anomaly | -109.85, 63.8 | 921311 1,680 ppb、925042 1,170 ppb、922618 1,010 ppb，report 083372/083277。 | 与 magnetic/EM lineaments 和 greenstone slivers 叠加，排除 diamond-focused leases。 |
| CS-1 Central Slave Colomac-Indin fringe | -113.98, 64.92 / -112.37, 65.00 | Au till 225/210/130/115/95 ppb；邻近 Colomac/Indin/Courageous known belt。 | 找 known deposits 外 5-20 km 的 mafic sill/BIF parallel structures。 |
| YK-analog Campbell/Yellowknife extensions | -114.3, 62.4 至 north/south strike | 286 gold showings、89 drilled、Campbell/Con/Giant 造山型模型强。 | 只做模型和小空档核验；不作为大面积 first-pass staking。 |

## 9. 假设

- 活动矿权计数是 2026-05-10 访问 GNWT MapServer 时的 broad bbox feature counts；不是面积占比，不代表 bbox 内没有空地。
- NTGS showings 的 `Deposit_ty = Unclassified` 不代表没有模型，只代表数据库分类不足；本报告用岩性/构造/矿物/钻孔证据做模型解释。
- Till Au ppb 行优先于 ppm 行用于统计，因为 ppm 行存在重复/方法差异风险。
- 公司披露的资源/储量/PEA/PFS 信息只用于证明 belt fertility 和钻孔验证，不用于本报告自行估算资源量或经济性。
- Gold Terra、STLLR、Seabridge 的披露按公司/NI 43-101 风险提示处理；本报告不是 Qualified Person opinion。

## 10. 数据空缺

- 没有下载完整 mineral tenure polygon 并做 polygon subtraction；所以还没有法律意义上的 unclaimed parcels。
- 没有逐份解析 NTGS assessment reports 083289、083279、083372、084080、083862 等；这些报告应包含原始 sampling method、QA/QC、可能的 maps 和历史工作。
- 没有叠加冰流方向、surficial geology、transport distance；till Au 异常必须做 up-ice correction。
- 没有做 airborne magnetic/EM/radiometric/grav lineament interpretation；这对 shear/BIF/mafic sill targets 是关键。
- 没有检查 land withdrawal、protected areas、Indigenous land agreements、surface access、environmental liabilities。
- 没有把 CDoGS 所有 NWT survey polygons 批量下载并标准化到同一 geodatabase。
- 没有在 report 中复核每个公司技术报告附录里的完整 drillhole database。

## 11. 下一步工作流

### 11.1 GIS claim-gap workflow

1. 从 GNWT Economy_LCC MapServer 下载 active claims、leases、prospecting permits 的 full geometry。
2. 从 NTGS 下载 showings、till Au、regional geology、airborne mag/EM、geological provinces、Slave/Rae boundaries。
3. 坐标统一到 EPSG:3978 或本地合适 equal-area CRS，用 WGS84 只做展示。
4. 建立 target buffers：
   - Au till ppb p99+ 样点：按冰流 up-ice 2、5、10 km 多级 buffer。
   - quartz vein + shear + iron formation/mafic volcanic showings：1-3 km structural buffer。
   - known producers/advanced projects：排除核心 tenure，保留 5-20 km belt-extension search zone。
5. 用 active tenure dissolve polygon 做 subtraction，得到 candidate open polygons。
6. 排除 protected/withdrawn/settlement/restricted lands。
7. 对剩余 polygons 计算 score：geochem、structure、lithology、nearby drilling、access、claim geometry、land status。
8. 在 claim staking 前当天复核 live map 的 `GROUND_OPEN_DATE`、status、owner、anniversary date。

### 11.2 地球化学和野外验证

- 对 SR-1、ES-1、ES-2 先下载原报告，确认样品介质、粒度、重分析、gold grain count、冰流方向。
- 设计 250-500 m spaced reconnaissance till/soil lines，异常区加密到 50-100 m。
- 分析 Au + As + Sb + Bi + W + Te + Ag + Cu + Pb + Zn + Mo + Hg；如果预算允许，增加 gold grain morphology / pristine vs modified grains。
- 在结构交汇和磁异常处做 prospecting、grab/channel sampling。
- 如果露头少，先做 drone mag / ground mag + VLF/EM，再布置 trench 或 scout drilling。

### 11.3 钻探优先级

- South Rae / Hearne：先 drill 浅部 shear/BIF/mafic volcanic contacts，而不是直接在 till 样点下钻。
- East Slave：只有在确认不落入 active leases/claims 后，才把强 till Au 异常作为 scout drilling target；否则做周边空档。
- Central Slave：围绕 mafic sill/parallel sill、BIF contact、Colomac/Indin/Courageous 外围二级结构做 short RC/diamond scout holes。
- Yellowknife：如果要做，重点是 near-surface Campbell/Giant shear analog gaps；但法律、城市、legacy mine risk 要先排除。

## 12. 最终建议

若目标是“寻找暂时还没被 claim 的优质地块”，我建议第一阶段不要从 Yellowknife 或已知大项目核心开始，而是：

1. 先做 South Rae / Hearne margin south of MacKay 的 full tenure subtraction。这一窗口兼具矿点、已钻点、till Au 异常和相对较低矿权压力，是最符合任务目标的区域。
2. 同时做 East Slave Lac de Gras-MacKay-McCrea 的异常源追踪，但把矿权风险作为第一过滤器。这里的 geochem 最强，若有 legal gap，优先级很高。
3. 把 Central Slave Indin-Colomac-Courageous 作为 belt-extension portfolio，不碰 known project cores，只找二级结构、parallel sill、BIF contacts 和矿权边界外空档。
4. Yellowknife 作为成矿理论和钻孔模型，不作为大面积找空地的第一目标。
5. Great Bear 和 Mackenzie/Selwyn 只在用户愿意接受 Au-polymetallic / Au-W-Cu-Bi 模型时继续。

## 13. Source register

- NTGS Web Applications: <https://app.nwtgeoscience.ca/>
- NTGS Open Data Hub: <https://ntgs-open-data-ntgs.hub.arcgis.com/>
- NTGS Mineral Showings 2021 FeatureServer: <https://services3.arcgis.com/GSr8HAQhtEt4sNnv/ArcGIS/rest/services/NWTShowings2021a/FeatureServer/0>
- NT-NU Till Geochemistry FeatureServer: <https://services3.arcgis.com/GSr8HAQhtEt4sNnv/ArcGIS/rest/services/NT_NU_TillGeochemistry/FeatureServer/0>
- GNWT NWT Mineral Tenure Viewer: <https://www.maps.geomatics.gov.nt.ca/Html5Viewer_PROD/index.html?viewer=NWT_MTV>
- GNWT Economy_LCC MapServer: <https://www.apps.geomatics.gov.nt.ca/arcgis/rest/services/GNWT/Economy_LCC/MapServer>
- CDoGS homepage: <https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm>
- CDoGS southern NWT till survey 270004: <https://geochem.nrcan.gc.ca/cdogs/content/svy_ext/svy270004_e.ext.htm>
- CDoGS Great Bear area lithogeochemical survey 210333: <https://geochem.nrcan.gc.ca/cdogs/content/svy_ext/svy210333_e.ext.htm>
- Gold Terra Campbell Shear priority target: <https://goldterracorp.com/projects/yellowknife-project/campbell-shear-priority-target/>
- Gold Terra 2025 drilling start: <https://goldterracorp.com/news/gold-terra-announces-start-of-2025-drilling-progra-9865/>
- Gold Terra 2025 GTCM25-056A result: <https://goldterracorp.com/news/gold-terra-confirms-campbell-shear-gold-potential-10145/>
- STLLR Colomac 2024 drilling: <https://stllrgold.com/news/stllr-gold-intersects-1-56-g-t-au-over-62-30-m-and-1-12-g-t-au-over-99-40-m-at-the-colomac-main-deposit>
- Seabridge Courageous Lake 2024 technical report filing: <https://www.seabridgegold.com/press-release/seabridge-gold-files-updated-ni-43-101-courageous-lake-technical-report>
- Seabridge Courageous Lake 2026 spin-out update: <https://www.seabridgegold.com/press-release/seabridge-gold-provides-update-on-courageous-lake-spin-out-information-circular-available-on-sedar-meeting-date-may-22nd-2026>
