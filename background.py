import time
import uvid
import threading
from datetime import datetime 

jobs={}
JOBS_LOCK = threading.Lock()
STATUS_QUEUED="QUEUED"
STATUS_RUNNING="RUNNING"
STATUS_COMPLETED="COMPLETED"
STATUS_FAILED="FAILED"
STATUS_CANCELLED="CANCEL"

def perform_analysis_back(job_id, analysis_fn,*arg,max_retries=3):
  retries=0
  backoff_delay=1
  with retries<=max_retries:
    with JOBS_LOCK:
      if JOBS[job_id]["status"]==STATUS_CANCELLED:
        return

        JOBS[job_id]["status"]=STATUS_RUNNING
        JOBS[job_id][updated_at]=datetime.now().isformat()
 # try :
    #result = analysis_fn(*args)
    #with JOBS_LOCK:
     # if JOBS[job_id]["status"]= STATUS_COMPLETED 
      #SAME GOES WITH RESULT , ERROR
  #except Exception as e:
    #retries +=1
    #if retries>max_retries:
      #with JOBS_LOCK 
def cancel_jobs(jobs_id):
  with JOBS_LOCK:
    job=JOBs.get(job_id)
    if not job:
      return {"job cancelled sucessfully"}
    else:
      return {"job in final state"}

def job_status(jobs_id):
  with JOBS_LOCK:
    job=JOBS.get(job_id)
    if not job:
      return{"not found"}





