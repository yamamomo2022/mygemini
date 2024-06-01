import typing_extensions as typing
import google.generativeai as genai
from config import Config


class Recipe(typing.TypedDict):
    popular_physical_phenomena: str

def json_mode(text : str,model_name : str = "models/gemini-1.5-pro-latest") -> str:

    genai.configure(api_key=Config.API_KEY)

    model = genai.GenerativeModel(model_name=model_name)

    result = model.generate_content(
        text,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json",
            response_schema = list[Recipe]),
        request_options={"timeout": 600},
    )

    return result.text    


if __name__ == '__main__':
    text = "List a few popular physical phenomenas"
    print(json_mode(text))
    