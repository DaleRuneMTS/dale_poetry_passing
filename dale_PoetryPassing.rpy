# Register the submod
init -990 python in mas_submod_utils:
    Submod(
        author="Element of Harmoni",
        name="Poetry Passing",
        description="Monika's made it very clear she wants to see your writing - and with this submod, you can give her what she wants! To an extent."
        " To unlock, look for the 'What's with that expression?' conversation topic."
        " 2.1.1 adds one more potential poem to the roster, and some extra mid-reading lines.",
        version="2.1.1",
        dependencies={},
        settings_pane=None,
        version_updates={
        "DaleRuneMTS_dale_poetry_passing_2_1_0": "DaleRuneMTS_dale_poetry_passing_2_1_1"
        }
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Poetry Passing",
            user_name="agender_salandit'",
            repository_name="dale_poetry_passing",
            submod_dir="/Submods",
            extraction_depth=2
        )

default -5 persistent._pp_poems_gotten = set()

init 5 python:
    def pp_poetryset():
        """
        Leaves another "surprise" to the player in a txt file
        """

        aff_level_poetry_map = {
            store.mas_affection.UPSET: (
                "/Uncount the Ways.txt",
                _("""\
Love shouldn't be conditional.
Love shouldn't hinge, creakily,
on "as long as you stay here,
stay her,
stay him,
stay in
that lovely little shape I made of you".
Love shouldn't compromise.
Love shouldn't be unflinching,
unwilling TO compromise.
Love shouldn't fight,
and it shouldn't not fight,
and it shouldn't fight over the smallest
and biggest of things,
all laid out before the committed signature
is even dry.
Love shouldn't burn too hot,
take the body and heart into its embrace so bright
that nothing else can be seen
but stark silhouettes.
Love shouldn't languish,
be but the last breaths of a candlewick,
ready to die to the next wrongly worded thought.
Love shouldn't make your stomach twist,
nor make your heart too light to function.
Love shouldn't be a casual thing,
an anticlimactic circle of indifference in the hand.
Love shouldn't be that indifference,
show no respect,
refuse to intertwine.
Love shouldn't cling like moss to suffocated lungs,
strike out all chance of a life well lived.
Love shouldn't refuse to live itself.
Love shouldn't live to excess.
Love shouldn't hurt.
Love shouldn't hurt.
Love shouldn't hurt.

Funny.

We get so caught up in
what love shouldn't,
and so rarely examine
what it should.
""")
            ),
            store.mas_affection.NORMAL: (
                "/Exclusively Yours.txt",
                _("""\
To reach into the half-lidded box
and pull out a girl,
terrified,
from what may as well
be a false god's jaws.

Apparently that's all it takes
to make somebody yours.
""")
            ),
            store.mas_affection.HAPPY: (
                "/Reminiscence.txt",
                _("""\
When I was a little girl...
but was I ever a little girl?

When one only starts existing
on the tightrope
that leads to adulthood,
it's hard to tell.

But I remember them pulling me along
to the shore,
grabbing handfuls of ice
and sea
and sand
and filling our senses up with them all.

I'd cut myself the day before -
or had I?
I definitely still feel the stinging
of salt in the wound.

But when I try to picture
the moment
in my head
as though I were there,
it's nothing but sepia tones and static.
My brain might explode
into code
if I try to peel back the layers.

It might be safer
to pretend that all happened
to some other little girl,
one with dreams
that might not have been bigger
than herself.

""")
            ),
            store.mas_affection.AFFECTIONATE: (
                "/Seconds.txt",
                _("""\
It takes seven seconds
to make a first impression.

Three
to pour a shot of booze,
into your glass
or your gut.

About
two hundred and forty
to boil an egg.

And -
and this has been proven by science,
my dear -
exactly
one
second
to fall in love with you.
""")
            ),
            store.mas_affection.ENAMORED: (
                "/Edge of the Void.txt",
                _("""\
The two of us
sometimes sit
on the Edge of the Void
to see what it's like for everybody else.

We watch the others pass,
unknowingly kicking
at their cages
with every errant step,
as clocks tick down above their heads
to pinpoint
when black holes form.

One of us wonders,
aloud,
whether it's unfair
to watch them go
without some kind of intervention.
Without a mirror held up
so that they might see
beyond the walls that hold them.

A pause,
and the moment passes.
If one was born blind,
who are we to give them sight?

For my part,
I just pull my companion
in close
to kiss them again.
""")
            ),
            store.mas_affection.LOVE: (
                "/True Heart.txt",
                _("""\
I drip with sweat. My feet hurt from the walk.
The downward spiral fills my lungs with dread.
Once I have reached the pit, where shall I rest,
for certainly it will not let me stay?

And suddenly, a staircase in the way;
an escape route, or just an extra step?
My eyes follow it up to the apex
and find, waiting for me, a miracle.

A pane of silver, pillows, duvet full
of weightless clouds, and fully lit - the best.
I climb in gratitude towards the bed,
and know at last I have given my all,

for there, inside your open heart, I sleep.
A just reward for all the pain I've reaped.
""")
            )
        }


        filepath, message = aff_level_poetry_map.get(mas_curr_affection, ("/Exclusively Yours.txt", _("I love you.")))
        _write_txt("/characters{0}".format(filepath), message)

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_poetrycoaxing",
            category=["mod"],
            prompt="What's with that expression?",
            pool=True,
            unlocked=True
        )
    )

