"use client";

import { useEffect } from "react";

export default function Home() {
  useEffect(() => {
    fetch("http://localhost:8000/api/v1/health")
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  }, []);

  return <h1>AI Document Intelligence</h1>;
}
