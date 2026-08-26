import api from "../client";
import {
  Source,
  Conversation,
  Message,
  ConversationCreateResponse,
  ConversationListItem,
  ConversationListResponse,
  AskRequest,
  AskResponse,
} from "../types/conversation";
export async function createConversation(tenantId: number): Promise<ConversationCreateResponse> {
  const response = await api.post<ConversationCreateResponse>(
    `/api/v1/conversations/?tenant_id=${tenantId}`,
  );

  return response.data;
}

export async function getConversations(tenantId: number): Promise<ConversationListItem[]> {
  const response = await api.get<{
    conversations: ConversationListItem[];
  }>(`/api/v1/conversations/?tenant_id=${tenantId}`);

  return response.data.conversations;
}

export async function getConversation(
  tenantId: number,
  conversationId: number,
): Promise<Conversation> {
  const response = await api.get<Conversation>(
    `/api/v1/conversations/${conversationId}?tenant_id=${tenantId}`,
  );
  return response.data;
}

export async function askQuestion(
  tenantId: number,
  conversationId: number,
  question: string,
  topK: number = 5,
): Promise<AskResponse> {
  const response = await api.post<AskResponse>(
    `/api/v1/conversations/${conversationId}/ask?tenant_id=${tenantId}`,
    {
      question,
      top_k: topK,
    },
  );
  return response.data;
}
