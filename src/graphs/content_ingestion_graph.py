"""
TODO: Define a LangGraph for content ingestion

This graph should:
- Orchestrate fetching from sources (RSS/HTML)
- Fan-out per source, then per article
- Call classification chain and chunking step
- Emit events/metrics for monitoring
"""

# TODO: Import langgraph primitives (StateGraph, Node, edge definitions)
# TODO: Define state schema for the graph (e.g., current_source, article_batch, errors)
# TODO: Create nodes: fetch_sources, fetch_articles, classify_article, chunk_article, persist_results
# TODO: Wire edges and conditional routing (success/error)
# TODO: Add entrypoint and runner helper
# TODO: Expose function `build_content_ingestion_graph()` returning the compiled graph
