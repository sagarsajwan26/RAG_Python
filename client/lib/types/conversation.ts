export interface Message {
  id: number;
  role: "user" | "assistant";
  content: string;
}

export interface Conversation {
  id: number;
  messages: Message[];
}
export interface ConversationCreateResponse {
  id: number;
}

export interface ConversationListItem {
  id: number;
  created_at: string;
  title: string | null;
}

export interface ConversationListResponse {
  conversations: ConversationListItem[];
}

export interface AskRequest {
  question: string;
  top_k?: number;
}

export interface Source {
  id: number;
  document_id: number;
  chunk_index: number;
  text: string;
}

export interface AskResponse {
  question: string;
  answer: string;
  sources: Source[];
}
