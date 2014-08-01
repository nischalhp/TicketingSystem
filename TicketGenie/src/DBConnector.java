import java.sql.Connection;
import java.sql.DriverManager;

public class DBConnector {

	public static final String host = "127.0.0.1";
	public static final String port = "5433";
	public static final String username = "postgres";
	public static final String password = "tiger";
	public static final String db = "postgres";

	public Connection getConnection() {
		Connection c = null;
		try {
			Class.forName("org.postgresql.Driver");
			String connString = "jdbc:postgresql://" + host + ":" + port + "/"
					+ db;
			c = DriverManager.getConnection(connString, username, password);
		} catch (Exception e) {
			e.printStackTrace();
			System.err.println(e.getClass().getName() + ": " + e.getMessage());
			System.exit(0);
		}
		System.out.println("Opened database successfully");
		return c;
	}

	public static void main(String args[]) {

		DBConnector obj = new DBConnector();
		Connection c = obj.getConnection();

	}

}
