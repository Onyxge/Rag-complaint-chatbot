from src.rag.retriever import ComplaintRetriever
from src.rag.generator import InsightGenerator
from src.rag.prompt import ANALYST_PROMPT

class RAGPipeline:
    def __init__(self):
        self.retriever = ComplaintRetriever()
        self.generator = InsightGenerator()

    def run(self, question: str, product: str | None = None):
        results = self.retriever.search(question, product=product)

        if not results:
            return "No relevant complaints found."

        context = "\n".join(
            f"- {r['text'].replace(chr(10), ' ').strip()}"
            for r in results[:3]
        )

        prompt = ANALYST_PROMPT.format(
            context=context,
            question=question
        )

        return self.generator.generate(prompt)
