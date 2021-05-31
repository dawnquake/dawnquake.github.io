/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function top_nav_toggle() {
  var x = document.getElementById("myTopnav");
      if (x.className === "topnav") {
        x.className += " responsive";
      } else {
        x.className = "topnav";
      }
} 

function write_navbar(){

    document.write("        <div class=\"topnav\" id=\"myTopnav\">");
    document.write("");
    document.write("");
    document.write("          <a href=\"\/index.html\" class=\"active\">About Me<\/a>");
    document.write("          <a href=\"\/CV\/CV.html\">CV<\/a>");
    document.write("          ");
    document.write("          ");
    document.write("          <div class=\"dropdown\">");
    document.write("            <button class=\"dropbtn\"> Software Projects");
    document.write("              <i class=\"fa fa-caret-down\"><\/i>");
    document.write("            <\/button>");
    document.write("            <div class=\"dropdown-content\">");
    document.write("              <a href=\"\/Cxx_projects\/Cxx_projects.html\">C++ projects<\/a>");
    document.write("              <a href=\"\/Python_projects\/Python_projects.html\">Python<\/a>");
    document.write("              <a href=\"\/Fortran_projects\/Fortran_projects.html\">Fortran<\/a>");
    document.write("            <\/div>");
    document.write("          <\/div>");
    document.write("          ");
    document.write("          <a href=\"\/PC_build\/PC_build.html\"> PC Build <\/a>");
    document.write("          <a href=\"\/Contact\/Contact.html\">Contact<\/a>");
    document.write("          ");
    document.write("          ");
    document.write("          <!-- This is for the respnsive design to collapse-->");
    document.write("          <a href=\"javascript:void(0);\" class=\"icon\" onclick=\"myFunction()\">&#9776;<\/a>");
    document.write("         <\/div> ");
  
}