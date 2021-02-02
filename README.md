##### DevModeRuleTest

#####  project dependent package

     
         1,when you deploy the project , you may need the `requirements.txt`  which record the Pip package,
      and then running `pip install -r requirements.txt` it means install all package at you server 
         2,install Mysql to you server
         
        

#####  The first get userId 

    http://test-algo-ai-ats-project/seniorMiddleSchool  
    
    It's a post request , You should provide the following parameters
       courseId={} 
       classIds={}
       sectionId={}
       rate={}
    1,The interface will runing unlock/getSessionId/nextActivity/MvorDQUEST, and return userId
    2,the interface is an asynchronous task, it means the error parameters, wo could not get web response
 
#####  get SessionId
    
    http://test-algo-ai-ats-project/seniorMiddleSchool?userId=`xxxxxxxxxx`  
    
      It's a get request, for this it will check the userId the the first step got , 
    if right it will return {"userId":"xxx","SessionId":"xxx","rate":"xxx"}      
     
    
#####  get test log
       
        http://test-algo-ai-ats-project/getlog?userId=`xxxxxxxxxx`  
    
       It's a get request, if you can got sessionid , it means the test is success, and you can request the inforface
     to get the logs, the way of get test failure log is analogous , It can help you check the the output meet you expect

#####  get userInfo list

     http://test-algo-ai-ats-project/getuserlist  
    
       It's a get request, It return UserListInfo message , You can think of it as a user details list page.
      
             {
              "xfl-46841605666970": {
                "course_id": "332222494456829952", 
                "rate": 0.9, 
                "section_id": "332222494456829952", 
                "session_id": "332222494456829952"
              }, 
              "xfl-46841605667039": {
                "course_id": "332222528881433600", 
                "rate": 0.8, 
                "section_id": "332222528881433600", 
                "session_id": "332222528881433600"
              }
            }


##### TesterModeRuleTest

#####   seniorMiddleSchool math Test


        http://test-algo-ai-ats-project/getuserlist/seniorMiddleSchool
    
       It's will running a task job for running seniorMiddleSchool math , It will retuen user_id 
    
 
#### ai_ats_project utils 

   ##### abilitySqlCheck.py
     
        This is a tool toolkit , every online test regress we will make users 
      which  the script will select and check lo_status and finally_ability 
      
      '''(lo_status = "PASSED" and finally_ability < 0.7) 
			  or (lo_status = "FAILED" and finally_ability >= 0.7)'''
      
    
   ###### ale_lo_map_kafka.py
      
       we can use ale_lo_map_kafka script help us connect,sent and accept for kafka
       
   ###### checkLog.py
   
    He is used to detect file differences 
    
   ##### loger_.py
     
     Save test results to files
     
   
   ##### pressureMeasurement.py
    
        used locust package detection performance change
   