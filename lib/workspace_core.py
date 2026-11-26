"""Loopback-only HTTP workspace. Maintainer: João Victor da Silva (JustJao1)."""
import argparse,base64,csv,datetime as dt,io,json,mimetypes,os,re,threading,time,urllib.parse,urllib.request
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from engine import *
ROOT=Path(__file__).resolve().parent

class Workspace:
    def __init__(self,path,port):self.store=Store(path);self.store.seed();self.port=port;self.stop=threading.Event();self.monitor_lock=threading.Lock();self.flow_lock=threading.Lock()
    def state(self,p):
        kinds=["flows","runs"]
        data={k:self.store.list(p,k) for k in kinds};
        return data
    def execute_flow(self,i,payload=None):
        with self.flow_lock:
            s=self.store;f=s.get('flow','flows',i);r=run_flow(f,f['input'] if payload is None else payload,self.port);r=s.put('flow','runs',{'flow':i,'name':f['name'],**r});s.trim('flow','runs',100)
            with s.lock:
                f=s.get('flow','flows',i);f['last_run']=time.time();s.put('flow','flows',f)
            return r
    def action(self,p,a,d):
        s=self.store;d=obj(d)
        if p=='flow':
            if a=='save':
                f={'name':text(d.get('name'),120),'input':obj(d.get('input',{})),'nodes':array(d.get('nodes')),'start':d.get('start'),'interval':whole(d.get('interval',0),0,86400),'enabled':bool(d.get('enabled'))};need(not f['enabled'] or f['interval']>=15,'Intervalo mínimo: 15 segundos.');validate_flow(f)
                if d.get('id'):prior=s.get(p,'flows',d['id']);f.update(id=prior['id'],created=prior['created'],last_run=prior.get('last_run',0))
                return s.put(p,'flows',f)
            if a=='run':return self.execute_flow(d['id'],d.get('input'))
            if a=='delete':s.remove(p,'flows',d['id']);return {'ok':True}
        raise ValueError('Operação desconhecida.')
