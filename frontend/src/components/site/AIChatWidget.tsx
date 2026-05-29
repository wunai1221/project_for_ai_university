import { useState, useRef, useEffect } from "react";
import { MessageCircle, X, Send, Loader2, CheckCircle2 } from "lucide-react";

type Msg = { role: "user" | "assistant"; content: string };

type CollectedData = {
  name: string;
  phone: string;
  service: string;
  date: string;
  color: string;
  note: string;
};

type ChatApiResponse = {
  reply: string;
  session_id: string;
  collected: CollectedData | null;
};

const PYTHON_API_URL = "http://localhost:8000/api/chat";

const GREETING: Msg = {
  role: "assistant",
  content:
    "您好，我是 AI 客服 👋\n請告訴我您想要的服務內容，我會一步一步協助您完成資料填寫。",
};

function createSessionId() {
  return `session_${Date.now()}_${Math.random().toString(36).slice(2)}`;
}

export function AIChatWidget() {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState<Msg[]>([GREETING]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [sessionId] = useState(() => createSessionId());

  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({
      top: scrollRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [messages, loading, submitted]);

  async function handleSend(e?: React.FormEvent) {
    e?.preventDefault();

    const text = input.trim();
    if (!text || loading) return;

    setMessages((m) => [...m, { role: "user", content: text }]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch(PYTHON_API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: text,
          session_id: sessionId,
        }),
      });

      if (!res.ok) {
        const errorText = await res.text();
        console.error("Python backend error:", res.status, errorText);

        setMessages((m) => [
          ...m,
          { role: "assistant", content: "⚠️ AI 服務暫時無法回應，請稍後再試。" },
        ]);
        return;
      }

      const result = (await res.json()) as ChatApiResponse;
      console.log("Python response:", result);

      setMessages((m) => [
        ...m,
        { role: "assistant", content: result.reply || "..." },
      ]);

      if (result.collected) {
        setSubmitted(true);
        setMessages((m) => [
          ...m,
          {
            role: "assistant",
            content:
              "✅ 資料已收集完成！系統已自動建立服務單，我們將盡快與您聯繫。",
          },
        ]);
      }
    } catch (err) {
      console.error("Chat error:", err);
      setMessages((m) => [
        ...m,
        { role: "assistant", content: "⚠️ 連線發生問題，請稍後再試。" },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <>
      {!open && (
        <button
          onClick={() => setOpen(true)}
          className="fixed bottom-5 right-5 z-50 flex items-center gap-2 rounded-full bg-ember px-5 py-3.5 text-sm font-semibold text-accent-foreground shadow-ember hover:brightness-110 transition group"
          aria-label="開啟 AI 客服"
        >
          <MessageCircle size={20} className="group-hover:scale-110 transition" />
          <span className="hidden sm:inline">AI 客服</span>
        </button>
      )}

      {open && (
        <div className="fixed bottom-5 right-5 z-50 w-[calc(100vw-2.5rem)] sm:w-96 h-[32rem] max-h-[80vh] flex flex-col rounded-xl bg-card border border-border shadow-steel overflow-hidden animate-in fade-in slide-in-from-bottom-4">
          <div className="flex items-center justify-between px-4 py-3 bg-hero text-primary-foreground">
            <div className="flex items-center gap-2.5">
              <div className="relative">
                <span className="flex h-9 w-9 items-center justify-center rounded-full bg-ember font-display text-sm shadow-ember">
                  AI
                </span>
                <span className="absolute -bottom-0.5 -right-0.5 h-2.5 w-2.5 rounded-full bg-green-400 ring-2 ring-[var(--steel-deep)]" />
              </div>
              <div>
                <p className="text-sm font-semibold">AI 客服</p>
                <p className="text-[11px] text-primary-foreground/70">
                  線上 · 即時回覆
                </p>
              </div>
            </div>

            <button
              onClick={() => setOpen(false)}
              className="p-1.5 rounded-md hover:bg-white/10 transition"
              aria-label="關閉"
            >
              <X size={18} />
            </button>
          </div>

          <div
            ref={scrollRef}
            className="flex-1 overflow-y-auto p-4 space-y-3 bg-muted/30"
          >
            {messages.map((m, i) => (
              <div
                key={i}
                className={`flex ${
                  m.role === "user" ? "justify-end" : "justify-start"
                }`}
              >
                <div
                  className={`max-w-[85%] rounded-2xl px-3.5 py-2.5 text-sm leading-relaxed whitespace-pre-wrap break-words ${
                    m.role === "user"
                      ? "bg-primary text-primary-foreground rounded-br-sm"
                      : "bg-card border border-border text-foreground rounded-bl-sm"
                  }`}
                >
                  {m.content}
                </div>
              </div>
            ))}

            {loading && (
              <div className="flex justify-start">
                <div className="bg-card border border-border rounded-2xl rounded-bl-sm px-3.5 py-2.5">
                  <Loader2 size={16} className="animate-spin text-accent" />
                </div>
              </div>
            )}

            {submitted && (
              <div className="flex items-center gap-2 rounded-lg border border-green-500/30 bg-green-500/10 px-3 py-2 text-sm text-green-700 dark:text-green-300">
                <CheckCircle2 size={16} />
                <span>資料已成功送出！</span>
              </div>
            )}
          </div>

          <form
            onSubmit={handleSend}
            className="flex items-end gap-2 p-3 border-t border-border bg-card"
          >
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  handleSend();
                }
              }}
              placeholder="輸入您的需求..."
              rows={1}
              maxLength={1000}
              className="flex-1 resize-none rounded-md border border-input bg-background px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-ring max-h-24"
            />

            <button
              type="submit"
              disabled={loading || !input.trim()}
              className="flex h-10 w-10 items-center justify-center rounded-md bg-ember text-accent-foreground shadow-ember hover:brightness-110 transition disabled:opacity-40 disabled:cursor-not-allowed"
              aria-label="送出"
            >
              <Send size={16} />
            </button>
          </form>
        </div>
      )}
    </>
  );
}