from transformers import pipeline

class InsightGenerator:
    def __init__(self):
        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            max_length=200,
            temperature=0.2,
            repetition_penalty=1.4,
            no_repeat_ngram_size=4
        )

    def generate(self, prompt: str):
        response = self.generator(
            prompt,
            do_sample=False
        )[0]["generated_text"]

        return response.strip()
