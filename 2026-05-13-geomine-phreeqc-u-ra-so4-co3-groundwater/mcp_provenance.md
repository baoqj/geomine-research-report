# GeoMine MCP 与数据来源记录

生成日期：2026-05-13  
主题：U-Ra-SO4-CO3 地下水 PHREEQC 科研链条与论文草稿  
研究边界：本目录中的 PHREEQC 数据为合成端元与混合场景，用于测试 GeoMine Research / PHREEQC skill 的科研链条，不是现场实测数据。

## 1. GeoMine MCP 调用状态

| 工具 | 查询 | 状态 | 解释 |
|---|---|---|---|
| `normalize_aoi` | Athabasca Basin uranium mining district and uranium tailings-affected groundwater, Saskatchewan, Canada | parsed | AOI 被保留为文本对象；未做权威地理编码、面积、距离或 CRS 转换。 |
| `search_canada_geodata` | uranium mine groundwater geochemistry radium sulfate carbonate Athabasca Basin Saskatchewan | planned / network disabled | 返回 Open Canada / Geo.ca 与 NRCan CDoGS 候选源；未下载 live catalogue records。 |
| `search_saskatchewan_mineral_data` | Athabasca Basin Saskatchewan uranium mine and tailings areas | planned / network disabled | 返回 Saskatchewan GeoAtlas 作为候选源；MCP 当前未实现 live GeoAtlas 查询。 |
| `search_cdogs_surveys` | Athabasca Basin Saskatchewan uranium | planned / network disabled | 返回 NRCan CDoGS 路线；未解析 spreadsheet。 |
| `search_canada_geodata` with `allow_network=true` | Radionuclide Releases Uranium Mines and Mills Direct Discharge | unsupported | MCP 当前版本提示 live HTTP retrieval 未实现，因此本研究采用网页核验和手工 provenance 表。 |

## 2. 已核验公开来源

| 来源 | URL | 用途 | 本次状态 |
|---|---|---|---|
| NRCan CDoGS home | https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm | 加拿大地球化学调查目录、metadata、spreadsheets、KML、WMS 路线 | 网页核验；未下载 raw spreadsheet。 |
| CDoGS Survey 210422 | https://geochem.nrcan.gc.ca/cdogs/content/svy/svy210422_e.htm | McClean Lake / Midwest area borehole groundwater 与 lake water/sediment survey metadata | 网页核验；作为真实数据采集候选。 |
| CDoGS Survey 210423 | https://geochem.nrcan.gc.ca/cdogs/content/svy/svy210423_e.htm | Key Lake area water survey, Rn/U/He exploration context | 网页核验；作为真实数据采集候选。 |
| EARMP FAQ | https://www.earmp.ca/faq | Eastern Athabasca regional monitoring media, COPCs, QA/QC laboratory context | 网页核验；作为区域环境监测背景。 |
| CNSC uranium mines and mills oversight | https://www.cnsc-ccsn.gc.ca/eng/reactors/regulating-nuclear-reactors-power-plants/regulatory-oversight-reports/uranium-mines-and-mills/ | uranium mines/mills regulatory oversight and reports | 网页核验；用于监管与环境保护背景。 |
| Open Canada CNSC datasets | https://search.open.canada.ca/opendata/?search_text=cnsc | radionuclide release datasets and direct-discharge data discovery | 网页核验；未下载 CSV。 |
| USGS PHREEQC Version 3 | https://www.usgs.gov/software/phreeqc-version-3 | PHREEQC software, downloads, documentation | 网页核验；本机使用 macOS PHREEQC 3.5.0-14000。 |
| USGS PHREEQC v3 online documentation | https://water.usgs.gov/water-resources/software/PHREEQC/documentation/phreeqc3-html/phreeqc3-1.htm | speciation, saturation index, batch reaction, transport, inverse modeling, Pitzer/SIT context | 网页核验。 |
| NWMO TR-2010-02 | https://www.nwmo.ca/-/media/Reports---Reports/1793_nwmotr-2010-02_groundwater_equilibration_and_radionuclide_solubility_calculations_r0d.ashx?rev=3bf18a8c77754e97bd38044c7adede13 | Ra sulfate/carbonate solubility control, SIT/Pitzer comparison, uncertainty framing | 网页核验；用于机制框架，不作 Athabasca 实测数据。 |

## 3. 本地计算 provenance

| 项目 | 值 |
|---|---|
| PHREEQC executable | `/Users/aibao/.local/bin/phreeqc` |
| Database | `/Users/aibao/.local/phreeqc/phreeqc-3.5.0-14000/database/llnl.dat` |
| Input file | `models/phreeqc/u_ra_so4_co3_screening.phr` |
| Output file | `models/phreeqc/u_ra_so4_co3_screening.out` |
| Selected output | `models/phreeqc/selected_output.tsv` |
| Parsed table | `data/screening_results.csv` |
| Figure script | `scripts/generate_phreeqc_u_ra_figures.py` |
| Run status | completed with return code 0 |

## 4. 关键限制

- MCP 未提供 live groundwater sample table；真实论文投稿前必须下载并清洗 CDoGS 或监管/项目数据。
- 本目录的 13 个样品是合成端元与混合场景，仅用于验证 PHREEQC skill 能否贯通数据表、输入文件、计算输出、分析图表和论文写作。
- Ra-226 活度按半衰期换算成元素 Ra 质量浓度后输入 PHREEQC；该处理适合工作流测试，真实研究应保留活度与元素质量两套字段并在方法中说明。
- `llnl.dat` 覆盖 Ra、U、barite、celestite、gypsum、uraninite、coffinite 等目标物种/相，但真实高盐水应进一步比较 `sit.dat` 或 `pitzer.dat`。
