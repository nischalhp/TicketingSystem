import org.restlet.Application;
import org.restlet.Restlet;
import org.restlet.data.Reference;
import org.restlet.resource.Directory;
import org.restlet.routing.Router;

public class TicketGenieRouter extends Application {
	
	public static final String ROOT_URI = "file:///home/rd/code/TicketingSystem/TicketGenie/static/";

	@Override
	public Restlet createInboundRoot(){

		
	Router router = new Router(getContext());

    // main page	
	router.attach("/",new Directory(getContext(),new Reference(ROOT_URI,"./index.html")));
	
	return router;


	}
}
