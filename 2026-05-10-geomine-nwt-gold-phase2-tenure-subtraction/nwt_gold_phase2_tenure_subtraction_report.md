# GeoMine Research Phase 2: NWT 金矿矿权扣减、异常源追踪与优先地块筛选

报告日期：2026-05-10  
检索时间：2026-05-10T01:22:20Z  
AOI：加拿大 Northwest Territories，重点为 South Rae / Hearne margin south of MacKay、East Slave Lac de Gras-MacKay-McCrea、Central Slave Indin-Colomac-Courageous  
Commodity：Au，兼顾 As-Sb-Bi-W-Ag-Cu-Pb-Zn-Mo-Hg 等 pathfinders  
输出目录：`report/2026-05-10-geomine-nwt-gold-phase2-tenure-subtraction/`

## 1. 结论摘要

这次二阶段工作完成了三件事：

1. 对三个重点窗口下载 GNWT 官方 active mineral claims、active mineral leases、active prospecting permits geometry。
2. 使用 GNWT ArcGIS GeometryServer 做 active tenure union，并用窗口 bbox 减去 active tenure union，得到 open-ground difference geometry。
3. 用 tenure-clear 网格把 open ground 与 NTGS till Au 异常、官方金矿点、已钻/advanced showings 叠加，给出下一步 claim-gap 优先级。

核心结论：

| 排名 | 窗口 | 结论 |
|---:|---|---|
| 1 | South Rae / Hearne margin south of MacKay | 最适合立即做 claim-gap 跟进。窗口内 active tenure 面积约 1,359 km2，open-ground 约 61,653 km2，约 97.8% 的 bbox 面积未被本次 active tenure union 覆盖。顶级 Au till cluster 不在 active tenure polygon 内。 |
| 2 | East Slave Lac de Gras-MacKay-McCrea | 地球化学最强，最高 Au till 9,420 ppb；但部分强异常点落入 active tenure polygon。若以矿权为第一过滤器，J922072/J922079 周边 tenure-clear cells 仍是很强的 source-tracing target。 |
| 3 | Central Slave Indin-Colomac-Courageous | 作为 belt-extension portfolio 保留。成矿带和类比强，但 known project cores 多，必须避开 Colomac / Tundra / Salmita / Courageous 核心区，只找矿权边界外的 parallel sill、BIF contact 和二级剪切带。 |

本报告不能直接断言任何具体点位“法律上可 claim”。这里的 open ground 是基于 2026-05-10 访问官方服务时的 active claims/leases/permits geometry 扣减结果；staking 前必须复核最新 NWT Mineral Tenure Viewer、Registrar、land withdrawals、protected/conservation lands、Indigenous land agreements、surface-access restrictions 和 staking 规则。

## 2. GeoMine Evidence Lanes

| Evidence lane | 本阶段动作 | 证据等级 |
|---|---|---|
| AOI / CRS | 3 个 bbox，WGS84 EPSG:4326；GeoMine MCP `normalize_aoi` 用于规范 AOI。 | 中等；bbox 是筛选范围，不是 legal polygon。 |
| Canada geodata discovery | GeoMine MCP `search_canada_geodata` 给出 Canada geodata / CDoGS 方向；实际检索用 NTGS/GNWT REST。 | 中等；MCP 当前为 planner，官方 REST 为直接证据。 |
| Tenure subtraction | GNWT active claims / leases / permits，GeometryServer union/difference。 | 高；但只覆盖 active mineral tenure，不含所有地表/法律限制。 |
| Geochemistry | NTGS NT-NU Till Geochemistry Au ppb records。 | 中高；需要原始报告和 QA/QC 复核。 |
| Occurrence / drilling proxy | NTGS Mineral Showings 2021 的 gold showings、Drilled、Advanced、Producer stages。 | 中高；showing stage 是 proxy，不等于完整 drillhole database。 |
| Deposit model | Orogenic Au、BIF/greenstone-hosted Au、mafic sill-hosted Colomac-style Au、intrusion-related Au-W-Cu-Bi。 | 模型级；不能推断经济性。 |
| Disclosure boundary | NI 43-101 风险提示；不作资源/储量/经济性判断。 | 必须保留。 |

