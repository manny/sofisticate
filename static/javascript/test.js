document.addEventListener('DOMContentLoaded', function(){
	var button = document.getElementById('sofisticate');
	console.log(message);
	button.addEventListener('click', function(){
		FB.login(function(){
			FB.getLoginStatus(function response() {
				if(response.status == 'connected'){			
					FB.api('me/feed', 'post',{message: 'This is a test!'});
				}
		}, {scope: 'publish_actions'});	
	});
});
});
