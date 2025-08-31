from langchain.prompts import PromptTemplate

template_1 = PromptTemplate(
    template="""Your task is to summarize the given climate news or research article into a plain-language summary that is easily understandable by a general audience.

To achieve this, keep the following guidelines in mind:
* The summary should be concise, capturing the main points of the article in one paragraph;
* Use plain language that avoids technical jargon and scientific terms wherever possible;
* Ensure the key information and findings from the article are retained and clearly conveyed;
* Structure the summary to be engaging and informative, making the subject matter approachable for readers without specialized knowledge;

The article to be summarized is provided below:
{article}

Please generate the summary according to the guidelines above.""",
    input_variables=["article"],
    validate_template=True
)

template_1.save("template1.json")