## 3. 方法说明

### 3.1 官方矿权数据

使用 GNWT Economy_LCC MapServer：

- Active Mineral Claims：layer 1
- Active Mineral Leases：layer 2
- Active Prospecting Permits：layer 3

每个重点窗口用 bbox geometry 查询 intersecting features，输出字段包括 claim/lease/permit number、status、issue date、anniversary/expiry date、area、owner、claim name、ground open date 和 land claim area。

### 3.2 Exact tenure subtraction

流程：

1. 每个窗口内把 claims、leases、permits 的 polygon geometry 合并为一个 active tenure geometry collection。
2. 调用 GNWT GeometryServer `/union`，得到 active tenure union。
3. 将窗口 bbox polygon 调用 GeometryServer `/difference`，减去 active tenure union。
4. 输出 ArcGIS JSON：
   - `data/processed/sr_open_ground_difference.json`
   - `data/processed/es_open_ground_difference.json`
   - `data/processed/cs_open_ground_difference.json`
5. 面积用本地近似等距投影脚本计算，作为筛选面积，不作为法律面积。

### 3.3 Tenure-clear 网格排序

为了把 open ground 转化为可操作的 target list，我又做了 0.10 x 0.05 度网格筛选。每个格子约 26-29 km2。规则：

- 若格子与任何 active claim / lease / prospecting permit polygon 相交，则不进入候选格子。
- 若格子 tenure-clear，则按以下证据打分：
  - 格内最高 till Au ppb。
  - 距离 p99+ Au till 异常的距离。
  - 距离 Drilled / Advanced / Producer gold showing 的距离。
  - 格内 gold showing 数量。
  - 窗口级成矿带权重。
  - Central Slave 若接近 known cores，则降低优先级。

输出：

- `data/processed/top_candidate_cells.csv`
- `data/processed/ranked_open_cells.geojson`
- `data/processed/anomaly_tenure_trace.csv`
- `data/processed/window_tenure_grid_summary.csv`

## 4. Exact Tenure Subtraction 结果

| Window | Active claims | Active leases | Active permits | Bbox area km2 | Active tenure inside bbox km2 | Open-ground km2 | Open-ground pct |
|---|---:|---:|---:|---:|---:|---:|---:|
| South Rae / Hearne margin south of MacKay | 85 | 99 | 0 | 63,011.9 | 1,359.3 | 61,652.6 | 97.8% |
| East Slave Lac de Gras-MacKay-McCrea | 189 | 375 | 0 | 48,432.1 | 4,655.0 | 43,777.2 | 90.4% |
| Central Slave Indin-Colomac-Courageous | 50 | 151 | 4 | 47,380.3 | 1,979.8 | 45,400.5 | 95.8% |

解释：

- South Rae 的 active tenure 面积占比最低，且强 Au till cluster 当前不在 active tenure polygon 内，是最符合“找未 claim 优质地块”的窗口。
- East Slave 虽然 open-ground 面积仍大，但 active tenure 与强 Au 异常交错，说明必须逐点过滤。这里不能只看 geochem。
- Central Slave open-ground 面积也大，但很多 open ground 不一定有成矿意义；必须用 Colomac/Courageous/Tundra-Salmita 模型约束。

## 5. South Rae / Hearne Margin: 第一优先窗口

### 5.1 为什么优先

South Rae / Hearne margin 的优势不是“已知大矿最多”，而是证据组合更适合找 claim 空档：

