import { Link } from "@tanstack/react-router";
import { useState } from "react";
import { Menu, X } from "lucide-react";

const navItems = [
  { to: "/", label: "首頁" },
  { to: "/about", label: "關於我們" },
  { to: "/services", label: "產品服務" },
  { to: "/projects", label: "工程實績" },
  { to: "/contact", label: "聯絡我們" },
] as const;

export function SiteHeader() {
  const [open, setOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 border-b border-border bg-background/85 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <Link to="/" className="flex items-center gap-2.5 group">
          <span className="flex h-9 w-9 items-center justify-center rounded-md bg-hero text-primary-foreground font-display text-base shadow-steel">
            鉅
          </span>
          <span className="flex flex-col leading-tight">
            <span className="font-display text-sm sm:text-base font-bold text-foreground">
              鉅昕鋼鐵
            </span>
            <span className="text-[10px] text-muted-foreground tracking-wider">
              JUSIN STEEL CO., LTD.
            </span>
          </span>
        </Link>

        <nav className="hidden md:flex items-center gap-1">
          {navItems.map((item) => (
            <Link
              key={item.to}
              to={item.to}
              className="px-3 py-2 text-sm font-medium text-foreground/80 hover:text-foreground transition-colors rounded-md hover:bg-secondary"
              activeProps={{ className: "text-accent" }}
              activeOptions={{ exact: item.to === "/" }}
            >
              {item.label}
            </Link>
          ))}
          <Link
            to="/contact"
            className="ml-3 inline-flex items-center rounded-md bg-ember px-4 py-2 text-sm font-semibold text-accent-foreground shadow-ember hover:brightness-110 transition"
          >
            立即詢價
          </Link>
        </nav>

        <button
          className="md:hidden p-2 text-foreground"
          aria-label="Toggle menu"
          onClick={() => setOpen((o) => !o)}
        >
          {open ? <X size={22} /> : <Menu size={22} />}
        </button>
      </div>

      {open && (
        <nav className="md:hidden border-t border-border bg-background">
          <div className="flex flex-col px-4 py-3 gap-1">
            {navItems.map((item) => (
              <Link
                key={item.to}
                to={item.to}
                onClick={() => setOpen(false)}
                className="px-3 py-2.5 text-sm font-medium text-foreground/80 rounded-md hover:bg-secondary"
                activeProps={{ className: "text-accent" }}
                activeOptions={{ exact: item.to === "/" }}
              >
                {item.label}
              </Link>
            ))}
          </div>
        </nav>
      )}
    </header>
  );
}
