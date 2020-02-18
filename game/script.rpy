define e = Character("Eva", color="#b83040")
define d= Character("Dawn", color="#f08da9")
define u= Character("You", color="#49c4d1")
define t= Character("Teacher", color="#47ba88")


transform slightleft:
    xalign 0.25
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0
transform move_slide_left:
    xalign .5 yalign 1.0
    linear 2.0 xalign 0.0
transform move_slide_zoom:
    xalign .5 yalign 1.0
    linear 1.0 xalign 0.0
transform move_slide_left_from_left:
    xalign .25 yalign 1.0
    linear 1.0 xalign 0.0
transform move_slide_right_from_right:
    xalign .75 yalign 1.0
    linear 1.0 xalign 0.0

#day 1

label start:
    $ mean = False
    $ sweaty = 0
    $ daffect = 0
    $ eaffect = 0
    $ chosed = False
    $ chosed2 = False

    scene classroom

    t "Hey class, just wanted to remind you all that there is a test tomorrow."
    t "I've arranged study groups for all of you."
    "The teacher points at you."
    t "You are with..."
    show dnormal at slightleft
    t "Dawn,"
    show enormal at slightright
    t "and Eva."

    u "Ummmm hi?"
    e "Who are you again?"
    e "Ugh, I hope you guys don't actually expect me to study."
    d "Oh, this is an interesting group..."
    "I should ask them about the homework, but who should I ask?"
    menu:
        "Dawn":
            jump hwkdawn
        "Eva":
            jump hwkeva
label hwkdawn:
    hide enormal
    hide dnormal
    show dnormal
    u "Do you understand #3 on the homework?"
    d "Uhh I think so. Let's compare answers."
    "You look at her assignment. It looks like you guys did the same steps,
    but her final answer is different."
    u "I think you may have added wrong here."
    hide dnormal
    show dflushed

    d "Oh gosh! I'm so stupid, sorry!"
    d "I can't believe I made such a simple mistake."
    menu:
        "Don't worry about it!":
            u "Don't worry about it, Dawn. It happens!"
            hide dflushed
            show dnormal
            "Dawn smiles at you."
            pause .5
            $ daffect += 1
        "That is unfortunate.":
            u "Wow, that's unfortunate."
            hide dflushed
            show dsweaty
            d "Sorry...."
    $ chosed = True
    jump endday1

label hwkeva:
    hide dnormal
    hide enormal
    show enormal
    u "Do you understand #3 on the homework?"
    e "I haven't started yet. Did you expect me to start it when it's not even due?"
    u "Do you want help with it?"
    hide enormal
    show eflushed
    e "I can do it by myself."
    menu:
        "Oh, okay.":
            u "Oh, okay. Let me know if you need help."
            $ eaffect += 1
        "Do you even know what we're doing?":
            u "Do you even know what we're doing in class?"
            $ mean = True
            hide eflushed
            show esweaty
            e "Shut up."
    jump endday1

label endday1:
    "The bell rings."
    t "Alright guys pack up. Class dismissed."
    hide esweaty
    hide eflushed
    hide dflushed
    if chosed:
        jump dmeeting
    else:
        jump emeeting


label dmeeting:
    scene corridor
    show dflushed
    d "W-what are you doing here!?"
    menu:
        "Uhhh... going home?":
            u "Uhhh... going home?"
            jump dmeetingOFC
        "What are you doing here?":
            u "What are you doing here?"
            jump dmeetinghome

label dmeetingOFC:
    hide dflushed
    show dsweaty
    d "Oh...yeah...AHHH I'M SUCH A DUMMY I'M SO SORRY!"
    jump dmeetingfinal

label dmeetinghome:
    d "G-going home, obviously!"
    jump dmeetingfinal

