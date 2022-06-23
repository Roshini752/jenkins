#Source: easyaslinux.com
#Python2 and 3 compatible

import requests

jenkins_job_name = "job1"              
jenkins_url = "http://localhost:8080"
jenkins_user = "Roshini"
jenkins_pwd = "11015644aafa98a84eac7a74de24277973"
buildWithParameters = True
string = input("Enter the string that you want search search : ")
jenkins_params = {'token': 'bwp752', 
                  'result2':'success',
                  'result1': 'success',
                  'string' : string}

try:
    auth= (jenkins_user, jenkins_pwd)
    
    result= requests.get("{0}/crumbIssuer/api/json".format(jenkins_url),auth = auth)

    if str(result.status_code) == "200":

        if buildWithParameters:
            data = requests.get("{0}/job/{1}/buildWithParameters".
                            format(jenkins_url,jenkins_job_name),auth=auth,
                            params=jenkins_params,
                        headers={'content-type': 'application/json','Jenkins-Crumb':
                                 result.json()['crumb']})
        else:
            data = requests.get("{0}/job/{1}/build".format(jenkins_url,jenkins_job_name),auth=auth,params=jenkins_params)
        if str(data.status_code) == "201":
            print ("Jenkins job is triggered")
        else:
            print ("Failed to trigger the Jenkins job")
		    

    else:
        print("Couldn't fetch Jenkins-Crumb")
        raise 
	

except Exception as e:
    print ("Failed triggering the Jenkins job")
    print ("Error: " + str(e))
