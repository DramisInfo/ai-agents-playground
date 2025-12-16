#!/usr/bin/env python3
"""
Quick test script to verify Ollama embeddings are working.
"""

import ollama

def test_embedding():
    print("Testing Ollama embedding generation...")
    print(f"Model: nomic-embed-text")
    print(f"Host: http://localhost:11434")
    print()
    
    test_text = "This is a test document about customer support and FAQ systems."
    
    try:
        print(f"Generating embedding for: '{test_text}'")
        response = ollama.embeddings(
            model="nomic-embed-text",
            prompt=test_text
        )
        
        embedding = response["embedding"]
        print(f"✓ Success!")
        print(f"  Embedding dimensions: {len(embedding)}")
        print(f"  First 5 values: {embedding[:5]}")
        print(f"  Sample value range: [{min(embedding):.4f}, {max(embedding):.4f}]")
        print()
        print("✓ Ollama embeddings are working correctly!")
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        print("\nMake sure Ollama is running: ollama serve")
        return False

if __name__ == "__main__":
    test_embedding()
