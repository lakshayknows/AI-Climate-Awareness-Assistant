from langchain.schema.runnable import RunnableParallel
from summarizer import summarize_text
from quiz_generator import generate_quiz
from recommender import recommender

# Build parallel chain
merge_chain = RunnableParallel(
    summary=summarize_text,
    quiz=generate_quiz,
    actions=recommender,
)

def merged_output(article: str):
    return merge_chain.invoke({"article": article})

if __name__ == "__main__":
    sample_text = "A rainbow is formed by refraction, reflection, and dispersion of sunlight in water droplets..."
    result = merged_output(sample_text)
    print(result)
