import requests
import os
import boto3
import time
from botocore import exceptions

API_ENDPOINT = "https://icanhazip.com/" if "API_ENDPOINT" not in os.environ else os.environ["API_ENDPOINT"]
SLEEP_MIN = 15 if "SLEEP_MIN" not in os.environ else int(os.environ["SLEEP_MIN"])
HOSTED_ZONE_ID = os.environ["HOSTED_ZONE_ID"]
TTL = 300 if "TTL" not in os.environ else int(os.environ["TTL"])
DOMAIN_NAME = os.environ["DOMAIN_NAME"]

client = boto3.client("route53")


def main():
    last_ip = "0.0.0.0"

    while True:
        r = requests.get(API_ENDPOINT)
        if r.status_code == 200:
            if r.text != last_ip:
                last_ip = r.text.strip()
                print("Updating to " + last_ip)
                request = {
                    'Comment': 'Updated via HomeDyDns',
                    'Changes': [
                        {
                            'Action': 'UPSERT',
                            'ResourceRecordSet': {
                                'Name': DOMAIN_NAME,
                                'Type': 'A',
                                'TTL': TTL,
                                'ResourceRecords': [
                                    {
                                        'Value': last_ip
                                    },
                                ]
                            }
                        },
                    ]
                }
                try:
                    client.change_resource_record_sets(
                        HostedZoneId=HOSTED_ZONE_ID,
                        ChangeBatch=request
                    )
                except exceptions.ClientError:
                    # If the record doesnt exist, try creating it instead.
                    request["Changes"][0]["Action"] = "CREATE"
                    client.change_resource_record_sets(
                        HostedZoneId=HOSTED_ZONE_ID,
                        ChangeBatch=request
                    )
                print("Success!")
        else:
            print("Bad Request!")

        print(f"Sleeping for {SLEEP_MIN} minutes.")
        time.sleep(SLEEP_MIN * 60)


if __name__ == "__main__":
    main()
