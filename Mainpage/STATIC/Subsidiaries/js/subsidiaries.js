var divarray = document.getElementsByClassName("childdiv")
var div = 360 / divarray.length;
var radius = 350;
var parentdiv = document.getElementById('parentdiv');
var offsetToParentCenter = parseInt(parentdiv.offsetWidth / 2); //assumes parent is square
var offsetToChildCenter = 80;
var totalOffset = offsetToParentCenter - offsetToChildCenter;

for (var i = 0; i < divarray.length; ++i) {
  var childdiv = divarray[i];
  childdiv.style.position = 'absolute';
  var y = Math.sin((div * i) * (Math.PI / 180)) * radius;
  var x = Math.cos((div * i) * (Math.PI / 180)) * radius;
  childdiv.style.top = (y + totalOffset).toString() + "px";
  childdiv.style.left = (x + totalOffset).toString() + "px";
}