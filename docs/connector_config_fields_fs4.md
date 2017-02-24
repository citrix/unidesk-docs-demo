[Add Connector Configuration](connector_config_create_co4)
 > Network file share
#Using the Network File Share Connector Configuration<a name="Azure_Platform_Connector_Fields"></a>
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#Network"> Network File Share location</a>                        </p>                        <p><a href="#How"> When to select the Network File Share as your Connector Configuration </a>                        </p>                    </td>                </tr>            </tbody>        </table>
When the Unidesk Enterprise Layer Manager is installed, you set up a network file share that you can then use as a Connector Configuration when creating layers and publishing Layered Images. This Connector Configuration contains the ELM's Network File Share credentials and location so you can deploy a Packaging Machine to the File Share when creating layers, or publishing Layered Images. 
Each Connector Configuration is set up to access a storage location via a specific account. For more about Connectors and Connector Configurations, see [About Connectors and Connector Configurations](connectors_about_co4)[. ](connectors_about_co4)
##Network File Share location<a name="Network"></a>
The name of the Network File Share Connector Configuration includes its location. Look for the Unidesk folder at the top level of the Network File Share. For details, see [ Set up a network file share](get_started_setup_fileshare_co4)[.](get_started_setup_fileshare_co4)
##When to select the Network File Share as your Connector Configuration <a name="How"></a>
When you publish Layered Images to a provisioning service for which we do not yet have a Connector, you can select the Network File Share Connector Configuration. You can then copy the Layered Image from the network file share to the correct location for provisioning servers. 