- 本窗口 active tenure inside bbox 约 1,359 km2，open-ground 约 61,653 km2。
- Tenure-clear grid 结果显示 2,088 / 2,200 个网格未与 active tenure 相交，tenure-clear cell ratio 为 94.9%。
- 主要 Au till anomaly cluster 不在 active tenure polygon 内。
- 前一阶段统计显示该窗口有 155 个官方含金矿点，其中 57 个 Drilled、3 个 Advanced。
- Top till Au cluster 位于约 -108.26 至 -108.31、62.55 至 62.60，来自 report 084080，多点异常而非孤立单点。

### 5.2 Top tenure-clear cells

| Cell | Center | Score | Max Au ppb | Au samples in cell | Nearest drilled/advanced km | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| `sr_-108.30_62.55` | -108.25, 62.575 | 68 | 322 | 1,256 | 53.28 | 第一优先。强、多点 till Au anomaly，当前 cell tenure-clear。 |
| `sr_-108.40_62.55` | -108.35, 62.575 | 62 | 212 | 144 | 48.35 | 与第一格相邻，可作为同一 source-tracing block。 |
| `sr_-108.30_62.50` | -108.25, 62.525 | 62 | 118 | 448 | 54.96 | 异常南延；用于定义 follow-up sampling line。 |
| `sr_-108.40_62.50` | -108.35, 62.525 | 56 | 70 | 246 | 50.18 | 次级南西延伸。 |
| `sr_-112.00_63.30` | -111.95, 63.325 | 41 | 82 | 71 | 15.73 | 较靠近已钻/advanced showing，适合做地质模型验证。 |

### 5.3 Top Au till samples 与矿权状态

| Sample | Report | Au ppb | lon | lat | Inside active tenure polygon | Nearest ranked tenure-clear cell |
|---|---|---:|---:|---:|---|---:|
| 1274 | 084080 | 322 | -108.27247 | 62.55127 | False | 2.88 km |
| 736 | 084080 | 310 | -108.29456 | 62.57928 | False | 2.33 km |
| 649 | 084080 | 236 | -108.26773 | 62.57901 | False | 1.01 km |
| 1256 | 084080 | 212 | -108.30615 | 62.55365 | False | 3.27 km |
| 1388 | 084080 | 210 | -108.29074 | 62.55027 | False | 3.45 km |
| 217 | 084080 | 184 | -108.26316 | 62.58692 | False | 1.49 km |

### 5.4 成矿解释

South Rae / Hearne margin 在本阶段应按 orogenic gold + shear/BIF/mafic volcanic contact 模型来处理。这里的关键不是一个孤立 Au 点，而是：

- 同一报告内多个 Au till ppb 异常聚集。
- Active tenure pressure 低。
- 区域存在 gold showings 和 drilled showings，但顶级 till cluster 与最近 drilled/advanced showing 距离较远，说明这可能是未充分验证的 geochemical target。
- 如果冰流方向把异常回溯到 mafic volcanic、BIF、gabbro、greywacke、gneiss-shear contacts，则可以形成可 claim 的 early-stage target block。

### 5.5 下一步

South Rae 应作为第一批 GIS staking review：

1. 下载 report 084080 原文和图件，确认样品介质、粒度、Au 分析方法、重复样、QA/QC、冰流方向。
2. 对 `sr_-108.30_62.55`、`sr_-108.40_62.55`、`sr_-108.30_62.50`、`sr_-108.40_62.50` 四个格子做 2-10 km up-ice corridor。
3. 叠加 bedrock geology、surficial geology、ice-flow indicators、magnetic lineaments、lake/overburden masks。
4. 当天复核 NWT Mineral Tenure Viewer 后，若仍 tenure-clear，再进入 legal claim block design。
5. 野外优先做 till infill + prospecting + drone/ground magnetic，不建议直接按 till 点下钻。

## 6. East Slave Lac de Gras-MacKay-McCrea: 地球化学最强，但先过滤矿权

### 6.1 为什么仍然高优先级

East Slave 是本次最强 Au geochemistry window：

