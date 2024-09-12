from langchain.schema import Document  # 이 줄을 수정
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

import os
# 일기데이터 요약해줘 
# 일기데이터 경험부분 벡터 데이터에 보관 
# 일기데이터 감정부분 벡터 데이터에 보관 
# 일기데이터 경험부분 벡터 데이터에 보관 
# 일기 전체 데이터 보관 

load_dotenv()
llm = HuggingFaceHub(repo_id="psyche/KoT5-summarization", model_kwargs={"temperature": 0.7, "max_length": 200}) # 한국어 요약 모델 , 상업적으로는 불가능 추후 upstage 사용 필요


prompt_template = PromptTemplate(
    input_variables=["content"],
    template="다음 일기 내용을 요약해주세요:\n\n{content}"
)

# LLMChain 생성
chain = LLMChain(llm=llm, prompt=prompt_template)

def summarize_diary(content):
        return chain.run(content=content)  # 여기를 수정했습니다

# 벡터화 

# embedding = OpenAIEmbeddings()

## db
def get_json_to_dictionary(dic_data):
    date = dic_data.get('date', '')
    name = dic_data.get('name', '')
    work = dic_data.get('work', {})
    experience_type = work.get('experience_type', '')
    feeling = work.get('feeling', '')
    detail_type = work.get('detail_type', '')
    story = work.get('story', '')
    insight = work.get('insight', '')

        # page_content를 문자열로 변환
    page_content = str(work)
    doc = Document(page_content=page_content, metadata={"date": date, "name": name, "experience_type": experience_type, "feeling": feeling, "detail_type": detail_type})
    return doc   

# 저장

def save_diary(content):
    print(content)
    docs = get_json_to_dictionary(content)
    print(docs) # 현재 벡터데이터가 아님
    embeddings = OpenAIEmbeddings(model='text-embedding-3-large')
    index_name = 'streamlit-diary'
    embedding_dim = len(embeddings.embed_query("test"))
    print(f"임베딩 차원: {embedding_dim}")
    # Pinecone API 키 설정
    pinecone_api_key = os.environ.get("PINECONE_API_KEY")
    # Pinecone 초기화
    pc = Pinecone(api_key=pinecone_api_key)

    vectorstore = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)
    vectorstore.add_documents([docs])




