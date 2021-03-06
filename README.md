# HomeDyDns
[![ci](https://github.com/Apollorion/HomeDyDNS/actions/workflows/ci.yaml/badge.svg)](https://github.com/Apollorion/HomeDyDNS/actions/workflows/ci.yaml) ![Version: 1.0.3](https://img.shields.io/badge/Version-1.0.3-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Dynamic DNS service that can run on a home kubernetes cluster to update route 53

# Installing

1. `helm repo add apollorion https://apollorion.github.io/helm/`
2. `helm repo update`
3. `helm install homedydns apollorion/homedynds --values ./my-awesome-values.yaml`

## Values

| Key | Required | Default | Description |
|-----|------|---------|-------------|
| appConfig.apiEndpoint | No | `"https://icanhazip.com/"` | API endpoint for getting your current IP address. This should ONLY return the ip address. |
| appConfig.domainName | Yes | | Domain to update in Route53 |
| appConfig.hostedZoneId | Yes | | Route53 hosted zone ID of the domain that is updated |
| appConfig.sleepMin | No | `15` | How many minutes to sleep between each IP check |
| appConfig.ttl | No | `300` | Domain TTL in Route53 |
| aws.accessKeyId | Yes | | AWS Access Key ID with permission to update domain in hosted zone |
| aws.region | Yes | | AWS default region for boto3 |
| aws.secretKeyId | Yes | | AWS Secret Key ID with permission to update domain in hosted zone |
| image.pullPolicy | No | `"IfNotPresent"` | K8s Image pull policy |
| image.repository | No | `"apollorion/homedydns"` | Image repository to pull the HomeDyDNS image from |
| image.tag | No | `"latest"` | Tag to use from the repository |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.7.0](https://github.com/norwoodj/helm-docs/releases/v1.7.0)