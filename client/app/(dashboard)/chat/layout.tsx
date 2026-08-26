"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { getConversations, createConversation } from "@/lib/api/conversations";
import { ConversationListItem } from "@/lib/types/conversation";
import { MessageSquarePlus, MessageSquare, Loader2 } from "lucide-react";

const TENANT_ID = 3;

export default function ChatLayout({ children }: { children: React.ReactNode }) {
  const [conversations, setConversations] = useState<ConversationListItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [creating, setCreating] = useState(false);
  const pathname = usePathname();
  const router = useRouter();

  useEffect(() => {
    async function fetchConversations() {
      try {
        const data = await getConversations(TENANT_ID);
        // Sort conversations by ID descending to show newest first
        const sorted = (data || []).sort((a, b) => b.id - a.id);
        setConversations(sorted);
      } catch (error) {
        console.error("Failed to fetch conversations", error);
      } finally {
        setLoading(false);
      }
    }
    fetchConversations();
  }, [pathname]);

  async function handleNewChat() {
    try {
      setCreating(true);
      const newChat = await createConversation(TENANT_ID);
      router.push(`/chat/${newChat.id}`);
    } catch (error) {
      console.error("Failed to create new chat", error);
    } finally {
      setCreating(false);
    }
  }

  return (
    <div className="flex h-[calc(100vh-8rem)] bg-white rounded-2xl border border-surface-200 overflow-hidden shadow-sm">
      {/* Sidebar for Chat History */}
      <div className="w-64 border-r border-surface-100 flex flex-col bg-surface-50/50 shrink-0">
        <div className="p-4 border-b border-surface-100">
          <button
            onClick={handleNewChat}
            disabled={creating}
            className="w-full flex items-center justify-center gap-2 bg-brand-600 text-white px-4 py-2.5 rounded-xl font-semibold hover:bg-brand-700 transition-colors disabled:opacity-50"
          >
            {creating ? <Loader2 className="w-4 h-4 animate-spin" /> : <MessageSquarePlus className="w-4 h-4" />}
            New Chat
          </button>
        </div>
        
        <div className="flex-1 overflow-y-auto p-3 space-y-1">
          {loading ? (
            <div className="flex justify-center py-4">
              <Loader2 className="w-5 h-5 text-brand-500 animate-spin" />
            </div>
          ) : conversations.length === 0 ? (
            <p className="text-center text-sm text-surface-500 py-4">No recent chats</p>
          ) : (
            conversations.map((chat) => (
              <Link
                key={chat.id}
                href={`/chat/${chat.id}`}
                className={`flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors ${
                  pathname === `/chat/${chat.id}`
                    ? "bg-brand-50 text-brand-700"
                    : "text-surface-700 hover:bg-surface-100"
                }`}
              >
                <MessageSquare className="w-4 h-4 shrink-0 opacity-50" />
                <span className="truncate">{chat.title || `Chat ${chat.id}`}</span>
              </Link>
            ))
          )}
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {children}
      </div>
    </div>
  );
}
