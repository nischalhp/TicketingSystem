
import java.net.InetAddress;

import org.restlet.Component;
import org.restlet.data.Protocol;


public class TicketGenieServer {
	public static void main(String[] args) throws Exception
	{
		
/*		DbConnector dbConnector = new DbConnector(); 
		boolean dbConnectionSuccessStatus = dbConnector.testDBConnection();
		
		if (dbConnectionSuccessStatus == false)
		{
			System.err.println("FATAL. Unable to connect to DB. Contact Admin");
			return;
		}
		
		else
		{
			System.out.println("DB Connection successful");
		}*/
		
		Component component = new Component();
		component.getServers().add(Protocol.HTTP,8182);
		component.getDefaultHost().attach("/ticketGenie",new TicketGenieRouter());
		component.start();
		
		InetAddress ip;
		ip = InetAddress.getLocalHost();
		

		System.out.println("Server started at: "+ip.getHostAddress());
		
	}
}