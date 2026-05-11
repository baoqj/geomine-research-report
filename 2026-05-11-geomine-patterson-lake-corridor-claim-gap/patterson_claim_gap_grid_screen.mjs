import fs from "node:fs";
import path from "node:path";

const root = "report/2026-05-11-geomine-patterson-lake-corridor-claim-gap";
const raw = path.join(root, "data", "raw");
const out = path.join(root, "data", "processed");

const aoi = {
  lonMin: -109.9,
  lonMax: -108.45,
  latMin: 57.25,
  latMax: 58.15,
};

const stepLon = 0.1;
const stepLat = 0.05;

function readGeojson(name) {
  return JSON.parse(fs.readFileSync(path.join(raw, name), "utf8"));
}

function flattenCoords(coords, acc = []) {
  if (!Array.isArray(coords)) return acc;
  if (typeof coords[0] === "number" && typeof coords[1] === "number") {
    acc.push([coords[0], coords[1]]);
    return acc;
  }
  for (const c of coords) flattenCoords(c, acc);
  return acc;
}

function bboxOfGeom(geom) {
  const pts = flattenCoords(geom.coordinates);
  const xs = pts.map((p) => p[0]);
  const ys = pts.map((p) => p[1]);
  return {
    lonMin: Math.min(...xs),
    lonMax: Math.max(...xs),
    latMin: Math.min(...ys),
    latMax: Math.max(...ys),
  };
}

function overlaps(a, b) {
  return a.lonMin <= b.lonMax && a.lonMax >= b.lonMin && a.latMin <= b.latMax && a.latMax >= b.latMin;
}

function pointInCell(pt, cell) {
  return pt[0] >= cell.lonMin && pt[0] < cell.lonMax && pt[1] >= cell.latMin && pt[1] < cell.latMax;
}

function haversineKm(lon1, lat1, lon2, lat2) {
  const r = 6371.0088;
  const dLat = ((lat2 - lat1) * Math.PI) / 180;
  const dLon = ((lon2 - lon1) * Math.PI) / 180;
  const a =
    Math.sin(dLat / 2) ** 2 +
    Math.cos((lat1 * Math.PI) / 180) *
      Math.cos((lat2 * Math.PI) / 180) *
      Math.sin(dLon / 2) ** 2;
  return 2 * r * Math.asin(Math.sqrt(a));
}

function csvEscape(value) {
  const s = String(value ?? "");
  if (s.includes(",") || s.includes('"') || s.includes("\n")) return `"${s.replaceAll('"', '""')}"`;
  return s;
}

const active = readGeojson("sk_active_mineral_dispositions.geojson").features.map((f) => ({
  id: f.properties.DISPOSIT_1,
  owner: f.properties.OWNERS,
  bbox: bboxOfGeom(f.geometry),
}));
const lapsed = readGeojson("sk_lapsed_mineral_dispositions.geojson").features.map((f) => ({
  id: f.properties.DISPOSIT_1,
  owner: f.properties.OWNERS,
  bbox: bboxOfGeom(f.geometry),
}));
const mdi = readGeojson("sk_mineral_deposits_index.geojson").features.map((f) => ({
  id: f.properties.SMDI,
  name: f.properties.NAME,
  primary: f.properties.PRIMARYCOMMODITIES ?? "",
  assoc: f.properties.ASSOCIATEDCOMMODITIES ?? "",
  grouping: f.properties.GROUPING ?? "",
  point: f.geometry.coordinates,
}));
const drillholes = readGeojson("sk_mineral_exploration_drillholes.geojson").features.map((f) => ({
  name: f.properties.DRILLHOLE_NAME,
  project: f.properties.PROJECT_OR_PROPERTY_NAME,
  commodity: f.properties.COMMODITY_OF_INTEREST ?? "",
  point: f.geometry.coordinates,
}));
const rocks = readGeojson("sk_government_rock_samples.geojson").features.map((f) => ({
  id: f.properties.OBJECTID,
  point: f.geometry.coordinates,
}));

const anchorDeposits = [
  { name: "Triple R", lon: -109.36185180937299, lat: 57.640282305652754 },
  { name: "Arrow", lon: -109.24958566930724, lat: 57.672999949772567 },
  { name: "Spitfire", lon: -109.17136770545872, lat: 57.693853191818434 },
  { name: "JR Zone", lon: -109.52397943248276, lat: 57.829750489719665 },
  { name: "Smart Lake", lon: -109.90212775155985, lat: 57.817983209752882 },
];

