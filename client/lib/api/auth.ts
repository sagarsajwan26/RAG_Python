import api from "../client";
export interface LoginRequest {
  email: string;
  password: string;
}
export interface RegisterRequest {
  email: string;
  password: string;
  name: string;
}

export interface AuthResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

export interface User {
  id: number;
  email: string;
  name: string;
}
export interface RegisterResponse {
  id: number;
  email: string;
  name: string;
}

export async function login(data: LoginRequest): Promise<AuthResponse> {
  const response = await api.post<AuthResponse>("/api/v1/auth/login", data);
  return response.data;
}

export async function register(
  data: RegisterRequest,
): Promise<RegisterResponse> {
  const response = await api.post<RegisterResponse>(
    "/api/v1/auth/register",
    data,
  );
  return response.data;
}

export async function refresh(): Promise<AuthResponse> {
  const response = await api.post<AuthResponse>("/api/v1/auth/refresh", {});
  return response.data;
}

export async function logout() {
  const response = await api.post("/api/v1/auth/logout", {});
  return response.data;
}
