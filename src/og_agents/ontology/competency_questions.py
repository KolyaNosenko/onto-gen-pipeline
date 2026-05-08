from pydantic import BaseModel, Field
from og_agents.ontology.competency_question import CompetencyQuestion

class CompetencyQuestions(BaseModel):
    questions: list[CompetencyQuestion] = Field(description="Список питань компетентності")