label dmeetingfinal:
    d "..."
    d "S-so..."
    d "I was wondering..."
    d "..."
    hide dflushed
    hide dsweaty
    show dsweaty
    d "Doyoumaybewanttostudywithmeinacoupledays?"

    menu:
        "Yes":
            u "Yeah, I'd love to."
            $ daffect += 1
            hide dsweaty
            jump day1end
        "No":
            u "Sorry, I have plans."
            d "O-Okay, sorry to bother you."
            "You start to get hungry, and decide to head to a cafe."
            scene black
            with fade
            jump emeeting

label day1end:
    hide dnormal
    show dflushed
    d "Oh!"
    d "Okay!!"
    d "Great!!!"
    hide dflushed
    show dnormal at move_slide_zoom
    scene black
    with fade
    "You go back home and suddenly become very tired."
    "It's time for sleep."
    jump day2am


#day1 eva cafe meeting
label emeeting:
    scene black
    "I could use a snack..."
    "You decide to walk to the cafe across the street."
    scene kitchen
    with fade
    hide dsweaty
    show enormal
    "You see Eva sitting alone at a table."
    u "Hey Eva."
    if mean:
        "She glares at you."
    e 'What are you doing here?'
    menu:
        'Sit with Eva':
            hide enormal
            jump eCafeSit
        "Don't sit with Eva":
            u "I just realized I left something at school, I need to go."
            e "Oh, okay. I don't care."
            "You quickly hurry back to school."
            scene black
            with fade
            jump dmeeting

label eCafeSit:
    show enormal
    u "Do you mind if I sit with you?"
    if mean:
        e 'I\'d rather you not...'
    else:
        e "I guess nothing's stopping you."
    u '...'
    e '...'
    u '...'
    hide enormal
    show eflushed
    "Eva stands up to leave."
    u "Wait Eva, come back!"
    "Eva sits back down."
    u "Have you started studying for the math test yet?"
    hide eflushed
    show enormal
    "Eva glares at you."
    e "I'm not going to study for it."
    u "Why not?"
    e "I don't want to."
    "You slam your hands on the table."
    hide enormal
    show esweaty
    u "You have to! The teacher said you would fail if you don't pass this test."
    u "I'm going to the library to study in a couple days. You should come."
    hide esweaty
    show eflushed
    e "We'll see..."
    scene black
    with fade
    "You feel tired so you go home."
    "You decide to go to sleep early."
    jump day2am

#day 2
label day2am:
    scene protagonist_bedroom
    with fade
    u "It's too early for my brain to think."
    u "..."
    u "Two days until the test."
    u "I should get to school."
    scene outside
    with fade
    u "I'm late! Gotta run!"
    scene classroom
    with fade
    show dnormal at slightleft
    d "Good morning!"
    show enormal at slightright
    e "Hey."
    u "Good morning guys!"
    t "Okay class, take your seats."
    t "Today is a review day."
    t "Remember that cosine cardioids have polar axis symmetry, and
    sine cardioids have theta = pi/2 symmetry."
    t "Now take out your notes and do problem 6."
    t "Please work on this quietly."
    "Both Dawn and Eva look really confused."
    "Who should I help?"
    menu:
        "Help Dawn":
            jump helpdawn
        "Help Eva":
            jump helpeva
label helpdawn:
    hide enormal
    hide dnormal
    "Dawn looks lost, I think I should help her."
    u "Dawn, you look a little confused. Need any help?"
    show dflushed
    d "Yeah....I'm sorry, I don't remember this lesson!"
    u "It's no problem. Look here, if you plot these points, the graph is symmetrical
    about the polar axis."
    d "Oh yeah, that makes so much sense. I get it now, thank you!"
    $ daffect +=2
    jump endclass2
label helpeva:
    hide dnormal
    hide enormal
    "Eva looks lost, I think I should help her."
    u "Eva, you look a little confused. Need any help?"
    show eflushed
    e "I never pay attention in class....of course I don't know what I'm doing."
    u "It's no problem. Look here, if you plot these points, the graph is symmetrical
    about the polar axis."
    e "Oh."
    e 'That makes some sense...'
    $ eaffect +=2
    jump endclass2
