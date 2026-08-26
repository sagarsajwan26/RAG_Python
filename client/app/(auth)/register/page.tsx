"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import axios from "axios";
import { register } from "@/lib/api/auth";
import { Mail, Lock, User, ArrowRight, Loader2 } from "lucide-react";

export default function RegisterPage() {
  const router = useRouter();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      await register({ name, email, password });
      router.push("/login");
    } catch (error) {
      console.error("Registration error:", error);
      if (axios.isAxiosError(error)) {
        setError(error.response?.data?.detail ?? "Failed to register account.");
      } else {
        setError("Something went wrong. Please try again.");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-gradient-to-br from-accent-50 via-white to-brand-50 p-4">
      {/* Decorative background blobs */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
        <div className="absolute -top-24 -right-24 w-96 h-96 bg-accent-500/20 rounded-full blur-3xl"></div>
        <div className="absolute bottom-0 left-1/4 w-80 h-80 bg-brand-500/20 rounded-full blur-3xl"></div>
      </div>

      <div className="glass w-full max-w-md rounded-2xl p-8 relative">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-accent-600 to-brand-600 mb-2">
            Create Account
          </h1>
          <p className="text-surface-800/60 font-medium text-sm">
            Join the Knowledge Platform today
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-5">
          <div className="space-y-1">
            <label
              htmlFor="name"
              className="text-xs font-semibold uppercase tracking-wider text-surface-800/70"
            >
              Full Name
            </label>
            <div className="relative">
              <User className="absolute left-3 top-1/2 -translate-y-1/2 text-surface-800/40 w-5 h-5" />
              <input
                type="text"
                id="name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
                className="w-full pl-10 pr-4 py-3 rounded-xl border border-surface-200 bg-white/50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-accent-500/50 focus:border-accent-500 transition-all-smooth text-sm font-medium"
                placeholder="Jane Doe"
              />
            </div>
          </div>

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
                className="w-full pl-10 pr-4 py-3 rounded-xl border border-surface-200 bg-white/50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-accent-500/50 focus:border-accent-500 transition-all-smooth text-sm font-medium"
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
                className="w-full pl-10 pr-4 py-3 rounded-xl border border-surface-200 bg-white/50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-accent-500/50 focus:border-accent-500 transition-all-smooth text-sm font-medium"
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
            className="group relative w-full flex justify-center items-center gap-2 py-3 px-4 border border-transparent text-sm font-bold rounded-xl text-white bg-gradient-to-r from-accent-600 to-brand-600 hover:from-accent-500 hover:to-brand-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent-500 shadow-md hover:shadow-lg disabled:opacity-70 disabled:cursor-not-allowed transition-all-smooth overflow-hidden"
          >
            {loading ? (
              <Loader2 className="w-5 h-5 animate-spin" />
            ) : (
              <>
                <span>Create Account</span>
                <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
              </>
            )}
            
            {/* Shimmer effect */}
            <div className="absolute inset-0 -translate-x-full group-hover:animate-[shimmer_1.5s_infinite] bg-gradient-to-r from-transparent via-white/20 to-transparent pointer-events-none"></div>
          </button>
        </form>

        <div className="mt-8 text-center text-sm font-medium text-surface-800/60">
          Already have an account?{" "}
          <Link
            href="/login"
            className="text-accent-600 hover:text-accent-500 font-bold transition-colors"
          >
            Sign in here
          </Link>
        </div>
      </div>
    </main>
  );
}
