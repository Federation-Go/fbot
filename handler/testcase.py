import json
import logging
import sys
import os.path

def parse(t):
    try:
        t=json.load(open(t,'r'))
    except ValueError:
        t=os.path.basename(t)
        logging.error("Testcase %s syntax invalid" % os.path.basename(t)) 
        sys.exit(-1)
    return t

class Config(object):
    def __init__(self,configs):
        self.__dict__.update(configs)

class TestResult(object):
    def __init__(self,result,testcase=None,name=None,reason=None):
        self.result=result
        self.test_name=name
        self.teastcase=testcase
        self.reason=reason
    def __str__(self):
        return "result: %s, reason: %s"%(self.result,self.reason)

class Testcase(object):
    def __init__(self,env,testcase):
        result=parse(testcase)
        self.test_file=os.path.basename(testcase)
        self.env=env
        self.configs=Config(result['configs'])
        self.tests=result['tests']
        self.variables=result['variables']
    def run_test(self):
        model=__import__('model',globals(),locals(),['*'])
        for name,test in self.tests.iteritems():
            service=test['service']
            m=getattr(model,service,None)
            if not m:
                logging.error("Error in %s, unknown service %s" %(name,service))
                sys.exit(-1)
            action=test['action']
            handler=getattr(m.model,action,None)
            if not handler:
                logging.error("Error in %s, action %s is not supported"%(name,action))
                sys.exit(-1)
            args=test['args']
            try:
                for key in args:
                    args[key]=args[key]%self.variables
            except KeyError as e:
                logging.error("Error in %s, unknown variable %s" %(name,e.args[0]))
                sys.exit(-1)

            supported_type={"verify":(0,["response"]),"store":(1,["store"])}
            try:
                t=list(set(test['type'].strip().split(" ")))
                _cmp=lambda x,y:cmp(supported_type[x][0],supported_type[y][0])
                t=sorted(t,cmp=_cmp)
                # TODO Check for necessary field
            except KeyError as e:
                logging.error("Error in %s, type %s is not supported" %(name,e.args[0]))
                sys.exit(-1)
            env=self.configs.env
            pandora=self.env[env]
            response=handler(pandora,**args)
            for f in t:
                func=getattr(self,f)
                result=func(response,name,test)
                if not result.result:
                   return result 
    def verify(self,response,test_name,test):
        if not int(test['response'])==response.status_code:
            reason="verify failed, response %d, %d expected. response body is %s"%(response.status_code,int(test['response']),response.text)
            return TestResult(False,self.test_file,test_name,reason)
        return TestResult(True)
    def store(self,response,test_name,test):
        try:
            self.variables[test['store']]=response.text
        except:
            return TestResult(False,self.test_file,test_name,"store failed")
        return TestResult(True)
