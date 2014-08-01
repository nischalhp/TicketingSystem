import java.sql.Connection;
import java.sql.PreparedStatement;

public class FormValidation {

	public boolean validate_data(String vehicle_type, String toll_type,
			String date, String price, String vehicle_no) throws Exception {

		Boolean flag = false;
		Connection conn = null;

		if (vehicle_type.trim().isEmpty() || toll_type.trim().isEmpty()
				|| date.trim().isEmpty() || price.trim().isEmpty()
				|| vehicle_no.trim().isEmpty()) {

			throw new Exception("Input Data has nulls");

		} else {

			try {
				DBConnector dbObj = new DBConnector();
				conn = dbObj.getConnection();
				PreparedStatement insertStmt = conn
						.prepareStatement("INSERT INTO transactions(vehicle_type,toll_type,timestamp,price,vehicle_no values (?,?,?,?,?)");
				int parameterPlaceHolder = 1;
				insertStmt.setString(parameterPlaceHolder++, vehicle_type);
				insertStmt.setString(parameterPlaceHolder++, toll_type);
				insertStmt.setString(parameterPlaceHolder++, date);
				insertStmt.setString(parameterPlaceHolder++, price);
				insertStmt.setString(parameterPlaceHolder++, vehicle_no);
				insertStmt.executeUpdate();
				flag = true;
			} catch (Exception e) {
				System.out.println("Exception while inserting data");
				e.printStackTrace();
			} finally {
				conn.close();
			}
		}

		return flag;
	}
}
