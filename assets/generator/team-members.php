<?php

echo '[Team Members] Starting Job'."\n\n";

echo '[Team Members] Listing Members'."\n";
$members = file_get_contents(__DIR__."/team-members.json");
$members = json_decode($members, true);
$teams = array();

for ($i = 0; $i < count($members); $i++) {
    echo $members[$i]['name'].", ";
}

echo "\n\n";


$file = fopen(__DIR__."/team-members.html.txt", "w") or die("Unable to open file!");

$content = '
                <!-- Team Members Placeholder Start -->
';
fwrite($file, $content);


echo '[Team Members] Executive Team: Starting'."\n\n";

echo '[Team Members] Executive Team: Creating Team'."\n\n";

for ($i = 0; $i < count($members); $i++) {
    foreach($members[$i]['team'] as $key => $value){
        if($key == 'executive'){
            $teams['executive'][(int)$members[$i]['team'][$key]['order']-1] = $members[$i];
        }
    }
}

echo '[Team Members] Executive Team: Listing Team'."\n";
for ($i = 0; $i < count($teams['executive']); $i++) {
    echo $teams['executive'][$i]['name'].", ";
}
echo "\n\n";

echo '[Team Members] Executive Team: Generating HTML'."\n\n";

for ($i = 0; $i < count($teams['executive']); $i++) {
$content = '
                <div class="card beside">
                    <div class="stacked">
';

if(isset($teams['executive'][$i]['image']) && $teams['executive'][$i]['image'] != ''){
$content .= '
                        <img src="'.$teams['executive'][$i]['image'].'" alt="'.$teams['executive'][$i]['name'].'">
';
} else {
$content .= '
                        <img src="assets/images/novacrypt.png" alt="NovaCrypt" style="filter: grayscale(100%); width: 200px; height: 200px; padding: 50px;">
';
}

$content .= '
                    </div>
                    <div class="stacked">
                        <p class="card-name">'.$teams['executive'][$i]['name'].'</p>
';

if(is_array($teams['executive'][$i]['team']['executive']['position'])){
$content .= '
                        <p class="card-position"><abbr title="'.$teams['executive'][$i]['team']['executive']['position']['long'].'">'.$teams['executive'][$i]['team']['executive']['position']['abbr'].'</abbr></p>
';
} else {
$content .= '
                        <p class="card-position">'.$teams['executive'][$i]['team']['executive']['position'].'</p>
';
}

if(isset($teams['executive'][$i]['description']) && $teams['executive'][$i]['description'] != ''){
$content .= '
                        <p class="card-description">'.$teams['executive'][$i]['description'].'</p>
';
}

$content .= '
                        <div class="card-some beside">
';

if(isset($teams['executive'][$i]['some']) && is_array($teams['executive'][$i]['some'])){

foreach($teams['executive'][$i]['some'] as $key => $value){

if($key == 'website'){
$content .= '
                            <a href="'.$value.'"><i class="fas fa-globe"></i></a>
';
}
if($key == 'linkedin'){
$content .= '
                            <a href="https://www.linkedin.com/in/'.$value.'/"><i class="fab fa-linkedin"></i></a>
';
}

if($key == 'instagram'){
$content .= '
                            <a href="https://www.instagram.com/'.$value.'/"><i class="fab fa-instagram"></i></a>
';
}

if($key == 'twitter'){
$content .= '
                            <a href="https://twitter.com/'.$value.'/"><i class="fab fa-twitter"></i></a>
';
}

}

}

$content .= '
                        </div>
                    </div>
                </div>
';

fwrite($file, $content);
}

echo '[Team Members] Executive Team: Ready'."\n\n";
/*

echo '[Team Members] Project Team: Starting'."\n";
echo '[Team Members] Project Team: Ready'."\n\n";


echo '[Team Members] Business Team: Starting'."\n";
echo '[Team Members] Business Team: Ready'."\n\n";


echo '[Team Members] Developer Team: Starting'."\n";
echo '[Team Members] Developer Team: Ready'."\n\n";


echo '[Team Members] Art Team: Starting'."\n";
echo '[Team Members] Art Team: Ready'."\n\n";


echo '[Team Members] Video & Audio Team: Starting'."\n";
echo '[Team Members] Video & Audio Team: Ready'."\n\n";


echo '[Team Members] Writer Team: Starting'."\n";
echo '[Team Members] Writer Team: Ready'."\n\n";
*/

echo '[Team Members] Ending Job'."\n";

$content = '
                <!-- Team Members Placeholder End -->
';

fwrite($file, $content);
fclose($file);

?>
