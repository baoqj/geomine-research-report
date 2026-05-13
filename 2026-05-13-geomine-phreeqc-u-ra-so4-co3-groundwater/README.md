# GeoMine PHREEQC U-Ra-SO4-CO3 Groundwater Workflow

Topic: 铀矿区地下水中 U-Ra-SO4-CO3 体系的地球化学控制机制

Files:

- `u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.md` - 中文学术论文草稿，包含数据采集、PHREEQC 方法、结果、二维图表和讨论。
- `u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.pdf` - 使用 GeoMine PDF math export skill 和 headless Chrome 导出的 PDF。
- `u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.html` - PDF 中间 HTML，SVG 图表已内联。
- `u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.normalized.md` - 导出器规范化后的 Markdown。
- `u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.print.css` - PDF 打印 CSS。
- `mcp_provenance.md` - GeoMine MCP 调用状态、公开数据源和本地 PHREEQC 运行 provenance。
- `datasets_evidence.json` - 数据源、候选数据集和本地 synthetic workflow data registry。
- `workflow_manifest.json` - 本地生成脚本、PHREEQC 状态、图表和限制摘要。
- `data/synthetic_groundwater_endmembers.csv` - 合成端元与混合场景输入表；不是实测数据。
- `data/screening_results.csv` - 合成输入 + PHREEQC selected output + mechanism scores。
- `models/phreeqc/u_ra_so4_co3_screening.phr` - PHREEQC 输入文件。
- `models/phreeqc/u_ra_so4_co3_screening.out` - PHREEQC 输出文件。
- `models/phreeqc/selected_output.tsv` - PHREEQC selected output。
- `scripts/generate_phreeqc_u_ra_figures.py` - 生成输入、运行 PHREEQC、解析输出和生成 SVG 图表的脚本。
- `figures/*.svg` - 二维相关性、散点图、机制分数和饱和指数热图。

Method boundary:

- GeoMine MCP discovery was used for AOI/source planning and provenance; live groundwater chemistry retrieval was not available through MCP in this run.
- The PHREEQC run completed locally with `/Users/aibao/.local/bin/phreeqc` and `llnl.dat`.
- The 13 water samples are synthetic end-members and mixtures for skill validation. They are not Athabasca field observations.
- Visualization is limited to flat data-analysis figures; GeoMine Visualization Studio 3D was intentionally not used for this paper deliverable.

Re-run:

```bash
python3 report/2026-05-13-geomine-phreeqc-u-ra-so4-co3-groundwater/scripts/generate_phreeqc_u_ra_figures.py
```
