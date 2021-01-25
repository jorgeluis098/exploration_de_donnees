$(document).ready(function (){
	// $("#button_apriory").click(function(){
	// 	console.log("Hola bebe");
	// 	event.preventDefault();
	// });

	$("#button_k").click(function(event){
		event.preventDefault();
		var formData = new FormData($('#form_k')[0]);
		console.log("Hola bebe entre a leer el archivo");
		$.ajax({
			url: '/read_k_means',
			data: formData,
			type: 'POST',
			contentType: false,
			processData: false,
			success: function(response){
				console.log(response)
				$('#centroides').html(response['keyk'])	
				$('#cen').DataTable();			
			},
			error: function(error){
				console.log(error);
				event.preventDefault();
			}
		});    
	});


});


