from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import unix_now, convert_unixtime_to_datetime, output_handler
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED,EXECUTION_STATE_TIMEDOUT
import requests



@output_handler
def main():
    siemplify = SiemplifyAction()

    for entity in siemplify.target_entities:
        if entity.identifier[:3] == 'CVE':
            cve = entity.identifier
            siemplify.LOGGER.info('Found CVE: ' + cve)
            cve_chunk = cve.split('-')
            if(len(cve_chunk[2]) == 5):
                cid = cve_chunk[2][:2]
            else:
                cid = cve_chunk[2][:1]
            url = 'https://raw.githubusercontent.com/cisagov/vulnrichment/develop/' + cve_chunk[1]
            url = url + '/' + cid + 'xxx/' + cve + '.json'

            req = requests.get(url)
            if(req.status_code==200):
                result_value = "CVE Found"
                siemplify.result.add_result_json(req.text)
            else:
                result_value = "CVE Not Found"

            siemplify.LOGGER.info(req.text)

    status = EXECUTION_STATE_COMPLETED
    output_message = result_value


    siemplify.LOGGER.info("\n  status: {}\n  result_value: {}\n  output_message: {}".format(status,result_value, output_message))
    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    main()