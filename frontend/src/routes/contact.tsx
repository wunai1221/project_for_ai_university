import { createFileRoute } from "@tanstack/react-router";
import { Phone, Mail, MapPin, Bot, MessageCircle } from "lucide-react";
import { SiteLayout } from "@/components/site/SiteLayout";
import { PageHero } from "@/routes/about";

export const Route = createFileRoute("/contact")({
  head: () => ({
    meta: [
      { title: "聯絡我們｜鉅昕鋼鐵股份有限公司" },
      {
        name: "description",
        content: "聯絡鉅昕鋼鐵，使用 AI 客服立即整理您的鋼鐵工程詢價需求。",
      },
      { property: "og:title", content: "聯絡鉅昕鋼鐵" },
      { property: "og:description", content: "使用右下角 AI 客服立即對話。" },
    ],
  }),
  component: ContactPage,
});

function ContactPage() {
  return (
    <SiteLayout>
      <PageHero
        eyebrow="Contact"
        title="聯絡我們"
        subtitle="請使用右下角 AI 客服立即對話，或透過下列方式聯繫我們"
      />

      <section className="py-16 md:py-24">
        <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8 grid md:grid-cols-2 gap-8">
          <div className="bg-hero text-primary-foreground rounded-lg p-7 shadow-steel">
            <h3 className="font-display text-xl font-bold mb-5">公司資訊</h3>
            <ul className="space-y-4 text-sm">
              <li className="flex items-start gap-3">
                <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-md bg-ember text-accent-foreground">
                  <Phone size={16} />
                </span>
                <div>
                  <p className="text-primary-foreground/60 text-xs mb-0.5">電話</p>
                  <p>請填入公司電話</p>
                </div>
              </li>
              <li className="flex items-start gap-3">
                <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-md bg-ember text-accent-foreground">
                  <Mail size={16} />
                </span>
                <div>
                  <p className="text-primary-foreground/60 text-xs mb-0.5">Email</p>
                  <p>請填入公司信箱</p>
                </div>
              </li>
              <li className="flex items-start gap-3">
                <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-md bg-ember text-accent-foreground">
                  <MapPin size={16} />
                </span>
                <div>
                  <p className="text-primary-foreground/60 text-xs mb-0.5">地址</p>
                  <p>請填入公司地址</p>
                </div>
              </li>
            </ul>
          </div>

          <div className="bg-card border border-border rounded-lg p-7 shadow-steel flex flex-col">
            <div className="flex items-center gap-3 mb-4">
              <span className="flex h-11 w-11 items-center justify-center rounded-md bg-ember/10 text-ember">
                <Bot size={22} />
              </span>
              <h3 className="font-display text-xl font-bold">AI 客服</h3>
            </div>
            <p className="text-sm text-muted-foreground leading-relaxed mb-5">
              點擊右下角 AI 客服按鈕，以對話方式快速整理您的詢價資料，
              24 小時即時服務，無需填寫表單。
            </p>
            <div className="mt-auto flex items-center gap-2 text-sm text-ember font-semibold">
              <MessageCircle size={16} />
              <span>右下角即可開啟對話</span>
            </div>
          </div>
        </div>
      </section>
    </SiteLayout>
  );
}
