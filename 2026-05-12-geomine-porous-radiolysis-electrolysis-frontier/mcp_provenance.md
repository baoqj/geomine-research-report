# GeoMine MCP Provenance

日期：2026-05-12

## 使用的 GeoMine MCP 工具

### `normalize_aoi`

输入对象为概念 AOI：

```text
water radiolysis in porous media relevant to Canadian Shield crystalline rock fractures, clay/bentonite engineered barriers, oxide/semiconductor nanopores, and nuclear-waste repository groundwater systems
```

工具输出结论：

- 该对象不是传统 GIS AOI，没有坐标、polygon、bbox、NTS sheet 或省区边界。
- 研究应被视为概念性、机理性和跨学科 AOI。
- 若未来需要计算面积、距离、地下水流域或矿权叠加，必须补充权威几何边界和 CRS。

### `summarize_dataset_provenance`

记录了两个本地材料来源：

| dataset_id | 路径 | 用途 | 限制 |
|---|---|---|---|
| `local_pdf_scibot_porous_media_radiolysis` | `plugins/report/Sci-Bot_ 关于多孔介质中的辐射分解.pdf` | 提供多孔介质水辐解、G 值、电场影响和参考文献线索 | 本地综合 PDF，不是原始数据集；关键数值需回到原始论文核对。 |
| `openminer_prior_radiolysis_reports` | `report/2026-05-10-radiolysis-porous-media-review/` 等 | 提供前序中文推导、能量账和 Revell/Athabasca 地球化学背景 | 二级研究记录，不替代同行评议文献和工程安全评估。 |

## 本次报告的复核边界

- 本报告中的 G 值比较统一标注了 `umol J^-1` 与 `molecule / 100 eV` 的换算关系。
- 表观 G 值增强与系统总能效分开处理，避免把吸收辐射能误判为免费能量。
- 产业化部分只建立成本模型和 go/no-go 指标，不作投资建议。
- 核废料处置、放射源和辐射辅助电解槽均需要持证核安全、化工安全、电化学工程和环境合规团队复核。

