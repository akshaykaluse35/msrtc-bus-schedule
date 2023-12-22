const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
}))



const searchFun = () => {

  
  let filter = document.getElementById('frm').value.toUpperCase();

  let myTable = document.getElementById('tbl_cntnt_id');

  let tr = myTable.getElementsByTagName('tr');

  for (var i = 0; i<tr.length; i++){
    let td = tr[i].getElementsByTagName('td')[0];

    if(td){
      let textvalue = td.textContent || td.innerHTML;
      if(textvalue.toUpperCase().indexOf(filter) > -1){
        tr[i].style.display = "";
      }else{
        tr[i].style.display = "none";
      }
    }

  }

}