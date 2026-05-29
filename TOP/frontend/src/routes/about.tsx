import { createFileRoute } from "@tanstack/react-router";
import { Target, Eye, Award, Users } from "lucide-react";
import { SiteLayout } from "@/components/site/SiteLayout";
import heroImg from "@/assets/hero-steel.jpg";

export const Route = createFileRoute("/about")({
  head: () => ({
    meta: [
      { title: "關於我們｜鉅昕鋼鐵股份有限公司" },
      {
        name: "description",
        content:
          "鉅昕鋼鐵專注鋼鐵材料供應、鋼筋加工、基礎螺栓製造與鋼構工程，重視品質、效率與客戶需求。",
      },
      { property: "og:title", content: "關於鉅昕鋼鐵" },
      { property: "og:description", content: "專業、穩重、值得信賴的鋼鐵工程夥伴。" },
    ],
  }),
  component: AboutPage,
});

function AboutPage() {
  return (
    <SiteLayout>
      <PageHero
        eyebrow="About"
        title="關於鉅昕鋼鐵"
        subtitle="專業、穩重、值得信賴的鋼鐵工程夥伴"
      />

      <section className="py-16 md:py-24">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 space-y-6 text-base md:text-lg text-foreground/85 leading-loose">
          <p>
            鉅昕鋼鐵專注於鋼鐵材料供應、鋼筋加工、基礎螺栓製造與鋼構工程應用，
            致力於提供穩定、可靠且符合工程需求的鋼鐵解決方案。
          </p>
          <p>
            我們重視品質、效率與客戶需求，協助營造業、工程公司與企業客戶
            完成各類鋼鐵相關專案。從材料採購、現場加工到鋼構工程安裝，
            鉅昕鋼鐵以完整的服務鏈，協助每一個工程準時、安全完工。
          </p>
        </div>
      </section>

      <section className="py-16 md:py-20 bg-secondary/50">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            { icon: Target, title: "使命", desc: "提供穩定可靠的鋼鐵工程解決方案" },
            { icon: Eye, title: "願景", desc: "成為客戶最信賴的鋼鐵工程夥伴" },
            { icon: Award, title: "品質", desc: "符合 CNS 規範與業界最高標準" },
            { icon: Users, title: "服務", desc: "以客戶需求為核心，全心投入" },
          ].map((v) => (
            <div
              key={v.title}
              className="bg-card border border-border rounded-lg p-6 hover:shadow-steel transition"
            >
              <span className="flex h-11 w-11 items-center justify-center rounded-md bg-ember/10 text-ember mb-4">
                <v.icon size={20} />
              </span>
              <h3 className="font-display text-lg font-bold mb-2">{v.title}</h3>
              <p className="text-sm text-muted-foreground">{v.desc}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="relative h-72 md:h-96 overflow-hidden">
        <img
          src={heroImg}
          alt="鉅昕鋼鐵廠"
          width={1920}
          height={600}
          loading="lazy"
          className="h-full w-full object-cover"
        />
        <div className="absolute inset-0 bg-[var(--steel-deep)]/70 flex items-center justify-center">
          <p className="font-display text-2xl md:text-4xl text-primary-foreground text-center px-4">
            <span className="text-ember">「</span>
            鋼鐵之力，工程之信
            <span className="text-ember">」</span>
          </p>
        </div>
      </section>
    </SiteLayout>
  );
}

export function PageHero({
  eyebrow,
  title,
  subtitle,
}: {
  eyebrow: string;
  title: string;
  subtitle: string;
}) {
  return (
    <section className="bg-hero text-primary-foreground py-20 md:py-28">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <p className="text-xs font-semibold tracking-[0.25em] text-ember uppercase mb-3">
          {eyebrow}
        </p>
        <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold">{title}</h1>
        <p className="mt-4 text-base md:text-lg text-primary-foreground/70 max-w-2xl">
          {subtitle}
        </p>
      </div>
    </section>
  );
}
