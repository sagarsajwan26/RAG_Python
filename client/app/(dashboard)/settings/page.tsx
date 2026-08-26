import React from "react";
import { Settings, Sliders } from "lucide-react";

export default function SettingsPage() {
  return (
    <div className="max-w-4xl mx-auto space-y-8 animate-in fade-in duration-500">
      <div>
        <h1 className="text-3xl font-extrabold text-surface-900 tracking-tight">Settings</h1>
        <p className="mt-2 text-surface-800/60 font-medium">Manage your account preferences and configurations.</p>
      </div>

      <div className="glass rounded-2xl border border-surface-200 p-10 bg-white/50 text-center relative overflow-hidden group">
        <div className="absolute top-0 right-0 w-64 h-64 bg-accent-500/10 rounded-full blur-3xl transform translate-x-1/2 -translate-y-1/2"></div>
        
        <div className="relative z-10 flex flex-col items-center">
          <div className="w-16 h-16 bg-surface-100 rounded-2xl flex items-center justify-center mb-6 border border-surface-200 group-hover:scale-110 transition-transform duration-300">
            <Sliders className="w-8 h-8 text-surface-500" />
          </div>
          <h2 className="text-xl font-bold text-surface-900 mb-2">Settings dashboard coming soon</h2>
          <p className="text-surface-800/60">
            Account management, API keys, and notification preferences will be available here.
          </p>
        </div>
      </div>
    </div>
  );
}
