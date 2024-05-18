init python:
    bangok_four_bryce1_unplayed = True
    bangok_four_bryce1_protected = False
    bangok_four_bryce1_protected_a = False
    bangok_four_bryce1_protected_b = False
    bangok_four_bryce1_brycecame = False
    bangok_four_bryce1_playercame = False
    bangok_four_bryce1_playerstuffed = False
    bangok_four_bryce1_position_picka = None
    bangok_four_bryce1_position_pickb = None
    bangok_four_bryce1_wstiming = None
    bangok_four_bryce1_oralspot = None

init python in bangok_four_bryce1:
    fuckwomb = False
    knotpos = None

label bangok_four_bryce1_skipmenu:
    play sound "fx/system3.wav"
    s "你想要和布莱斯做吗？"
    menu:
        "是的。我想和布莱斯做。":
            play sound "fx/system3.wav"
            if bangok_four_common.bangnokay.check():
                s "太糟糕了。{cps=2}..{/cps}{w=1.0}{nw}"
            else:
                s "如你所愿。{cps=2}..{/cps}{w=1.0}{nw}"
                jump bangok_four_bryce1_apartment_decided
        "不。不想那么过分。":
            pass
    jump bangok_four_bryce1_skipmenu_return

label bangok_four_bryce1_ws_conversation:
    Br stern dk "嗯。"
    Br "在你开始之前，我有件事要问你。"
    c "嗯？"
    Br "之前喝了那么多酒，我有点得去解决一下。"
    if bangok_four_bryce1_playercame == True:
        Br smirk dk "就像你那样。"
    Br brow dk "这对你有关系吗？"
    menu:
        "去处理你的事。":
            $ brycemood -= 1
            Br brow dk "好吧。"
            call bangok_four_bryce1_ws_emptying_the_tank(True)
        "我可能会感兴趣。":
            Br smirk dk "在我射精之前还是之后？"
            menu:
                "淋浴我。":
                    show bryce stern dk with dissolve
                    $ renpy.pause(0.5)
                    Br "呃，不行。不能那样。"
                    c "为什么不？"
                    Br brow dk "你已经会闻起来像我和酒精。不确定实际淋浴能不能把这些味道洗掉。如果他们还能闻到尿液，你会是个好大使吗？"
                    c "..."
                    Br stern dk "今晚没有在外面做。"
                    c "好吧。"
                    menu:
                        "之前。":
                            $ bangok_four_bryce1_wstiming = "before"
                        "之后。":
                            $ bangok_four_bryce1_wstiming = "after"
                        "不再感兴趣了。":
                            $ brycemood -= 1
                            $ renpy.pause(0.8)
                            Br "如果你这么说。让我去把它弄出来，然后。"
                            call bangok_four_bryce1_ws_emptying_the_tank(True)
                            return
                "之前。":
                    $ bangok_four_bryce1_wstiming = "before"
                "之后。":
                    $ bangok_four_bryce1_wstiming = "after"
            Br flirty dk "你知道的。"
    return

label bangok_four_bryce1_ws_emptying_the_tank(feelbad=False, condom=False):
    hide bryce with dissolve
    c "(现在想想，龙是怎么用厕所的？)"
    play sound "fx/door/door_open.wav"
    menu:
        c "(我应该跟过去看看吗？)"
        "跟过去。":
            m "好奇心战胜了我，我走到布莱斯的开着的浴室门前。"
            m "他站在马桶上，一只前爪放在水箱上，努力保持平衡并将勃起的阴茎对准马桶开口开始小便。"
            play sound "fx/pour.ogg"
            m "听到我的脚步声，他看了我一眼，眨了眨眼。"
            if condom:
                play soundloop "fx/faucet2.ogg" fadein 1.0
                m "避孕套仍在他的阴茎上，在他面前充满了尿液。"
            else:
                play sound "fx/spray.ogg" fadein 0.5
                play soundloop "fx/faucet2.ogg" fadein 1.0
                m "他一时失去了对准的注意力，水流洒在马桶座、马桶水箱和地板上。"
            Br stern dk "该死。"
            Br flirty dk "喜欢看吗？"
            $ brycemood += 1
            if not condom:
                play sound "fx/spray.ogg"
            m "我的脸颊发烫。布莱斯弓起背，调整臀部，把他的阴茎重新对准马桶，排出他膀胱里的最后一滴尿液。"
            stop soundloop fadeout 2.0
            Br "我猜你们人类不是这样做的。"
            if condom:
                play sound "fx/bubbles.ogg"
                m "布莱斯摇了摇他的阴茎，塑料套在他尿液的压力下显得很滑稽。"
            else:
                m "布莱斯摇了摇他的阴茎，抖掉最后几滴尿液，然后把前爪放回湿润的地板上。"
            c "这取决于马桶，但对小便来说差不多。醉的时候瞄准会好点。"
            Br smirk dk "嗯。"
            m "我跟着他回到他的公寓的主要生活区。"
        "留在原地。":
            if feelbad:
                $ renpy.pause (2.0)
                m "我赤身裸体坐在龙的沙发上，手里拿着一瓶润滑剂。"
                $ renpy.pause (3.0)
                c "(也许我应该说些别的？我不知道为什么还在想这个...)"
                $ renpy.pause (3.0)
            else:
                $ renpy.pause (2.0)
                c "..."
                $ renpy.pause (3.0)
                if bangok_four_playerhasdick:
                    if bangok_four_bryce1_playercame == True:
                        m "我玩弄了一下我的软阴茎来打发时间。"
                    else:
                        m "我玩弄了一下我的硬阴茎来打发时间。"
                else:
                    m "我挑逗地分开湿润的阴唇来打发时间。"
                $ renpy.pause (3.0)
    play sound "fx/door/doorclose3.wav"
    show bryce normal dk with dissolve
    $ renpy.pause (0.5)
    Br flirty dk "我们到哪了？"
    return

label bangok_four_bryce1_position(pos):
    python:
        if not bangok_four_bryce1_position_picka:
            bangok_four_bryce1_position_picka = pos
        elif not bangok_four_bryce1_position_pickb:
            bangok_four_bryce1_position_pickb = pos
        else:
            renpy.error("你和布莱斯都不能一夜两次！")
    return

label bangok_four_bryce1_setprotected(p):
    python:
        bangok_four_bryce1_protected = p
        if bangok_four_bryce1_position_pickb is not None:
            bangok_four_bryce1_protected_b = p
        elif bangok_four_bryce1_position_picka is not None:
            bangok_four_bryce1_protected_a = p
        else:
            renpy.error("在你知道正在进行什么性行为之前，不应该戴上避孕套。")
    return

label bangok_four_bryce1_poke:
    m "在入睡时，布莱斯部分侧身趴下，让我比以前看得更清楚。"
    c "(嗯。那里什么也没有？)"
    m "好奇心战胜了我，我推开布莱斯的一条后腿，更近地看。"
    m "两腿之间，鳞片微微分开，露出一条水平的裂缝。当我的手触碰到它时，布莱斯开始醒来。"
    show bryce stern with dissolve
    $ renpy.pause(0.3)
    if brycemood > 6:
        Br flirty "那是我想的那个吗？"
        Br smirk "我不确定你--"
        show bryce stern with dissolve
        $ renpy.pause(0.4)
        Br "呃...我们在哪里？"
        c "还在酒吧里。"
        Br brow "你在...？"
    elif brycemood < 1:
        Br "那是什么？"
        c "呃..."
        Br brow "我感觉到了。你刚才在做什么？"
    else:
        Br brow "呃...我们在哪里？"
        c "还在酒吧里。"
        c "来吧。让我们送你回家。"
        jump bangok_four_bryce1_apartment

    menu:
        "没什么。":
            $ brycemood -= 3
            if brycemood > 3:
                Br stern "我只能相信你的话了。"
                c "让我帮你回家。"
                Br brow "..."
                Br stern "好吧。我确实需要帮忙。"
                jump bangok_four_bryce1_apartment
            else:
                Br stern "你在撒谎。"
                c "..."
                Br "我觉得我能...找到自己的路。你走吧。"
                c "..."
                scene black with dissolvemed
                stop music fadeout 1.0
                $ brycestatus = "bad"
                $ leftbryce = True
                $ brycescenesfinished = 1
                jump _mod_fixjmp
        "我只是好奇。":
            $ brycemood -= 2
            c "我还没见过龙...你懂的样子。"
            Br "..."
            c "在人类身上它是挂在外面的。我只是想看看..."
            Br "..."
            c "..."
            if brycemood > 4 and not (bangok_four_common.bangnokay.check()):
                Br "如果我给你看，你会有兴趣...{w=1.2}{nw}"
                Br flirty "如果我给你看，你会有兴趣{fast}试试吗？"
                menu:
                    "接受。":
                        $ brycemood += 2
                        show bryce smirk with dissolve
                        show zhong shy b flip at left with easeinleft
                        Wr "请别在这里。我已经有很多要打扫的了。"
                        Br normal "如果你这么说。"
                        show zhong shy b
                        $ renpy.pause (0.3)
                        hide zhong with easeoutleft
                        Br flirty "我觉得我家比较近，[player_name]。"
                        c "带路。"
                        jump bangok_four_bryce1_apartment_decided
                    "拒绝。":
                        $ brycemood -= 2
                        Br stern "在那种情况下，去生产设施找一个生物学家吧。让我..."
                        play sound "fx/chair.wav"
                        $ renpy.pause(1.5)
                        Br "..."
                        c "我会帮你走回家。"
                        $ renpy.pause(0.5)
                        Br normal "谢谢。"
                        jump bangok_four_bryce1_nevermind
        "你认为呢。":
            if brycemood < 6 or (bangok_four_common.bangnokay.check()):
                Br stern "那你就该走了。"
                c "..."
                Br "现在。"
                scene black with dissolvemed
                stop music fadeout 1.0
                $ brycestatus = "bad"
                $ leftbryce = True
                $ brycescenesfinished = 1
                jump _mod_fixjmp
            else:
                Br smirk "我明白了。"
                Br flirty "我们在我家试试清醒的做法怎么样？"
                c "好啊。"
                jump bangok_four_bryce1_apartment_decided
        "试图叫醒你。":
            c "对于人类来说，那是一个敏感的地方。我以为戳一下可能..."
            $ renpy.pause(0.8)
            Br brow "..."
            $ renpy.pause(0.8)
            play sound "fx/tableslap.wav"
            Br laugh "这倒是有效，我猜。"
            if brycemood < 4 or (bangok_four_common.bangnokay.check()):
                show bryce stern with dissolve
            else:
                show bryce smirk with dissolve
            Br "所以，这在人类中是正常的吗？"
            c "我的意思是，我们会有衣服保护它。"
            Br brow "对，你们穿了很多层。"
            if brycemood < 6 or (bangok_four_common.bangnokay.check()):
                Br stern "好吧，我需要回家，你也需要回家，让我们集中精力在这上。"
                c "我会帮你走回家。"
                $ renpy.pause(0.5)
                Br normal "谢谢。"
            else:
                Br flirty "你知道，我有点想看看你的衣服下有什么，回我家看看？"
                c "你在调戏我吗？"
                Br smirk "你有兴趣吗？"
                menu:
                    "接受。":
                        show bryce flirty with dissolve
                        $ renpy.pause(0.5)
                        jump bangok_four_bryce1_apartment_decided
                    "拒绝。":
                        $ brycemood -= 1
                        c "我们还是先送你回家，布莱斯。"
                        Br laugh "好吧！"
                        jump bangok_four_bryce1_nevermind

label bangok_four_bryce1_apartment:
    scene black with dissolvemed
    $ renpy.pause (0.6)
    scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0) with dissolvemed
    $ renpy.pause (0.5)
    show bryce normal dk with dissolve
    m "在布莱斯黑暗的公寓里，大龙直接冲向他的沙发。"
    menu:
        "[[打断他。]]":
            pass
        "[[回家。]]":
            m "我没能走到门口。"
            c "(不...我想我还是躺在这里吧。)"
            jump bangok_four_bryce1_nevermind
    c "布莱斯？"
    Br brow dk "嗯？"
    menu:
        "没事。":
            c "(所以...累。)"
            m "我没能走到门口。"
            jump bangok_four_bryce1_nevermind
        "想做点蠢事吗？":
            c "你喝醉了。我也喝醉了。而且你...非常吸引人。"
            c "你觉得怎么样？"
            $ renpy.pause (0.4)
            if brycemood < 5 or (bangok_four_common.bangnokay.check()):
                play sound "fx/cartslide.ogg"
                hide bryce with dissolve
                m "在我问完问题之前，布莱斯已经在他的沙发上睡得很熟了。"
                m "我放弃了，转身向门口走去，但很快又失去了仅有的一点力气。"
                c "(也许...我就睡在这里。)"
                jump bangok_four_bryce1_nevermind
            else:
                pass

    Br flirty dk "好吧。去他的。你也很可爱。"
    $ brycemood = 4

    if False:
        label bangok_four_bryce1_apartment_decided:
        scene black with dissolvemed
        $ renpy.pause (0.6)
        scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0) with dissolvemed
        $ renpy.pause (0.5)
        show bryce flirty dk with dissolve

    play sound "fx/undress.ogg"
    if bangok_four_common.bangnokay.check():
        $ renpy.pause(0.8)
        jump bangok_four_bangnokay_kill_replay
    m "我尽可能快地脱掉衣服，我的欲望昏了头。"
    if bangok_four_malepartners + bangok_four_femalepartners < 1:
        c "(这真的发生了吗？我真的要和一条龙做爱吗？)"
    show bryce at Position(ypos=1.1) with ease
    m "布莱斯把他的下半身翻到一边，一根巨大的阴茎从他两腿之间伸出来。"
    if persistent.bangok_balls == True:
        if persistent.bangok_inflation == True:
            m "当他的肌肉收紧时，一个无鳞的囊袋也显现出来，两个比苹果还大的圆球在他尾巴下湿润地晃动。"
        else:
            m "当他的肌肉收紧时，一个无鳞的囊袋也显现出来，两个比橘子还大的圆球在他尾巴下湿润地晃动。"
    c "嗯。看来你没有威士忌鸡巴。"
    Br brow dk "那是什么？"
    c "就是酒精让人很难...保持硬度。"
    Br "它总是硬的。"
    c "嗯。"
    Br smirk dk "那是我的。现在给我看看你的。"
    if bangok_four_playerhasdick == None:
        menu:
            "给他看你的阴茎。":
                $ bangok_four_playerhasdick = True
            "告诉他你没有阴茎。":
                $ bangok_four_playerhasdick = False

    if bangok_four_playerhasdick == True:
        jump bangok_four_bryce1_m
    else:
        jump bangok_four_bryce1_f

label bangok_four_bryce1_f:
    m "撩开我的阴唇，我给了他一瞥我的阴道。"
    Br flirty dk "啊。"
    Br smirk dk "想保持简单，直接来吗？"
    menu:
        "当然。":
            $ bangok_four_malepartners += 1
            $ brycemood += 1
            jump bangok_four_bryce1_f_fuck
        "嗯。其实...":
            show bryce brow dk with dissolve
            $ bangok_four_bryce1_m2_size = True
            $ bangok_four_bryce1_m2_fit = True
            label bangok_four_bryce1_f_menu:
            menu:
                "我想尝尝你。":
                    $ bangok_four_malepartners += 1
                    jump bangok_four_bryce1_oralbot
                "我想让你进入我的后门。":
                    $ bangok_four_malepartners += 1
                    jump bangok_four_bryce1_analbot
                "我想让你的舌头进入我。":
                    $ bangok_four_malepartners += 1
                    Br flirty dk "当然。但你得回敬我。"
                    jump bangok_four_bryce1_f_tonguefuck
                "我不确定我能容纳你。":
                    call bangok_four_bryce1_m2_fit from bangok_four_bryce1_f_menu_fit
                    jump bangok_four_bryce1_f_menu
                "好吧，继续。":
                    $ bangok_four_malepartners += 1
                    show bryce smirk dk with dissolve
                    jump bangok_four_bryce1_f_fuck

label bangok_four_bryce1_f_tonguefuck:
    call bangok_four_bryce1_position("oraltop")
    show bryce flirty dk with dissolve
    show bryce at Position(ypos=1.3) with ease
    show bryce at Position(ypos=1.5) with ease
    m "布莱斯低下身体，热气扑向我越来越湿润的阴唇。"
    if bangok_four_bryce1_position_picka != "oraltop":
        menu:
            "等一下！保护措施！":
                $ brycemood -= 1
                show bryce brow dk at Position(ypos=1.3) with ease
                Br "你在开玩笑吗？"
                c "我们不知道我的东西对你有什么影响。"
                Br stern dk "好吧，我有个坏消息。口交几乎从来不会引起什么问题，所以我不买牙套。"
                Br "而且我这个尺寸的也不便宜。"
                m "我停顿了一下，考虑我的选择。"
                menu:
                    "去他的。还是吃我吧。":
                        Br brow dk "你确定吗？"
                        c "是的。"
                        Br smirk dk "如你所愿。"
                        show bryce at Position(ypos=1.5) with ease
                        show bryce flirty dk
                    "跳过这个，我想让你进入我的后门。":
                        $ bangok_four_bryce1_position_picka = "analbot"
                        Br smirk dk "好吧。我有避孕套。在那边。最上面的抽屉。"
                        jump bangok_four_bryce1_analbot_fetchcondom
                    "跳过这个，我想让你进入我的阴道。":
                        $ bangok_four_bryce1_position_picka = "vag"
                        Br smirk dk "好吧。我有避孕套。在那边。最上面的抽屉。"
                        jump bangok_four_bryce1_f_fuck_getprotection
                    "也许我会给你口交。":
                        $ bangok_four_bryce1_position_picka = "oralbot"
                        Br flirty dk "哦？"
                        play sound "fx/cartslide.ogg"
                        show bryce normal dk at Position(xpos=0.4, xanchor='center') with dissolve
                        show bryce at Position(xpos=0.45, xanchor='center', ypos=1.05) with ease
                        m "布莱斯躺回沙发，尾巴勾住地毯和茶几，一条后腿伸展，给我提供了方便接触他的阴茎的机会。"
                        Br smirk dk "好吧。我有避孕套。在那边。最上面的抽屉。"
                        jump bangok_four_bryce1_oralbot_getprotection
            "[[享受。]]":
                    pass
    show bryce at Position(ypos=1.51) with ease
    m "布莱斯向前倾，张开大嘴包住我的下体，他的舌头直冲我的爱巢。"
    m "舌头和牙齿的感觉太过强烈。我向后倒，跌在地毯的边缘。"
    play sound "fx/impact3.ogg"
    show bryce brow dk at Position(ypos=1.2)
    show bangok_four_bryce1_apartment night at Pan((0,120), (0,120), 0.0)
    with vpunch
    Br "小心。"
    c "哦。"
    Br "你还好吗？"
    c "还好。"
    show bryce normal dk at Position(ypos=1.2)
    show bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
    with ease
    m "我站起来，环顾四周寻找可以依靠的东西，以便我们下次尝试。"
    menu:
        "墙。":
            $ bangok_four_bryce1_oralspot = "wall"
            c "这里，靠墙。"
            Br smirk dk "如果你这么说。"
            m "我稍微靠在墙上，分开双腿，让布莱斯更容易接近我的下体。"
            $ renpy.pause (0.3)
        "沙发。":
            $ bangok_four_bryce1_oralspot = "couch"
            c "这里，我坐在你的沙发上怎么样？"
            $ renpy.pause (0.5)
            Br brow dk "稍微向前一点。我不想让我的下巴角撕裂我的垫子。"
            $ renpy.pause (0.3)
    Br flirty dk "好吧。现在看看人类是什么味道。"
    show bryce smirk dk at Position(ypos=1.3) with ease
    show bryce smirk dk at Position(ypos=1.5) with ease
    $ renpy.pause(0.3)
    m "布莱斯在我腿间找到了位置，他的鼻子鳞片摩擦着我的大腿。"
    m "房间里的冷空气在我的下体变成了他的呼吸的温暖。"
    show bryce smirk dk at Position(ypos=1.51) with ease
    m "他再次张开嘴，小心地保持牙齿不碰到我的皮肤。我颤抖着，他长长的舌头在我的阴唇上来回舔。"
    c "哇。"
    show bryce flirty dk with dissolve
    $ renpy.pause(0.3)
    show bryce flirty dk at Position(ypos=1.52) with ease
    m "他深入探入，用舌头玩弄我的私密处，品尝着周围。"
    m "他的鳞片唇摩擦着我的大腿和肚子，牙齿的尖锐边缘轻轻触及。"
    if bangok_four_bryce1_oralspot == "couch":
        m "这种感觉和一丝危险让我的下半身麻木无力，滑向他的沙发，更深地承受他的舌头的侵入。"
    else:
        m "这种感觉和一丝危险让我的腿软，让我更进一步地滑在墙上，接受他热切的舌头侵入。"

    if persistent.bangok_watersports == True:
        m "当他的舌头向上探索我的阴唇顶部时，我感到体内的一个液袋被压缩，然后开始溢出到他的嘴里。"
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        show bryce brow dk with dissolve
        c "哦天哪，布莱斯我--"
        show bryce laugh dk with dissolve
        play sound "fx/gulping.wav"
        m "一旦开始，我就停不下来。我脸颊发烫，布莱斯显然知道发生了什么，但他继续用舌头玩弄我，吞噬我排出的液体。"
        stop soundloop fadeout 1.5
        stop sound fadeout 0.5
        $ renpy.pause (1.5)
        m "直到我完全释放后，他才缓缓抽出舌头，站起来朝我眨了眨眼。"
        show bryce flirty dk with dissolve
        show bryce at Position(ypos=1.4) with ease
        Br smirk dk "我经常和饮酒的伙伴做爱。你以为你是第一个在我身上排尿的人吗？"
        Br flirty dk "我的舌头可能甚至能进去。你介意吗...？"
        menu:
            "[[让布莱斯进入你的尿道。]]":
                $ bangok_four_bryce1_wstiming = "before"
                c "我...可以。"
                show bryce at Position(ypos=1.5) with ease
                m "布莱斯回到我的下体，热气扑向我发红的皮肤，他的舌头在我的阴道口周围寻找着。"
                m "我颤抖着，电火花般的快感在我的肚子上跳动，当他挑逗我的阴蒂时。"
                m "然后他找到了我的尿道口。"
                c "哦！"
                m "他的舌头在一个不该被扩张的孔洞里扩展开来，这种充实的感觉完全不同。"
            "[[拒绝。]]":
                show bryce brow dk with dissolve
                c "在人类中，这样做会导致尿路感染。龙中是否更常见？"
                Br "确实比较常见。什么是...？"
                show bryce stern dk with dissolve
                $ renpy.pause (0.3)
                m "他摇了摇头。"
                Br normal dk "哦，好吧。"
                show bryce at Position(ypos=1.5) with ease
                m "给我一点时间准备，布莱斯再次潜入我的下体。"

    show bryce laugh dk with dissolve
    m "我的背弓起来，失去了对他在我下体做的事情的控制。他小心地深入，湿润的嘴唇与我的下体紧贴，尽可能多地把舌头伸进去。"

    if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming is not None:
        m "随着他的舌头轻易穿过膀胱的入口，味道到达了我无法企及的地方，我再次感到尿意。"
        c "(我需要在龙的舌头上排尿。哦，这太美妙了。)"
    else:
        c "啊！"
        m "我的整个肚子都在颤抖，他的舌尖刚刚碰到了我的子宫口，内在的门。"

    if bangok_four_bryce1_oralspot == "wall":
        m "我在墙上滑下来，越来越接近高潮。我想让他再深入一点。"
    else:
        m "我几乎超越了有意识的思考。我距离高潮很近，我只需要他再深入一点。"
    menu:
        "[[抓住他的角。]]":
            $ bangok_four_hornincident = True
            $ brycemood -= 2
            if bangok_four_bryce1_oralspot == "couch":
                play sound ["fx/hit2.ogg", "fx/cartdown.ogg"]
                show bryce stern dk at Position(ypos=1.3) with vpunch
                m "布莱斯猛然一震，舌头从我体内抽出，鼻子撞到我的肚子上，震动了沙发。只是运气好我没有被他的牙齿或鼻角割伤。"
            else: # bangok_four_bryce1_oralspot == "wall":
                play sound ["fx/hit2.ogg", "fx/impact3.ogg"]
                show bryce stern dk at Position(ypos=1.3) with vpunch
                m "布莱斯猛然一震，舌头从我体内抽出，鼻子撞到我的肚子上，把我压在墙上。只是运气好我没有被他的牙齿或鼻角割伤。"
            c "他妈的！"
            $ renpy.pause (1.2)
            m "我颤抖着，他瞪着我，我几乎高潮的感觉慢慢消退，我的下体仍然充满热量。"
            c "好吧，不要摸角。明白了。"
            Br brow dk "不。可以。但要告诉我。这是我们一个敏感的地方。错误的方向拉角可能会把它们从我们的头骨上撕下来。"
            c "我不觉得我有那么强。"
            Br stern dk "我也不认为。但如果我没预料到，我还是会有反应。"
            m "布莱斯在我腿间重新找位置，几乎立刻把我带回到脸靠近他脸的状态。他的舌头在我下体来回舔着，玩弄我的阴蒂。"
            menu:
                "我能抓住你的...":
                    $ brycemood += 1
                    m "他简短的肯定性哼声是我需要的所有许可。我抓住他的角，把他的脸和舌头拉得更深，然后我达到了高潮。"
                "[[向下推。]]":
                    pass
        "[[向下推。]]":
            pass

    show black with fadequick
    if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming is not None:
        m "我的空爱道抽搐着，我的情欲液体滴落在他的下颌，他的舌头刺穿我的膀胱。"
        hide black with dissolveslow
        m "他慢慢抽出小心不引起我的尿道疼痛，尽管我的欲望大部分已经被释放。即便如此，这种感觉仍然让我颤抖不已。"
        m "然后他滑回了我的阴道里，舔了我的液体。"
    else:
        m "我的爱道紧紧缠绕他的舌头，挤压他的唾液，他的舌尖再次在子宫口轻轻吻。"
        hide black with dissolveslow
        m "他在那种深度停留了一会儿，我的抽搐让他的舌尖一次次顶到子宫口。"
        m "然后他退到较浅的地方，舔了我的高潮液体。"
    c "小心。我可能还..."
    show bryce flirty dk with dissolve
    show bryce normal dk at Position(ypos=1.3) with ease
    m "他对我眨了眨眼，然后完全抽出。"

    if bangok_four_bryce1_oralspot == "wall":
        m "我的腿几乎撑不住我靠在墙上。我的脑子一片混乱。"
    else: # couch
        m "我瘫倒在沙发上，一时完全用尽了力气。"

    m "一个细细的半圆形红点围绕在我的肚脐上方，是他牙齿的印记。"

    show bryce brow dk with dissolve
    show bryce at center with ease
    Br "你还好吗？"

    menu:
        "我再也不会找人类舔了。":
            Br stern dk "什么？有什么问题吗？"
            c "那...那太棒了。"
            $ brycemood += 1
            Br flirty dk "哦。"
            $ renpy.pause (0.5)
            Br smirk dk "你还能站起来吗？"
            c "可能需要点时间。"
        "你咬我了！":
            $ brycemood -= 2
            Br stern dk "我没有咬下来。你把你的下体撞到我的牙齿上。"
            Br brow dk "我尽力了，但我能做的有限。"
        "恢复中。":
            pass
    m "喘过气来，我挣扎着站起来。"
    $ bangok_four_bryce1_wstiming = None

    Br smirk dk "现在轮到我了？"
    label bangok_four_bryce1_f_preciprocity_menu:
    menu:
        "哦，干我吧。":
            jump bangok_four_bryce1_f_fuck
        "是的。轮到我尝尝你了。":
            jump bangok_four_bryce1_oralbot
        "插入我的后门。":
            jump bangok_four_bryce1_analbot
        "手淫可以吗？":
            jump bangok_four_bryce1_hand
        "我不确定我能容纳你。" if bangok_four_bryce1_m2_fit:
            call bangok_four_bryce1_m2_fit from bangok_four_bryce1_f_preciprocity_menu_fit
            jump bangok_four_bryce1_f_preciprocity_menu
        "我...觉得我已经够了。":
            Br brow dk "抱歉？"
            c "我..."
            $ renpy.pause (0.8)
            c "我觉得我要晕过去了。"
            Br stern dk "嘿！"
            scene black with fade
            play sound "fx/impact3.ogg"
            jump bangok_four_bryce1_badmorning