- Top till Au：J922072 = 9,420 ppb，J922079 = 790 ppb，J922062 = 450 ppb，report 083289。
- 另有 922618 = 1,010 ppb、921135 = 801 ppb、920046 = 650 ppb 等多组异常。
- Exact difference 显示 open-ground 约 43,777 km2，bbox 的 90.4% 未被 active tenure union 覆盖。

但这里的 active claims 189、active leases 375，很多可能与 diamond tenure 或既有勘探项目相关；强异常不等于可 claim。

### 6.2 Top tenure-clear cells

| Cell | Center | Score | Max Au ppb | Au samples in cell | Nearest drilled/advanced km | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| `es_-111.60_63.90` | -111.55, 63.925 | 69 | 9,420 | 3 | 19.44 | 全报告最强地球化学 cell，J922072/J922079 source-tracing priority。 |
| `es_-111.40_64.00` | -111.35, 64.025 | 67 | 210 | 2 | 4.91 | 距已钻/advanced showing 近，地质验证价值较高。 |
| `es_-111.10_63.90` | -111.05, 63.925 | 66 | 585 | 7 | 10.71 | 强 Au cluster，可作为 ES-A corridor 的东延。 |
| `es_-111.00_63.95` | -110.95, 63.975 | 65 | 600 | 5 | 10.89 | 与上一格构成连续 source-tracing trend。 |
| `es_-109.90_64.15` | -109.85, 64.175 | 65 | 1,010 | 5 | 41.34 | 强 geochem-only target，需先找 bedrock/ice-flow support。 |

### 6.3 Top Au till samples 与矿权状态

| Sample | Report | Au ppb | lon | lat | Inside active tenure polygon | Nearest ranked tenure-clear cell |
|---|---|---:|---:|---:|---|---:|
| J922072 | 083289 | 9,420 | -111.52176 | 63.91144 | False | 2.04 km |
| 922566 | 083279 | 1,770 | -111.30367 | 64.47383 | True | 5.87 km |
| 921311 | 083372 | 1,680 | -109.87126 | 63.85189 | True | 8.20 km |
| 925042 | 083372 | 1,170 | -109.81592 | 63.66835 | False | 5.82 km |
| 922618 | 083277 | 1,010 | -109.89357 | 64.18746 | False | 2.52 km |
| 921135 | 083358 | 801 | -110.47000 | 63.86430 | False | 1.54 km |
| J922079 | 083289 | 790 | -111.56059 | 63.96784 | False | 0.95 km |

### 6.4 成矿解释

East Slave 的 Au till 异常更像“source-tracing problem”，而不是马上确定 bedrock target。判断逻辑：

- 9,420 ppb 是极强异常，但单点极值可能受 nugget effect 影响，必须看同报告内多点异常、gold grain morphology、sample weight、screen metallics/ICP method。
- J922072/J922079/J922062 同在 -111.5 至 -111.8、63.7 至 64.0 附近，支持一个可追踪的西部 anomaly train。
- 922618、921135、920046、920037 等在 -110.0 至 -110.6、63.8 至 64.2 一带构成另一组异常。
- 922566 和 921311 虽然很强，但本次 screening 显示其点位在 active tenure polygon 内，应暂时作为模型证据而不是 claim target。

### 6.5 下一步

East Slave 的工作顺序必须是：

1. 先剔除 active tenure 内的强异常，不在已占区域投入 claim 设计。
2. 对 J922072/J922079 cell 做 5-10 km up-ice source corridor，优先查是否存在 greenstone sliver、BIF、mafic volcanic contacts、magnetic breaks。
3. 对 `es_-111.60_63.90`、`es_-111.40_64.00`、`es_-111.10_63.90`、`es_-111.00_63.95` 形成 ES-A target block。
4. 对 `es_-109.90_64.15` 和 925042/922618 周边形成 ES-B target block，但需要先处理 diamond-tenure and access conflicts。
5. 下载 reports 083289、083279、083372、083277、083358，建立 report-level QA/QC 表。

