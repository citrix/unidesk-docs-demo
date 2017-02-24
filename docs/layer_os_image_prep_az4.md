[OS Layer](layer_os_co4)
 > In Azure
#Prepare the OS Image (Azure)
This topic explains how to prepare an OS Image for the Unidesk environment. 
##Prepare a Windows 2012 R2 image (Session Host)<a name="Prep_2012_Host"></a>
This topic explains how to prepare an OS Image for Session Hosts in the Unidesk environment. 
Notes:
<ul>            <li>The OS Image should <i>not</i> be in a domain.</li>            <li>The OS Image should get its IP address from DHCP.</li>            <li>Ensure that the VM for your OSLayer is  MBR partitioned, rather than GPT partitioned. Otherwise, you will not be able to install the Unidesk OS Machine Tools. </li>        </ul>
###STEP 1: Set up a Windows Server 2012 R2 OS Image on a virtual machine 
<ol>            <li>In the Azure Portal, create a new VM from the "Windows Server Remote Desktop Session Host Windows Server 2012 R2" image (<b>New > Compute > Virtual Machine > From Gallery > Windows  Server Remote Desktop Session Host Windows Server 2012 R2</b>). </li>            <li>When specifying the Size of the virtual machine, we recommend you select A2 or larger.</li>            <li><b>Important:</b> When specifying the Cloud Service, select the same Cloud Service that contains your (Undefined variable: Unidesk.MA).</li>            <li>Select the same Storage Account that contains your appliances, unless your appliances are in <i>Premium Storage</i>, in which case you must use a <i>Standard Storage</i> group. </li>            <li>Log into the new VM, open a Windows PowerShell window, and run the <b>Enable-PSRemoting</b> command.</li>            <li>Restart the new VM.</li>        </ol>
###STEP 2: Apply Windows Updates
<ol>            <li>                <p>Apply all Windows Updates to the image so that it is at the most current Microsoft patch level and complete any reboot processes that Windows Updates may require.</p>            </li>        </ol>
###STEP 3: Copy the Unidesk Tools onto the OS Image 
<ol>            <li>Copy the Unidesk_OS_Machine_Tools RAR file onto the OS Image. You can find these tools in the Unidesk Download center.</li>            <li>Run the RAR file. This copies the tools to the C:windows\setup\scripts directory.</li>        </ol>
###STEP 4: Install the Unidesk tools onto the OS Image
<ol>            <li>                <p>In the c:\Windows\Setup\Scripts folder, run Unidesk setup_x64.exe.</p>            </li>            <li>                <p>The installation prompts for the location of the Management Appliance <i>IPaddress</i> and the location of the unattend.xml file (the default location is c:\windows\panther).</p>                <p>Note: Do <i>not</i> run the UnattendBuilder included with the tools. </p>            </li>        </ol>
###STEP 5: Run NGen
About Microsoft NGen operations
NGen is the Microsoft "Native Image Generator". It is part of the .NET system, and basically re-compiles .NET byte code into native images and constructs the registry entries to manage them.  Windows will decide when to run NGen, based on what is being installed and what Windows detects in the configuration.  When NGen is running, you must let it complete.  An interrupted NGen operation can leave you with non-functioning .NET assemblies or other problems in the .NET system.


Force an NGen operation to the foreground
Normally, NGen is a background operation and will pause if there is foreground activity.  Bringing the task into the foreground can help the task to complete as quickly as possible.
<ol>                    <li>                        <p>Open a command prompt as Administrator.</p>                    </li>                    <li>                        <p>Go to the Microsoft .NET Framework directory for the version currently in use:</p><pre>cd C:\Windows\Microsoft.NET\FrameworkNN\vX.X.XXXXX</pre>                    </li>                    <li>                        <p>Enter the NGen command to execute the queued items:</p><pre>ngen update /force</pre>                        <p>This brings the NGen task to the foreground in the command prompt, and lists the assemblies being compiled. </p>                        <li>                            <p>Ensure that all NGen processes have run to completion. Optionally, you can now shut down the OS Image VM.</p>                        </li>                    </li>                </ol>


Once you have completed these steps, you are ready to [create a Unidesk Operating System Layer](layer_os_version_az4)[.](layer_os_version_az4)