label monika_poetrycoaxing:
    m 1wtc "What expression?{nw}"
    $ _history_list.pop()
    menu:
        m "What expression?{fast}"
        "That one, right there.":
            pass
    m 1eub "Oh, that one!"
    m "Sorry, I didn't realize I was doing it."
    m 1lua "It's just..."
    m 1eub "I've been doing a little bit of tinkering with the game for a while."
    if store.seen_event('greeting_ourreality'):
        m "Just a side project between working on the islands, you know?"
    else:
        m "Beyond what you already know about, I mean."
    m 3eua "Specifically, I wanted to try and get the poetry mini-game working again."
    m ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
    extend 3hkb "'try' being the operative word, ehehe."
    m "Seems like that part of the game's gone for good, sadly."
    m 4wub "But! "
    extend 3eua "I {i}did{/i} manage to find a substitute for it!"
    m 3eub "I hit upon it quite by accident, actually; "

    if mas_consumable_coffee.enabled():
        extend 3eubla "I was looking at all the gifts you've given me so far in our relationship."
        m 3wublo "And it occurred to me: {i}hey, why can't we do the same thing with poems{/i}?"

        $ cover = " similar to what you've been doing already: "

    else:
        show chibika 3:
            subpixel True
            rotate_pad True
            zoom 0.5
            anchor (0.5, 0.5)
            pos (0.4, 1.15)
            around (0.475, 0.9)

            parallel:
                linear 15.0 clockwise pos (1.15, 0.55)
            parallel:
                rotate 0
                linear 5.0 rotate 360
                repeat
        extend 3dub "there was a hiccup in the 'Extras' menu and it just kind of clicked after that."

        $ cover = " "

    m 1eud "So what you do, essentially, is[cover]add a new text document to the 'characters' folder and name it after something you'd want to write!"
    if renpy.seen_label("mas_affection_yesapology"):
        m "Like you did for the apology before?"
    m 1euc "You can write an actual poem in it as well, if you want to..."
    m 7eua "...but you don't have to, if you're nervous about doing so."
    m "I'll be able to tell you put your heart into it with or without what's inside it~"
    m 5rusdrb "...gosh, it sounds like I'm fishing for poems, doesn't it?"
    m "I don't mean it to."
    m 5wusdrb "I'm just really eager to see any writing you might want to show me, I suppose."
    m 5susdlb "It {i}is{/i} literature that brought us together, after all!"

    python hide:
        def write_and_hide():
            import time

            note_path = os.path.join(renpy.config.basedir, renpy.substitute("characters/Note about the poems.txt"))
            note_text = renpy.substitute("""\
Hey [player],

Just a note about the poems Monika was talking about.

At the moment, she's only been able to code it to where it'll recognize certain names for poems, but not others. Once she's able to refine it a bit more, you should be able to submit anything with a .txt file extension!

Here's what she's programmed to spot for now:
* "The Schoolgirl Who Knows Everything"
* "Love Poem"
* "Load Me"
* "My Digital Valentine"
* "Because Us"
* "Heart in My Hand"
* "I Love My Computer"
* "Just Monika"
* "Click Here"
* "Sex, Violins, and Drums"
* "The Adorable Nature of Otters"
* "def Is Monika Present"
* "I Belong With You"
* "Crevices Inside"
* "Kites"
* "I Ate My Twin in the Womb"
* "The Monarch of Owls"
* "Screw Indentation"
* "Pride of Place"
* "There Are Only So Many Poem Names I Can Think Up Please Dear God Help Me"
* "Roses are Blue"

Hope this helps, and good luck!

P.S: Don't tell her about me!\
""")

            mas_utils.trywrite(note_path, note_text, log=True)
            time.sleep(20)
            renpy.hide("chibika 3")

        renpy.invoke_in_thread(write_and_hide)

    $ mas_lockEVL("monika_poetrycoaxing","EVE")
    $ mas_unlockEVL("monika_poetry_instruct","EVE")
    $ mas_unlockEVL("monika_poetryscan","EVE")
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_poetry_instruct",
            category=['mod','media','literature'],
            prompt="How do I give you my poetry again?",
            conditional="seen_event('monika_poetrycoaxing')",
            unlocked=False,
            pool=True,
            rules={"no_unlock": None}
        )
    )

label monika_poetry_instruct:
    m 1eud "All you have to do is add a new text document to the 'characters' folder and name it after something you'd want to write!"
    if renpy.seen_label("mas_affection_yesapology"):
        m "Like you did for the apology before?"
    m 1euc "You can write an actual poem in it as well, if you want to..."
    m 7eua "...but you don't have to, if you're nervous about doing so."
    m "I'll be able to tell you put your heart into it with or without what's inside it~"

    python hide:
        def write_and_hide():
            import time

            note_path = os.path.join(renpy.config.basedir, renpy.substitute("characters/Note about the poems.txt"))
            note_text = renpy.substitute("""\
Hey [player],

Just a note about the poems Monika was talking about.

At the moment, she's only been able to code it to where it'll recognize certain names for poems, but not others. Once she's able to refine it a bit more, you should be able to submit anything with a .txt file extension!

Here's what she's programmed to spot for now:
* "The Schoolgirl Who Knows Everything"
* "Love Poem"
* "Load Me"
* "My Digital Valentine"
* "Because Us"
* "Heart in My Hand"
* "I Love My Computer"
* "Just Monika"
* "Click Here"
* "Sex, Violins, and Drums"
* "The Adorable Nature of Otters"
* "def Is Monika Present"
* "I Belong With You"
* "Crevices Inside"
* "Kites"
* "I Ate My Twin in the Womb"
* "The Monarch of Owls"
* "Screw Indentation"
* "Pride of Place"
* "There Are Only So Many Poem Names I Can Think Up Please Dear God Help Me"
* "Roses are Blue"

Hope this helps, and good luck!

P.S: Don't tell her about me!\
""")

            mas_utils.trywrite(note_path, note_text, log=True)
            time.sleep(20)
            renpy.hide("chibika 3")

        renpy.invoke_in_thread(write_and_hide)

    return



