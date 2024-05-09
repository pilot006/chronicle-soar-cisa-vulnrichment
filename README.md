# Unofficial CISA Vulnrichment Enrichment Action for Gogole SecOps/Chronicle SOAR


## Overview
On 5/18/24 [CISA announced their release of Vulnrichment](https://www.linkedin.com/posts/cisagov_we-understand-that-timely-and-accurate-information-activity-7193995615737901056-8PNq?utm_source=share&utm_medium=member_desktop), enabling security team with up-to-date CVE data to use for enrichment. This repo provide an action for Chronicle SOAR/Google SecOps customers to leverage this new enrichment withing playbooks

## Installation
1. Navigate to Releases in this repo and download the .zip package.
2. In Chronicle SOAR/Security Operations, install the integration by opening the IDE and importing the package.
3. Set up an integration via Integrations. No additional configuration is required

## Example
Here's the example JSON output that will be available in playbooks upon successful enrichment.

![Vulnrichment](vulnrichment-output.png?raw=true)
