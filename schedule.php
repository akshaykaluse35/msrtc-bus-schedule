<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="schedule.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <header>
        <div class="container"> 

          <div class="subcontainer">

            <nav class="navbar">

              <a href="Main.html" class="nav-branding">MSRTC INDEX</a>

              <ul class="nav-menu">

                <li class="nav-item">
                  <a href="Main.html" class="nav-link">Home</a>
                </li>
                <li class="nav-item">
                  <a href="About.html" class="nav-link">About Us</a>
                </li>

                <li class="nav-item">
                    <a href="Gallery.html" class="nav-link">Gallery</a>
                </li>

                <li class="nav-item">
                    <a href="schedule.html" class="nav-link">Schedule</a>
                </li>

              </ul>

              <div class="hamburger">

                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>

              </div>

            </nav>

          </div>

         </div>

       </header>

       <!-- search button  -->

        <div class="head">
          <form action="" method="GET">
            <div class="form-box">
              <input type="text" name="search" id="frm" class="search-field business" required value="<?php if(isset($_GET['search'])){echo $_GET['search']; } ?>" list="taluka" placeholder="From.." onkeyup="searchFun()">
              <div class="options">
                <datalist id="taluka">
                  
                  <option value="Karjat taluka, Raigad "></option>
                  <option value="Ahmednagar "></option>
                  <option value="Akola"></option>
                  <option value="Amravati"></option>
                  <option value="Aurangabad"></option>
                  <option value="Beed"></option>
                  <option value="Bhandara"></option>
                  <option value="Buldhana"></option>
                  <option value="Chandrapur"></option>
                  <option value="Dhule"></option>
                  <option value="Gadchiroli"></option>
                  <option value="Gondia"></option>
                  <option value="Hingoli"></option>
                  <option value="J-R "></option>
                  <option value="Jalgaon"></option>
                  <option value="Jalna"></option>
                  <option value="Kolhapur"></option>
                  <option value="Latur"></option>
                  <option value="Mumbai City"></option>
                  <option value="Mumbai Suburban"></option>
                  <option value="Nagpur"></option>
                  <option value="Nanded"></option>
                  <option value="Nandurbar"></option>
                  <option value="Nashik"></option>
                  <option value="Osmanabad"></option>
                  <option value="Palghar "></option>
                  <option value="Parbhani"></option>
                  <option value="Pune"></option>
                  <option value="Raigad"></option>
                  <option value="Ratnagiri "></option>
                  <option value="S-Z"></option>
                  <option value="Sangli "></option>
                  <option value="Satara"></option>
                  <option value="Sindhudurg"></option>
                  <option value="Solapur"></option>
                  <option value="Thane"></option>
                  <option value="Wardha "></option>
                  <option value="Washim"></option>
                  <option value="Yavatmal"></option>
                  <option value="MALSHIRAS"></option>
                  
               <option value="AKOLA "></option> <option value="BHOOM "></option> <option value="CHANDGAD "></option> <option value="AHMADPUR "></option> <option value="CHOPDA "></option> <option value="JINTUR "></option> <option value="MALEGAON "></option> <option value="GUJ "></option> <option value="KOPARGAON "></option> <option value="KINWAT "></option> <option value="AHERI "></option> <option value="VENGURLA "></option> <option value="PALGHAR "></option> <option value="PANDHARPUR "></option> <option value="RATNAGIRI "></option> <option value="SATANA "></option> <option value="SATARA "></option> <option value="UMRI "></option> <option value="AMBEGAON "></option> <option value="BHUDARGAD "></option> <option value="BASMAT "></option> <option value="IGATPURI "></option> <option value="POLADPUR "></option> <option value="HADGAON "></option> <option value="AURANGABAD "></option> <option value="NANDGAON "></option> <option value="KANKAVLI "></option> <option value="MAJALGAON "></option> <option value="INDAPUR "></option> <option value="JAFRABAD "></option> <option value="NASIK "></option> <option value="DHARUR "></option> <option value="HINGANGHAT "></option> <option value="PARANDA "></option> <option value="SHRIGONDA "></option> <option value="AMBAJOGAI "></option> <option value="CHAKUR "></option> <option value="MALVAN "></option> <option value="WARORA "></option> <option value="SHEVGAON "></option> <option value="GUHAGAR "></option> <option value="JALGAON "></option> <option value="JUNNAR "></option> <option value="JAWHAR "></option> <option value="NANDURBAR "></option> <option value="PATAN "></option> <option value="SANGAMESHWAR "></option> <option value="VASAI "></option> <option value="ASHTI "></option> <option value="JALGAON JAMOD"></option> <option value="BHOKARDAN "></option> <option value="KAGAL "></option> <option value="JAMKHED "></option> <option value="AHMEDNAGAR "></option> <option value="PACHORA CHIPL"></option> <option value="PACHORA"></option> <option value="CHIPLUN"></option> <option value="SAKRI "></option> <option value="MANDANGAD"></option> <option value="SHRIVADHAN"></option> <option value="OSMANABAD"></option> <option value="NAGPUR"></option> <option value="LONAR "></option> <option value="SAWANTWADI"></option> <option value="TULJAPUR"></option> <option value="VIKRAMGAD"></option> <option value="GAGANBAWADA"></option> <option value="KAR "></option> <option value="PATHARDI"></option> <option value="PHALTAN"></option> <option value="DHARNI"></option> <option value="KARAD "></option> <option value="SINNAR"></option> <option value="RADHANANGARI"></option> <option value="SHIROL"></option> <option value="MIRAJ "></option> <option value="PETH "></option> <option value="DEONI "></option> <option value="KHED "></option> <option value="BHIVANDI"></option> <option value="NANDURA"></option> <option value="DAPOLI"></option> <option value="SILLOD"></option> <option value="HAVELI"></option> <option value="SOYGAON"></option> <option value="SHINDKHEDA"></option> <option value="ARJUNI MORGAON"></option> <option value="RAVER "></option> <option value="DAHANU"></option> <option value="GADHINGALJ"></option> <option value="RAJAPUR"></option> <option value="SHAHAPUR"></option> <option value="GANGAKHED"></option> <option value="KUDAL "></option> <option value="KHATAV"></option> <option value="WARUD "></option> <option value="WANI "></option> <option value="MP "></option> <option value="MANVAT"></option> <option value="MAHAD "></option> <option value="HATKANANGLE"></option> <option value="AKKALKUWA"></option> <option value="BARAMATI"></option> <option value="AMBAD "></option> <option value="WADA "></option> <option value="DHULE "></option> <option value="DEOLI "></option> <option value="BHOR "></option> <option value="MUMBAI"></option> <option value="MORSHI"></option> <option value="MADHA "></option> <option value="NARKHED "></option> <option value="BHOKAR "></option> <option value="SHIRUR "></option> <option value="MANGAON "></option> <option value="BARSHI "></option> <option value="MANWAT "></option> <option value="PATHRI "></option> <option value="PUSAD "></option> <option value="KALWAN "></option> <option value="SHIRPUR "></option> <option value="MAWAL "></option> <option value="TRIMBAKESHWAR "></option> <option value="RAJURA "></option> <option value="KADEGAON "></option> <option value="KHAMGAON "></option> <option value="KANDHAR "></option> <option value="SUDHAGAD PALI "></option> <option value="LANJA "></option> <option value="PURLI "></option> <option value="KHANAPUR(VITA) "></option> <option value="MHASLA "></option> <option value="MANTHA "></option> <option value="SANGAMNER "></option> <option value="BHANDARA "></option> <option value="DEOGAD "></option> <option value="PARTUR "></option> <option value="AKOLE "></option> <option value="DEORUKH "></option> <option value="PANHALA "></option> <option value="THANE "></option> <option value="MAHABLESHWAR "></option> <option value="CHIKHALI "></option> <option value="UMERGA "></option> <option value="ACHALPUR "></option> <option value="VAIBHAVWADI "></option> <option value="AUSA "></option> <option value="TRIBAKESHWAR "></option> <option value="DEULGAON RAJA "></option> <option value="MOHADI "></option> <option value="HINGOLI "></option> <option value="AP "></option> <option value="YAVATMAL "></option> <option value="NANDED "></option> <option value="SHRIRAMPUR "></option> <option value="CHANDRAPUR "></option> <option value="VELHA "></option> <option value="PAITHAN "></option> <option value="CHALISGAON "></option> <option value="KANNAD "></option> <option value="HINGNA "></option> <option value="PALAM "></option> <option value="NEWASA "></option> <option value="TASGAON "></option> <option value="MURUD "></option> <option value="JALNA "></option> <option value="PARBHANI "></option> <option value="POMBHURNA "></option> <option value="BALAPUR "></option> <option value="KALAMB "></option> <option value="MANORA "></option> <option value="KARVIR "></option> <option value="YEOLA ROHA SANGOLA"></option> <option value="PARNER "></option> <option value="JAT "></option> <option value="AMRAVATI "></option> <option value="KAVTHE MAHANKAL "></option> <option value="GOND PIMPRI "></option> <option value="RISOD "></option> <option value="KARMALA "></option> <option value="SHAHUWADI "></option> <option value="NIPHAD "></option> <option value="BRAHMAPURI "></option> <option value="MUL "></option> <option value="VAIJAPUR "></option> <option value="ALIBAG "></option> <option value="AKOT "></option> <option value="AUNDHA "></option> <option value="BEED "></option> <option value="KARANJA "></option> <option value="PAONI "></option> <option value="PURNA "></option> <option value="SHAHADA "></option> <option value="SELU "></option> <option value="TUMSAR "></option> <option value="AKRANI "></option> <option value="AKKALKOT "></option> <option value="DHAMANGAON "></option> <option value="LOHARA "></option> <option value="ARVI "></option> <option value="RAHURI "></option> <option value="RALEGAON "></option> <option value="TALODA "></option> <option value="WARDHA "></option> <option value="KALLAMB "></option> <option value="KOREGAON "></option> <option value="JAVLI "></option> <option value="SOLAPUR "></option> <option value="BHATKULI "></option> <option value="RAHATA "></option> <option value="GONDPIMPRI "></option> <option value="MOHOL "></option> <option value="MOTALA "></option> <option value="TIWASA "></option> <option value="LOHA "></option> <option value="KARJAT "></option> <option value="SHIRALA "></option> <option value="DINDORI "></option> <option value="TALASARI "></option> <option value="WALWA-ISLAMPUR "></option> <option value="PARGAON KHANDALA "></option> <option value="SHIRUR ANANTPAL "></option> <option value="ARNI "></option> <option value="SENGAON "></option> <option value="SOYEGAON "></option> <option value="BULDHANA "></option> <option value="ANJANGAON SURJI "></option> <option value="DHARANGAON "></option> <option value="LAKHANDUR "></option> <option value="MAHUR "></option> <option value="AJRA "></option> <option value="JAMNER "></option> <option value="MULSHI "></option> <option value="PANVEL "></option> <option value="WAI SHEGAONPATURM"></option> <option value="PHULAMBARI "></option> <option value="DEGLOOR "></option> <option value="SURGANA "></option> <option value="CHAMORSHI "></option> <option value="KELAPUR "></option> <option value="SANGRAMPUR "></option> <option value="MAHAGAON "></option> <option value="DODAMARG "></option> <option value="ARDHAPUR "></option> <option value="PEN "></option> <option value="AMBERNATH "></option> <option value="LATUR "></option> <option value="KHALAPUR "></option> <option value="AMGAON "></option> <option value="AMALNER "></option> <option value="PATODA "></option> <option value="KUHI "></option> <option value="GADCHIROLI "></option> <option value="KAIJ "></option> <option value="MANGALVEDHA "></option> <option value="SOLAPUR SOUTH "></option> <option value="JALKOT "></option> <option value="DIGRAS "></option> <option value="KALAMNOORI "></option> <option value="MAN "></option> <option value="PALUS "></option> <option value="YAWAL "></option> <option value="MAUDA "></option> <option value="WASHIM "></option> <option value="MEHKAR "></option> <option value="BADNAPUR "></option> <option value="SOLAPUR NORTH "></option> <option value="RAMTEK "></option> <option value="NER "></option> <option value="ATPADI "></option> <option value="KALYAN "></option> <option value="BILLOLI "></option> <option value="ARMORI "></option> <option value="SIRONCHA "></option> <option value="NILANGA "></option> <option value="NAIGAON "></option> <option value="ERANDOL "></option> <option value="MURTIJAPUR "></option> <option value="TIRODA "></option> <option value="PAROLA "></option> <option value="GOA "></option> <option value="CHANDUR BAZAR "></option> <option value="UMRED "></option> <option value="TELHARA "></option> <option value="KAMPTEE "></option> <option value="UDGIR "></option> <option value="PUNE "></option> <option value="SAONER "></option> <option value="TARAKPUR "></option> <option value="HIMYAT NAGAR "></option> <option value="CHIMUR "></option> <option value="MUKTAINAGAR "></option> <option value="GEORAI "></option> <option value="GHANSANGHVI "></option> <option value="SIRUR "></option> <option value="PARSEONIURANDARWAH"></option> <option value="TALA "></option> <option value="CHANDWAD "></option> <option value="BHADRAVATI "></option> <option value="CHIKHALDARA "></option> <option value="KORCHI "></option> <option value="DEOLA "></option> <option value="BHADGAON "></option> <option value="SHELU "></option> <option value="BALLARPUR "></option> <option value="KALMESHWAR "></option> <option value="MUDKHED "></option> <option value="KHULTABAD "></option> <option value="NAVAPUR "></option> <option value="MULCHERA "></option> <option value="DHARMABAD "></option> <option value="GONDIA "></option> <option value="BABHULGAON "></option> <option value="JIVTI "></option> <option value="SINDHKHED RAJ"></option> <option value="BODWAD "></option> <option value="SAKOLI "></option> <option value="DESAIGANJ (VA"></option> <option value="MURBAD "></option> <option value="LAKHNI "></option> <option value="ZARI JAMNI "></option> <option value="GANGAPUR "></option> <option value="BARSHI TAKLI "></option> <option value="RENAPUR "></option> <option value="KORPANA "></option> <option value="DAUND "></option> <option value="TALEGAON "></option> <option value="BHIVAPUR "></option> <option value="KATOL "></option> <option value="- "></option> <option value="SONPETH "></option> <option value="MALKAPUR "></option> <option value="UMARKHED "></option> <option value="NANDGAON KHAN"></option> <option value="GHATANJI "></option> <option value="BHUSAVAL "></option> <option value="NAGBHID "></option> <option value="BHAMRAGAD "></option> <option value="DEORI "></option> <option value="GOREGAON "></option> <option value="CHANDUR RAILW"></option> <option value="SALEKASA "></option> <option value="SAMUDRAPUR "></option> <option value="MANGRULPIR "></option> <option value="DARYAPUR "></option> <option value="ULHASNAGAR "></option> <option value="PURANDHAR "></option> <option value="SAOLI "></option> <option value="WADWANI "></option> <option value="DHANORA "></option> <option value="KURKHEDA "></option>

                     </datalist>
                     </div>
                  <input type="text" class="search-field location" placeholder="To.." list="taluka">
                  <button class="search-btn" type="button">Search</button>
                  </div> 
                  </form>
                  </div>


       <!---------------------------- table--------------------------------  -->


       <form action="" method="GET">
        <div class="input-group mb-3">
            <input type="text" name="search" required value="<?php if(isset($_GET['search'])){echo $_GET['search']; } ?>" class="form-control" placeholder="Search data">
            <button type="submit" class="btn btn-primary">Search</button>
        </div>
    </form>

