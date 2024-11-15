let links = document.querySelectorAll('.list__link');
let targetID;

links.forEach(function (element) {
    element.addEventListener('click', function (event) {
        event.preventDefault(); 
        targetID = element.getAttribute('href'); 
        document.querySelector(targetID).scrollIntoView({
            behavior: 'smooth', 
            block: 'start'
        });
    });
});


let menu = document.querySelector('.menu');
let isActive = false;

function showMenu() {
    menu.style.visibility = 'visible'; 
    anime({
        targets: '.menu',
        translateX: ['100%', '-300%'],
        easing: 'easeInOutQuad',
        duration: 1000,
        complete: function () {
            isActive = true;
        }
    });
}

function hideMenu() {
    anime({
        targets: '.menu',
        translateX: ['-300%', '100%'], 
        easing: 'easeInOutQuad',
        duration: 1000,
        complete: function () {
            menu.style.visibility = 'hidden';
            isActive = false;
        }
    });
}

$('.logo').click(function () {
    if (!isActive) {
        showMenu();
    } else {
        hideMenu();
    }
});

$(document).ready(function() {
    $(".category").click(function() {
        $(".category").removeClass("active");
        $(this).addClass("active");

        $(".wishlist-item").removeClass("active");

        const id = $(this).attr("id");
        if (id === "active") {
            $("#active-content").addClass("active");
        } else if (id === "marked") {
            $("#marked-content").addClass("active");
        } else if (id === "all") {
            $("#all-content").addClass("active");
        }
    });
});

const passwordInput = document.getElementById('password');
const passwordToggle = document.querySelector('.password-toggle');

if (passwordToggle) {
    passwordToggle.addEventListener('click', () => {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            passwordToggle.textContent = '🙈';
        } else {
            passwordInput.type = 'password';
            passwordToggle.textContent = '👁';
        }
    });
}

const passwordInput1 = document.getElementById('password1');
const passwordToggle1 = document.querySelector('.password-toggle1');

if (passwordToggle1) {
    passwordToggle1.addEventListener('click', () => {
        if (passwordInput1.type === 'password') {
            passwordInput1.type = 'text';
            passwordToggle1.textContent = '🙈';
        } else {
            passwordInput1.type = 'password';
            passwordToggle1.textContent = '👁';
        }
    });
}