label bangok_four_bryce1_f_fuck:
    call bangok_four_bryce1_position("vag")
    m "布莱斯示意我躺在他的沙发上。"
    $ renpy.pause(0.5)
    scene bangok_four_bryce1_apartment night ceiling at Pan((0,360), (0,0), 2.0) with dissolve
    c "你要来了吗？"
    show bangok_four_bryce_underside_large dk at Position(yanchor='top',ypos=0.8) with dissolve
    Br flirty dk "马上就来。"
    menu:
        "等一下！保护措施！":
            m "我坐起来，阻止他压在我身上。"
            scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
            show bryce brow dk
            with dissolvemed
            Br "这真的有必要吗？我们是不同的物种。不可能怀孕。"
            menu:
                "[[坚持。]]":
                    $ brycemood -= 1
                    call bangok_four_bryce1_setprotected(True) from bangok_four_bryce1_f_fuck_protected
                    c "我们不知道你的体液对我有什么影响。"
                    show bryce stern dk with dissolve
                    m "布莱斯呻吟了一声，然后指着旁边的一个抽屉。"
                    Br "最上面的那个。我想。赶紧的。"
                    label bangok_four_bryce1_f_fuck_getprotection:
                    play sound "fx/rummage.wav"
                    m "有几种不同品牌的避孕套，包装上标着实际尺寸。随便选了一个。"
                    if persistent.bangok_balls == True:
                        m "拆开包装后，我回到他跟前，跪下来把避孕套套在他的阴茎上，一直到他的滑润的睾丸。"
                    else:
                        m "拆开包装后，我回到他跟前，跪下来把避孕套套在他的阴茎上。"
                "[[接受他的精液。]]":
                    call bangok_four_bryce1_setprotected(False) from bangok_four_bryce1_f_fuck_rejectprotection
                    c "有道理。"
            Br flirty dk "那我们继续吧。"
            scene bangok_four_bryce1_apartment night ceiling at Pan((0,0), (0,0), 2.0)
            show bangok_four_bryce_underside_large dk at Position(yanchor='top',ypos=0.8)
            with fade
            m "一眨眼的工夫，我又回到了沙发上。"
        "[[分开双腿。]]":
            call bangok_four_bryce1_setprotected(False) from bangok_four_bryce1_f_fuck_noprotection
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.6) with ease
    m "布莱斯站在我上方，再次朝我眨了眨眼，我把一条腿扔到沙发背上，另一条腿落在前面，试图为他腾出足够的空间。"
    Br "给我点时间，找准目标。"
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
    m "布莱斯爬上我，后腿仍在地上，前腿撑在沙发上。他的下腹传来的热量覆盖了我的裸露皮肤。"
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
    m "他的阴茎在我的腿上弹跳，终于找到了我们都渴望的位置。"
    Br laugh dk "在那里！"
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
    m "他的大阴茎轻松进入我的湿润阴道，刺痛着我的神经，让我的双腿变软。"
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
    m "我的反应显然让布莱斯担心，他立刻抽出来。"
    Br stern dk "[player_name]？你没事吧？"
    m "我点了点头，喉咙在努力想找到声音。"
    $ renpy.pause(0.8)
    c "没事。继续。"
    label bangok_four_bryce1_f_fuck_merge:
    Br flirty dk "哦？好吧。"
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
    m "他再次进入我的阴道，一股快感从我的腰下传来。"
    m "他停了一会儿，让我适应。"
    $ renpy.pause(0.8)
    Br smirk dk "再进一步？"
    menu:
        "请。":
            pass
        "是的！":
            pass
        "你打算一整晚都这么慢吗？":
            $ brycemood += 1
            play sound "fx/tableslap.wav"
            Br laugh dk "如果你继续说这些话，就不会了！"
            Br smirk dk "但我们现在慢慢来。我不想伤害你。"
    $ renpy.pause(0.5)
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.0) with ease
    m "他慢慢地推进，更深了一点。电火花在我的腹部跳跃，每根神经都感受到了滑动的入侵者。"
    m "然后他碰到了什么。"
    c "停！"
    m "布莱斯立刻停了下来，等我解释或给他更多指示。我稍微动了动，尝试感受情况。"
    m "我突然意识到他太深了，他正顶在我的子宫口！"
    if persistent.bangok_cervpen != True:
        c "我不能再深入了。"
        jump bangok_four_bryce1_f_fuck_nowomb
    menu:
        "小心地继续。":
            Br stern dk "怎么了？"
            c "你正顶着我的子宫。"
            Br brow dk "你确定要我继续吗？"
            menu:
                "是的。":
                    $ bangok_four_bryce1.fuckwomb = True
                    show bangok_four_bryce_underside_large:
                        ease 4.0 ypos (-2.1)
                    m "布莱斯小心地推进，把我的子宫口轻轻撑开。"
                    m "我努力放松，呼吸，不紧张地让他进入我的最深处。"
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.12) with ease
                    m "当他的阴茎头通过子宫口时，我们都发出了喘息声。"
                    menu:
                        "太棒了。":
                            pass
                        "太疼了！停下来！":
                            $ brycemood -= 1
                            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.04) with ease
                            m "布莱斯立刻抽出来，把他的阴茎头从子宫口退出来，让内在的门关闭。"
                            c "啊。天哪。"
                            Br stern dk "我们不会再这么深了。"
                            $ bangok_four_bryce1.fuckwomb = False
                            menu:
                                "但...":
                                    $ brycemood -= 1
                                    Br stern dk "[player_name]，那伤害了你。我们都不够清醒去医院。"
                                    c "..."
                                "谢谢。":
                                    $ brycemood += 1
                            $ renpy.pause(0.8)
                            jump bangok_four_bryce1_f_fuck_postwomb
                        "这可能让我对人类失去兴趣。":
                            Br stern dk "失去兴趣？什么意思？"
                            c "你的尺寸太棒了。没有人类这么大。"
                            Br smirk dk "啊。"
                            $ brycemood += 1
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.14) with ease
                    if persistent.bangok_balls == True:
                        if persistent.bangok_inflation == True:
                            m "他继续推进，直到我感受到他的睾丸在我的屁股上，双腿贴在我的大腿上。"
                        else:
                            m "他继续推进，直到我感受到他的睾丸在我的屁股上，双腿贴在我的大腿上。"
                    else:
                        m "他继续推进，直到我感受到他的大腿的温暖鳞片贴在我的大腿上。"
                    m "每一寸滑过我的子宫口，比他进入我的外阴道更让人愉悦。"
                "不。":
                    $ bangok_four_bryce1.fuckwomb = False
                    c "我不确定。我不知道我是否曾经..."
                    $ renpy.pause(0.8)
                    Br stern dk "..."
                    $ renpy.pause(0.8)
                    Br "我们最好不要冒这个险。"
                    c "好吧。"
        "我不能再深入了。":
            label bangok_four_bryce1_f_fuck_nowomb:
            $ bangok_four_bryce1.fuckwomb = False
            Br brow dk "我这么深入会伤害到你吗？"
            c "不，不会。但再深入你就会进入我的子宫。"
            Br stern dk "明白了。"