label endclass2:
    hide eflushed
    hide dflushed
    show dnormal at slightleft
    show enormal at slightright
    "The teacher walks up to your table."
    hide enormal
    show eflushed at slightright
    t "Hey, I need all of you guys to stay after class. Eva needs to pass this test
    to pass the class."
    hide eflushed
    show esweaty at slightright
    t "So, I'm making all of you stay after school to help her."
    jump detention

label detention:
    hide dnormal
    hide esweaty
    scene classroom2
    with fade
    show enormal at slightright
    show dflushed at slightleft
    pause .5
    hide dflushed
    show dsweaty at slightleft
    pause .5
    hide dsweaty
    show dflushed at slightleft
    pause .5
    hide dflushed
    show dsweaty at slightleft
    $ sweaty += 1
    hide dsweaty
    show dsweaty at slightleft
    #add dawn zooming around
    d "We're in trouble we're in trouble
    we'reintroublewe'reintrouble!!"
    "Eva looks visibly annoyed."
    d "I've never had detention before oh gosh what are we going to do I-"
    hide enormal
    show esweaty at slightright
    e "SHUT UP."
    "Everyone goes silent."
    d "..."
    e "I'M TIRED OF YOU COMPLAINING ABOUT EVERYTHING."
    d "Umm...what?"
    d "We wouldn't even be here if you could just do your homework and try a little."
    pause .5
    $ sweaty += 1
    pause .5
    e "I-I...."
    "This is getting out of hand. I should do something."
    menu:
        "Defend Dawn":
            hide dsweaty
            hide esweaty
            jump ddefend
        "Defend Eva":
            hide dsweaty
            hide esweaty
            jump edefend
label ddefend:
    show esweaty at slightright
    show dsweaty at slightleft
    u "Eva, stop. She's clearly freaking out right now. Just give her some space."
    hide dsweaty
    show dflushed at slightleft
    "Eva scoffs and storms off."
    pause .5
    hide esweaty
    show esweaty at move_slide_right_from_right
    pause 1.1
    hide esweaty
    pause .5
    d "T-thanks for standing up for me back there."
    u "It's nothing, Eva was being insensitive."
    "Dawn smiles at you."
    hide dflushed
    show dnormal
    d "Still, I really appreciate it."
    d "I should get going, I have a lot of homework to do."
    d "See you tomorrow!"
    hide dnormal
    show dnormal at move_slide_left
    "I should start heading home too."
    jump endday2

label edefend:
    show esweaty at slightright
    show dsweaty at slightleft
    u "Dawn, stop. Can't you see that Eva is trying her best? You aren't helping to motivate anyone."
    pause .5
    "Dawn looks embarrassed and hurries off."
    hide dsweaty
    pause 1.2
    hide dsweaty
    pause .5
    hide esweaty
    show esweaty
    pause .5
    e "You didn't have to do that"
    u "She was blaming you for things that aren't your fault."
    hide esweaty
    show eflushed
    e "...I appreciate it."
    e "I have to go now. Bye."
    hide eflushed
    show esweaty at move_slide_left
    "I should head home too."
    jump endday2

label endday2:
    scene outside
    with fade
    "You walk home quickly, desperately needing sleep."
    scene protagonist_bedroom
    with fade
    "You can't reach your bed fast enough."
    "You remember that your math test is soon."
    scene black
    with fade
    "You drift off to sleep..."
    pause 2
    jump day3start


label day3start:
    scene protagonist_bedroom
    with fade
    "You wake up slowly; you're still tired from the chaos of the last couple days."
    u "Ahh, I just remembered my math test is tomorrow."
    u "I should study after school today."
    "You look at the clock."
    u "It's already 7:45??? I'm almost late!"
    scene outside
    with fade
    u "Go go go go go."
    scene black
    with fade
    "School proceeded as usual for the rest of the day."
    "After school, you see Dawn and Eva in the halls."
    scene corridor
    with fade
    show dnormal at slightleft
    show enormal at slightright
    "I should ask one of them to join me for studying, but who should I ask?"
    menu:
        "Dawn":
            "I think I should ask Dawn if she wants to study with me."
            hide dnormal
            hide enormal
            jump dfinal
        "Eva":
            "I think I should ask Eva if she wants to study with me."
            hide dnormal
            hide enormal
            jump efinal

