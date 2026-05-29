import { createServerFn } from "@tanstack/react-start";
import { z } from "zod";
import { supabaseAdmin } from "@/integrations/supabase/client.server";

const messageSchema = z.object({
  role: z.enum(["user", "assistant"]),
  content: z.string().min(1).max(4000),
});

const inputSchema = z.object({
  messages: z.array(messageSchema).min(1).max(40),
});

const PYTHON_API_URL = "http://localhost:8000/api/chat";

interface ApiResponse {
  reply: string;
  isEnded: boolean;
  structuredData: {
    name: string;
    company: string;
    phone: string;
    email: string;
    message: string;
  } | null;
}

export const sendChatMessage = createServerFn({ method: "POST" })
  .inputValidator((data: unknown) => inputSchema.parse(data))
  .handler(async ({ data }) => {
    try {
      const res = await fetch(PYTHON_API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: data.messages[data.messages.length - 1].content,
          history: data.messages,
        }),
      });

      if (!res.ok) {
        const text = await res.text();
        console.error("Python backend error", res.status, text);
        return { reply: "", error: "AI 服務暫時無法回應，請稍後再試。" };
      }

      const json = (await res.json()) as ApiResponse;
      const reply = json.reply;

      if (json.isEnded && json.structuredData !== null) {
        const s = json.structuredData;
        const { error: insertError } = await supabaseAdmin.from("inquiries").insert({
          name: s.name,
          company: s.company,
          phone: s.phone,
          email: s.email,
          message: s.message,
          source: "ai-chat",
        });
        if (insertError) {
          console.error("Insert inquiry failed", insertError);
        }
      }

      return { reply, error: null as string | null };
    } catch (err) {
      console.error("AI chat error", err);
      return { reply: "", error: "連線發生問題，請稍後再試。" };
    }
  });
