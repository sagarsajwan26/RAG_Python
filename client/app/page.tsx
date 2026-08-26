"use client";

import { useEffect, useState } from "react";
import { getCurrentUser, User } from "@/lib/api/users";
import axios from "axios";

export default function Home() {
  const [user, setUser] = useState<User | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadUser() {
      try {
        const data = await getCurrentUser();
        setUser(data);
      } catch (error) {
        console.error("FULL ERROR:", error);

        if (axios.isAxiosError(error)) {
          console.log("Axios error:", error);
          console.log("message:", error.message);
          console.log("code:", error.code);
          console.log("request:", error.request);
          console.log("response:", error.response);

          setError(
            `Axios error: ${error.message} | code: ${error.code ?? "none"}`,
          );
        } else {
          console.error("Non-Axios error:", error);
          setError("Unknown error");
        }
      }
    }

    loadUser();
  }, []);

  if (error) {
    return <div>{error}</div>;
  }

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <main>
      <h1>Welcome {user.name}</h1>
      <p>{user.email}</p>
    </main>
  );
}
