import { createFileRoute, Link } from "@tanstack/react-router";
import { ArrowRight, Check, Wrench, Anchor, Building2, Layers, Leaf } from "lucide-react";
import { SiteLayout } from "@/components/site/SiteLayout";
import { PageHero } from "@/routes/about";
import rebarImg from "@/assets/service-rebar.jpg";
import boltsImg from "@/assets/service-bolts.jpg";
import structureImg from "@/assets/service-structure.jpg";

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
    icon: Layers,
    title: "鋼鐵材料供應",
    desc: "提供完整鋼鐵材料品項，依工程需求快速調配，從規格諮詢到送達現場全程協助。",
    img: rebarImg,
    items: ["H 型鋼 / I 型鋼", "鋼板 / 鋼捲", "角鋼 / 槽鋼", "圓鋼 / 方管"],
  },
  {
    icon: Wrench,
    title: "鋼筋加工",
    desc: "精密鋼筋加工服務，依工程圖面進行裁切、彎曲、續接，確保現場施工效率。",
    img: rebarImg,
    items: ["精準裁切彎曲", "螺紋套筒續接", "依圖面客製", "符合 CNS 規範"],
  },
  {
    icon: Anchor,
    title: "基礎螺栓製造",
    desc: "專業基礎螺栓、地腳螺栓、化學螺栓製造，依結構需求客製尺寸與材質。",
    img: boltsImg,
    items: ["地腳 / 基礎螺栓", "化學錨栓", "客製尺寸規格", "防鏽處理"],
  },
  {
    icon: Building2,
    title: "鋼構工程",
    desc: "鋼構設計、製造、現場安裝一條龍服務，廠房、商業建築與特殊結構皆可承接。",
    img: structureImg,
    items: ["鋼構設計製造", "現場吊裝施工", "廠房 / 商辦結構", "結構補強改建"],
  },
  {
    icon: Leaf,
    title: "綠能與工程應用",
    desc: "投入再生能源工程結構件，包含太陽能支架、風電基礎與相關綠能工程件。",
    img: structureImg,
    items: ["太陽能支架", "風電基礎件", "綠建築鋼構", "綠能週邊工程"],
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
              className={`grid md:grid-cols-2 gap-10 items-center ${
                i % 2 === 1 ? "md:[&>*:first-child]:order-2" : ""
              }`}
            >
              <div className="relative">
                <img
                  src={s.img}
                  alt={s.title}
                  loading="lazy"
                  width={800}
                  height={600}
                  className="rounded-lg shadow-steel w-full aspect-[4/3] object-cover"
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
