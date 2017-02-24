You are here: Learn about Citrix App Layering [UnideskVersion Layering 4.0.8] > Set up > Unidesk Glossary
#Unidesk Glossary
This section contains terminology across all platforms and operating systems that Unidesk supports. Note that some of the terms may not pertain to your specific environment.
A
A virtual disk containing one or more applications that you can use in any number of Layered Images. When publishing a Layered Image, you can combine an App Layer with the OS Layer used to create it, other App Layers, and a Platform Layer.

C
Connectors are the interfaces to environments where layers are created and images are published. The type of platform connector determines the information required to create a specific Connector Configuration.

A stored set of values for connecting to a specific environment. A configuration typically includes credentials for authentication, a storage location, and any other information required to interface with the environment where you will be creating layers or publishing images.

D
A connection to a base Distinguished Name in a directory service (such as Microsoft Active Directory). Adding a Directory Junction to the local tree allows you to assign Administrator privileges to users that are defined in the directory service instead of in the Unidesk Management Console.

A hierarchical repository of information about users, devices and services on a network server. Microsoft Active Directory and LDAP are examples of directory services.

A user whose attributes reside in a remote directory service but is also visible in the Unidesk environment through the use of a directory junction. You can assign Unidesk Administrator privileges to users.

A view of data in a hierarchical, tree-like structure. The Unidesk directory tree contains entries for users, groups, containers, and Virtual Machines. You can extend this view by adding connections to a remote directory service, such as Active Directory.

E
A Unidesk App Layer that the Unidesk administrator can deliver based on user entitlements when users log onto sessions or standalone desktops. Elastic Layers allow administrators to give each user his/her own unique set of applications, on top of the base Layered Image used across sessions (in the case of session hosts), and across floating pools/shared groups (in the case of desktops). This can drastically reduce the number of base Layered Images that administrators need to maintain.

A virtual appliance that coordinates communication in the Unidesk environment, and  hosts the Unidesk Management Console (UMC), the administrator interface for the Unidesk environment. The ELM also manages copies of all Layers.

I
An Image Template saves the OSLayer, App Layer, and Platform Layer assignments you have chosen for a Layered Image, allowing you to use any combination of layers to provision any number of servers.

L
A Unidesk layer captures a Windows Operating System, a Windows Application, or the configuration settings and tools required for Images to run on a particular platform in a virtual disk that can be combined with other layers to create a Layered Image. Layers are created from a simple install of the application or operating system. You can select any combination of Layers for each Layered Image. You can reuse the same layers in any combination to provision a variety of servers.

A bootable image composited from an OS Layer, a Platform Layer, and any number of App Layers. Layered Image(s) are published using Image Templates where you save your layer selections for a particular use, usually provisioning servers in a specific silo.

The Web-based management console that runs on the Enterprise Layer Manager (ELM). This console allows you to manage the App Layering components in your environment. You can use is to create Layers, publish Layered Images, and manage system settings.

A Layer repository where the ELM creates, composites, and stores Layers and Layered Images. Local storage is used for temporary files during the creation of Layers and Layered Images, and for persistent files, for example, Layers and Image Templates. Administrators can define the Network File Share location that will be used for Elastic Layers in the UMC’s System and Settings.

O
The virtual disk containing the Operating System that is imported to create an OS layer. To prepare the OS disk you will install and configure an Operating System on a virtual machine and install the Unidesk tools. The OS Disk is the virtual disk where the Operating System was installed.

A virtual disk containing the operating system. You can use an OS Layer with any compatible App Layers in any number of Layered Images. You can create a new Version of the OS Layer for every patch you need to roll out, and continue deploying every and all versions of the layer as you add patches.

The Operating System (OS) Machine is a virtual machine that you create from which you can generate an OS Disk and an OS Layer.

P
A bootable virtual disk used to create a Packaging Machine needed for creating or updating a Layer.  The Packaging Disk always includes your OS Layer and may also include selected Application and Platform Layers.

A virtual machine that acts as a staging area for the creation of App Layers, App Layer Versions, and OS Layer Versions. The Packaging Machine is booted from a Packaging Disk using the credentials and location specified in the selected Connector Configuration.

A layer that includes configuration settings, tools, and other software required for Images to run on a particular platform. For example, a platform layer for vSphere would include vmTools. Platform Layers also remove leftover software from other platforms from your image.

An application that is required when installing another application for a new Application Layer or Layer Version. For example, you would select your Microsoft Office App Layer as a Prerequisite Layer when installing a Microsoft Office plugin in a separate App Layer. Or, you would select your Java App Layer as a Prerequisite Layer when creating a Layer for an application that requires Java.

S
A Citrix technology that allows different users logged into the same Session Host to be assigned different versions of the same Elastic Layer, and ensures that those Layer versions do not conflict.


