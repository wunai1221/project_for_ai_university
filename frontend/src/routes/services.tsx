import { createFileRoute, Link } from "@tanstack/react-router";
import { ArrowRight, Check, Wrench, Building2, Layers, Sun, Utensils, Sprout } from "lucide-react";
import { SiteLayout } from "@/components/site/SiteLayout";
import { PageHero } from "@/routes/about";
import rebarImg from "@/assets/service-rebar.jpg";
import structureImg from "@/assets/service-structure.jpg";
import materialsVideo from "../../public/videos/materials.mp4.asset.json";
import rebarVideo from "../../public/videos/rebar.mp4.asset.json";
import boltsVideo from "../../public/videos/bolts.mp4.asset.json";
import structureVideo from "../../public/videos/structure.mp4.asset.json";

export const Route = createFileRoute("/services")({
  head: () => ({
    meta: [
      { title: "產品服務｜鉅昕鋼鐵股份有限公司" },
      {
        name: "description",
        content:
          "鉅昕鋼鐵提供鋼鐵材料供應、鋼筋加工、基礎螺栓製造、鋼構工程與綠能工程應用服務。",
      },
      { property: "og:title", content: "產品與服務｜鉅昕鋼鐵" },
      {
        property: "og:description",
        content: "鋼鐵材料、鋼筋加工、基礎螺栓、鋼構工程一站式服務。",
      },
    ],
  }),
  component: ServicesPage,
});

const services = [
  {
    id: "rebar",
    icon: Wrench,
    title: "鋼筋加工",
    desc: "精密鋼筋加工服務，依工程圖面進行裁切、彎曲、續接，確保現場施工效率。",
    img: rebarImg,
    video: rebarVideo.url,
    items: ["精準裁切彎曲", "螺紋套筒續接", "依圖面客製", "符合 CNS 規範"],
  },
  {
    id: "structure",
    icon: Building2,
    title: "鋼構工程",
    desc: "鋼構設計、製造、現場安裝一條龍服務，廠房、商業建築與特殊結構皆可承接。",
    img: structureImg,
    video: structureVideo.url,
    items: ["鋼構設計製造", "現場吊裝施工", "廠房 / 商辦結構", "結構補強改建"],
  },
  {
    id: "materials",
    icon: Layers,
    title: "鋼材買賣及加工",
    desc: "提供完整鋼材買賣與加工服務，依工程需求快速調配，從規格諮詢到送達現場全程協助。",
    img: rebarImg,
    video: materialsVideo.url,
    items: ["H 型鋼 / I 型鋼", "鋼板 / 鋼捲", "角鋼 / 槽鋼", "客製裁切加工"],
  },
  {
    id: "solar",
    icon: Sun,
    title: "太陽能統包",
    desc: "從設計規劃、申請、施工到送電完成一條龍統包服務，協助業主完整建置太陽能系統。",
    img: structureImg,
    video: "/videos/green.mp4",
    items: ["系統設計規劃", "申請與併聯送電", "施工安裝統包", "後續維運服務"],
  },
  {
    id: "restaurant",
    icon: Utensils,
    title: "餐廳推廣",
    desc: "結合在地餐飲品牌行銷與通路推廣，協助餐廳擴展知名度與營收。",
    img: structureImg,
    video: boltsVideo.url,
    items: ["品牌行銷策略", "活動企劃推廣", "通路合作媒合", "社群曝光協助"],
  },
  {
    id: "agriculture",
    icon: Sprout,
    title: "農產品推銷",
    desc: "協助在地優質農產品行銷推廣，建立穩定銷售通路與品牌價值。",
    img: rebarImg,
    video: structureVideo.url,
    items: ["產地直送推廣", "通路開發合作", "品牌包裝建議", "活動展售協助"],
  },
];

function ServicesPage() {
  return (
    <SiteLayout>
      <PageHero
        eyebrow="Services"
        title="產品與服務"
        subtitle="鋼鐵材料、加工、螺栓、鋼構工程，五大核心業務一站式服務"
      />

      <section className="py-16 md:py-24">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 space-y-16">
          {services.map((s, i) => (
            <article
              key={s.title}
              id={s.id}
              className={`scroll-mt-24 grid md:grid-cols-2 gap-10 items-center ${
                i % 2 === 1 ? "md:[&>*:first-child]:order-2" : ""
              }`}
            >
              <div className="relative">
                <video
                  src={s.video}
                  poster={s.img}
                  autoPlay
                  muted
                  loop
                  playsInline
                  preload="metadata"
                  className="rounded-lg shadow-steel w-full aspect-[4/3] object-cover bg-muted"
                />
                <span className="absolute top-4 left-4 flex h-11 w-11 items-center justify-center rounded-md bg-ember text-accent-foreground shadow-ember">
                  <s.icon size={20} />
                </span>
              </div>
              <div>
                <p className="text-xs font-semibold tracking-[0.2em] text-ember uppercase mb-2">
                  0{i + 1} / 服務項目
                </p>
                <h2 className="text-2xl md:text-3xl font-bold mb-4">{s.title}</h2>
                <p className="text-muted-foreground leading-relaxed mb-6">{s.desc}</p>
                <ul className="grid grid-cols-2 gap-3 mb-6">
                  {s.items.map((it) => (
                    <li key={it} className="flex items-center gap-2 text-sm">
                      <span className="flex h-5 w-5 items-center justify-center rounded-full bg-ember/15 text-ember">
                        <Check size={12} strokeWidth={3} />
                      </span>
                      {it}
                    </li>
                  ))}
                </ul>
                <Link
                  to="/contact"
                  className="inline-flex items-center gap-2 text-sm font-semibold text-foreground border-b-2 border-ember pb-1 hover:gap-3 transition-all"
                >
                  詢問此項服務 <ArrowRight size={14} />
                </Link>
              </div>
            </article>
          ))}
        </div>
      </section>
    </SiteLayout>
  );
}
