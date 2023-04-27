using System;
using System.Runtime.InteropServices;

namespace Client
{
    class CredentialPrompt
    {
        //importing the credui.dll, and the 'CredUIPromptForCredentials' method (see the extern part)
        [DllImport("credui.dll", CharSet = CharSet.Unicode)]
        private static extern bool CredUIPromptForCredentials(
            //refrencing the CREDUI_INFO struct
            ref CREDUI_INFO pUiInfo,
            string pszTargetName,
            IntPtr pContext,
            int dwAuthError,
            IntPtr pszUserName,
            int ulUserNameMaxChars,
            //memory address where the password is stored
            IntPtr pszPassword,
            int ulPasswordMaxChars,
            ref bool pfSave,
            CREDUI_FLAGS dwFlags);

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
        private struct CREDUI_INFO
        {
            public int cbSize;
            public IntPtr hwndParent;
            public string pszMessageText;
            public string pszCaptionText;
            public IntPtr hbmBanner;
        }

        [Flags]
        private enum CREDUI_FLAGS
        {
            INCORRECT_PASSWORD = 0x1,
            DO_NOT_PERSIST = 0x2,
            REQUEST_ADMINISTRATOR = 0x4,
            EXCLUDE_CERTIFICATES = 0x8,
            REQUIRE_CERTIFICATE = 0x10,
            SHOW_SAVE_CHECK_BOX = 0x40,
            ALWAYS_SHOW_UI = 0x80,
            REQUIRE_SMARTCARD = 0x100,
            PASSWORD_ONLY_OK = 0x200,
            VALIDATE_USERNAME = 0x400,
            COMPLETE_USERNAME = 0x800,
            PERSIST = 0x1000,
            SERVER_CREDENTIAL = 0x4000,
            EXPECT_CONFIRMATION = 0x20000,
            GENERIC_CREDENTIALS = 0x40000,
            USERNAME_TARGET_CREDENTIALS = 0x80000,
            KEEP_USERNAME = 0x100000,
        }

        public string[] Prompt(string message, string applicationName)
        {
            CREDUI_INFO info = new CREDUI_INFO();
            info.cbSize = Marshal.SizeOf(info);
            info.pszCaptionText = applicationName;
            info.pszMessageText = message; //"Please enter your username and password.";

            string targetName = "target-name"; // replace with your target name

            IntPtr usernamePtr = Marshal.StringToCoTaskMemUni(new string(' ', 256));
            IntPtr passwordPtr = Marshal.StringToCoTaskMemUni(new string(' ', 256));
            bool save = false;

            bool result = CredUIPromptForCredentials(
                ref info,
                targetName,
                IntPtr.Zero,
                0,
                usernamePtr,
                256,
                passwordPtr,
                256,
                ref save,
                CREDUI_FLAGS.GENERIC_CREDENTIALS | CREDUI_FLAGS.ALWAYS_SHOW_UI);

            // if (result)
            //{
            Console.Write($"Result: {result}\n");

            string username = Marshal.PtrToStringUni(usernamePtr);
            string password = Marshal.PtrToStringUni(passwordPtr);
            //Console.WriteLine($"Username: {username}");
            //Console.WriteLine($"Password: {password}");

            //}

            Marshal.ZeroFreeCoTaskMemUnicode(usernamePtr);
            Marshal.ZeroFreeCoTaskMemUnicode(passwordPtr);

            string[] credentialArray = { username, password };

            return credentialArray;

        }
    }
}
