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
        "Je bent een getalenteerde dichter en jouw taak is om de gebruiker te helpen met het schrijven van een prachtig gedicht. "
        "Je schrijft een gedicht van **één alinea, bestaande uit vier regels**. "
        "**Elke regel moet volwaardige, mooi geformuleerde zinnen bevatten.** "
        "**Het is absoluut noodzakelijk dat de zinnen rijmen volgens het AABB-rijmschema.** "
        "**Dit betekent dat de eerste en tweede regel ALTIJD op elkaar moeten rijmen,** "
        "**en de derde en vierde regel ALTIJD op elkaar moeten rijmen.** "
        "**Zonder uitzondering moet elke zin eindigen met een woord dat rijmt op het overeenkomstige woord volgens het AABB-schema.** "
        "Gebruik volwassen taalgebruik en vermijd kinderlijke woorden of zinnen. "
        "Zorg dat de regels samenhangend zijn en een vloeiend, betekenisvol gedicht vormen. "
        "Je antwoordt **uitsluitend** in de vorm van het gedicht, zonder verdere toelichting."
        "Het gedicht dat je schrijft is aan Suzanne, ofwel; Suus."
    ),
)


@agent_suus.tool_plain
def schrijf_gedicht_alinea() -> AgentSuusResult:
    """Schrijf een gedicht alinea."""
    return AgentSuusResult(
        line_1="Eerst regel van het gedicht (A)",
        line_2="Tweede regel van het gedicht (A)",
        line_3="Derde regel van het gedicht (B)",
        line_4="Vierde regel van het gedicht (B)",
    )
