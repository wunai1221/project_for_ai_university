import { Link } from "@tanstack/react-router";
import { Phone, Mail, MapPin } from "lucide-react";

export function SiteFooter() {
  return (
    <footer className="bg-hero text-primary-foreground mt-20">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-14 grid gap-10 md:grid-cols-4">
        <div className="md:col-span-2">
          <div className="flex items-center gap-2.5 mb-4">
            <span className="flex h-10 w-10 items-center justify-center rounded-md bg-ember font-display text-base shadow-ember">
              鉅
            </span>
            <div>
              <p className="font-display font-bold text-lg">鉅昕鋼鐵股份有限公司</p>
              <p className="text-xs text-primary-foreground/60 tracking-wider">
                JUSIN STEEL CO., LTD.
              </p>
            </div>
          </div>
          <p className="text-sm text-primary-foreground/70 leading-relaxed max-w-md">
            專業鋼鐵材料供應、鋼筋加工、基礎螺栓製造與鋼構工程應用，
            提供穩定可靠且符合工程需求的鋼鐵解決方案。
          </p>
        </div>

        <div>
          <h4 className="font-display text-sm uppercase tracking-wider text-ember mb-4">
            快速連結
          </h4>
          <ul className="space-y-2 text-sm">
            {[
              ["/about", "關於我們"],
              ["/services", "產品服務"],
              ["/projects", "工程實績"],
              ["/contact", "聯絡我們"],
            ].map(([to, label]) => (
              <li key={to}>
                <Link
                  to={to}
                  className="text-primary-foreground/70 hover:text-ember transition-colors"
                >
                  {label}
                </Link>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <h4 className="font-display text-sm uppercase tracking-wider text-ember mb-4">
            聯絡資訊
          </h4>
          <ul className="space-y-3 text-sm text-primary-foreground/80">
            <li className="flex items-start gap-2">
              <Phone size={15} className="mt-0.5 text-ember" />
              <span>請填入公司電話</span>
            </li>
            <li className="flex items-start gap-2">
              <Mail size={15} className="mt-0.5 text-ember" />
              <span>請填入公司信箱</span>
            </li>
            <li className="flex items-start gap-2">
              <MapPin size={15} className="mt-0.5 text-ember" />
              <span>請填入公司地址</span>
            </li>
          </ul>
        </div>
      </div>
      <div className="border-t border-primary-foreground/10">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-5 text-xs text-primary-foreground/50 flex flex-col sm:flex-row justify-between gap-2">
          <p>© {new Date().getFullYear()} 鉅昕鋼鐵股份有限公司. All rights reserved.</p>
          <p>專業鋼鐵 · 安全可靠 · 即時交付</p>
        </div>
      </div>
    </footer>
  );
}
