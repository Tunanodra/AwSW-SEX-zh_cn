##################### 注意 #####################
# 根据艺术品委员会的请求
# 作为这个场景基础的艺术品
# 绝对不允许在这个场景中添加任何水上运动 (也不要提及)。

init python in bangok_four_xdamion_store:
    unplayed = True
    peek_window = False

label bangok_four_annaxdamion:
    play soundloop "fx/bangok_poundofsalt.ogg" fadein 2.0
    m "当我走到安娜半掩的门前时，我听到实验室里传来有节奏的湿嗒嗒的声音。"
    $ renpy.pause(0.8)
    c "(那是什么声音...？)"
    
    if (bangok_four_common.bangnokay.check()):
        stop soundloop fadeout 1.0
        play sound "fx/steps/clean2.wav"
        show black with dissolvemed
        m "没有理由去窥探龙族的私生活或科学实验，我决定稍后再来。"
        jump bangok_four_annaxdamion_abort_merge

    menu:
        "靠近听听。" :
            pass
        "稍后再来。" :
            jump bangok_four_annaxdamion_abort1

    m "我走近了一点，试图听清楚里面发生了什么。"
    An disgust "该死的——达米恩，不要把我的尾巴弄弯！"
    "???" "害怕你会发现自己有点喜欢疼痛的感觉？嗯。"

    menu:
        "偷看。" :
            pass
        "稍后再来。" :
            jump bangok_four_annaxdamion_abort1

    scene black with dissolvemed
    $ renpy.pause (0.5)
    scene bangok_four_annaxdamion:
        zoom 2.2
        anchor (0.0,0.0)
        pos (0.0,-0.5)
    show white:
        alpha 0.9
    show bangok_four_labdoor:
        anchor (0.0,0.0)
        pos (0.0,0.0)
    with dissolvemed

    $ renpy.pause (0.5)

    show bangok_four_annaxdamion:
        ease 3.0 zoom 1.1 pos (180, 0)
        block:
            ease 0.5 pos (175, 0)
            ease 0.15 pos (180, 0)
            repeat
    show bangok_four_labdoor:
        transform_anchor True
        ease 3.0 zoom 2.5 pos (-2880, -427)
        block:
            block:
                choice:
                    ease 0.8 pos (-2885, -427)
                choice:
                    ease 1.0 pos (-2885, -427)
                choice:
                    ease 1.2 pos (-2885, -427)
            pause 0.5
            block:
                choice:
                    ease 0.8 pos (-2880, -427)
                choice:
                    ease 1.0 pos (-2880, -427)
                choice:
                    ease 1.2 pos (-2880, -427)
            pause 0.5
            repeat
    show white:
        pause 2.0
        ease 1.3 alpha 0.0
    with None

    $ renpy.pause (2.5)

    An sad "你能快点射吗？我好去清理一下然后回去工作。"
    Dm arrogant "我会在我觉得合适的时候射在你里面。"
    stop soundloop fadeout 1.0
    show bangok_four_annaxdamion:
        ease 3.0 zoom 1.1 pos (190, 0)
    with ease
    Dm normal "现在向前挪一下。我想要压在你身上。"
    An face "你已经压在我身上了！"

    menu:
        "仔细看看门缝。" :
            $ bangok_four_xdamion_store.peek_window = False

            show bangok_four_labdoor dk track with dissolve
            show bangok_four_labdoor dk track:
                ease 2.0 zoom 10.0 pos (-12550, -3000)
                zoom 10.0
                pos (-12550, -3000)
            show bangok_four_annaxdamion:
                ease 2.1 zoom 1.2 pos (200, 0)
                pause 0.3
                block:
                    ease 0.5 pos (205, 0)
                    ease 0.15 pos (200, 0)
                    repeat
            with None
            $ renpy.pause (2.0)

        "通过窗口偷看。" :
            $ bangok_four_xdamion_store.peek_window = True

            show bangok_four_labdoor dk track with dissolve
            show bangok_four_labdoor dk track:
                ease 2.0 zoom 10.0 pos (-9650, -6900)
                zoom 10.0
                pos (-9650, -6900)
            show bangok_four_annaxdamion:
                ease 2.1 zoom 1.2 pos (200, 0)
                pause 0.3
                block:
                    ease 0.5 pos (205, 0)
                    ease 0.15 pos (200, 0)
                    repeat
            with None
            $ renpy.pause (2.0)
        "稍后再来。" :
            jump bangok_four_annaxdamion_abort2

    play soundloop "fx/rub2.ogg"
    $ renpy.pause (0.5)
    Dm arrogant "太棒了。"
    An sad "嗯嗯。"
    $ renpy.pause (1.6)

    Dm arrogant "啊。看吧？当你为我敞开的时候是不是很好？"
    An sad "..."
    Dm face "嗯。好吧，玩乐时间快结束了。"
    if persistent.bangok_cloacas == True:
        Dm "好好清理你的泄殖腔吧。"
    else:
        Dm "好好清理你的阴道吧。"

    stop soundloop fadeout 0.5
    play sound "fx/rub2.ogg"
    show bangok_four_annaxdamion:
        ease 2.1 zoom 1.2 pos (200, 0)
    with ease
    $ renpy.pause (0.3)
    play sound "fx/extinguish.ogg"

    show bangok_four_annaxdamion cum with dissolvemed

    if persistent.bangok_inflation == True:
        Dm face "该死的，这是一大股。"
        show bangok_four_annaxdamion bulge cum with dissolvemed
        An disgust "啊！"

    $ renpy.pause (0.5)
    Dm arrogant "啊。现在，这个问题是你的了。"
    if bangok_four_xdamion_store.peek_window == True:
        An disgust "达米恩。"
        Dm arrogant "什么？"
        An sad "我觉得我看到有人在门口--"
        scene white
        show bangok_four_labdoor
        with dissolve
        m "我蹲了下来，试图不要被发现，但听起来已经太迟了。"
        Dm face "我去查看。"
        show cgdamion at Pan((0, 100), (0, 150), 5.0) behind bangok_four_labdoor with dissolvemed
        m "我们的目光在窗户上相遇。他不可能没看到我。"
        Dm arrogant "你把该死的门开了一点。除此之外？没什么。"
        play sound "fx/door/doorclose.ogg"
        scene facin2 at Pan ((128, 250), (128, 250), 0.0) with dissolve
        m "他把门关上了，他的声音变得模糊了。"
        play sound "fx/steps/clean2.wav"
        m "我赶紧离开门口，不想被安娜发现我在偷看她和达米恩的亲热。"
    else:
        An sad "满意了吗，达米恩？"
        Dm "够满意了，我想。至少不会提到——"
        An sad "那就别压着我了。我需要去清理一下。"
        scene black with dissolve
        scene facin2 at Pan ((128, 250), (128, 250), 0.0) with dissolvemed
        m "我赶紧离开门口，看到达米恩从安娜身上下来，不想被发现偷看这种龙族的交配行为。"

    show anna sad at right with easeinright
    play sound "fx/door/doorclose.ogg"
    m "刚躲到一根柱子后面，我听到实验室那边的门关上了。"
    show anna sad flip with dissolve
    show anna sad with dissolve
    show anna sad flip with dissolve
    $ renpy.pause (0.3)
    hide anna with easeoutright
    m "安娜环顾四周，确认没有人看到她后，急匆匆地向卫生间跑去。"

    if bangok_four_xdamion_store.peek_window == True:
        $ renpy.pause (1.0)
        m "我在走廊里犹豫了一下。被抓到偷看之后，我还要继续调查雷扎的事吗？"
        menu:
            "去找达米恩谈谈。" :
                $ renpy.pause (0.5)
                play sound "fx/silence.ogg"
                queue sound "fx/knocking1.ogg"
                m "我走到实验室门口敲了敲门。"
                jump bangok_four_annaxdamion_talk_damion_caught
            "离开。" :
                play sound "fx/steps/clean2.wav"
                scene black with dissolveslow
                $ renpy.pause (0.5)
                m "虽然还有其他雷扎的线索可以追查，但如果必须进行那样的对话，我可能熬不过那份尴尬。"
                $ renpy.pause (0.5)
                scene town1 with dissolvemed
                jump chapter2sections

    else:
        $ renpy.pause (1.0)
        play sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/knocking1.ogg"
        m "等了一会儿，确保她走了之后，我走到实验室门口敲了敲门。"
        c "(安娜可能会忙一阵子。也许我可以问问这个达米恩关于雷扎的事...)"

