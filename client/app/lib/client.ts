const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function getHealth() {
  const response = await fetch(`${API_URL}/api/v1/health`);
  if (!response.ok) {
    throw new Error("backend request failed");
  }
  return response.json();
}
