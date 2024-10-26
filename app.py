from flask import Flask, render_template, url_for, request
import random
import google.generativeai as genai
import os
usernames=[]
app = Flask(__name__)
import google.generativeai as genai

genai.configure(api_key='AIzaSyBBb5lsruycrNh6DmOfY80yZmiFE5UgDd8')
model = genai.GenerativeModel("gemini-1.5-flash")
takeid=0
name='John'
username='johnthedon'
intrest='Reading'
charecter='Viking'
theme='Cyberpunk'
superpower='Flash'
stories=[]
# Function to generate a random story
def generate_random_story():
    characters = [
    "Aldor the Unyielding Warrior", 
    "Eldara the Ancient Mage", 
    "Lira the Shadow Rogue", 
    "Thorin the Noble Paladin", 
    "Seraphine the Eagle-Eyed Archer", 
    "Maelis the Dark Sorcerer", 
    "Aurelia the Nature Priestess", 
    "Balrik the Cunning Thief", 
    "Draven the Exiled King", 
    "Kaelan the Wandering Bard"
    ]

    actions = [
    "Setting out on a ship bound for uncharted waters, they sailed to the edge of the known world, where storms raged, and the sea grew darker than night. After days adrift in fog and ghostly silence, they arrived at the Abyss—a place whispered of in tales. The waters cascaded into an endless void, and as they peered over the edge, strange whispers filled the air, hinting at realms beyond. They returned forever changed, carrying a fragment of the unknown in their soul, an understanding that the world was far stranger and larger than anyone could ever imagine.", 
    "In the heart of a dormant volcano lay the Eternal Flame, a fire said to grant immortality. Guarding it was a creature of ancient power, forged from molten rock and fury. After a grueling battle, they struck down the guardian, and the flame dimmed for a moment before blazing brighter than ever. Standing in its light, they felt the weight of time shift, as if gazing into eternity itself. They could feel the flame’s energy hum within them, promising life beyond life. But the price of immortality would become a riddle to solve for all eternity.", 
    "Venturing into the Labyrinth of Lost Souls, a twisting maze filled with echoes of despair, they braved the voices of those who had wandered in before and never escaped. Shadows shifted, and walls seemed to breathe as the cries of lost souls grew louder. Finally, in the labyrinth's heart, they found the Spirit Stone, which held the memories of every soul lost there. With the stone in hand, they traced their steps back, knowing the lives of countless souls had been entrusted to them. Leaving, they felt the burden of endless memories trailing them like shadows.", 
    "In a valley untouched by time, they discovered a place where ancient spirits lay imprisoned, bound by spells long since faded from memory. Whispering incantations, they freed the spirits, who rose like mist, grateful and mournful all at once. Each spirit shared its story, fragments of a forgotten age of peace and beauty. But as the last spirit faded, a darkness awoke within the valley—a warning that with the spirits’ freedom, an ancient enemy had also been stirred, one now set to haunt the world once more.", 
    "After a journey through frozen wastelands and blizzards, they reached the Icebound Fortress, a towering structure carved from glacier stone and sealed by powerful magic. Within its frigid walls, legends claimed, lay the lost Crown of Winters. Battling creatures of ice and frost, they pressed on to the throne room, where the crown lay encased in crystal. With one touch, the fortress began to tremble as ancient magics reawakened. The power of winter itself pulsed within them, binding their fate to the icy lands and their unforgiving cold.", 
    "Hidden deep within a mountain, they found the Oracle's Sanctuary, a sacred place where visions of past and future merged. As they entered, the air was thick with shimmering lights, each a glimpse of a moment in time. The Oracle, an ancient seer, granted them a vision—a glimpse of their destiny and a warning of betrayal to come. The visions twisted and overlapped, each one more cryptic than the last, and they left with an understanding that their future would demand choices they could scarcely imagine.", 
    "In a dense forest rumored to be alive with sentient trees and ancient magic, they encountered the Wildwood Spirits, protective beings made of bark and vine. The forest was restless, whispering in forgotten tongues, stirring as if in pain. Through song and incantation, they soothed the spirits, bringing a sense of peace to the forest. As dawn broke, they felt a bond with the forest, knowing it would guard them in times of need. But as they left, an unease lingered—an ancient warning of forces stirring that even the forest might not withstand.", 
    "On a cloudless night, they climbed the tallest peak and stole a fragment of the Moon’s Tear, a rare gem that shone with ethereal light. Said to grant wishes at great cost, the Moon’s Tear was coveted by many. As they held it, they felt its pull—visions of possible futures, of power and loss, flickering before them. But with each vision, a shadow grew within, for the Tear’s wishes came with an irreversible price. With it in hand, they descended, knowing they now held the weight of their own fate—and that of others—in their hands.", 
    "Traveling through swamps thick with fog and decay, they finally faced the Lich King, an ancient sorcerer who ruled the Black Marsh. After a fierce battle of both magic and wits, they vanquished him, shattering his amulet that held the souls of his victims. As the amulet broke, the marsh sighed in relief, and the souls ascended, free at last. Yet, in the silence that followed, they felt a chill, a reminder that such darkness leaves its mark on those who conquer it, and that the Lich’s magic would linger in the land.", 
    "Sailing the Tempest Sea, where storms roared and the waters themselves seemed alive, they encountered the Storm Spirits. Their power lay in chaos, stirring waves and winds with a flick of a finger. The negotiation was tense, the spirits capricious and demanding. After hours of bargaining, an accord was reached: safe passage through the storms, but at a future cost. Leaving the Tempest Sea, they felt a strange sense of calm, knowing the spirits’ favor was fleeting, and that one day, the sea would call upon them to fulfill their part of the bargain."
    ]

    consequences = [
    "Having achieved their victory, they returned to find themselves haunted by an ancient curse, a lingering shadow that whispered secrets and demands. This curse tied their fate to the deeds they had performed, casting shadows over even the brightest moments. Each step forward reminded them of what they’d lost and the sacrifice they’d made. Though the world hailed them as a hero, they alone bore the curse’s silent toll, watching as those around them aged while they remained frozen in a strange stasis, bound forever to a pact they had unknowingly sealed.", 
    "Having disturbed forces that should have remained dormant, they found themselves pursued by shadows that whispered of vengeance. These phantoms lurked in corners and appeared at twilight, each one a reminder of the cost of their actions. Though friends and allies sought to help, only they could see the shadows, which seemed drawn to their every move. Every quiet moment became a test, a reminder of what they had awakened, and a haunting promise that the past would not be so easily forgotten.", 
    "In return for their sacrifice, they were granted the gift of vision, seeing beyond the present moment into possible futures. The gift, though powerful, was not without its burdens, as they glimpsed the suffering and joy of countless lives, events that they were powerless to change. As they walked among others, they could see moments of loss, love, and betrayal flicker around them. With every vision, their heart grew heavier, burdened by the knowledge that they were both blessed and cursed to witness time’s inexorable flow.", 
    "After conquering the Eternal Flame, they found its warmth burned within them, gifting them life beyond life. But the flame came with a cost, for they could not escape the endless passage of time. Friends grew old, while they remained unchanged, bearing witness to countless generations. The flame’s light in their eyes marked them as different, and in time, they became a stranger in their own land. Though they lived, they carried the sorrow of a soul that had seen centuries pass, knowing that the gift of life could be its own kind of prison.", 
    "Having earned the trust of the ancient spirits, they found themselves bound to the land, their life entwined with the cycles of nature. Seasons changed, and they felt each one within their own bones. As the land thrived, so did they; but with every drought or blight, they weakened. In exchange for the spirits’ aid, they could never leave the forest’s reach. They became its guardian, eternally watching over its creatures and trees, a mortal soul made part of an ageless realm, forever at the mercy of the land they had vowed to protect.", 
    "Having walked the Labyrinth of Lost Souls, they emerged carrying the memories of those who had perished within. The voices of the lost echoed in their dreams, filling their nights with fragmented memories and pleas for peace. Every step brought a reminder of the lives that had been taken, and though they carried on, they felt the weight of countless souls pressing upon their heart. The labyrinth’s secrets had seeped into their mind, and with each whisper, they felt a piece of themselves slipping into the shadows, lost to the maze forever.", 
    "Having struck a deal with the Storm Spirits, they bore a mark upon their skin, a symbol of the spirits' favor and their obligation. They became attuned to the shifting weather, feeling every gust of wind and drop of rain as if it were a heartbeat. The storm was now part of them, a companion that would never leave. Yet, they knew the spirits were watching, waiting for the day when they would demand repayment. Until that time, they lived in the eye of the storm, both calm and turbulent, a mortal forever bound to nature’s untamed fury.", 
    "The Oracle’s vision had shown them their destiny, but as they returned, the visions persisted, appearing at random moments with blinding clarity. Each one offered glimpses of the future, of paths not yet taken. But with each vision, a sense of dread grew, for they knew not all paths could end well. The visions had a mind of their own, refusing to show the full picture, and they were left haunted by fragments of what might come, their mind a battleground between the known and unknown, haunted by futures they could neither embrace nor escape.", 
    "In the wake of their victory, they found the celebration hollow, for they had lost a dear friend along the way. Memories of laughter and shared battles now felt bittersweet, as the absence of their companion weighed heavily on their heart. Every victory felt incomplete, tainted by the realization that true joy could only be shared. The world saw a hero, but all they could feel was the ache of a soul left behind, a reminder that even the greatest victories demand sacrifices that echo long after the battles have ended.", 
    "After conquering the Icebound Fortress, they felt the chill of winter linger within them. The frost had entered their veins, and they found warmth scarce even under the sun. Seasons passed, yet the cold never left, marking them as something apart from others. Though they held the power of winter, they paid the price in isolation, their touch a reminder of the fortress they had conquered. They became a living embodiment of winter’s beauty and solitude, a force that could bring both life and death, forever bound to the icy magic they now carried within."
    ]
    character = random.choice(characters)
    action = random.choice(actions)
    consequence = random.choice(consequences)

    return f"The {character} {action}, {consequence}."
