import gradio as gr
from src.rag.pipeline import RAGPipeline

pipeline = RAGPipeline()

def chat(query, product):
    product = product if product.strip() else None
    return pipeline.run(query, product)

with gr.Blocks(title="RAG Complaint Chatbot") as demo:
    gr.Markdown("## Financial Complaint Insight Assistant")

    query = gr.Textbox(label="User Question")
    product = gr.Textbox(label="Product Filter (optional)")
    output = gr.Textbox(label="Insight", lines=6)

    btn = gr.Button("Analyze")

    btn.click(chat, inputs=[query, product], outputs=output)

if __name__ == "__main__":
    demo.launch()
