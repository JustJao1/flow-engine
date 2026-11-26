import unittest
from api.workspace import process

class WorkspaceTest(unittest.TestCase):
    def setUp(self):self.snapshot=None
    def request(self,action,data=None):
        r=process({'project':'flow','action':action,'data':data or {},'snapshot':self.snapshot})
        self.snapshot=r['snapshot']
        return r['result']
    def test_primary_flow(self):
        state=self.request('state')
        flow=state['flows'][0]
        high=self.request('run',{'id':flow['id'],'input':{'total':150}})
        low=self.request('run',{'id':flow['id'],'input':{'total':50}})
        self.assertEqual(high['output']['status'],'prioritário')
        self.assertEqual(low['output']['status'],'normal')
    def test_reject_other_project(self):
        with self.assertRaises(ValueError):
            process({'project':'affiliate','action':'state','data':{}})