<!-- </div>
</div>
</div>
</div>
</div> -->

<div class="col-md-12">
<div class="card mt-4">
<div class="card-body">
<table class="table table-bordered">
<thead>
    <tr>
        <th>Sr.No</th>
        <th>To From</th>
        <th>To Stop</th>
        <th>Service Type</th>
        <th>Bus Timing</th>
    </tr>
</thead>
<tbody>
    <?php 
        $con = mysqli_connect("localhost","root","","data");

        if(isset($_GET['search']))
        {
            $filtervalues = $_GET['search'];
            $query = "SELECT * FROM sheet1 WHERE CONCAT(from_stop, to_stop,bus_service, timing) LIKE '%$filtervalues%' ";
            $query_run = mysqli_query($con, $query);

            if(mysqli_num_rows($query_run) > 0)
            {
                foreach($query_run as $items)
                {
                    ?>
                    <tr>
                        <td><?= $items['Sr_No']; ?></td>
                        <td><?= $items['from_stop']; ?></td>
                        <td><?= $items['to_stop']; ?></td>
                        <td><?= $items['bus_service']; ?></td>
                        <td><?= $items['timing']; ?></td>
                    </tr>
                    <?php
                }
            }
            else
            {
                ?>
                    <tr>
                        <td colspan="4">No Record Found</td>
                    </tr>
                <?php
            }
        }
    ?>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>





