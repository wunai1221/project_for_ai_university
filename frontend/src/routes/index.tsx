import { createFileRoute, Link } from "@tanstack/react-router";
import {
  ArrowRight,
  ShieldCheck,
  Factory,
  Truck,
  Bot,
  Wrench,
  Building2,
  Anchor,
  Layers,
  Leaf,
} from "lucide-react";
import { SiteLayout } from "@/components/site/SiteLayout";
import heroImg from "@/assets/hero-steel.jpg";
import rebarImg from "@/assets/service-rebar.jpg";
import boltsImg from "@/assets/service-bolts.jpg";
import structureImg from "@/assets/service-structure.jpg";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "鉅昕鋼鐵股份有限公司｜專業鋼鐵加工・基礎螺栓・鋼構工程" },
      {
        name: "description",
        content:
          "鉅昕鋼鐵專業提供鋼鐵材料供應、鋼筋加工、基礎螺栓製造與鋼構工程，內建 AI 客服，快速整理您的工程需求。",
      },
      { property: "og:title", content: "鉅昕鋼鐵股份有限公司" },
      { property: "og:description", content: "專業鋼鐵加工、基礎螺栓與鋼構工程解決方案。" },
    ],
  }),
  component: HomePage,
});

const services = [
  {
    icon: Layers,
    title: "鋼鐵材料供應",
    desc: "提供各類鋼板、型鋼、H 型鋼、角鋼、槽鋼等鋼鐵材料，穩定品質、即時交付。",
    img: rebarImg,
  },
  {
    icon: Wrench,
    title: "鋼筋加工",
    desc: "依工程圖面精準裁切、彎曲、套筒接合等鋼筋加工服務，符合 CNS 規範。",
    img: rebarImg,
  },
  {
    icon: Anchor,
    title: "基礎螺栓製造",
    desc: "客製化各類基礎螺栓、地腳螺栓、化學螺栓，適用廠房、橋梁、機電基礎。",
    img: boltsImg,
  },
  {
    icon: Building2,
    title: "鋼構工程",
    desc: "從設計、製造到現場安裝一條龍鋼構工程服務，承接廠房、商業建築與特殊結構。",
    img: structureImg,
  },
  {
    icon: Leaf,
    title: "綠能與工程應用",
    desc: "太陽能支架、風力發電基礎與其他綠能工程結構件，協助再生能源建置。",
    img: structureImg,
  },
];

const features = [
  { icon: ShieldCheck, title: "品質保證", desc: "符合 CNS 國家標準與工程規範" },
  { icon: Factory, title: "自有產線", desc: "從材料到加工全流程自主管控" },
  { icon: Truck, title: "即時交付", desc: "完整物流配送網絡，準時抵達工地" },
  { icon: Bot, title: "AI 客服", desc: "24 小時智慧客服即時服務" },
];

