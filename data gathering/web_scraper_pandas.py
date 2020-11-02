import csv
import os
import urllib.request                           # Library for opening url and creating requests
import psycopg2
from database.config import config

from html_table_parser import HTMLTableParser   # for parsing all the tables present on the website
import pandas as pd                             # for converting the parsed data in a  pandas dataframe


def main(url, decoding):
    # Function to connect to Database
    def connect():
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

            # execute a statement
            #cur.execute("SELECT name FROM \"PokemonData\"")
            cur.execute("INSERT INTO Test VALUES ('Test String22', 22)")
            postgres_insert_query = """ INSERT INTO test (test1, test2) VALUES (%s,%s)"""
            record_to_insert = ('arg', 1337)
            cur.execute(postgres_insert_query, record_to_insert)

            conn.commit()
            count = cur.rowcount
            print(count, "Record inserted successfully into table")

            # display the query result
            result = cur.fetchall()
            print(result)

            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

    # Opens a website and read its binary contents (HTTP Response Body)
    def url_get_contents(url):
        req = urllib.request.Request(url=url)       # making request to the website
        f = urllib.request.urlopen(req)             # reading contents of the website
        return f.read()

    ''' ========= '''
    ''' VARIABLES '''
    ''' ========= '''
    # defining the html contents of a URL.
    xhtml = url_get_contents(url).decode(decoding)

    # Fix for pidgeot page on serebii
    if url == 'https://www.serebii.net/spindex/018.shtml':
        xhtml = '''
        
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>

<head>
<title>Serebii.net Spin-Off Pok&eacute;dex - #018 Pidgeot</title>

<meta name="GENERATOR" content="Arachnophilia 4.0">
<meta name="FORMATTER" content="Arachnophilia 4.0">


<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="imagetoolbar" CONTENT="no">

<link rel="preconnect" href="https://tags.bkrtx.com/">
<link rel="preconnect" href="https://securepubads.g.doubleclick.net/" crossorigin>
<link rel="preconnect" href="https://cdn.consentmanager.mgr.consensu.org/" crossorigin>

<!-- GDPR Compliancy -->
<style>
body {
	--cmpBgColor: #507C36;
	--cmpTextColor: #eeeeee;
	--cmpLinkColor: #ffffff;
	--cmpPurposesColor: #eeeeee;
	--cmpBrandColor: #565656;
	--cmpLogo: url('https://www.serebii.net/extralogo.png');
}
</style>
<!-- GDPR Compliancy --><!-- GDPR Compliancy -->
    <link rel="stylesheet" type="text/css" HREF="/spp-temp.css">

  <link rel="search" href="/serebii-opensearch.xml" type="application/opensearchdescription+xml" title="Serebii Open Search" />
   <LINK REL="SHORTCUT ICON" HREF="/favicon.ico">
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-128947957-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-128947957-1');
</script>
<!-- Place the below code anywhere you like in the <head> (higher is better) -->



<script>window.AdSlots = window.AdSlots || {cmd: [], disableScripts: ['gpt','bk']};</script>
<script async src="https://tags.bkrtx.com/js/bk-coretag.js"></script>
<script async src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"></script>

<script src="/dist/serebii2.min.js" async></script>


</head>

<BODY  ondragstart="return false"  text=#000000 bottomMargin=0 bgcolor="#383838"

leftMargin=0 topMargin=0 rightMargin=0>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TPSZKKL"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->



    <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" height="1" background="/BannerBg.jpg">

      <tr>

        <td width="100%" background="/BannerBg.jpg" height="1">

    <div align="center">

    <font color="#000000">

    <a href="/"><img border="0" src="/Banner.jpg" alt="Serebii.net Header"></a></font></td>

      </tr>

    </table>

    <table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" bordercolor="#111111" width="100%" height="1">

      <tr>

        <td width="95%" height="1" colspan="3" bgcolor="#507C36" bordercolor="#111111">

    <table border="0" cellpadding="0" cellspacing="0" width="100%" height="1">

			<td colspan="2" height="1">
        <div id="menu"><b>Quick Links -</b> <a href="/index2.shtml">Home</a> - <a href="http://www.serebiiforums.com/" target="blank">Forums</a> - <a href="mailto:webmaster@serebii.net">Contact</a> - <a href="/discord.shtml">Discord</a> - <a href="/pokemon">Pokédex Hub</a> - <a href="/pokemongo/pokemon">GO Pokédex</a> - <a href="/pokedex-swsh">Sword & Shield Pokédex</a> - <a href="/pokearth">Pokéarth</a></div></td>
<td align="right" width="300" height="1">
<div id="menu">  <form id="searchbox_018410473690156091934:6gahkiyodbi" action="/search.shtml" style="margin:0px;">
    <input type="hidden" name="cx" value="018410473690156091934:6gahkiyodbi" />
    <input type="hidden" name="cof" value="FORID:11" />
    <input name="q" type="text" size="20" />
    <input type="submit" name="sa" value="Search" />
  </form>
  <script type="text/javascript" src="//www.google.com/coop/cse/brand?form=searchbox_018410473690156091934%3A6gahkiyodbi"></script>
</div>
</td>
</tr>
</table>
</td>

      </tr>




<tr>
<td width="1%" height="362" valign="top" bgcolor="#507C36" bordercolor="#111111">
<div id="menu"><img src="/Toolbar/headers/SPP.gif" width="140" height="27" alt="Main Header"></a><br />
<a href="/index2.shtml">News</a><br />
<a href="/archive.shtml">Archived news</a><br />
<a href="/pokemon/"><b>Pokédex</b></a><br />
<a href="/pokedex/">-Red/Blue Pokédex</a><br />
<a href="/pokedex-gs/">-Gold/Silver Pokédex</a><br />
<a href="/pokedex-rs/">-Ruby/Sapphire Pokédex</a><br />
<a href="/pokedex-dp/">-Diamond/Pearl Pokédex</a><br />
<a href="/pokedex-bw/">-Black/White Pokédex</a><br />
<a href="/pokedex-xy/">-X & Y Pokédex</a><br />
<a href="/pokedex-sm/">-Sun & Moon Pokédex</a><br />
<a href="/pokedex-sm/">-Let's Go Pokédex</a><br />
<a href="/pokedex-swsh/">-Sword & Shield Pokédex</a><br />
<b>Attackdex</b><br />
<a href="/attackdex-rby/">-Gen 1 Attackdex</a><br />
<a href="/attackdex-gs/">-Gen 2 Attackdex</a><br />
<a href="/attackdex/">-Gen 3 Attackdex</a><br />
<a href="/attackdex-dp/">-Gen 4 Attackdex</a><br />
<a href="/attackdex-bw/">-Gen 5 Attackdex</a><br />
<a href="/attackdex-xy/">-Gen 6 Attackdex</a><br />
<a href="/attackdex-sm/">-Gen 7 Attackdex</a><br />
<a href="/attackdex-swsh/">-Gen 8 Attackdex</a><br />
<a href="/itemdex/">ItemDex</a><br />
<a href="/pokearth/">Pokéarth</a><br />
<a href="/abilitydex/">Abilitydex</a><br />
<a href="/spindex/">Spin-Off Pokédex</a><br />
<a href="/spindex-dp/">Spin-Off Pokédex DP</a><br />
<a href="/spindex-bw/">Spin-Off Pokédex BW</a><br />
<a href="/card/dex/">Cardex</a><br />
<a href="/movies/dex/">Cinematic Pokédex</a><br />
<a href="/games/mechanics.shtml">Game Mechanics</a><br />
<a href="/games/iv-calcswsh.shtml">-Sword/Shield IV Calc.</a><br />
<a href="/potw-swsh">Pokémon of the Week</a><br />
<a href="/potw-swsh/">-8th Gen </a><br />
<a href="/potw-sm/">-7th Gen </a><br />
<a href="/potw-xy/">-6th Gen </a><br />
<a href="http://www.serebiiforums.com" target="blank">Forums</a><br />
<a href="/discord.shtml">Discord Chat</a><br />
<a href="/games/currentevents.shtml">Current & Upcoming Events</a><br />
<a href="/events">Event Database</a><br />
<a href="/swordshield/pokemon.shtml">8th Generation Pokémon</a><br />
<a href="/swordshield/dlcpokemon.shtml">-DLC Gen 8 Pokémon</a><br />
<a href="/anime/"><img src="/Toolbar/headers/Anime.gif" border="0" width="140" height="27" alt="Anime Header"></a><br />
<a href="/anime/epiguide/">Episode Listings & Pictures</a><br />
<a href="/anime/dex/">AniméDex</a><br />
<a href="/anime/characters/">Character Bios</a><br />
<a href="/anime/epiguide/indigo/">The Indigo League</a><br />
<a href="/anime/epiguide/orange/">The Orange League</a><br />
<a href="/anime/epiguide/johto/">The Johto Saga</a><br />
<a href="/anime/epiguide/houen/">The Saga in Hoenn!</a><br />
<a href="/anime/epiguide/kanto/">Kanto Battle Frontier Saga!</a><br />
<a href="/anime/epiguide/shinou/">The Sinnoh Saga!</a><br />
<a href="/anime/epiguide/bestwishes/">Best Wishes - Unova Saga</a><br />
<a href="/anime/epiguide/xy/">XY - Kalos Saga</a><br />
<a href="/anime/epiguide/sunmoon/">Sun & Moon - Alola Saga</a><br />
<a href="/anime/epiguide/pokemon/">Pokémon Journeys - Galar Saga</a><br />
<a href="/anime/epiguide/chronicles/">Pokémon Chronicles</a><br />
<a href="/anime/epiguide/generations/">Pokémon Generations</a><br />
<a href="/anime/epiguide/twilightwings/">Pokémon Twilight Wings</a><br />
<a href="/anime/epiguide/specials/">The Special Episodes</a><br />
<a href="/anime/banned.shtml">The Banned Episodes</a><br />
<a href="/anime/shiny/">Shiny Pokémon</a><br />
<a href="/anime/movies/">Movies In Anime</a><br />
<a href="/anime/gba/">GBA Video Listings</a><br />

<a href="/games/"></a><img src="/Toolbar/headers/Games.gif" border="0" width="140" height="27" alt="Video Games Header"></b></a><br />
<a href="/pokemon/generation8.shtml"><b>Gen VIII</b></a><br />
<a href="/swordshield/">Sword & Shield</a><br />
<a href="/pokemonhome/">Pokémon HOME</a><br />
<a href="/pokemonmasters/">Pokémon Masters</a><br />
<a href="/dungeonrescueteamdx/">Pokémon Mystery Dungeon Rescue Team DX</a><br />
<a href="/pokemonsmile/">Pokémon Smile</a><br />
<a href="/cafemix/">Pokémon Café Mix</a><br />
<a href="/newpokemonsnap/">New Pokémon Snap</a><br />
<a href="/pokemonsleep/">Pokémon Sleep</a><br />
<a href="/detectivepikachu2/">Detective Pikachu 2</a><br />
<a href="/pokemon/generation7.shtml"><b>Gen VII</b></a><br />
<a href="/sunmoon/">Sun & Moon</a><br />
<a href="/ultrasunultramoon/">Ultra Sun & Ultra Moon</a><br />
<a href="/letsgopikachueevee/">Let's Go, Pikachu! & Let's Go, Eevee!</a><br />
<a href="/pokemongo/">Pokémon GO</a><br />
<a href="/magikarpjump/">Pokémon: Magikarp Jump</a><br />
<a href="/rumblerush/">Pokémon Rumble Rush</a><br />
<a href="/pokkendx/">Pokkén Tournament DX</a><br />
<a href="/detective/">Detective Pikachu</a><br />
<a href="/quest/">Pokémon Quest</a><br />
<a href="/smashbrosultimate/">Super Smash Bros. Ultimate</a><br />
<a href="/pokemon/generation6.shtml"><b>Gen VI</b></a><br />
<a href="/xy/">X & Y</a><br />
<a href="/omegarubyalphasapphire/">Omega Ruby & Alpha Sapphire</a><br />
<a href="/bank/">Pokémon Bank</a><br />
<a href="/battletrozei/">Pokémon Battle Trozei<br />Pokémon Link: Battle</a><br />
<a href="/artacademy/">Pokémon Art Academy</a><br />
<a href="/bandofthieves/">The Band of Thieves & 1000 Pokémon</a><br />
<a href="/shuffle/">Pokémon Shuffle</a><br />
<a href="/rumbleworld/">Pokémon Rumble World</a><br />
<a href="/supermysterydungeon/">Pokémon Super Mystery Dungeon</a><br />
<a href="/picross/">Pokémon Picross</a><br />
<a href="/detective/">Detective Pikachu</a><br />
<a href="/pokken/">Pokkén Tournament</a><br />
<a href="/duel/">Pokémon Duel</a><br />
<a href="/smashbros3dswiiu/">Smash Bros for 3DS/Wii U</a><br />
<a href="/games/badge/">Nintendo Badge Arcade</a><br />
<a href="/pokemon/generation5.shtml"><b>Gen V</b></a><br />
<a href="/blackwhite/">Black & White</a><br />
<a href="/black2white2/">Black 2 & White 2</a><br />
<a href="/dreamradar/">Pokémon Dream Radar</a><br />
<a href="/trettalab/">Pokémon Tretta Lab</a><br />
<a href="/rumbleu/">Pokémon Rumble U</a><br />
<a href="/dungeoninfinity/">Mystery Dungeon: Gates to Infinity</a><br />
<a href="/conquest/">Pokémon Conquest</a><br />
<a href="/pokepark2/">PokéPark 2: Wonders Beyond</a><br />
<a href="/rumble2/">Pokémon Rumble Blast</a><br />
<a href="/pokedex3d/">Pokédex 3D</a><br />
<a href="/pokedex3dpro/">Pokédex 3D Pro</a><br />
<a href="/typingds/">Learn With Pokémon: Typing Adventure</a><br />
<a href="/card/howtoplayds/">TCG How to Play DS</a><br />
<a href="/pokedexios/">Pokédex for iOS</a><br />
<a href="/pokemon/generation4.shtml"><b>Gen IV</b></a><br />
<a href="/diamondpearl/">Diamond & Pearl</a><br />
<a href="/platinum/">Platinum</a><br />
<a href="/heartgoldsoulsilver/">Heart Gold & Soul Silver</a><br />
<a href="/ranger3/">Pokémon Ranger: Guardian Signs</a><br />
<a href="/melee/">Pokémon Rumble</a><br />
<a href="/dungeon3/">Mystery Dungeon: Blazing, Stormy & Light Adventure Squad</a><br />
<a href="/pokepark/">PokéPark Wii - Pikachu's  Adventure</a><br />
<a href="/battle/">Pokémon Battle Revolution</a><br />
<a href="/dungeonsky/">Mystery Dungeon - Explorers of Sky</a><br />
<a href="/ranger2/">Pokémon Ranger: Shadows of Almia</a><br />
<a href="/dungeon2/">Mystery Dungeon - Explorers of Time & Darkness</a><br />
<a href="/ranch/">My Pokémon Ranch</a><br />
<a href="/battrio/">Pokémon Battrio</a><br />
<a href="/ssbb/">Smash Bros Brawl</a><br />
<a href="/pokemon/generation3.shtml"><b>Gen III</b></a><br />
<a href="/rubysapphire/">Ruby & Sapphire</a><br />
<a href="/fireredleafgreen/">Fire Red & Leaf Green</a><br />
<a href="/emerald/">Emerald</a><br />
<a href="/colosseum/">Pokémon Colosseum</a><br />
<a href="/xd/">Pokémon XD: Gale of Darkness</a><br />
<a href="/dash/">Pokémon Dash</a><br />
<a href="/pokemon_channel/">Pokémon Channel</a><br />
<a href="/pokemon_box/">Pokémon Box: RS</a><br />
<a href="/pinball_rs/">Pokémon Pinball RS</a><br />
<a href="/ranger/">Pokémon Ranger</a><br />
<a href="/mysteriousdungeon/">Mystery Dungeon Red & Blue</a><br />
<a href="/torouze/">PokémonTrozei</a><br />
<a href="/pikachu/">Pikachu DS Tech Demo</a><br />
<a href="/pokeparkfish/">PokéPark Fishing Rally</a><br />
<a href="/e-reader/">The E-Reader</a><br />
<a href="/pokemate/">PokéMate</a><br />
<a href="/pokemon/generation2.shtml"><b>Gen II</b></a><br />
<a href="/gs/">Gold/Silver</a><br />
<a href="/crystal/">Crystal</a><br />
<a href="/stadium2/">Pokémon Stadium 2</a><br />
<a href="/puzzlechallenge/">Pokémon Puzzle Challenge</a><br />
<a href="/mini/">Pokémon Mini</a><br />
<a href="/smash_bros_2/">Super Smash Bros. Melee</a><br />
<a href="/pokemon/generation1.shtml"><b>Gen I</b></a><br />
<a href="/rb/">Red, Blue & Green</a><br />
<a href="/yellow/">Yellow</a><br />
<a href="/puzzleleague/">Pokémon Puzzle League</a><br />
<a href="/snap/">Pokémon Snap</a><br />
<a href="/pinball/">Pokémon Pinball </a><br />
<a href="/stadiumjp/">Pokémon Stadium (Japanese)</a><br />
<a href="/stadium/">Pokémon Stadium </a><br />
<a href="/tradingcardgamegb/">Pokémon Trading Card Game GB </a><br />
<a href="/smash_bros/">Super Smash Bros. </a><br />
<b>Miscellaneous</b><br />
<a href="/games/mechanics.shtml">Game Mechanics</a><br />
<a href="/playpokemon">Play! Pokémon Championship Series</a><br />
<a href="/games/others.shtml">In Other Games </a><br />
<a href="/games/virtualconsole.shtml">Virtual Console </a><br />
<a href="/games/consoles.shtml">Special Edition Consoles </a><br />
<a href="/games/themes.shtml">Pokémon 3DS Themes</a><br />
<a href="/apps">Smartphone & Tablet Apps </a><br />
<a href="/virtualpet">Virtual Pets</a><br />
<a href="/amiibo">amiibo</a><br />

<a href="/manga/"><img src="/Toolbar/headers/Manga.gif" border="0" width="140" height="27" alt="Manga Header"></a><br />
<a href="/manga/">General Information</a><br />
<a href="/manga/dex">MangaDex</a><br />
<a href="/manga/characters">Character BIOs</a><br />
<a href="/manga/characters-new">Detailed BIOs</a><br />
<a href="/manga/chapter.shtml">Chapter Guides</a><br />
<a href="/manga/volume.shtml">Volume Guides</a><br />
<a href="/manga/rby/">RBG Series</a><br />
<a href="/manga/yellow/">Yellow Series</a><br />
<a href="/manga/gsc/">GSC Series</a><br />
<a href="/manga/rs/">RS Series</a><br />
<a href="/manga/frlg/">FRLG Series</a><br />
<a href="/manga/bf/">Emerald Series</a><br />
<a href="/manga/dp/">DP Series</a><br />
<a href="/manga/pt/">Platinum Series</a><br />
<a href="/manga/hgss/">HGSS Series</a><br />
<a href="/manga/bw/">BW Series</a><br />
<a href="/manga/b2w2/">B2W2 Series</a><br />
<a href="/manga/xy/">XY Series</a><br />
<a href="/manga/oras/">ORAS Series</a><br />
<a href="/manga/sunmoon/">SM Series</a><br />

<a href="/movies/"><img src="/Toolbar/headers/Movies.gif" border="0" width="140" height="27" alt="Movies Header"></a><br />
<b>Anime</b><br />
<a href="/movies/mewtwo/origin/">The Origin of Mewtwo </a><br />
<a href="/movies/mewtwo/">Mewtwo Strikes Back </a><br />
<a href="/movies/lugia/">The Power of One </a><br />
<a href="/movies/entei/">Spell Of The Unown </a><br />
<a href="/anime/epiguide/specials/002.shtml">Mewtwo Returns </a><br />
<a href="/movies/serebii/">Celebi: Voice of the Forest</a><br />
<a href="/movies/latias_latios/">Pokémon Heroes</a><br />
<a href="/movies/jirachi/">Jirachi - Wish Maker</a><br />
<a href="/movies/deoxys/">Destiny Deoxys!</a><br />
<a href="/movies/mew/">Lucario and the Mystery of Mew!</a><br />
<a href="/movies/kyogre/">Pokémon Ranger & The Temple of the Sea!</a><br />
<a href="/movies/dp/">The Rise of Darkrai!</a><br />
<a href="/movies/giratina/">Giratina & The Sky Warrior!</a><br />
<a href="/movies/arceus/">Arceus and the Jewel of Life</a><br />
<a href="/movies/celebi/">Zoroark - Master of Illusions</a><br />
<a href="/movies/victini/">Black: Victini & Reshiram<br />White: Victini & Zekrom</a><br />
<a href="/movies/kyurem/">Kyurem VS The Sword of Justice</a><br />
<a href="/movies/meloetta/">-Meloetta's Midnight Serenade</a><br />
<a href="/movies/genesect/">Genesect and the Legend Awakened</a><br />
<a href="/movies/xy/">Diancie & The Cocoon of Destruction</a><br />
<a href="/movies/hoopa/">Hoopa & The Clash of Ages</a><br />
<a href="/movies/volcanion/">Volcanion and the Mechanical Marvel</a><br />
<a href="/movies/pokemon20/">Pokémon I Choose You!</a><br />
<a href="/movies/thepowerofus/">Pokémon The Power of Us</a><br />
<a href="/movies/mewtwoevolution/">Mewtwo Strikes Back Evolution</a><br />
<a href="/movies/coco/">Coco</a><br />
<b>Live Action</b><br />
<a href="/movies/detectivepikachu/">Pokémon's Detective Pikachu</a><br />
<b>Sections</b><br />
<a href="/movies/dex/">Cinematic Pokédex</a><br />
<a href="/movies/biography/">Live Action Character Biographies</a><br />

<a href="/movies/"><img src="/Toolbar/headers/PikachuShorts.gif" border="0" width="140" height="27" alt="Pikachu Shorts Header"></a><br />
<a href="/movies/pikachu1/">Pikachu's Summer Vacation</a><br />
<a href="/movies/pikachu2/">Pikachu's Rescue Adventure</a><br />
<a href="/movies/pikachu3/">Pikachu And Pichu </a><br />
<a href="/movies/pikachu4/">Pikachu's PikaBoo </a><br />
<a href="/movies/pikachu5/">Camp Pikachu!</a><br />
<a href="/movies/pikachu6/">Gotta Dance!!</a><br />
<a href="/movies/pikachu7/">Pikachu's Summer Festival!</a><br />
<a href="/movies/pikachu8/">Pikachu's Ghost Festival!</a><br />
<a href="/movies/pikachu9/">Pikachu's Island Adventure!</a><br />
<a href="/movies/pikachu10/">Pikachu's Exploration Club</a><br />
<a href="/movies/pikachu11/">Pikachu's Great Ice Adventure</a><br />
<a href="/movies/pikachu12/">Pikachu's Sparkling Search</a><br />
<a href="/movies/pikachu13/">Pikachu's Really Mysterious Adventure</a><br />
<a href="/movies/eevee/">Eevee & Friends</a><br />
<a href="/movies/klefki/">Pikachu, What's This Key?</a><br />
<a href="/movies/pikachumusic/">Pikachu & The Pokémon Music Squad</a><br />

<img src="/Toolbar/headers/TradingCards.gif" border="0" width="140" height="27" alt="Trading Card Game Header"></a><br />
<a href="/card/dex/">Cardex</a><br />
<a href="/card/dex/extra">-Extra Pokémon Types</a><br />
<a href="/card/dex/trainers">Trainer Cards</a><br />
<a href="/card/dex/energy">Energy Cards</a><br />
<a href="/card/dex/extra/altart.shtml">Alternate Art Cards</a><br />
<a href="/card/english.shtml"><b>English Sets</b></a><br />
<a href="/card/rebelclash">-Rebel Clash</a><br />
<a href="/card/swordshield">-Sword & Shield</a><br />
<a href="/card/cosmiceclipse">-Cosmic Eclipse</a><br />
<a href="/card/hiddenfates">-Hidden Fates</a><br />
<a href="/card/unifiedminds">-Unified Minds</a><br />
<a href="/card/unbrokenbonds">-Unbroken Bonds</a><br />
<a href="/card/pokemondetectivepikachu">-Detective Pikachu</a><br />
<a href="/card/teamup">-Team Up</a><br />
<a href="/card/lostthunder">-Lost Thunder</a><br />
<a href="/card/dragonmajesty">-Dragon Majesty</a><br />
<a href="/card/celestialstorm">-Celestial Storm</a><br />
<a href="/card/forbiddenlight">-Forbidden Light</a><br />
<a href="/card/ultraprism">-Ultra Prism</a><br />
<a href="/card/shininglegends">-Shining Legends</a><br />
<a href="/card/crimsoninvasion">-Crimson Invasion</a><br />
<a href="/card/burningshadows">-Burning Shadows</a><br />
<a href="/card/guardiansrising">-Guardians Rising</a><br />
<a href="/card/sunmoon">-Sun & Moon</a><br />
<a href="/card/xy.shtml">-XY Series</a><br />
<a href="/card/bw.shtml">-BW Series</a><br />
<a href="/card/dpt.shtml">-DPtHS Series</a><br />
<a href="/card/ex.shtml">-EX Series</a><br />
<a href="/card/neo.shtml">-Neo/eSeries</a><br />
<a href="/card/first.shtml">-First Gen Series</a><br />
<a href="/card/engpromo.shtml"><b>English Promos</b></a><br />
<a href="/card/swshpromos">-SWSH Promos</a><br />
<a href="/card/smpromos">-SM Promos</a><br />
<a href="/card/xypromos">-XY Promos</a><br />
<a href="/card/bwpromos">-BW Promos</a><br />
<a href="/card/hgsspromo">-HGSS Promo</a><br />
<a href="/card/popseries.shtml">-POP Series</a><br />
<a href="/card/japanese.shtml"><b>Japanese Sets</b></a><br />
<a href="/card/infinityzone">-Infinity Zone</a><br />
<a href="/card/explosivewalker">-Explosive Walker</a><br />
<a href="/card/rebelliousclash">-Rebellious Clash</a><br /><a href="/card/sword">-Sword</a><br />
<a href="/card/shield">-Shield</a><br />
<a href="/card/tagallstars">-Tag All Stars</a><br />
<a href="/card/altergenesis">-Alter Genesis</a><br />
<a href="/card/dreamleague">-Dream League</a><br />
<a href="/card/remixbout">-Remix Bout</a><br />
<a href="/card/miracletwin">-Miracle Twin</a><br />
<a href="/card/skylegend">-Sky Legend</a><br />
<a href="/card/ggend">-GG End</a><br />
<a href="/card/doubleblaze">-Double Blaze</a><br />
<a href="/card/fullmetalwall">-Full Metal Wall</a><br />
<a href="/card/nightunison">-Night Unison</a><br />
<a href="/card/tagbolt">-Tag Bolt</a><br />
<a href="/card/gxultrashiny">-GX Ultra Shiny</a><br />
<a href="/card/vs">-Pokémon VS</a><br />
<a href="/card/jppromo.shtml"><b>Japanese Promos</b></a><br />
<a href="/card/spromo">-S Promos</a><br />
<a href="/card/smpromo">-SM Promos</a><br />
<a href="/card/xypromo">-XY Promos</a><br />
</div>
</td>
<td width="99%" height="362" valign="top" bordercolor="#111111">
<font face="Verdana" size="1" color="#FFFFFF"><div align="center" style="margin-top:10px;padding-bottom: 4px">
<div id="nn_lb1"></div>
</div>


<div align=center><table align=center width="95%" border="0" cellspacing="0" cellpadding="0">

<tr>

<td align="center" width="33%"><FORM NAME="nav"><DIV>

 <SELECT NAME="SelectURL" onChange="document.location.href=document.nav.SelectURL.options[document.nav.SelectURL.selectedIndex].value" style="color:#383838; font-size: 8pt; background:#CEBC77" size=1>

 <OPTION><b>001 - 151

<option value="/spindex/001.shtml">001 Bulbasaur

<option value="/spindex/002.shtml">002 Ivysaur

<option value="/spindex/003.shtml">003 Venusaur

<option value="/spindex/004.shtml">004 Charmander

<option value="/spindex/005.shtml">005 Charmeleon

<option value="/spindex/006.shtml">006 Charizard

<option value="/spindex/007.shtml">007 Squirtle

<option value="/spindex/008.shtml">008 Wartortle

<option value="/spindex/009.shtml">009 Blastoise

<option value="/spindex/010.shtml">010 Caterpie

<option value="/spindex/011.shtml">011 Metapod

<option value="/spindex/012.shtml">012 Butterfree

<option value="/spindex/013.shtml">013 Weedle

<option value="/spindex/014.shtml">014 Kakuna

<option value="/spindex/015.shtml">015 Beedrill

<option value="/spindex/016.shtml">016 Pidgey

<option value="/spindex/017.shtml">017 Pidgeotto

<option value="/spindex/018.shtml">018 Pidgeot

<option value="/spindex/019.shtml">019 Rattata

<option value="/spindex/020.shtml">020 Raticate

<option value="/spindex/021.shtml">021 Spearow

<option value="/spindex/022.shtml">022 Fearow

<option value="/spindex/023.shtml">023 Ekans

<option value="/spindex/024.shtml">024 Arbok

<option value="/spindex/025.shtml">025 Pikachu

<option value="/spindex/026.shtml">026 Raichu

<option value="/spindex/027.shtml">027 Sandshrew

<option value="/spindex/028.shtml">028 Sandslash

<option value="/spindex/029.shtml">029 Nidoran-F

<option value="/spindex/030.shtml">030 Nidorina

<option value="/spindex/031.shtml">031 Nidoqueen

<option value="/spindex/032.shtml">032 Nidoran-M

<option value="/spindex/033.shtml">033 Nidorino

<option value="/spindex/034.shtml">034 Nidoking

<option value="/spindex/035.shtml">035 Clefairy

<option value="/spindex/036.shtml">036 Clefable

<option value="/spindex/037.shtml">037 Vulpix

<option value="/spindex/038.shtml">038 Ninetales

<option value="/spindex/039.shtml">039 Jigglypuff

<option value="/spindex/040.shtml">040 Wigglytuff

<option value="/spindex/041.shtml">041 Zubat

<option value="/spindex/042.shtml">042 Golbat

<option value="/spindex/043.shtml">043 Oddish

<option value="/spindex/044.shtml">044 Gloom

<option value="/spindex/045.shtml">045 Vileplume

<option value="/spindex/046.shtml">046 Paras

<option value="/spindex/047.shtml">047 Parasect

<option value="/spindex/048.shtml">048 Venonat

<option value="/spindex/049.shtml">049 Venomoth

<option value="/spindex/050.shtml">050 Diglett

<option value="/spindex/051.shtml">051 Dugtrio

<option value="/spindex/052.shtml">052 Meowth

<option value="/spindex/053.shtml">053 Persian

<option value="/spindex/054.shtml">054 Psyduck

<option value="/spindex/055.shtml">055 Golduck

<option value="/spindex/056.shtml">056 Mankey

<option value="/spindex/057.shtml">057 Primeape

<option value="/spindex/058.shtml">058 Growlithe

<option value="/spindex/059.shtml">059 Arcanine

<option value="/spindex/060.shtml">060 Poliwag

<option value="/spindex/061.shtml">061 Poliwhirl

<option value="/spindex/062.shtml">062 Poliwrath

<option value="/spindex/063.shtml">063 Abra

<option value="/spindex/064.shtml">064 Kadabra

<option value="/spindex/065.shtml">065 Alakazam

<option value="/spindex/066.shtml">066 Machop

<option value="/spindex/067.shtml">067 Machoke

<option value="/spindex/068.shtml">068 Machamp

<option value="/spindex/069.shtml">069 Bellsprout

<option value="/spindex/070.shtml">070 Weepinbell

<option value="/spindex/071.shtml">071 Victreebel

<option value="/spindex/072.shtml">072 Tentacool

<option value="/spindex/073.shtml">073 Tentacruel

<option value="/spindex/074.shtml">074 Geodude

<option value="/spindex/075.shtml">075 Graveler

<option value="/spindex/076.shtml">076 Golem

<option value="/spindex/077.shtml">077 Ponyta

<option value="/spindex/078.shtml">078 Rapidash

<option value="/spindex/079.shtml">079 Slowpoke

<option value="/spindex/080.shtml">080 Slowbro

<option value="/spindex/081.shtml">081 Magnemite

<option value="/spindex/082.shtml">082 Magneton

<option value="/spindex/083.shtml">083 Farfetch'd

<option value="/spindex/084.shtml">084 Doduo

<option value="/spindex/085.shtml">085 Dodrio

<option value="/spindex/086.shtml">086 Seel

<option value="/spindex/087.shtml">087 Dewgong

<option value="/spindex/088.shtml">088 Grimer

<option value="/spindex/089.shtml">089 Muk

<option value="/spindex/090.shtml">090 Shellder

<option value="/spindex/091.shtml">091 Cloyster

<option value="/spindex/092.shtml">092 Gastly

<option value="/spindex/093.shtml">093 Haunter

<option value="/spindex/094.shtml">094 Gengar

<option value="/spindex/095.shtml">095 Onix

<option value="/spindex/096.shtml">096 Drowzee

<option value="/spindex/097.shtml">097 Hypno

<option value="/spindex/098.shtml">098 Krabby

<option value="/spindex/099.shtml">099 Kingler

<option value="/spindex/100.shtml">100 Voltorb

<option value="/spindex/101.shtml">101 Electrode

<option value="/spindex/102.shtml">102 Exeggcute

<option value="/spindex/103.shtml">103 Exeggutor

<option value="/spindex/104.shtml">104 Cubone

<option value="/spindex/105.shtml">105 Marowak

<option value="/spindex/106.shtml">106 Hitmonlee

<option value="/spindex/107.shtml">107 Hitmonchan

<option value="/spindex/108.shtml">108 Lickitung

<option value="/spindex/109.shtml">109 Koffing

<option value="/spindex/110.shtml">110 Weezing

<option value="/spindex/111.shtml">111 Rhyhorn

<option value="/spindex/112.shtml">112 Rhydon

<option value="/spindex/113.shtml">113 Chansey

<option value="/spindex/114.shtml">114 Tangela

<option value="/spindex/115.shtml">115 Kangaskhan

<option value="/spindex/116.shtml">116 Horsea

<option value="/spindex/117.shtml">117 Seadra

<option value="/spindex/118.shtml">118 Goldeen

<option value="/spindex/119.shtml">119 Seaking

<option value="/spindex/120.shtml">120 Staryu

<option value="/spindex/121.shtml">121 Starmie

<option value="/spindex/122.shtml">122 Mr.Mime

<option value="/spindex/123.shtml">123 Scyther

<option value="/spindex/124.shtml">124 Jynx

<option value="/spindex/125.shtml">125 Electabuzz

<option value="/spindex/126.shtml">126 Magmar

<option value="/spindex/127.shtml">127 Pinsir

<option value="/spindex/128.shtml">128 Tauros

<option value="/spindex/129.shtml">129 Magikarp

<option value="/spindex/130.shtml">130 Gyarados

<option value="/spindex/131.shtml">131 Lapras

<option value="/spindex/132.shtml">132 Ditto

<option value="/spindex/133.shtml">133 Eevee

<option value="/spindex/134.shtml">134 Vaporeon

<option value="/spindex/135.shtml">135 Jolteon

<option value="/spindex/136.shtml">136 Flareon

<option value="/spindex/137.shtml">137 Porygon

<option value="/spindex/138.shtml">138 Omanyte

<option value="/spindex/139.shtml">139 Omastar

<option value="/spindex/140.shtml">140 Kabuto

<option value="/spindex/141.shtml">141 Kabutops

<option value="/spindex/142.shtml">142 Aerodactyl

<option value="/spindex/143.shtml">143 Snorlax

<option value="/spindex/144.shtml">144 Articuno

<option value="/spindex/145.shtml">145 Zapdos

<option value="/spindex/146.shtml">146 Moltres

<option value="/spindex/147.shtml">147 Dratini

<option value="/spindex/148.shtml">148 Dragonair

<option value="/spindex/149.shtml">149 Dragonite

<option value="/spindex/150.shtml">150 Mewtwo

<option value="/spindex/151.shtml">151 Mew

</SELECT></FORM></td>

<td align="center" width="33%">

<FORM NAME="nav2"><DIV>

 <SELECT NAME="SelectURL" onChange="document.location.href=document.nav2.SelectURL.options[document.nav2.SelectURL.selectedIndex].value" style="color:#383838; font-size: 8pt; background:#CEBC77" size=1>

 <OPTION><b>152 - 251

<option value="/spindex/152.shtml">152 Chikorita

<option value="/spindex/153.shtml">153 Bayleef

<option value="/spindex/154.shtml">154 Meganium

<option value="/spindex/155.shtml">155 Cyndaquil

<option value="/spindex/156.shtml">156 Quilava

<option value="/spindex/157.shtml">157 Typhlosion

<option value="/spindex/158.shtml">158 Totodile

<option value="/spindex/159.shtml">159 Croconaw

<option value="/spindex/160.shtml">160 Feraligatr

<option value="/spindex/161.shtml">161 Sentret

<option value="/spindex/162.shtml">162 Furret

<option value="/spindex/163.shtml">163 Hoothoot

<option value="/spindex/164.shtml">164 Noctowl

<option value="/spindex/165.shtml">165 Ledyba

<option value="/spindex/166.shtml">166 Ledian

<option value="/spindex/167.shtml">167 Spinarak

<option value="/spindex/168.shtml">168 Ariados

<option value="/spindex/169.shtml">169 Crobat

<option value="/spindex/170.shtml">170 Chinchou

<option value="/spindex/171.shtml">171 Lanturn

<option value="/spindex/172.shtml">172 Pichu

<option value="/spindex/173.shtml">173 Cleffa

<option value="/spindex/174.shtml">174 Igglybuff

<option value="/spindex/175.shtml">175 Togepi

<option value="/spindex/176.shtml">176 Togetic

<option value="/spindex/177.shtml">177 Natu

<option value="/spindex/178.shtml">178 Xatu

<option value="/spindex/179.shtml">179 Mareep

<option value="/spindex/180.shtml">180 Flaaffy

<option value="/spindex/181.shtml">181 Ampharos

<option value="/spindex/182.shtml">182 Bellossom

<option value="/spindex/183.shtml">183 Marill

<option value="/spindex/184.shtml">184 Azumarill

<option value="/spindex/185.shtml">185 Sudowoodo

<option value="/spindex/186.shtml">186 Politoed

<option value="/spindex/187.shtml">187 Hoppip

<option value="/spindex/188.shtml">188 Skiploom

<option value="/spindex/189.shtml">189 Jumpluff

<option value="/spindex/190.shtml">190 Aipom

<option value="/spindex/191.shtml">191 Sunkern

<option value="/spindex/192.shtml">192 Sunflora

<option value="/spindex/193.shtml">193 Yanma

<option value="/spindex/194.shtml">194 Wooper

<option value="/spindex/195.shtml">195 Quagsire

<option value="/spindex/196.shtml">196 Espeon

<option value="/spindex/197.shtml">197 Umbreon

<option value="/spindex/198.shtml">198 Murkrow

<option value="/spindex/199.shtml">199 Slowking

<option value="/spindex/200.shtml">200 Misdreavus

<option value="/spindex/201.shtml">201 Unown

<option value="/spindex/202.shtml">202 Wobbuffet

<option value="/spindex/203.shtml">203 Girafarig

<option value="/spindex/204.shtml">204 Pineco

<option value="/spindex/205.shtml">205 Forretress

<option value="/spindex/206.shtml">206 Dunsparce

<option value="/spindex/207.shtml">207 Gligar

<option value="/spindex/208.shtml">208 Steelix

<option value="/spindex/209.shtml">209 Snubbull

<option value="/spindex/210.shtml">210 Granbull

<option value="/spindex/211.shtml">211 Qwilfish

<option value="/spindex/212.shtml">212 Scizor

<option value="/spindex/213.shtml">213 Shuckle

<option value="/spindex/214.shtml">214 Heracross

<option value="/spindex/215.shtml">215 Sneasel

<option value="/spindex/216.shtml">216 Teddiursa

<option value="/spindex/217.shtml">217 Ursaring

<option value="/spindex/218.shtml">218 Slugma

<option value="/spindex/219.shtml">219 Magcargo

<option value="/spindex/220.shtml">220 Swinub

<option value="/spindex/221.shtml">221 Piloswine

<option value="/spindex/222.shtml">222 Corsola

<option value="/spindex/223.shtml">223 Remoraid

<option value="/spindex/224.shtml">224 Octillery

<option value="/spindex/225.shtml">225 Delibird

<option value="/spindex/226.shtml">226 Mantine

<option value="/spindex/227.shtml">227 Skarmory

<option value="/spindex/228.shtml">228 Houndour

<option value="/spindex/229.shtml">229 Houndoom

<option value="/spindex/230.shtml">230 Kingdra

<option value="/spindex/231.shtml">231 Phanpy

<option value="/spindex/232.shtml">232 Donphan

<option value="/spindex/233.shtml">233 Porygon 2

<option value="/spindex/234.shtml">234 Stantler

<option value="/spindex/235.shtml">235 Smeargle

<option value="/spindex/236.shtml">236 Tyrogue

<option value="/spindex/237.shtml">237 Hitmontop

<option value="/spindex/238.shtml">238 Smoochum

<option value="/spindex/239.shtml">239 Elekid

<option value="/spindex/240.shtml">240 Magby

<option value="/spindex/241.shtml">241 Miltank

<option value="/spindex/242.shtml">242 Blissey

<option value="/spindex/243.shtml">243 Raikou

<option value="/spindex/244.shtml">244 Entei

<option value="/spindex/245.shtml">245 Suicune

<option value="/spindex/246.shtml">246 Larvitar

<option value="/spindex/247.shtml">247 Pupitar

<option value="/spindex/248.shtml">248 Tyranitar

<option value="/spindex/249.shtml">249 Lugia

<option value="/spindex/250.shtml">250 Ho-oh

<option value="/spindex/251.shtml">251 Celebi

</SELECT></FORM></td>

<td align="center" width="33%"> <FORM NAME="nav4"><DIV>

 <SELECT NAME="SelectURL" onChange="document.location.href=document.nav4.SelectURL.options[document.nav4.SelectURL.selectedIndex].value" style="color:#383838; font-size: 8pt; background:#CEBC77" size=1>

 <OPTION><b>252-386

<option value="/spindex/252.shtml">252 Treecko

<option value="/spindex/253.shtml">253 Grovyle

<option value="/spindex/254.shtml">254 Sceptile

<option value="/spindex/255.shtml">255 Torchic

<option value="/spindex/256.shtml">256 Combusken

<option value="/spindex/257.shtml">257 Blaziken

<option value="/spindex/258.shtml">258 Mudkip

<option value="/spindex/259.shtml">259 Marshtomp

<option value="/spindex/260.shtml">260 Swampert

<option value="/spindex/261.shtml">261 Poochyena

<option value="/spindex/262.shtml">262 Mightyena

<option value="/spindex/263.shtml">263 Zigzagoon

<option value="/spindex/264.shtml">264 Linoone

<option value="/spindex/265.shtml">265 Wurmple

<option value="/spindex/266.shtml">266 Silcoon

<option value="/spindex/267.shtml">267 Beautifly

<option value="/spindex/268.shtml">268 Cascoon

<option value="/spindex/269.shtml">269 Dustox

<option value="/spindex/270.shtml">270 Lotad

<option value="/spindex/271.shtml">271 Lombre

<option value="/spindex/272.shtml">272 Ludicolo

<option value="/spindex/273.shtml">273 Seedot

<option value="/spindex/274.shtml">274 Nuzleaf

<option value="/spindex/275.shtml">275 Shiftry

<option value="/spindex/276.shtml">276 Taillow

<option value="/spindex/277.shtml">277 Swellow

<option value="/spindex/278.shtml">278 Wingull

<option value="/spindex/279.shtml">279 Pelipper

<option value="/spindex/280.shtml">280 Ralts

<option value="/spindex/281.shtml">281 Kirlia

<option value="/spindex/282.shtml">282 Gardevoir

<option value="/spindex/283.shtml">283 Surskit

<option value="/spindex/284.shtml">284 Masquerain

<option value="/spindex/285.shtml">285 Shroomish

<option value="/spindex/286.shtml">286 Breloom

<option value="/spindex/287.shtml">287 Slakoth

<option value="/spindex/288.shtml">288 Vigoroth

<option value="/spindex/289.shtml">289 Slaking

<option value="/spindex/290.shtml">290 Nincada

<option value="/spindex/291.shtml">291 Ninjask

<option value="/spindex/292.shtml">292 Shedinja

<option value="/spindex/293.shtml">293 Whismur

<option value="/spindex/294.shtml">294 Loudred

<option value="/spindex/295.shtml">295 Exploud

<option value="/spindex/296.shtml">296 Makuhita

<option value="/spindex/297.shtml">297 Hariyama

<option value="/spindex/298.shtml">298 Azurill

<option value="/spindex/299.shtml">299 Nosepass

<option value="/spindex/300.shtml">300 Skitty

<option value="/spindex/301.shtml">301 Delcatty

<option value="/spindex/302.shtml">302 Sableye

<option value="/spindex/303.shtml">303 Mawile

<option value="/spindex/304.shtml">304 Aron

<option value="/spindex/305.shtml">305 Lairon

<option value="/spindex/306.shtml">306 Aggron

<option value="/spindex/307.shtml">307 Meditite

<option value="/spindex/308.shtml">308 Medicham

<option value="/spindex/309.shtml">309 Electrike

<option value="/spindex/310.shtml">310 Manectric

<option value="/spindex/311.shtml">311 Plusle

<option value="/spindex/312.shtml">312 Minun

<option value="/spindex/313.shtml">313 Volbeat

<option value="/spindex/314.shtml">314 Illumise

<option value="/spindex/315.shtml">315 Roselia

<option value="/spindex/316.shtml">316 Gulpin

<option value="/spindex/317.shtml">317 Swalot

<option value="/spindex/318.shtml">318 Carvanha

<option value="/spindex/319.shtml">319 Sharpedo

<option value="/spindex/320.shtml">320 Wailmer

<option value="/spindex/321.shtml">321 Wailord

<option value="/spindex/322.shtml">322 Numel

<option value="/spindex/323.shtml">323 Camerupt

<option value="/spindex/324.shtml">324 Torkoal

<option value="/spindex/325.shtml">325 Spoink

<option value="/spindex/326.shtml">326 Grumpig

<option value="/spindex/327.shtml">327 Spinda

<option value="/spindex/328.shtml">328 Trapinch

<option value="/spindex/329.shtml">329 Vibrava

<option value="/spindex/330.shtml">330 Flygon

<option value="/spindex/331.shtml">331 Cacnea

<option value="/spindex/332.shtml">332 Cacturne

<option value="/spindex/333.shtml">333 Swablu

<option value="/spindex/334.shtml">334 Altaria

<option value="/spindex/335.shtml">335 Zangoose

<option value="/spindex/336.shtml">336 Seviper

<option value="/spindex/337.shtml">337 Lunatone

<option value="/spindex/338.shtml">338 Solrock

<option value="/spindex/339.shtml">339 Barboach

<option value="/spindex/340.shtml">340 Whiscash

<option value="/spindex/341.shtml">341 Corphish

<option value="/spindex/342.shtml">342 Crawdaunt

<option value="/spindex/343.shtml">343 Baltoy

<option value="/spindex/344.shtml">344 Claydol

<option value="/spindex/345.shtml">345 Lileep

<option value="/spindex/346.shtml">346 Cradily

<option value="/spindex/347.shtml">347 Anorith

<option value="/spindex/348.shtml">348 Armaldo

<option value="/spindex/349.shtml">349 Feebas

<option value="/spindex/350.shtml">350 Milotic

<option value="/spindex/351.shtml">351 Castform

<option value="/spindex/352.shtml">352 Kecleon

<option value="/spindex/353.shtml">353 Shuppet

<option value="/spindex/354.shtml">354 Banette

<option value="/spindex/355.shtml">355 Duskull

<option value="/spindex/356.shtml">356 Dusclops

<option value="/spindex/357.shtml">357 Tropius

<option value="/spindex/358.shtml">358 Chimecho

<option value="/spindex/359.shtml">359 Absol

<option value="/spindex/360.shtml">360 Wynaut

<option value="/spindex/361.shtml">361 Snorunt

<option value="/spindex/362.shtml">362 Glalie

<option value="/spindex/363.shtml">363 Spheal

<option value="/spindex/364.shtml">364 Sealeo

<option value="/spindex/365.shtml">365 Walrein

<option value="/spindex/366.shtml">366 Clamperl

<option value="/spindex/367.shtml">367 Huntail

<option value="/spindex/368.shtml">368 Gorebyss

<option value="/spindex/369.shtml">369 Relicanth

<option value="/spindex/370.shtml">370 Luvdisc

<option value="/spindex/371.shtml">371 Bagon

<option value="/spindex/372.shtml">372 Shellgon

<option value="/spindex/373.shtml">373 Salamence

<option value="/spindex/374.shtml">374 Beldum

<option value="/spindex/375.shtml">375 Metang

<option value="/spindex/376.shtml">376 Metagross

<option value="/spindex/377.shtml">377 Regirock

<option value="/spindex/378.shtml">378 Regice

<option value="/spindex/379.shtml">379 Registeel

<option value="/spindex/380.shtml">380 Latias

<option value="/spindex/381.shtml">381 Latios

<option value="/spindex/382.shtml">382 Kyogre

<option value="/spindex/383.shtml">383 Groudon

<option value="/spindex/384.shtml">384 Rayquaza

<option value="/spindex/385.shtml">385 Jirachi

<option value="/spindex/386.shtml">386 Deoxys

<option value="/spindex/387.shtml">??? Munchlax

</SELECT></FORM></td>

</tr></table>
<table align=center width="95%" border="0" cellspacing="0" cellpadding="0">

<tr>

<td align="center" width="50%"><FORM NAME="nav5"><DIV>

 <SELECT NAME="SelectURL" onChange="document.location.href=document.nav5.SelectURL.options[document.nav5.SelectURL.selectedIndex].value" style="color:#383838; font-size: 8pt; background:#CEBC77" size=1>

 <OPTION>Ranger Browser: 001-105
<option value="/spindex/001.shtml">R-001 Bulbasaur
<option value="/spindex/002.shtml">R-002 Ivysaur
<option value="/spindex/003.shtml">R-003 Venusaur
<option value="/spindex/069.shtml">R-004 Bellsprout
<option value="/spindex/070.shtml">R-005 Weepinbell
<option value="/spindex/071.shtml">R-006 Victreebel
<option value="/spindex/152.shtml">R-007 Chikorita
<option value="/spindex/153.shtml">R-008 Bayleef
<option value="/spindex/154.shtml">R-009 Meganium
<option value="/spindex/187.shtml">R-010 Hoppip
<option value="/spindex/258.shtml">R-011 Mudkip
<option value="/spindex/259.shtml">R-012 Marshtomp
<option value="/spindex/260.shtml">R-013 Swampert
<option value="/spindex/079.shtml">R-014 Slowpoke
<option value="/spindex/255.shtml">R-015 Torchic
<option value="/spindex/256.shtml">R-016 Combusken
<option value="/spindex/257.shtml">R-017 Blaziken
<option value="/spindex/078.shtml">R-018 Rapidash
<option value="/spindex/155.shtml">R-019 Cyndaquil
<option value="/spindex/156.shtml">R-020 Quilava
<option value="/spindex/157.shtml">R-021 Typhlosion
<option value="/spindex/172.shtml">R-022 Pichu
<option value="/spindex/025.shtml">R-023 Pikachu
<option value="/spindex/026.shtml">R-024 Raichu
<option value="/spindex/015.shtml">R-025 Beedrill
<option value="/spindex/280.shtml">R-026 Ralts
<option value="/spindex/281.shtml">R-027 Kirlia
<option value="/spindex/282.shtml">R-028 Gardevoir
<option value="/spindex/063.shtml">R-029 Abra
<option value="/spindex/325.shtml">R-030 Spoink
<option value="/spindex/290.shtml">R-031 Nincada
<option value="/spindex/291.shtml">R-032 Ninjask
<option value="/spindex/292.shtml">R-033 Shedinja
<option value="/spindex/231.shtml">R-034 Phanpy
<option value="/spindex/232.shtml">R-035 Donphan
<option value="/spindex/276.shtml">R-036 Taillow
<option value="/spindex/277.shtml">R-037 Swellow
<option value="/spindex/149.shtml">R-038 Dragonite
<option value="/spindex/021.shtml">R-039 Spearow
<option value="/spindex/022.shtml">R-040 Fearow
<option value="/spindex/084.shtml">R-041 Doduo
<option value="/spindex/085.shtml">R-042 Dodrio
<option value="/spindex/123.shtml">R-043 Scyther
<option value="/spindex/212.shtml">R-044 Scizor
<option value="/spindex/227.shtml">R-045 Skarmory
<option value="/spindex/198.shtml">R-046 Murkrow
<option value="/spindex/263.shtml">R-047 Zigzagoon
<option value="/spindex/264.shtml">R-048 Linoone
<option value="/spindex/128.shtml">R-049 Tauros
<option value="/spindex/046.shtml">R-050 Paras
<option value="/spindex/047.shtml">R-051 Parasect
<option value="/spindex/060.shtml">R-052 Poliwag
<option value="/spindex/061.shtml">R-053 Poliwhirl
<option value="/spindex/062.shtml">R-054 Poliwrath
<option value="/spindex/186.shtml">R-055 Politoed
<option value="/spindex/081.shtml">R-056 Magnemite
<option value="/spindex/082.shtml">R-057 Magneton
<option value="/spindex/041.shtml">R-058 Zubat
<option value="/spindex/042.shtml">R-059 Golbat
<option value="/spindex/169.shtml">R-060 Crobat
<option value="/spindex/050.shtml">R-061 Diglett
<option value="/spindex/051.shtml">R-062 Dugtrio
<option value="/spindex/112.shtml">R-063 Rhydon
<option value="/spindex/074.shtml">R-064 Geodude
<option value="/spindex/075.shtml">R-065 Graveler
<option value="/spindex/076.shtml">R-066 Golem
<option value="/spindex/311.shtml">R-067 Plusle
<option value="/spindex/312.shtml">R-068 Minun
<option value="/spindex/114.shtml">R-069 Tangela
<option value="/spindex/098.shtml">R-070 Krabby
<option value="/spindex/341.shtml">R-071 Corphish
<option value="/spindex/342.shtml">R-072 Crawdaunt
<option value="/spindex/158.shtml">R-073 Totodile
<option value="/spindex/159.shtml">R-074 Croconaw
<option value="/spindex/160.shtml">R-075 Feraligatr
<option value="/spindex/007.shtml">R-076 Squirtle
<option value="/spindex/008.shtml">R-077 Wartortle
<option value="/spindex/009.shtml">R-078 Blastoise
<option value="/spindex/100.shtml">R-079 Voltorb
<option value="/spindex/066.shtml">R-080 Machop
<option value="/spindex/067.shtml">R-081 Machoke
<option value="/spindex/068.shtml">R-082 Machamp
<option value="/spindex/296.shtml">R-083 Makuhita
<option value="/spindex/297.shtml">R-084 Hariyama
<option value="/spindex/307.shtml">R-085 Meditite
<option value="/spindex/308.shtml">R-086 Medicham
<option value="/spindex/088.shtml">R-087 Grimer
<option value="/spindex/089.shtml">R-088 Muk
<option value="/spindex/109.shtml">R-089 Koffing
<option value="/spindex/096.shtml">R-090 Drowzee
<option value="/spindex/097.shtml">R-091 Hypno
<option value="/spindex/122.shtml">R-092 Mr. Mime
<option value="/spindex/127.shtml">R-093 Pinsir
<option value="/spindex/092.shtml">R-094 Gastly
<option value="/spindex/093.shtml">R-095 Haunter
<option value="/spindex/094.shtml">R-096 Gengar
<option value="/spindex/209.shtml">R-097 Snubbull
<option value="/spindex/300.shtml">R-098 Skitty
<option value="/spindex/052.shtml">R-099 Meowth
<option value="/spindex/039.shtml">R-100 Jigglypuff
<option value="/spindex/019.shtml">R-101 Rattata
<option value="/spindex/020.shtml">R-102 Raticate
<option value="/spindex/137.shtml">R-103 Porygon
<option value="/spindex/352.shtml">R-104 Kecleon
<option value="/spindex/143.shtml">R-105 Snorlax
</SELECT></FORM></td>

<td align="center" width="50%">

<FORM NAME="nav6"><DIV>

 <SELECT NAME="SelectURL" onChange="document.location.href=document.nav6.SelectURL.options[document.nav6.SelectURL.selectedIndex].value" style="color:#383838; font-size: 8pt; background:#CEBC77" size=1>

 <OPTION>Ranger Browser: 106-210


<option value="/spindex/131.shtml">R-106 Lapras
<option value="/spindex/116.shtml">R-107 Horsea
<option value="/spindex/117.shtml">R-108 Seadra
<option value="/spindex/230.shtml">R-109 Kingdra
<option value="/spindex/118.shtml">R-110 Goldeen
<option value="/spindex/119.shtml">R-111 Seaking
<option value="/spindex/120.shtml">R-112 Staryu
<option value="/spindex/121.shtml">R-113 Starmie
<option value="/spindex/223.shtml">R-114 Remoraid
<option value="/spindex/224.shtml">R-115 Octillery
<option value="/spindex/226.shtml">R-116 Mantine
<option value="/spindex/318.shtml">R-117 Carvanha
<option value="/spindex/319.shtml">R-118 Sharpedo
<option value="/spindex/320.shtml">R-119 Wailmer
<option value="/spindex/370.shtml">R-120 Luvdisc
<option value="/spindex/054.shtml">R-121 Psyduck
<option value="/spindex/278.shtml">R-122 Wingull
<option value="/spindex/279.shtml">R-123 Pelipper
<option value="/spindex/129.shtml">R-124 Magikarp
<option value="/spindex/130.shtml">R-125 Gyarados
<option value="/spindex/043.shtml">R-126 Oddish
<option value="/spindex/044.shtml">R-127 Gloom
<option value="/spindex/045.shtml">R-128 Vileplume
<option value="/spindex/252.shtml">R-129 Treecko
<option value="/spindex/253.shtml">R-130 Grovyle
<option value="/spindex/254.shtml">R-131 Sceptile
<option value="/spindex/270.shtml">R-132 Lotad
<option value="/spindex/271.shtml">R-133 Lombre
<option value="/spindex/272.shtml">R-134 Ludicolo
<option value="/spindex/322.shtml">R-135 Numel
<option value="/spindex/323.shtml">R-136 Camerupt
<option value="/spindex/126.shtml">R-137 Magmar
<option value="/spindex/218.shtml">R-138 Slugma
<option value="/spindex/219.shtml">R-139 Magcargo
<option value="/spindex/004.shtml">R-140 Charmander
<option value="/spindex/005.shtml">R-141 Charmeleon
<option value="/spindex/006.shtml">R-142 Charizard
<option value="/spindex/324.shtml">R-143 Torkoal
<option value="/spindex/058.shtml">R-144 Growlithe
<option value="/spindex/059.shtml">R-145 Arcanine
<option value="/spindex/309.shtml">R-146 Electrike
<option value="/spindex/310.shtml">R-147 Manectric
<option value="/spindex/214.shtml">R-148 Heracross
<option value="/spindex/056.shtml">R-149 Mankey
<option value="/spindex/057.shtml">R-150 Primeape
<option value="/spindex/023.shtml">R-151 Ekans
<option value="/spindex/024.shtml">R-152 Arbok
<option value="/spindex/048.shtml">R-153 Venonat
<option value="/spindex/265.shtml">R-154 Wurmple
<option value="/spindex/266.shtml">R-155 Silcoon
<option value="/spindex/267.shtml">R-156 Beautifly
<option value="/spindex/167.shtml">R-157 Spinarak
<option value="/spindex/168.shtml">R-158 Ariados
<option value="/spindex/330.shtml">R-159 Flygon
<option value="/spindex/207.shtml">R-160 Gligar
<option value="/spindex/229.shtml">R-161 Houndoom
<option value="/spindex/287.shtml">R-162 Slakoth
<option value="/spindex/288.shtml">R-163 Vigoroth
<option value="/spindex/289.shtml">R-164 Slaking
<option value="/spindex/371.shtml">R-165 Bagon
<option value="/spindex/372.shtml">R-166 Shelgon
<option value="/spindex/373.shtml">R-167 Salamence
<option value="/spindex/124.shtml">R-168 Jynx
<option value="/spindex/338.shtml">R-169 Solrock
<option value="/spindex/202.shtml">R-170 Wobbuffet
<option value="/spindex/356.shtml">R-171 Dusclops
<option value="/spindex/220.shtml">R-172 Swinub
<option value="/spindex/221.shtml">R-173 Piloswine
<option value="/spindex/361.shtml">R-174 Snorunt
<option value="/spindex/362.shtml">R-175 Glalie
<option value="/spindex/293.shtml">R-176 Whismur
<option value="/spindex/294.shtml">R-177 Loudred
<option value="/spindex/295.shtml">R-178 Exploud
<option value="/spindex/208.shtml">R-179 Steelix
<option value="/spindex/273.shtml">R-180 Seedot
<option value="/spindex/274.shtml">R-181 Nuzleaf
<option value="/spindex/275.shtml">R-182 Shiftry
<option value="/spindex/134.shtml">R-183 Vaporeon
<option value="/spindex/136.shtml">R-184 Flareon
<option value="/spindex/135.shtml">R-185 Jolteon
<option value="/spindex/196.shtml">R-186 Espeon
<option value="/spindex/197.shtml">R-187 Umbreon
<option value="/spindex/125.shtml">R-188 Electabuzz
<option value="/spindex/317.shtml">R-189 Swalot
<option value="/spindex/374.shtml">R-190 Beldum
<option value="/spindex/375.shtml">R-191 Metang
<option value="/spindex/376.shtml">R-192 Metagross
<option value="/spindex/246.shtml">R-193 Larvitar
<option value="/spindex/247.shtml">R-194 Pupitar
<option value="/spindex/248.shtml">R-195 Tyranitar
<option value="/spindex/333.shtml">R-196 Swablu
<option value="/spindex/334.shtml">R-197 Altaria
<option value="/spindex/142.shtml">R-198 Aerodactyl
<option value="/spindex/215.shtml">R-199 Sneasel
<option value="/spindex/359.shtml">R-200 Absol
<option value="/spindex/115.shtml">R-201 Kangaskhan
<option value="/spindex/244.shtml">R-202 Entei
<option value="/spindex/243.shtml">R-203 Raikou
<option value="/spindex/245.shtml">R-204 Suicune
<option value="/spindex/377.shtml">R-205 Regirock
<option value="/spindex/378.shtml">R-206 Regice
<option value="/spindex/379.shtml">R-207 Registeel
<option value="/spindex/382.shtml">R-208 Kyogre
<option value="/spindex/383.shtml">R-209 Groudon
<option value="/spindex/384.shtml">R-210 Rayquaza
<option value="/spindex/386.shtml">R-211 Deoxys
<option value="/spindex/251.shtml">R-212 Celebi
<option value="/spindex/151.shtml">R-213 Mew
</SELECT></FORM></td>

</tr></table>







<div align="center"><table  width="98%" border="1" cellspacing="0" cellpadding="4">
  <tr>
    <td width="80%"><table  width="100%" border="0" cellspacing="0" cellpadding="0">
  		<tr>
    		<td width="32" align="center"><img src="/dungeon2//018.png"></td>
		<td><font size="4"><b>&nbsp;#018 Pidgeot</b></font></td></tr></table></td>
    <td width="5%" align="center"><font size="1"><a href="#general">General</a></font></td>
    <td width="5%" align="center"><font size="1"><a href="#location">Location</a></font></td>
    <td width="5%" align="center"><font size="1"><a href="#attacks">Attacks</a></font></td>
    <td width="5%" align="center"><font size="1"><a href="#tms">TMs</a></font></td>
    <td width="32" align="center"><a href="/pokedex-dp/018.shtml"><img src="/pokedex-rs/icon/018.gif" border="0"></a></td>
  </tr>
</table><p>
<a name="general"></a><table  width="98%" border="1" bordercolor="#868686" cellspacing="0" cellpadding="4">
	<tr>
		<td>
		<b>Pok&eacute;mon Game Picture</b>
		</td>
		<td>
		<b>National No.</b>
		</td>
		<td>
		<b>Browser No.</b>
		</td>
		<td >
		<b>English name</b>
		</td>
		<td >
		<b>Japanese Name</b>
		</td>
	</tr>
	<tr height="55">
		<td width="128" align="center">
		<img src="/mysteriousdungeon/pokemon/018.png">		</td>
		<td >
		#018
		</td>
		<td >
		R---
		</td>
		<td >
		Pidgeot
		</td>
		<td >
		&#12500;&#12472;&#12519;&#12483;&#12488;<br />Pidgeott
		</td>
	</tr>
	<tr>
		<td colspan=5>
		<b>Ability: Keen Eye</b>
		</td>
	</tr>
	<tr>
		<td colspan=5>
		Pidgeot's Accuracy cannot be Lowered by Opponent
		</td>
	</tr>
	<tr>
		<td >
		<b>Classification</b>
		</td>
		<td >
		<b>Type 1</b>
		</td>
		<td >
		<b>Type 2</b>
		</td>
		<td >
		<b>Height</b>
		</td>
		<td >
		<b>Weight</b>
		</td>
	</tr>
	<tr>
		<td >
		Bird Pok&eacute;mon
		</td>
		<td >
		<div align="center"><a href="/pokedex-rs/normal.shtml"><img src="/pokedex-rs/type/normal.gif" border=0></a></div>
		</td>
		<td >
		<div align="center"><a href="/pokedex-rs/flying.shtml"><img src="/pokedex-rs/type/flying.gif" border=0></a></div>
		</td>
		<td >
		4'11"
		</td>
		<td >
		87.1 lbs
		</td>
	</tr>
	<tr>
		<td colspan=5>
		<div align="center"><b>Evolution Chain</b></div>
		</td>
	</tr>
	<tr>
		<td colspan=5>
		<div align="center"><a href="/spindex/016.shtml"><img src="/pokedex/evo/016.gif" border="0"></a>--Lv. 18--><a href="/spindex/017.shtml"><img src="/pokedex/evo/017.gif" border="0"></a>--Lv. 36--><a href="/spindex/018.shtml"><img src="/pokedex/evo/018.gif" border="0"></a></div>
		</td>
	</tr>
</table><p>


<table width="98%" cellspacing="0" cellpadding="4" bordercolor="#868686" border="1">
	<tbody><tr>
		<td colspan="2">
		<b>Mystery Dungeon 1 Info</b>
		</td>
	</tr>
	<tr>
		<td>
		<b>Body Size</b>
		</td>
		<td>
		<b>Friend Area</b>
		</td>
	</tr>
	<tr>
		<td align="center"><img src="/spindex/icon/size.png">		</td>
		<td align="center">
		<a href="/mysteriousdungeon/friendarea/03.shtml">Flyaway Forest</a>
		</td>
	</tr>
</tbody></table><p>
<a name="location"></a><table  width="98%" border="1" bordercolor="#868686" cellspacing="0" cellpadding="4">
	<tr>
		<td colspan="3" align="center">
		<b>Location</b>
		</td>
	</tr>
	<tr>
		<td align="center" width="15%">
		<b>Game</b>
		</td>
		<td align="center" width="15%">
		<b>Get Rate</b>
		</td>
		<td align="center" width="70%">
		<b>Obtainable Location</b>
		</td>
	</tr>
	<tr>
		<td align="left" width="15%">
		<font color="FE8432"><b>Trozei</b></font>
		</td>
		<td align="left" width="15%">
		Rare
		</td>
		<td align="left" width="70%">
		Endless Level 51<br>Endless Level 72<br>Forever Level 1<br>Mr. Who's Den
		</td>
	</tr>
	<tr>
		<td align="left" width="15%">
		<font color="FD3B3B"><b>Dungeon</b></font>
		</td>
		<td align="left" width="15%">
		Impossible
		</td>
		<td align="left" width="70%">
		Evolve Pidgeotto
		</td>
	</tr>
	<tr>
		<td align="left" width="15%">
		<font color="69DD01"><b>Ranger</b></font>
		</td>
		<td align="left" width="15%">
		-
		</td>
		<td align="left" width="70%">
		Pidgeot is not in Pokémon Ranger 		</td>
	</tr>
</table><p><a name="attacks"></a><table  width="98%" border="1" bordercolor="#868686" cellspacing="0" cellpadding="4"><thead><tr ><th colspan="10"><font color="#ffffff">Dungeon Level Up</th></tr><tr><th><font color="#ffffff">Level</th><th><font color="#ffffff">Attack Name</th><th><font color="#ffffff">Type</th><th><font color="#ffffff">Description</th></tr></thead><tbody><tr><td>&#8212;</td><td>Tackle</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td align="left">Charges the foe with a full- body tackle.</td></tr><tr><td>&#8212;</td><td>Sand-attack</td><td align="center"><div align="center"><img src="/pokedex-rs/type/ground.gif"></div></td><td align="left">Reduces the foe's accuracy by hurling sand in its face.</td></tr><tr><td>&#8212;</td><td>Gust</td><td align="center"><div align="center"><img src="/pokedex-rs/type/flying.gif"></div></td><td align="left">Strikes the foe with a gust of wind whipped up by wings.</td></tr><tr><td>&#8212;</td><td>Quick Attack</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td align="left">An extremely fast attack that always strikes first.</td></tr><tr><td>5</td><td>Sand-attack</td><td align="center"><div align="center"><img src="/pokedex-rs/type/ground.gif"></div></td><td align="left">Reduces the foe's accuracy by hurling sand in its face.</td></tr><tr><td>9</td><td>Gust</td><td align="center"><div align="center"><img src="/pokedex-rs/type/flying.gif"></div></td><td align="left">Strikes the foe with a gust of wind whipped up by wings.</td></tr><tr><td>13</td><td>Quick Attack</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td align="left">An extremely fast attack that always strikes first.</td></tr><tr><td>20</td><td>Whirlwind</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td align="left">Blows away the foe with wind and ends the battle.</td></tr><tr><td>27</td><td>Wing Attack</td><td align="center"><div align="center"><img src="/pokedex-rs/type/flying.gif"></div></td><td align="left">Strikes the foe with wings spread wide.</td></tr><tr><td>34</td><td>Featherdance</td><td align="center"><div align="center"><img src="/pokedex-rs/type/flying.gif"></div></td><td align="left">Envelops the foe with down to sharply reduce ATTACK.</td></tr><tr><td>48</td><td>Agility</td><td align="center"><div align="center"><img src="/pokedex-rs/type/psychic.gif"></div></td><td align="left">Relaxes the body to sharply boost SPEED.</td></tr><tr><td>62</td><td>Mirror Move</td><td align="center"><div align="center"><img src="/pokedex-rs/type/flying.gif"></div></td><td align="left">Counters the foe's attack with the same move.</td></tr></tbody></table><p><table  width="98%" border="1" bordercolor="#868686" cellspacing="0" cellpadding="4"><thead><tr ><th colspan="10"><a name="tms"><font color="#ffffff">TM & HM Attacks</font></a></th></tr><tr><th><font color="#ffffff">TM/HM #</th><th><font color="#ffffff">Attack Name</th><th><font color="#ffffff">Type</th><th><font color="#ffffff">Description</th></tr></thead><tbody><tr><td>TM06</td><td>Toxic</td><td align="center"><div align="center"><img src="/pokedex-rs/type/poison.gif"></div></td><td >Poisons the foe with an intensifying toxin.</td></tr><tr><td>TM10</td><td>Hidden Power</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >The effectiveness varies with the user.</td></tr><tr><td>TM11</td><td>Sunny Day</td><td align="center"><div align="center"><img src="/pokedex-rs/type/fire.gif"></div></td><td >Boosts the power of FIRE- type moves for 5 turns.</td></tr><tr><td>TM15</td><td>Hyper Beam</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >Powerful, but leaves the user immobile the next turn.</td></tr><tr><td>TM17</td><td>Protect</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >Evades attack, but may fail if used in succession.</td></tr><tr><td>TM18</td><td>Rain Dance</td><td align="center"><div align="center"><img src="/pokedex-rs/type/water.gif"></div></td><td >Boosts the power of WATER- type moves for 5 turns.</td></tr><tr><td>TM21</td><td>Frustration</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >An attack that is stronger if the TRAINER is disliked.</td></tr><tr><td>TM27</td><td>Return</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >An attack that increases in power with friendship.</td></tr><tr><td>TM32</td><td>Double Team</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >Creates illusory copies to raise evasiveness.</td></tr><tr><td>TM40</td><td>Aerial Ace</td><td align="center"><div align="center"><img src="/pokedex-rs/type/flying.gif"></div></td><td >An extremely speedy and unavoidable attack.</td></tr><tr><td>TM42</td><td>Facade</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >Boosts ATTACK when burned, paralyzed, or poisoned.</td></tr><tr><td>TM43</td><td>Secret Power</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >An attack with effects that vary by location.</td></tr><tr><td>TM44</td><td>Rest</td><td align="center"><div align="center"><img src="/pokedex-rs/type/psychic.gif"></div></td><td >The user sleeps for 2 turns, restoring HP and status.</td></tr><tr><td>TM45</td><td>Attract</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >Makes the opposite gender less likely to attack.</td></tr><tr><td>TM46</td><td>Thief</td><td align="center"><div align="center"><img src="/pokedex-rs/type/dark.gif"></div></td><td >While attacking, it may steal the foe's held item.</td></tr><tr><td>TM47</td><td>Steel Wing</td><td align="center"><div align="center"><img src="/pokedex-rs/type/steel.gif"></div></td><td >Strikes the foe with hard wings spread wide.</td></tr><tr><td>HM02</td><td>Fly</td><td align="center"><div align="center"><img src="/pokedex-rs/type/flying.gif"></div></td><td >Flies up on the first turn, then strikes the next turn.</td></tr><tr><td>DM01</td><td>Horizontal Cut</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >Inflicts Damage in 3 Directions</td></tr><tr><td>DM02</td><td>Vacuum Cut</td><td align="center"><div align="center"><img src="/pokedex-rs/type/normal.gif"></div></td><td >Inflicts 30 Damage to any Pokémon in the same room</td></tr></tbody></table><p>
</div>
</td>

        <td width="1%" height="86" valign="top" bgcolor="#507C36"><div id="menu">
<a href="/potw-swsh/"><img src="/Toolbar/headers/PotW.gif" border="0" width="140" height="27"></a></b><br />
<a href="/potw-swsh/065.shtml"><img src="/potw-swsh/065.jpg" border=0 alt="Pokémon of the Week" width="140"></a>
          <img src="/Toolbar/headers/NextInJapan.gif" border="0" width="140" height="27"></b><br />
<img border="0" src="/anime/NextOn/1130.jpg" width="140"><br />
Episode 1130<br />
<b>Operation: Dub Pikachu<br />Half Marshtomp</b><br />
<img border="0" src="/anime/NextOn/1130-i.jpg" width="140"><br />
Airdate: 16/10/2020<br />
         <img src="/Toolbar/headers/RecentlyUsa.gif" border="0" width="140" height="27"></font></b><br />
            <a href="/anime/epiguide/pokemon/1113.shtml"><img border="0" src="/1113.jpg" width="140"><br />
Episode 1113<br />
<b>A Little Rocket R &amp; R!</b><br />
<img src="/anime/synopsis.gif" border=0>Synopsis</a><br />
          <a href="/anime/pictures/pokemon/1113.shtml"><img src="/anime/pictures.gif" border=0>Pictures</a><br />
       <img src="/Toolbar/headers/ComingInUsa.gif" border="0" width="140" height="27"></font></b><br />
            <a href="/anime/epiguide/pokemon/1114.shtml"><img border="0" src="/1114.jpg" width="140"><br />
Episode 1114<br />
<b> 	A Battle Festival Exploding With Life! VS Mega Lucario!!</b><br />
Airdate: 12/2020</a><br />
          <a href="/anime/epiguide/pokemon/1114.shtml"><img src="/anime/synopsis.gif" border=0>Synopsis</a><br />
          <a href="/anime/pictures/pokemon/1114.shtml"><img src="/anime/pictures.gif" border=0>Pictures</a><br />
         <img src="/Toolbar/headers/SocialMedia.gif" border="0" width="140" height="27"></b><br />
<div align="center"><a href="http://www.facebook.com/SerebiiNetPage" target="blank"><img src="/Toolbar/headers/Facebook.png" border="0" width="30" alt="Facebook" /></a> <a href="http://www.twitter.com/SerebiiNet" target="blank"><img src="/Toolbar/headers/Twitter.png" border="0" width="30" alt="Twitter" /></a> <a href="http://www.youtube.com/serebiispp" target="blank"><img src="/Toolbar/headers/youtube.png" border="0" width="30" alt="YouTube" /></a> <a href="http://www.instagram.com/serebii" target="blank" rel="nofollow"><img src="/Toolbar/headers/instagram.png" border="0" width="30" alt="Instagram" /></a></div>
 <img src="/Toolbar/headers/Association.gif" border="0" width="140" height="27"></font></b><br />
          <div align="center"><a href="http://www.pocketmonsters.net/" target="blank" rel="nofollow"><img src="/Toolbar/pm.png" border="0" alt="#PM"></a><br /><a href="http://www.legendarypokemon.net/" target="blank" rel="nofollow"><img src="/Toolbar/lpoke.png" border="0" alt="Legendary Pokémon"></a><br /></div>

</td>
      </tr>
    </table>

    &nbsp;

      <center>
      <table border="1" cellpadding="0" cellspacing="0" style="border-collapse: collapse" width="93%" bordercolor="#000000">
        <tr>
          <td width="28%" bgcolor="#507C36" valign="top">
          <font SIZE="1" face="Verdana" color="#000000">All Content is

          ©Copyright of Serebii.net 1999-2019. | <a href="/privacy.shtml"><font color="#000000">Privacy Policy</font></a> | <a style="cursor:pointer" onclick="window.__cmp('showConsentModal')"><font color="#000000">Manage Cookie Settings</font></a><br />
Pokémon And All Respective Names are Trademark & &copy; of Nintendo 1996-2019</font></b></td>
          <td width="12%" bgcolor="#507C36" valign="top">

<div id="menu"><b>Navigation<br />
          </b><a href="javascript:history.back()">Back</a> - <a href="javascript:history.forward()">Forward</a> - <a href="#top">Top</a></div></td>
        </tr>
      </table>
      </center>
<br /><div align="center" style="height:102px"><div id="nn_lb2"></div></div>
<div id="celtra-reveal-wrapper" style="position:fixed; height: auto; width: 100%">
<div id="nn_1by1"></div>
</div>



</body>
</html>

        '''
    # Add Empty 'Ranger Info' table into html if it doesn't exist
    if not xhtml.partition('Ranger Info')[1]:
        ranger_info_insert = ['''
        <p>
<table width="98%" cellspacing="0" cellpadding="4" bordercolor="#868686" border="1">
	<tbody><tr>
		<td colspan="3">
		<b>Ranger Info</b>
		</td>
	</tr>
	<tr>
		<td align="center">
		<b>Type Group</b>
		</td>
		<td align="center">
		<b>Field Ability</b>
		</td>
		<td align="center">
		<b>Pkmn Assist</b>
		</td>
	</tr>
	<tr>
		<td align="center">
		-
		</td>
		<td align="center">
		-
		</td>
		<td align="center">
		-
		</td>
	</tr>
</tbody></table></p>
         ''']
        new_html_ranger = xhtml.partition('size.png">')[0] + \
                          xhtml.partition('size.png">')[1] + \
                          xhtml.partition('size.png">')[2].partition('</table>')[0] + \
                          xhtml.partition('size.png">')[2].partition('</table>')[1] +\
                          ranger_info_insert[0] + \
                          xhtml.partition('size.png">')[2].partition('</table>')[2]
        xhtml = new_html_ranger

    if not xhtml.partition('TM & HM Attacks')[1]:
        tm_info_insert = ['''
                <p><table  width="98%" border="1" bordercolor="#868686" cellspacing="0" cellpadding="4">
                <thead><tr ><th colspan="10"><a name="tms"><font color="#ffffff">TM & HM Attacks
                </font></a></th></tr><tr><th><font color="#ffffff">TM/HM #</th><th><font color="#ffffff">
                Attack Name</th><th><font color="#ffffff">Type</th><th><font color="#ffffff">
                Description</th></tr></thead><tbody><tr>
                </tr></tbody></table>
                ''']
        # Make it check for no tm/hm
        new_html_tm = xhtml.partition('Dungeon Level Up')[0] + \
                      xhtml.partition('Dungeon Level Up')[1] + \
                      xhtml.partition('Dungeon Level Up')[2].partition('</table><p>')[0] + \
                      xhtml.partition('Dungeon Level Up')[2].partition('</table><p>')[1] + \
                      tm_info_insert[0] + \
                      xhtml.partition('Dungeon Level Up')[2].partition('</table><p>')[2]
        xhtml = new_html_tm
        #print(xhtml)
    p = HTMLTableParser()  # Defining the HTMLTableParser object
    p.feed(xhtml)           # feeding the html contents in the HTMLTableParser object

    # Empty dicts to later add data to
    general_info_dict = {}
    mystery_dungeon_dict = {}
    ranger_dict = {}
    get_dict = {}
    level_up_moves_dict = {}
    tms_hms_dict = {}

    # Dictionary of dictionaries
    dicts = {6: general_info_dict,
             7: mystery_dungeon_dict,
             8: ranger_dict,
             9: get_dict,
             10: level_up_moves_dict,
             11: tms_hms_dict}

    dicts_names = ['', '', '', '', '', '',
                   'general_info_dict',
                   'mystery_dungeon_dict',
                   'get_dict',
                   'level_up_moves_dict',
                   'tms_hms_dict']

    # Remove unwanted rows of data, will probably remove and rework later
    def remove_unneeded_rows():
        for x in range(6, 11):
            if x != 6:
                del p.tables[x][0]

    # Prints a readable list of the contents of each dictionary in the console
    def print_dicts():
        print('\n------------------------------------------\n', 'pokemon number(change later)', '\n------------------------------------------')
        for print_i in range(6, 12):
            print('\n===|', dicts_names[print_i], '|===')
            for print_j in dicts[print_i].items():
                print(print_j)

    def save_as_csv():
        for dict_key in range(6, 12):
            pd.DataFrame(dicts[dict_key]).to_csv('out.csv', index=False)

    def generate():
        remove_unneeded_rows()
        # Might remove / rework later
        for x in range(6, 12):                          # Iterate 6 through 11; the keys to the dict values in 'dicts'
            for y in range(0, len(p.tables[x])-1, 2):
                if x == 6:
                    for lists_counter in range(1, 8, 2):
                        col_name = p.tables[x][lists_counter - 1]
                        if lists_counter in (1, 5):
                            for sublist_counter in range(5):
                                dicts[x][col_name[sublist_counter]] = p.tables[x][lists_counter][sublist_counter]
                        elif lists_counter == 7:
                            pass

                            dicts[x][col_name[0]] = p.tables[x][lists_counter][0]

                if x in (7, 8, 9, 10, 11):
                    for lists_counter in range(len(p.tables[x][0])):
                        nested_list = []

                        for moves_counter in range(len(p.tables[x])):
                            if x == 11:
                                    if not p.tables[x][2]:
                                        break
                            # Skip first row (Header)
                            if moves_counter > 0:
                                nested_list.append(p.tables[x][moves_counter][lists_counter])
                            dicts[x][p.tables[x][0][lists_counter]] = nested_list

                        if x == 7 and p.tables[x][0][lists_counter] == 'Body Size':
                            # Count number of 'size.png' in the html to determine if pokemon is size * or ****
                            size_count = xhtml.count('size.png')
                            dicts[x][p.tables[x][0][lists_counter]] = '*' * size_count

    generate()
    # For getting evo data from html
    def substring_after(s, word):
        substr = s.partition(word)[2]
        end_result = ''
        exceptions_list = [43, 44,  # Oddish Line
                           60, 61,  # Poliwag Line
                           79,      # Slowpoke Line
                           133,     # Eevee Line
                           236,     # Tyrogue
                           366,     # Clamperl
                           0]
        if int(dicts[6]['National No.'][1:]) not in exceptions_list:

            # Is there a non-level-up base pokemon evolution?
            if substr.partition('alt=')[2][1:8] != 'Pokémon' and not substr.partition('Lv. ')[1]:
                base_mon_alt = substr.partition('spindex/')[2][:3]
                base_evo_alt = substr.partition('alt="')[2].partition('"')[0][:100]
                stage1_mon_alt = substr.partition(base_evo_alt)[2].partition('spindex/')[2][:3]
                end_result += str(base_mon_alt) + ' --> ' + str(base_evo_alt) + ' --> ' + stage1_mon_alt

            # Is there a base pokemon level-up evolution?
            elif substr.partition('Lv.')[1]:
                base_mon_lv = substr.partition('evo/')[2][:3]
                base_evo_lv = 'Lv.' + substr.partition('Lv.')[2][:3]
                if base_evo_lv[-1] == '-':
                    base_evo_lv = base_evo_lv[:-1]
                stage1_mon_lv = substr.partition(base_evo_lv)[2].partition('spindex/')[2][:3]
                end_result += str(base_mon_lv) + ' --> ' + str(base_evo_lv) + ' --> ' + stage1_mon_lv

            if end_result != '':
                # Is there a stage 1 level-up evolution?
                if substr.partition(end_result[-3:])[2].partition('Lv.')[1]:
                    stage_1_evo_lv = 'Lv.' + substr.partition(end_result[-3:])[2].partition('Lv.')[2][:3]
                    stage2_mon = substr.partition(stage_1_evo_lv)[2].partition('spindex/')[2][:3]
                    end_result += ' --> ' + str(stage_1_evo_lv) + ' --> ' + str(stage2_mon)

                # Is there a stage 1 non-level-up evolution?
                elif substr.partition(end_result[-3:])[2].partition('alt=')[2][1:8] != 'Pokémon':
                    stage_1_evo_alt = substr.partition(end_result[-3:])[2].partition('alt="')[2].partition('"')[0][:100]
                    stage2_mon = substr.partition(stage_1_evo_alt)[2].partition('spindex/')[2][:3]
                    end_result += ' --> ' + str(stage_1_evo_alt) + ' --> ' + str(stage2_mon)

            if end_result == '':
                end_result = 'No Evolution'

            print(end_result)
        else:
            print('Skipping: ' + str(dicts[6]['National No.'][1:]))
    #substring_after(xhtml, 'Evolution Chain')

    # Change incorrect automatically generated Evolution Chain to correct data gathered with substring_after()
    f = open('evo_lines.csv') # (Deleted)
    lines = f.readlines()
    p.tables[6][7][0] = lines[int(url.partition('spindex/')[2][:3])-1][1:-2]

    with open('dex_part2.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        # Make new
        writer.writerow(['Ranger Browser No.', 'Ability_md', 'Height_ft', 'Weight_lvs', 'Evolution Chain', 'Body Size',
                         'Friend Area', 'Type Group', 'Field Ability', 'Pkmn Assist', 'get_trozei', 'location_trozei',
                         'get_md', 'location_md', 'location_ranger'])
        writer.writerow([p.tables[6][1][2], (p.tables[6][2][0][9:] + ': ' + p.tables[6][3][0]), p.tables[6][5][3],
                         p.tables[6][5][4], p.tables[6][7][0], dicts[7]['Body Size'], dicts[7]['Friend Area'][0],
                         dicts[8]['Field Ability'][0], dicts[8]['Pkmn Assist'][0], dicts[8]['Type Group'][0],
                         p.tables[9][1][1], p.tables[9][1][2], p.tables[9][2][1], p.tables[9][2][2], p.tables[9][3][2]])

    # Create levelup moves csv file if it doesn't exist
    if not os.path.exists(os.path.join('../PokemonMovesets', str(p.tables[6][1][1]) + '_levelup_moves.csv')):
        with open(os.path.join('../PokemonMovesets', str(p.tables[6][1][1]) + '_levelup_moves.csv'), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Level', 'Move'])

    # Create tm moves csv file if it doesn't exist
    if not os.path.exists(os.path.join('../PokemonMovesets', str(p.tables[6][1][1]) + '_tm_moves.csv')):
        with open(os.path.join('../PokemonMovesets', str(p.tables[6][1][1]) + '_tm_moves.csv'), 'w', newline='') as file:
            pass

    # Levelup moves
    for lv_move in range(1, len(p.tables[10])):
        with open(os.path.join('../PokemonMovesets', str(p.tables[6][1][1]) + '_levelup_moves.csv'), 'a+', newline='') as file:
            if open(os.path.join('../PokemonMovesets', str(p.tables[6][1][1]) + '_levelup_moves.csv'), 'r').read().find(p.tables[10][lv_move][1]) == -1:
                writer = csv.writer(file)
                writer.writerow([p.tables[10][lv_move][0], p.tables[10][lv_move][1]])

        # print('lv_' + p.tables[10][lv_move][0], '=', p.tables[10][lv_move][1])         # lv - move name

        # Add to move_descriptions if not already there
        with open('../csv/move_descriptions.csv', 'a+', newline='') as file:
            if open('../csv/move_descriptions.csv', 'r').read().find(p.tables[10][lv_move][1]) == -1:
                writer = csv.writer(file)
                writer.writerow([p.tables[10][lv_move][1], p.tables[10][lv_move][3]])
            else:
                # print('Skipping:', p.tables[10][lv_move][1], "because it already exists in file")
                pass

    # TM Moves
    for lv_move in range(1, len(p.tables[11])):
        if p.tables[11][2]:
            # Add tm moveset data to csv if not already there
            with open(os.path.join('../PokemonMovesets', str(p.tables[6][1][1]) + '_tm_moves.csv'), 'a+', newline='') as file:
                if open(os.path.join('../PokemonMovesets', str(p.tables[6][1][1]) + '_tm_moves.csv'), 'r').read().find(p.tables[11][lv_move][1]) == -1:
                    writer = csv.writer(file)
                    writer.writerow([p.tables[11][lv_move][0], p.tables[11][lv_move][1]])

            # print('tm_' + p.tables[11][lv_move][0], '=', p.tables[11][lv_move][1])        # lv - move name

            # Add to move_descriptions if not already there
            with open('../csv/move_descriptions.csv', 'a+', newline='') as file:
                if open('../csv/move_descriptions.csv', 'r').read().find(p.tables[11][lv_move][1]) == -1:
                    writer = csv.writer(file)
                    writer.writerow([p.tables[11][lv_move][1], p.tables[11][lv_move][3]])
                    print('adding move / description:', p.tables[11][lv_move][1], p.tables[11][lv_move][3])
                else:
                    # print('Skipping:', p.tables[10][lv_move][1], "because it already exists in file")
                    pass


    # === Save to CSV ===
    #pd.DataFrame(dicts[6]).to_csv('out.csv', index=False)

    # Connect to Database
    #if __name__ == '__main__':
        #connect()


def go_through_pokedex(first_pokemon_number, last_pokemon_number):
    for current_number in range(first_pokemon_number, last_pokemon_number+1):
        print('Current number:', current_number)
        if current_number < 10:
            main('https://www.serebii.net/spindex/00' + str(current_number) + '.shtml', 'cp1252')
        elif 10 <= current_number < 100:
            main('https://www.serebii.net/spindex/0' + str(current_number) + '.shtml', 'cp1252')
        else:
            main('https://www.serebii.net/spindex/' + str(current_number) + '.shtml', 'cp1252')

go_through_pokedex(386, 386)