const rows = [];
let cellIndex = 0;
for (let lat = aoi.latMin; lat < aoi.latMax - 1e-9; lat += stepLat) {
  for (let lon = aoi.lonMin; lon < aoi.lonMax - 1e-9; lon += stepLon) {
    const cell = {
      lonMin: Number(lon.toFixed(6)),
      lonMax: Number(Math.min(lon + stepLon, aoi.lonMax).toFixed(6)),
      latMin: Number(lat.toFixed(6)),
      latMax: Number(Math.min(lat + stepLat, aoi.latMax).toFixed(6)),
    };
    const centerLon = (cell.lonMin + cell.lonMax) / 2;
    const centerLat = (cell.latMin + cell.latMax) / 2;
    const activeHits = active.filter((f) => overlaps(f.bbox, cell));
    const lapsedHits = lapsed.filter((f) => overlaps(f.bbox, cell));
    const mdiHits = mdi.filter((f) => pointInCell(f.point, cell));
    const drillHits = drillholes.filter((f) => pointInCell(f.point, cell));
    const rockHits = rocks.filter((f) => pointInCell(f.point, cell));
    const text = mdiHits.map((m) => `${m.primary} ${m.assoc} ${m.grouping}`).join(" | ");
    const uraniumMdi = (text.match(/uranium/gi) ?? []).length;
    const goldMdi = (text.match(/gold/gi) ?? []).length;
    const reeThoriumMdi = (text.match(/rare earth|thorium|yttrium/gi) ?? []).length;
    const baseMetalMdi = (text.match(/copper|nickel|cobalt|zinc|lead|molybdenum/gi) ?? []).length;
    const distances = anchorDeposits.map((d) => ({
      name: d.name,
      km: haversineKm(centerLon, centerLat, d.lon, d.lat),
    }));
    distances.sort((a, b) => a.km - b.km);
    const nearest = distances[0];
    let score = 0;
    if (activeHits.length === 0) score += 40;
    score += Math.min(lapsedHits.length * 8, 24);
    score += Math.min(uraniumMdi * 15, 30);
    score += Math.min(goldMdi * 8, 16);
    score += Math.min(reeThoriumMdi * 5, 15);
    score += Math.min(baseMetalMdi * 4, 16);
    score += Math.min(Math.log1p(drillHits.length) * 8, 24);
    score += Math.min(rockHits.length * 2, 8);
    if (nearest.km <= 10) score += 16;
    else if (nearest.km <= 20) score += 12;
    else if (nearest.km <= 35) score += 6;
    if (activeHits.length > 0) score -= 60;

    rows.push({
      cell_id: `PLC-${String(++cellIndex).padStart(3, "0")}`,
      lon_min: cell.lonMin,
      lon_max: cell.lonMax,
      lat_min: cell.latMin,
      lat_max: cell.latMax,
      center_lon: Number(centerLon.toFixed(6)),
      center_lat: Number(centerLat.toFixed(6)),
      active_bbox_intersections: activeHits.length,
      lapsed_bbox_intersections: lapsedHits.length,
      lapsed_ids: lapsedHits.map((f) => f.id).join(";"),
      lapsed_owners: [...new Set(lapsedHits.map((f) => f.owner))].join(";"),
      mdi_count: mdiHits.length,
      uranium_mdi_count: uraniumMdi,
      gold_mdi_count: goldMdi,
      ree_thorium_mdi_count: reeThoriumMdi,
      base_metal_mdi_count: baseMetalMdi,
      mdi_names: mdiHits.map((m) => `${m.id}:${m.name}`).join(";"),
      drillhole_count: drillHits.length,
      rock_sample_count: rockHits.length,
      nearest_anchor: nearest.name,
      nearest_anchor_km: Number(nearest.km.toFixed(1)),
      score: Number(score.toFixed(2)),
      status_note:
        activeHits.length === 0
          ? "No active disposition bbox intersection in this screening grid; verify in MARS before staking."
          : "Intersects active disposition bbox; only boundary slivers may be open, if any.",
    });
  }
}

rows.sort((a, b) => b.score - a.score);

fs.mkdirSync(out, { recursive: true });
const headers = Object.keys(rows[0]);
const csv = [headers.join(","), ...rows.map((r) => headers.map((h) => csvEscape(r[h])).join(","))].join("\n");
fs.writeFileSync(path.join(out, "patterson_lake_corridor_claim_gap_grid.csv"), csv);

const candidateFeatures = rows.slice(0, 80).map((r) => ({
  type: "Feature",
  properties: r,
  geometry: {
    type: "Polygon",
    coordinates: [
      [
        [r.lon_min, r.lat_min],
        [r.lon_max, r.lat_min],
        [r.lon_max, r.lat_max],
        [r.lon_min, r.lat_max],
        [r.lon_min, r.lat_min],
      ],
    ],
  },
}));
fs.writeFileSync(
  path.join(out, "patterson_lake_corridor_top_grid_cells.geojson"),
  JSON.stringify({ type: "FeatureCollection", features: candidateFeatures }, null, 2),
);

const summary = {
  generated_at: new Date().toISOString(),
  aoi,
  grid: { stepLon, stepLat, cell_count: rows.length },
  source_counts: {
    active_dispositions: active.length,
    lapsed_dispositions: lapsed.length,
    mineral_deposits_index: mdi.length,
    drillholes: drillholes.length,
    government_rock_samples: rocks.length,
  },
  method_limitations: [
    "Active and lapsed claim intersections use feature bounding boxes, not exact polygon overlay; this is conservative for identifying fully open cells.",
    "A cell with zero active bbox intersections is likely open at this screen scale, but MARS parcel-level verification is mandatory.",
    "The lapsed layer downloaded from the public GeoAtlas endpoint does not expose lapse date; recent expiry within one to two years must be confirmed in MARS or by ministry searchbook.",
    "The score is an exploration-screening index, not a mineral resource estimate, target ranking by a Qualified Person, or investment recommendation.",
  ],
  top_open_cells: rows.filter((r) => r.active_bbox_intersections === 0).slice(0, 20),
};
fs.writeFileSync(path.join(out, "patterson_lake_corridor_screen_summary.json"), JSON.stringify(summary, null, 2));

console.log(JSON.stringify(summary, null, 2));
