You are here: Learn about Citrix App Layering [UnideskVersion Layering 4.0.8] > Connectors > Connector essentials
#Connector essentials
In this article:
[ What are Connectors?](#What)[        ](#What)
[ What are Connector Configurations?](#What2)[        ](#What2)
[ What Connector Configurations do I need?](#Selectin)[        ](#Selectin)
[ How and when to add a new Connector Configuration](#Before)[        ](#Before)
##What are Connectors?<a name="What"></a>
Connectors are the interfaces to environments where layers are created and images are published. The type of platform connector determines the information required to create a specific Connector Configuration.
##What are Connector Configurations?<a name="What2"></a>
A Connector Configuration is a stored set of values for connecting to a storage location in your environment. A configuration typically includes credentials for authentication, a storage location, and any other information required to interface with the environment where you will be creating layers or publishing images. You can create multiple Connector Configurations, each configured to access a unique location in your environment. 
##What Connector Configurations do I need?<a name="Selectin"></a>
###Connector Configurations for importing an OS###to create an OS###Layer 
When you create an OSLayer, you need a Connector Configuration to give Unidesk access to the location of the OSimage that you want to use for your OSLayer. 
###Connector Configurations for creating and updating App Layers, and adding Versions to OS Layers
When creating or updating an App Layer, or adding Versions to an OSLayer, you need a Connector Configuration for the location in your environment where you will package the Layer. You can create as many configurations as you need, for example, if you have more than one storage location in the environment.
###Connector Configurations for publishing Layered Images
Publishing Layered Images will require different Connector Configurations than the ones you use for creating Layers, if, for example, you publish Layered Images to a variety of storage locations near the users being served. For example, you can prepare your Layers for a server farm in vSphere, and publish Layered Images to Citrix PVS for streaming to servers in vSphere. Or, you can publish Layered Images to more than one storage location in the same environment, each requiring a different Connector Configuration. Each location is likely to require different credentials.
##How and when to add a new Connector Configuration<a name="Before"></a>
If this is your first time using Unidesk, you will need to add one or more Connector Configurations in the process of adding Layers and publishing Layered Images. In the Unidesk Management Console, the wizards for Creating Layers, Adding Versions, and Publishing Layered Images each include a page for selecting and creating Connector Configurations. For details, click [Add a Connector Configuration](connector_config_create_co4)[. and select a platform.](connector_config_create_co4)