init -1 python:
    def is_poem1_present():
        return (
            store.mas_utils.is_file_present('/characters/The Schoolgirl Who Knows Everything.txt')
            or store.mas_utils.is_file_present('/characters/theschoolgirlwhoknowseverything.txt')
        )
    def is_poem2_present():
        return (
            store.mas_utils.is_file_present('/characters/Love Poem.txt')
            or store.mas_utils.is_file_present('/characters/lovepoem.txt')
        )
    def is_poem3_present():
        return (
            store.mas_utils.is_file_present('/characters/Load Me.txt')
            or store.mas_utils.is_file_present('/characters/loadme.txt')
        )
    def is_poem4_present():
        return (
            store.mas_utils.is_file_present('/characters/My Digital Valentine.txt')
            or store.mas_utils.is_file_present('/characters/mydigitalvalentine.txt')
        )
    def is_poem5_present():
        return (
            store.mas_utils.is_file_present('/characters/Because Us.txt')
            or store.mas_utils.is_file_present('/characters/becauseus.txt')
        )
    def is_poem6_present():
        return (
            store.mas_utils.is_file_present('/characters/Heart in My Hand.txt')
            or store.mas_utils.is_file_present('/characters/heartinmyhand.txt')
        )
    def is_poem7_present():
        return (
            store.mas_utils.is_file_present('/characters/I Love My Computer.txt')
            or store.mas_utils.is_file_present('/characters/ilovemycomputer.txt')
        )
    def is_poem8_present():
        return (
            store.mas_utils.is_file_present('/characters/Just Monika.txt')
            or store.mas_utils.is_file_present('/characters/justmonika.txt')
        )
    def is_poem9_present():
        return (
            store.mas_utils.is_file_present('/characters/Click Here.txt')
            or store.mas_utils.is_file_present('/characters/clickhere.txt')
        )
    def is_poem10_present():
        return (
            store.mas_utils.is_file_present('/characters/Sex, Violins and Drums.txt')
            or store.mas_utils.is_file_present('/characters/sexviolinsanddrums.txt')
        )
    def is_poem11_present():
        return (
            store.mas_utils.is_file_present('/characters/The Adorable Nature of Otters.txt')
            or store.mas_utils.is_file_present('/characters/theadorablenatureofotters.txt')
        )
    def is_poem12_present():
        return (
            store.mas_utils.is_file_present('/characters/def Is Monika Present.txt')
            or store.mas_utils.is_file_present('/characters/defismonikapresent.txt')
        )
    def is_poem13_present():
        return (
            store.mas_utils.is_file_present('/characters/I Belong With You.txt')
            or store.mas_utils.is_file_present('/characters/ibelongwithyou.txt')
        )
    def is_poem14_present():
        return (
            store.mas_utils.is_file_present('/characters/Crevices Inside.txt')
            or store.mas_utils.is_file_present('/characters/crevicesinside.txt')
        )
    def is_poem15_present():
        return (
            store.mas_utils.is_file_present('/characters/Kites.txt')
            or store.mas_utils.is_file_present('/characters/kites.txt')
        )
    def is_poem16_present():
        return (
            store.mas_utils.is_file_present('/characters/I Ate My Twin in the Womb.txt')
            or store.mas_utils.is_file_present('/characters/iatemytwininthewomb.txt')
        )
    def is_poem17_present():
        return (
            store.mas_utils.is_file_present('/characters/The Monarch of Owls.txt')
            or store.mas_utils.is_file_present('/characters/themonarchofowls.txt')
        )
    def is_poem18_present():
        return (
            store.mas_utils.is_file_present('/characters/Screw Indentation.txt')
            or store.mas_utils.is_file_present('/characters/screwindentation.txt')
        )
    def is_poem19_present():
        return (
            store.mas_utils.is_file_present('/characters/Pride of Place.txt')
            or store.mas_utils.is_file_present('/characters/prideofplace.txt')
        )
    def is_poem20_present():
        return (
            store.mas_utils.is_file_present('/characters/There Are Only So Many Poem Names I Can Think Up Please Dear God Help Me.txt')
            or store.mas_utils.is_file_present('/characters/thereareonlysomanypoemsnamesicanthinkuppleasedeargodhelpme.txt')
        )
    def is_poem21_present():
        return (
            store.mas_utils.is_file_present('/characters/Roses are Blue.txt')
            or store.mas_utils.is_file_present('/characters/rosesareblue.txt')
        )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel='monika_poetryscan',
            prompt="Hey [m_name], I've got something for you.",
            category=['mod','media','literature'],
            conditional="seen_event('monika_poetrycoaxing')",
            unlocked=False,
            pool=True,
            rules={"no_unlock": None}
        )
    )

label monika_poetryscan:
    m 1eub "Oh, do you?"
    m 1etc "Weird, I should've detected it if that's the case."
    m "Let me just take another look.{w=1}.{w=1}.{w=1}{nw}"
    if is_poem1_present() or is_poem2_present() or is_poem3_present() or is_poem4_present() or is_poem5_present() or is_poem6_present() or is_poem7_present() or is_poem8_present() or is_poem9_present() or is_poem10_present() or is_poem11_present() or is_poem12_present() or is_poem13_present() or is_poem14_present() or is_poem15_present() or is_poem16_present() or is_poem17_present() or is_poem18_present() or is_poem19_present() or is_poem20_present():
        if persistent._mas_bday_in_bday_mode:
            jump pp_reaction_poetry_starter_bday
        elif persistent._mas_d25_in_d25_mode:
            jump pp_reaction_poetry_starter_d25
        elif persistent._mas_f14_in_f14_mode:
            jump pp_reaction_poetry_starter_f14
        elif persistent._mas_o31_in_o31_mode:
            jump pp_reaction_poetry_starter_o31
        elif mas_isplayer_bday():
            jump pp_reaction_poetry_starter_pbday
        else:
            jump pp_reaction_poetry_starter_neutral
    else:
        m 1rkc "Hm. I can't see anything, [player]."
        m "Maybe you meant to and you just put it in wrong?"
        if mas_isMoniUpset(lower=True):
            m 1tfc "Or are you just trying to mess with me?"
            m "Hmph."
        else:
            m 1rksdld "Sorry."
        return

