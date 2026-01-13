import gradio as gr
from src.rag.pipeline import RAGPipeline

pipeline = RAGPipeline()

def chat(query, product):
    product = product if product.strip() else None
    return pipeline.run(query, product)


categories = [
    "All Products",
    "Credit card",
    "Buy Now, Pay Later (BNPL)",
    "Mortgage",
    "Student loan",
    "Debt collection",
    "Bank account or service",
    "Money transfers"
]

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    # Header
    gr.Markdown("# 🏦 CrediTrust Financial | AI Complaint Analyst")
    gr.Markdown("Ask questions about customer complaints and see the evidence used by the AI.")

    with gr.Row():
        # Input Column
        with gr.Column(scale=2):
            msg = gr.Textbox(
                label="Your Question",
                placeholder="e.g., Why are customers angry about late fees?",
                lines=2
            )
            dropdown = gr.Dropdown(
                choices=categories,
                value="All Products",
                label="Filter by Product"
            )
            submit_btn = gr.Button("🔍 Analyze Complaints", variant="primary")
            clear_btn = gr.ClearButton([msg, dropdown])

        # Output Column
        with gr.Column(scale=3):
            # The AI Answer
            output_answer = gr.Textbox(
                label="🤖 AI Executive Summary",
                lines=3,
                show_copy_button=True
            )

            # The Evidence (Trust Layer)
            with gr.Accordion("📚 View Source Evidence", open=False):
                output_sources = gr.Textbox(
                    label="Retrieved Context (Raw Data)",
                    lines=10,
                    interactive=False
                )

    # --- STEP 4: LINK INPUTS TO OUTPUTS ---
    submit_btn.click(
        fn=rag_interface,
        inputs=[msg, dropdown],
        outputs=[output_answer, output_sources]
    )

if __name__ == "__main__":
    demo.launch()
