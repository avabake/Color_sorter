
var imagedata = [];

var images_with_most_red = [];
var images_with_most_orange = [];
var images_with_most_yellow = [];
var images_with_most_green = [];
var images_with_most_blue = [];
var images_with_most_purple = [];
var images_with_most_pink = [];


function renderImages(imagearray) {
  var src = document.getElementById('original_images');

  imagearray.forEach((image) => {
    // add an image to the page
    var img = document.createElement('div');
    img.setAttribute('class', 'image_holder');

    if (image['file']) {
      img.style.backgroundImage = 'url(' + 'original_images/' + image['file'] +')';

      src.appendChild(img);
    }
  });
}

// fetch csv file
fetch('colors.csv', {method: 'GET'})
  .then(response => response.text())
  .then(data => {
    // split the csv file into lines
    lines = data.split(/\r?\n/);

    // for each line in lines, do the following
    lines.forEach((line) => {
      // split the line into values
      values = line.split(',');

      // log the other deatils to the console
      entry = {
        'red': Number(values[1]),
        'orange': Number(values[2]),
        'yellow': Number(values[3]),
        'green': Number(values[4]),
        'blue': Number(values[5]),
        'purple': Number(values[6]),
        'pink': Number(values[7])
      }

      let highest = Math.max(...Object.values(entry));
      highest = Object.keys(entry).find(key => entry[key] === highest);
      entry.file = values[0];
      entry.highest = highest;


      if (highest == 'red') {
        images_with_most_red.push(entry);
      }

      if (highest == 'orange') {
        images_with_most_orange.push(entry);
      }

      if (highest == 'yellow') {
        images_with_most_yellow.push(entry);
      }

      if (highest == 'green') {
        images_with_most_green.push(entry);
      }

      if (highest == 'blue') {
        images_with_most_blue.push(entry);
      }

      if (highest == 'purple') {
        images_with_most_purple.push(entry);
      }

      if (highest == 'pink') {
        images_with_most_pink.push(entry);
      }

      imagedata.push(entry);
    });

    renderImages(imagedata);
  });

function filterBy(color) {
  imagedata.sort(function (a, b) {
    return a[color] - b[color];
  });
  var src = document.getElementById('original_images');
  src.innerHTML = '';
  renderImages(imagedata.reverse());
}

function drawRainbow() {
  var src = document.getElementById('original_images');
  src.innerHTML = '';
  renderImages(images_with_most_red);
  renderImages(images_with_most_orange);
  renderImages(images_with_most_yellow);
  renderImages(images_with_most_green);
  renderImages(images_with_most_blue);
  renderImages(images_with_most_purple);
  renderImages(images_with_most_pink);

}

// zoom .............................................

var imagesize = 300

function resizeImages(inc){
  imagesize += inc;
  var images = document.querySelectorAll('#original_images .image_holder');

  images.forEach(img => {
    img.style.width = imagesize + 'px';
    img.style.height = imagesize + 'px';
  });
}
