import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from suus_utils.llm_handler import AgentSuusDependencies, agent_suus

HOME_PAGE_NAME = "home-page"
GET_LLM_RESPONSE_FOR_SUUS_NAME = "get-llm-response-for-suus"


class HomePage(View):
    def get(self, request):
        return render(request, "home-page.html", {})
    

class GetLLMResponseForSuus(View):
    async def post(self, request):
        try:
            data = json.loads(request.body)
            result = await agent_suus.run(data["prompt"])

            poem_lines = [
                result.data.line_1,
                result.data.line_2,
                result.data.line_3,
                result.data.line_4
            ]

            print("RESULT", poem_lines)

            return JsonResponse(
                {
                    "status": "success",
                    "poem_lines": poem_lines
                },
                status=200
            )
        except Exception as e:
            return JsonResponse(
                {
                    "status": "error",
                    "message": str(e)
                },
                status=500
            )