# HomeDyDns

Dynamic DNS service that can run on a home kubernetes cluster to update route 53

# Installing

1. `helm repo add apollorion https://apollorion.github.io/helm/`
2. `helm repo update`
3. `helm install homedydns apollorion/homedynds --values ./my-awesome-values.yaml`

See the values in `chart/homedydns/values.yaml`