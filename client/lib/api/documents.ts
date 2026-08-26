import api from "../client";
import { Document } from "../types/document";

export async function getDocuments(tenantId: number): Promise<Document[]> {
  const response = await api.get<Document[]>(`/api/v1/document/${tenantId}/documents`);
  return response.data;
}

export async function uploadDocument(
  tenantId: number,
  file: File,
): Promise<Document> {
  const formData = new FormData();
  formData.append("file", file);

  const response = await api.post<Document>(
    `/api/v1/document/${tenantId}/documents`,
    formData,
  );

  return response.data;
}
