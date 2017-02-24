[Publish Layered Images](layered_images_publish_co4)
 > Nutanix AHV
#Publish Layered Images (Nutanix AHV)
In this article:
<table>            <col></col>            <tbody>                <tr>                    <td>                        <p><a href="#Pre"> Prerequisites</a>                        </p>                        <p><a href="#Pub"> Publish a Layered Image</a>                        </p>                    </td>                </tr>            </tbody>        </table>
A Layered Image is a virtual machine that Unidesk has composited from the Layers and settings specified in an Image Template. You can publish one or more Layered Images to Nutanix AHV, and add each one to a collection, provisioning service, or other method for provisioning your systems.
##Prerequisites<a name="Pre"></a>
[ Create Image Templates (Nutanix AHV)](layered_images_create_template_ah4)[        ](layered_images_create_template_ah4)
##Publish a Layered Image<a name="Pub"></a>
<ol>            <li>                <p>In the Images module, select one or more Image Templates to publish.</p>            </li>            <li>                <p>From the Action menu, select <b>Publish Layered Image</b>.</p>            </li>            <li>                <p>On the Confirm and Complete page, select <b>Publish Layered Images</b>. For each template, this starts a task called, <i>Publishing Layered Image</i>. When each task completes, the task description provides the information you need to navigate to the image in your environment.</p>            </li>            <li>                <p>Use the information in the expanded Packaging Disk Task shown above to navigate to the location in Nutanix AHV where the Layered Image has been published.</p>            </li>            <li>                <p>In the Prism console, power on the Packaging Machine VM. This enables the Guest OS to run and execute any Layer scripts via Unidesk's kmssetup.cmd functionality. </p>                <p>You can use scripts  to perform important Layer-specific steps, for example, activating Microsoft Office, which may need to be done before the VM is used to create or update an MCS catalog. </p>                <p><i>Note:</i> You can execute Layer scripts  using Unidesk's kmssetup.cmd functionality, Unidesk's Run-once script support, or even manual execution. </p>            </li>            <li>Once the VM is in the desired state the VM must be shut down. If you need to shut it down manually, do so now. Otherwise, wait for the script you've configured to do so. </li>        </ol>
##Next Step
Use the image to provision Nutanix AHV servers.