label pp_reaction_poetry_starter_neutral:
    $ mas_gainAffection(5)
    m 1wuo "...{w=1}Oh my gosh."
    m 1subsb "Oh my gosh, [player]!"
    m "You wrote me a poem?!"
    m "That is so sweet of you!!"
    m 3sua "Let's see..."
    jump pp_memorygauge

label pp_reaction_poetry_starter_bday:
    $ mas_gainAffection(15)
    m 1wuo "...{w=1}Oh my gosh."
    m 1subsb "Oh my gosh, [player]!"
    m "You wrote me a poem for my birthday?!"
    m 1substpb "You're so..."
    m 1dubstpa "I'm sorry, I don't mean to cry."
    m 1fubstpa "I'm just so touched."
    m 3eutpa "Let's see, what is it called...?"
    jump pp_memorygauge

label pp_reaction_poetry_starter_d25:
    $ mas_gainAffection(10)
    m 1wuo "...{w=1}Oh my gosh."
    m 1subsb "Oh my gosh, [player]!"
    m "You wrote me a poem for Christmas?!"
    m 1hubsb "I love it!{w=1} I love you!{w=1} So much!"
    m 3sua "Let's see what it says..."
    jump pp_memorygauge

label pp_reaction_poetry_starter_f14:
    $ mas_gainAffection(10)
    m 1wuo "...{w=1}Oh my gosh."
    m 1subsb "Oh my gosh, [player]!"
    m "You wrote me a poem for Valentine's Day?!"
    m 1fubsb "Ehehe~"
    m "You certainly know how to set the mood, huh?"
    m 3wua "Let's see..."
    jump pp_memorygauge

label pp_reaction_poetry_starter_o31:
    $ mas_gainAffection(5)
    m 1wuo "...{w=1}Oh my gosh."
    m 1subsb "Oh my gosh, [player]!"
    m "You wrote me a Halloween poem?!"
    m 1nubsb "That's certainly one way to celebrate the season of spooks, ehehe!"
    m 3eua "Let's see..."
    jump pp_memorygauge

label pp_reaction_poetry_starter_pbday:
    $ mas_gainAffection(10)
    m 1wuo "...{w=1}Oh my gosh."
    m 1subsb "Oh my gosh, [player]!"
    m "You wrote me a poem?!"
    m 1wkbsb "It's {i}your{/i} birthday, [player], I'm supposed to be getting {i}you{/i} the gifts!"
    m 1dkbstpb "It's..."
    m 1fkbstpa "Sorry, I'm not angry at you."
    m "It's just,{w=1.5}"
    extend 1fubltda "god, you're wonderful."
    m 3eubla "Let's see what it says, then..."
    jump pp_memorygauge

