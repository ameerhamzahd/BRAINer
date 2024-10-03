const loginWrapper = document.querySelector('.login-wrapper');
const registrationWrapper = document.querySelector('.registration-wrapper');
const loginLink = document.querySelector( '.login-link' );
const registerLink = document.querySelector( '.register-link' );
const Login = document.querySelector( '.Log-in' );
const register = document.querySelector( '.Register' );
const iconClose = document.querySelector( '.icon-close' );

registerLink.addEventListener('click', () => {
    loginWrapper.classList.remove('active');
    registrationWrapper.classList.add('active');
});

loginLink.addEventListener('click', () => {
    registrationWrapper.classList.remove('active');
    loginWrapper.classList.add('active');
});

Login.addEventListener('click', ()=>{
    loginWrapper.classList.add('active-popup');
});

register.addEventListener('click', ()=>{
    registrationWrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', ()=>{
    wrapper.classList.remove('active-popup');
});
