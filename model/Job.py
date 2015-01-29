'''
Created on Jan 24, 2015
@status: basic model for a Job 
@author: Cody Henrichsen
'''
class Job:
    
    
    def __init__(self, jobname, salary, jobURL):
        """
        self.metroClose is if the job location is near a Metro stop.
        self.collateral is if the job is subject to collateral limitations.
        self.collateralRestrictions are the restrictions associated with the job.
        self.paroleVisitable is if the job is easy to visit by a parole officer.
        self.worksWithChildCare is whether the job is child care friendly
        self.shift is the type of shift (day, night, swing, grave)
        
        Args:
            jobname (str): The name of the job
            salary (int): Salary for the job
            jobURL (str): URL for the job posting
        
        """
        self.jobName = jobname
        self.company = ""
        self.jobLocation = ""
        
        self.salary = salary
        self.appURL = jobURL
        
        self.jobTypes = {}
        
        
        self.shift = ""
        self.collateral = False
        self.collateralRestrictions = []
        self.metroClose = False
        self.paroleVisitable = False
        self.worksWithChildCare = False
        self.setJobTypes()
      
    '''
    Sets all basic job types to false. Change these values as needed for the job.
    '''  
    def setJobTypes(self):    
        self.jobTypes["Accounting"] = False    
        self.jobTypes["Administrative"] = False    
        self.jobTypes["Banking"] = False    
        self.jobTypes["Construction"] = False    
        self.jobTypes["Business"] = False        
        self.jobTypes["Creative"] = False        
        self.jobTypes["CustomerSupport"] = False        
        self.jobTypes["Editorial"] = False        
        self.jobTypes["Education"] = False        
        self.jobTypes["Engineering"] = False        
        self.jobTypes["Hospitality"] = False        
        self.jobTypes["HumanResources"] = False        
        self.jobTypes["Software"] = False        
        self.jobTypes["Maintenance"] = False        
        self.jobTypes["Legal"] = False        
        self.jobTypes["Logistics"] = False       
        self.jobTypes["Manufacturing"] = False      
        self.jobTypes["Marketing"] = False        
        self.jobTypes["Medical"] = False        
        self.jobTypes["Other"] = False    
        self.jobTypes["Project"] = False    
        self.jobTypes["Government"] = False     
        self.jobTypes["NonProfit"] = False    
        self.jobTypes["Sales"] = False    
        self.jobTypes["Security"] = False    