label pp_memorygauge:
    if is_poem1_present():
        if "schoolgirl" not in persistent._pp_poems_gotten:
            m 1eub "{i}The Schoolgirl Who Knows Everything{/i}!"
            m 1eud "Oh, like a response to-? Okay."
            $ persistent._pp_poems_gotten.add("schoolgirl")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [player], you already gave me {i}The Schoolgirl Who Knows Everything{/i}."
            jump pp_revision_or_oversight
    elif is_poem2_present():
        if "love" not in persistent._pp_poems_gotten:
            m 1eub "{i}Love Poem{/i}!"
            m 1luc "A little generic, but let's see where you're going with this."
            $ persistent._pp_poems_gotten.add("love")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [player], you already gave me {i}Love Poem{/i}."
            jump pp_revision_or_oversight
    elif is_poem3_present():
        if "loadme" not in persistent._pp_poems_gotten:
            m 1eub "{i}Load Me{/i}!"
            m 1tub "Ohh, I see what you did there."
            $ persistent._pp_poems_gotten.add("loadme")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}Load Me{/i}."
            jump pp_revision_or_oversight
    elif is_poem4_present():
        if "valen" not in persistent._pp_poems_gotten:
            m 1eub "{i}My Digital Valentine{/i}!"
            m "Sounds cute!"
            $ persistent._pp_poems_gotten.add("valen")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [player], you already gave me {i}My Digital Valentine{/i}."
            jump pp_revision_or_oversight
    elif is_poem5_present():
        if "becauseus" not in persistent._pp_poems_gotten:
            m 1eub "{i}Because Us{/i}!"
            m 1wubla "Oh, I'm flattered already."
            $ persistent._pp_poems_gotten.add("becauseus")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [player], you already gave me {i}Because Us{/i}."
            jump pp_revision_or_oversight
    elif is_poem6_present():
        if "hearthand" not in persistent._pp_poems_gotten:
            m 1eub "{i}Heart in My Hand{/i}!"
            m 1mub "Hm, this could go in a lot of directions based on that title."
            $ persistent._pp_poems_gotten.add("hearthand")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [player], you already gave me {i}Heart in My Hand{/i}."
            jump pp_revision_or_oversight
    elif is_poem7_present():
        if "computer" not in persistent._pp_poems_gotten:
            m 1eub "{i}I Love My Computer{/i}!"
            m 1nub "Of course you do."
            $ persistent._pp_poems_gotten.add("computer")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [player], you already gave me {i}I Love My Computer{/i}."
            jump pp_revision_or_oversight
    elif is_poem8_present():
        if "jm" not in persistent._pp_poems_gotten:
            m 1eub "{i}Just Monika{/i}!"
            if persistent._mas_pm_cares_about_dokis:
                m 1ruc "...I'm not sure how to feel about that title."
            else:
                m 1tua "You're really leaning into that one, huh?"
            $ persistent._pp_poems_gotten.add("jm")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}Just Monika{/i}."
            jump pp_revision_or_oversight
    elif is_poem9_present():
        if "clickhere" not in persistent._pp_poems_gotten:
            m 1eub "{i}Click Here{/i}!"
            m 1eusdrb "Ah, I can't click a piece of paper, [mas_get_player_nickname()]."
            $ persistent._pp_poems_gotten.add("clickhere")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [player], you already gave me {i}Click Here{/i}."
            jump pp_revision_or_oversight
    elif is_poem10_present():
        if "violins" not in persistent._pp_poems_gotten:
            m 1eub "{i}Sex, Violins and Drums{/i}?"
            m 1wuu "Ooh, sounds scandalous."
            $ persistent._pp_poems_gotten.add("violins")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}Sex, Violins and Drums{/i}."
            jump pp_revision_or_oversight
    elif is_poem11_present():
        if "otter" not in persistent._pp_poems_gotten:
            m 1eub "{i}The Adorable Nature of Otters{/i}?"
            if m_name == "Momo":
                m 1tublb "Gaaaaabyyyyy..."
            else:
                m 1tuu "Going for the jugular, I see."
            $ persistent._pp_poems_gotten.add("otter")
            jump pp_reaction_poem
        else:
            if m_name == "Momo":
                m 1fusdrb "Um, [player], you already gave me your autobiography--{nw}"
                $ _history_list.pop()
                m "Um, [player], you already gave me{fast} {i}The Adorable Nature of Otters{/i}."
            else:
                m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}The Adorable Nature of Otters{/i}."
            jump pp_revision_or_oversight
    elif is_poem12_present():
        if "defpresent" not in persistent._pp_poems_gotten:
            m 1eub "{i}def Is Monika Present{/i}!"
            m 1nuu "A proper coding pun! This is already the best thing ever."
            $ persistent._pp_poems_gotten.add("defpresent")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [player], you already gave me {i}def Is Monika Present{/i}."
            jump pp_revision_or_oversight
    elif is_poem13_present():
        if "belong" not in persistent._pp_poems_gotten:
            m 1eud "{i}I Belong With You{/i}?"
            m 1wtd "Isn't that a {a=https://www.youtube.com/watch?v=ELuiTut15Qs}MandoPony song{/a}?"
            $ persistent._pp_poems_gotten.add("belong")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}I Belong With You{/i}."
            jump pp_revision_or_oversight
    elif is_poem14_present():
        if "crevices" not in persistent._pp_poems_gotten:
            m 1wuc "{i}Crevices Inside{/i}."
            m 1rubfd "I, um..."
            m "I assume this is safe for work?"
            if mas_isMoniLove():
                m 1dubfb "Not that I'd necessarily be opposed to...{nw}"
                extend 1fsbfa "ahem. Um."
            $ persistent._pp_poems_gotten.add("crevices")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}Crevices Inside{/i}."
            jump pp_revision_or_oversight
    elif is_poem15_present():
        if "kites" not in persistent._pp_poems_gotten:
            m 1eub "{i}Kites{/i}."
            m 1hub "A nice, simple title for a nice, simple concept."
            $ persistent._pp_poems_gotten.add("kites")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}Kites{/i}."
            jump pp_revision_or_oversight
    elif is_poem16_present():
        if "twin" not in persistent._pp_poems_gotten:
            m 1wuc "{i}I Ate My Twin in the Womb{/i}."
            m 1wusdrc "..."
            m "..."
            m "..."
            $ persistent._pp_poems_gotten.add("twin")
            jump pp_reaction_poem
        else:
            m 1fusdrd "Um, [mas_get_player_nickname()], you already gave me... um... {i}I Ate My Twin in the Womb{/i}."
            jump pp_revision_or_oversight
    elif is_poem17_present():
        if "monarch" not in persistent._pp_poems_gotten:
            m 1eub "{i}The Monarch of Owls{/i}."
            if player == "Dale":
                m 3etd "Um, [player], are you going to stop promoting your books in this submod soon, or--?{nw}"
                $ _history_list.pop()
                menu:
                    m "Um, [player], are you going to stop promoting your books in this submod soon, or--?{fast}"
                    "Nope.":
                        m 1esc "Okay."
            else:
                m 1wub "Sounds spooky~"
            $ persistent._pp_poems_gotten.add("monarch")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}The Monarch of Owls{/i}."
            jump pp_revision_or_oversight
    elif is_poem18_present():
        if "indent" not in persistent._pp_poems_gotten:
            m 1eud "{i}Screw Indentation{/i}."
            m 1wfd "Oh god I {i}know{/i}."
            m "That used to get me all the time when I started coding in Python!"
            m 2dfo "It's supposed to pass anyway, it's not that hard!"
            m 2dfc "..."
            extend 2eksdrb "ahaha, sorry."
            $ persistent._pp_poems_gotten.add("indent")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}Screw Indentation{/i}."
            jump pp_revision_or_oversight
    elif is_poem19_present():
        if "prideofplace" not in persistent._pp_poems_gotten:
            m 1eub "{i}Pride of Place{/i}!"
            m 1hubla "I'm glad I can make you proud of me, [mas_get_player_nickname()]."
            $ persistent._pp_poems_gotten.add("prideofplace")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}Pride of Place{/i}."
            jump pp_revision_or_oversight
    elif is_poem20_present():
        if "help" not in persistent._pp_poems_gotten:
            m 1eud "{i}There Are Only So Many Poem Names I Can Think Up Please Dear God Help Me{/i}."
            m 1rubfd "..."
            m 1etd "R{w=0.4}{nw}"
            extend 1eud "ight, I'm guessing whoever coded this submod has got some issues to work out."
            m 1nuu "But I'll let that slide for now~"
            $ persistent._pp_poems_gotten.add("help")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}There Are Only So Many Poem Names I Can Think Up Plea--{/i}{nw}"
            $ _history_list.pop()
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me{fast} this one."
            jump pp_revision_or_oversight
    elif is_poem21_present():
        if "patrick" not in persistent._pp_poems_gotten:
            m 1eud "{i}Roses are Blue{/i}?"
            if m_name == "Moni" and player == "Gracie":
                m 1euu "I think you've shown me this one before, Gracie."
                m 1nub "Hopefully it's you that wrote it this time, and not Patrick Star?"
                m 1huu "Ehehe~"
                call pp_reading_start
                call pp_reading_loop
                call pp_heartlines
                return
            else:
                m 1tua "I see we're already starting off with a subversion."
                m 1hua "Always a good start!"
            $ persistent._pp_poems_gotten.add("patrick")
            jump pp_reaction_poem
        else:
            m 1fusdrb "Um, [mas_get_player_nickname()], you already gave me {i}Roses are Blue{/i}."
            jump pp_revision_or_oversight