label bangok_four_bryce1_f_fuck_postwomb:
    if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming is not None:
        m "布莱斯深吸一口气，皱了皱眉。"
        Br brow dk "你还要我在你体内小便吗？我不确定这样是否安全..."
        menu:
            "现在就小便。":
                label bangok_four_bryce1_f_fuck_postwomb_wsnow:
                $ bangok_four_bryce1_wstiming = "before"
                $ brycemood += 1
                Br smirk dk "好吧。"
                $ renpy.pause(0.3)
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                m "布莱斯的阴茎抽搐了一下，然后扩张，开始放松膀胱。"
                Br laugh dk "啊..."
                if bangok_four_bryce1_protected == True:
                    if bangok_four_bryce1.fuckwomb == True:
                        m "温暖在我的最深处绽放，布莱斯直接把他的尿液排进避孕套里。"
                    else:
                        m "温暖在我的最深处绽放，布莱斯的尿液填满避孕套的储液囊，在我的阴道里剩余的空间里。"
                    if persistent.bangok_inflation == True:
                        m "他的液体源源不断地涌入，像厕所碗一样填满我的圣殿。我颤抖着，无法逃脱这种荣耀的压力，被迫围绕他膨胀的尿液气球扩展。"
                        $ bangok_four_bryce1_playerstuffed = True
                else:
                    if bangok_four_bryce1.fuckwomb == True:
                        m "温暖在我的最深处绽放，布莱斯直接把他的尿液排入我的子宫。"
                    else:
                        m "温暖在我的最深处绽放，布莱斯的尿液填满我剩余的空间，然后泄入我的子宫。"
                    if persistent.bangok_inflation == True:
                        m "他的液体源源不断地涌入，像厕所碗一样填满我的圣殿。我颤抖着，无法逃脱这种荣耀的压力，被迫围绕尿液扩展。"
                        $ bangok_four_bryce1_playerstuffed = True
                stop soundloop fadeout 1.0
                Br smirk dk "天哪。你真狂野。"
                Br flirty dk "我可能自换班开始就没撒尿了。希望你不介意。"
                $ renpy.pause(0.8)
                Br flirty dk "感觉好吗？"
                m "我点了点头，沉浸在温暖和充实感中。"
                Br smirk dk "好吧。让我们继续。"
            "等你射精后。":
                $ bangok_four_bryce1_wstiming = "after"
                c "我们先确保我能应付。"
                Br normal dk "好。我想我能忍住。"
            "也许还是不要。":
                label bangok_four_bryce1_f_fuck_postwomb_emptytank:
                $ bangok_four_bryce1_wstiming = None
                Br stern dk "那我得快点去。"
                if bangok_four_bryce1.fuckwomb == True:
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.04) with ease
                    m "他突然抽回子宫口，留下我太虚弱无法动弹，也无法思考。"
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
                m "我躺在那里，极度愉悦，他的阳具一寸一寸地退出来，留下了空虚。"
                hide bangok_four_bryce_underside_large with easeoutbottom
                scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0) with fade
                m "当他完全退出时，思绪回到我的脑海，我的第一个想法是一个奇怪的想法。"
                call bangok_four_bryce1_ws_emptying_the_tank(False, bangok_four_bryce1_protected)
                if bangok_four_bryce1_protected == True:
                    m "避孕套仍挂在他的阴茎上，像一个充满尿液的气球。"
                    menu:
                        "[[喝掉它。]]":
                            m "我捏住避孕套的末端，然后取下底部的环，把整个东西滑下来。尿液的味道扑面而来。"
                            show bryce flirty dk with dissolve
                            m "在我还没反应过来之前，我已经把环放进了嘴里，并把气球举到头顶。"
                            show bryce smirk dk with dissolve
                            play sound "fx/water2.ogg"
                            if persistent.bangok_inflation == True:
                                queue sound "fx/gulpslow2.wav"
                                $ renpy.pause (9.0)
                                m "这是一大体积。我必须中途暂停一下。当我喝完时，我感到充满了布莱斯膀胱刚刚离开的温暖。"
                            else:
                                queue sound "fx/gulping.wav"
                                $ renpy.pause (3.0)
                                stop sound fadeout 1.0
                            python:
                                brycemood += 1
                                bangok_four_bryce1_playerstuffed = True
                            Br flirty dk "看着你喝真热。"
                            m "吸吮着剩下的一点，我把它重新套在他的阴茎上。"
                            c "再次插入我。"
                        "[[换一个。]]":
                            m "我捏住避孕套的末端，然后取下底部的环，把整个东西滑下来。尿液的味道扑面而来。"
                            m "我打了个结，把它滚到一边。我回到抽屉，拿了另一个避孕套。"
                            c "继续吧。"

                scene bangok_four_bryce1_apartment night ceiling at Pan((0,0), (0,0), 2.0)
                show bangok_four_bryce_underside_large dk at Position(yanchor='top',ypos=-1.5)
                with dissolvemed
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.0) with ease
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.1) with ease
                m "布莱斯再次填满我，完成了我的洞。"
                if bangok_four_bryce1.fuckwomb == True:
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.14) with ease
                    m "然后他再次突破我的子宫口，清晰的思绪瞬间抛弃了我。"

    elif persistent.bangok_watersports == True and bangok_four_bryce1_wstiming is None:
        Br stern dk "嗯。"
        Br stern dk "该死。"
        c "嗯？"
        Br "之前喝了那么多酒，我有点得去解决一下。"
        if bangok_four_bryce1_playercame == True:
            Br smirk dk "就像你那样。"
        Br brow dk "这对你有关系吗？"
        menu:
            "什么？在我里面？":
                $ brycemood -= 2
                Br stern dk "不喜欢这种反应。"
                jump bangok_four_bryce1_f_fuck_postwomb_emptytank
            "去处理你的事。":
                $ brycemood -= 1
                jump bangok_four_bryce1_f_fuck_postwomb_emptytank
            "我可能会感兴趣。":
                Br smirk dk "现在，还是等会儿？我的膀胱倾向于现在。"
                menu:
                    "现在。":
                        jump bangok_four_bryce1_f_fuck_postwomb_wsnow
                    "等你射精后。":
                        $ bangok_four_bryce1_wstiming = "after"
                        c "我们先确保我能应付。"
                        Br normal dk "好。我想我能忍住。"

    if persistent.bangok_balls == True:
        m "他坐在那里很长一段时间，完全插入我体内，我的身体在他身下抽搐，我的下体每次抽搐都伴随着他的重球碰撞。"
    else:
        m "他坐在那里很长一段时间，完全插入我体内，我的身体在他身下抽搐。"
    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.95) with ease
    if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
        if bangok_four_bryce1_protected == True:
            m "然后他抽出来，避孕套在我子宫口被拉伸的时候卡住了。"
            Br smirk dk "我最好小心点。不想让它在你里面破裂。"
        else:
            m "然后他抽出来，拔出我的子宫口，让里面的尿液有了新的去处。"
            Br smirk dk "我最好小心点。不想让它洒得到处都是。"
    else:
        if bangok_four_bryce1.fuckwomb == True:
            if bangok_four_bryce1_protected == True:
                m "然后他抽出来，留下内门紧缩的避孕套储液囊。"
            else:
                m "然后他抽出来，留下内门只有他的阴茎头在里头。"
            Br laugh dk "感觉像是你在里面有个嘴巴！"
            Br flirty dk "介意我继续干它吗？"
        else:
            m "然后他抽出来，留下我的通道宽敞而疼痛，渴望他。"
            Br "准备好了吗？"
    c "是的。"

    $ renpy.pause(0.5)

    if bangok_four_bryce1.fuckwomb == True:
        play soundloop "fx/rub2.ogg" fadein 1.0
        show bangok_four_bryce_underside_large:
            ease 0.5 ypos (-2.12)
            ease 0.7 ypos (-2.0)
            repeat
        $ renpy.pause(0.8)
        if persistent.bangok_balls == True:
            m "布莱斯开始真正干我，他的球撞击我的屁股，每次抽出时都保持大部分阴茎在内，他一次又一次突破我的子宫。"
        else:
            m "布莱斯开始真正干我，每次抽出时都保持大部分阴茎在内，他一次又一次突破我的子宫。"
        if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
            m "尿液在我体内来回流动，他的每一次抽插都把它推进更深。"
    else:
        play soundloop "fx/rub2.ogg" fadein 1.0
        show bangok_four_bryce_underside_large:
            ease 0.5 ypos (-2.0)
            ease 0.7 ypos (-1.9)
            repeat
        $ renpy.pause(0.8)
        m "布莱斯开始真正干我，用力量刺穿我的爱道。"
        if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
            m "尿液在我体内来回流动，他的每一次抽插都把它推进更深。"

    m "我毫无抵抗力。"
    $ bangok_four_bryce1_playercame = True
    show black with fadequick
    c "哦！布莱斯！"
    $ renpy.pause(0.8)
    hide black with dissolveslow
    $ renpy.pause(0.5)

    m "从高潮中下来花了一些时间，因为他一直保持节奏。"
    $ renpy.pause(1.0)
    m "我确信我的下半身的每一块肌肉在几天内都无法动弹，每次他抽插都在我的心灵海岸上掀起一波又一波的快感。"

    if persistent.bangok_knot == True:
        if bangok_four_bryce1.fuckwomb == True:
            Br stern dk "内射还是外射？"
            c "什么？"
            Br brow dk "结！内射还是外射？"
            $ renpy.pause(0.5)
            menu:
                "你有结？！":
                    $ bangok_four_bryce1.knotpos = "inoops"
                "内射！":
                    $ brycemood += 1
                    $ bangok_four_bryce1.knotpos = "in"
                "外射！":
                    $ bangok_four_bryce1.knotpos = "out"
        else:
            m "布莱斯俯身靠近我，呼出的热气扑向我的头发。"
            Br stern dk "该死的，我想打个结。"
            $ renpy.pause(0.8)
            menu:
                "你有结？！":
                    $ bangok_four_bryce1.knotpos = "out"
                "那就来吧！":
                    $ bangok_four_bryce1.knotpos = "in"
                "我希望...":
                    $ brycemood += 1
                    $ bangok_four_bryce1.knotpos = "out"
                "别！":
                    $ bangok_four_bryce1.knotpos = "out"
                "[[什么都不说。]]":
                    $ bangok_four_bryce1.knotpos = "out"
    else:
        Br stern dk "不久了..."
    stop soundloop fadeout 1.0
    play sound "fx/snarl.ogg"
    if bangok_four_bryce1.knotpos == "in" 或 (bangok_four_bryce1.knotpos is None 且 bangok_four_bryce1.fuckwomb == True):
        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.15) with ease
        if bangok_four_bryce1.fuckwomb == False:
            m "我大声尖叫，猛然向后抽身，当布莱斯咆哮着穿透我的子宫，直接射到了我的子宫里。"
        else:
            if bangok_four_bryce1_protected == True:
                if persistent.bangok_balls == True:
                    m "布莱斯射精了，把我的腿分得更开，把我们的臀部拉在一起，他的球撞击我的屁股，完全插入我体内，填满避孕套。"
                else:
                    m "布莱斯射精了，把我的腿分得更开，把我们的臀部拉在一起，完全插入我体内，填满避孕套。"
            else:
                if persistent.bangok_balls == True:
                    m "布莱斯射精了，把我的腿分得更开，把我们的臀部拉在一起，他的球撞击我的屁股，完全插入我体内，涂满了我的子宫。"
                else:
                    m "布莱斯射精了，把我的腿分得更开，把我们的臀部拉在一起，完全插入我体内，涂满了我的子宫。"
    else:
        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.05) with ease
        if bangok_four_bryce1_protected == True:
            m "布莱斯射精了，阴茎头紧贴内门，然后抽出来，在避孕套里射精。"
        else:
            m "布莱斯射精了，阴茎头紧贴内门，在里头射出了白色的绳索。"

    if bangok_four_bryce1.knotpos == "in" 且 bangok_four_bryce1.fuckwomb == False:
        play sound ["fx/hit1.ogg", "fx/hit2.ogg"]
        m "疼痛太过强烈，我无法从中找到任何享受。我拍打他的腹部鳞片，试图引起他的注意，让他抽出来。"
    else:
        show black with fadequick
        m "这种感觉让我的高潮再次推向顶峰。"
        $ renpy.pause(0.8)
        hide black with dissolveslow
        $ renpy.pause(0.5)

    if persistent.bangok_inflation == True:
        m "布莱斯没有减速，他的阴茎继续抽搐，源源不断地射出精液。"
        if bangok_four_bryce1_protected == True:
            if persistent.bangok_watersports == True 且 bangok_four_bryce1_wstiming == "before":
                m "避孕套的储液囊在我子宫内膨胀，压迫着我所有的内在空间，精液和尿液寻找空间填满我。"
            else:
                if persistent.bangok_cervpen:
                    m "避孕套的储液囊在我子宫内膨胀，压迫着我所有的内在空间，精液寻找空间填满我。"
                else:
                    m "避孕套的储液囊在我的阴道内膨胀，压迫着我所有的内在空间，精液寻找空间填满我。"
        else:
            $ bangok_four_bryce1_playerstuffed = True
            if persistent.bangok_watersports == True 且 bangok_four_bryce1_wstiming == "before":
                m "精液和尿液充满了我的子宫，把我的圣殿充满了他的液体。"
            else:
                m "精液充满了我的子宫，把我的圣殿充满了他的种子。"

        if bangok_four_bryce1.knotpos == "in" 且 bangok_four_bryce1.fuckwomb == False:
            c "布莱斯！求你！"
        else:
            c "布莱斯！"
        Br flirty dk "差不多..."
        m "看向下方，我发现自己的肚子几乎看起来像怀孕了一样，膨胀着龙的阴茎和液体。"

        if bangok_four_bryce1_protected == True 且 persistent.bangok_watersports == True 且 bangok_four_bryce1_wstiming == "before":
            play sound "fx/bubbles.ogg"
            c "啊！"
            m "避孕套破裂了，精液和尿液立即充满了我的管道，浸透了我的子宫，将我的圣殿充满了布莱斯的液体。"
            m "我的肚子现在清晰地凸起，随着液体和肉体的膨胀。"
            $ bangok_four_bryce1_playerstuffed = True

    $ renpy.pause(0.8)

    if bangok_four_bryce1.knotpos != "in" 或 (bangok_four_bryce1.fuckwomb == True):
        show bangok_four_bryce_underside_large:
            ease 1.0 ypos -2.0
            ease 1.0 ypos -1.7
            ease 1.0 ypos -1.3
            ease 1.0 ypos -0.7
    else:
        show bangok_four_bryce_underside_large:
            ease 1.0 ypos -2.0
            ease 1.0 ypos -1.7
    m "在高潮后的一长段时间里，布莱斯用前腿撑着我的肩膀，把臀部和阴茎保持在原位，弯下头来看着我。"
    $ bangok_four_bryce1_brycecame = True


    if bangok_four_bryce1.knotpos == "in" 且 bangok_four_bryce1.fuckwomb == False:
        m "他的表情立刻变得严肃。"
        $ brycemood -= 3
        Br brow dk "怎么了？"
        Br stern dk "该死。"
        m "在布莱斯的目光中，我几乎要哭了，手放在我的子宫上，希望能让他的阴茎回到正确的位置。"
        c "快把它拿出来。"

        m "他用前腿撑住我的肩膀，拉扯着，但那只会让我再一次痛苦地喊叫，因为他的结几乎要撕裂我的阴道。"
        Br stern dk "见鬼，[player_name]，你为什么要鼓励我？"
        menu:
            "对不起。":
                $ brycemood += 1
                c "我不是故意的...我没想到..."
                c "我以为我能..."
                c "但我不能..."
            "我没想到你会！":
                $ brycemood -= 2
                c "你是搞砸了！"
                c "我本来觉得很棒，直到你想把我撕裂！"
                c "快把它拔出来！"
            "求你了...":
                $ brycemood -= 1
                c "太疼了。"
        Br stern dk "我尽力了。"
        m "他放松了角度，疼痛减轻了很多，但他的结仍然太大，无法取出。"
        Br stern dk "我觉得我拔不出来了。"
        menu:
            "谢谢...你尽力了。":
                c "这...稍微好点了。"
                Br normal dk "够睡了吗？"
                c "也许吧。"
            "去你的。":
                $ brycemood -= 2
                Br stern dk "如果你没有鼓励我，我们就不会这样。"
        Br brow dk "我觉得唯一的选择就是试着睡一觉。"
        if persistent.bangok_watersports == True 且 bangok_four_bryce1_wstiming == "after":
            c "你不是还需要撒尿吗？"
            if brycemood < 0:
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                m "我刚问完这个问题，他就释放了一种不同的粘稠温暖液体进入我被堵住的子宫。"
                Br stern dk "不合时宜的问题。"
                menu:
                    "去你！":
                        $ brycemood -= 2
                        Br stern dk "我之前问过你时就提醒过你。"
                        c "你他妈的说话时还没完全插入我子宫！"
                    "哦。":
                        $ renpy.pause(0.5)
                label bangok_four_bryce1_f_fuck_badknot_piss:
                if persistent.bangok_inflation == True:
                    m "尿液对子宫颈的压力导致新的痉挛，我的动作只会让事情变得更糟。"
                    if bangok_four_bryce1_protected == True:
                        play sound "fx/bubbles.ogg"
                        c "啊！"
                        m "避孕套破裂了，精液和尿液立即充满了我的管道，浸透了我的子宫，将我的圣殿充满了布莱斯的液体。"
                        m "我的肚子现在清晰地凸起，随着液体和肉体的膨胀。"
                        Br stern dk "抱歉。"
                stop soundloop fadeout 1.0
                menu:
                    "我可能能熬过去。":
                        $ brycemood += 1
                    "永远别让你靠近我的阴道。":
                        $ brycemood -= 2
            else:
                Br stern dk "我需要撒尿。很勉强忍住。"
                menu:
                    "试着忍住？":
                        Br stern dk "我会尽力。"
                    "好吧...":
                        Br normal dk "你确定吗？"
                        c "我看不出这会让事情变得更糟。"
                        $ renpy.pause(0.5)
                        play soundloop "fx/faucet1.ogg" fadein 1.0
                        queue soundloop "fx/faucet2.ogg"
                        $ renpy.pause(0.8)
                        jump bangok_four_bryce1_f_fuck_badknot_piss
        jump bangok_four_bryce1_tiedsleep

    if persistent.bangok_watersports == True 且 bangok_four_bryce1_wstiming == "after":
        Br flirty dk "准备好第二部分了吗？"
        if persistent.bangok_inflation == True:
            c "呃。"
        else:
            c "嗯。"
        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
        m "布莱斯呻吟着向前靠，然后他的阴茎在我体内再次抽搐，一种新的、更粘稠的温暖液体开始在我最神圣的地方蔓延开来。"
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        Br laugh dk "啊..."
        if persistent.bangok_inflation == True 且 bangok_four_bryce1_protected == True:
            play sound "fx/bubbles.ogg"
            c "啊！"
            m "避孕套破裂，布莱斯更多的尿液让它无法承受。我几乎看起来像怀孕了一样，肚子因为液体和肉体而膨胀。"
            $ bangok_four_bryce1_playerstuffed = True
        elif bangok_four_bryce1_protected == True:
            m "我呻吟着，身体麻木，布莱斯在避孕套里尿尿。"
        else:
            $ bangok_four_bryce1_playerstuffed = True
            m "我呻吟着，身体麻木，布莱斯在我体内尿尿，直到每一寸都被他的尿液浸透。"
        if persistent.bangok_inflation == True:
            m "我看起来像怀孕了一样，肚子因为液体和肉体而膨胀。"
        
        stop soundloop fadeout 1.5
        m "布莱斯慢慢向下看，一边处理着我们制造的混乱。"
        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.7) with ease
        Br flirty dk "可能从换班开始就没有尿了。希望你不介意。"

    if persistent.bangok_inflation == True:
        m "他用爪子揉了揉我突起的肚子。"
        Br flirty dk "肯定填满了你，对吧？"
        m "我无法回答，只能在温暖的液体下沉浸。"

    if persistent.bangok_watersports and persistent.bangok_inflation and bangok_four_bryce1_protected:
        $ brycemood += 1
        Br stern dk "哦。该死。我想避孕套破了。"
        menu:
            "显然！":
                $ brycemood -= 2
                Br "我不完全控制它的完整性。"
                c "不在里面尿尿可能会保持它完好。"
                Br "是谁说他们同意的？"
            "该死。":
                Br "是的，抱歉。"
                Br flirty dk "不过，一场不错的做爱，对吧？"
                m "我点了点头。"
            "那感觉还不错...":
                Br flirty dk "是吗？"
    else:
        Br flirty dk "好了吗？"
        m "我点了点头。"

    if persistent.bangok_knot == True 且 bangok_four_bryce1.knotpos == "in":
        Br flirty dk "希望你喜欢，因为我不认为你的阴道会再让结出来。"
        jump bangok_four_bryce1_tiedsleep
    else:
        if brycemood < 0:
            jump bangok_four_bryce1_f_fuck_pullout
        else:
            Br "你要我抽出来吗？还是想这样睡？"
            menu:
                "这样睡。":
                    $ brycemood += 1
                    scene black with dissolveslow
                    m "布莱斯瘫倒在沙发上，小心地把我移到边缘，以免压坏我。"
                    if bangok_four_bryce1_protected == False 或 (persistent.bangok_watersports 和 persistent.bangok_inflation):
                        m "他也调整了臀部，把阴茎头顶在子宫口，以防泄漏。"
                    Br smirk dk "晚安，[player_name]。"
                    jump bangok_four_bryce1_morningcouch
                "抽出来。":
                    label bangok_four_bryce1_f_fuck_pullout:
                    scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
                    show bryce stern dk
                    with dissolvemed
                    if (persistent.bangok_watersports 和 persistent.bangok_inflation 和 bangok_four_bryce1_protected) 或没有使用避孕套:
                        # 破了的避孕套或没有避孕套
                        play sound ["fx/slide.ogg","fx/spray.ogg"] fadein 0.5
                        m "布莱斯的阴茎从我体内抽出，边缘滴着我们的液体。"
                    elif persistent.bangok_inflation:
                        # 满的避孕套
                        play sound "fx/slide.ogg" fadein 0.5
                        m "布莱斯用力拉，但无法把充满液体的避孕套拉出我的子宫。"
                        Br stern dk "见鬼。我的尺寸问题。"
                        c "也许我应该推一下？"
                        Br brow dk "先让我把避孕套的一些部分拿出来。"
                        play sound "fx/pour.ogg"
                        $ renpy.pause(3.0)
                        m "我感受到液体从我的子宫流入避孕套，布莱斯继续拉出来，就像拔软木塞一样。"
                        play sound "fx/uncork.ogg"
                        m "最后一点液体的释放带来的感觉足以震颤我的身体。"
                    else:
                        # 正常使用的避孕套
                        play sound ["fx/slide.ogg","fx/uncork.ogg"] fadein 0.5
                        if persistent.bangok_watersports 和 bangok_four_bryce1_wstiming 不是 None:
                            m "布莱斯把自己拉出来，避孕套里他的精液和尿液在子宫颈处爆发，带来震颤的快感。"
                        else:
                            if persistent.bangok_cervpen:
                                m "布莱斯拉出来，避孕套里的精液从子宫颈处滑过，带来震颤的快感。"
                            else:
                                m "布莱斯拉出来，避孕套里的精液从阴道滑过，带来震颤的快感。"
        if brycemood < 0:
            Br stern dk "地板是开放的。或者你可以这样回家。"
            m "我挣扎着从沙发上站起来，双腿太软无法支撑我。"
            c "地板就好..."
            play sound "fx/impact3.ogg"
            scene black with vpunch
            jump bangok_four_bryce1_morningfloor
        else:
            Br normal dk "你想留在沙发上吗？"
            m "我点了点头。"
            c "在经历了这些之后，我不确定我能动了。天哪。"
            Br flirty dk "好吧，我准备睡觉了。"
            scene black with dissolveslow
            Br "晚安，[player_name]。"
            c "晚安。"
            jump bangok_four_bryce1_morningcouch


label bangok_four_bryce1_m:
    show bryce brow dk with dissolve
    $ renpy.pause(0.9)
    m "Bryce 看起来并不满意。"
    c "你比我大两倍，当然显得更大。"
    if persistent.bangok_balls:
        Br "不，不，我懂了。你的裂缝呢？"
        c "裂缝？{w=0.8}我没有那个。"
        Br smirk dk "那你的器官就这样暴露在外？没有保护？还那么软趴趴的？"
    else:
        Br "不，不，我懂了。那是什么？"
        c "嗯？{w=0.8}哦，是睾丸。精子从那里出来。"
        Br smirk dk "它们就这样暴露在外？没有保护？在这么软的东西下？"
    c "是的。虽然，现在不应该这么软的。可能是威士忌效应吧。"
    $ renpy.pause(0.5)
    Br flirty dk "你的睾丸敏感吗？"
    c "... 我不确定我喜欢这个方向。"
    show bryce at Position(ypos=1.3) with ease
    show bryce at Position(ypos=1.5) with ease
    m "Bryce 磕磕绊绊地靠近了一点，舌头伸出，露出大大的笑容。"
    menu:
        "[[让他继续。]]":
            pass
        "小心角！":
            c "我有点脆弱！"
            Br smirk dk "我会小心的。"
        "[[停止他。]]":
            m "我后退了一步，Bryce 突然停住了。"
            show bryce at center with ease
            c "{i}真的{/i}很敏感。我觉得最好不要这样..."
            show bryce normal dk with dissolve
            show bryce at Position(ypos=1.3) with ease
            $ renpy.pause(0.4)
            show bryce at center with ease
            Br smirk dk "好吧。"
            jump bangok_four_bryce1_m2

    show bryce flirty dk with dissolve
    m "Bryce 带着酒味的热气息让我的腹股沟颤抖。{w=0.3}绕过我的阳具，他用舌头缠绕住了我的阴囊底部，轻轻拉扯。"
    m "这么多粗糙的舌头在我的睾丸上滑动是如此新奇的体验，我的阳具立即跳了起来，碰到了他的鼻子。"
    show bryce smirk dk at Position(ypos=1.3) with ease
    Br flirty dk "现在你硬了。"
    c "是的，那，呃，那是新的体验。"
    Br laugh dk "对我来说也是新的体验！"
    show bryce normal dk with dissolve
    show bryce at center with ease
    if persistent.bangok_balls:
        Br normal dk "从没见过这些东西...总是这样在外面。干燥的皮肤味道也很奇怪。"
    else:
        Br normal dk "从没见过这些东西...在外面。皮肤的味道也很奇怪。"
    c "好奇怪还是坏奇怪？"
    Br brow dk "不同。"