## 7. Central Slave Indin-Colomac-Courageous: Belt-extension Portfolio

### 7.1 为什么不是第一优先 staking

Central Slave 的成矿带证据非常强，但用户目标是“找还没被 claim 的优质地块”。本窗口的问题是：

- 已知项目多：Colomac、Indin/Lexindin、Treasure Island、Tundra、Salmita、Courageous。
- Active tenure 虽然按面积只覆盖约 1,980 km2，但 known project cores 与历史矿山周边不能作为新空地目标。
- 本阶段 top tenure-clear cells 多为外围 geochemical cells，距离已钻/advanced showing 较远；这有机会，也有更高地质不确定性。

### 7.2 Top tenure-clear cells

| Cell | Center | Score | Max Au ppb | Au samples in cell | Nearest drilled/advanced km | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| `cs_-114.00_64.90` | -113.95, 64.925 | 54 | 225 | 4 | 62.36 | Central Slave east-fringe geochem target；需先验证 bedrock context。 |
| `cs_-114.00_64.95` | -113.95, 64.975 | 54 | 130 | 5 | 58.39 | 与上一格同一 anomaly corridor。 |
| `cs_-112.40_64.95` | -112.35, 64.975 | 46 | 30 | 313 | 46.95 | 大量低至中等 Au samples，需看是否有 BIF/greenstone support。 |
| `cs_-115.80_64.45` | -115.75, 64.475 | 32 | unknown | 0 | 2.24 | 靠近已钻/advanced evidence，但缺少 cell 内 Au till；只作 belt-edge check。 |
| `cs_-112.70_64.25` | -112.65, 64.275 | 30 | 6 | 2 | 0.97 | 靠近 known showing/drilling，geochem 弱，不是 first staking。 |

### 7.3 Top Au till samples 与矿权状态

| Sample | Report | Au ppb | lon | lat | Inside active tenure polygon | Nearest ranked tenure-clear cell |
|---|---|---:|---:|---:|---|---:|
| 921284 | 083372 | 225 | -113.97671 | 64.92000 | False | 1.38 km |
| 2130 | 083862 | 210 | -112.45787 | 65.00494 | False | 6.07 km |
| 921289 | 083372 | 130 | -113.98835 | 64.95793 | False | 2.62 km |
| 1032 | 083862 | 115 | -112.36689 | 65.00376 | False | 3.30 km |
| 302 | 083862 | 95 | -112.36636 | 65.00785 | False | 3.73 km |

### 7.4 成矿解释

Central Slave 要按 portfolio 方式处理，而不是按单点 anomaly staking：

- Colomac-style：找 mafic sill 的 parallel sill、fault offsets、fold/strain dilation zones。
- Courageous/Tundra/Salmita-style：找 greenstone belt 上 gold showings and historical drill intercepts 之间的 gaps，尤其是 BIF/mafic volcanic contacts。
- Indin/Lexindin-style：找 quartz-carbonate vein/shear systems 的二级结构和未系统钻探的 splays。

这里最有价值的不是 known cores，而是“已知矿化带外 5-20 km、同一结构走向、仍 tenure-clear”的区域。`cs_-114.00_64.90` 和 `cs_-114.00_64.95` 是地球化学外围候选；`cs_-115.80_64.45`、`cs_-115.60_64.55` 这类靠近 drill/advanced evidence 的 cells 则需要特别确认是否属于 known project land package 或边界空档。

## 8. 综合证据矩阵