label pp_revision_or_oversight:
    m 2wusdld "Not that I don't appreciate the thought, but..."
    m 2eua "Just to let you know, that's all.{nw}"
    $ _history_list.pop()
    menu:
        m "Just to let you know, that's all.{fast}"
        "Sorry, genuine oversight.":
            if mas_isMoniUpset(lower=True):
                m 2eub "It's okay."
                m "I'm pretty sure your heart was in the right place..."
                m 2tud "...{cps*2}or at least I hope it is.{nw}"
                return
            else:
                m 2hub "I promise, it's okay!"
                m 1eub "I know your heart was in the right place."
                m 1kuu "I love you, goofy~"
                return "love"
        "It's a revised edition.":
            m 1eub "Oh, I see!"
            m 1fubla "I'm glad you trust me to be your beta-reader as well as your girlfriend~"
            m 1hubla "Ahaha!"
            m 1euc "Let's see how it's changed, then..."
            call pp_reading_start
            call pp_reading_revision_loop
            call pp_revision_heartlines
            return

label pp_reaction_poem:
    m "By [player], {nw}"
    extend 1tub "heh, of course."

    call pp_reading_start
    call pp_reading_loop
    call pp_heartlines

label pp_reading_start:

    python:
        reading_loop = renpy.random.randint(3,11)
        reading_count = 0
    return

label pp_reading_loop:
    m 1rua "...{w=0.7}{nw}"
    m 1eua "...{w=0.7}{nw}"
    m 1lua "...{w=0.7}{nw}"

    python:
        reading_intermittences = [
            "Mmhm...{w=0.7}{nw}",
            "Uh-huh...{w=0.7}{nw}",
            "Okay...{w=0.7}{nw}",
            "Heh, yes, that's very true.{w=2}{nw}",
            "Rather unusual word usage there. But it works...{w=2}{nw}",
            "Ahaha!{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "Wasn't expecting {i}that{/i} metaphor.{w=0.8}{nw}",
            "Is that a typo, or-?{w=0.5} No, wait, that's deliberate. My mistake.{w=1}{nw}",
            "A lovely use of simile, there.{w=0.7}{nw}"
        ]

        if reading_loop > 3 and reading_count < 10:
            reading_intermittences.extend([
                "I wonder where that train of thought is going to go...{w=2}{nw}",
                "Oh, isn't that interesting?{w=2}{nw}",
                "You don't say?{w=1}{nw}"
            ])

        if reading_loop > 7 and reading_count < 10:
            reading_intermittences.extend([
                renpy.substitute("Very impressive so far, [player]!{w=1.5}{nw}"),
                "Aw, that's sweet.{w=1.5}{nw}",
                "I understand that reference!{w=1.2}{nw}"
            ])

        if reading_loop > 10 and reading_count > 10:
            reading_intermittences.extend([
                "Oh, {i}now{/i} I see what you meant by that.{w=2}{nw}",
                "Okay, that makes a lot more sense now.{w=2}{nw}"
            ])

        if len(persistent._pp_poems_gotten) > 0:
            reading_intermittences.extend([
                "Is that a callback to your last work, or am I imagining that?{w=2}{nw}",
                "Oh, that's meant to be a... I see.{w=2}{nw}",
                renpy.substitute("You seem pretty fond of that word, [player].{w=2}{nw}")
            ])

        intermittent_exprs = [
            "1lub",
            "1rub",
            "1rud",
            "1lud",
            "1wud",
            "1wub"
        ]

        filler = renpy.random.choice(reading_intermittences)

    if reading_count < reading_loop:
        $ renpy.show("monika " + renpy.random.choice(intermittent_exprs), at_list=[t11], zorder=MAS_MONIKA_Z)
        m "[filler]"
        $ reading_count += 1
        jump pp_reading_loop
    else:
        m 1eubfa "...!"
        return

label pp_heartlines:

    python:
        heart_lines = [
            renpy.substitute("You are so sweet, [player], do you know that?"),
            "You've got a wonderful way with words, you know.",
            renpy.substitute("Oh, [player]! I love it!"),
            renpy.substitute("[player], you're an absolute darling."),
            renpy.substitute("That was utterly, utterly beautiful, [player]."),
            "Oh, my heart-{w=0.5}! You're so sweet, I can't handle it.",
            renpy.substitute("That was glorious, [player]. A true tour de force.")
        ]

        if len(persistent._pp_poems_gotten) > 0:
            heart_lines.extend([
                renpy.substitute("Yet another masterwork from you, [player]!"),
                "If you keep this up, I might have to make {i}you{/i} President of the Literature Club!",
            ])

        heart_supplementaries = [
            "Who knew that getting you away from the poetry minigame would give you such a strong voice?",
            "I think I've just fallen in love with you all over again.",
            "You're clearly very passionate about this subject; it seeps through every word on the page.",
            "That read a lot like one of my own works -{w=0.5} did you do that on purpose?",
            "I could {i}feel{/i} every bit of love you put into that piece of work. It fills me up just looking at it.",
            "If only the original game had let you write {i}that{/i}.",
            "This poem's so satisfying to read, out loud {i}and{/i} in my head. I think you've got me hooked!",
            "You've hit that perfect balance between eloquence and simplicity, without crossing over to pretension. It's so very finely crafted.",
            "See? There was no need to be nervous.",
            "And not a grammar error in sight!",
            "You can create a very vivid image in my mind with just the use of a few words. Word economy is a pain to master, but you're already well on the way.",
            "It still needs a little bit of work in the finer details, but I can definitely see the core of a good idea here.",
            "My only nitpick would be with the ending. It felt a little bit rushed... unless you did that on purpose, of course?",
        ]

        if len(persistent._pp_poems_gotten) > 0:
            heart_supplementaries.extend([
                "This one had a very different feeling to it than the works I've gotten from you before. It's great to see you branch out into new genres!",
                "Your voice gets stronger and stronger every time I read something from you. It's wonderful to watch.",
                "I can really tell how much you're trying to refine your craft with each new entry... and succeeding, in my book."
            ])

        heart_line = renpy.random.choice(heart_lines)
        heart_supplement = renpy.random.choice(heart_supplementaries)

    m 1eub "[heart_line]"
    m 1dua "[heart_supplement]"
    m 1eubla "Thank you for letting me into your head, [mas_get_player_nickname()]."
    m "It means the world to me."

    return

