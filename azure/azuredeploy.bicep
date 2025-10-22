param location string = resourceGroup().location

var vnetName = 'my-vnet'
var subnetName = 'my-subnet-1'

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
    }
  }
}

output subnetResourceId string = virtualNetwork::subnet1.id