function HomePage() {
  return (
    <SiteLayout>
      {/* HERO */}
      <section className="relative isolate overflow-hidden bg-hero text-primary-foreground">
        <img
          src={heroImg}
          alt="鉅昕鋼鐵廠"
          width={1920}
          height={1080}
          className="absolute inset-0 h-full w-full object-cover opacity-40"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-[var(--steel-deep)]/60 via-[var(--steel-deep)]/40 to-[var(--steel-deep)]" />

        <div className="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-24 md:py-36">
          <span className="inline-flex items-center gap-2 rounded-full border border-ember/40 bg-ember/10 px-3 py-1 text-xs font-medium text-ember mb-6">
            <span className="h-1.5 w-1.5 rounded-full bg-ember animate-pulse" />
            JUSIN STEEL · 鉅昕鋼鐵
          </span>
          <h1 className="font-display text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold leading-tight max-w-4xl">
            鉅昕鋼鐵
            <span className="block text-ember mt-2">股份有限公司</span>
          </h1>
          <p className="mt-6 text-lg md:text-xl text-primary-foreground/80 max-w-2xl leading-relaxed">
            專業鋼鐵加工、基礎螺栓與鋼構工程解決方案
          </p>
          <p className="mt-3 text-sm md:text-base text-primary-foreground/60 max-w-2xl">
            穩定可靠的鋼鐵材料供應與工程服務，協助營造、工程與企業客戶完成各類專案。
          </p>

          <div className="mt-10 flex flex-wrap gap-3">
            <Link
              to="/contact"
              className="inline-flex items-center gap-2 rounded-md bg-ember px-6 py-3.5 text-sm font-semibold text-accent-foreground shadow-ember hover:brightness-110 transition"
            >
              立即 AI 客服 <ArrowRight size={16} />
            </Link>
            <Link
              to="/services"
              className="inline-flex items-center gap-2 rounded-md border border-primary-foreground/30 bg-white/5 px-6 py-3.5 text-sm font-semibold text-primary-foreground hover:bg-white/10 transition backdrop-blur"
            >
              查看產品服務
            </Link>
          </div>

          {/* feature strip */}
          <div className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-px bg-primary-foreground/10 rounded-lg overflow-hidden border border-primary-foreground/10">
            {features.map((f) => (
              <div key={f.title} className="bg-[var(--steel-deep)]/80 p-5 flex flex-col gap-2">
                <f.icon size={22} className="text-ember" />
                <p className="font-semibold text-sm">{f.title}</p>
                <p className="text-xs text-primary-foreground/60">{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ABOUT INTRO */}
      <section className="py-20 md:py-28 bg-background">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 grid md:grid-cols-2 gap-12 items-center">
          <div>
            <p className="text-xs font-semibold tracking-[0.2em] text-ember uppercase mb-3">
              About Us
            </p>
            <h2 className="text-3xl md:text-4xl font-bold mb-6">
              專業、穩重、值得信賴的
              <br />
              鋼鐵工程夥伴
            </h2>
            <p className="text-muted-foreground leading-relaxed mb-4">
              鉅昕鋼鐵專注於鋼鐵材料供應、鋼筋加工、基礎螺栓製造與鋼構工程應用，
              致力於提供穩定、可靠且符合工程需求的鋼鐵解決方案。
            </p>
            <p className="text-muted-foreground leading-relaxed mb-8">
              我們重視品質、效率與客戶需求，協助營造業、工程公司與企業客戶
              完成各類鋼鐵相關專案。
            </p>
            <Link
              to="/about"
              className="inline-flex items-center gap-2 text-sm font-semibold text-foreground border-b-2 border-ember pb-1 hover:gap-3 transition-all"
            >
              了解更多關於我們 <ArrowRight size={14} />
            </Link>
          </div>
          <div className="relative">
            <img
              src={structureImg}
              alt="鋼構工程"
              loading="lazy"
              width={800}
              height={600}
              className="rounded-lg shadow-steel w-full"
            />
            <div className="absolute -bottom-6 -left-6 bg-ember text-accent-foreground rounded-lg px-6 py-5 shadow-ember hidden md:block">
              <p className="font-display text-3xl font-bold">20+</p>
              <p className="text-xs">年產業經驗</p>
            </div>
          </div>
        </div>
      </section>

      {/* SERVICES PREVIEW */}
      <section className="py-20 md:py-28 bg-secondary/50">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-14">
            <p className="text-xs font-semibold tracking-[0.2em] text-ember uppercase mb-3">
              Services
            </p>
            <h2 className="text-3xl md:text-4xl font-bold">產品與服務項目</h2>
            <p className="text-muted-foreground mt-3 max-w-2xl mx-auto">
              五大核心業務，從原料到工程一站式服務
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {services.map((s) => (
              <article
                key={s.title}
                className="group bg-card rounded-lg overflow-hidden border border-border hover:shadow-steel hover:-translate-y-1 transition-all duration-300"
              >
                <div className="aspect-[4/3] overflow-hidden bg-muted">
                  <img
                    src={s.img}
                    alt={s.title}
                    loading="lazy"
                    width={800}
                    height={600}
                    className="h-full w-full object-cover group-hover:scale-105 transition-transform duration-500"
                  />
                </div>
                <div className="p-6">
                  <div className="flex items-center gap-3 mb-3">
                    <span className="flex h-9 w-9 items-center justify-center rounded-md bg-ember/10 text-ember">
                      <s.icon size={18} />
                    </span>
                    <h3 className="font-display text-lg font-bold">{s.title}</h3>
                  </div>
                  <p className="text-sm text-muted-foreground leading-relaxed">{s.desc}</p>
                </div>
              </article>
            ))}
          </div>

          <div className="text-center mt-12">
            <Link
              to="/services"
              className="inline-flex items-center gap-2 rounded-md bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground hover:bg-[var(--steel)] transition"
            >
              查看所有服務 <ArrowRight size={16} />
            </Link>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 bg-hero text-primary-foreground relative overflow-hidden">
        <div className="absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_30%_50%,var(--ember),transparent_50%)]" />
        <div className="relative mx-auto max-w-4xl px-4 text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            有鋼鐵工程需求？立即與我們聯絡
          </h2>
          <p className="text-primary-foreground/70 mb-8">
            點擊右下角 AI 客服，或填寫聯絡表單，我們將盡快回覆您。
          </p>
          <Link
            to="/contact"
            className="inline-flex items-center gap-2 rounded-md bg-ember px-7 py-4 text-base font-semibold text-accent-foreground shadow-ember hover:brightness-110 transition"
          >
            立即詢價 <ArrowRight size={18} />
          </Link>
        </div>
      </section>
    </SiteLayout>
  );
}
