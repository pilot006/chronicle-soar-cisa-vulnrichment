from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import unix_now, convert_unixtime_to_datetime, output_handler
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED,EXECUTION_STATE_TIMEDOUT
import requests
import json


@output_handler
def main():
    siemplify = SiemplifyAction()


    r = requests.get('https://raw.githubusercontent.com/cisagov/vulnrichment/develop/2019/19xxx/CVE-2019-19751.json')

    if 'providerMetadata' in r.text:
        status = EXECUTION_STATE_COMPLETED
        output_message = "output message :"
        result_value = True
    else:
        output_message = f"Unable to connect to CISA Vulnrichment Github"
        status = EXECUTION_STATE_FAILED
        siemplify.LOGGER.error(output_message)
        result_value = False

    siemplify.LOGGER.info("\n  status: {}\n  result_value: {}\n  output_message: {}".format(status,result_value, output_message))
    siemplify.end(output_message, result_value, status)

if __name__ == "__main__":
    main()