<!-- 
       <section>
        <h1>MSRTC Schedule</h1>
        <div class="tbl-header">
          <table cellpadding="0" cellspacing="0" border="0" class="tbl" id="tbl_id">
            <thead>
              <tr>
                <th>From</th>
                <th>To</th>
                <th>Bus Type</th>
                <th>Dep. Time</th>
                <th>Ticket</th>
              </tr>
            </thead>
          </table>
        </div>
        <div class="tbl-content">
          <table cellpadding="0" cellspacing="0" border="0" class="tbl_cntnt" id="tbl_cntnt_id">
            <tbody>
              <tr>
                <td>Shirdi</td>
                <td>Parel</td>
                <td>Semi Luxury</td>
                <td>7:00 AM</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
              </tr>
              <tr>
                <td>Shirdi</td>
                <td>Bhoisar</td>
                <td>Ordinary Express</td>
                <td>8:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
              </tr>
              <tr>
                <td>Shirdi</td>
                <td>Selvasa</td>
                <td>Ordinary Express</td>
                <td>9:30</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
              </tr>
              <tr>
                <td>Shirdi</td>
                <td>Selvasa</td>
                <td>Ordinary Express</td>
                <td>12:30 AM</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
              </tr>
              <tr>
                <td>Shirdi</td>
                <td>Thane CBS </td>
                <td>Ordinary Express</td>
                <td>15:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
              </tr>
              <tr>
                <td>Shirdi</td>
                <td>Andheri Char Bunglow</td>
                <td>Semi Luxury</td>
                <td>15:32</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
              </tr>
              <tr>
                <td>MCT via NEW SHIVAJI NAGAR PUNE</td>
                <td>BHN</td>
                <td>Ordinary Express</td>
                <td>00:01:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td>PRL via PANDHARPUR</td>
                <td>SNGO</td>
                <td>Ordinary Express</td>
                <td>00:15:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td>PRL via KASURDI</td>
                <td>BHR</td>
                <td>Semi Luxury</td>
                <td>00:15:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
              
             <tr>
                <td>MCT via CHANDANI CHOWK</td>
                <td>BHR</td>
                <td>Semi Luxury</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.020833333333333332}'>00:30:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"MCT via EXPRESS MUMBAI HIGHWAY START"}'>MCT via EXPRESS MUMBAI HIGHWAY START</td>
                <td data-sheets-value='{"1":2,"2":"TKPR"}'>TKPR</td>
                <td data-sheets-value='{"1":2,"2":"Semi Luxury"}'>Semi Luxury</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.020833333333333332}'>00:30:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"PRL"}'>PRL</td>
                <td data-sheets-value='{"1":2,"2":"VIRL"}'>VIRL</td>
                <td data-sheets-value='{"1":2,"2":"Ordinary Express"}'>Ordinary Express</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.020833333333333332}'>00:30:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
              </tr>
            
             <tr>
                <td data-sheets-value='{"1":2,"2":"BVINC via PANVEL VILLAGE FATA"}'>BVINC via PANVEL VILLAGE FATA</td>
                <td data-sheets-value='{"1":2,"2":"SWR"}'>SWR</td>
                <td data-sheets-value='{"1":2,"2":"Semi Luxury"}'>Semi Luxury</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.020833333333333332}'>00:30:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
              </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"MCT via BARSHI"}'>MCT via BARSHI</td>
                <td data-sheets-value='{"1":2,"2":"KLM"}'>KLM</td>
                <td data-sheets-value='{"1":2,"2":"Day Ordinary"}'>Day Ordinary</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.0625}'>01:30:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"PRL"}'>PRL</td>
                <td data-sheets-value='{"1":2,"2":"SNSL"}'>SNSL</td>
                <td data-sheets-value='{"1":2,"2":"Ordinary Express"}'>Ordinary Express</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.1875}'>04:30:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"ANL via BORIVALI NANCY COLONY"}'>ANL via BORIVALI NANCY COLONY</td>
                <td data-sheets-value='{"1":2,"2":"UMG"}'>UMG</td>
                <td data-sheets-value='{"1":2,"2":"Ordinary Express"}'>Ordinary Express</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.18819444444444444}'>04:31:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"VSI via BORIVALI"}'>VSI via BORIVALI</td>
                <td data-sheets-value='{"1":2,"2":"STR"}'>STR</td>
                <td data-sheets-value='{"1":2,"2":"Semi Luxury"}'>Semi Luxury</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.20833333333333334}'>05:00:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"MCT via TARDOLI"}'>MCT via TARDOLI</td>
                <td data-sheets-value='{"1":2,"2":"BMT"}'>BMT</td>
                <td data-sheets-value='{"1":2,"2":"Semi Luxury"}'>Semi Luxury</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.20833333333333334}'>05:00:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"KNN"}'>KNN</td>
                <td data-sheets-value='{"1":2,"2":"MWD"}'>MWD</td>
                <td data-sheets-value='{"1":2,"2":"Ordinary Express"}'>Ordinary Express</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.20833333333333334}'>05:00:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
            
             <tr>
                <td data-sheets-value='{"1":2,"2":"BVINC via SION"}'>BVINC via SION</td>
                <td data-sheets-value='{"1":2,"2":"SWR"}'>SWR</td>
                <td data-sheets-value='{"1":2,"2":"AC-Shivneri"}'>AC-Shivneri</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.20833333333333334}'>05:00:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"PRL via PUNE RLY. STN."}'>PRL via PUNE RLY. STN.</td>
                <td data-sheets-value='{"1":2,"2":"AWBCBS"}'>AWBCBS</td>
                <td data-sheets-value='{"1":2,"2":"Ordinary Express"}'>Ordinary Express</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.20833333333333334}'>05:00:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"KNN via MAHUD"}'>KNN via MAHUD</td>
                <td data-sheets-value='{"1":2,"2":"SNGO"}'>SNGO</td>
                <td data-sheets-value='{"1":2,"2":"Day Ordinary"}'>Day Ordinary</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.20833333333333334}'>05:00:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"MCT via KURLA NEHRU NAGAR"}'>MCT via KURLA NEHRU NAGAR</td>
                <td data-sheets-value='{"1":2,"2":"KML"}'>KML</td>
                <td data-sheets-value='{"1":2,"2":"Ordinary Express"}'>Ordinary Express</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.21875}'>05:15:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"ANL"}'>ANL</td>
                <td data-sheets-value='{"1":2,"2":"PHL"}'>PHL</td>
                <td data-sheets-value='{"1":2,"2":"Ordinary Express"}'>Ordinary Express</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.21944444444444444}'>05:16:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"BVINC via KURLA NEHRU NAGAR"}'>BVINC via KURLA NEHRU NAGAR</td>
                <td data-sheets-value='{"1":2,"2":"KWD"}'>KWD</td>
                <td data-sheets-value='{"1":2,"2":"Ordinary Express"}'>Ordinary Express</td>
                <td data-sheets-numberformat='{"1":6,"2":"hh:mm:ss","3":1}' data-sheets-value='{"1":3,"3":0.22916666666666666}'>05:30:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td data-sheets-value='{"1":2,"2":"MCT via SHEVGAON"}'>MCT via SHEVGAON</td>
                <td>GVI</td>
                <td >Semi Luxury</td>
                <td >05:30:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
             
             <tr>
                <td >BVINC via KOKAN BHAVAN</td>
                <td>KML</td>
                <td >Ordinary Express</td>
                <td>05:30:00</td>
                <td><button class="tkt" onclick="window.location.href='https://www.redbus.in/';">
                  Book Now
                </button></td>
             </tr>
            </tbody>
          </table>
        </div>
      </section>
      
      
       next and previous button  -->
      <!-- <div class="pagination-wrapper">
        <div class="pagination">
          <a class="prev page-numbers" href="javascript:;">prev</a>
          <span aria-current="page" class="page-numbers current">1</span>
          <a class="page-numbers" href="sch">2</a>
          <a class="page-numbers" href="javascript:;">3</a>
          <a class="page-numbers" href="javascript:;">4</a>
          <a class="page-numbers" href="javascript:;">5</a>
          <a class="page-numbers" href="javascript:;">6</a>
          <a class="page-numbers" href="javascript:;">7</a>
          <a class="page-numbers" href="javascript:;">8</a>
          <a class="page-numbers" href="javascript:;">9</a>
          <a class="page-numbers" href="javascript:;">10</a>
          <a class="next page-numbers" href="javascript:;">next</a>
        </div>
      </div> --> -->



       <!-- footer  -->


       <footer class="footer_1">
        <div class="footer-content">
            <h3>MSRTC Index</h3>
            <p>MSRTC Index is a blog website where you will find great and useful information about MSRTC. Here each part of Information is beautifully described step by step with the required source code.</p>
            <ul class="socials">
                <li><a href=""><i class="fa fa-facebook"></i></a></li>
                <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                <li><a href="#"><i class="fa fa-google-plus"></i></a></li>
                <li><a href="#"><i class="fa fa-youtube"></i></a></li>
                <li><a href="#"><i class="fa fa-linkedin-square"></i></a></li>
            </ul>
        </div>
        <div class="footer-bottom">
            <p>copyright &copy; <a href="#"> MSRTC Index</a>  </p>
                    <div class="footer-menu">
                      <ul class="f-menu">
                        <li><a href="">Home</a></li>
                        <li><a href="">About Us</a></li>
                        <li><a href="">Gallery</a></li>
                        <li><a href="">Schedule</a></li>
                      </ul>
                    </div>
        </div>
    
    </footer>

    <script src="myjs.js"></script>

</body>
</html>