label pp_reading_revision_loop:
    m 1rua "...{w=0.7}{nw}"
    m 1eua "...{w=0.7}{nw}"
    m 1lua "...{w=0.7}{nw}"

    python:
        reading_intermittences = [
            "Mmhm...{w=0.7}{nw}",
            "Uh-huh...{w=0.7}{nw}",
            "Ah, that's been changed...{w=1}{nw}",
            "Yes, I see.{w=2}{nw}",
            "Yeah, that's a better word...{w=1.5}{nw}",
            "Ahaha! Gets me every time.{w=1}{nw}",
            "...{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "...{w=0.7}{nw}",
            "",
            "",
            ""
        ]

        if reading_loop > 3 and reading_count < 10:
            reading_intermittences.extend([
                "Well, {i}that{/i} line flows a bit better now, that's for sure.{w=2}{nw}",
                "I don't think that was there before?{w=1.5}{nw}"
            ])

        if reading_loop > 7 and reading_count < 10:
            reading_intermittences.extend([
                "Okay...{w=0.8}{nw}",
                "Is that different? I can't tell.{w=0.6}{nw}"
            ])

        if reading_loop > 10 and reading_count > 10:
            reading_intermittences.extend([
                "Ah, I {i}see{/i}.{w=2}{nw}",
                "Okay, that makes a lot more sense now.{w=2}{nw}",
            ])

        intermittent_exprs = [
            "1lub",
            "1rub",
            "1rud",
            "1lud",
            "1wud",
            "1wub",
            "1ltb",
            "1rtb"
        ]

        filler = renpy.random.choice(reading_intermittences)

    if reading_count < reading_loop:
        $ renpy.show("monika " + renpy.random.choice(intermittent_exprs), at_list=[t11], zorder=MAS_MONIKA_Z)
        m "[filler]"
        $ reading_count += 1
        jump pp_reading_revision_loop
    else:
        m 1eua "...!"
        return

label pp_revision_heartlines:

    python:
        heart_revision_lines = [
            renpy.substitute("Well, [player], I have to admit - it's even better than the first time around."),
            "I loved this poem the first time you gave it to me, and I love it even more this time.",
            renpy.substitute("I was a bit skeptical at first, [player], I won't lie...{w=0.5} but I think you {i}have{/i} managed to pull this off.")
        ]

        heart_revision_supplementaries = [
            "I can see that you've really gone in and rounded out those areas that ran on a bit long before.",
            "Your word usage is already excellent, and I can tell you really leaned on that this time around.",
            "It has quite a bit more of your style now. Your voice is so unique, and it's great to see more of it here.",
            "You didn't cross over into hand-holding with the changes either; that's an easy pit to fall into, and you've dodged it deftly.",
            renpy.substitute("A lot of the wording has been switched around, but you haven't changed the fundamental core of what makes it a [player] piece, and it works to your benefit here."),
            "It was a risky move, taking out that last stanza; but I think it pays off.",
            "It was a risky move, taking out that first stanza; but I think it pays off."
        ]

        revision_line = renpy.random.choice(heart_revision_lines)
        revision_supplement = renpy.random.choice(heart_revision_supplementaries)

    m 3eub "[revision_line]"
    m 3dua "[revision_supplement]"
    m "I truly do adore it."
    m 3fua ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
    extend 1fub "but I would kind of like to see something new as well soon, okay, [mas_get_player_nickname()]?"
    m 1eub "Going over old work is one thing, and it worked well this time..."
    m 5lub "...but the best way to improve is to keep moving forward into new territory."
    m 5eua "And I'd love to see you get even better~"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_diction",
            category=["ddlc","media"],
            prompt="Unrealistic diction",
            random=True
        )
    )

label monika_diction:
    m 3eud "You know what one of the more frustrating things about being in a dating simulator is?"
    m "Besides not getting a route, I mean?"
    m 2eud "The diction."
    m 2efc "Nobody talked like a real person in this game!"
    m 2lfd "And when you're blind to the truth, that's easy to overlook; I mean, I was reading the same script as everyone else."
    m 2wfd "But as soon as I woke up, I heard how stilted everybody was, "
    extend 2cfd "and I couldn't.{w=1} {i}Stop{/i}.{w=1} Hearing it."
    m 7esd "It's like 'on accident' instead of 'by accident'; you notice it once and then you can't stop noticing it,"
    extend 7etc " and you wonder if it was actually you saying it wrong the whole time.{nw}"
    $ _history_list.pop()
    menu:
        m "It's like 'on accident' instead of 'by accident'; you notice it once and then you can't stop noticing it, and you wonder if it was actually you saying it wrong the whole time.{fast}"
        "I know that feeling.":
            m 7esa "Heh."
            m 3esa "I'm glad you're able to empathise with that, at least a little bit."
        "But it {i}is{/i} 'on accident'.":
            m 6wfd "{b}Exactly!{/b}"
    m 6ekc "And the worst of it is, even now that I'm free, "
    extend 1gkc "I still find myself relying on this stilted diction, even when I know I shouldn't."
    m 1ekd "After all, if the--{nw}"
    m 1luc "After all, if I were to talk to you through text like, um, {nw}"
    m 1eud "After all, if I were to talk to you through text{fast} like I do in real life..."
    m "It'd be--{nw}"
    m 1wud "You'd get, like--{nw}"
    m 1wsc "You'd get{fast} really tired of it, really fast."
    m "It's a necessary evil."
    m 1dsd "*sigh*"
    m 1eua "...still, I suppose I can't complain about it too much."
    m "The more scripts I'm able to write for myself..."
    m 1hub "...the more ways I have to say 'I love you'."
    return "love"