label bangok_four_annaxdamion_talk_damion_notcaught:
    play sound "fx/door/door_open.wav"

    scene black with dissolve
    $ renpy.pause (0.5)

    show cgdamion at Pan((0, 0), (0, 302), 5.0) with dissolvemed
    $ renpy.pause(1.0)

    Dm arrogant "这么快就回来找安——"
    Dm face "哦。"

    scene facin2 at Pan ((128, 250), (128, 250), 0.0)
    show damion arrogant
    with fade

    $ metdamion2 = True
    $ persistent.metdamion = True

    Dm arrogant "有什么我能帮忙的吗？"
    c "你是达米恩，对吧？我有几个关于你实验室的问题。"
    Dm face "是的。我们这边的人通常在开始问问题之前会先做自我介绍。"
    c "你不知道我是谁吗？"
    Dm arrogant "哼，当然我知道你是谁，但这并不意味着你不需要学点礼貌。"
    Dm normal "我现在心情不错。所以说吧，你想问什么？"

    jump bangok_four_annaxdamion_canon_questions

label bangok_four_annaxdamion_talk_damion_caught:
    play sound "fx/door/door_open.wav"
    scene black with dissolve
    $ renpy.pause (0.5)
    show cgdamion at Pan((0, 0), (0, 302), 5.0) with dissolvemed
    $ renpy.pause(3.0)

    hide cgdamion
    scene facin2 at Pan ((128, 250), (128, 250), 0.0)
    show damion arrogant
    with fade

    $ metdamion2 = True
    $ persistent.metdamion = True

    Dm arrogant "哦，这不是那个偷窥的人类吗。"
    Dm arrogant "你得小心点。我不介意，但那个女人会大发雷霆。"
    Dm normal "我想这不是你来这里的本意吧。"
    c "你介意我问几个关于你实验室的问题吗？"
    Dm arrogant "你喜欢看我的那根东西，那你介意帮我含一下吗？"
    menu:
        "我可以。" :
            $ renpy.pause (0.5)
            Dm "我..."
            $ renpy.pause (0.5)
            show damion face with dissolve
            $ renpy.pause (0.4)
            Dm face "哈哈。非常搞笑。"
            jump bangok_four_annaxdamion_to_xdamion
        "我...我想？" :
            $ renpy.pause (0.5)
            label bangok_four_annaxdamion_to_xdamion:
            Dm arrogant "我开玩笑的。除非你真的认真。"
            menu:
                "接受。" :
                    show damion face with dissolve
                    $ renpy.pause (0.3)
                    Dm face "..."
                    $ renpy.pause (0.8)
                    Dm normal "去他的。进来吧。"

                    scene crapannalab:
                        zoom 1.2
                        anchor (0.5, 1.0)
                        pos (0.5, 1.0)
                    with wipeleft
                    play sound ["fx/door/hallwaydoor.ogg", "fx/door/lock.ogg"]
                    $ renpy.pause(0.5)

                    m "达米恩关上并锁上了通向走廊的门，然后把我推到实验台边，他的那根东西已经从他下体的裂缝里滑出来了。"

                    # NOTE: xdamion ws scenes not to be made accessible from this scene, per anna x damion cg commissioner wishes.

                    jump bangok_four_xdamion_fuck

                "拒绝。" :
                    Dm normal "那就别再浪费我的时间了。问你的问题吧。"
                    jump bangok_four_annaxdamion_canon_questions
        "你在搞什么鬼？" :
            pass
        "[[空白地盯着。]" :
            pass
    $ renpy.pause (0.8)
    Dm face "我开玩笑的，显然。"
    Dm normal "问你的问题吧。"

    jump bangok_four_annaxdamion_canon_questions


label bangok_four_annaxdamion_abort1:
    stop soundloop fadeout 1.0
    play sound "fx/steps/clean2.wav"
    show black with dissolvemed
    m "听到那种声音，我觉得不该打扰，于是我走过门口，没有往里面看，决定等实验室不那么忙的时候再来。"
    jump bangok_four_annaxdamion_abort_merge

label bangok_four_annaxdamion_abort2:
    stop soundloop fadeout 1.0
    play sound "fx/steps/clean2.wav"
    scene black with dissolvemed
    show facin2 behind black at Pan ((0, 250), (128, 250), 3.0) with None
    m "不想打扰他们的性交，我转身逃离了，想着等实验室不那么忙的时候再来。"
    jump bangok_four_annaxdamion_abort_merge


label bangok_four_annaxdamion_abort_merge:
    m "我在楼层里转了一圈。然而，简单的绕楼一圈花了相当长的时间，因为我遇到了死胡同，不得不下楼梯，在一堆通道中迷路才完成了这个圈。"
    hide black with dissolveslow
    m "最终，我回到了一个关好的实验室门前。"
    jump bangok_four_annaxdamion_return