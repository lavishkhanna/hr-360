from docx import Document
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity





def convert(filepath):

    document = Document(filepath)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text



resume = ""


resume_text = convert(resume)

job_desc=""

job_desc_text=convert(job_desc)

text=[resume_text,job_desc_text]


cv=CountVectorizer()
count_matrix=cv.fit_transform(text)

print(cosine_similarity(count_matrix))


match=cosine_similarity(count_matrix)[0][1]

match=round(match*100,2)