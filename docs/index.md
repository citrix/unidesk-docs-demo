You are here: Learn about Citrix App Layering [UnideskVersion Layering 4.0.8] > Set up > Welcome to Unidesk 4
#Welcome to Citrix App Layering 4 
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#Applicat"> The ultimate in application management simplicity</a>                        </p>                        <p><a href="#Provision"> Provision servers in any environment</a>                        </p>                        <p><a href="#Provide"> Deliver applications with ease</a>                        </p>                        <p><a href="#Works"> A simple addition to your environment</a>                        </p>                        <p><a href="#Get"> Get started </a>                        </p>                    </td>                </tr>            </tbody>        </table>
##The ultimate in application management simplicity<a name="Applicat"></a>
Unidesk makes it easier to manage your Windows applications. Regardless of which hypervisor or provisioning service you use, Unidesk can help you manage your applications and operating systems. 
Unidesk separates the management of your Operating System and applications from your infrastructure. With Unidesk you can install each of your applications and operating system patches once, and use them as part of any image you deploy. You can publish Layered Images as open standard virtual disks usable in any environment. This allows you to maintain a single Windows installation, and a single copy of each application, that you use for all of your images across all of your virtual environments.
<ul>            <li>Unidesk wraps each of your applications in a Layer, and stores the Layers as virtual disks.</li>            <li>You can pull together any combination of these App Layers and an OS Layer as part of a Layered Image, and publish it to your target platform.</li>            <li>That means that you can install an application or an operating system once, and deploy it as part of any number of images.</li>        </ul>
##Provision servers in any environment<a name="Provision"></a>
Unidesk lets you to package any Windows app as a virtual disk Layer and deliver it, installation-free, to session hosts. With Unidesk Layering, you can:
<ul>            <li>Install and manage a single copy of your Windows OS and a single copy of each of your applications in Layers. </li>            <li>Select any combination of Layers to create Layered Images that are deployable as Session Hosts.</li>            <li>Deploy those Layered Images to virtual machine session hosts, making the applications available to users. </li>        </ul>
New applications, application updates, and Windows patches can be delivered to an entire RDSH farm with a single image update. 
##Deliver applications with ease<a name="Provide"></a>
Using the Unidesk Management Console, you can:
<ul>            <li>Layer Applications and deliver them as read-only virtual disks to session hosts. Layering is faster and easier than app virtualization and is compatible with more apps. Layers have the look and feel of a local installation and enable full application interoperability.</li>            <li>Layer a Windows OS and deliver it as a read-only virtual disk to all session hosts. Patch an OS layer once to update an entire RDSH server farm.</li>            <li>Maintain platform-independent OSand App Layers by creating Platform Layers to hold infrastructure-related software and settings. </li>            <li>Provision RDSH VMs. You can create custom RDSH virtual machines by assigning any combination of compatible OS and App layers in any order.</li>        </ul>
##A simple addition to your environment<a name="Works"></a>
The heart of the Unidesk deployment is the Enterprise Layer Manager (ELM), a virtual appliance that you deploy in your environment. The ELM hosts the Unidesk Management Console (UMC), a friendly interface where you create Unidesk Layers and assign the OSLayer and App Layers for each of your Layered Images.
###Unidesk Layers  
With Unidesk you can create an OSLayer or App Layer once, and use it to create any number of images. You can then update the OS or application by adding a new Version to the Layer for each patch or update that you apply.  
In App Layers you can deploy virtually any applications compatible with the OS. Each App Layer can include one or more applications. When it's time to upgrade an application, you can add a new version to the Layer for the latest update.
Platform Layers are designed to support your environment. A Platform Layer containing your hypervisor tools and settings makes it easy to create layers using VMs in your hypervisor environment. A Platform Layer containing your hypervisor, provisioning service, and connection broker software isolates App and OSLayers from the infrastructure where they will be published.
###Layered Images for provisioning Session Hosts
Image Templates are where you choose the Operating System and  Layer assignments for an Image. You can include OS and App layers in any number of Image Templates. Using an Image Template and a Platform Layer, you can publish a Layered Image to your provisioning service, hypervisor, or network file share .
You can publish Layered Images as virtual disks to any location to which the ELM has access, and use the disks to provision as many servers as you need. 
###Platform Connectors 
A Unidesk Platform Connector configured with the credentials for a specific location in your virtual environment, allows Unidesk to publish the Layered Images and provision servers in a specific location. 
##Compatibility
For compatibility details, see [ Supported Platforms](welcome_platform_support_co4)[. ](welcome_platform_support_co4)
##Get started <a name="Get"></a>
If you haven't yet started your free trial, you can find out how to install Unidesk [here](get_started_deploy_unidesk_elm_co4)[.](get_started_deploy_unidesk_elm_co4)


