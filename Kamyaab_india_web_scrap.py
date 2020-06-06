
#Update below imports
from flask import render_template,request,jsonify
import requests
import json
import time
from urllib3.exceptions import InsecureRequestWarning
from flask_cors import CORS

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

app = Flask( __name__, static_url_path='' )

port = int( os.getenv( 'PORT', 8000 ) ) 
CORS(app) 

@app.route('/api/getJobs/',methods=['GET'])
def fetch_jobs_from_naukri():
    print('-' * 100)
    print('\nDont worry chap! I am watching you..\n')
    job_keyword = request.args.get('jobKeyWord')
    print('Hold on creating URL using passed keyword -> ' + job_keyword)
    URL = 'https://www.naukri.com/jobapi/v3/search?noOfResults=100&urlType=search_by_keyword&searchType=adv&keyword=' + job_keyword + '&k=' + job_keyword + '&seoKey=' + job_keyword + '-jobs&src=jobsearchDesk&latLong='
    print('\nBrilliant URL created -> ' + URL)
    print('\nPreparing to send a request...\n')
    response = requests.get(URL,verify=False,headers={'appid':'109','systemid':'109'})
    print('Ahoy! got something from the requested URL\n')
    print('Now passing it to JSON..\n')
    json_result = json.loads(response.text)
    print('JSON parsing and loading is done..\n')
    extracted_data = json_result['jobDetails']
    print('Sorry now i am dead tired sleeping for 1 sec.\n')
    time.sleep(1)
    print('-' * 100)
    return jsonify(extracted_data)

	
if __name__ == "__main__":
    
    #app.run(debug=True)
    app.run( host='0.0.0.0', port=port, debug=True) 