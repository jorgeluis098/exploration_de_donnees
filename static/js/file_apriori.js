$(document).ready(function (){
	// $("#button_apriory").click(function(){
	// 	console.log("Hola bebe");
	// 	event.preventDefault();
	// });

	$("#button_apriory").click(function(event){
		event.preventDefault();
		var formData = new FormData($('#form_apriori')[0]);
		console.log("Hola bebe entre a leer el archivo");
		$.ajax({
			url: '/read_apriori',
			data: formData,
			type: 'POST',
			contentType: false,
			processData: false,
			success: function(response){
				console.log(response['key']);
				$('#table_values').html(response['key'])
				$('#table_apriori').DataTable();
				
			
			},
			error: function(error){
				console.log(error);
				event.preventDefault();
			}
		});    
	});


});


