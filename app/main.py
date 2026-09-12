import json,io
from fastapi import FastAPI,UploadFile,File,Depends,HTTPException
from sqlalchemy.orm import Session
from .db import db,Job
from .extractor import extract
app=FastAPI(title='Document Processing Service')
ALLOWED={'.txt','.csv'}
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/documents')
async def upload(file:UploadFile=File(...),s:Session=Depends(db)):
    if not any(file.filename.lower().endswith(x) for x in ALLOWED): raise HTTPException(400,'Only .txt and .csv are supported in this demo')
    data=await file.read();
    if len(data)>2_000_000: raise HTTPException(413,'File too large')
    try: text=data.decode('utf-8')
    except UnicodeDecodeError: raise HTTPException(400,'File must be UTF-8 text')
    job=Job(filename=file.filename,status='queued'); s.add(job); s.commit(); s.refresh(job)
    # Local worker simulation: production version can hand this job to Celery/RQ.
    try:
      job.status='processing'; job.extracted_json=json.dumps(extract(text)); job.status='completed'
    except Exception as e: job.status='failed'; job.error=str(e)
    s.commit(); return {'job_id':job.id,'status':job.status}
@app.get('/documents/{job_id}')
def result(job_id:int,s:Session=Depends(db)):
    j=s.get(Job,job_id)
    if not j: raise HTTPException(404,'Job not found')
    return {'id':j.id,'filename':j.filename,'status':j.status,'result':json.loads(j.extracted_json) if j.extracted_json else None,'error':j.error}
