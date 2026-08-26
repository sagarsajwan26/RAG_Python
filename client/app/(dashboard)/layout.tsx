"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { getCurrentUser, User } from "@/lib/api/users";
import { logout } from "@/lib/api/auth";
import { FileText, MessageSquare, Settings, LogOut, Loader2, Zap } from "lucide-react";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadUser() {
      try {
        const currentUser = await getCurrentUser();
        setUser(currentUser);
      } catch (error) {
        console.error("failed to load user", error);
        router.replace("/login");
      } finally {
        setLoading(false);
      }
    }
    loadUser();
  }, [router]);

  async function handleLogout() {
    try {
      await logout();
      router.replace("/login");
    } catch (error) {
      console.error("Logout failed:", error);
    }
  }

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-surface-50">
        <Loader2 className="w-10 h-10 text-brand-500 animate-spin" />
      </div>
    );
  }

  if (!user) {
    return null;
  }

  const navigation = [
    {
      name: "Documents",
      href: "/documents",
      icon: <FileText className="w-5 h-5" />,
    },
    {
      name: "Chat",
      href: "/chat",
      icon: <MessageSquare className="w-5 h-5" />,
    },
    {
      name: "Settings",
      href: "/settings",
      icon: <Settings className="w-5 h-5" />,
    },
  ];

  return (
    <div className="flex h-screen bg-surface-50 overflow-hidden text-surface-900">
      {/* Sidebar */}
      <aside className="w-72 flex flex-col bg-white border-r border-surface-200 shadow-sm z-10">
        <div className="p-6 border-b border-surface-100 flex items-center gap-3">
          <div className="p-2 bg-gradient-to-br from-brand-500 to-accent-500 rounded-lg text-white">
            <Zap className="w-6 h-6 fill-current" />
          </div>
          <div>
            <h1 className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-brand-600 to-accent-600">
              Nexus AI
            </h1>
            <p className="text-xs text-surface-800/60 font-medium">Knowledge Platform</p>
          </div>
        </div>

        <nav className="flex-1 px-4 py-6 overflow-y-auto">
          <div className="space-y-1">
            {navigation.map((item) => {
              const active = pathname.startsWith(item.href);

              return (
                <Link
                  key={item.href}
                  href={item.href}
                  className={`flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-semibold transition-all-smooth ${
                    active
                      ? "bg-gradient-to-r from-brand-50 to-accent-50 text-brand-700 shadow-sm border border-brand-100"
                      : "text-surface-800/70 hover:bg-surface-100 hover:text-surface-900"
                  }`}
                >
                  <div className={active ? "text-brand-500" : "text-surface-800/50"}>
                    {item.icon}
                  </div>
                  {item.name}
                  {active && (
                    <div className="ml-auto w-1.5 h-5 rounded-full bg-brand-500"></div>
                  )}
                </Link>
              );
            })}
          </div>
        </nav>

        <div className="p-4 border-t border-surface-100">
          <div className="flex items-center gap-3 mb-4 p-2 rounded-xl bg-surface-50 border border-surface-100">
            <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-accent-500 to-brand-500 flex items-center justify-center text-white font-bold text-sm shadow-inner">
              {user.name.charAt(0).toUpperCase()}
            </div>
            <div className="overflow-hidden">
              <p className="font-semibold text-sm truncate">{user.name}</p>
              <p className="text-xs text-surface-800/60 truncate">{user.email}</p>
            </div>
          </div>

          <button
            type="button"
            onClick={handleLogout}
            className="w-full flex items-center justify-center gap-2 rounded-xl border border-surface-200 px-4 py-2.5 text-sm font-semibold text-surface-800/80 hover:bg-red-50 hover:text-red-600 hover:border-red-200 transition-colors"
          >
            <LogOut className="w-4 h-4" />
            Logout
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col h-full overflow-hidden relative">
        {/* Top gradient blur */}
        <div className="absolute top-0 inset-x-0 h-32 bg-gradient-to-b from-white to-transparent pointer-events-none z-10"></div>
        
        <div className="flex-1 overflow-y-auto p-8 lg:p-12 z-0">
          <div className="max-w-6xl mx-auto">
            {children}
          </div>
        </div>
      </main>
    </div>
  );
}