label bangok_four_bryce1_m2:
    Br normal dk "接下来呢？你想让我在上面？还是你想把那小东西插进我里面？"
    $ bangok_four_bryce1_m2_size = True
    $ bangok_four_bryce1_m2_fit = True
    label bangok_four_bryce1_m2_menu:
    menu:
        "我想尝尝你。":
            $ bangok_four_malepartners += 1
            label bangok_four_bryce1_oralbot:
            call bangok_four_bryce1_position("oralbot")
            Br smirk dk "你真想尝试吗？"
            play sound "fx/cartslide.ogg"
            show bryce normal dk at Position(xpos=0.4,xanchor='center') with dissolve
            show bryce at Position(xpos=0.45,xanchor='center',ypos=1.05) with ease
            m "Bryce 靠在沙发上，卷起地毯并拉动咖啡桌，他的尾巴在一刻抓住了。"
            m "他伸出了一条后腿，让我从沙发旁轻松接触到他的阳具。"
            Br flirty dk "过来吧。"
            if bangok_four_bryce1_protected == False and not bangok_four_bryce1_playercame:
                m "我昏昏沉沉的大脑在跟随他的命令之前，提出了一个重要的想法。"
                c "等一下，保护措施呢？"
                if bangok_four_playerhasdick == True:
                    Br brow dk "你在开玩笑吧？口交不会怀孕。我们都是男人。"
                else:
                    Br brow dk "你在开玩笑吧？口交不会怀孕。"
                Br smirk dk "除非人类有我不理解的地方。"
                c "不，基本上是这样。"
                Br "那有什么问题？"
                menu:
                    "[[坚持。]]":
                        c "我们不知道你的东西对我会有什么影响。"
                        if chapter2unplayed == False and chapter2storeunplayed == False and chap2storehealth == False:
                            c "我见过健康区。你们有避孕套。"
                        else:
                            c "你们的种族有避孕套，对吗？"
                        show bryce stern dk with dissolve
                        m "Bryce 哼了一声，然后指了指角落里的一个抽屉柜。"
                        Br "顶层。我想。快点。"
                        label bangok_four_bryce1_oralbot_getprotection:
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.wav"
                        if bangok_four_playerhasdick == True:
                            m "有几个不同品牌，上面有与Bryce比例相符的“实际尺寸”标记。我选择了一个标有安全口交的，然后又深挖了一下，找一个适合我尺寸的，以防事情进一步发展。"
                            m "只在挖到最底层时，才终于找到一个更接近我尺寸的未开封的避孕套。"
                        else:
                            m "有几个不同品牌，上面有与Bryce比例相符的“实际尺寸”标记。我选择了一个标有安全口交的。"
                        m "撕开包装，我带着必要的装备回来了。"
                        label bangok_four_bryce1_oralbot_condom:
                        m "我跪在 bryce 旁边，感觉唾液在我口中聚集，当我沿着他的阳具展开橡胶安全套时。"
                        Br flirty dk "该死。这有点挑逗。你的手真的很光滑。"
                        $ brycemood += 1
                    "[[直接饮用。]]":
                        $ bangok_four_bryce1_protected = False
                        c "好像没有，我猜。"
                        m "我跪在Bryce旁边，感觉唾液因预期而在嘴里聚集。"
            elif bangok_four_bryce1_protected:
                menu:
                    "[[给他戴上避孕套。]]":
                        jump bangok_four_bryce1_oralbot_condom
                    "[[直接饮用。]]":
                        $ bangok_four_bryce1_protected = False
                        m "我跪在Bryce旁边，感觉唾液因预期而在嘴里聚集。"
                        Br brow dk "保护措施？"
                        c "改变主意了。我想要这个。"
                        if bangok_four_bryce1_position_picka in ["oraltopwall","oraltopcouch"]:
                            $ brycemood -= 3
                            Br stern dk "我也想尝尝你的负荷。但你想保护我免受它的伤害。你怎么能确定我的不会伤害你？"
                            c "我想我不能。"
                            Br "..."
                            m "当我靠近时，他并没有阻止我。"
            
            if bangok_four_bryce1_protected:
                m "我俯身在 Bryce 的肚子和后腿上，轻轻握住他的阳具靠近根部。我不太确定可以多粗鲁，因为他是不同的物种。"
            else:
                m "我俯身在Bryce的肚子和后腿上，轻轻握住他的阳具靠近根部。我不太确定可以多粗鲁，因为他是不同的物种。"

            Br laugh dk "嘿！不要{我}挠{/i}它！"
            m "我收紧了握力，尝试上下抽动了一下，然后松开，向上看寻求他的认可。"
            Br flirty dk "更好。"

            if not bangok_four_bryce1_protected:
                m "我锁定了他的阳具顶端，它奖励我一滴闪亮的前液。"

            if persistent.bangok_watersports == True:
                call bangok_four_bryce1_ws_conversation from bangok_four_bryce1_oralbot_ws_conversation
                if bangok_four_bryce1_wstiming not in ["before","after"]:
                    show bryce normal dk at Position(xpos=0.4,xanchor='center') with dissolve
                    show bryce at Position(xpos=0.45,xanchor='center',ypos=1.05) with ease
                    if bangok_four_bryce1_protected:
                        m "Bryce 又躺回沙发上。等他定下来后，我把避孕套拉回他的阳具。"
                    else:
                        m "Bryce 又躺回沙发上。"

            m "调整我的位置，我躺在他的一条后腿上，使我的脸与他的顶端齐平，同时还能看到他的脸。"
            if bangok_four_bryce1_protected:
                m "然后我的嘴唇碰上了他的顶端，轻轻撕开避孕套，开始小心翼翼地探索我能装多少。"
            else:
                if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming not in ["before","after"]:
                    m "然后我的嘴唇碰上了他的顶端。我还能品尝到他最近小便的味道，我自问为何要让他摆脱那金色的液体。"
                else:
                    m "然后我的嘴唇碰上了他的顶端。他的前液，远远超乎我对人类的理解，实际上是接近甜的！"
                m "我向下沉了一小段，开始小心翼翼地探索我能装多少。"
            if persistent.bangok_balls == True:
                if persistent.bangok_inflation == True:
                    m "当我探索他的顶端时，我轻轻地开始提升和按摩他的温暖，沉重的睾丸。我能感觉到里面的种子重量，因为我玩弄它们。它们的无鳞表面仍然微湿，从裂缝内部。"
                else:
                    m "当我探索他的顶端时，我轻轻地开始提升和按摩他的温暖的睾丸。我能感觉到它们的无鳞表面仍然微湿，从裂缝内部。"
            m "他的反应不是我预期的。"
            Br smirk dk "如果你想这么慢，我们可能要在这里待一整晚。你几乎没有用过你的舌头。"
            m "当我用一个湿润的“啪”声释放他的顶端时，他的表情改变了。"
            Br brow dk "那是什么？"
            menu:
                "吸力。":
                    c "人类的嘴唇可以很好地密封。猜你还没有感受过吧？"
                    Br flirty dk "猜没有。但我想再感受一次。"
                "你会发现的。":
                    $ brycemood += 1
                    Br flirty dk "不管是什么，感觉很好。"
            $ renpy.pause (0.8)
            show bryce stern dk with dissolve
            $ renpy.pause (0.3)
            m "他的后腿在我下面弯曲，他皱起眉头。"
            Br "我们可能需要换一个位置。"
            play sound "fx/cartslide.ogg"
            show bryce normal dk flip with dissolvemed
            m "靠后，我给了 Bryce 空间，他转向一侧。在他努力下，沙发发出了抱怨声。"
            m "现在，他的阳具在我面前摆动，轻松可见。"
            Br flirty dk flip "更好？"
            c "好多了。"

            if bangok_four_bryce1_protected:
                m "我再次握住他的阳具以稳住它，然后包住他的整个头部。避孕套的储液囊在我的舌头上滑下，我尽量把嘴唇向下滑动。它停在我喉咙的某个地方，他的大头撞到了我的嘴后，我便干呕起来。"
            else:
                m "我再次握住他的阳具以稳住它，然后包住他的整个头部。他的阴茎头的皮肤光滑，几乎已经有点湿润。他尝起来像..."
                menu:
                    "龙。":
                        m "真的没有更好的词来形容了。"
                    "啤酒。":
                        m "他的阳具有一种啤酒花和酒精的余味。我不得不怀疑，这是因为他喝了多少，还是意外洒出来，或者是之前的酒后口交残留物没有清理干净。"
                    "裂缝液。":
                        m "稍微有点咸，这种湿润来自他阴茎上的某种润滑剂。"
                    "人类的体液。" if persistent.bangok_cloacas and bangok_four_bryce1_position_picka=="ptop" and not bangok_four_bryce1_protected_a:
                        m "由于他的阳具和屁股共用同一个洞，我能品尝到我插入他身体后的结果。结合他的自然味道，这是一种无与伦比的味道。"
            
            m "当我吸气，使我的嘴形成一个真空包围他的头时，Bryce 抬起了一条腿。"
            Br laugh dk flip "就是这个！"
            m "我上下摇动我的头，保持我的密封。"

            if persistent.bangok_watersports == True:
                if bangok_four_bryce1_wstiming == "after":
                    Br stern dk flip "等一下。我需要一秒钟来憋住小便。"
                    Br flirty dk flip "除非你现在想要？"
                    menu:
                        "继续吸。":
                            label bangok_four_bryce1_oralbot_ws_before:
                            $ bangok_four_bryce1_wstiming = "before"
                            show bryce laugh dk flip with dissolve
                            if bangok_four_bryce1_protected:
                                menu:
                                    "喉咙。":
                                        play soundloop "fx/faucet1.ogg" fadein 1.0
                                        queue soundloop "fx/faucet2.ogg"
                                        m "我尽量向前推，避免触发干呕反射，然后{i}吸{/i}。{w=0.5}Bryce 的嘴巴在极乐中张开，他的膀胱放松，将金色液体送入我的喉咙。"
                                        m "但有些东西不对劲。避孕套的储液囊仍然在我的喉咙里，但现在它因注入的液体而膨胀并向下垂。它堵住了我的喉咙！"
                                        stop soundloop fadeout 6.0
                                        m "我用双手抓住Bryce的阳具，确保避孕套，然后猛地将头后拉。"
                                        play sound "fx/water1.ogg"
                                        m "避孕套的膨胀储液囊在Bryce小便结束时，以淫荡的拍击声打在沙发的一侧。"
                                        Br flirty dk flip "有点太多了？"
                                        m "我点了点头，眼睛充满泪水，仍在努力均匀呼吸，并清除喉咙中的粘液。"
                                        Br stern dk flip "等一下，你还好吗？"
                                        c "会好的。"
                                        python:
                                            brycemood -= 2
                                            renpy.pause (1.5)
                                        Br "不要伤到自己。我认为我们俩都不够清醒，无法送你去医院。"
                                        c "..."
                                        $ renpy.pause (0.8)
                                    "嘴巴。":
                                        play soundloop "fx/faucet1.ogg" fadein 1.0
                                        queue soundloop "fx/faucet2.ogg"
                                        m "我后退了一步，只让 Bryce 的顶端留在我的嘴里，预料到即将发生的事情，我继续吸吮。{w=0.5}Bryce 的嘴巴在极乐中张开，他的膀胱放松，将金色液体送入避孕套的储液囊。"
                                        m "我玩弄着口中膨胀的尿液气球，直到感觉安全为止，{w=0.5}{nw}"
                                        stop soundloop fadeout 6.0
                                        play sound "fx/water1.ogg"
                                        m "我玩弄着口中膨胀的尿液气球，直到感觉安全为止，{fast}然后让它在 Bryce 小便结束时，以淫荡的拍击声从我的嘴里掉到沙发的一侧Br flirty dk flip "有点太多了？"
                                        c "是的。但我有点预料到了。你比我大很多。"
                                Br smirk dk flip "我们可能需要一个新的避孕套。"
                                menu:
                                    "拿一个新的避孕套。":
                                        m "在脱下并系好他的尿液气球后，我回到柜子里拿了另一个避孕套，准备继续我们的口交。"
                                        m "当我回来时，他的阴茎头上依然有尿液的气味，直到我将新的橡胶安全套滚到上面。我还是把它放回嘴里，想象着可以舔和吸出更多的金色液体——即使那不安全。"
                                        $ renpy.pause(0.8)
                                        Br brow dk flip "我不认为只靠顶端能满足我。"
                                    "直接饮用他的精液。":
                                        $ bangok_four_bryce1_protected = False
                                        c "其实，算了。我改变主意了。"
                                        $ brycemood += 1
                                        Br smirk dk flip "哦？"
                                        m "我脱下并系好他的尿液气球，然后瞄准他的阴茎，把他的整个头部直接放入我没有保护的嘴里。"
                                        m "尿液的独特味道淹没了其他所有味道，但仍有几滴留在他的尿道里，我急切地吮吸出来。"
                                        Br flirty dk flip "如果这是你想要的。"
                                        show bryce stern dk flip with dissolve
                                        m "他用力，给我送来了更多的尿液。{w=0.5}我脸红了，想着地板旁的避孕套里还装着金色的液体。"
                                        menu:
                                            "喝他的尿。":
                                                m "Bryce皱起眉头，当我放弃他的阴茎时，直到他看到我在做什么。"
                                                Br flirty dk flip "你这么喜欢它吗？"
                                                m "他伸出一条后腿。我用一只爪子的爪子戳开在避孕套上的一个洞。然后我把它倒进我的嘴里。"
                                                show bryce smirk dk flip with dissolve
                                                play sound "fx/water2.ogg"
                                                if persistent.bangok_inflation == True:
                                                    queue sound "fx/gulpslow2.wav"
                                                    $ renpy.pause (9.0)
                                                    m "这是一个巨大的量。我不得不停下来休息一下。当我喝完后，我感觉被Bryce最近离开的温暖填满了。"
                                                else:
                                                    queue sound "fx/gulping.wav"
                                                    $ renpy.pause (3.0)
                                                    stop sound fadeout 1.0
                                                python:
                                                    brycemood += 1
                                                    bangok_four_bryce1_playerstuffed = True
                                                Br flirty dk flip "那真是激动人心的观看。"
                                                m "我擦了擦嘴，然后抓住他突出的阴茎。"
                                                c "还没完呢。"
                                                m "吸吮他的头部，我终于品尝到了他的第一滴甜甜的前液，与尿液的清洁剂形成了鲜明对比。"
                                                Br laugh dk flip "继续吧。"
                                            "继续下一个。":
                                                pass
                            else:
                                play soundloop "fx/faucet1.ogg" fadein 1.0
                                queue soundloop "fx/faucet2.ogg"
                                m "我尽量向前推，避免触发干呕反射，然后{i}吸{/i}。{w=0.5}Bryce 的嘴巴在极乐中张开，他的膀胱放松，将金色液体送入我的喉咙。"
                                m "几乎比我能吞下的还多，温暖的液体回流，覆盖了我的嘴巴，带来那独特的味道。我的身体变暖，Bryce 的热量直接转移到我的胃里。"
                                stop soundloop fadeout 5.0
                                m "不幸的是，所有美好的事物都有终结。他结束了，然后给了我一个满意的眨眼。"
                                Br flirty dk flip "可能从开始在警察局上班以来就没有小便过。希望你不介意。"
                                Br flirty dk flip "好了吗？"
                                m "我点了点头，仍在吮吸他的顶端，吸取最后的几滴。"
                                Br smirk dk flip "随意继续。"
                        "[[给他几秒钟。]]":
                            show bryce stern dk flip with dissolve
                            m "我停止了我的活动，等待他调整一下自己。"
                            $ renpy.pause(1.0)
                            Br flirty dk flip "好了，应该可以了。"
                elif bangok_four_bryce1_wstiming == "before":
                    Br flirty dk flip "我现在可以小便了吗？"
                    jump bangok_four_bryce1_oralbot_ws_before

            show bryce normal dk flip with dissolve
            m "我再次让嘴巴自由，深吸几口气，想着手该怎么做。"
            if bangok_four_bryce1_protected:
                m "我先积攒了一大口唾液，涂在避孕套的表面，然后从头部开始，一直将其涂满，缓解手指的滑动。"
            else:
                m "我先用前液和唾液的混合物从头部开始涂满，缓解手指的滑动。"
            m "然后我用拇指和食指形成了一个紧密的环，围住了他。"
            show bryce brow dk flip with dissolve
            if persistent.bangok_balls == True:
                m "我再次将他的头部放入嘴里，然后同时上下抽动我的手和嘴。每当我的手指到达他的根部时，我都会对他的睾丸进行挑逗、抚摸或按摩。"
            else:
                m "我再次将他的头部放入嘴里，然后同时上下抽动我的手和嘴。"
            show bryce laugh dk flip with dissolve
            m "Bryce 把头向后仰，陶醉于我给他的感觉中。"
            c "嗯。嗯嗯？"
            Br flirty dk flip "我不知道！不会太久！"
            if bangok_four_bryce1_protected:
                m "我继续我的活动，珍惜每一滴前液，尽量每次向下推动时都能多装一些在嘴里。"
            else:
                m "我继续我的活动，珍惜每一滴前液，尽量每次向下推动时都能多装一些在嘴里。"
            show bryce laugh dk flip with dissolve
            $ bangok_four_bryce1_brycecame = True
            play sound "fx/snarl.ogg"
            if bangok_four_bryce1_protected:
                if persistent.bangok_balls:
                    m "Bryce 的睾丸在我的手指下翻腾。然后他的第一次喷射突然让避孕套的顶部鼓起。我把他的顶端大部分从嘴里抽出来，只留一点点在里面，让储液囊有扩展的空间。"
                else:
                    m "Bryce 的第一次喷射突然让避孕套的顶部鼓起。我把他的顶端大部分从嘴里抽出来，只留一点点在里面，让储液囊有扩展的空间。"
                m "即便如此，这也是一个强大的负荷，越来越多的精液把避孕套压在我的舌头和口腔的顶部。"
                play sound "fx/uncork.ogg"
                if persistent.bangok_balls:
                    m "我把膨胀的储液囊从嘴里抽出来，一手握着他的阴茎头，一手继续抽动他，挤出最后的每一滴精液。"
                else:
                    m "我把膨胀的储液囊从嘴里抽出来，一手握着他的阴茎头，一手继续抽动他，挤出最后的每一滴精液。"
                m "最终 Bryce 结束了，瘫倒在背上。"
                Br flirty dk flip "该死...那真是另一个体验。"
                if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after":
                    $ brycemood -= 1
                    Br stern dk flip "哦。没想到单单是精液就会太多。"
                    c "我也没想到，但我不能直接吞下避孕套。"
                    Br laugh dk flip "确实！"
                    Br normal dk flip "脱掉它？我真的需要去小便。"
                    m "我把避孕套脱掉，立即闻到Bryce精液的味道，即使我系上了保护措施。"
                    menu:
                        "喝他的尿。":
                            c "啊，算了。"
                            m "我再次含住他的头部，抓住他的臀部，把它们尽可能地靠近自己，把他的顶端放在我的喉咙深处。仍然涂满精液的阴茎头尝起来出奇的甜。"
                            $ brycemood += 1
                            Br flirty dk flip "你确定吗？"
                            m "一股颤抖穿过他的身体，他皱了皱眉。"
                            Br laugh dk flip "现在已经晚了！"
                            play soundloop "fx/faucet1.ogg" fadein 1.0
                            queue soundloop "fx/faucet2.ogg"
                            m "温暖的金色液体涌入我的喉咙。我只能吞下它，因为 Bryce 把我的嘴当作他的尿壶。"
                            if persistent.bangok_inflation == True:
                                m "正常吞咽快速的流量是不可能的。它回流并洗去了我口中的精液味，取而代之的是尿液的味道。"
                                m "不想失去嘴唇周围的任何一滴，我把Bryce的阴茎头推进比我想象的还要深，部分进入我的喉咙，这样他可以直接将尿液送入我的胃里。"
                                $ bangok_four_bryce1_playerstuffed = True
                            else:
                                m "几乎不可能吞下那些流量。它回流并洗去了我口中的精液味，取而代之的是尿液的味道。"
                            jump bangok_four_bryce1_oralbot_afterpissend


                        "让他去。":
                            call bangok_four_bryce1_ws_emptying_the_tank(False)

                else:
                    m "我把避孕套脱掉，系好。"
            else:
                label bangok_four_bryce1_oralbot_cum:
                if persistent.bangok_balls:
                    m "当我抽出时，Bryce 的第一次喷射击中了我的喉咙后部，浸透了我的嘴巴，充满了浓厚的精液。"
                else:
                    m "当我抽出时，Bryce 的第一次喷射击中了我的喉咙后部，浸透了我的嘴巴，充满了浓厚的精液。"
                m "我立即改变方向，把接下来的几次喷射直接送入我的喉咙。"
                m "即便如此，这也是一个强大的负荷，越来越多的爱液从他的头部泄出，每次爆发都填满了我的嘴巴。"
                if persistent.bangok_inflation == True:
                    m "我感到头晕目眩，似乎无尽的精液几乎让我无法呼吸。"
                    if persistent.bangok_watersports == True and bangok_four_bryce1_playerstuffed == True:
                        m "毫无疑问，我在很长一段时间里都不需要吃喝了。我的肚子鼓起来，胃里和肠子里都装满了尿液和精液。"
                    else:
                        m "毫无疑问，我在很长一段时间里都不需要吃喝了。我的肚子微微鼓起，被一个更大的伙伴的精液填满。"
                $ bangok_four_bryce1_playerstuffed = True
                m "最终 Bryce 结束了，瘫倒在背上。"
                Br flirty dk flip "该死...那真是另一个体验。"
                if persistent.bangok_inflation == True:
                    m "我让他的阴茎从我的嘴里弹出，努力吞咽积聚在嘴巴每一个角落的浓稠精液。{w=0.5}然后，握住他的阴茎，我开始舔去我遗留在他顶端的部分。"
                else:
                    m "我让他的阴茎从我的嘴里弹出，吞咽积聚在嘴巴每一个角落的浓稠精液。{w=0.5}然后，握住他的阴茎，我开始舔去我遗留在他顶端的部分。"

                if persistent.bangok_knot == True:
                    m "当他射精时，他的阴茎底部出现了一个突起，这在激情之中我没有注意到。"
                    menu:
                        "[[挤压它。]]":
                            Br laugh dk "嘿！"
                            Br smirk dk "有点太早了，试图让我再次兴奋起来。"
                        "[[留着它。]]":
                            pass

                show bryce smirk dk flip with dissolve
                if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after":
                    c "有东西可以冲下这些吗？"
                    Br "有很多。"
                    m "我再次含住他的头部，抓住他的臀部，把它们尽可能地靠近自己，把他的顶端放在我的喉咙深处。"
                    Br "准备好了吗？"
                    $ renpy.pause(0.5)
                    show bryce laugh dk flip with dissolve
                    play soundloop "fx/faucet1.ogg" fadein 1.0
                    queue soundloop "fx/faucet2.ogg"
                    m "我欣赏的哼声被温暖的金色液体流打断了。我更加深地吞下他的阴茎，渴望被这条大龙用来做他的精液和尿液容器。"
                    if persistent.bangok_inflation == True:
                        m "正常吞咽快速的流量是不可能的，因为我的内脏已经装满了。他回流并洗去了我口中的精液味，取而代之的是尿液的味道。"
                        m "不想失去嘴唇周围的任何一滴，我把Bryce的阴茎头推进比我想象的还要深，部分进入我的喉咙，这样他可以直接将尿液送入我的胃里。"
                        m "随着液体的流动，我的腹部鼓起，液体在体内移动。"
                    else:
                        m "几乎不可能吞下那些流量。它回流并洗去了我口中的精液味，取而代之的是尿液的味道。"
                    label bangok_four_bryce1_oralbot_afterpissend:
                    stop soundloop fadeout 3.0
                    m "不幸的是，所有美好的事物都有终结。他结束了，然后给了我一个满意的眨眼。"
                    Br flirty dk flip "可能从开始在警察局上班以来就没有小便过。希望你不介意。"
                    Br flirty dk flip "好了吗？"
                    if persistent.bangok_inflation == True:
                        m "我点了点头，仍在吮吸他的顶端，吸取最后的几滴。"
                        m "一些尿液从我的嘴里流出，当我让他的阴茎离开我的嘴时，我试图用舌头清理它。"
                    else:
                        m "我点了点头，仍在吮吸他的顶端。"
                        m "Bryce 在我让他的阴茎离开我的嘴时，最后一滴尿液流过我的舌头。我试图吮吸他的顶端，只为了那一点点更多。"
                if persistent.bangok_inflation == True:
                    Br smirk dk flip "别这样。之后得洗个澡清洁一下。"
                    Br flirty dk flip "你可能需要的不止这些。"
                else:
                    Br smirk dk flip "别这样。之后得洗个澡清洁一下。你也可能需要。"
                m "当我完全释放他的阴茎时，它部分回到了他的身体里，只从裂缝中微微露出。"

            
            if not bangok_four_bryce1_playercame and not bangok_four_bryce1_protected and not (persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after"):
                play sound "fx/cartslide.ogg"
                show bryce normal dk at center with dissolve
                if persistent.bangok_inflation == True and bangok_four_bryce1_playerstuffed:
                    m "Bryce 从沙发上翻身下来，然后转身面对我。我艰难地从膝盖上站起来，增加的液体重量让我有点失衡。"
                    Br flirty dk "真的把你填满了，是吗？"
                    m "我拍了拍我的肚子。"
                else:
                    m "Bryce 从沙发上翻身下来，然后转身面对我。我从膝盖上站了起来。"
            
            if not bangok_four_bryce1_playercame:
                Br flirty dk "那是我。现在轮到你了。"
                menu:
                    "我...我想我完成了。":
                        Br brow dk "嗯？"
                        c "我...差不多满足了。我想我快要昏过去了。"
                        Br flirty dk "你确定
                c "差不多是这样。"
                        $ brycemood -= 1
                        Br normal dk "如果你这么说。"
                        pass
                    "想让我吸你吗？" if bangok_four_playerhasdick == True:
                        jump bangok_four_bryce1_m2_bsucc_merge
                    "我可以插你吗？" if bangok_four_playerhasdick == True:
                        jump bangok_four_bryce1_ptop
                    "吃我吗？" if bangok_four_playerhasdick == False:
                        jump bangok_four_bryce1_f_tonguefuck

            label bangok_four_bryce1_bothdone:
            Br normal dk "好吧，那是你那是我。"
            c "是的。"
            if brycemood < 0:
                Br brow dk "地板是开放的，如果你不能回家。"
                c "地板。地板不错。"
                Br "当然。"
                scene black with dissolveslow
                jump bangok_four_bryce1_morningfloor
            else:
                Br "那我睡地板吧。你可以睡沙发。"
                label bangok_four_bryce1_couchsleepchoice:
                menu:
                    "谢谢。":
                        pass
                    "你不必睡地板。":
                        Br brow dk "沙发并不是{我}那么{/i}宽敞，我想。"
                        c "我们可以分享。"
                        $ renpy.pause(0.9)
                        $ brycemood += 1
                        Br flirty dk "好吧。"
                scene black with dissolveslow
                jump bangok_four_bryce1_morningcouch


        "我想要你在我里面。":
            $ bangok_four_malepartners += 1
            label bangok_four_bryce1_analbot:
            call bangok_four_bryce1_position("analbot")
            if bangok_four_playerhasdick == True:
                Br brow dk "我们可以试试。但是，呃，在哪里？我看不到你的“睾丸”后面有什么东西。"
            elif persistent.bangok_cloacas == True:
                Br brow dk "我们可以试试。但是，呃，真的有区别吗？反正是进你的泄殖腔。"
                c "不完全是。人类没有那个。"
            else:
                Br normal dk "好吧。你的屁股在哪里？"
            c "它在更后面。这里。"
            scene bangok_four_bryce1_apartment night ceiling at Pan((0,360), (0,0), 2.0) with dissolve
            m "我躺在Bryce的沙发上，抬起腿，让他看得更清楚。"
            show bangok_four_bryce_underside_large dk flip at Position(yanchor='top',ypos=0.8) with dissolve
            Br "哦。原来是在这里。"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.6) with ease
            if bangok_four_playerhasdick == True or persistent.bangok_cloacas == True:
                Br flirty dk "没见过这个。"
            scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
            show bryce normal dk at Position(ypos=1.1)
            with dissolve
            m "Bryce 后退，让我坐起来，把润滑油递给我。"
            Br "如果你认为它能适应。但是肯定需要大量的这个。"
            c "对。"
            if persistent.bangok_watersports == True:
                call bangok_four_bryce1_ws_conversation from bangok_four_bryce1_analbot_ws_conversation
            if bangok_four_bryce1_protected == False and not bangok_four_bryce1_playercame:
                m "在我跪下开始将润滑油涂在他的阳具上之前，我昏昏沉沉的大脑提出了一个重要的想法。"
                c "哦，我几乎忘了保护措施。"
                Br stern dk "这真的有必要吗？"
                if bangok_four_bryce1_wstiming is not None:
                    Br smirk dk "我以为你想要我的体液在你体内。"
                    if bangok_four_playerhasdick == True:
                        Br brow dk "况且，我们都是男人。不会有孩子。"
                    else:
                        Br brow dk "况且，我们是不同的物种。不会有孩子。"
                else:
                    if bangok_four_playerhasdick == True:
                        Br "我们都是男人。不会有孩子。"
                    else:
                        Br "我们是不同的物种。不会有孩子。"
                Br brow dk "除非关于人类有我真的不理解的地方。"
                menu:
                    "[[坚持。]]":
                        $ brycemood -= 1
                        $ bangok_four_bryce1_protected = True
                        c "我们不知道你的体液对我会有什么影响。"
                        show bryce stern dk with dissolve
                        m "Bryce 哼了一声，然后指了指一个附近的抽屉柜。"
                        Br "顶层，我想。快点。"
                        label bangok_four_bryce1_analbot_fetchcondom:
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.wav"
                        if bangok_four_playerhasdick == True:
                            m "有几个不同品牌，上面有与Bryce比例相符的“实际尺寸”标记。我选择了一个，然后又深挖了一下，以防事情进一步发展。"
                            m "只在挖到最底层时，才终于找到一个更接近我尺寸的未开封的避孕套。"
                        else:
                            m "有几个不同品牌，上面有与Bryce比例相符的“实际尺寸”标记。我随机选了一个。"
                        m "撕开包装，我带着必要的装备回来了。"
                    "[[接受他的负荷。]]":
                        $ bangok_four_bryce1_protected = False
                        c "有道理。"
            elif bangok_four_bryce1_protected:
                menu:
                    "[[给他戴上避孕套。]]":
                        pass
                    "[[接受他的负荷。]]":
                        $ bangok_four_bryce1_protected = False
                        show bryce at center with ease
                        m "我跪在Bryce面前，沿着他令人印象深刻的长度涂上了大量润滑油。"
                        Br brow dk "润滑油应该涂在避孕套的外面。"
                        Br flirty dk "还是你改变主意了？"
                        c "嗯，最坏的情况会怎么样？况且，我想要你输出的东西。"
                        $ brycemood += 1
                        Br smirk dk "对我来说没问题。"
                        jump bangok_four_bryce1_analbot_luberub

            show bryce at center with ease
            if bangok_four_bryce1_protected == True:
                m "我跪在Bryce面前，将避孕套沿着他令人印象深刻的长度展开，然后涂上大量润滑油。"
            else:
                m "我跪在Bryce面前，沿着他令人印象深刻的长度涂上大量润滑油。"
            label bangok_four_bryce1_analbot_luberub:
            show bryce smirk dk with dissolve
            play soundloop "fx/massage.ogg"
            m "放下瓶子，我将润滑油涂抹在他的阳具周围，尽量确保每个地方都涂满，同时推一大块到顶端以帮助插入。"
            Br stern dk "该死，你的手真软。"
            stop soundloop fadeout 1.0
            c "这样应该可以了。"
            scene bangok_four_bryce1_apartment night ceiling at Pan((0,360), (0,0), 2.0) with dissolve
            m "预料到接下来会发生什么，我再次躺在Bryce的沙发上，把一条腿抬过靠背，尽可能分开另一条腿。"
            m "我仍然涂满润滑油的一只手，我揉搓我的肛门，既是挑逗也是为了帮助准备。"
            show bangok_four_bryce_underside_large dk at Position(yanchor='top',ypos=0.6) with easeinbottom
            $ renpy.pause(0.8)
            Br stern dk "你确定吗？"
            c "是的。"
            Br brow dk "如果有什么不对或疼痛，你会告诉我吗？"
            c "嗯哼。"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.6) with ease
            Br flirty dk "那就给我一秒钟来瞄准。"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
            m "Bryce 爬到我上面，后腿仍在地板上，他用前腿支撑在沙发上。他的腹部散发的热量传遍了我的裸露皮肤。"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
            if bangok_four_playerhasdick == True:
                m "冷冷的润滑油在他的阴茎顶端碰到我的大腿，然后轻拍我的睾丸，因为他试图找到我的肛门。"
            else:
                m "冷冷的润滑油在他的阴茎顶端碰到我的大腿，然后刺入我的阴道，因为他试图找到我的肛门。"
                menu:
                    "下边一点！":
                        pass
                    "[[什么都不说。]]":
                        Br laugh dk "在那里！"
                        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.8) with ease
                        m "他的顶端轻易地滑入我的阴道，刺穿了我，给我的双腿带来快感，使它们无力。"
                        Br brow dk "那...比我预期的要容易。"
                        Br "等等。"
                        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
                        Br stern dk "[player_name]，那是错误的地方，是吗？"
                        menu:
                            "继续那里。":
                                c "那...我想那一推改变了我的想法。"
                                jump bangok_four_bryce1_f_fuck_merge
                            "是的...":
                                $ brycemood -= 2
                                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
                                Br "我和你一样喜欢玩这个，但你需要和我说话，告诉我这些事情。"
                                c "抱歉。"
                                Br stern dk "下次注意。我不想因为你闭嘴不说而伤到你。"
                                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.7) with ease
                                m "他再次在我的腿间滑动，试图找到我的肛门，这次更加小心。即便如此，他很快又碰到了我的阴道口。"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.8) with ease
            Br stern dk "为什么这么难？"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.85) with ease
            m "顺着我的大腿内侧，他终于把他的硬阴茎嵌在我的会阴中。"
            c "接近了。"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
            if bangok_four_playerhasdick == True:
                m "他推动时，我尖叫了一声，那块细嫩的皮肤在我的睾丸和肛门之间向内压。"
            else:
                m "他推动时，我尖叫了一声，那块细嫩的皮肤在我的阴道和肛门之间向内压。"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.8) with ease
            Br brow dk "你还好吗？发生了什么？"
            c "再低一点。再低一点。"
            Br laugh dk "如果它这么小我找不到，我怎么能装进去？"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.85) with ease
            m "他又试了一次，他的阴茎顶端淫荡地弹离了我的一边。"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.82) with ease
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.9) with ease
            m "我抓住他，指导他剩下的那段短距离，直到他的顶端正好对着我的玫瑰花蕾。"
            Br smirk dk "准备好了吗？"
            $ renpy.pause (0.3)
            c "是的。"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.98) with ease
            m "我们涂上了大量润滑油，这是他能够进入的唯一方式。我的肛门张得大大的，几乎快疼了，因为他只插入了他的顶端。"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.0) with ease
            m "当我的环绕过他的头部，宽度稍微减小时，我喘了一口气。"
            m "Bryce 立刻停住了。"
            Br brow dk "有问题吗？"
            c "不，没问题。只是..."
            $ renpy.pause (1.2)
            Br flirty dk "想再多一点吗？"
            m "我点了点头，失去了语言。"
            show bangok_four_bryce_underside_large:
                ease 4.0 ypos (-2.2)
            $ renpy.pause (4.0)
            if bangok_four_playerhasdick == True:
                m "Bryce 以极大的小心向内推进，尽管我们都喝醉了。他腹部的鳞片划过我的阴茎，增加了体验的刺激。"
            else:
                m "Bryce 以极大的小心向内推进，尽管我们都喝醉了。他腹部的鳞片划过我的腹部，离我的前入口只有几厘米远，粗糙的刺激和即将到来的更多体验增加了感觉。"
            if persistent.bangok_balls:
                m "当温暖的鳞片在他的腿上压在我的皮肤上时，他的睾丸靠在我的臀部上，我试图进一步分开我的腿，让自己能更接近，完全接受他。"
            else:
                m "当温暖的鳞片在他的腿上压在我的皮肤上时，我试图进一步分开我的腿，让自己能更接近，完全接受他。"
            Br laugh dk "真紧！"
            c "你真大！"
            Br flirty dk "我经常听到这个。"
            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                if bangok_four_bryce1_protected == True:
                    m "突然，我感觉到肠子里有一种温暖的感觉，伴随着避孕套储液囊的膨胀，从我认为他的顶端的位置开始扩散。"
                else:
                    m "突然，我感觉到肠子里有一种温暖的感觉，从我认为他的顶端的位置开始扩散。"
                $ renpy.pause(0.5)
                Br laugh dk "啊...好了。"
                if bangok_four_bryce1_protected == True:
                    m "我稍微扭动了一下，这让 Bryce 用避孕套在我肛门里当尿壶的感觉更强烈。"
                else:
                    m "我稍微扭动了一下，这让 Bryce 用我的肛门当尿壶的感觉更强烈。"
                stop soundloop fadeout 1.5
                if persistent.bangok_inflation:
                    m "在他的阴茎和尿液之间，我感到被填满了。我有点不确定在这种情况下我们还能怎么做。"
                $ renpy.pause(0.8)
                Br flirty dk "可能从开始在警察局上班以来就没有小便过。希望你不介意。"
                $ renpy.pause(0.8)
                Br flirty dk "感觉怎么样？"
                c "嗯。"
                $ renpy.pause(1.0)
            Br smirk dk "现在的大小怎么样？"
            m "接近根部几乎和顶端一样宽，扩展我在他的爱的制造中。"
            if persistent.bangok_knot == True:
                m "我能感觉到在根部附近有一点额外的东西，因为我的括约肌在它周围痉挛。"
            menu:
                "[[不连贯的话。]]":
                    pass
                "好满...":
                    pass
                "喜欢。":
                    pass
                "我想我见过更大的。":
                    $ brycemood += 1
                    play sound "fx/tableslap.wav"
                    Br laugh dk "是吗？"
                    m "他的笑声通过我们身体接触的部位传递过来，在我的内脏中引起震动。"
                    Br smirk dk "那我猜你不会介意我们继续了。"
            show bangok_four_bryce_underside_large:
                ease 3.5 ypos (-2.05)
            m "Bryce 像进入时一样缓慢地往回抽动，保持润滑油均匀分布在他的阴茎和我的肛门上，没有感到任何明显的震动。"
            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                if bangok_four_bryce1_protected:
                    m "避孕套的膨胀储液囊随着我的内脏移动，液体在内部移动带来的感觉非常疯狂。"
                else:
                    m "尿液随着他的阴茎头回流，液体在内部流动带来的感觉增加了另一层刺激。"
            m "他停在他的顶端，等待。"
            menu:
                "慢一点。":
                    Br brow dk "我已经尽可能慢了。"
                    c "再来几个慢一点的。还在适应你。"
                    $ renpy.pause(0.3)
                    show bangok_four_bryce_underside_large:
                        ease 4.0 ypos (-2.2)
                        pause 0.5
                        ease 4.0 ypos (-2.05)
                        pause 0.3
                        repeat
                    m "Bryce 照我说的做了，给了我更多的满与空的循环。"
                    show bangok_four_bryce_underside_large:
                        ease 4.0 ypos (-2.2)
                    m "我在大阴茎上扭动，几乎失去了自我，直到他再一次停下来，最深处进入了我。"
                    label bangok_four_bryce1_analbot_adaptation:
                    Br smirk dk "感觉如何？"
                    menu:
                        "还在适应。":
                            $ renpy.pause(0.3)
                            show bangok_four_bryce_underside_large:
                                ease 3.5 ypos (-2.05)
                                ease 3.5 ypos (-2.2)
                                ease 3.5 ypos (-2.05)
                                ease 3.5 ypos (-2.2)
                            $ renpy.pause(14.0)
                            jump bangok_four_bryce1_analbot_adaptation
                        "{i}更多。{/i}":
                            pass
                    $ renpy.pause(0.5)
                    Br smirk dk "给我一秒。"
                    m "他没有加速，而是花了很长时间，将阴茎从我的深处慢慢地拖出来。"
                    show bangok_four_bryce_underside_large:
                        ease 5.0 ypos (-2.0)
                    $ renpy.pause (5.0)
                    if bangok_four_playerhasdick == True:
                        m "他这样做时，阴茎在内部抽搐，最终找到了我深处的那个愉快的按钮。"
                        show bangok_four_bryce1_apartment night ceiling at Pan((0,0), (0,30), 0.5)
                        show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.05)
                        with ease
                        m "我猛地摆动臀部，几乎让他的顶端从我体内滑出。"
                        Br flirty dk "所以这就是那个按钮。"
                    else:
                        m "他这样做时，阴茎在内部抽搐，发送出小波的快感。"
                        c "该死，别逗我！"
                        m "他没有停下，只是轻轻地将顶端抵在我的后入口。"
                    m "我欣赏地呻吟了一声。"
                    Br smirk dk "好吧。准备好了吗？"
                    $ renpy.pause(0.3)
                "哦，操我。":
                    $ brycemood += 1
                    show bangok_four_bryce1_apartment night ceiling at Pan((0,0), (0,30), 0.5)
                    show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.05)
                    with ease
                    if persistent.bangok_balls:
                        m "我把臀部向后推向他的阴茎，重新获得了一些他刚才取走的部分，并碰到了他的睾丸。"
                    else:
                        m "我把臀部向后推向他的阴茎，重新获得了一些他刚才取走的部分。"
                    Br flirty dk "如果你这么说。"

            play soundloop "fx/rub2.ogg" fadein 1.0
            show bangok_four_bryce_underside_large:
                ease 0.5 ypos (-2.15)
                ease 0.7 ypos (-2.1)
                repeat
            if persistent.bangok_balls:
                if persistent.bangok_inflation:
                    m "Bryce 开始真正地操我，滑进滑出，每次动作都把我扩展到极限，并用他的大而沉重的睾丸拍打我的臀部。"
                else:
                    m "Bryce 开始真正地操我，滑进滑出，每次动作都把我扩展到极限，并用他的睾丸拍打我的臀部。"
            else:
                m "Bryce 开始真正地操我，滑进滑出，每次动作都把我扩展到极限。"
            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                if bangok_four_bryce1_protected:
                    m "他的尿液气球被推入我肠道更深处，每次抽出时避孕套在内部淫荡地伸展。"
                else:
                    m "他的尿液被推入我肠道更深处，每次抽插时几乎可以听到湿润的声音。"
            $ renpy.pause(3.0)
            m "不过多久，我们俩就发出了不体面的声音。"
            $ renpy.pause(0.9)
            if persistent.bangok_knot == True:
                Br stern dk "在里面还是外面？"
                c "什-什么？"
                Br brow dk "结！在里面还是外面？"
                $ renpy.pause(0.5)
                menu:
                    "你有{i}结{/i}？！":
                        $ bangok_four_bryce1.knotpos = "inoops"
                    "在里面！":
                        $ brycemood += 1
                        $ bangok_four_bryce1.knotpos = "in"
                    "在外面！":
                        $ bangok_four_bryce1.knotpos = "out"
            else:
                Br stern dk "快了..."
            stop soundloop fadeout 1.0
            play sound "fx/snarl.ogg"
            show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-2.15) with ease
            if not persistent.bangok_knot or (persistent.bangok_knot and bangok_four_bryce1.knotpos != "out"):
                if persistent.bangok_balls:
                    if bangok_four_bryce1_protected == True:
                        m "Bryce 射了，他的睾丸在我的臀部拍打着，他的阴茎在我的内部爆发，将他的避孕套填满。"
                    else:
                        m "Bryce 射了，他的睾丸在我的臀部拍打着，他的阴茎在我的内部爆发，将我的内部涂满白色。"
                else:
                    if bangok_four_bryce1_protected == True:
                        m "Bryce 射了，他的阴茎在我的内部爆发，将他的避孕套填满。"
                    else:
                        m "Bryce 射了，他的阴茎在我的内部爆发，将我的内部涂满白色。"
            else:
                if bangok_four_bryce1_protected == True:
                    m "Bryce 射了，他的阴茎在我的内部爆发，离插到最深处还有几英寸的时候将避孕套填满。"
                else:
                    m "Bryce 射了，他的阴茎在我的内部爆发，离插到最深处还有几英寸的时候将我的内部涂满白色。"

            
            if bangok_four_playerhasdick == True:
                if not bangok_four_bryce1_playercame:
                    m "他阴茎的抽搐顶在我内部的愉快按钮上。在我能形成清晰的语言之前，我也达到了高潮，射在我们两个的胸膛上。"
                else:
                    m "他阴茎的抽搐顶在我内部的愉快按钮上，最近的高潮后过度刺激让我扭动不已。"
            else:
                if not bangok_four_bryce1_playercame:
                    m "我的肛门通道在他的阴茎周围痉挛，他的精液滚滚不断地填满我，加上他的大和粗暴的操弄，足以让我达到高潮。"
                else:
                    m "我的肛门通道在他的阴茎周围痉挛，他的精液滚滚不断地填满我，加上他的大和粗暴的操弄，再次让我达到高潮。"
                
            $ bangok_four_bryce1_playercame = True

            if persistent.bangok_inflation == True:
                m "即使我完成了，Bryce 还有几次喷射。"
                if bangok_four_bryce1_protected == True:
                    m "我惊恐地意识到，我感觉到避孕套在内部继续膨胀，把液体更深地推入我的肠道。"
                else:
                    m "我惊恐地意识到，我感觉{i}非常{/i}饱满。"
                    $ bangok_four_bryce1_playerstuffed = True
                c "Bryce！"
                Br flirty dk "几乎..."
                m "低头一看，我发现我的肚子比正常稍微大了一点。"

            $ renpy.pause(0.8)
            show bangok_four_bryce_underside_large:
                ease 1.0 ypos -2.0
                ease 1.0 ypos -1.7
                ease 1.0 ypos -1.3
                ease 1.0 ypos -0.7
            m "在长时间的内部射精后，Bryce 用前腿向后移动，同时保持臀部和阴茎的位置，向下看着我。"
            $ bangok_four_bryce1_brycecame = True

            if persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "before":
                if bangok_four_bryce1_protected == True:
                    play sound "fx/bubbles.ogg"
                    m "内部的堤坝决堤，Bryce 的精液负荷对避孕套来说实在是太多了。"
                    m "温暖的感觉充满了我的内部，液体在我的肠道内流动，达到平衡，不再受限制。"
                    $ bangok_four_bryce1_playerstuffed = True
            elif persistent.bangok_watersports == True and bangok_four_bryce1_wstiming == "after":
                Br flirty dk "准备好第二部分了吗？"
                if persistent.bangok_inflation == True:
                    c "呃。"
                else:
                    c "嗯嗯。"
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-1.5) with ease
                m "伴随着一声呻吟，Bryce 向前倾身，然后他的阴茎在我内部再次抽搐。一种新的，粘性较小的温暖开始在我的内脏中扩散。"
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                Br laugh dk "啊..."
                if persistent.bangok_inflation == True:
                    if bangok_four_bryce1_protected == True:
                        play sound "fx/bubbles.ogg"
                        m "内部的堤坝决堤，Bryce 的额外尿液负荷对避孕套来说实在是太多了。"
                        $ bangok_four_bryce1_playerstuffed = True
                    m "我呻吟着，感觉到液体在我的内脏中冒泡和流动，为更多液体腾出空间。"
                    
                    stop soundloop fadeout 1.5
                    if bangok_four_bryce1_protected == True:
                        m "当他用我的内脏作为尿壶时，我的肚子紧贴着他的，明显因Bryce的精液和尿液而鼓起。"
                    else:
                        m "当他用我的内脏作为尿壶时，我的肚子紧贴着他的，明显因Bryce的精液和尿液而鼓起。"
                else:
                    if bangok_four_bryce1_protected == True:
                        m "我躺着，呼吸平稳下来，满足于Bryce用避孕套在我内脏中当尿壶的感觉。"
                    else:
                        m "我躺着，呼吸平稳下来，满足于Bryce用我的内脏作为尿壶的感觉。"
                stop soundloop fadeout 1.5
                m "当他回到我的眼前时，我几乎能听到所有液体在我体内的流动声。"
                show bangok_four_bryce_underside_large at Position(yanchor='top',ypos=-0.7) with ease
                Br flirty dk "可能从开始在警察局上班以来就没有小便过。希望你不介意。"

            if persistent.bangok_inflation == True:
                m "他用爪子揉搓我的突出的肚子。"
                Br flirty dk "真的把你填满了，是吗？"
                m "我无法回答，只是躺在那儿，享受着我们交合后留下的温暖液体。"

            
            if persistent.bangok_watersports and persistent.bangok_inflation and bangok_four_bryce1_protected:
                $ brycemood += 1
                Br flirty dk "嗯。我想避孕套破了。"
                menu:
                    "显然！":
                        $ brycemood -= 2
                        Br "我无法控制它的完整性。"
                        c "不尿在里面可能会保存它。"
                        Br "谁说他们同意了？"
                    "该死。":
                        Br "是的，抱歉。"
                        Br flirty dk "不过真是一次美好的XX。"
                        m "我点了点头。"
                    "那感觉真不错...":
                        Br "是吗？"
            else:
                Br flirty dk "感觉好吗？"
                m "我点了点头。"
            # menu:
            #     "[[点头。]]":
            #         pass
            #     ""
            #     "太多了。" if persistent.bangok_inflation:
            #         $ brycemood -= 1
            #         Br flirty dk "你知道你自己在做什么。"
            if persistent.bangok_knot == True and bangok_four_bryce1.knotpos != "out":
                Br flirty dk "希望你喜欢，因为我不认为你的肛门会这么快让结出来。"
                if bangok_four_bryce1.knotpos == "inoops":
                    $ brycemood -= 1
                    c "什么？！"
                    scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
                    show bryce brow dk
                    with dissolvemed
                    play sound "fx/sheet.wav"
                    m "他向后退，给我空间让我用肘部撑起来。"
                    $ renpy.pause(0.5)
                    Br "我没有太多时间或空间来思考，你也不够清楚。"
                    menu:
                        "我甚至不知道你有结！":
                            $ brycemood -= 1
                            Br stern dk "你和另一个物种互动，却没想到要检查一下这种基本事实？"
                        "你应该把它留在外面的！":
                            $ brycemood -= 2
                        "没关系。":
                            $ brycemood += 1
                            c "这是个误会。作为误会来说，还有更糟的。"
                            Br normal dk "现在也没什么好做的了。我们不如睡一觉。"
                            jump bangok_four_bryce1_tiedsleep
                    Br stern dk "现在也没什么好做的了。我们不如睡一觉。"
                    
                    if persistent.bangok_watersports == True:
                        c "那对你来说很容易说，没有一整个屁股被龙的精液、尿液和阴茎塞满。"
                    else:
                        c "那对你来说很容易说，没有一整个屁股被龙的阴茎和精液塞满。"

            
                label bangok_four_bryce1_tiedsleep:
                scene black with dissolveslow
                m "Bryce 在沙发上趴在我身上，无法做更多的事情，因为我们的臀部绑在一起。"
                if brycemood >= 0:
                    Br "晚安，[player_name]。"
                else:
                    Br stern dk "我希望我们不必这样睡觉，和你一样。"
                    c "去你的。"
                    Br "你已经这样了。"
                jump bangok_four_bryce1_morningcouch
            else:
                if brycemood < 0:
                    jump bangok_four_bryce1_analbot_pullout
                else:
                    Br "你想让我拔出来吗？还是想这样睡觉？"
                    menu:
                        "这样睡。":
                            $ brycemood += 1
                            scene black with dissolveslow
                            m "Bryce 趴在我身上，在沙发上小心地挪动我到边缘，这样他不会压着我。"
                            if persistent.bangok_knot == True:
                                m "他调整了臀部，把结压在我的臀部上，以防漏出来。"
                            Br smirk dk "晚安，[player_name]。"
                            jump bangok_four_bryce1_morningcouch
                        "拔出来。":
                            label bangok_four_bryce1_analbot_pullout:
                            scene bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
                            show bryce stern dk
                            with dissolvemed
                            if (persistent.bangok_watersports and persistent.bangok_inflation and bangok_four_bryce1_protected) or not bangok_four_bryce1_protected:
                                # 破裂的避孕套或没有避孕套
                                play sound ["fx/slide.ogg","fx/spray.ogg"] fadein 0.5
                                m "Bryce 把自己拉出来，一小股我们性爱的液体滴在他的沙发边上。"
                                # if persistent.bangok_rimming == True:
                                #     Br "介意我尝尝我们的结果吗？"
                                #     c "怎么尝？"
                                #     Br "你见过我的舌头。自己想吧。"
                                #     c "好吧。"
                            elif persistent.bangok_inflation:
                                # 完整的避孕套
                                play sound "fx/slide.ogg" fadein 0.5
                                m "Bryce 拉，但不能把避孕套膨胀的储液囊从我的肠道里拖出来。"
                                Br stern dk "该死。又是那个大小差异。"
                                c "也许我要推一下？"
                                Br brow dk "让我先把避孕套多拉出来一点。"
                                play sound "fx/pour.ogg"
                                $ renpy.pause(3.0)
                                m "我能感觉到液体从避孕套里从我的肠道排出来，通过我扩张的肛门进入外部部分。"
                                play sound "fx/uncork.ogg"
                                m "最后一点随着一股空气的冲出，离开了我的肠道，感觉变得空虚。"
                            else:
                                # 普通使用过的避孕套
                                play sound ["fx/slide.ogg","fx/uncork.ogg"] fadein 0.5
                                if persistent.bangok_watersports:
                                    m "Bryce 拉出自己，避孕套储液囊里的精液和尿液以满足的声音弹出。"
                                else:
                                    m "Bryce 拉出自己，避孕套储液囊里的精液以满足的声音弹出。"
                    if brycemood < 0:
                        Br stern dk "地板是开放的。或者你可以像这样回家。"
                        m "我挣扎着从沙发上起身，我的臀部每次移动都在大声抱怨。"
                        c "地板不错…"
                        play sound "fx/impact3.ogg"
                        scene black with vpunch
                        jump bangok_four_bryce1_morningfloor
                    else:
                        Br normal dk "你想继续留在沙发上吗？"
                        m "我点点头。"
                        c "我不确定在那之后还能不能动。该死。"
                        Br flirty dk "好吧，我也快熬不住了。"
                        scene black with dissolveslow
                        Br "晚安，[player_name]。"
                        c "晚安。"
                        jump bangok_four_bryce1_morningcouch

        "我想插你。":
            $ bangok_four_malepartners += 1
            label bangok_four_bryce1_ptop:
            call bangok_four_bryce1_position("ptop")
            Br flirty dk "对我来说没问题。"
            play sound "fx/cartslide.ogg"
            show bryce normal dk at Position(xpos=0.4,xanchor='center') with ease
            show bryce at Position(xpos=0.45,xanchor='center',ypos=1.05) with ease
            m "Bryce 靠在沙发上，卷起地毯并拉动咖啡桌，他的尾巴在一刻抓住了。"
            m "他分开了后腿，眨眼示意。"
            Br flirty dk "你还在等什么？"
            m "我的昏昏沉沉的大脑在跟随他时，推了几个想法。"
            if bangok_four_bryce1_protected_a:
                menu:
                    "[[戴上避孕套。]]":
                        $ bangok_four_bryce1_protected = True
                    "[[不戴套。]]":
                        $ bangok_four_bryce1_protected = False
                c "干吗？"
                m "我在黑暗中眯起眼睛，完全错过了他的阳具底下的任何地方。"
                c "还有，呃，在哪里？"
            else:
                c "干吗？没有保护吗？"
                m "我在黑暗中眯起眼睛，完全错过了他的阳具底下的任何地方。"
                c "还有，呃，在哪里？"
                m "在问到保护措施时，他笑得有些歪。"
                Br flirty dk "来吧。我们都是男人。不会有孩子。"
                menu:
                    "[[坚持。]]":
                        c "不。没有保护不行。"
                        if chapter2unplayed == False and chapter2storeunplayed == False and chap2storehealth == False:
                            c "我见过健康区。你们有避孕套。"
                        else:
                            c "你们的种族有避孕套，对吗？"
                        $ brycemood -= 1
                        show bryce stern dk with dissolve
                        m "Bryce 哼了一声，然后指了指角落里的一个抽屉柜。"
                        Br "顶层。我想。快点。"
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.wav"
                        m "有几个不同品牌，上面有与Bryce比例相符的“实际尺寸”标记。只有在挖到最底层时，才终于找到一个更接近我尺寸的未开封的避孕套。"
                        m "撕开包装，我带着必要的装备回来了。"
                    "[[不戴套。]]":
                        $ bangok_four_bryce1_protected = False
                        c "好吧。在哪里？"
            m "Bryce 转过头去看沙发后面，又用嘴叼起一瓶润滑油。"
            show bryce stern dk with dissolve
            if persistent.bangok_balls == True:
                if persistent.bangok_cloacas == True:
                    m "他费力地向前弯下身子，把瓶子放在他的睾丸下，然后按压柱塞，把一团润滑油直接挤进睾丸下面的裂缝。"
                else:
                    m "他费力地向前弯下身子，把瓶子放在他的睾丸下，然后按压柱塞，把一团润滑油挤在睾丸出来的裂缝下面两片板之间。"
            else:
                if persistent.bangok_cloacas == True:
                    m "他费力地向前弯下身子，把瓶子放在他的阴茎上，然后按压柱塞，把一团润滑油挤在阴茎出来的裂缝底部。"
                else:
                    m "他费力地向前弯下身子，把瓶子放在他的阴茎上，然后按压柱塞，把一团润滑油挤在阴茎出来的裂缝下面两片板之间。"
            play sound "fx/box.wav"
            m "他把瓶子扔在咖啡桌上。"
            Br smirk dk "好了。还有问题吗？"
            if persistent.bangok_balls == True:
                m "我用跨坐在他的尾巴，支撑在他的后腿上，然后再次决定到底该把我的阳具插在哪里。"
            else:
                m "我用跨坐在他的尾巴，支撑在他的后腿上，然后试探性地在他指示的阴茎下挖了一下。"
                m "我错过了。"
                Br brow dk "再低一点。那个地方是我的拔出来的地方。"
            menu:
                "插入他。":
                    if not bangok_four_bryce1_brycecame:
                        m "我插入他的阴茎旁边，试探性地探索他的生殖裂缝。Bryce 有点扭动。"
                        $ brycemood -= 1
                        if persistent.bangok_balls == True:
                            Br stern dk "错边了。再低一点。"
                        else:
                            Br stern dk "我{i}刚说过{/i}什么？"
                        c "呃。"
                        menu:
                            "[[继续插入。]]":
                                $ brycemood -= 1
                                play sound "fx/impact3.ogg"
                                show bryce at center
                                show bangok_four_bryce1_apartment night at Pan((0,0), (0,0), 0.0)
                                with vpunch
                                m "我摔倒在地，Bryce 的一脚踢得我呼吸急促，头晕目眩。"
                                Br brow dk "这不是单向的。你想进来，你得{i}听{/i}我的。"
                                Br brow dk "瞄准低一点，好吗？我太激动了。"
                                play sound "fx/cartslide.ogg"
                                show bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 2.0)
                                show bryce normal dk at Position(xpos=0.45,xanchor='center',ypos=1.05)
                                with ease
                                m "Bryce 再次躺回沙发上，给我分开腿再一次尝试。"
                                menu:
                                    "[[干他。]]":
                                        pass
                                    "[[再插入。]]":
                                        play sound "fx/impact3.ogg"
                                        with vpunch
                                        scene black with fade
                                        jump bangok_four_bryce1_badmorning
                            "[[听他的话。]]":
                                pass
                    else:
                        if persistent.bangok_balls == True:
                            m "我插入他的阴茎旁边，试探性地探索他的生殖裂缝。Bryce 有点扭动。"
                            Br stern dk "错边了。再低一点。"
                        else:
                            m "我插入他的阴茎旁边，试探性地探索他的生殖裂缝。Bryce 有点扭动。"
                            Br stern dk "还是错了。"
                        if brycemood < 2:
                            c "如果我想干你的生殖裂缝呢？"
                            if brycemood < 0:
                                play sound "fx/impact3.ogg"
                                show bangok_four_bryce1_apartment night at Pan((0,0), (0,0), 0.0)
                                with vpunch
                                m "Bryce 用一条腿把我推开。"
                                Br "那我们可以叫这次行为结束了。"
                                show bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 2.0)
                                with ease
                                m "我爬起来。"
                                c "嘿！我不是白给你口交的！"
                                Br "你也没干得很好。"
                                m "我向 Bryce 仍然暴露的后腿前进。"
                                play sound "fx/impact3.ogg"
                                with vpunch
                                scene black with fade
                                jump bangok_four_bryce1_badmorning
                            else:
                                $ renpy.pause (1.2)
                                Br "好吧。"
                        else:
                            c "人类没有这些裂缝。我猜我只是很好奇，干一个是什么感觉。"
                            c "我可以吗？"
                            $ renpy.pause (0.8)
                            Br "好吧。"
                        if not bangok_four_bryce1_protected:
                            Br brow dk "但不要{i}在里面{/i}射。那里清理起来太麻烦了，还容易感染。"
                            c "所以拔出来？"
                            Br stern dk "插进我的屁股。这才是我预期的。"

                        m "慢慢来，我把自己插入 Bryce 的生殖裂缝，靠近他的阴茎。"
                        m "他是对的。即使缩回到体内，他的阴茎仍然硬得像扩展时一样。柔软、温暖的墙壁从每个方向压在我的阴茎上，除了他阴茎坚硬、圆润的表面，这种感觉与我以前经历的任何事情都不同。"
                        m "更何况，他的阴茎和生殖裂缝都{i}紧紧的{/i}，夹住我的阴茎，他每次抽动都在抽搐。"
                        m "当我到达底部时，他的顶端戳进我的骨盆，Bryce 终于松了一口气。"
                        Br normal dk "好吧。你可以加快速度了。"
                        m "我先小心翼翼地做了几次慢抽，寻找最适合干他的角度，这样不会伤到他的阴茎和我的。"
                        play soundloop "fx/rub2.ogg" fadein 3.0
                        m "然后我开始抽插，进入和退出这个紧凑、湿润的洞。"
                        Br smirk dk "这就是你想要的吗？"
                        m "我无法回答，过于沉浸在被他的抽搐阴茎和每次抽插时他生殖裂缝的墙壁夹住的感觉中。"
                        $ renpy.pause (0.8)
                        show bryce stern dk with dissolve
                        m "他的笑容在我滑到他阴茎的一侧时变成了皱眉，他的顶端戳进我的骨盆而不是睾丸。"
                        Br "你还差多远？"
                        m "答案是很近，近得我不得不开始考虑即将发生的事情。"
                        if bangok_four_bryce1_protected:
                            m "避孕套有足够的空间来射吗？还是会导致精液外溢？"
                        menu:
                            "[[拔出来。]]":
                                stop soundloop fadeout 0.5
                                m "拔出来的动作，加上房间的寒冷空气，把我推到了顶点。"
                                menu:
                                    "屁股。":
                                        jump bangok_four_bryce1_ptop_asscum
                                    "外面。":
                                        play sound "fx/extinguish.ogg"
                                        show bryce brow dk
                                        show black
                                        with dissolve
                                        if bangok_four_bryce1_protected:
                                            m "我稳住自己，把负荷放进避孕套的储液囊，挂在Bryce 的后腿上。"
                                            $ brycemood += 1
                                            if persistent.bangok_watersports == True:
                                                play soundloop "fx/faucet1.ogg" fadein 1.0
                                                queue soundloop "fx/faucet2.ogg"
                                                m "过了一会儿，我意识到更多的液体从我体内流出，进一步膨胀了避孕套。"
                                                c "呃。"
                                                m "我的脸颊因为尴尬而涨红。"
                                                stop soundloop fadeout 1.5
                                                show bryce laugh dk with dissolve
                                                m "Bryce 用爪子弹了弹充满的避孕套储液囊。"
                                                Br "喝太多了？"
                                                show bryce smirk dk with dissolve
                                                Br "我经常和喝酒的伙伴睡觉。这种情况经常发生。"
                                                Br flirty dk "不过，避孕套确实不错。"
                                            else:
                                                label bangok_four_bryce1_ptop_protectedslitcum:
                                                m "Bryce 用爪子弹了弹充满的避孕套储液囊。"
                                                Br flirty dk "好吧。还好有避孕套，省了很多清理工作。"
                                                c "谢谢。"
                                            m "爬下 Bryce，我脱下并系好避孕套，然后沉重地坐下。"
                                        else:
                                            m "我没有时间找到他的屁股。我射了，薄薄的绳索喷在他的后腿和胸膛上。"
                                            hide black with dissolvemed
                                            if persistent.bangok_watersports == True:
                                                play soundloop "fx/faucet1.ogg" fadein 1.0
                                                queue soundloop "fx/faucet2.ogg"
                                                m "过了一会儿，我意识到更多的液体从我体内流出，顺着 Bryce 的腹部板流下。"
                                                c "呃。"
                                                m "我的脸颊因为尴尬而涨红。"
                                                stop soundloop fadeout 1.5
                                                if bangok_four_bryce1_wstiming not in ["before","after"]:
                                                    $ brycemood -= 1
                                                    Br stern dk "..."
                                                $ brycemood -= 1
                                                Br "没想到今天会遇到黄金浴。"
                                            else:
                                                Br "没想到今天要清理这么多。"
                                            Br laugh dk "我猜该做的都做了。"
                                            Br normal dk "我们都得睡地板了。"
                                            show bryce normal dk flip at center with dissolve
                                            m "Bryce 从沙发上翻身下来，当我坐下时，我感到头晕目眩，因为与大龙的性交
                                                                                        m "导致的疲惫。"
                                        Br brow dk "不，不要。我睡地板。"
                                        jump bangok_four_bryce1_couchsleepchoice
                                    "再进去。":
                                        jump bangok_four_bryce1_docking_inside
                            "[[射在里面。]]":
                                label bangok_four_bryce1_docking_inside:
                                stop soundloop fadeout 0.5
                                play sound "fx/extinguish.ogg"
                                if bangok_four_bryce1_protected:
                                    show bryce smirk dk
                                else:
                                    show bryce angry dk
                                show black
                                with dissolve
                                m "我深深地推入，射了出来，夹在Bryce的巨大的阴茎和他的生殖裂缝的墙壁之间。"
                                if bangok_four_bryce1_protected:
                                    hide black with dissolvemed
                                    $ renpy.pause(0.3)
                                    if persistent.bangok_watersports == True:
                                        play soundloop "fx/faucet1.ogg" fadein 1.0
                                        queue soundloop "fx/faucet2.ogg"
                                        show bryce brow dk with dissolve
                                        m "过了一会儿，我意识到更多的液体从我体内流出，膨胀了避孕套并填满了他紧凑的内部空间。"
                                        c "呃。"
                                        m "我的脸颊因为尴尬而涨红。"
                                        Br stern dk "太紧了。拔出来！"
                                        menu:
                                            "等一下...":
                                                m "射完后的尿液在他紧凑的空间里是种极乐，我不想错过体验的每一滴。"
                                                stop soundloop fadeout 1.0
                                                play sound "fx/bubbles.ogg"
                                                m "...直到某些东西给了。"
                                                show bryce stern dk with dissolve
                                                Br "[player_name]！"
                                                play sound "fx/stones.ogg"
                                                m "我拔出来，但损害已经造成。精液和尿液的团块沿着从避孕套脱出的裂缝流下，滴入我在他生殖裂缝中制造的混乱。"
                                                show bryce stern dk with dissolve
                                                m "尽管他的阴茎再次探出——他被这个体验激发了——他的脸上却显示出冷冷的愤怒。"
                                                jump bangok_four_bryce1_ptop_unprotectedslitcum
                                            "[[拔出来！]]":
                                                stop soundloop fadeout 1.5
                                                m "我拔出了充满液体的避孕套，它在 Bryce 的后腿上淫荡地晃动。"
                                                jump bangok_four_bryce1_ptop_protectedslitcum
                                else:
                                    hide black with dissolvemed
                                    show bryce stern dk with dissolve
                                    $ renpy.pause(0.3)
                                    if persistent.bangok_watersports == True:
                                        play soundloop "fx/faucet1.ogg" fadein 1.0
                                        queue soundloop "fx/faucet2.ogg"
                                        $ renpy.pause (0.5)
                                        m "过了一会儿，我意识到更多的液体从我体内流出，填满了他紧凑的内部空间。"
                                        c "呃。"
                                        stop soundloop fadeout 1.5
                                        m "我在他里面尿完了，猜测这可能不会让事情变得更糟。"
                                        $ renpy.pause (0.5)
                                    play sound "fx/stones.ogg"
                                    m "当我拔出来时，我的阴茎上滴下我在他生殖裂缝中制造的混乱。"
                                    m "尽管他的阴茎再次探出——他被这个体验激发了——他的脸上却显示出冷冷的愤怒。"
                                    label bangok_four_bryce1_ptop_unprotectedslitcum:
                                    $ renpy.pause (0.5)
                                    m "Bryce 用一条腿把我推开，在我还没来得及找借口之前，我已经被他的尾巴绊倒，重重摔在地上。"
                                    play sound "fx/impact3.ogg"
                                    show bangok_four_bryce1_apartment night at Pan((0,0), (0,0), 0.0)
                                    with vpunch
                                    jump bangok_four_bryce1_badmorning

                "[[干他。]]":
                    pass
            show bryce flirty dk with dissolve
            if bangok_four_bryce1_protected == True:
                m "随着润滑油在避孕套上进一步扩散，他的一块硬腹板在我的阴茎下磨擦。然后一切都变成了温暖的包裹，当我尽可能深地进入他时。"
            else:
                m "随着润滑油在我的阴茎上进一步扩散，他的一块硬腹板在我的阴茎下磨擦。然后一切都变成了温暖的包裹，当我尽可能深地进入他时。"
            if persistent.bangok_balls == True:
                m "当他的睾丸在他的阴茎周围滚动，戳到我的躯干时，他淫荡地笑了。"
            else:
                m "当他的阴茎在我的躯干上摩擦时，他淫荡地笑了。"
            Br "那是那个点，对吗？"
            m "我点点头，失去了言语能力。"
            Br smirk dk "好吧，玩得开心吧。"
            m "我慢慢拔出来，开始试探性地抽动，注意Bryce的脸，以确保我没有让他感到不适。"
            play soundloop "fx/rub2.ogg" fadein 3.0
            show bryce flirty dk with dissolve
            m "这似乎对他没有任何影响。他向我挑逗地眨了眨眼，当我加快速度时。"
            m "在他坚硬的板块下，他的内部组织是柔软和温暖的。对我阴茎的压力很轻，更多的是他外括约肌的紧密度而非内部解剖的紧密度。"
            m "当然，我不仅仅是为了自己。虽然很难形成一个完整的想法，除了下一次抽插，我还是拼凑了一些话。"
            c "你有感觉吗？"
            Br laugh dk "有点！"
            if not bangok_four_bryce1_brycecame:
                Br smirk dk "如果你在问能不能让我高潮，这样是做不到的。"
                m "把这当作一种挑战，我把一只手从支撑他的腿移到夹在他的阴茎和我的腹部之间。"
                play sound "fx/buck.ogg"
                show bryce stern dk with dissolve
                m "Bryce 把臀部顶向我的，显然被这个动作吓了一跳。"
                Br flirty dk "该死。这是个好技巧！"
                m "我没有回应，他的顶回让我接近高潮。"
            else:
                Br flirty dk "如果你在问是否会疼，那完全不会。"
                if persistent.bangok_balls == True:
                    m "我把这当作进一步的鼓励，向前倾，同时把他的睾丸推到一边，开始干他。"
                else:
                    m "我把这当作进一步的鼓励，向前倾，开始干他。"
                Br laugh dk "现在我几乎感觉到了！"
            stop soundloop fadeout 0.5
            $ renpy.pause(0.5)
            show bryce smirk dk with dissolve
            play sound "fx/rub1.ogg"
            $ renpy.pause(1.5)
            label bangok_four_bryce1_ptop_asscum:
            play sound "fx/extinguish.ogg"
            show black with dissolve
            if bangok_four_bryce1_protected == True:
                m "我达到了高潮，把负荷放在避孕套的储液囊里，深埋在Bryce的屁股里。"
            else:
                m "我达到了高潮，把负荷尽可能深地放在Bryce的屁股里。"
            $ bangok_four_bryce1_playercame = True
            hide black with dissolvemed

            if persistent.bangok_watersports == True:
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                show bryce brow dk with dissolve
                m "过了一会儿，我意识到更多的液体从我体内流出。"
                c "呃。"
                Br laugh dk "喝太多了？"
                m "我的脸颊因为尴尬而涨红。"
                stop soundloop fadeout 1.5
                Br smirk dk "我经常和喝酒的伙伴睡觉。你不是第一个在我里面尿尿的。"

            if bangok_four_bryce1_protected == True:
                m "他移动臀部，我身体的液体输出在避孕套的头部淫荡地流动。"
            else:
                m "他移动臀部，我身体的液体输出在他屁股里淫荡地流动。"

            if bangok_four_bryce1_brycecame:
                if brycemood > 0:
                    show bryce flirty dk with dissolve
                else:
                    show bryce brow dk with dissolve
                m "我拔出来，晚上性爱的疲劳终于赶上了我。"
                play sound "fx/cartslide.ogg"
                show bryce at center with ease
                m "Bryce 从沙发上翻身下来。"
                jump bangok_four_bryce1_bothdone
            else:
                Br flirty dk "那是你。现在轮到我了。"
                
                if bangok_four_bryce1_protected == True:
                    m "我先拔出来，考虑我的选项，然后脱下并系好避孕套。我的头脑更清醒了，但我也感到因为性交所消耗的精力而头晕。"
                else:
                    m "我先拔出来，考虑我的选项。我的头脑更清醒了，但我也感到因为性交所消耗的精力而头晕。"
                label bangok_four_bryce1_preciprocity_menu:
                menu:
                    "我...我想我完成了。":
                        Br brow dk "什么？"
                        c "我..."
                        $ renpy.pause (0.8)
                        c "我想我要晕过去了。"
                        Br stern dk "嘿！"
                        scene black with fade
                        play sound "fx/impact3.ogg"
                        jump bangok_four_bryce1_badmorning
                    "想干我吗？":
                        jump bangok_four_bryce1_analbot
                    "我可以吸你。":
                        jump bangok_four_bryce1_oralbot
                    "手淫可以吗？":
                        label bangok_four_bryce1_hand:
                        call bangok_four_bryce1_position("hand")
                        show bryce brow dk with dissolve
                        c "我只是...你有点大。"
                        Br "当然。如果你觉得这样安全，手淫没问题。"
                        if bangok_four_bryce1_protected == True:
                            Br "介意给我戴上你拿的避孕套吗？"
                            Br laugh dk "显然我的爪子不好用。"
                            Br normal dk "我也不想再清理更多的污渍了。"
                            c "当然。"
                        else:
                            Br normal dk "介意给我拿个避孕套吗？我不想再清理更多的污渍了。"
                            c "当然。在哪里？"
                            Br "抽屉，那边。顶层，我想。"
                            $ renpy.pause(0.3)
                            play sound "fx/rummage.wav"
                            $ renpy.pause(2.0)
                            stop sound fadeout 1.0
                            m "找避孕套并不难。我带回了一个他尺寸的，大多数盒子都是这种。"
                        call bangok_four_bryce1_setprotected(True)
                        if persistent.bangok_balls == True:
                            m "坐在他下面，我沿着他的长度展开了避孕套，一直到他的睾丸。"
                        else:
                            m "坐在他下面，我沿着他的长度展开了避孕套。"
                        Br smirk dk "好了，开始吧。"
                        m "我轻轻地握住Bryce的阴茎，靠近底部。我不太确定跟不同物种如何能多粗鲁。"
                        Br laugh dk "嘿！不要{i}挠{/i}它！"
                        m "我收紧了握力，试探性地上下抽动了一下，然后松开，看向他头部寻求认可。"
                        Br flirty dk "更好。"
                        play soundloop "fx/massage.ogg" fadein 8.0
                        m "再次抓住他，我继续抽动，润滑的避孕套表面发出声响，直到Bryce告诉我停下。"
                        show bryce laugh dk with dissolve
                        m "他没有，只是张开嘴，陶醉在我手中。"
                        m "他甚至顶着我的手，稍微干着我的手指，享受我给予他的感觉。"
                        if persistent.bangok_watersports == True:
                            $ renpy.pause(0.8)
                            Br "啊该死。"
                            stop soundloop fadeout 4.0
                            m "我大幅放松了握力。"
                            c "怎么了？"
                            Br stern dk "我要小便了。"
                            label bangok_four_bryce1_handjob_wsmenu:
                            menu:
                                "让我先把避孕套取下来，这样你可以去厕所。":
                                    stop soundloop fadeout 0.5
                                    m "从顶端和环处取下避孕套，我让Bryce去洗手间。"
                                    m "当他走开时，我有了另一个想法。"
                                    call bangok_four_bryce1_ws_emptying_the_tank(False,False)
                                "如果是在避孕套里...":
                                    Br "马上就会在里面。"
                                    m "我放手了。Bryce 颤抖了一下，然后他的阴茎抽搐着，将液体负荷释放到避孕套中。"
                                    label bangok_four_bryce1_handjob_wsgoout:
                                    $ bangok_four_bryce1_wstiming = "before"
                                    play soundloop "fx/faucet1.ogg" fadein 1.0
                                    queue soundloop "fx/faucet2.ogg"
                                    Br laugh dk "啊..."
                                    m "我看着，迷惑地看着避孕套的储液囊膨胀起来。{w=0.8}几秒钟过去了，体积比任何人类的都大。"
                                    stop soundloop fadeout 1.0
                                    $ renpy.pause(1.0)
                                    stop soundloop
                                    Br normal dk "好了。我们到哪儿了？"
                                    label bangok_four_bryce1_handjob_wscondomleft:
                                    if persistent.bangok_balls == True:
                                        m "避孕套还挂在他的阴茎上，一个充满尿液的摇摆气球比他的睾丸还大。"
                                    else:
                                        m "避孕套还挂在他的阴茎上，一个充满尿液的摇摆气球。"
                                    menu:
                                        "喝下它。":
                                            m "我捏住他避孕套的顶端，然后抓住底部的环，滑下整个避孕套。尿液的气味像春药一样扑来。"
                                            show bryce flirty dk with dissolve
                                            m "在我能思考之前，我已经把环放进嘴里，并把气球举到头顶上方。"
                                            show bryce smirk dk with dissolve
                                            play sound "fx/water2.ogg"
                                            if persistent.bangok_inflation == True:
                                                queue sound "fx/gulpslow2.wav"
                                                $ renpy.pause (9.0)
                                                m "这是一个巨大的量。我不得不停下来休息一下。当我喝完后，我感觉被Bryce最近离开的温暖填满了。"
                                                $ bangok_four_bryce1_playerstuffed = True
                                                $ bangok_four_bryce1_position_pickb = "oralbot"
                                            else:
                                                queue sound "fx/gulping.wav"
                                                $ renpy.pause (3.0)
                                                stop sound fadeout 1.0
                                            $ brycemood += 1
                                            Br flirty dk "那真是激动人心的观看。"
                                            m "吮吸最后从现在空的避孕套中，我把它重新套回他的阴茎。"
                                            c "让我们继续。"
                                        "更换它。":
                                            m "我捏住他避孕套的顶端，然后抓住底部的环，滑下整个避孕套。尿液的气味像浪潮一样袭来。"
                                            m "系上它，我把它滚到一边，在地板上滚到一边。然后我回到他的避孕套抽屉，拿了另一个。"
                                            c "让我们继续。"
                                "好时机。我可以洗个澡。" if bangok_four_bryce1_wstiming is None:
                                    $ bangok_four_bryce1_wstiming = "after"
                                    Br stern dk "哦不。今晚我不清理这个。"
                                    Br brow dk "再说，你{i}已经{/i}会闻到我和酒精的味道。不确定实际洗澡能不能洗掉。你认为他们能闻到尿液还是会是个好大使？"
                                    c "..."
                                    Br stern dk "今晚没有外头的东西。"
                                    c "好吧。"
                                    jump bangok_four_bryce1_handjob_wsmenu
                                "让我给你一个地方。":
                                    $ bangok_four_bryce1_wstiming = "before"
                                   $ brycemood += 1
                                    Br brow dk "嗯？"
                                    m "我用手握住避孕套的顶端和环部，将它从布莱斯的阴茎上完全拉了下来。"
                                    m "然后我将他的阴茎对准我的嘴，只吸吮着顶端。"
                                    Br stern dk "你确定？"
                                    menu:
                                        "公平而已。":
                                            pass
                                        "是的。":
                                            pass
                                    m "我含着他的肉茎顶端，含糊不清地说。"
                                    m "布莱斯颤抖了一下，然后当他的尿流进入我的嘴时，他的阴茎抽动了一下。"
                                    $ bangok_four_bryce1_wstiming = "之前"
                                    play soundloop "fx/faucet1.ogg" fadein 1.0
                                    queue soundloop "fx/faucet2.ogg"
                                    Br laugh dk "啊..."
                                    play sound ["fx/massage.ogg", "fx/massage.ogg", "fx/massage.ogg", "fx/massage.ogg"]
                                    m "当他在我嘴里小便时，我继续抽动，想要给他尽可能多的感觉。"
                                    if persistent.bangok_inflation == True:
                                        m "正常吞咽快速的尿流是不可能的。我呛了一下，尿液在我的嘴里四溢，带有独特的味道。布莱斯的热量直接传递到我的胃里，身体开始发热。"
                                        m "不想在嘴唇的密封处失去一滴，我将布莱斯的阴茎更深地送入咽喉，部分进入我的喉咙，让他直接尿进我的肚子。"
                                        $ bangok_four_bryce1_playerstuffed = True
                                    else:
                                        m "正常吞咽尿流几乎是不可能的。我呛了一下，尿液在我的嘴里四溢，带有独特的味道。布莱斯的热量直接传递到我的胃里，身体开始发热。"
                                    stop soundloop fadeout 3.0
                                    m "当尿流开始减少，我在吞咽间隙中喘气时，布莱斯的呼吸变得沉重。"
                                    Br stern dk "嗯。继续这样下去我可能现在就要射了。"
                                    menu:
                                        "给他一点时间。":
                                            stop sound fadeout 1.0
                                        "现在。":
                                            $ bangok_four_bryce1_protected = False
                                            show bryce laugh dk flip with dissolve
                                            $ bangok_four_bryce1_brycecame = True
                                            play sound2 "fx/snarl.ogg"
                                            stop sound fadeout 4.0
                                            jump bangok_four_bryce1_oralbot_cum
                                    m "我松开手，将他的阴茎从我的嘴里弹出来，给他几秒钟时间恢复。"
                                    $ renpy.pause(1.5)
                                    Br flirty dk "谢谢。这...真是好东西。"
                                "继续。":
                                    m "我又抽动了几下布莱斯的阴茎，表示我并没有因为尿液而厌恶，只是觉得无法安全处理。"
                                    m "布莱斯颤抖了一下，然后他的阴茎抽动了一下，将液体释放到避孕套中。"
                                    jump bangok_four_bryce1_handjob_wsgoout
                            play soundloop "fx/massage.ogg" fadein 3.0
                            m "我重新拿回他的阴茎，等他适应了片刻后，继续之前的抽动节奏。"
                        $ renpy.pause(1.4)
                        Br smirk dk "别以为我以后还能接受龙的手淫。"
                        Br laugh dk "你的光滑的手..."
                        play sound "fx/snarl.ogg"
                        stop soundloop fadeout 1.5
                        m "突然，避孕套的储液囊膨胀了，他的第一次喷射在里面四溢。"
                        show bryce laugh dk with dissolve
                        m "我又抽动了几下，将他完全释放出来，他的嘴巴张开着。"
                        $ renpy.pause(0.8)
                        Br smirk dk "操，那真舒服。"
                        if bangok_four_bryce1_playerstuffed == True:
                            m "又一股液体负载使避孕套在我面前膨胀。我还有空间吗？"
                        else:
                            m "布莱斯的精液球在我面前晃动。"
                        menu:
                            "喝掉。":
                                m "我捏住避孕套的顶端，然后握住底部的环，将整个东西滑了下来。精液的气味浓烈而令人陶醉。"
                                show bryce flirty dk with dissolve
                                m "在我意识到自己在做什么之前，我已经将环放入嘴里，并将避孕套的球提到头顶。"
                                show bryce smirk dk with dissolve
                                if persistent.bangok_inflation == True:
                                    queue sound "fx/gulpslow2.wav"
                                    $ renpy.pause (9.0)
                                    if persistent.bangok_watersports == True and bangok_four_bryce1_playerstuffed == True:
                                        m "即使中途休息一下，布莱斯的精液量还是太多了，无法在他的尿液上装下，我不得不放弃，避孕套只空了四分之三。"
                                        m "我的肚子明显隆起。"
                                        Br flirty dk "你这贪婪的小东西。"
                                    else:
                                        m "这是一个巨大的量。我不得不中途暂停休息一下。当我完成时，布莱斯的精液把我塞得满满的，我确信我的肚子略微隆起。"
                                    $ bangok_four_bryce1_playerstuffed = True
                                    $ bangok_four_bryce1_position_pickb = "oralbot"
                                else:
                                    queue sound "fx/gulping.wav"
                                    $ renpy.pause (3.0)
                                    stop sound fadeout 1.0
                                $ brycemood += 1
                                Br flirty dk "那真是好看。"
                                m "我丢弃了避孕套，感觉到我的消耗使我所剩不多的能量被消耗殆尽。"
                            "拿掉。":
                                m "我捏住避孕套的顶端，然后握住底部的环，将整个东西滑了下来。精液的气味浓烈。"
                                m "我把它扎好，放在旁边，不会被踩到的地方。"

                        if persistent.bangok_knot == True:
                            m "虽然他已经射精了，但他的阴茎根部出现了一股肿块，我在热潮中没有注意到。"
                            menu:
                                "挤压它。":
                                    Br laugh dk "嘿！"
                                    Br smirk dk "现在就试图让我再次兴奋有点早。"
                                "放过它。":
                                    pass


                        jump bangok_four_bryce1_bothdone


                    "我不确定我能容纳你。" if bangok_four_bryce1_m2_fit:
                        call bangok_four_bryce1_m2_fit from bangok_four_bryce1_preciprocity_menu_fit
                        jump bangok_four_bryce1_preciprocity_menu

