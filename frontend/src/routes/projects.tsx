import { createFileRoute } from "@tanstack/react-router";
import { MapPin, Calendar } from "lucide-react";
import { SiteLayout } from "@/components/site/SiteLayout";
import { PageHero } from "@/routes/about";
import rebarImg from "@/assets/service-rebar.jpg";
import boltsImg from "@/assets/service-bolts.jpg";
import structureImg from "@/assets/service-structure.jpg";
import heroImg from "@/assets/hero-steel.jpg";

export const Route = createFileRoute("/projects")({
  head: () => ({
    meta: [
      { title: "工程實績｜鉅昕鋼鐵股份有限公司" },
      {
        name: "description",
        content: "鉅昕鋼鐵歷年廠房、鋼構、基礎螺栓與綠能工程實績案例。",
      },
      { property: "og:title", content: "工程實績｜鉅昕鋼鐵" },
      { property: "og:description", content: "歷年鋼構工程與應用案例展示。" },
    ],
  }),
  component: ProjectsPage,
});

const projects = [
  {
    img: structureImg,
    title: "中部科學園區廠房鋼構工程",
    category: "鋼構工程",
    location: "台中・中部科學園區",
    year: "2024",
    desc: "承接大型半導體廠房鋼構設計、製造與現場安裝，總用鋼量超過 1,200 噸。",
  },
  {
    img: boltsImg,
    title: "風力發電基礎螺栓供應案",
    category: "基礎螺栓",
    location: "彰化外海・離岸風電",
    year: "2024",
    desc: "客製化大尺寸基礎螺栓，提供離岸風電基礎結構，通過嚴格防鏽與抗拉測試。",
  },
  {
    img: rebarImg,
    title: "都市更新住宅大樓鋼筋加工",
    category: "鋼筋加工",
    location: "台北・大安區",
    year: "2023",
    desc: "為高層住宅大樓提供加工後鋼筋及套筒接合服務，縮短現場施工時間 30%。",
  },
  {
    img: heroImg,
    title: "物流中心鋼結構廠房",
    category: "鋼構工程",
    location: "桃園・觀音工業區",
    year: "2023",
    desc: "10,000 坪物流倉儲鋼構設計與施工，含夾層、屋頂桁架與設備支撐結構。",
  },
  {
    img: structureImg,
    title: "太陽能電廠支架系統",
    category: "綠能應用",
    location: "雲林・口湖",
    year: "2022",
    desc: "地面型太陽能電廠支架結構件供應與安裝，總裝置容量 12MW。",
  },
  {
    img: rebarImg,
    title: "公共工程橋梁鋼材供應",
    category: "鋼鐵材料",
    location: "高雄・市區聯絡道",
    year: "2022",
    desc: "穩定供應符合工程規範之 H 型鋼與鋼板，協助公共工程準時完工。",
  },
];

function ProjectsPage() {
  return (
    <SiteLayout>
      <PageHero
        eyebrow="Projects"
        title="工程實績"
        subtitle="歷年參與之鋼構、鋼材與工程應用案例，見證我們對品質的承諾"
      />

      <section className="py-16 md:py-24">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {projects.map((p) => (
            <article
              key={p.title}
              className="group bg-card rounded-lg overflow-hidden border border-border hover:shadow-steel hover:-translate-y-1 transition-all duration-300"
            >
              <div className="relative aspect-[4/3] overflow-hidden bg-muted">
                <img
                  src={p.img}
                  alt={p.title}
                  loading="lazy"
                  width={800}
                  height={600}
                  className="h-full w-full object-cover group-hover:scale-105 transition-transform duration-500"
                />
                <span className="absolute top-3 left-3 rounded-md bg-ember px-2.5 py-1 text-[11px] font-semibold text-accent-foreground shadow-ember">
                  {p.category}
                </span>
              </div>
              <div className="p-5">
                <h3 className="font-display text-lg font-bold mb-2 leading-snug">
                  {p.title}
                </h3>
                <p className="text-sm text-muted-foreground leading-relaxed mb-4">
                  {p.desc}
                </p>
                <div className="flex items-center gap-4 text-xs text-muted-foreground border-t border-border pt-3">
                  <span className="inline-flex items-center gap-1">
                    <MapPin size={12} className="text-ember" />
                    {p.location}
                  </span>
                  <span className="inline-flex items-center gap-1">
                    <Calendar size={12} className="text-ember" />
                    {p.year}
                  </span>
                </div>
              </div>
            </article>
          ))}
        </div>
      </section>
    </SiteLayout>
  );
}
