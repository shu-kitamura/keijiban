param location string = resourceGroup().location

param subnetId string


// Container App Environment Definition
param environmentName string = 'my-container-app-env'

resource environment 'Microsoft.App/managedEnvironments@2025-02-02-preview' = {
  name: environmentName
  location: location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    vnetConfiguration: {
      internal: true
      infrastructureSubnetId: subnetId
    }
    workloadProfiles: [
      {
        workloadProfileType: 'Consumption'
        name: 'Consumption'
        enableFips: false
      }
    ]
    publicNetworkAccess: 'Disabled'
  }
}