```python
        "我想让你吸我。":
            $ bangok_four_malepartners += 1
            Br flirty dk "当然。但你也要对我做同样的事。"
            if False:
                label bangok_four_bryce1_m2_bsucc_merge:
                Br normal dk "对我来说没问题。"
            call bangok_four_bryce1_position("oraltop")
            show bryce flirty dk with dissolve
            show bryce at Position(ypos=1.3) with ease
            show bryce at Position(ypos=1.5) with ease
            m "布莱斯靠近我的裆部，他的热气洒在我逐渐硬挺的阴茎上。"
            if bangok_four_bryce1_protected:
                menu:
                    "[[戴上你的避孕套。]":
                        c "等一下！保护措施！"
                        show bryce brow dk at Position(ypos=1.3) with ease
                        m "布莱斯叹了口气，等了一会儿让我戴上避孕套。"
                        $ renpy.pause (0.3)
                        show bryce at Position(ypos=1.5) with ease
                    "[[不用戴。]":
                        $ bangok_four_bryce1_protected = False
            elif not bangok_four_bryce1_brycecame:
                menu:
                    "等一下！保护措施！":
                        show bryce brow dk at Position(ypos=1.3) with ease
                        Br "你在开玩笑吗？"
                        c "我们不知道我的东西对你会有什么影响。"
                        if chapter2unplayed == False and chapter2storeunplayed == False and chap2storehealth == False:
                            c "我在这儿看到过健康区。你有避孕套。"
                        else:
                            c "你们这种生物有避孕套，对吧？"
                        show bryce stern dk with dissolve
                        m "布莱斯呻吟了一声，然后指了指角落里的一个抽屉。"
                        Br "顶层。我想。赶快。"
                        $ bangok_four_bryce1_protected = True
                        play sound "fx/rummage.wav"
                        m "有几种不同品牌的避孕套，上面标着布莱斯尺寸的实际大小。我挑了一个，以防万一，然后继续寻找适合我尺寸的。"
                        m "直到挖到最底层，我才终于找到一个接近我尺寸的完整包装的避孕套盒。"
                        m "撕开包装，我带着必要的装备回来了。"
                        c "好了。"
                        Br smirk dk "终于。"
                        show bryce at Position(ypos=1.5) with ease
                    "[[享受吧。]":
                        pass
            show bryce at Position(ypos=1.51) with ease
            m "向前一推，他一口将我的整根阴茎吞入嘴中，撞到了我的骨盆。我几乎没有机会享受这种感觉，因为..."
            
            play sound "fx/impact3.ogg"
            show bryce brow dk at Position(ypos=1.2)
            show bangok_four_bryce1_apartment night at Pan((0,120), (0,120), 0.0)
            with vpunch
            m "我失去了平衡，摔倒在地。"
            Br "哎呀。"
            c "疼。"
            show bryce normal dk at Position(ypos=1.2)
            show bangok_four_bryce1_apartment night at Pan((0,360), (0,360), 0.0)
            with ease
            m "爬起来后，我环顾房间寻找下一次尝试的支撑物。"
            menu:
                "墙。":
                    $ bangok_four_bryce1_oralspot = "wall"
                    c "这里，靠着墙。"
                    Br smirk dk "你说了算。"
                    m "我轻轻靠在墙上，张开双腿，让布莱斯更容易接触到我的裆部。"
                    $ renpy.pause (0.3)
                "沙发。":
                    $ bangok_four_bryce1_oralspot = "couch"
                    c "这里，我坐在你的沙发上怎么样？"
                    $ renpy.pause (0.5)
                    Br brow dk "往前一点。我不想我的下巴角弄破我的垫子。"
                    $ renpy.pause (0.3)
            Br flirty dk "好了。现在看看人类是什么味道。"
            if bangok_four_bryce1_protected == True:
                $ brycemood -= 1
                Br brow dk "通过避孕套。"
            show bryce smirk dk at Position(ypos=1.3) with ease
            show bryce smirk dk at Position(ypos=1.5) with ease
            $ renpy.pause(0.3)
            m "布莱斯在我的双腿之间安顿下来，他的鼻鳞摩擦着我的大腿。"
            m "房间里的冷空气被他的呼气温暖了我的裆部。"
            show bryce smirk dk at Position(ypos=1.51) with ease
            m "然后他猛地一吸，把我的阴茎和睾丸都包在他温暖的口中。"
            c "嗯！"
            m "我只能努力坐稳，他的舌头在我的阴茎根部缠绕，尖端轻轻拉扯着我的睾丸，足以使它们弹跳和挑逗。"
            c "哇。"
            show bryce flirty dk with dissolve
            $ renpy.pause(0.3)
            show bryce smirk dk at Position(ypos=1.5) with ease
            m "他往后拉，牙齿和鳞唇的边缘刚刚擦过我的阴茎顶部和嚼过我的睾丸底部。我握紧拳头，努力不把自己送入他的脸。"
            m "他让我的睾丸从他的嘴里滑出，把他的鳞唇和舌头集中在我的阴茎上。"
            m "这是奢侈的体验。但他并没有完全深入到我的裆部；我的阴茎顶端还有一点地方在他的嘴外。"
            menu:
                "[[抓住他的角。]":
                    $ bangok_four_hornincident = True
                    $ brycemood -= 2
                    if bangok_four_bryce1_oralspot == "couch":
                        play sound ["fx/hit2.ogg", "fx/cartdown.ogg"]
                        show bryce stern dk at Position(ypos=1.3) with ease
                        m "布莱斯猛地一动，松开了我的阴茎，把他的口鼻撞在我的胸口，震动了沙发。幸运的是，我没有被他的下巴和鼻角割伤。"
                    else: # bangok_four_bryce1_oralspot == "wall":
                        play sound ["fx/hit2.ogg", "fx/impact3.ogg"]
                        show bryce stern dk at Position(ypos=1.3) with ease
                        m "布莱斯猛地一动，松开了我的阴茎，把他的口鼻撞在我的胸口，把我压在墙上。幸运的是，我没有被他的下巴和鼻角割伤。"
                    c "妈的！"
                    $ renpy.pause (1.2)
                    c "好吧，不要碰角。明白了。"
                    Br brow dk "不，要碰。但请告诉我。那是我们很脆弱的地方。某些方向猛拉我们的角会把它们从颅骨上扯下来。"
                    c "我不认为我有那么大力气。"
                    Br stern dk "我也不认为。但如果我没预料到，我还是会有反应的。"
                    m "经过一会儿严肃的目光，布莱斯又回到了我的大腿之间。"
                    show bryce at Position(ypos=1.5) with ease
                    show bryce flirty dk with dissolve
                    m "他一开始工作，我几乎立刻又到了想要把脸埋进他的状态。他的舌头在我的裆部注入了强烈的感觉，戏弄着我的阴茎。"
                    menu:
                        "我可以抓你的...":
                            $ brycemood += 1
                            m "把他的脸更深地推入我的裆部当作鼓励，我抓住了布莱斯的角并推送。"
                        "[[射精。]":
                            pass
                "[[让他更深。]":
                    if bangok_four_bryce1_oralspot == "couch":
                        m "布莱斯照做了，他的脸挤进了我的大腿和裆部，而他的下巴角几乎割裂了我的睾丸，并戳到了枕头。"
                    else: # bangok_four_bryce1_oralspot == "wall":
                        m "布莱斯照做了，他的脸把我的骨盆紧紧地压在墙上。"
                    c "小心点！"
                    m "他发出了一声难以分辨的声音，这声音在他的口腔里围绕着我的阴茎震动。"
                    m "这是我能忍受的极限了。"
                "我快要高潮了！":
                    pass
            
            play sound "fx/extinguish.ogg"
            show black with dissolve
            if bangok_four_bryce1_protected == True:
                m "我射了，把我的精液存储在布莱斯舌头上的避孕套里。"
            else:
                m "我射了，射进了布莱斯的嘴里。"
            $ bangok_four_bryce1_playercame = True
            hide black with dissolvemed

            if persistent.bangok_watersports == True:
                play soundloop "fx/faucet1.ogg" fadein 1.0
                queue soundloop "fx/faucet2.ogg"
                show bryce brow dk with dissolve
                m "一会儿后，我意识到更多的液体从我体内排出。"
                c "呃。"
                if bangok_four_bryce1_protected == True:
                    m "我的脸颊红了。我确定布莱斯知道发生了什么，但他还是继续吸着避孕套。"
                else:
                    play sound "fx/gulping.wav"
                    m "我的脸颊红了。我确定布莱斯知道发生了什么，但听起来他似乎在..."
                stop soundloop fadeout 1.5
                stop sound fadeout 0.5
                $ renpy.pause (1.5)
                show bryce at Position(ypos=1.3) with ease
                Br smirk dk "我经常和喝酒的朋友发生性关系。你以为你是第一个在我体内尿尿的人吗？"

            show bryce at Position(ypos=1.0) with ease
            if brycemood > 0:
                show bryce flirty dk with dissolve
                m "站起来后，布莱斯对我眨了眨眼。"
            else:
                show bryce stern dk with dissolve
                m "布莱斯站了起来。"
            if bangok_four_bryce1_brycecame:
                jump bangok_four_bryce1_bothdone
            else:
                Br flirty dk "那是你的。现在轮到我了，好吗？"
                jump bangok_four_bryce1_preciprocity_menu
```
        "其实没那么小..." if bangok_four_bryce1_m2_size:
            $ bangok_four_bryce1_m2_size = False
            c "我知道这可能比你习惯的要小，而且可能根本不能让你高潮--"
            # show bryce laugh dk with dissolve
            # $ renpy.pause(0.8)
            Br smirk dk "别担心。我见过更小的。如果你不能用工具，也可以用手啊。"
            jump bangok_four_bryce1_m2_menu

        "我不确定我能装得下你。" if bangok_four_bryce1_m2_fit:
            call bangok_four_bryce1_m2_fit from bangok_four_bryce1_m2_menu_fit
            jump bangok_four_bryce1_m2_menu
            label bangok_four_bryce1_m2_fit:
                $ bangok_four_bryce1_m2_fit = False
                c "你，呃..."
                Br flirty dk "你没见过这样的，对吧？"
                c "确实没有。"
                Br smirk dk "而且，尤其是像我这样的，他们...我想你明白我的意思。"
                c "嗯哼。"
                Br "如果你不想尝试的话，你不需要勉强自己。"
                c "好的。"
                return

