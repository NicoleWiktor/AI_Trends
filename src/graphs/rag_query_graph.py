"""
TODO: Define a LangGraph for RAG-powered Q&A

This graph should:
- Embed query
- Retrieve from vector index (RAGService)
- Synthesize answer via LLM with retrieved context
- Optionally call web_search tool when retrieval is weak
"""

# TODO: Import langgraph
# TODO: Define state schema (query, lane_filter, retrieved_chunks, needs_web_search)
# TODO: Nodes: embed_query, retrieve, decide_need_web, web_search, synthesize_answer
# TODO: Expose `build_rag_query_graph()`
