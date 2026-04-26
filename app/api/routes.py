from fastapi import APIRouter, BackgroundTasks
from app.services.factory import get_ai_service
from app.models.schemas import AnalyzeRequest, AnalyzeResponse

router = APIRouter()
ai_service = get_ai_service()

# Temporary in-memory store (we’ll upgrade later)
results_store = {}

@router.post("/analyze")
async def analyze(payload: AnalyzeRequest, background_tasks: BackgroundTasks):
    job_id = str(len(results_store) + 1)

    background_tasks.add_task(process_task, job_id, payload.text)

    return {
        "job_id": job_id,
        "status": "processing"
    }


async def process_task(job_id: str, text: str):
    result = await ai_service.analyze(text)
    results_store[job_id] = result

@router.get("/result/{job_id}")
def get_result(job_id: str):
    if job_id not in results_store:
        return {"status": "processing"}
    
    return {
        "status": "completed",
        "data": results_store[job_id]
    }    