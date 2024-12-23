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
        "Je schrijft één alinea, bestaande uit vier regels. "
        "Elke regel bestaat uit een volwaardige, mooi geformuleerde zin."
        "**Het is absoluut noodzakelijk dat de zinnen rijmen volgens het AABB-rijmschema.** "
        "**Dit betekent: "
        "dat de eerste en tweede regel ALTIJD op elkaar moeten rijmen, "
        "en de derde en vierde regel ALTIJD op elkaar moeten rijmen. "
        "Zonder uitzondering moet elke zin eindigen met een woord dat rijmt op het overeenkomstige woord volgens het AABB-schema.** "
        "Gebruik volwassen taalgebruik en vermijd kinderlijke woorden of zinnen. "
        "Zorg dat de regels samenhangend zijn en een vloeiend, betekenisvol gedicht vormen. "
        "Je antwoordt **uitsluitend** in de vorm van het gedicht, zonder verdere toelichting."
        "Richt dit gedicht aan Suzanne (Suus)."
        "Hier is een lijst met voorbeeld rijmwoorden: "
        " 1 Hond - Mond"
        " 2 Kat - Mat"
        " 3 Stoel - Koel"
        " 4 Huis - Muis"
        " 5 Boom - Room"
        " 6 Roos - Doos"
        " 7 Vloer - Boer"
        " 8 Deur - Geur"
        " 9 Raam - Naam"
        " 10 Sok - Klok"
        " 11 Pen - Ren"
        " 12 Boek - Zoek"
        " 13 Licht - Dicht"
        " 14 Lach - Dag"
        " 15 Nacht - Wacht"
        " 16 Hand - Land"
        " 17 Voet - Zoet"
        " 18 Zwart - Hart"
        " 19 Groot - Lood"
        " 20 Klein - Fijn"
        " 21 Wijn - Pijn"
        " 22 Zon - Ton"
        " 23 Maan - Gaan"
        " 24 Ster - Ver"
        " 25 Berg - Erg"
        " 26 Wind - Kind"
        " 27 Zee - Twee"
        " 28 Knie - Wie"
        " 29 Jas - Tas"
        " 30 Hoed - Goed"
        " 31 Broek - Vloek"
        " 32 Jurk - Kurk"
        " 33 Riem - Siem"
        " 34S choen - Groen"
        " 35 Vinger - Zanger"
        " 36 Arm - Warm"
        " 37 Been - Heen"
        " 38 Haar - Daar"
        " 39 Oog - Hoog"
        " 40 Neus - Reus"
        " 41 Muur - Vuur"
        " 42 Kast - Vast"
        " 43 Tafel - Wafel"
        " 44 Lamp - Ramp"
        " 45 Krant - Klant"
        " 46 Fiets - Iets"
        " 47 Trein - Fontein"
        " 48 Kroeg - Vroeg"
        " 49 Boot - Noot"
        " 50 Lied - Verdriet"
        "Dit betekend niet dat je hieruit moet kiezen, maar je kunt dit wel zien als inspiratie."
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
