from pydantic import BaseModel, Field

class CompetencyQuestion(BaseModel):
    text: str = Field(description="Текст питання компетентності")