def generate_ai(stories, profile, takeids):
    global takeid
    if str(takeids)=='0':
        response = model.generate_content("Hello gemini you are assigned to generate a fantasy story based on the given charectrestics the story should consist of 300 words the least, charecter is "+profile["character_class"]+" ,theme is "+profile["theme"]+" ,interest is"+profile['intrest']+" ,superpower is"+profile['superpower']+".just give me the story only no other answers are needed, the story should be complete with a twist, make sure the story is more humanized with less literature terms")
    else:
        print(takeids)
        for i in stories:
            print(str(i['id']))
            if str(takeids)==str(i['id']):
                maga=i['story']
        response = model.generate_content("Hello gemini you are assigned to generate a fantasy story based on the given charectrestics the story should consist of 300 words the least, charecter is "+profile["character_class"]+" ,theme is "+profile["theme"]+" ,interest is"+profile['intrest']+". also add a new charecter based on the given description as a friend or foe in the given story,"+maga+". just give me the story only no other answers are needed,  the story should be complete with a twist , make sure the story is more humanized with less literature terms")
    takeid=0
    maga=''
    return response.text

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/story_feed', methods = ['POST', 'GET'])
def story_feed():
    # Initial stories data
    global takeid
    global stories
    if stories:
        manaosas='dsakfnfk'
    else:
        stories = [
            {"id": 1, "author": "Alice", "story": generate_random_story(), "likes": 15, "comments": 3, "connections": []},
            {"id": 2, "author": "Bob", "story": generate_random_story(), "likes": 8, "comments": 1, "connections": []},
            {"id": 3, "author": "Charlie", "story": generate_random_story(), "likes": 23, "comments": 7, "connections": []}
        ]
    profile = {
        "name": name,
        "username": username,
        "theme": theme,
        "character_class": charecter,
        "intrest": intrest,
        "superpower": superpower,
        "stories": 15,
        "followers": 230,
        "following": 185,
        "connections": []
    }
    if request.form.get("btn1", "my default")=="Connect":
        if request.method == 'POST':
            names = str(request.form.get('man',0))
            takeid = names
            print(takeid)
            storyd =generate_ai(stories, profile, takeid)
            stories.append({"id": random.randint(4, 100) , "author":'You', "story": storyd, "likes":random.randint(4, 100), "comments":random.randint(4, 15), "connections": []})
    if request.form.get("btn1", "my default")=="Genrate Story":
        if request.method == 'POST':
            storyd =generate_ai(stories, profile, takeid)
            stories.append({"id": random.randint(4, 100) , "author":'You', "story": storyd, "likes":random.randint(4, 100), "comments":random.randint(4, 15), "connections": []})
    return render_template('story_feed.html', stories=stories, profile=profile)

@app.route('/profile')
def profile():
    global name
    global username
    global theme
    global intrest
    global charecter
    global superpower
    return render_template('profile.html',name=name, username=username, theme=theme, intrest=intrest, charecter=charecter, superpower=superpower)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    global name
    global username
    global theme
    global intrest
    global charecter
    global superpower
    if request.method == 'POST':
        name = str(request.form.get('name1', 0))
        username = str(request.form.get('username1', 0))
        theme = str(request.form.get('theme1', 0))
        intrest = str(request.form.get('intrest1', 0))
        charecter = str(request.form.get('charecter1', 0))
        superpower = str(request.form.get('superpower1', 0))
    return render_template('edit.html', name=name, username=username, theme=theme, intrest=intrest, charecter=charecter,superpower=superpower)


@app.route('/messages')
def messages():
    return render_template('messages.html')
if __name__ == '__main__':
    app.run(debug=True)
