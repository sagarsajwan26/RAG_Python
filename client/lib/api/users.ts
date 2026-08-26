import api from "../client";

export interface User {
  id: number;
  email: string;
  name: string;
}

export async function getCurrentUser(): Promise<User> {
  const response = await api.get<User>("/api/v1/users/me");

  return response.data;
}
