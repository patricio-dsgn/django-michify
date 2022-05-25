const COLORS = [
    "red darken-1",
    "pink darken-1",
    "purple darken-1",
    "blue",
    "indigo",
    "deep-purple",
    "indigo accent-3",
    "blue accent-3",
    "deep-purple accent-3",
    "light-blue darken-2",
    "cyan",
    "teal",
    "teal accent-3",
    "cyan accent-3",
    "blue accent-3",
    "green accent-3",
    "light-green accent-4",
    "lime accent-4",
    "lime darken-2",
    "light-green darken-2",
    "green darken-1",
    "green accent-2",
    "lime lighten-1",
    "light-green lighten-1",
    "yellow darken-2",
    "orange darken-2",
    "amber darken-4",
    "yellow accent-4",
    "amber accent-3",
    "orange accent-3",
    "deep-orange",
    "deep-orange darken-3",
]
let len = COLORS.length;
color1Random = COLORS[Math.floor(Math.random() * len)];
color2Random = COLORS[Math.floor(Math.random() * len)];

let c1 = color1Random.split(' ');
let c2 = color2Random.split(' ');

const nav = document.querySelector('nav');
const footer = document.querySelector('footer');

c1.forEach(function(color) {
    nav.classList.add(color);
});

c2.forEach(function(color) {
    footer.classList.add(color);
});


