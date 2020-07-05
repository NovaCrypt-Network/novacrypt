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

class Team {

    public $name;
    public $code;
    public $members;
    public $team;
    public $htmlContent;

    public function setName ($name) {
        $this->name = $name;
    }

    public function setCode ($code) {
        $this->code = $code;
    }

    public function setMembers($members) {
        $this->members = $members;
    }

    public function outputConsole ($task) {
        echo '[Team Members] '.$this->name.' Team: '.$task."\n\n";
    }

    public function createTeam () {
        for ($i = 0; $i < count($this->members); $i++) {
            foreach($this->members[$i]['team'] as $key => $value){
                if($key == $this->code){
                    $this->team[(int)$this->members[$i]['team'][$key]['order']-1] = $this->members[$i];
                }
            }
        }
    }

    public function listTeam (){
        for ($i = 0; $i < count($this->team); $i++) {
            echo $this->team[$i]['name'].", ";
        }
    }

    public function generateHTML (){

        if($this->code == "executive"){
$content = '
                <section id="'.$this->code.'">
                    <header>
                        <h2 style="display: none;">'.$this->name.'</h2>
                    </header>
';
        } else {
$content = '
                <section id="'.$this->code.'">
                    <header>
                        <h2>'.$this->name.'</h2>
                    </header>
';
        }

        for ($i = 0; $i < count($this->team); $i++) {
$content .= '
                    <div class="card beside">
                        <div class="stacked">
';

            if(isset($this->team[$i]['image']) && $this->team[$i]['image'] != ''){
$content .= '
                            <img src="'.$this->team[$i]['image'].'" alt="'.$this->team[$i]['name'].'">
';
            } else {
$content .= '
                            <img src="assets/images/novacrypt.png" alt="NovaCrypt" style="filter: grayscale(100%); padding: 50px;">
';
            }

$content .= '
                        </div>
                        <div class="stacked">
                            <p class="card-name">'.$this->team[$i]['name'].'</p>
';

            if(is_array($this->team[$i]['team'][$this->code]['position'])){
$content .= '
                            <p class="card-position"><abbr title="'.$this->team[$i]['team'][$this->code]['position']['long'].'">'.$this->team[$i]['team'][$this->code]['position']['abbr'].'</abbr></p>
';
            } else {
$content .= '
                            <p class="card-position">'.$this->team[$i]['team'][$this->code]['position'].'</p>
';
            }

            if(isset($this->team[$i]['description']) && $this->team[$i]['description'] != ''){
$content .= '
                            <p class="card-description">'.$this->team[$i]['description'].'</p>
';
            }

            if(isset($this->team[$i]['some']) && is_array($this->team[$i]['some'])){

$content .= '
                            <div class="card-some beside">
';

                foreach($this->team[$i]['some'] as $key => $value){

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

                    if($key == 'discord'){
$content .= '
                                <a href="#" title="'.$value.'"><i class="fab fa-discord"></i></a>
';
                    }

                }

$content .= '
                            </div>
';

            }

$content .= '
                        </div>
                    </div>

';

        }
$content .= '
                </section>
';

            $this->htmlContent .= $content;
    }

    public function doTasks (){
        $this->outputConsole("Starting");
        $this->outputConsole("Creating Team");
        $this->createTeam();
        $this->outputConsole("Listing Team");
        $this->listTeam();
        echo "\n\n";
        $this->outputConsole("Generating HTML");
        $this->generateHTML();
    }

    public function getHTML (){
        $this->outputConsole("Writing to file");
        return $this->htmlContent;
    }
}

$team = new Team();
$team->setName("Executive");
$team->setCode("executive");
$team->setMembers($members);
$team->doTasks();
fwrite($file, $team->getHTML());

$team = new Team();
$team->setName("Project");
$team->setCode("project");
$team->setMembers($members);
$team->doTasks();
fwrite($file, $team->getHTML());

$team = new Team();
$team->setName("Business");
$team->setCode("business");
$team->setMembers($members);
$team->doTasks();
fwrite($file, $team->getHTML());

$team = new Team();
$team->setName("Developer");
$team->setCode("developer");
$team->setMembers($members);
$team->doTasks();
fwrite($file, $team->getHTML());

$team = new Team();
$team->setName("Art");
$team->setCode("art");
$team->setMembers($members);
$team->doTasks();
fwrite($file, $team->getHTML());

$team = new Team();
$team->setName("Video & Audio");
$team->setCode("video/audio");
$team->setMembers($members);
$team->doTasks();
fwrite($file, $team->getHTML());

$team = new Team();
$team->setName("Writing");
$team->setCode("writing");
$team->setMembers($members);
$team->doTasks();
fwrite($file, $team->getHTML());

echo '[Team Members] Ending Job'."\n";

$content = '
                <!-- Team Members Placeholder End -->
';

fwrite($file, $content);
fclose($file);

?>
