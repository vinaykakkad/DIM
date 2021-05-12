document.addEventListener('DOMContentLoaded', ()=> {
    const togglePassword = document.querySelector('.eye-toggler');
    const password = document.querySelector('#password');
    	
    togglePassword.onclick = ()=> {
		if(password.getAttribute('type') === 'password') {
			password.setAttribute('type', 'text');
			document.querySelector('.eye-toggler svg').classList.remove('fa-eye');
			document.querySelector('.eye-toggler svg').classList.add('fa-eye-slash');
		}
		else {
			password.setAttribute('type', 'password');
			document.querySelector('.eye-toggler svg').classList.remove('fa-eye-slash');
			document.querySelector('.eye-toggler svg').classList.add('fa-eye');
		}
    };
});