using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Mail;
using System.Text;
using System.Threading.Tasks;

namespace Spambot
{
    class Program
    {
        static void Main(string[] args)
        {
            string whom = string.Join("", File.ReadAllLines("who.txt"));
            using (SmtpClient client = new SmtpClient("smtp.gmail.com", 587))
            {
                client.EnableSsl = true;
                client.DeliveryMethod = SmtpDeliveryMethod.Network;
                client.UseDefaultCredentials = false;
                client.Credentials = new System.Net.NetworkCredential("ohm.flare.007@gmail.com", "uqnedllaldckdlmf");
                MailMessage mm = new MailMessage();
                mm.To.Add(whom);
                mm.From = new MailAddress("ohm.flare.007@gmail.com");
                mm.Subject = "FEED YOUR DOG YOU FUCK";
                mm.Body = "FUCK YOU";
                client.Send(mm);
            }
        }
    }
}