label bangok_four_bryce1_badmorning:
    scene black with fade
    $ renpy.pause (1.5)
    scene pad at Pan ((0, 0), (0,360), 5.0) with dissolveslow
    play music "mx/campfire.ogg" fadein 2.0
    nvl clear
    window show
    n "我醒来时看着一个陌生的天花板。"
    n "有一瞬间，我在想我在哪里，然后昨晚的一些事情回到了我的脑海。"
    n "我起身四处看看，发现自己显然是裸着睡在地板上。"
    if bangok_four_bryce1_protected and not bangok_four_bryce1_playercame:
        n "一个未填满的避孕套还挂在我软软的阴茎上。"
    window hide
    nvl clear
    show bryce brow with dissolve
    Br "嘿，你还好吗？"
    c "我们昨晚做了什么？"
    if bangok_four_bryce1_playercame == False and bangok_four_bryce1_brycecame == False:
        Br stern "没做什么。"
    elif not bangok_four_bryce1_brycecame:
        Br stern "不够。"
    else:
        Br stern "太多了。"
    c "我们有个喝酒比赛..."
    Br brow "那么你记得不少。"
    Br stern "拿上你的衣服，走吧。"
    c "什么？"
    if bangok_four_bryce1_brycecame == False:
        Br "比赛是个愚蠢的主意。单方面的性行为更是如此。"
    else:
        Br "比赛是个愚蠢的主意。那拙劣的性爱尝试更是如此。"
    c "等等，你是那个推崇比赛的人。"
    Br "而你是那个推动性爱的人。愚蠢的想法到处都是。"
    c "事后说起来很容易。"
    Br brow "说得好像完全是你的错似的。"
    c "抱歉？我们都喝醉了。"
    Br stern "昨晚开始时，我认为我已经很清楚地表达了我期望的事情是互相的。"
    c "如果我{i}没有喝醉{/i}的话，你的表达会更清楚。"
    Br "那这就成了我的错了？"
    stop music fadeout 3.0
    c "差不多。作为大使，我不能真的拒绝与警察局长的社交会面。"
    play sound "fx/tableslap.wav"
    m "布莱斯挥尾巴的动作几乎把他的咖啡桌打翻。"
    Br angry "是你逼我{i}和你{/i}发生关系！" with vpunch
    c "..."
    Br "..."
    Br stern "这从你我醉倒时不合适的触摸开始。"
    c "因为我是醉了，因为你的愚蠢喝酒比赛。"
    Br brow "所以永远不是你的错，总是我的错？真是精彩，除了你自己，谁的错都行。干得好，[player_name]。"
    Br stern "拿上你的衣服，走吧。"
    m "他几乎不给我穿衣服的时间，用他尖尖的鼻子把我推出了他的门，还是赤身裸体的。"
    play sound "fx/door/doorclose3.wav"
    scene black with dissolve
    if bangok_four_bryce1_protected and not bangok_four_bryce1_playercame:
        m "那个未填满的避孕套还挂在我软软的阴茎上。"
    $ bangok_four_bryce1_unplayed = False
    $ brycestatus = "bad"
    $ brycescenesfinished = 1
    jump _mod_fixjmp
