$( function(){
	app = {


			//init is the property of the object app which is
			// represented as a function	
			init : function(){
				$("#price").val('');
				$("#vehicle_no").val('');

				$.ajax({
					type: "GET",
					url: "/data"
				}).success(function(response){
					app.data = JSON.parse(response);
					app.onDataSuccess(app.data.data);

				});
			},


			onDataSuccess: function(data){
				var lineItemsVehicle = '';
				$.each(data, function(index,vehicle){
					var lineItem = '<option value='+vehicle.vehicle_type_id+'>'+vehicle.vehicle_type+'</option>';
					lineItemsVehicle = lineItemsVehicle+lineItem;
				});
				$("#vehicle-type").html(lineItemsVehicle);
				$('#vehicle-type').trigger('change');
			},

			onClickVehicle: function(id){
				var lineItemsToll = '';
				$.each(app.data.data, function(index,vehicle){
					if (vehicle.vehicle_type_id == id){
						journey_array = vehicle.journey;
						$.each(journey_array,function(index,journey){
							var lineItem = '<option value='+journey.toll_id+'>'+journey.toll_type+'</option>';
							lineItemsToll = lineItemsToll+lineItem;
						})
					}
				});

				$("#toll-type").html(lineItemsToll);
				$("#toll-type").trigger('change');
			},

			onClickToll: function(vehicle_type_id,toll_type_id){
				var lineItemsToll = '';
				$.each(app.data.data, function(index,vehicle){
					if (vehicle.vehicle_type_id == vehicle_type_id){
						journey_array = vehicle.journey;
						$.each(journey_array,function(index,journey){
							if(journey.toll_id == toll_type_id){
								app.user_selection.price = journey.price;
								$("#price").val(journey.price);
							}
						})
					}
				});

			},

			insertData : function(vehicle_type,toll_type,time,price,vehicle_no){
				$.ajax({
					type: "POST",
					url: "/ticket/",
					data: {'vehicle_type':vehicle_type,'toll_type':toll_type
					,'time':time,'price':price,'vehicle_no':vehicle_no}
				}).success(function(response){
					$("#info").html('<div class="alert alert-info">Succesfully inserted data <button class="close" data-dismiss="alert">&times;</button></div>');
				}).error(function(response){
					resp = JSON.parse(response.responseText);
					$("#info").html('<div class="alert alert-error">'+resp.message+'<button class="close" data-dismiss="alert">&times;</button></div>');


				});



			},
			getData: function(vehicle_no){
				$.ajax({
					type: "GET",
					url: "/search/?vehicle_no="+vehicle_no
				}).success(function(response){
					var init_template = "<thead><tr> <th>Vehicle No</th> <th>Vehicle Type</th> <th>Toll Type</th> <th>Price</th> <th>Time</th> </tr> </thead>";
					$("#search-op").show();
					resp = JSON.parse(response);
					var template = '';
					$.each(resp.data,function(index,data){
						template = template + "<tr><td>"+data.vehicle_no+"</td><td>"+data.vehicle_type+"</td><td>"+data.toll_type+"</td><td>"+data.price+"</td><td>"+data.time+"</td>";
					})
					$("#search-op").html(init_template+template)
				}).error(function(response){
					resp = JSON.parse(response.responseText);
					$("#info").html('<div class="alert alert-error">'+resp.message+'<button class="close" data-dismiss="alert">&times;</button></div>');


				});



			}	

		}}());


$("#vehicle-type").on('change',function(event){
	app.user_selection = new Object();
	app.user_selection.vehicle_type_id = $(this).val();
	app.onClickVehicle(app.user_selection.vehicle_type_id);
});

$("#toll-type").on('change',function(event){
	app.user_selection.toll_type_id = $(this).val();
	app.onClickToll(app.user_selection.vehicle_type_id,app.user_selection.toll_type_id);
});

$("#submit-button").on('click',function(event){
	app.insertData(app.user_selection.vehicle_type_id,app.user_selection.toll_type_id,getTimeStamp(),
		app.user_selection.price,$("#vehicle_no").val());

});

$("#submit-button-search").on('click',function(event){
	app.getData($("#vehicle-search").val());

});
function getTimeStamp(){
	d = new Date();
	date = d.getDate();
	year = d.getFullYear();
	month = d.getMonth();
	month = month + 1;
	hour = d.getHours();
	min = d.getMinutes();
	sec = d.getSeconds(); 
	if (month < 10){
		month = '0'+month;
	}
	if (date < 10){
		date = '0'+date;
	}
	return year+'-'+month+'-'+date+' '+hour+':'+min+':'+sec;//+"-"+month+"-"date;
}



app.init();



