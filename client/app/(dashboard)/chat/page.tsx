"use client";

import { MessageSquare } from "lucide-react";

export default function ChatIndexPage() {
  return (
    <div className="flex h-full flex-col items-center justify-center text-gray-500 gap-4">
      <div className="p-6 bg-white rounded-full shadow-sm border border-gray-100 mb-2">
        <MessageSquare className="h-12 w-12 text-brand-500 opacity-60" />
      </div>
      <h2 className="text-xl font-semibold text-surface-900">Welcome to Chat</h2>
      <p className="text-base text-surface-500 text-center max-w-sm">
        Select a conversation from the sidebar or click "New Chat" to start exploring your documents.
      </p>
    </div>
  );
}