label efinal:
    show enormal
    u "Hey Eva, want to study with me after school at the library?"
    e 'Y-you want to go study...'
    hide enormal
    show eflushed
    e 'W-with me...?'
    e 'S-sure I guess...'
    'She seems surprised, but almost... grateful?'
    hide eflushed
    show enormal
    e 'Wait.'
    u 'Yeah?'
    e 'Isn\'t the library closed on Thursdays?'
    u 'It is?'
    hide enormal
    show eflushed
    e 'Yeah it is. I... like to go there sometimes.'
    pause 1.5
    e 'It\'s peaceful.'
    u 'That\'s interesting. You didn\'t seem like the type to hang out at the library to me.'
    hide eflushed
    show esweaty
    e 'Y-yeah whatever.'
    pause 1
    hide esweaty
    show eflushed
    e 'W-well since that didn\'t work out... maybe...'
    hide eflushed
    show esweaty
    pause 1
    'Eva trails off.'
    e 'Maybe we could... could study at...'
    hide esweaty
    show eflushed
    pause 1
    e 'A-at my house...'
    u "Sounds good to me."
    hide eflushed
    show esweaty
    e 'Y-yeah okay whatever bye.'
    hide esweaty
    show esweaty at move_slide_zoom
    pause .25
    hide esweaty
    scene black
    with fade
    "You meet up with Eva after school."
    scene outside
    with fade
    show enormal
    u "Hey Eva! Ready to study?"
    hide enormal
    show esweaty
    pause 1
    hide esweaty
    show eflushed
    e 'I guess.'
    e 'You can come in.'
    hide eflushed

    scene sayori_bedroom with fade
    show enormal
    pause 1
    hide enormal
    show eflushed
    e 'I hope you didn\'t expect me to clean or anything.'
    'The room looks nearly spotless, aside from the pile of clothes shoved under her bed.'
    e 'Anyway...'
    u "We should probably start studying now, huh."
    hide eflushed
    show enormal
    e 'Yeah. Probably. I\'ll go get some snacks.'
    'She leaves...'
    hide enormal
    pause 1
    show enormal
    '...and comes back with a big bag of chips.'
    scene black with fade
    "You both start working on the remaning problems in your handouts."
    "Suddenly, you reach for the chip bag..."
    "But it turns out Eva was reaching for it too! Your hands brush lightly."
    scene sayori_bedroom with fade
    hide enormal
    show esweaty
    e 'Oh! S-sorry.'
    hide esweaty
    show eflushed
    u "It's okay, really."
    "Is it warm in here?"
    "..."
    "The air feels thick around you."
    "..."
    hide eflushed
    scene black
    with fade
    "The rest of the night, you and Eva do your best to focus on the math.
    However, there is an unmistakable sense of awkwardness between you."
    "For now, you decide to focus on the math test."
    pause 2

    jump test

