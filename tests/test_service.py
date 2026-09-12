from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_upload_and_extract():
 r=c.post('/documents',files={'file':('invoice.txt',b'Contact a@b.com total $12.50')}); assert r.status_code==200; jid=r.json()['job_id']; out=c.get(f'/documents/{jid}').json(); assert out['result']['email']=='a@b.com'