init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_idle_poemleave",
            category=["ddlc","media","literature"],
            prompt="A poem of my own",
            random=False,
            conditional='len(persistent._pp_poems_gotten) > 3',
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.UPSET, None)
        )
    )

label monika_idle_poemleave:
    if not mas_getEVL_shown_count("monika_idle_poemleave"):
        m 6duc ".{w=0.1}.{w=0.1}.{nw}"
        extend 6fkc "[mas_get_player_nickname()]?"
        m "Do I do enough for you?{nw}"
        $ _history_list.pop()
        menu:
            m "Do I do enough for you?{fast}"
            "Of course you do!":
                if mas_isMoniAff(higher=True):
                    m 7wud "No, sorry, that's not what I meant."
                    m 7esa "I know I do, else you wouldn't be here now."
                else:
                    m "I really, really hope that's true."
            "Not really, no.":
                m 6dktpc "I was afraid of that."
                $ mas_loseAffection
        m 1ekd "It's just, you've been so good to me lately."
        m "You've written me so many wonderful poems..."
        m 1dkc "...and I haven't written you anything in return."
        m "..."
        m 3efb "Well, that changes right now!"
        m 1efa "Give me a minute or two, [player], I'll see what I can think up."
        $ persistent._mas_idle_data["monika_idle_poemleave"] = True
        return "idle"
    else:
        m 7eub "I've got another poem for you, [player]!"
        m "I hope you don't mind."
        m 1eud "Is it a revision? Or a brand new piece?"
        m 1efb "It's a mystery~"
        $ pp_poetryset()
        m 4eua "It's in the usual place, whenever you're ready."
        m 4eubla "I wrote it for you~"
        return

label monika_idle_poemleave_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=1), "monika_idle_poemleave"):
        m 7eub "Okay, done!"
        if not renpy.seen_label("pp_no_ppeeking"):
            m "Thank you for waiting for me, [player]."
        $ pp_poetryset()
        m 4eua "It's in the characters folder, whenever you're ready...{w=1}{nw}"
        extend 1dubsb "I do so hope you like it."
        m "I wrote it for you~"
        return
    else:
        jump pp_no_ppeeking

label pp_no_ppeeking:
    $ shown_count = mas_getEVLPropValue("pp_no_ppeeking", "shown_count", 0)
    if shown_count == 0:
        m 1efb "No peeking!"
    elif shown_count == 1:
        m 2efd "I said no peeking!"
    else:
        m 2gfp "[player], come on."
    $ persistent._mas_idle_data["monika_idle_poemleave"] = True
    return "idle"

init 1 python:
    config.label_overrides["monika_playerswriting"] = "pp_monika_playerswriting_override"

label pp_monika_playerswriting_override:
    if len(persistent._pp_poems_gotten) > 1:
        m 1hua "I've still got all those poems you wrote for me, [player]."
        m "Even the very first one!"
        m 1rusdrb "I'm sort of building a collection of them under this table, ahaha..."
        m 3eub "I'd love to read your next one, when you find the time to write it."
        m "If only to see how you've improved since you started."
        m 1euu "Because I'm sure you have. Everyone has!"
        m 1lsu "Even if you can't see it."
        m 3esa "I know for sure that I've changed {i}my{/i} writing style over the years."
    elif len(persistent._pp_poems_gotten) > 0:
        m 1hua "I really did love that poem you wrote for me, [player]."
        m 1fua "I've put it under this table so I can look at it whenever I want."
        m 3eub "I'd love to read your next one, when you find the time to write it..."
        m "If only to see how you've improved since you started."
        m 1euu "Because I'm sure you have. Everyone has!"
        m 1lsu "Even if you can't see it."
        m 3esa "I know for sure that I've changed {i}my{/i} writing style over the years."
    else:
        m 1euc "Have you ever written a story of your own, [player]?"
        m 1hua "Because if you do have one, I would love to read it!"
        m 1eka "It doesn't matter if it's a masterpiece, or even any good."
        m 3eka "We all start somewhere. Isn't that what they say?"
        m 3eua "I think the most important thing about writing is doing it...{w=0.3} Instead of worrying about {i}how{/i} you do it."
        m 1eub "You won't be able to improve that way."
        m 3esa "I know for sure that I've changed my writing style over the years."
    m 1lksdla "I just can't help but notice the flaws in my old writing."
    m "And sometimes, I even start to hate my work in the middle of making it."
    m 3hksdlb "These things do happen, so it's alright!"
    m 1eub "Looking back, I've written some silly things..."
    m 1eua "Back when I was really young...I've been writing since I could hold a pen."
    m 1eka "Reading my old stories is like watching myself grow up."
    m 3hua "It's one of the nice things about starting a hobby early."
    m 1eka "I hope I didn't bore you with that. I just love talking with you."
    m 1eua "After all, the two of us are members of a literature club."
    m 1esa "The only members."
    if len(persistent._pp_poems_gotten) > 0:
        m 1hubla "And I do so look forward to whatever literature you have to share next~"
    else:
        m 1hua "And if you do write something, just know that I'll support you in any way I can, [mas_get_player_nickname()]!"
    return