| Target block | Window | Evidence | Tenure status in this pass | Model fit | Confidence | Next action |
|---|---|---|---|---|---|---|
| SR-A | South Rae | 多点 Au till 322/310/236/212/210 ppb，report 084080；top cells tenure-clear。 | 强异常点不在 active tenure polygon；open-ground pct 97.8%。 | Orogenic Au / shear-BIF-mafic contact。 | 中高 geochem；中等 geology。 | 立即下载 report 084080，做 up-ice corridor 和 legal claim check。 |
| ES-A | East Slave | J922072 9,420 ppb、J922079 790 ppb、J922062 450 ppb，report 083289；top cell score 69。 | J922072/J922079 不在 active tenure polygon；部分邻区 active tenure 密。 | Orogenic Au source tracing；possible greenstone/BIF contacts。 | 高 geochem；中等 tenure；中等 geology。 | 第一批 East Slave target，先查 ice-flow + bedrock + land status。 |
| ES-B | East Slave | 922618 1,010 ppb、921135 801 ppb、920046 650 ppb；多个 tenure-clear cells。 | 多数强样点不在 active tenure polygon，但周边 leases 多。 | Geochem-only to moderate model fit。 | 中等。 | 作为第二 East Slave block，先排除 diamond tenure and access conflicts。 |
| CS-A | Central Slave | 921284 225 ppb、921289 130 ppb；tenure-clear cells。 | 不在 active tenure polygon；距 known drill evidence 较远。 | Belt-extension / possible orogenic Au。 | 中等偏低；地球化学支持但缺少 nearby drill。 | 只作为 portfolio peripheral target。 |
| CS-B | Central Slave | 靠近 drilled/advanced evidence 的 cells，但 cell 内 Au till 弱或无。 | 部分 tenure-clear，但需避免 known cores。 | Colomac/Courageous/Indin belt analog。 | 中等 model；低 geochem。 | 做 known-core exclusion 和 claim-boundary audit。 |

## 9. 判断逻辑

我的判断顺序如下：

1. 先看矿权，不把强异常但已在 active tenure 内的点作为 claim target。
2. 再看地球化学是否为多点 cluster。South Rae SR-A 和 East Slave ES-A 都满足；单点极值只作为线索。
3. 再看成矿模型是否能解释异常。South Rae 需要 shear/BIF/mafic contact；East Slave 需要 ice-flow source tracing；Central Slave 需要 belt extension / mafic sill / BIF contact。
4. 再看 drilling proxy。靠近 Drilled / Advanced / Producer showings 的 open cells 对模型更强，但也更容易靠近 known project boundaries。
5. 最后看行动成本。South Rae 的 tenure pressure 较低，适合先做法律核验和小规模野外；East Slave geochem 更强但 tenure/access 风险更高；Central Slave 要更精细地避开已知项目。

## 10. 数据空缺与风险

- Active tenure subtraction 只扣除了 active mineral claims、leases、prospecting permits；未扣除 land withdrawals、protected areas、settlement lands、surface restrictions、environmental liabilities。
- GeometryServer difference 是按 bbox 做研究筛选，不是 cadastral survey。
- 面积为近似计算，需用正式 equal-area CRS 或 GNWT/GIS 软件复核。
- Top cells 是 0.10 x 0.05 度网格，不是可直接 claim 的边界。
- NTGS till Au 数据需按 report 逐份核验 QA/QC；Au nugget effect 可能影响单点高值。
- `inside_active_tenure_polygon = False` 只说明点位未落入本次下载的 active tenure polygon，不能说明周边可进入、可采样、可 claim。
- Pending applications、ground open date 变化、owner changes、anniversary date forfeiture 等都需要当天复核。
- 没有解析完整 drillhole database；Drilled/Advanced showing 只是 drill evidence proxy。

## 11. 下一步工作计划

### 11.1 立即 GIS 工作

1. 将 `sr_open_ground_difference.json`、`es_open_ground_difference.json`、`cs_open_ground_difference.json` 导入 QGIS/ArcGIS。
2. 将 `ranked_open_cells.geojson` 叠加在 open-ground polygons 上。
3. 对 SR-A、ES-A、ES-B 创建 2 km、5 km、10 km up-ice corridors。
4. 加入 surficial geology、ice-flow indicators、bedrock geology、magnetic/EM lineaments、lakes/wetlands、roads/airstrips/winter-road access。
5. 用 land management layers 做第二轮 subtraction。

