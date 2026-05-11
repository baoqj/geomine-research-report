# South Rae / Hearne margin south of MacKay 结论解释

本说明解释二阶段报告中这句话的含义：

> South Rae / Hearne margin south of MacKay 最适合立即做 claim-gap 跟进。窗口内 active tenure 面积约 1,359 km2，open-ground 约 61,653 km2，约 97.8% 的 bbox 面积未被本次 active tenure union 覆盖。顶级 Au till cluster 不在 active tenure polygon 内。

## 1. 这句话不是在说什么

这句话不是说：

- 该区域已经确认可以合法 staking。
- 该区域一定有经济金矿。
- 61,653 km2 全部都值得 claim。
- 顶级 Au till 点下面就是矿体。

它真正表达的是：在本次三大重点窗口中，South Rae 同时满足“矿权压力低、Au till 异常成簇、存在区域金矿证据、可继续做法律核验和野外追踪”的条件，因此最适合作为下一步 claim-gap GIS 和报告复核的第一对象。

## 2. 计算口径

### 2.1 AOI

South Rae / Hearne margin south of MacKay 使用的筛选 bbox 为：

`-113.0, 61.3, -108.0, 63.5`，WGS84 / EPSG:4326。

这是一个区域筛选框，不是法律 claim boundary。

### 2.2 Active tenure

本次从 GNWT Economy_LCC MapServer 下载并扣减了三类 active mineral tenure：

- Active Mineral Claims：85 个
- Active Mineral Leases：99 个
- Active Prospecting Permits：0 个

然后用 GNWT GeometryServer 做：

1. active claims + leases + permits 的 polygon union。
2. South Rae bbox polygon minus active tenure union。
3. 得到 open-ground difference geometry。

### 2.3 面积结果

| 指标 | 数值 |
|---|---:|
| South Rae bbox 近似面积 | 63,011.9 km2 |
| bbox 内 active tenure 面积 | 1,359.3 km2 |
| active tenure 扣减后 open-ground 面积 | 61,652.6 km2 |
| open-ground 面积比例 | 97.8% |
| open-ground polygon ring parts | 40 |

解释：这个 97.8% 说明在这个大筛选框内，当前 active mineral tenure 覆盖面积相对很低。它不等于 97.8% 都可以 claim，因为还没有扣除 land withdrawals、protected areas、Indigenous land agreement restrictions、surface access constraints、pending applications 等非 mineral-tenure 限制。

## 3. 为什么说它适合 claim-gap 跟进

我使用的是“先矿权，后地质”的判断顺序：

1. 先看 active tenure 是否已经把目标区占满。
2. 再看 open ground 中是否有成簇 Au till 异常。
3. 再看附近是否有官方 gold showings / drilled showings / advanced showings。
4. 再用成矿模型解释异常是否合理。
5. 最后决定是否值得进入 claim-gap legal review。

South Rae 在这几个层面都比其它窗口更平衡。

## 4. 关键证据

### 4.1 矿权证据

Exact tenure subtraction 结果：

| Window | Active tenure inside bbox | Open ground | Open-ground pct |
|---|---:|---:|---:|
| South Rae | 1,359.3 km2 | 61,652.6 km2 | 97.8% |
| East Slave | 4,655.0 km2 | 43,777.2 km2 | 90.4% |
| Central Slave | 1,979.8 km2 | 45,400.5 km2 | 95.8% |

South Rae 的 active tenure 面积最低、open-ground 占比最高，所以更适合先做 claim-gap 跟进。

### 4.2 网格证据

为了避免只看大面积，我把 South Rae bbox 切成 0.10 x 0.05 degree 网格：

- 总网格数：2,200
- 与 active tenure 不相交的 tenure-clear 网格：2,088
- tenure-clear cell ratio：94.9%
- 近似 tenure-clear grid area：59,972.4 km2

这说明 South Rae 不只是整体面积上 open，细分网格后也有大量未与 active tenure 相交的格子。

### 4.3 顶级 Au till cluster

South Rae 的顶级 Au till 异常集中在 report 084080，坐标约在 `-108.26` 到 `-108.31`、`62.55` 到 `62.60` 附近。关键样品如下：

| Sample | Report | Au ppb | lon | lat | Inside active tenure polygon |
|---|---|---:|---:|---:|---|
| 1274 | 084080 | 322 | -108.27247 | 62.55127 | False |
| 736 | 084080 | 310 | -108.29456 | 62.57928 | False |
| 649 | 084080 | 236 | -108.26773 | 62.57901 | False |
| 1256 | 084080 | 212 | -108.30615 | 62.55365 | False |
| 1388 | 084080 | 210 | -108.29074 | 62.55027 | False |
| 217 | 084080 | 184 | -108.26316 | 62.58692 | False |
| 619 | 084080 | 175 | -108.27771 | 62.58035 | False |

这里最重要的不是单个 322 ppb，而是多个样品在同一小区域内组成 cluster，并且这些顶级点在本次 active tenure polygon 检查中均为 `False`。

