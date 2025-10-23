param location string
param vnetName string
param subnetName string

resource virtualNetwork 'Microsoft.Network/virtualNetworks@2021-05-01' = {
  name: vnetName
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        '10.0.0.0/16'
      ]
    }
  }

  resource subnet1 'subnets' = {
    name: subnetName
    properties: {
      addressPrefix: '10.0.0.0/24'
      delegations: [
        {
          name: 'Microsoft.App.environments'
          id: '${virtualNetwork.id}/delegations/Microsoft.App.environments'
          properties: {
            serviceName: 'Microsoft.App/environments'
          }
          type: 'Microsoft.Network/virtualNetworks/subnets/delegations'
        }
      ]
    }
  }
}

output subnetId string = virtualNetwork::subnet1.id
