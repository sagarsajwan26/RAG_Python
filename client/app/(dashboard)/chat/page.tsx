"use client";
import React from "react";
import { FormEvent, useEffect, useState } from "react";
import { MessageSquare, Sparkles } from "lucide-react";
import { askQuestion, createConversation } from "@/lib/api/conversations";
import { Message } from "@/lib/types/conversation";

const TENANT_ID = 3;

export default function ChatPage() {
  const [conversationId, setConversationId] = useState<number | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [initializing, setInitializing] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function initializeConversation() {
      try {
        setInitializing(true);
        setError(null);
        const consersation = await createConversation(TENANT_ID);
        setConversationId(consersation.id);
      } catch (error) {
        console.error("Failed to create conversation:", error);
        setError("Failed to start conversation.");
      } finally {
        setInitializing(false);
      }
    }
    initializeConversation();
  }, []);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (!conversationId) {
      setError("conversation is not ready");
    }
    if (!question.trim()) {
      return;
    }
    const currentQuestion = question.trim();
    try {
      setLoading(true);
      setError(null);
      const userMessage: Message = {
        id: Date.now(),
        role: "user",
        content: currentQuestion,
      };
      setMessages((current) => [...current, userMessage]);
      setQuestion("");
      const response = await askQuestion(TENANT_ID, conversationId, currentQuestion, 5);
      const assistantMessage: Message = {
        id: Date.now() + 1,
        role: "assistant",
        content: response.answer,
      };
      setMessages((current) => [...current, assistantMessage]);
    } catch (error) {
      console.error("failed to ask question: ", error);
      setError("failed to get an answer");
    } finally {
      setLoading(false);
    }
  }
  if (initializing) {
    return (
      <main className="flex h-[calc(100vh-8rem)] items-center justify-center text-gray-500">
        <div className="flex flex-col items-center gap-3">
          <Sparkles className="h-8 w-8 animate-pulse text-blue-500" />
          <p className="text-lg font-medium">Starting conversation...</p>
        </div>
      </main>
    );
  }

  return (
    <div className="max-w-5xl mx-auto p-4 space-y-6 animate-in fade-in duration-500 h-[calc(100vh-8rem)] flex flex-col w-full">
      {error && (
        <div className="p-4 bg-red-50 text-red-600 rounded-lg border border-red-200 shadow-sm">
          {error}
        </div>
      )}
      
      <div className="flex-1 overflow-y-auto rounded-xl border bg-gray-50/50 p-4 sm:p-6 shadow-inner">
        {messages.length === 0 ? (
          <div className="flex h-full flex-col items-center justify-center text-gray-500 gap-4">
            <div className="p-4 bg-white rounded-full shadow-sm border border-gray-100">
              <MessageSquare className="h-10 w-10 text-blue-500" />
            </div>
            <p className="text-lg font-medium text-gray-600">Ask a question about your documents</p>
          </div>
        ) : (
          <div className="space-y-6">
            {messages.map((message) => (
              <div 
                key={message.id} 
                className={`flex flex-col max-w-[85%] sm:max-w-[75%] ${
                  message.role === "user" ? "ml-auto" : "mr-auto"
                }`}
              >
                <div className={`flex items-center gap-2 mb-1.5 ${message.role === "user" ? "justify-end" : "justify-start"}`}>
                  <strong className="text-sm font-medium text-gray-500 px-1">
                    {message.role === "user" ? "You" : "Assistant"}
                  </strong>
                </div>
                <div 
                  className={`px-5 py-3.5 rounded-2xl shadow-sm ${
                    message.role === "user" 
                      ? "bg-blue-600 text-white rounded-tr-sm" 
                      : "bg-white border border-gray-200 text-gray-800 rounded-tl-sm"
                  }`}
                >
                  <p className="whitespace-pre-wrap leading-relaxed">{message.content}</p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      <form onSubmit={handleSubmit} className="flex gap-3 shrink-0">
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask something..."
          disabled={loading}
          className="flex-1 rounded-xl border border-gray-300 bg-white px-5 py-4 text-base focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent shadow-sm disabled:bg-gray-50 disabled:text-gray-500 transition-all"
        />
        <button 
          type="submit" 
          disabled={loading || !question.trim()}
          className="rounded-xl bg-blue-600 px-8 py-4 font-semibold text-white shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:hover:bg-blue-600 transition-all flex items-center justify-center min-w-[120px]"
        >
          {loading ? (
            <span className="flex items-center gap-2">
              <div className="h-4 w-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
              Thinking
            </span>
          ) : (
            "Send"
          )}
        </button>
      </form>
    </div>
  );
}
