"""Check the safety of your post."""

import os

from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeTextOptions

import dotenv
import streamlit as st

dotenv.load_dotenv()

def is_safe_content(content: str) -> bool:
    """Check the safety of your content. If the content corresponds to hate/sexual/violence/self-harm, return False."""

    endpoint = os.getenv("AZURE_AI_ENDPOINT")
    api_key = os.getenv("AZURE_AI_APIKEY")
    client = ContentSafetyClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(api_key)
    )

    request = AnalyzeTextOptions(text=content)
    response = client.analyze_text(request)
    for item in response.categories_analysis:
        if item.severity >= 4:
            st.error(f"不適切な内容を含んでいます")
            return False
    return True
