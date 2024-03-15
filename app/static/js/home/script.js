const menuItems = document.querySelectorAll('.menu-items');

const changeActiveClass = () => {
    menuItems.forEach(item => {
        item.classList.remove('active');
    });
};

menuItems.forEach(item => {
    item.addEventListener('click', () => {
        changeActiveClass();
        item.classList.add('active');
    });
});

var pathArray = window.location.pathname.split('/');
var pageName = pathArray[pathArray.length - 1];

document.title = "MedSync Solutions - " + pageName;