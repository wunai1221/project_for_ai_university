import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";
import { Phone, Mail, MapPin, Send, Loader2, CheckCircle2, Bot } from "lucide-react";
import { z } from "zod";
import { SiteLayout } from "@/components/site/SiteLayout";
import { PageHero } from "@/routes/about";
import { supabase } from "@/integrations/supabase/client";

export const Route = createFileRoute("/contact")({
  head: () => ({
    meta: [
      { title: "聯絡我們｜鉅昕鋼鐵股份有限公司" },
      {
        name: "description",
        content: "聯絡鉅昕鋼鐵，留下您的鋼鐵工程詢價需求，我們將盡快回覆。",
      },
      { property: "og:title", content: "聯絡鉅昕鋼鐵" },
      { property: "og:description", content: "立即填寫詢價表單或使用 AI 客服。" },
    ],
  }),
  component: ContactPage,
});

const schema = z.object({
  name: z.string().trim().min(1, "請輸入姓名").max(80),
  company: z.string().trim().max(120).optional().or(z.literal("")),
  phone: z.string().trim().min(6, "請輸入有效電話").max(30),
  email: z.string().trim().email("請輸入有效 Email").max(120),
  message: z.string().trim().min(5, "請輸入需求內容").max(2000),
});

function ContactPage() {
  const [form, setForm] = useState({
    name: "",
    company: "",
    phone: "",
    email: "",
    message: "",
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [submitting, setSubmitting] = useState(false);
  const [done, setDone] = useState(false);

  function update<K extends keyof typeof form>(k: K, v: string) {
    setForm((f) => ({ ...f, [k]: v }));
  }

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setErrors({});
    const parsed = schema.safeParse(form);
    if (!parsed.success) {
      const errs: Record<string, string> = {};
      for (const issue of parsed.error.issues) {
        const k = issue.path[0] as string;
        if (!errs[k]) errs[k] = issue.message;
      }
      setErrors(errs);
      return;
    }
    setSubmitting(true);
    const { error } = await supabase.from("inquiries").insert({
      name: parsed.data.name,
      company: parsed.data.company || null,
      phone: parsed.data.phone,
      email: parsed.data.email,
      message: parsed.data.message,
      source: "contact",
    });
    setSubmitting(false);
    if (error) {
      setErrors({ form: "送出失敗，請稍後再試或來電聯絡。" });
      return;
    }
    setDone(true);
    setForm({ name: "", company: "", phone: "", email: "", message: "" });
  }

  return (
    <SiteLayout>
      <PageHero
        eyebrow="Contact"
        title="聯絡我們"
        subtitle="留下您的需求，或使用右下角 AI 客服立即對話"
      />

      <section className="py-16 md:py-24">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 grid lg:grid-cols-5 gap-10">
          {/* info */}
          <aside className="lg:col-span-2 space-y-6">
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

            <div className="bg-card border border-border rounded-lg p-6">
              <div className="flex items-center gap-3 mb-3">
                <span className="flex h-10 w-10 items-center justify-center rounded-md bg-ember/10 text-ember">
                  <Bot size={20} />
                </span>
                <h3 className="font-display font-bold">AI 客服</h3>
              </div>
              <p className="text-sm text-muted-foreground leading-relaxed">
                點擊右下角 AI 客服按鈕，以對話方式快速整理您的詢價資料，
                24 小時即時服務。
              </p>
            </div>
          </aside>

          {/* form */}
          <div className="lg:col-span-3">
            {done ? (
              <div className="bg-card border border-border rounded-lg p-10 text-center shadow-steel">
                <CheckCircle2 size={56} className="mx-auto text-ember mb-4" />
                <h3 className="font-display text-2xl font-bold mb-2">已收到您的詢價</h3>
                <p className="text-muted-foreground">
                  感謝您聯絡鉅昕鋼鐵，我們將於 1 個工作日內由專員與您聯繫。
                </p>
                <button
                  onClick={() => setDone(false)}
                  className="mt-6 text-sm font-semibold text-ember hover:underline"
                >
                  送出另一份詢價
                </button>
              </div>
            ) : (
              <form
                onSubmit={onSubmit}
                className="bg-card border border-border rounded-lg p-6 md:p-8 shadow-steel space-y-5"
              >
                <h3 className="font-display text-xl font-bold mb-1">詢價表單</h3>
                <p className="text-sm text-muted-foreground mb-3">
                  請填寫以下資訊，我們將盡快回覆您。
                </p>

                <div className="grid sm:grid-cols-2 gap-4">
                  <Field
                    label="姓名 *"
                    value={form.name}
                    onChange={(v) => update("name", v)}
                    error={errors.name}
                  />
                  <Field
                    label="公司名稱"
                    value={form.company}
                    onChange={(v) => update("company", v)}
                    error={errors.company}
                  />
                  <Field
                    label="電話 *"
                    value={form.phone}
                    onChange={(v) => update("phone", v)}
                    error={errors.phone}
                  />
                  <Field
                    label="Email *"
                    type="email"
                    value={form.email}
                    onChange={(v) => update("email", v)}
                    error={errors.email}
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium mb-1.5">需求內容 *</label>
                  <textarea
                    value={form.message}
                    onChange={(e) => update("message", e.target.value)}
                    rows={6}
                    maxLength={2000}
                    placeholder="請說明所需產品、規格尺寸、數量、用途與預計交期..."
                    className="w-full rounded-md border border-input bg-background px-3 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-ring resize-none"
                  />
                  {errors.message && (
                    <p className="text-xs text-destructive mt-1">{errors.message}</p>
                  )}
                </div>

                {errors.form && (
                  <p className="text-sm text-destructive">{errors.form}</p>
                )}

                <button
                  type="submit"
                  disabled={submitting}
                  className="inline-flex items-center gap-2 rounded-md bg-ember px-6 py-3 text-sm font-semibold text-accent-foreground shadow-ember hover:brightness-110 transition disabled:opacity-60"
                >
                  {submitting ? (
                    <>
                      <Loader2 size={16} className="animate-spin" /> 送出中...
                    </>
                  ) : (
                    <>
                      送出詢價 <Send size={15} />
                    </>
                  )}
                </button>
              </form>
            )}
          </div>
        </div>
      </section>
    </SiteLayout>
  );
}

function Field({
  label,
  value,
  onChange,
  error,
  type = "text",
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
  error?: string;
  type?: string;
}) {
  return (
    <div>
      <label className="block text-sm font-medium mb-1.5">{label}</label>
      <input
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full rounded-md border border-input bg-background px-3 py-2.5 text-sm focus:outline-none focus:ring-2 focus:ring-ring"
      />
      {error && <p className="text-xs text-destructive mt-1">{error}</p>}
    </div>
  );
}
