import { NextRequest, NextResponse } from "next/server";
const protectedRoutes = ["/chat", "/documents", "/settings"];
const authRoutes = ["/login", "/register"];

export function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const accessToken = request.cookies.get("access_token");
  const isProtectedRoute = protectedRoutes.some(
    (route) => pathname === route || pathname.startsWith(`${route}/`),
  );

  const isAuthRoute = authRoutes.some(
    (route) => pathname === route || pathname.startsWith(`${route}/`),
  );

  if (!isProtectedRoute && !accessToken) {
    return NextResponse.redirect(new URL("/login", request.url));
  }
  if (isAuthRoute && accessToken) {
    return NextResponse.redirect(new URL("/chat", request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: [
    "/chat/:path*",
    "/documents/:path*",
    "/settings/:path",
    "/login",
    "/register",
  ],
};