### 11.2 报告/数据复核

优先下载并解析：

- 084080：South Rae top Au cluster。
- 083289：East Slave J922072/J922079/J922062 cluster。
- 083372：East Slave / Central Slave 多个高 Au 样品。
- 083277、083358、083862：East/Central Slave secondary clusters。

需要提取：

- Sampling medium、sample depth、fraction、method、detection limit。
- Au grain count / morphology，如有。
- QA/QC duplicate、blank、standard。
- Ice-flow map 和 transport interpretation。
- Any follow-up prospecting, trenching, drilling.

### 11.3 野外工作建议

第一批野外优先级：

1. SR-A：在 -108.26 至 -108.35、62.52 至 62.60 附近做 infill till + prospecting + ground/drone magnetics。
2. ES-A：围绕 J922072/J922079 做 up-ice boulder/till tracing，不直接按样点下钻。
3. ES-B：对 -110.95 至 -110.45、63.82 至 64.00 异常带做 land-status audit 后再进场。
4. CS-A：只在确认有 greenstone/BIF/mafic sill support 后进入第二批。

### 11.4 Claim 设计前必须完成

- 当天打开 NWT Mineral Tenure Viewer 复核。
- 用 claim rules 将 open-ground polygon 转为可 staking 的合法 claim cell/block。
- 检查 `GROUND_OPEN_DATE`、anniversary/expiry date、owner、land claim area。
- 联系 NWT registrar 或使用官方流程确认是否存在 pending or recently staked ground。
- 检查 Indigenous consultation / land access / environmental constraints。

## 12. 成果文件

本阶段生成：

- `data/processed/exact_tenure_difference_summary.csv`：exact union/difference 面积摘要。
- `data/processed/window_tenure_grid_summary.csv`：tenure-clear 网格摘要。
- `data/processed/top_candidate_cells.csv`：排序后的候选 tenure-clear cells。
- `data/processed/anomaly_tenure_trace.csv`：top Au samples 是否落入 active tenure polygon 及最近 ranked open cell。
- `data/processed/ranked_open_cells.geojson`：可在 GIS 中加载的候选 open cells。
- `data/processed/sr_open_ground_difference.json`：South Rae open-ground difference geometry。
- `data/processed/es_open_ground_difference.json`：East Slave open-ground difference geometry。
- `data/processed/cs_open_ground_difference.json`：Central Slave open-ground difference geometry。
- `phase2_summary.json`：机器可读摘要。

## 13. Source Register

- GNWT NWT Mineral Tenure Viewer: <https://www.maps.geomatics.gov.nt.ca/Html5Viewer_PROD/index.html?viewer=NWT_MTV>
- GNWT Economy_LCC MapServer: <https://www.apps.geomatics.gov.nt.ca/arcgis/rest/services/GNWT/Economy_LCC/MapServer>
- GNWT GeometryServer: <https://www.apps.geomatics.gov.nt.ca/arcgis/rest/services/Utilities/Geometry/GeometryServer>
- NTGS Mineral Showings 2021 FeatureServer: <https://services3.arcgis.com/GSr8HAQhtEt4sNnv/ArcGIS/rest/services/NWTShowings2021a/FeatureServer/0>
- NT-NU Till Geochemistry FeatureServer: <https://services3.arcgis.com/GSr8HAQhtEt4sNnv/ArcGIS/rest/services/NT_NU_TillGeochemistry/FeatureServer/0>
- CDoGS home: <https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm>

## 14. Disclosure Caveat

This is a research-screening report only. It is not legal advice, investment advice, a staking opinion, a Qualified Person opinion, a mineral resource or reserve estimate, an economic assessment, or a permitting decision. Historical showings, till geochemical anomalies, and proximity to drilled/advanced occurrences do not establish economic mineralization. All claim availability and ground access must be verified against authoritative NWT systems immediately before action.
