from dataclasses import dataclass
from datetime import date
from typing import Dict, List, Optional
from django.conf import settings
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel


gpt_35_turbo = OpenAIModel(
    "gpt-3.5-turbo",
    api_key=settings.OPENAI_API_KEY,
)


class AgentSuusResult(BaseModel):
    line_1: str = Field(description="Eerst regel van het gedicht (A)")
    line_2: str = Field(description="Tweede regel van het gedicht (A)")
    line_3: str = Field(description="Derde regel van het gedicht (B)")
    line_4: str = Field(description="Vierde regel van het gedicht (B)")


@dataclass
class AgentSuusDependencies:
    prompt: str = Field(
        description="Informatie die de gebruiker heeft gegeven om een gedicht te schrijven."
    )


agent_suus = Agent(
    model=gpt_35_turbo,
    result_type=AgentSuusResult,
    system_prompt=(
        "Het enige dat je hoeft te doen is de gebruiker te helpen met het schrijven van een gedicht. "
        "Gebaseerd op de informatie, schrijf je een alinea van 4 regels (die niet al te lang zijn). "
        "De manier van rijmen is als volgt: AABB. "
        "De eerste en tweede regel rijmen met elkaar, "
        "en de derde en vierde regel rijmen met elkaar. "
        "Zorg ervoor dat de regels goed bij elkaar passen en "
        "dat het gedicht een mooi geheel vormt. "
        "Spreek altijd in de vorm van een gedicht, "
        "en maak gebruik van mooie & volwassen woorden en zinnen."
        "Het gedicht mag niet al te kinderlijk gemaakt zijn."
    ),
)


@agent_suus.tool_plain
def schrijf_gedicht_alinea() -> AgentSuusResult:
    """Schrijf een gedicht alinea."""
    return AgentSuusResult(
        line_1="Eerst regel van het gedicht (A)", 
        line_2="Tweede regel van het gedicht (A)", 
        line_3="Derde regel van het gedicht (B)", 
        line_4="Vierde regel van het gedicht (B)"
    )