label dfinal:
    show dnormal
    u "Hey Dawn, want to study with me after school at the library?"
    pause .5
    hide dnormal
    show dflushed
    pause .5
    d "M-me? Uhh, yeah sure...sounds great."
    d "At the library you said?"
    u "Yeah."
    d "The library is closed on Thursdays but we could..."
    "Dawn trails off awkwardly."
    hide dflushed
    show dsweaty
    pause 1
    d "...study at my house."
    #we find ourselves in the thought bubble
    "..."
    u "Sounds good to me."
    d "Alright, cool. I'll see you after school."
    hide dsweaty
    show dsweaty at move_slide_zoom
    pause .25
    hide dsweaty
    scene black
    with fade
    "You meet up with Dawn after school."
    scene outside
    with fade
    show dsweaty
    u "Hey Dawn! Ready to study?"
    d "Ready when you are hahahahhahaha...hah..ha..aaah..."
    d "Come inside!"
    hide dsweaty
    show sayori_bedroom
    with fade
    show dflushed
    u "We should probably start studying now, huh."
    d "Haha yeah we should."
    u "Uh oh! I think I forgot a calculator."
    d "Don't worry about it! I have mine with me...Ilovemycalculatoralotokay?!?"
    "You both work on the remaning problems in your handouts."
    "You reach for Dawn's calculator..."
    "But it turns out Dawn was reaching for it too!"
    "Your hands brush lightly."
    hide dflushed
    show dsweaty
    d "OH MY GOSH I'M SORRY I DIDN'T MEAN TO..."
    hide dsweaty
    show dflushed
    pause .5
    hide dflushed
    show dsweaty
    pause .5
    hide dsweaty
    show dflushed
    pause .5
    hide dflushed
    show dsweaty
    $ sweaty += 1
    hide dsweaty
    show dsweaty
    u "It's okay, really."
    "Is it warm in here?"
    "..."
    "You feel the air grow heavy between you."
    "..."
    scene black
    with fade
    "The rest of the night, you and Dawn do your best to focus on the math.
    However, there is an unmistakable sense of awkwardness between you."
    pause 2
    $chosed2 = True
    jump test

#day 3


label test:
    "It's the day of the test."
    t "Good luck class."
    scene classroom
    with fade
    u "I did really well!"
    u "I wonder how they did."
    if chosed2:
        jump dend
    else:
        jump eend

label dend:
    show dnormal
    d "How did you do?"
    u "Oh, I did alright. How about you?"
    "She shows you her paper."
    u "Wow you did so well!"
    d "Thanks."
    hide dnormal
    show dflushed
    d 'Hey...'
    d "Could I talk to you...outside?"
    hide dflushed

    scene corridor
    with fade
    show dflushed
    d 'Hey...'
    u '...'
    d 'These past few days...'
    d 'I\'ve really admired all the effort you\'ve put into helping me study.'
    hide dflushed
    show dsweaty
    pause .5
    hide dsweaty
    show dflushed
    d 'W-Would you...'
    d 'Would you go out with me?'

    menu:
        "Yes":
            jump ddate
        "No":
            jump dnodate

label ddate:
    show dflushed
    u "I'd love to."
    hide dflushed
    show dnormal
    d "R-really??"
    pause .5
    u "Of course."
    d "I-I..uh...Let's schedule a time soon!"
    hide dnormal
    "You smile happily, knowing that you and Dawn are going to be seeing more of each other in the future."
    pause .5
    jump end
label dnodate:
    u "Sorry, I like someone else."
    hide dflushed
    show dsweaty at move_slide_zoom
    $ sweaty += 1
    d "I'M SORRY I ASKED."
    hide dsweaty
    "You probably could have handled that better."
    jump end
label eend:
    show enormal
    u "How did you do?"
    e "I...passed."
    u "You sound surprised."
    hide enormal
    show eflushed
    e "Yeah, I guess I am."
    hide eflushed
    show enormal
    pause .5
    hide enormal
    show eflushed
    e "Thanks for helping me study... I really appreciate it..."
    pause .5
    e '...'
    u "..."
    e "W-would you want to... um... hang out... or whatever..."
    menu:
        "Yes":
            jump edate
        "No":
            jump enodate
label edate:
    u "I'd love to hang out."
    e 'Wh-'
    hide eflushed
    show esweaty
    pause 1
    hide esweaty
    show eflushed
    e 'I-I need to go now!'
    hide eflushed
    show eflushed at move_slide_zoom
    pause 1
    hide eflushed
    u "You look at her running away, and see her grinning from ear to ear."
    jump end
label enodate:
    u "Sorry, I'm really busy right now."
    hide eflushed
    show esweaty at move_slide_zoom
    $ sweaty += 1
    e "Predictable."
    hide esweaty
    "You probably could have handled that better."
    jump end

    # This ends the game.
label end:

    return
