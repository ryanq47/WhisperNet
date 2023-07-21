using System.Diagnostics;

namespace Client.Tools
{
    class PwshExec
    {
        string help = "HELPMENU\nrunViaExe: Spawns powershell.exe, and runs it. VERY High chance of getting flagged";

        //temp public for testing
        //get a better name for this, come up with a standard. Maybe actionMethod or similar
        public static string runViaExe(string command)
        /* runs a PS command - most likely will get flagged by edr, creats a PS subprocess on EACH CALL*/
        {
            

            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "powershell.exe";
            psi.Arguments = command;
            psi.RedirectStandardOutput = true;
            psi.UseShellExecute = false;

            // Create a new Process object and start it
            Process proc = new Process();
            proc.StartInfo = psi;
            proc.Start();

            // Read the output of the PowerShell command
            string output = proc.StandardOutput.ReadToEnd();

            // Display the output in the console
            Console.WriteLine(output);

            // Wait for the process to exit
            proc.WaitForExit();

            return output;
        }
    }

}