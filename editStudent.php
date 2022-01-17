<!DOCTYPE html>
<html lang="en">
<head>
<?php include 'inc/head.php'; ?>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Edit Student | Rendezvous </title>
</head>
<body>

   <?php include'inc/nav.php';

   $error =  "";
$id = mysqli_real_escape_string($conn, $_GET['id']);
   if(isset($_POST['submit'])){
       $name= mysqli_real_escape_string($conn, $_POST['name']);
       $campus= mysqli_real_escape_string($conn, $_POST['campus']);
       $section= mysqli_real_escape_string($conn, $_POST['section']);
       $team= mysqli_real_escape_string($conn, $_POST['team']);
       $chest= mysqli_real_escape_string($conn, $_POST['chest']);
      $card= mysqli_real_escape_string($conn, $_POST['card']);

       $mysql = "UPDATE students SET name='$name', campus='$campus', section='$section', team='$team', chest='$chest', card_no='$card' WHERE id = $id";
       
       if(mysqli_query($conn, $mysql)){
           $error = '<div class="alert alert-success" role="alert">
           Student updated successfully!
         </div>';
       }else{
        $error = '<div class="alert alert-danger" role="alert">Failed to update student!
        
       </div>';
           echo mysqli_error($conn);
       }
   }
   
   
   
   ?>

<div class="centerCard card">
    <?php echo $error; 
    $viewSql = "SELECT * FROM students WHERE id = $id";
    $viewRes = mysqli_query($conn, $viewSql);

   $row = mysqli_fetch_assoc($viewRes);
    
    ?>
    
    <form action="" method="post">
        <h3>Fill the student details</h3> <br>
        <!-- Student Name -->
        <div class="input-group mb-3">
<input type="text"  class="form-control"  name="name" id="name" placeholder="Student Name" value="<?php echo $row['name']; ?>" autocomplete="off" required>
</div>
<!-- Campus Name -->
<select class="form-select" aria-label="Campus"  name="campus" id="campus" required>
  <option  <?php if($row['campus']==""){echo "selected";}?>>Campus</option>
  <option value="mnc"  <?php if($row['campus']=="mnc"){echo "selected";}?>>Madeenathunnoor</option>
</select> <br>
<!-- Group Name -->
<select class="form-select" aria-label="Section"  name="section" id="section" required>
  <option  <?php if($row['section']==""){echo "selected";}?>>Section</option>
  <option value="jr" <?php if($row['section']=="jr"){echo "selected";}?>>Junior</option>
  <option value="sr" <?php if($row['section']=="sr"){echo "selected";}?>>Senior</option>
</select>
<br>
<!-- Section -->
<select class="form-select" aria-label="Group" name="team" id="team" required>
<option disabled <?php if($row['team']==""){echo "selected";}?>>Group</option> 
<?php 
$grpSQL = "SELECT * FROM team";
$grpRES = mysqli_query($conn, $grpSQL);
while($r = mysqli_fetch_assoc($grpRES)){
  echo' <option value="'.$r['code'].'"'; if($row['team']==$r['code']){echo "selected";}
  echo'>'.$r['name'].'</option> ';
}

?>
</select> <br>
<!-- Chest Number -->

<div class="input-group mb-3">
<input type="number"  class="form-control"  value="<?php echo $row['chest']; ?>" name="chest" id="chest" placeholder="Chest Number" required>
</div>
<div class="input-group mb-3">
<input type="text"  class="form-control"  value="<?php echo $row['card_no']; ?>" name="card" id="card" placeholder="Card Number" required>
</div>
<input type="submit" value="Update Student" name="submit"   class="btn btn-primary" style="float: right; margin-right:30px;">


    </form>
</div>

</body>
</html>