import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.Hashtable;

public class Search {

	public ArrayList<Hashtable<String, String>> search_vehicle(String vehicle_no)
			throws Exception {

		ArrayList<Hashtable<String, String>> outputObj = new ArrayList<Hashtable<String, String>>();
		Connection conn = null;

		if (vehicle_no.trim().isEmpty()) {
			throw new Exception("input data has nulls");
		} else {
			try {
				DBConnector dbObj = new DBConnector();
				conn = dbObj.getConnection();
				String queryStmt = "select t2.vehicle_type,t2.toll_type,t1.timestamp,t1.price,t1.vehicle_no from (SELECT * FROM transactions where vehicle_no = '"
						+ vehicle_no
						+ "') as t1 inner join (select * from master_data) as t2 on t2.vehicle_type_id = t1.vehicle_type and t2.toll_type_id = t1.toll_type";
				PreparedStatement stmt = conn.prepareStatement(queryStmt);
				ResultSet rs = stmt.executeQuery();
				if (rs == null) {
					throw new Exception();
				} else {
					while (rs.next()) {
						Hashtable<String, String> hash = new Hashtable<String, String>();
						hash.put("vehicle_type", rs.getString(0));
						hash.put("toll_type", rs.getString(1));
						hash.put("time", rs.getString(2));
						hash.put("price", rs.getString(3));
						hash.put("vehicle_no", rs.getString(4));
						outputObj.add(hash);

					}
				}

			} catch (Exception e) {
				System.out
						.println("Something went wrong while retrieving data");
				e.printStackTrace();
			} finally {
				conn.close();
			}

		}

		return outputObj;
	}
}
