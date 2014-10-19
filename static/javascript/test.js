document.addEventListener('DOMContentLoaded', function(){
	var button = document.getElementById('sofisticate');
	button.addEventListener('click', function(){
		FB.login(function(){
			FB.getLoginStatus(function response() {
				if(response.status == 'connected'){			
					FB.api('me/feed', 'post', :w
{message: 'This is a test!'});
				}
			);
		}, {scope: 'publish_actions'});	
	});
});
