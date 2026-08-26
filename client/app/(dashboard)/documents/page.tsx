"use client";

import { getDocuments, uploadDocument } from "@/lib/api/documents";
import React, { useEffect, useState, useRef } from "react";
import { Document } from "@/lib/types/document";
import { UploadCloud, FileText, CheckCircle2, Loader2, AlertCircle, Clock } from "lucide-react";

const TENANT_ID = 3;

export default function DocumentsPage() {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [loading, setLoading] = useState(true);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  async function loadDocuments() {
    try {
      setLoading(true);
      setError(null);
      const data = await getDocuments(TENANT_ID);
      setDocuments(data);
    } catch (error) {
      console.error("Failed to load documents:", error);
      setError("Failed to load documents.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadDocuments();
  }, []);

  async function handleUpload(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    try {
      setUploading(true);
      setError(null);

      const document = await uploadDocument(TENANT_ID, file);
      setDocuments((current) => [document, ...current]);
    } catch (error) {
      console.error("Upload failed:", error);
      setError("Failed to upload document. Please ensure it's a PDF or TXT file.");
    } finally {
      setUploading(false);
      if (fileInputRef.current) {
        fileInputRef.current.value = "";
      }
    }
  }

  if (loading) {
    return (
      <div className="flex min-h-[400px] items-center justify-center">
        <Loader2 className="w-10 h-10 text-brand-500 animate-spin" />
      </div>
    );
  }

  return (
    <div className="max-w-5xl mx-auto space-y-8 animate-in fade-in duration-500">
      <div>
        <h1 className="text-3xl font-extrabold text-surface-900 tracking-tight">Documents</h1>
        <p className="text-surface-800/60 mt-2 font-medium">Upload and manage your knowledge base.</p>
      </div>

      {error && (
        <div className="flex items-center gap-3 p-4 bg-red-50 text-red-600 border border-red-100 rounded-xl">
          <AlertCircle className="w-5 h-5 flex-shrink-0" />
          <p className="text-sm font-medium">{error}</p>
        </div>
      )}

      {/* Upload Zone */}
      <div className="relative group">
        <div className="absolute inset-0 bg-gradient-to-r from-brand-500 to-accent-500 rounded-2xl blur-xl opacity-20 group-hover:opacity-30 transition-opacity duration-500"></div>
        <div className="relative glass border-2 border-dashed border-brand-200 hover:border-brand-400 rounded-2xl p-10 text-center transition-all-smooth bg-white/50 hover:bg-white/80">
          <input
            type="file"
            accept=".pdf,.txt"
            onChange={handleUpload}
            disabled={uploading}
            ref={fileInputRef}
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer disabled:cursor-not-allowed"
          />
          <div className="flex flex-col items-center justify-center space-y-4">
            <div className="w-16 h-16 bg-brand-50 rounded-full flex items-center justify-center text-brand-500 group-hover:scale-110 group-hover:bg-brand-100 transition-all-smooth">
              {uploading ? (
                <Loader2 className="w-8 h-8 animate-spin" />
              ) : (
                <UploadCloud className="w-8 h-8" />
              )}
            </div>
            <div>
              <h3 className="text-lg font-bold text-surface-900">
                {uploading ? "Uploading document..." : "Click or drag to upload"}
              </h3>
              <p className="text-sm font-medium text-surface-800/60 mt-1">
                Supports PDF and TXT files up to 10MB
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Documents List */}
      <div className="space-y-4">
        <h2 className="text-xl font-bold text-surface-900 flex items-center gap-2">
          <FileText className="w-5 h-5 text-brand-500" />
          Your Files
        </h2>

        {documents.length === 0 ? (
          <div className="glass rounded-2xl p-12 text-center border border-surface-200">
            <FileText className="w-12 h-12 text-surface-300 mx-auto mb-4" />
            <h3 className="text-lg font-bold text-surface-900">No documents found</h3>
            <p className="text-surface-800/60 mt-1 text-sm">Upload your first document above to get started.</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {documents.map((document) => (
              <div 
                key={document.id} 
                className="group glass bg-white hover:bg-gradient-to-br hover:from-white hover:to-brand-50 border border-surface-200 hover:border-brand-200 rounded-2xl p-5 transition-all-smooth hover:-translate-y-1 hover:shadow-lg"
              >
                <div className="flex items-start justify-between mb-4">
                  <div className="w-10 h-10 rounded-lg bg-accent-50 text-accent-600 flex items-center justify-center">
                    <FileText className="w-5 h-5" />
                  </div>
                  <div className={`px-2.5 py-1 rounded-full text-xs font-bold flex items-center gap-1 border ${
                    document.status?.toLowerCase() === 'processed' 
                      ? 'bg-green-50 text-green-700 border-green-200' 
                      : document.status?.toLowerCase() === 'failed'
                      ? 'bg-red-50 text-red-700 border-red-200'
                      : 'bg-yellow-50 text-yellow-700 border-yellow-200'
                  }`}>
                    {document.status?.toLowerCase() === 'processed' ? <CheckCircle2 className="w-3 h-3" /> : <Clock className="w-3 h-3" />}
                    {document.status || 'Processing'}
                  </div>
                </div>
                
                <h3 className="font-bold text-surface-900 truncate" title={document.filename}>
                  {document.filename}
                </h3>
                <div className="mt-4 flex items-center justify-between text-xs font-medium text-surface-800/50">
                  <span>ID: {document.id}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