### 4.4 候选 open cells

排序最高的 tenure-clear cells：

| Cell | Center | Score | Max Au ppb | Au sample count | Nearest high-Au sample km | Nearest drilled/advanced km |
|---|---:|---:|---:|---:|---:|---:|
| `sr_-108.30_62.55` | -108.25, 62.575 | 68 | 322 | 1,256 | 1.01 | 53.28 |
| `sr_-108.40_62.55` | -108.35, 62.575 | 62 | 212 | 144 | 2.88 | 48.35 |
| `sr_-108.30_62.50` | -108.25, 62.525 | 62 | 118 | 448 | 3.12 | 54.96 |
| `sr_-108.40_62.50` | -108.35, 62.525 | 56 | 70 | 246 | 3.52 | 50.18 |
| `sr_-112.00_63.30` | -111.95, 63.325 | 41 | 82 | 71 | 43.14 | 15.73 |

解释：

- 前四个格子构成一个紧凑的 SR-A target block。
- 它们分数高，主要来自 Au till cluster 和 tenure-clear 状态。
- 最近 Drilled / Advanced showing 距离较远，这一方面说明不是已经充分钻探验证的 known project core，另一方面也说明 bedrock source 仍需验证。

## 5. 地质和成矿解释

South Rae / Hearne margin 的目标逻辑是 early-stage orogenic gold source tracing。

### 5.1 为什么 Au till 有意义

till Au 异常是冰川搬运介质中的金异常，通常不应直接解释为样点正下方有矿体。正确逻辑是：

1. Au till cluster 表明冰川搬运路径上游可能存在 bedrock gold source。
2. 多个样品同一区域异常，比单个高值更可靠。
3. 需要结合 ice-flow direction，把异常向 up-ice 方向追踪。
4. 再看 up-ice 区域是否存在剪切带、BIF、mafic volcanic、quartz-carbonate vein、sulphide alteration 等成矿条件。

### 5.2 可能的金矿模型

当前最合理的模型是：

- Orogenic Au in shear zones。
- BIF / iron formation associated gold。
- Mafic volcanic / gneiss / greywacke contacts 上的 quartz-carbonate vein gold。

预计伴生和 pathfinder：

- Au + As/Sb/Ag/Pb，局部 Bi/W。
- pyrite、pyrrhotite、arsenopyrite。
- quartz-carbonate veins、shear fabric、carbonate-sericite-chlorite alteration。

### 5.3 为什么不是直接钻探

因为 till sample 是搬运介质，第一步应该是：

1. 查 report 084080 原始采样和 QA/QC。
2. 查冰流方向。
3. 做 infill till sampling。
4. 做 prospecting、boulder tracing、drone/ground magnetics。
5. 找到 bedrock structure/source 后再考虑 scout drilling。

## 6. 为什么优先级高于 East Slave 和 Central Slave

### 6.1 相比 East Slave

East Slave 的 geochemistry 更强，最高 Au till 9,420 ppb，但它的问题是：

- active claims 189、active leases 375，矿权压力更高。
- 部分强异常点落入 active tenure polygon，例如 922566、921311。
- 需要先把 diamond/mineral tenure 和 access conflicts 过滤掉。

所以 East Slave 是“高回报但矿权过滤更复杂”的窗口。

### 6.2 相比 Central Slave

Central Slave 的成矿带证据很强，但：

- Colomac、Tundra、Salmita、Courageous、Indin/Lexindin 等 known project cores 多。
- 很多好地质位置很可能已被项目边界、历史矿权或 leases 控制。
- 它更适合做 belt-extension portfolio，而不是第一批大面积找空地。

所以 South Rae 的优势是：地球化学证据足够强，同时矿权压力明显低。

## 7. 结论

South Rae / Hearne margin south of MacKay 被列为第一优先，不是因为它已经证明有经济矿床，而是因为它最符合“找暂时未被 claim 的优质地块”的筛选逻辑：

1. active mineral tenure 覆盖低，open-ground 比例高。
2. 顶级 Au till cluster 在本次检查中不在 active tenure polygon 内。
3. 异常不是孤立点，而是 report 084080 内多个样品成簇。
4. 区域存在官方 gold showings 和 drilled showings，说明不是完全无矿化背景。
5. 距离已知 drilled/advanced core 较远，可能代表未充分跟进的 geochemical source area。

最稳妥的下一步是把 SR-A target block 作为第一批工作对象：

- `sr_-108.30_62.55`
- `sr_-108.40_62.55`
- `sr_-108.30_62.50`
- `sr_-108.40_62.50`

下一步不应直接 staking 或钻探，而应先做：

1. report 084080 原文复核。
2. ice-flow/up-ice corridor 解释。
3. land withdrawal / protected / Indigenous land / surface-access 扣减。
4. 当天 NWT Mineral Tenure Viewer 和 Registrar 复核。
5. infill till + prospecting + magnetics。

只有完成这些步骤后，才能把“claim-gap candidate”升级为“可提交 claim 的具体地块”。
