param location string = resourceGroup().location

module vnetModule 'vnet.bicep' = {
  name: 'vnetDeployment'
  params: {
    location: location
    vnetName: 'my-vnet'
    subnetName: 'my-subnet-1'
  }
}

module containerAppEnvModule 'containerApps.bicep' = {
  name: 'containerAppEnvDeployment'
  params: {
    location: location
    subnetId: vnetModule.outputs.subnetId
    environmentName: 'my-container-app-env'
  }
}
