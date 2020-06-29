<?php

$members = file_get_contents(__DIR__."/team-members.json");
$members = json_decode($members, true);

echo '
                <div class="card beside">
                    <div class="stacked">
                        <img src="https://cdn.discordapp.com/attachments/706393501973348454/726896563418562590/image3.jpg" alt="Nakkia">
                    </div>
                    <div class="stacked">
                        <p class="card-name">Roland Yan</p>
                        <p class="card-position"><abbr title="Chief Executive Officer">CEO</abbr></p>
                        <p class="card-description">Bacon ipsum dolor amet shankle brisket shank kevin porchetta hamburger sirloin chicken strip steak alcatra pancetta drumstick. Flank strip steak buffalo frankfurter biltong, jerky meatloaf. </p>
                        <div class="card-some beside">
                            <a href="https://rolandyan.com"><i class="fas fa-globe"></i></a>
                            <a href="https://www.linkedin.com/in/roland-yan-52618a1a7/"><i class="fab fa-linkedin"></i></a>
                            <a href="https://www.instagram.com/robo_panda_x/"><i class="fab fa-instagram"></i></a>
                        </div>
                    </div>
                </div>
';




?>
