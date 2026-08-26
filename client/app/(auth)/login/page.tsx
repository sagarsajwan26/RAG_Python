"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import axios from "axios";
import { login } from "@/lib/api/auth";
import { Mail, Lock, ArrowRight, Loader2 } from "lucide-react";

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      await login({ email, password });
      router.push("/chat");
    } catch (error) {
      console.error("Login error:", error);
      if (axios.isAxiosError(error)) {
        setError(error.response?.data?.detail ?? "Invalid email or password.");
      } else {
        setError("Something went wrong. Please try again.");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-gradient-to-br from-brand-100 via-white to-brand-50 p-4">
      {/* Decorative background blobs */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
        <div className="absolute -top-24 -left-24 w-96 h-96 bg-brand-500/20 rounded-full blur-3xl"></div>
        <div className="absolute top-1/2 right-0 w-80 h-80 bg-accent-500/20 rounded-full blur-3xl transform translate-x-1/2"></div>
      </div>

      <div className="glass w-full max-w-md rounded-2xl p-8 relative">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-brand-600 to-accent-600 mb-2">
            Welcome Back
          </h1>
          <p className="text-surface-800/60 font-medium text-sm">
            Sign in to your Knowledge Platform account
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-5">
          <div className="space-y-1">
            <label
              htmlFor="email"
              className="text-xs font-semibold uppercase tracking-wider text-surface-800/70"
            >
              Email Address
            </label>
            <div className="relative">
              <Mail className="absolute left-3 top-1/2 -translate-y-1/2 text-surface-800/40 w-5 h-5" />
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="w-full pl-10 pr-4 py-3 rounded-xl border border-surface-200 bg-white/50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-brand-500/50 focus:border-brand-500 transition-all-smooth text-sm font-medium"
                placeholder="name@example.com"
              />
            </div>
          </div>

          <div className="space-y-1">
            <label
              htmlFor="password"
              className="text-xs font-semibold uppercase tracking-wider text-surface-800/70"
            >
              Password
            </label>
            <div className="relative">
              <Lock className="absolute left-3 top-1/2 -translate-y-1/2 text-surface-800/40 w-5 h-5" />
              <input
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                className="w-full pl-10 pr-4 py-3 rounded-xl border border-surface-200 bg-white/50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-brand-500/50 focus:border-brand-500 transition-all-smooth text-sm font-medium"
                placeholder="••••••••"
              />
            </div>
          </div>

          {error && (
            <div className="p-3 bg-red-50 text-red-600 border border-red-100 rounded-lg text-sm font-medium text-center animate-in fade-in zoom-in duration-200">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="group relative w-full flex justify-center items-center gap-2 py-3 px-4 border border-transparent text-sm font-bold rounded-xl text-white bg-gradient-to-r from-brand-600 to-accent-600 hover:from-brand-500 hover:to-accent-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-500 shadow-md hover:shadow-lg disabled:opacity-70 disabled:cursor-not-allowed transition-all-smooth overflow-hidden"
          >
            {loading ? (
              <Loader2 className="w-5 h-5 animate-spin" />
            ) : (
              <>
                <span>Sign In</span>
                <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
              </>
            )}
            
            {/* Shimmer effect */}
            <div className="absolute inset-0 -translate-x-full group-hover:animate-[shimmer_1.5s_infinite] bg-gradient-to-r from-transparent via-white/20 to-transparent pointer-events-none"></div>
          </button>
        </form>

        <div className="mt-8 text-center text-sm font-medium text-surface-800/60">
          Don't have an account?{" "}
          <Link
            href="/register"
            className="text-brand-600 hover:text-brand-500 font-bold transition-colors"
          >
            Create one now
          </Link>
        </div>
      </div>
    </main>
  );
}