```

label bangok_four_bryce1_morningcouch:
    scene black with fade
    $ renpy.pause (1.5)
    scene pad at Pan ((0, 0), (0,360), 5.0) with dissolveslow
    play music "mx/campfire.ogg" fadein 2.0
    nvl clear
    window show
    n "我醒来看着一个陌生的天花板。"
    n "一会儿，我不知道我在哪儿，直到昨晚发生的事情回到了我的记忆中。"
    if bangok_four_bryce1_playerstuffed 或 "analbot" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
        n "我的内脏在我坐起来时抱怨着，仍然被昨晚的所作所为扰乱了。我发现自己睡在布莱斯的沙发上，赤身裸体。"
    elif "vag" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
        n "我的爱道在我坐起来时抱怨着，仍然被昨晚的所作所为扰乱了。我发现自己睡在布莱斯的沙发上，赤身裸体。"
    else:
        n "我坐起来环顾四周，发现自己睡在布莱斯的沙发上，赤身裸体。"
    show bryce laugh at Position(ypos=1.2, xpos=0.55, xanchor='center') with dissolvemed
    n "布莱斯趴在沙发和茶几之间的地毯上，口水流在地毯上。昨晚我们疯狂的爱的证据仍然在他两腿之间的鳞片上。"
    window hide
    nvl clear

    c "嘿，布莱斯。"
    menu:
        "你在流口水。":
            $ brycemood -= 1
            m "这条龙动了一下，呻吟着，然后睁开眼睛。"
            show bryce brow with dissolve
            Br "就像你偶尔也会的那样，我打赌。"
        "醒醒，胖子。":
            $ brycemood -= 2
            m "这条龙动了一下，呻吟着，然后睁开眼睛。"
            show bryce stern with dissolve
            c "(这话激怒了他。)"
            Br "告诉你吧，我们的种类通常看起来比其他的要大，这也使得我们最强壮。"
            show bryce brow with dissolve
        "早安，阳光。":
            $ brycemood += 1
            m "这条龙动了一下，呻吟着，然后睁开眼睛。"
            show bryce normal with dissolve
    $ renpy.pause(0.9)
    show bryce brow with dissolve
    $ renpy.pause(0.5)
    m "布莱斯似乎在思考昨晚的记忆，然后猛然开始挣扎着站起来。"
    show bryce stern at Position(ypos=1.2, xpos=0.45, xanchor='center') with ease
    show bryce at Position(ypos=1.2, xpos=0.55, xanchor='center') with ease
    m "我自己也从沙发上站起来，然后把茶几推到一边，给他翻身的空间。"
    show bryce at center with ease
    Br normal "谢谢。"
    $ brycemood += 1
    $ renpy.pause (0.9)

    if False:
        label bangok_four_bryce1_morningfloor:
        scene black with fade
        $ renpy.pause(1.5)
        scene pad at Pan ((0, 0), (0,360), 5.0) with dissolveslow
        play music "mx/campfire.ogg" fadein 2.0

        nvl clear
        window show
        n "我醒来看着一个陌生的天花板。"
        n "一会儿，我不知道我在哪儿，直到昨晚的事情回到了我的记忆中。"
        if bangok_four_bryce1_playerstuffed 或 "analbot" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            n "我的内脏在我坐起来时抱怨着，仍然被昨晚的所作所为扰乱了。我发现自己睡在布莱斯的地板上，赤身裸体。"
        elif "vag" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            n "我的爱道在我坐起来时抱怨着，仍然被昨晚的所作所为扰乱了。我发现自己睡在布莱斯的地板上，赤身裸体。"
        else:
            n "我坐起来环顾四周，发现自己睡在布莱斯的地板上，赤身裸体。"
        window hide
        nvl clear

        scene black with dissolve
        $ renpy.pause (0.5)
        scene cgbryce with dissolvemed
        $ renpy.pause(2.0)

        c "嘿，布莱斯。"
        menu:
            "你在流口水。":
                $ brycemood -= 1
                m "这条龙动了一下，呻吟着，然后睁开眼睛。"
                scene pad at Pan ((0, 360), (0,360), 0.0)
                show bryce brow
                with dissolve
                Br "就像你偶尔也会的那样，我打赌。"
            "醒醒，胖子。":
                $ brycemood -= 2
                m "这条龙动了一下，呻吟着，然后睁开眼睛。"
                scene pad at Pan ((0, 360), (0,360), 0.0)
                show bryce stern
                with dissolve
                c "(这话激怒了他。)"
                Br "告诉你吧，我们的种类通常看起来比其他的要大，这也使得我们最强壮。"
                show bryce brow with dissolve
            "早安，阳光。":
                $ brycemood += 1
                m "这条龙动了一下，呻吟着，然后睁开眼睛。"
                scene pad at Pan ((0, 360), (0,360), 0.0)
                show bryce normal
                with dissolve
                Br "嘿，[player_name]。"
        show bryce laugh with dissolve
        m "这条龙从沙发上起身，伸了伸懒腰，揉了揉眼睛，然后高傲地抬起头，发出一声低吼并打了个大哈欠。"
        show bryce stern with dissolve
        m "然后他眨了眨眼睛。"

    Br brow "你记得昨晚的事情吗？"

    menu:
        "我记得布莱斯，没事。":
            c "我们双方都是自愿的。我至少是很享受的。"
            m "布莱斯立即放松了下来。"
            Br normal "哦。"
        "我送你回了家，对吧？":
            $ brycemood -= 1
            Br stern "这不是开玩笑，[player_name]。你记得我们之间发生了什么吗？"
            c "当然。我只是开个玩笑。"
            $ renpy.pause (0.8)
        "我不能相信那样的事情发生了。":
            Br "以什么样的方式？"
            c "那真是太棒了。"
            $ brycemood += 1
            if brycemood > 2:
                show bryce smirk with dissolve
            else:
                show bryce brow with dissolve
            Br "那确实是一种体验。"
        "我的屁股还在疼。" if "analbot" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            Br laugh "我一点也不惊讶。"
            Br normal "你还好吗？"
            c "我想应该可以。"
        "我今天可能会走路怪怪的。" if "vag" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            Br laugh "我一点也不惊讶。"
            Br normal "你还好吗？"
            c "我想应该可以。"
        "布莱斯，避孕套还挂在我的阴道里。" if "vag" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb] 和 bangok_four_bryce1_protected 和 persistent.bangok_knot 和 bangok_four_bryce1.knotpos != "out" 和没有（persistent.bangok_watersports 和 persistent.bangok_inflation） 和没有 bangok_four_bryce1_playerstuffed:
            Br smirk "是吗？"
            m "布莱斯看了看。"
            Br brow "哦。该死。真的是。"
            m "靠在他的沙发上，我打了个结，然后把整个东西拉出来。"
            play sound "fx/uncork.ogg"
            $ renpy.pause (0.5)
            $ brycemood += 2
            Br laugh "我猜我在打结后忘记了它，然后就睡着了。"
            c "看来是这样。"
        "布莱斯，避孕套还挂在我的屁股里。" if "analbot" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb] 和 bangok_four_bryce1_protected 和 persistent.bangok_knot 和 bangok_four_bryce1.knotpos != "out" 和没有（persistent.bangok_watersports 和 persistent.bangok_inflation） 和没有 bangok_four_bryce1_playerstuffed:
            Br smirk "是吗？"
            m "布莱斯看了看。"
            Br brow "哦。该死。真的是。"
            m "靠在他的沙发上，我打了个结，然后把整个东西拉出来。"
            play sound "fx/uncork.ogg"
            $ renpy.pause (0.5)
            $ brycemood += 2
            Br laugh "我猜我在打结后忘记了它，然后就睡着了。"
            c "看来是这样。"

    if persistent.bangok_watersports 和 bangok_four_bryce1_playerstuffed:
        if "vag" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            m "我的手放在肚子上，感觉昨晚的液体在里面移动。"
        else:
            m "我的手放在肚子上，感觉昨晚的液体在里面移动。"
        if "analbot" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb] 或 "vag" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            m "几乎所有的都还在里面。"
        else: # "oralbot" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            m "我肚子里的液体在我睡觉时转移到了我的膀胱！"
        c "该死。我能用一下你的洗手间吗？"
        Br brow "当然。"
        if brycemood > 0:
            if persistent.bangok_watersports 和 "oralbot" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
                Br flirty "或者你可以让我尝尝。"
                menu:
                    "[[让布莱斯喝你的尿。]]":
                        $ brycemood += 1
                        m "我蹒跚地走向布莱斯，不确定我还能坚持多久。"
                        show bryce at Position(ypos=1.3) with ease
                        show bryce at Position(ypos=1.5) with ease
                        show bryce laugh with dissolve
                        m "他低下头，张开大嘴，让我直接尿到他的喉咙深处。"
                        play soundloop "fx/faucet1.ogg" fadein 1.0
                        queue soundloop "fx/faucet2.ogg"
                        if bangok_four_playerhasdick == True:
                            c "啊..."
                            m "我的金色尿液流到了他的喉咙深处，我能看到他在吞咽。他的舌头舔着我的阴茎，几个小流滴落在他的脸颊两侧。"
                            stop soundloop fadeout 3.0
                            $ renpy.pause (2.5)
                            show bryce at Position(ypos=1.3) with ease
                            m "布莱斯舔了舔我的阴茎头，然后站起来。"
                            show bryce at center with ease
                            m "布莱斯舔了舔我的阴茎头，然后站起来。然后用他的前腿擦了擦嘴，舔了舔那只爪子。"
                            $ renpy.pause(0.8)
                            c "我们要来第二轮吗？"
                            Br laugh "不行！"
                            Br smirk "我们都得清理一下，你也一样。人们会注意到我们都不在工作。"
                            c "该死。"
                        else:
                            c "啊..."
                            m "我压在他的嘴上，把他当成一个巨大的活生生的马桶，反向坐在他上面。"
                            m "热气在他的每次吞咽之间从我的私密处吹过。他的牙齿轻轻碰触我的下腹，他的舌头深入我体内，寻找更多的金色液体。"
                            stop soundloop fadeout 3.0
                            c "哦，天哪！"
                            m "其他液体混合着尿液和他的唾液流出，他一直在寻找更多。"
                            label bangok_four_bryce1_morningride_menu:
                            menu:
                                "你让我兴奋了！":
                                    show bryce flirty with dissolve
                                    m "布莱斯朝我眨了眨眼，知道他在做什么。"
                                    jump bangok_four_bryce1_morningride
                                "我能抓住你的角吗？" if bangok_four_hornincident == True:
                                    $ brycemood += 1
                                    show bryce flirty with dissolve
                                    m "布莱斯朝我眨了眨眼，把这当成许可，我抓住了他的角，把他的脸更深地压在我的下体上。"
                                    jump bangok_four_bryce1_morningride
                                "[[离开他。]]":
                                    $ brycemood -= 1
                                    m "我用手按住他的鼻子，后退了一步。"
                                    c "布莱斯，我们先谈谈吧！"
                                    m "一股热气吹过我的下腹，然后布莱斯收回了舌头，让我安全地退开。"
                                    show bryce normal with dissolve
                                    $ renpy.pause(0.3)
                                    show bryce at Position(ypos=1.3) with ease
                                    $ renpy.pause(0.5)
                                    show bryce at center with ease
                                    m "我喘气。"
                                    c "这是不是意味着你想要来第二轮？"
                                    Br flirty "我希望是。"
                                    Br stern "但不幸的是，我们都有工作要做。"
                                    Br smirk "我们都得清理一下，你也一样。人们会注意到我们都不在工作。"
                                    c "哦。该死。"
                                "[[骑他。]]":
                                    label bangok_four_bryce1_morningride:
                                    show bryce laugh with dissolve
                                    m "双腿无力，我把更多的重量压在他的嘴上，他的牙齿稍微更紧地碰触我的皮肤。"
                                    c "哦，天哪。"
                                    play sound "fx/cartdown.ogg"
                                    with vpunch
                                    m "布莱斯压得更紧，让我后退几步，直到我重重地摔在沙发上。"
                                    show bryce flirty with dissolve
                                    m "他的舌头深入，把我带到高潮。"
                                    show black
                                    show bryce laugh
                                    with fadequick
                                    m "我在他的舌头里狠狠抽动，随着颤抖的快感减弱。"
                                    hide black with dissolveslow
                                    $ renpy.pause(0.5)
                                    m "布莱斯在抽出舌头时，像是告别亲吻般地舔了舔我的阴唇。"
                                    show bryce smirk with dissolve
                                    show bryce at Position(ypos=1.3) with ease
                                    $ renpy.pause(0.3)
                                    show bryce at center with ease
                                    m "然后他站了起来。"
                                    menu:
                                        "这真是太棒了。":
                                            $ brycemood += 1
                                            Br flirty "毫无疑问。"
                                        "轮到你了吗？":
                                            Br laugh "没机会！"
                                    Br normal "不幸的是，我们都有工作要做。"
                                    Br smirk "我们得清理一下，你也一样。人们会注意到我们都不在工作。"
                                    c "哦。该死。"
                                "[[抓住他的角并骑上去。]]" if bangok_four_hornincident == False:
                                    $ brycemood -= 2
                                    play sound ["fx/hit2.ogg", "fx/impact3.ogg"]
                                    show bryce angry with vpunch
                                    show bryce stern at center
                                    show pad at Pan((0,120), (0,120), 0.0)
                                    with ease
                                    with vpunch
                                    m "布莱斯猛然一震，把我的脚抬离地面，我摔倒在地，震惊得无话可说。"
                                    c "布莱斯，什么鬼？！"
                                    Br "那是我们一个敏感的地方。错误的方向拉角可能会把它们从我们的头骨上撕下来。"
                                    c "我不觉得我有那么强。"
                                    Br brow "我也不认为。但如果我没预料到，我还是会有反应。"
                                    c "抱歉。"
                                    $ renpy.pause (0.5)
                                    c "疼。"
                                    show pad at Pan((0,360), (0,360), 0.0) with ease
                                    m "我慢慢爬起来，仍在摆脱受伤的影响。"
                                    c "所以... 你舔我那意味着你想要来第二轮吗？"
                                    Br smirk "我希望是。"
                                    Br stern "但我们都有工作要做。"
                                    Br smirk "我们得清理一下，你也一样。人们会注意到我们都不在工作。"
                                    c "哦。该死。"

                        Br normal "嘿。别太失望。"
                        jump bangok_four_bryce1_morningcont
                    "[[洗手间。现在。]]":
                        pass
            elif "vag" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
                Br flirty "或者你可以让我尝尝。"
                menu:
                    "[[让布莱斯把他的液体喝回去。]]":
                        $ brycemood += 1
                        m "我蹒跚地走向布莱斯，不确定我还能坚持多久。"
                        show bryce at Position(ypos=1.3) with ease
                        show bryce at Position(ypos=1.5) with ease
                        show bryce laugh with dissolve
                        m "他低下头，张开大嘴，让我把子宫里的内容物推到他的喉咙深处。"
                        play soundloop "fx/faucet1.ogg" fadein 1.0
                        queue soundloop "fx/faucet2.ogg"
                        play sound (["fx/stones.ogg"]*10) fadein 3.0
                        c "啊..."
                        m "我把我的私密部位按在他的嘴里。热气在他的每次吞咽之间从我的私密处吹过。他的牙齿轻轻碰触我的下腹，他的舌头深入我体内，寻找更多他的精液。"
                        stop sound fadeout 2.0
                        stop soundloop fadeout 1.0
                        c "哦，天哪！"
                        m "其他液体混合着我们的交合结果和他的唾液流出，他一直在寻找更多。"
                        jump bangok_four_bryce1_morningride_menu
                    "[[洗手间。现在。]]":
                        pass
            # Feck. I don't know enough about rimming for this.
            # elif "analbot" 在 [bangok_four_bryce1_position_picka, bangok_four_bryce1_position_pickb]:
            #     Br flirty "或者你可以让我舔出来。"
            #     menu:
            #         "[[让布莱斯舔你。]]":
            #             c "得快点。我不知道还能忍多久..."
            #             show bryce at Position(ypos=1.3) with ease
            #             show bryce at Position(ypos=1.5) with ease
            #             m "他靠过来，头伸进我两腿之间，我分开腿给他更好的接触。"
            #             c "嘿--"
            #             m "我的抱怨被他的大舌头打断，舌头深入我的屁股，搅动里面的液体。"
            #         "[[洗手间。现在。]]":
            #             pass
        hide bryce with dissolve
        scene black with dissolve
        play sound "fx/door/doorclose3.wav"
        m "我跑进洗手间，把多余的液体都排进了马桶。"
        $ renpy.pause(1.8)
        scene pad at Pan ((0, 360), (0,360), 0.0)
        show bryce normal
        with dissolvemed
        Br "好点了吗？"
        c "嗯，好多了。"

    label bangok_four_bryce1_morningcont:
    $ renpy.pause (1.0)

    if brycemood > 0:
        if brycemood > 4:
            Br flirty "你知道吗，昨晚是我有过的最棒的性爱之一。"
            c "真的吗？"
            Br smirk "真的。你有很多...独特的特质。"
        elif brycemood > 2:
            Br flirty "昨晚真是美好时光。"
            Br normal "我很高兴我们最后做了。"
            c "我也很高兴。"
            Br smirk "你有很多...独特的特质。"
        else:
            Br normal "所以...昨晚。我们之间有一些误解，但我认为它解决了。"
            Br smirk "肯定是非常独特的。"
        menu:
            "所以你喜欢只是因为我是人类。":
                $ brycemood -= 1
                Br brow "不是仅仅如此。"
                c "..."
                Br normal "好吧，这可能是主要部分。"
            "你也很棒。":
                $ brycemood += 1
                Br flirty "是吗？"
            "[[什么都不说。]]":
                pass
        
        Br brow "问题是，我通常不会这么快进入关系。即便是计划过的一夜情。"
        c "所以你需要两个晚上来完成一夜情？"
        Br normal "通常是这样。那场饮酒比赛是个特别愚蠢的提议，尤其是对你。"
        c "嗯，这不是你逼我参与的，所以我也应该承担一些责任..."
        Br "让我们假装饮酒从未发生过，也许在我们对发生的事情冷静下来之前，暂时停止更多性行为。"
        c "成交。"
        Br normal "别误会了。我愿意邀请你过来，展示一下警察局长不单单是喝酒和性。"
        c "比如清醒时做爱？"
        Br flirty "还不完全。"
        Br normal "至少再见一面，做做朋友。"
        c "当然可以。"
        Br smirk "找到你的衣服了吗？"
        c "找到了。"
        stop music fadeout 1.0
        python:
            renpy.pause(1.0)
            brycestatus = "good"
            brycescenesfinished = 1
            persistent.bryce1skip = True
            bangok_four_bryce1_unplayed = False
        scene black with dissolveslow
        jump _mod_fixjmp
    else:
        Br stern "昨晚，我们之间有一些严重的误解。"
        c "哦？"
        Br brow "我不是说我对我们做的事情不满意，或者我没有享受，但我们显然太醉了，无法正常交流。"
        Br stern "之前的饮酒比赛也是个愚蠢的主意，我不该建议它，尤其是对你。"
        c "嗯，这不是你逼我参与的，所以我也应该承担一些责任..."
        show bryce normal with dissolve
        Br "让我们假装整个事情从未发生过。"
        menu:
            "包括性吗？":
                Br smirk "让我们对那方面冷静一下。那次太狂野了，甚至对我来说。"
                Br stern "而且我们下次需要大部分保持清醒。如果我们决定有下一次。"
                c "成交。"
            "成交。":
                pass
        show bryce brow with dissolve
        Br "等等...现在几点了？"
        Br "该死，我真的该开始清理了。我想我会迟到几分钟。你知道怎么从这里回你的公寓，对吧？"
        c "我想知道。"
        show bryce normal with dissolve
        Br "看来你也该走了，孩子。也许我会再见到你。"
        stop music fadeout 1.0
        python:
            brycestatus = "neutral"
            brycescenesfinished = 1
            persistent.bryce1skip = True
            bangok_four_bryce1_unplayed = False
        jump _mod_fixjmp

label bangok_four_bryce1_bryce2fix:
    c "你昨晚没注意到吗？"
    Br flirty "我有更多的注意力在其他地方。"
    Br laugh "但是认真的吗？所有活着的东西都有尾巴。怎么可能没有？"
    jump bangok_four_bryce1_bryce2fix_end