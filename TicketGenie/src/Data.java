import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.Hashtable;

public class Data {

	public ArrayList<Hashtable<String, Object>> get_data() {

		ArrayList<Hashtable<String, Object>> outputObj = new ArrayList<Hashtable<String, Object>>();
		Connection conn = null;

		try {
			DBConnector dbObj = new DBConnector();
			conn = dbObj.getConnection();
			String queryStmt = "SELECT vehicle_type,vehicle_type_id,toll_type,toll_type_id,price from master_data";
			PreparedStatement stmt = conn.prepareStatement(queryStmt);
			ResultSet rs = stmt.executeQuery();
			Hashtable<String, String> vehicle_hash = new Hashtable<String, String>();
			if (rs == null) {
				throw new Exception();
			} else {
				// iterating thru the rows
				while (rs.next()) {
					String vehicle_name = rs.getString(0);
					String id = rs.getString(1);
					String m = vehicle_hash.get(id);
					// checking if the particular vehicle has already been
					// considered or not
					if (m == null) {
						// if not considered then adding different types of
						// journey for the vehicle
						Hashtable<String, Object> vehicle_journey = new Hashtable<String, Object>();
						ArrayList<Hashtable<String, String>> journey_list = new ArrayList<Hashtable<String, String>>();
						vehicle_hash.put(id, "1");
						// now we have to re iterate thru all the types again so
						// using rs.first()
						if (rs.first()) {
							// going thru all the rows
							while (rs.next()) {

								Hashtable<String, String> journey_type = new Hashtable<String, String>();
								// checking if that row belongs to the type we
								// are looking for
								if (rs.getString(1) == id) {
									journey_type.put("toll_type",
											rs.getString(2));
									journey_type
											.put("toll_id", rs.getString(3));
									journey_type.put("price", rs.getString(4));
									journey_list.add(journey_type);
								}

							}// all the journey types for that vehicle add have
								// been added to the journey list
						}
						// now that we have the journey list completely , we
						// need to add it to vehicle name and type so that this
						// can be shown on UI
						vehicle_journey.put("vehicle_type", vehicle_name);
						vehicle_journey.put("vehicle_type_id", id);
						vehicle_journey.put("journey", journey_list);
						// adding output to outputobj which holds for all the vehicles
						outputObj.add(vehicle_journey);
					}// end of check for vehicle if already present

				}// end of iteration of all the rows

			}// rows exist
		} catch (Exception e) {
			System.out.println("Something went wrong while retrieving data");
			e.printStackTrace();

		}

		return outputObj;
	}
}
