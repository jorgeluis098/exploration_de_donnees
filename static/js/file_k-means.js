$(document).ready(function (){


	$("#button_k").click(function(event){
		event.preventDefault();
		var formData = new FormData($('#form_k')[0]);
		$.ajax({
			url: '/read_k_means',
			data: formData,
			type: 'POST',
			contentType: false,
			processData: false,
			success: function(response){
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


