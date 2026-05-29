import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import {
  Outlet,
  Link,
  createRootRouteWithContext,
  useRouter,
  HeadContent,
  Scripts,
} from "@tanstack/react-router";

import appCss from "../styles.css?url";

function NotFoundComponent() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background px-4">
      <div className="max-w-md text-center">
        <h1 className="text-7xl font-bold text-foreground">404</h1>
        <h2 className="mt-4 text-xl font-semibold text-foreground">Page not found</h2>
        <p className="mt-2 text-sm text-muted-foreground">
          The page you're looking for doesn't exist or has been moved.
        </p>
        <div className="mt-6">
          <Link
            to="/"
            className="inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
          >
            Go home
          </Link>
        </div>
      </div>
    </div>
  );
}

function ErrorComponent({ error, reset }: { error: Error; reset: () => void }) {
  console.error(error);
  const router = useRouter();

  return (
    <div className="flex min-h-screen items-center justify-center bg-background px-4">
      <div className="max-w-md text-center">
        <h1 className="text-xl font-semibold tracking-tight text-foreground">
          This page didn't load
        </h1>
        <p className="mt-2 text-sm text-muted-foreground">
          Something went wrong on our end. You can try refreshing or head back home.
        </p>
        <div className="mt-6 flex flex-wrap justify-center gap-2">
          <button
            onClick={() => {
              router.invalidate();
              reset();
            }}
            className="inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
          >
            Try again
          </button>
          <a
            href="/"
            className="inline-flex items-center justify-center rounded-md border border-input bg-background px-4 py-2 text-sm font-medium text-foreground transition-colors hover:bg-accent"
          >
            Go home
          </a>
        </div>
      </div>
    </div>
  );
}

export const Route = createRootRouteWithContext<{ queryClient: QueryClient }>()({
  head: () => ({
    meta: [
      { charSet: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { title: "鉅昕鋼鐵股份有限公司｜專業鋼鐵加工・基礎螺栓・鋼構工程" },
      {
        name: "description",
        content:
          "鉅昕鋼鐵專注於鋼鐵材料供應、鋼筋加工、基礎螺栓製造與鋼構工程應用，提供穩定可靠的鋼鐵解決方案，並提供 AI 線上詢價服務。",
      },
      { name: "author", content: "鉅昕鋼鐵股份有限公司" },
      { property: "og:title", content: "鉅昕鋼鐵股份有限公司｜專業鋼鐵加工・基礎螺栓・鋼構工程" },
      {
        property: "og:description",
        content: "專業鋼鐵加工、基礎螺栓與鋼構工程解決方案。",
      },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
      { name: "twitter:title", content: "鉅昕鋼鐵股份有限公司｜專業鋼鐵加工・基礎螺栓・鋼構工程" },
      { name: "description", content: "Juxin Steel Solutions offers a corporate website showcasing steel processing, supply, and AI-powered inquiry services." },
      { property: "og:description", content: "Juxin Steel Solutions offers a corporate website showcasing steel processing, supply, and AI-powered inquiry services." },
      { name: "twitter:description", content: "Juxin Steel Solutions offers a corporate website showcasing steel processing, supply, and AI-powered inquiry services." },
      { property: "og:image", content: "https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/1c2a9c8f-6240-44e1-b781-ce632e4226ce/id-preview-6deddef5--31312373-be94-43a6-b4a2-1f716b3b7a0f.lovable.app-1779170292743.png" },
      { name: "twitter:image", content: "https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/1c2a9c8f-6240-44e1-b781-ce632e4226ce/id-preview-6deddef5--31312373-be94-43a6-b4a2-1f716b3b7a0f.lovable.app-1779170292743.png" },
    ],
    links: [
      { rel: "stylesheet", href: appCss },
      { rel: "preconnect", href: "https://fonts.googleapis.com" },
      { rel: "preconnect", href: "https://fonts.gstatic.com", crossOrigin: "anonymous" },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Orbitron:wght@600;700;800&display=swap",
      },
    ],
  }),
  shellComponent: RootShell,
  component: RootComponent,
  notFoundComponent: NotFoundComponent,
  errorComponent: ErrorComponent,
});

function RootShell({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <HeadContent />
      </head>
      <body>
        {children}
        <Scripts />
      </body>
    </html>
  );
}

function RootComponent() {
  const { queryClient } = Route.useRouteContext();

  return (
    <QueryClientProvider client={queryClient}>
      <Outlet />
    </QueryClientProvider>
  );
}
