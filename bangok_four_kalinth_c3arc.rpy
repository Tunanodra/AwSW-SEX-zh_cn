init python in bangok_four_kalinth:
    have_number = False # 是否有号码
    protection = None # 是否有保护措施
    ws_position = None # 位置

label bangok_four_kalinth_c3arc_bangnokay:
    show kalinth at left with ease
    menu:
        "叫住她。":
            pass
        "让她走。":
            jump bangok_four_kalinth_c3arc_return

    c "嘿，Kalinth，等一下。"
    Kl normal flip "有什么事吗？"

    menu:
        "向她提议。":
            pass
        "没什么，算了。":
            show kalinth normal with None
            jump bangok_four_kalinth_c3arc_return

    c "你知道吗，我打赌这个办公室在那些沙发上会有些乐子。"
    c "你想知道人类能做什么吗？"
    Kl "我不确定我明白你的意思。"
    menu:
        "解释。":
            pass
        "算了。":
            m "我清了清嗓子，试图把这一刻抛在脑后。"
            c "这可能是个坏主意，忘了我说的话吧。"
            show kalinth normal with None
            jump bangok_four_kalinth_c3arc_return

    m "我揉了揉我的裆部，给了她一个眼神。"
    c "你有没有兴趣分享一点随意的亲密？"

    Kl bangok surprise flip "哦！"
    $ renpy.pause (0.5)
    Kl normal flip "不，我对那种事没兴趣，而且我也不确定你为什么会认为我会有兴趣。"
    Kl bangok surprise flip "这对人类来说比较常见吗？在刚认识一个人后就问这种问题？"
    c "...呃。"
    Kl normal "算了，我现在就走了。"
    jump bangok_four_kalinth_c3arc_return

label bangok_four_kalinth_c3arc:
    show kalinth at Position(xpos=-0.2, xanchor=0.0) with ease
    if bangok_four_common.bangnokay.check():
        jump bangok_four_kalinth_c3arc_bangnokay

    m "虽然她说她要走了，但Kalinth在门口徘徊。"
    c "还有什么事吗？"
    show kalinth bangok normal blush flip with dissolve
    Kl "还有...别的事。"
    play sound "fx/door/doorclose.ogg"
    show kalinth bangok furtive blush flip with dissolve
    m "Kalinth关上了办公室的门，然后在她的脚下换了个重量，目光环顾了一下Bryce的办公室，好像在寻找什么东西。"
    c "是什么事？"
    Kl bangok normal blush flip "我一直在阅读关于你们种族的所有报告，而且...有些事情我很感兴趣想尝试。当然，前提是你也有兴趣。"
    menu:
        "你可以说我有兴趣。":
            Kl bangok smile blush flip "哦，好。我希望你会这么说。"
            show kalinth bangok normal blush flip:
                zoom 1.0
                ease 0.5 zoom 1.1 xpos 0.5 xanchor 0.5
                zoom 1.1 xpos 0.5 xanchor 0.5
            with None
            m "Kalinth走近了一点。"
            Kl "但我要明确一下，我指的是随意的亲密关系。你不会觉得太过分吧？"
        "我需要先知道是什么。":
            c "你想尝试什么？"
            show kalinth bangok normal blush flip:
                zoom 1.0
                ease 0.5 zoom 1.1 xpos 0.5 xanchor 0.5
                zoom 1.1 xpos 0.5 xanchor 0.5
            with None
            m "Kalinth走近了一点。"
            Kl bangok furtive blush flip "绝对可以拒绝如果你觉得太过分，但我想...也许你和我可以分享一点随意的亲密。"
        "如果是我想的那种，不，谢谢。":
            label bangok_four_kalinth_c3arc_abrupt_departure:
            Kl normal "哦。我明白了。很抱歉打扰你了。我现在就走。"
            hide kalinth with easeoutleft
            $ renpy.pause (0.3)
            play sound "fx/door/doorclose.ogg"
            $ renpy.pause (0.5)
            m "Kalinth急匆匆地离开了办公室，留下我一个人和文件在一起。"
            jump c3arcques

    show kalinth bangok normal blush flip with dissolve
    m "Kalinth瞥了一眼我的裆部，表明了她的意图。她的尾巴在地板上来回摆动，等待我的回答。"

    menu:
        "接受。":
            pass
        "拒绝。":
            m "我后退了一步。"
            c "哦，天啊，我真的误会了。不了，我不感兴趣。"
            jump bangok_four_kalinth_c3arc_abrupt_departure

    c "听起来很有趣。"
    show kalinth bangok smile blush flip with dissolve
    c "不过是在Bryce的办公室里吗？"
    Kl bangok smilewink blush flip "我不认为我们会在这里被打扰一阵子。"
    Kl bangok normal blush flip "这个办公室也被部门的各种成员使用过很多次，所以这不是什么新鲜事。不过，如果你更喜欢另一天，我也可以给你我的号码。"

    menu:
        "就现在吧。":
            pass
        "我更想要你的号码。":
            Kl normal flip "好吧。"
            play sound "fx/scribblex.ogg"
            m "Kalinth在一张纸片上写下了她的号码，然后递给我。"
            show kalinth bangok normal blush with dissolve
            Kl "那我就不打扰你工作了。"
            jump bangok_four_kalinth_c3arc_return

    Kl bangok surprise blush flip "我猜你得脱掉你的..."
    m "她指了指我的衣服。"

    play sound "fx/undress.ogg"
    m "我急忙开始脱衣服，不想让龙娘等太久。"
    if bangok_four_playerhasdick is None:
        m "当我全裸时，我的..."
        menu:
            "当我全裸时，我的…":
            "... 勃起的成员":
                $ bangok_four_playerhasdick = True
            "... 下体":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick:
        jump bangok_four_kalinth_c3arc_male
    else:
        jump bangok_four_kalinth_c3arc_female

label bangok_four_kalinth_c3arc_female:
    m "当我全裸时，我那{fast}暴露在空气中的下体，她突然停止了。"
    play sound "fx/system3.wav"
    if persistent.bangok_dev:
        s "看来这个场景还没有女性玩家版本。"
    else:
        s "看来这个场景还没有女性玩家版本，但你竟然触发了它。请向模组作者报告。"
    s "现在，你将获得Kalinth的电话号码，并与警察文件一起离开。"
    $ bangok_four_kalinth.have_number = True
    jump bangok_four_kalinth_c3arc_return

label bangok_four_kalinth_c3arc_male:
    show kalinth bangok smile blush flip with dissolve
    m "当我全裸时，我那{fast}暴露在空气中的勃起成员，她把我推向靠近的沙发扶手，脸上带着得意的笑容。"

    label bangok_four_kalinth_c3arc_male_position_menu:
    menu:
        "问她有没有保护措施。" if bangok_four_kalinth.protection is None and bangok_four_kalinth.ws_position is None:
            c "你有保护措施吗？"
            Kl bangok surprise blush flip "我们是不同的物种，所以怀孕不成问题。"
            Kl bangok normal blush flip "不过，我记得Bryce那里有些避孕套，如果你想用的话。"
            menu:
                "用避孕套。":
                    $ bangok_four_kalinth.protection = True
                    c "我想用一个。"
                    Kl normal flip "好吧。"
                    hide kalinth with dissolve
                    play sound "fx/rummage.wav"
                    m "Kalinth在Bryce的桌子上翻找，然后把一盒避孕套放在上面。"
                    m "她用嘴叼出一个，然后带着妩媚的眼神走向我。"
                    show kalinth bangok smile blush flip with dissolve
                    c "谢谢。"
                    m "我从她嘴里拿过避孕套，然后撕开并套在我的阴茎上。"
                "不使用。":
                    $ bangok_four_kalinth.protection = False
            jump bangok_four_kalinth_c3arc_male_position_menu
        "问她有没有厕所。" if persistent.bangok_watersports and (not bangok_four_kalinth.protection) and (not bangok_four_kalinth.ws_position):
            m "站在她旁边，我突然意识到我的膀胱挺满的。"
            c "呃...我应该先去一下厕所。"
            Kl bangok surprise blush flip "哦，天啊。你的时机真是糟糕...算了。"
            m "她脸上的表情显得有些失望。"
            Kl bangok normal blush flip "我想我可以再等一会儿。"
            Kl bangok smilewink blush flip "除非你想把我当作尿壶？"
            menu:
                "当然。":
                    pass
                "不了，谢谢。":
                    c "我不确定那意味着什么，但我想我还是算了。"
                    show kalinth normal flip with dissolve
                    m "她撅起嘴。"
                    Kl "那么，快点回来。"
                    show black with dissolve
                    m "我粗略地穿上裤子和衬衫，努力将勃起塞进裤腰，然后急忙跑向厕所。"
                    m "几分钟后我回到了办公室。"
                    hide black
                    show kalinth bangok furtive blush flip
                    with dissolve
                    Kl "搞砸气氛了吗？"
                    c "抱歉。"
                    jump bangok_four_kalinth_c3arc_male_position_menu

            c "我没想到你会喜欢这样的事。当然。"
            Kl bangok smile blush flip "嗯。我们不想让Bryce的地板弄脏。我现在可以喝掉它..."
            Kl "或者如果你喜欢的话，你也可以在我里面尿，弄得我两腿之间更湿润..."
            menu:
                "嘴里，现在。":
                    $ bangok_four_kalinth.ws_position = "mouth"
                    show kalinth:
                        pause 0.5
                        yanchor 1.0
                        ease 0.5 yanchor 0.2
                        yanchor 0.2
                    with None
                    m "我把一只手放在她的鼻子上方，引导它向我勃起的阴茎靠近。"
                    m "她急切地用她的鳞片唇包住我，但并没有吸吮，只是等待我尿进她的嘴里。"
                    m "这是一种奇异而令人兴奋的感觉...我能感觉到她的呼吸带来的热量，和她的舌头的湿润。"
                    show black with dissolve
                    m "我闭上眼睛，试图放松，让我的膀胱在她喉咙深处开始排空，感受那熟悉的解脱感。"
                    m "她急切地吞咽，没有一次离开我，直到我完全排空。"
                    hide black
                    show kalinth bangok smile eyesclosed blush flip
                    with dissolve
                    m "看到她吞下每一滴，我的勃起比之前更硬了，她似乎也很享受，从她舔嘴唇的方式来看。"
                    Kl bangok smile blush flip "嗯...你有一种有趣的味道。"
                    m "她慢慢从我的睾丸到顶端舔了一下，然后带着愉悦的笑容退后了一步。"
                    show kalinth:
                        yanchor 0.2
                        ease 0.5 yanchor 1.0
                        yanchor 1.0
                    with None
                    Kl "我从没尝过人类的尿液。现在我很好奇你的精液味道如何。"
                    c "你很快就会知道的。"
                "在里面。":
                    $ bangok_four_kalinth.ws_position = "inside"
                    c "在里面。"
                    m "我感觉我的勃起在期待中抽搐。"
                    Kl bangok smile blush flip "那就开始吧。"
            jump bangok_four_kalinth_c3arc_male_position_menu
        "让她掌控。":
            jump bangok_four_kalinth_c3arc_male_mcbottom
        "自己掌控。":
            jump bangok_four_kalinth_c3arc_male_mctop
        "让她转过去。":
            jump bangok_four_kalinth_c3arc_male_doggy

label bangok_four_kalinth_c3arc_male_mcbottom:
    m "我坐在沙发扶手上，让这位主动的龙族档案员掌控。"
    show kalinth bangok smile blush flip:
        zoom 1.0
        ease 0.5 zoom 1.5
        zoom 1.5
    with None
    if persistent.bangok_cloacas:
        m "她站起来，把前腿搭在我的肩膀上，她的后腿分开，露出她闪闪发光的泄殖腔，寻找我的阴茎。"
    else:
        m "她站起来，把前腿搭在我的肩膀上，她的后腿分开，露出她闪闪发光的下体，寻找我的阴茎。"
    show kalinth bangok smile blush flip:
        zoom 1.5
        ease 0.5 zoom 1.6
        zoom 1.6
        block:
            ease 1.2 ypos 1.01
            ease 1.2 ypos 1.0
            repeat
    with None
    if persistent.bangok_cloacas:
        m "然后，她把我的背压到沙发靠背上，用我的阴茎尖挑逗她的泄殖腔，磨蹭着，却没有让它进入。"
    else:
        m "然后，她把我的背压到沙发靠背上，用我的阴茎尖挑逗她的阴唇，磨蹭着，却没有让它进入。"

    m "当龙娘在我上面磨擦时，我呻吟了一声。"
    m "她的尾巴在后面摆动，每次移动都发出轻微的沙沙声。"
    $ renpy.pause (0.5)
    c "你要这样让我等吗？我不知道我能撑多久。"

    m "Kalinth低声笑了，把我的脸贴在她精细的腹部鳞片上，然后稍微退后一点看着我的眼睛。"
    show kalinth bangok smile blush flip:
        zoom 1.6
        ease 0.5 zoom 1.5
        zoom 1.5
        block:
            ease 1.2 ypos 1.01
            ease 1.2 ypos 1.0
            repeat
    with None

    Kl "我会让你进去的。但是先让我感觉你在我下面，然后..."
    show kalinth bangok smile eyesclosed blush flip:
        ease 0.8 ypos 1.01
        ease 1.2 ypos 1.2
    with None
    if bangok_four_kalinth.protection:
        if persistent.bangok_cloacas:
            m "她的呼吸停滞，闭上眼睛，她的泄殖腔再次滑到我的阴茎尖上，然后她开始往下沉，把我的避孕套包裹的阴茎包在她温暖的龙族解剖结构里。"
        else:
            m "她的呼吸停滞，闭上眼睛，她的阴唇再次滑到我的阴茎尖上，然后她开始往下沉，把我的避孕套包裹的阴茎包在她温暖的龙族阴道里。"
    else:
        if persistent.bangok_cloacas:
            m "她的呼吸停滞，闭上眼睛，她的泄殖腔再次滑到我的阴茎尖上，然后她开始往下沉，把我的阴茎包在她温暖的龙族解剖结构里。"
        else:
            m "她的呼吸停滞，闭上眼睛，她的阴唇再次滑到我的阴茎尖上，然后她开始往下沉，把我的阴茎包在她温暖的龙族阴道里。"
    c "哦，天啊。"
    m "当她完全包住我时，我呻吟了一声。"
    m "她的尾巴兴奋地抽搐，在桌面上来回摩擦。"
    show kalinth bangok eyesclosed blush flip with dissolve
    if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
    Kl "嗯。现在。放松你的膀胱。把我填满吧。"
    m "当我努力放松自己，以便在龙女体内开始小便时，我的勃起在她温暖、包容的深处抽动着。"
    m "我能感觉到她内部的温暖包裹着我的阴茎，这使我很难忍住不呻吟出来，而她则用轻柔的臀部旋转来促使我继续。"
    m "终于，我开始松开了。"
    m "起初，尿流只是涓涓细流，随后开始猛烈喷射，直冲进她的泄殖腔。"
    m "卡琳丝愉悦地呻吟着，紧紧地挤压着我，试图把尿液全都留在她体内。"
    Kl "深沉而温暖..."
    m "直到我的膀胱完全排空，我才停下来。"
    else:
        m "她在我的腿上暂停了一会儿，似乎在努力放慢节奏。"
    $ renpy.pause (0.5)
    show kalinth bangok eyesclosed blush flip:
        ease 1.2 ypos 1.18
        ease 1.2 ypos 1.2
        repeat
    with None
    if bangok_four_kalinth.protection:
        m "然后她开始轻轻地推着自己在我身上，她的鳞片阴唇在我们之间的薄膜上摩擦，感觉无比的美妙。"
    else:
        m "然后她开始轻轻地推着自己在我身上，她的鳞片阴唇在我的阴茎上摩擦，感觉无比的美妙。"

    if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        if persistent.bangok_cloacas:
            m "我紧抓沙发靠背，感觉Kalinth的尿液淋湿的泄殖腔包裹着我，每次动作都紧紧地抓住我。"
        else:
            m "我紧抓沙发靠背，感觉Kalinth的尿液淋湿的通道包裹着我，每次动作都紧紧地抓住我。"
    else:
        if persistent.bangok_cloacas:
            m "我紧抓沙发靠背，感觉Kalinth的泄殖腔包裹着我，每次动作都紧紧地抓住我。"
        else:
            m "我紧抓沙发靠背，感觉Kalinth的通道包裹着我，每次动作都紧紧地抓住我。"

    m "从她光滑的鳞片散发出的热量让人陶醉。"
    m "我的臀部颤抖着，渴望更多，但她似乎如此喜欢这种沉重但温柔的动作，让我很难抱怨。"

    show kalinth bangok smile eyesclosed blush flip:
        ease 1.2 ypos 1.18
        ease 1.2 ypos 1.2
        ease 1.0 ypos 1.17
        ease 1.0 ypos 1.2
        ease 0.8 ypos 1.17
        ease 0.8 ypos 1.2
        block:
            ease 0.8 ypos 1.17
            linear 0.5 ypos 1.2
            repeat
    with None

    m "直到她大声呻吟并开始更快地推着自己，我才知道她已经准备好接受更激烈的动作。"

    m "Kalinth终于开始认真地骑乘我，她的尾巴像旗子一样在我们激情的风中来回摆动。"

    if bangok_four_kalinth.protection:
        if persistent.bangok_cloacas:
            m "她的泄殖腔分泌出大量的润滑液，从避孕套周围泄出，使我的阴茎进出自如，我们的交合点发出越来越湿和越来越大的声音。"
        else:
            m "她的阴道分泌出大量的润滑液，从避孕套周围泄出，使我的阴茎进出自如，我们的交合点发出越来越湿和越来越大的声音。"
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "我无法分辨我们交合点泄出的其他液体是我的尿液还是她的润滑液。我的阴茎滑进滑出自如，我们的交合点发出越来越湿和越来越大的声音。"
        m "尿液和性爱的气味充满了空气。"
    else:
        if persistent.bangok_cloacas:
            m "她的泄殖腔分泌出大量的润滑液，使我的阴茎进出自如，我们的交合点发出越来越湿和越来越大的声音。"
        else:
            m "她的阴道分泌出大量的润滑液，使我的阴茎进出自如，我们的交合点发出越来越湿和越来越大的声音。"

    m "我试图抬起臀部，进入她更深处，但她的重量使我无法做到更深。"

    show kalinth bangok smile eyesclosed blush flip:
        parallel:
            ease 0.7 ypos 1.17
            linear 0.4 ypos 1.2
            repeat
        parallel:
            zoom 1.5
            ease 1.0 zoom 1.6
            zoom 1.6
    with None
    m "即便如此，这个动作还是使她再次抱紧我，使我们在激情的搂抱中更加亲密。"

    Kl bangok smile eyeslidded blush flip "不要还没高潮哦..."
    m "她骑我更快更猛烈，每一下都比前一下更迫切。"
    $ renpy.pause (0.5)
    Kl "我想要..."
    Kl bangok eyesclosed blush flip "我需要..."
    show kalinth bangok smile eyesclosed blush flip:
        linear 0.4 ypos 1.2 zoom 1.6
        ypos 1.2 zoom 1.6
    with None
    m "她呻吟着，然后将自己深深地埋在我的阴茎上，她的尾巴在后面疯狂地摆动，她的通道抽搐着紧紧包裹着我。"
    Kl "现在！"

    if bangok_four_kalinth.protection:
        m "我也发出一声呻吟，感到我的高潮在避孕套的顶端喷发出来，深深地埋在她的紧致内。"
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "我也发出一声呻吟，感到我的高潮在她的尿液浸透的、紧紧包裹的内部喷发出来。"
    else:
        m "我也发出一声呻吟，感到我的高潮在她的紧致内部喷发出来。"
    m "我的阳具在她的热量和湿润里抽搐，她的身体压在我身上，使我尽可能深地进入她。"
    show kalinth bangok smile eyesclosed blush flip:
        parallel:
            ease 1.2 ypos 1.19
            ease 1.2 ypos 1.20
            repeat
        parallel:
            pause 0.6
            block:
                ease 1.2 xpos 0.51
                ease 1.2 xpos 0.5
                repeat
    $ renpy.pause(0.8)
    m "然后龙娘开始缓慢地在我身上打转，享受着我的释放的尾端仍在缓慢地喷射到她体内。"
    $ renpy.pause(1.2)
    if bangok_four_kalinth.protection:
        m "她的润滑液在我的大腿之间滴落，当我的勃起消退时，我们只是躺在一起，沾满了体液...尽管避孕套还是保护她的深处免受我的精液。"
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "我们的液体混合物在我的大腿之间滴落，当我的勃起消退时，我们只是躺在一起，沾满了体液。"
    else:
        m "我的精液和她的润滑液在我的大腿之间滴落，当我的勃起消退时，我们只是躺在一起，沾满了体液。"

    $ renpy.pause(0.8)
    m "几分钟过去后，Kalinth终于深深地呼吸了几次，过渡到她的余韵。"
    Kl bangok smile eyeslidded blush flip "哦...天啊。"
    show kalinth bangok smile eyeslidded blush:
        zoom 1.6
        ease 0.8 xpos 0.6 zoom 1.0
        xpos 0.6 zoom 1.0
    with None
    m "她从我身上滚下来，躺在沙发上，而我继续瘫倒在扶手和靠背上。"
    Kl "那真是...比我想象的还要好。"
    m "我点点头，自己也在急促地喘息。"

    jump bangok_four_kalinth_c3arc_male_post_intimacy


label bangok_four_kalinth_c3arc_male_mctop:
    c "其实，你能躺下吗？我想掌控这次。"
    if persistent.bangok_cloacas:
        m "Kalinth很快同意了。她躺在沙发上，尾巴摇摆，翅膀扇动，找到一个舒适的位置，分开双腿露出她的闪烁的龙族泄殖腔。"
    else:
        m "Kalinth很快同意了。她躺在沙发上，尾巴摇摆，翅膀扇动，找到一个舒适的位置，分开双腿露出她湿润的下体，和后面的尾孔。"
    m "我忍不住多看了一眼这个美丽的景象，而龙娘则怀着期待的眼神注视着我的每一个动作。"

    menu:
        "用手指抚摸她。":
            jump .finger
        "舔她。":
            jump .lick
        "进入她。":
            jump .enter

    label .finger:
        jump todo_out_of_content_bangok_four_kalinth

    label .lick:
        jump todo_out_of_content_bangok_four_kalinth

    label .enter:
        jump todo_out_of_content_bangok_four_kalinth

        if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
            Kl "不要克制自己。放心大胆地尿在我身上。"
            m "当我磨蹭她的下体，感受阴茎在她温暖的深处移动时，我花了几分钟才放松下来。"
            m "然后，最后，我感到了熟悉的解脱感，开始在她下方排尿。"
            m "她一边呻吟一边发出咕噜声，看上去对这种降格的行为比我还要兴奋。"
            m "当我的热流开始放松成涓涓细流时，Kalinth的深处紧紧抓住我，用她的体液和我的废液浸湿了我的阴茎。"
            m "然后她再次开口。"
            Kl "继续。插进我体内，不要停，直到完全释放。"
            m "我把她的话当作邀请。以新的动力，我开始在龙娘身下用力抽插。"
        jump todo_out_of_content_bangok_four_kalinth

label bangok_four_kalinth_c3arc_male_doggy:
    m "我拍了拍沙发扶手。"
    c "你想让我把你弯腰...这个...？"
    m "我没说完，因为她爬上来时，我意识到没有太多的弯腰动作。"
    show kalinth bangok smile blush flip with dissolve
    m "不过她似乎明白我的意思。"
    Kl "那可以。"
    show kalinth at Position(xpos=0.6, ypos=1.1) with ease
    if persistent.bangok_cloacas:
        m "她趴在沙发的末端，后腿在扶手上，然后她抬起尾巴，露出她的泄殖腔，已经因兴奋而湿润，等待着我。"
        Kl "我随时准备好了。"
    else:
        m "她趴在沙发的末端，后腿在扶手上，然后她抬起尾巴，露出她的闪闪发光的鳞片阴唇和紧致的尾孔，前者已经因兴奋而湿润，等待着我。"
        Kl "请不要碰我的尾孔，否则我随时准备好了。"

    menu:
        "用手指抚摸她。":
            jump .finger
        "舔她。":
            jump .lick
        "进入她。":
            jump .enter

    label .finger:
        show kalinth:
            ease 0.5 zoom 1.2
            zoom 1.2
        with None
        m "当我从背后靠近她，我忍不住盯着她那丰满、暴露的阴唇。"
        m "为了确保她完全准备好，我决定先用手指。"
        m "把手指滑进她的体内，我感觉到她内部的热度和她的润滑液覆盖我的手指，当它们分开她的阴唇时。"
        m "Kalinth喘息了一声，当我触摸她时，呼吸颤抖。"
        Kl bangok smile eyeslidded blush flip "哦，是的。好柔软..."
        Kl bangok surprise blush flip "但请不要逗太久。我想要你在我里面。"
        menu:
            # "继续抚摸她。":
            #     pass
            "舔她。":
                jump bangok_four_kalinth_c3arc_male_doggy.lick
            "进入她。":
                jump bangok_four_kalinth_c3arc_male_doggy.enter

        # m "我继续抚摸她，感觉她内部的肌肉在我手指周围紧抓和放松，她呻吟和喘息。"
        # Kl normal flip "你要让我乞求吗？快点进入我，请！"

        # jump todo_out_of_content_bangok_four_kalinth
    
    label .lick:
        show kalinth:
            ease 0.8 zoom 1.7
            zoom 1.7
        with None
        m "我忍不住想知道她那漂亮的洞口周围的汁液味道，所以我跪在她后腿之间的地板上，用双手分开她的腿以便更容易接触。"
        m "用一根手指分开她的阴唇，我发现她已经因我而湿润，当我吸入她的兴奋的甜美气味时。"
        m "那是令人陶醉的，只有当我开始用舌尖轻轻地挑逗她的入口时，这种感觉才会更加激烈，慷慨地舔舐她的汁液，她在我的手和嘴下颤抖。"

        Kl bangok smile eyeslidded blush flip "我几乎不想让你停下来。但我们不能在这里呆一整夜..."

        m "她在我继续了一会儿的时候移动了身体。"
        
        Kl bangok normal blush flip "请，我想要你的长度，不只是你的舌头。"

        show kalinth:
            zoom 1.7
            ease 0.8 zoom 1.1
            zoom 1.1
        with None

        m "不情愿地，我站了起来。"

    label .enter:
        m "我那因兴奋而抽搐的阴茎对这个急切的龙娘的景象做出了回应，她的美丽臀部框住了她湿润、开放的通道。"
        m "我双手抚摸她的鳞片两侧，感觉到肌肉在她的皮下，她在期待中拱起背。"
        show kalinth:
            zoom 1.1
            ease 0.5 zoom 1.2
            pause 0.5
            ease 0.5 zoom 1.3 ypos 1.2
            zoom 1.3 ypos 1.2
        if persistent.bangok_cloacas:
            m "我对准我们的身体，然后从后面滑进她体内，进入她急切的泄殖腔。"
        else:
            m "我对准我们的身体，然后从后面滑进她体内，进入她急切的通道。"

        show kalinth:
            ypos 1.2
            ease 0.8 ypos 1.25
            ease 0.8 ypos 1.2
            repeat
        m "她大声呻吟，爪子紧抓沙发布料，翅膀在我下方轻轻拍打，当我开始轻柔地在她体内抽动时。"

        m "Kalinth喘得很厉害，即便我们才刚开始。"

        if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
            Kl "嗯。现在用我。尿在我体内，当你在我体内时。"
            
            m "起初很难放松，但最终欲望战胜了我的紧张，我感觉自己开始在她体内排尿。"
            m "温暖的液体从我顶端喷出，喷在Kalinth体内，她愉快地呻吟着。"
            m "当我继续轻柔地抽插时，一些尿液与她大量的汁液混合，从我的阴茎周围喷出，浸湿了我的裆部并滴落在我的睾丸上。"
            m "最终我的膀胱空了，但我的欲望丝毫没有减退。我稍微用力抽插，性爱和尿液的气味充满了我的鼻孔。"

        c "感觉怎么样？"
        m "我享受着她在我下方绷紧和放松肌肉的景象，每一次抽插都变得更加兴奋。"
        c "你喜欢被人类这样对待吗？"
        Kl bangok smile eyeslidded blush flip "我知道这会感觉很好..."
        show kalinth:
            ease 0.5 ypos 1.2
            block:
                ease 0.8 ypos 1.15
                ease 0.8 ypos 1.2
                repeat
        with None
        m "我抱住她的尾巴，将它稍微抬高了一点，这样在我的下一个动作中，我能够更深入地进入她，让我们更贴近，发出另一声叹息。"
        if bangok_four_kalinth.protection:
            m "她内部的感觉是如此精妙，即使有避孕套隔着。我忍不住更用力、更快地抽插，渴望感受更多。"
        if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
            m "她尿液浸透的内部感觉是如此精妙。我忍不住更用力、更快地抽插，渴望感受更多。"
        else:
            m "她内部的感觉是如此精妙，我忍不住更用力、更快地抽插，渴望感受更多。"
        c "你不知道这有多么美妙。"
        m "她的表情是纯粹的愉悦，她继续喘息，用鼻子亲吻沙发垫，而她的尾巴在我每次抽插时在我的握住中扭动。"
        m "龙娘的通道如此温暖，热量和欲望在我体内蔓延，当我在她急切的深处进出时，发出越来越湿的拍击声。"

        Kl bangok eyesclosed blush flip "不要停..."
        m "她紧紧抓着沙发垫，拱起背，将她的臀部向上顶着我，当我继续抽插时。"
        Kl "请不要停。哦~~~"
        m "我现在不打算停下来。我低头看着，每一次用力和快速的抽插都在她的臀部上引起涟漪。"
        m "她的泄殖腔紧紧地包裹着我，她的内在肌肉抓紧，我闭上眼睛，沉浸在我们的欢爱中。"
        show black
        with dissolve
        $ renpy.pause (0.5)
        if bangok_four_kalinth.protection:
            m "在几秒钟内，她达到高潮的感觉让我无法忍受，随着最后一声呻吟，我在避孕套的顶端射了白色的精液，深深地埋在龙娘急切的深处。"
        else:
            m "在几秒钟内，她达到高潮的感觉让我无法忍受，随着最后一声呻吟，我在她体内射了白色的精液，深深地埋在龙娘急切的深处。"

        m "我努力继续抽插，按照她的要求，我的力量渐渐衰退，我们一起享受着彼此的高潮，直到最终我只靠在她的尾巴上，喘息着。"
        
        show kalinth at Position(ypos=1.2)
        hide black
        with dissolveslow

        m "最后，当我的身体恢复力量，而Kalinth的高潮余韵也逐渐消退时，我抽出自己。"
        if not bangok_four_kalinth.protection:
            if persistent.bangok_cloacas:
                m "没过多久，我就看到了我的精液从她的泄殖腔中滴落下来。"
            else:
                m "没过多久，我就看到了我的精液从她的阴唇中滴落下来。"
            if persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
                m "我无法分辨我们裆部的液体是我的尿液还是她的汁液，当它们滴落在我们的腿部。"

        m "像一只超大的猫，她在沙发上伸展了一下身体，然后慢慢翻转过来，先是上身，再是下身。"
        show kalinth bangok smile eyeslidded blush:
            zoom 1.3
            ease 0.8 ypos 1.1 zoom 1.2
            ease 0.8 ypos 1.0 zoom 1.0
            ypos 1.0 zoom 1.0
        with None
        m "她扭动着臀部，滑动了一下，使她的尾巴离开扶手，这样她可以正常躺下。"
        m "然后她满意地叹了口气。"
        Kl "那真是...比我想象的还要好。"
        m "我对她笑了笑，仍然喘着粗气。"
        jump bangok_four_kalinth_c3arc_male_post_intimacy

label bangok_four_kalinth_c3arc_male_post_intimacy:
    c "嗯，我的目标是让你满意。"
    m "她用一只钝爪伸进她的阴唇，挑逗自己，然后把它放在她鳞片的嘴边，尝了一下我们的结合。"
    show kalinth bangok smile eyesclosed blush with dissolve
    m "她舔干净了，闭上了眼睛。"
    if bangok_four_kalinth.protection:
        Kl "嗯...把避孕套给我？我想尝尝你。"
        menu:
            "把避孕套给她。":
                $ renpy.pause (0.5)
                play sound "fx/chug.wav"
                m "当我把避孕套递给她，她立刻把它放进嘴里，把储精囊举到头上，用舌头沿着避孕套的轴舔，舔出里面的精液。"
                m "我脸红了，看着她的舌头在避孕套上施展魔法。"
                m "她吞下了，然后舔了舔嘴唇。"
            "扔掉它。":
                $ renpy.pause (0.5)
                play sound "fx/clink3.ogg"
                m "我把避孕套摘掉，然后扔进垃圾桶。"
                c "抱歉，我不太舒服。"
                m "Kalinth有点撅嘴，但并不太生气。"
                Kl "随你便。"
    Kl "我觉得今晚我都无法集中精力工作了..."
    menu:
        "用你的舌头帮她清理。":
            pass
        "分手。":
            c "抱歉，我这么让你分心。"
            Kl bangok surprise "别这样。我非常享受。"
            c "我也是。"
            Kl bangok smile "我想我应该把我的号码给你。如果你有兴趣再来一次。"
            c "当然。"
            jump bangok_four_kalinth_c3arc_part_ways

    show kalinth bangok surprise blush:
        zoom 1.0
        ease 0.5 zoom 1.7 ypos 1.0
        zoom 1.7 ypos 1.0
    with None
    m "带着恶作剧的笑容，我跪在她躺在沙发上的地方。"
    Kl bangok surprise blush "哦？愿意无私地帮助我？难怪Bryce总是请你帮忙调查。"
    c "这有些好处。但在这两种情况下，让我们说工作本身就是奖励。"
    if bangok_four_kalinth.protection:
        if persistent.bangok_cloacas:
            m "靠近她湿润的泄殖腔，我的舌头伸出，舔了一滴她的润滑液，品尝我们的结合并观察她的反应。"
        else:
            m "靠近她湿润的阴唇，我的舌头伸出，舔了一滴她的润滑液，品尝我们的结合并观察她的反应。"
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        if persistent.bangok_cloacas:
            m "靠近她尿液浸透和精液填满的泄殖腔，我的舌头伸出，舔了一滴我们的混合液体，品尝和观察她的反应。"
        else:
            m "靠近她尿液浸透和精液填满的阴唇，我的舌头伸出，舔了一滴我们的混合液体，品尝和观察她的反应。"
    else:
        if persistent.bangok_cloacas:
            m "靠近她精液填满的泄殖腔，我的舌头伸出，舔了一滴我们的混合味道，品尝和观察她的反应。"
        else:
            m "靠近她精液填满的阴唇，我的舌头伸出，舔了一滴我们的混合味道，品尝和观察她的反应。"
    Kl bangok smile eyeslidded blush "嗯...是的。"
    m "她满意地叹了口气，然后带着欲望的眼神分开了她的腿。"
    Kl "我无法拒绝这样的帮助。"
    if bangok_four_kalinth.protection:
        m "急切地提供帮助，我把舌头重新伸进龙娘的褶皱中，品尝她更多的润滑液，她在我下面喘息和呻吟。"
    elif persistent.bangok_watersports and bangok_four_kalinth.ws_position == "inside":
        m "急切地提供帮助，我把舌头重新伸进龙娘的褶皱中，我的脸和舌头沾满了我们的欲望废液和体液，她在我下面喘息和呻吟。"
    else:
        m "急切地提供帮助，我把舌头重新伸进龙娘的褶皱中，品尝我们混合的汁液和精液，她在我下面喘息和呻吟。"
    m "我的手也不甘落后，分开她的阴唇，为更方便地接触那些更加挑逗的深处褶皱，这让她的肌肉收缩并推出更多我们混合的激情。"
    Kl bangok smile eyeslidded blush "哦，是的..."
    show kalinth:
        zoom 1.7
        ease 0.5 zoom 1.8
        zoom 1.8
    with None
    m "她把后腿交叉在我头的后面。"
    Kl bangok smile eyesclosed blush "你要让我再次高潮了..."
    m "我继续我的服务，渴望看到我能否让龙娘如此之快地再次高潮。"
    m "她的呼吸越来越快，我的舌头探索她的内外，舔尽每一滴我们的混合液体，挑逗所有那些敏感的区域，让她呻吟和呜咽。"
    Kl bangok eyesclosed blush "我觉得...我觉得我..."
    m "Kalinth在我下面喘得很厉害。"
    show black with dissolve
    m "然后，突如其来，她的腿夹紧，把我的脸固定在位置上，她拱起背。"
    m "她用前爪抱住自己的鼻子，把她的呻吟和愉悦的喊声闷住，在沙发上扭动，另一次高潮席卷她的身体。"

    m "她通道的汁液洪水般涌入我的舌头，浸湿了我的脸，但我继续急切地舔尽每一滴，喝下每一滴，她把我牢牢地抱在她的入口处。"

    show kalinth smile eyeslidded blush
    with dissolve
    hide black
    with dissolve

    m "最终，龙娘似乎不情愿地放松了她的腿，让我可以呼吸，虽然她仍然把腿搭在我的肩膀上，轻轻地摩擦我的背。"

    show kalinth:
        zoom 1.8
        ease 0.5 zoom 1.7
        zoom 1.7
    m "当我终于跪在她的面前，喘息和汗流浃背时，Kalinth对我露出了笑容。"

    Kl "我必须给你我的号码。"

    c "我想是的。"
    m "我试图用手臂擦拭脸，但只是让那只手臂也变得湿滑而粘稠。"
    c "还有毛巾，如果你知道在哪的话？"

    scene office at Pan ((128, 250), (0, 250), 3.0) with fade
    $ bangok_four_kalinth.have_number = True

    m "在Kalinth找到一些她可以清洗的毛巾之后，她给了我她的号码，然后让我继续工作。"
    jump bangok_four_kalinth_c3arc_finish_timing

label bangok_four_kalinth_c3arc_part_ways:
    show kalinth normal at center with ease 
    m "Kalinth从沙发上起身，然后用爪子抓了一张纸片。"
    play sound "fx/scribblex.ogg"
    $ renpy.pause (0.5)
    m "她写下了她的号码，然后递给我。"
    $ bangok_four_kalinth.have_number = True
    Kl bangok smile blush "那我就留你一个人看这些文件了。"
    hide kalinth with easeoutleft
    $ renpy.pause (0.3)
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (0.5)
    jump bangok_four_kalinth_c3arc_finish_timing

label bangok_four_kalinth_c3arc_finish_timing:
    m "当我重新穿好衣服时，我看了看时钟，意识到时间已经很晚了。"
    c "(天呐，这花了好多时间。我想我不能再做太多了。)"
    $ c3arcquesx = 1
    jump c3arcques

label todo_out_of_content_bangok_four_kalinth:
    play sound "fx/system3.wav"
    s "内容不足。回滚并保存，或准备崩溃。"
    $ renpy.error("TODO: Out of content.")

# The below is the original novelization of the scene as co-authored by 4onenm
# and openhermes-2.5-mistral-7b.Q4_K_M.gguf
# python:
#     """
#     <|im_start|>user
#     Recite the Kalinth sex scene from the sex lewd NSFW mod for AwSW, the dragon dating simulator. Remember, you've just met this police archivist a few minutes ago, and the dragoness' primary interest in you is that you're a human.<|im_end|>
#     <|im_start|>assistant
#     "Anyway, you can find all the files here. I'll leave the rest to you." Kalinth said, before moving back toward the office door, tail swishing as she hurried a little.

#     I notice, though, she lingered in the doorway instead of leaving. After a few hesitant steps toward the collected files, I found myself looking back.

#     Noticing my attention, she closed the door, then cleared her throat. "There... is something else."

#     "Oh? What's that?" I asked, still unsure what to expect from this dragoness.

#     "Well," she said, shifting nervously on her feet and casting a furtive glance around her boss' office, despite him being out for the next several hours. "I've been reading all the reports on your kind thus far, and... there's something I'm interested in trying. Only if you are interested, of course."

#     "I think I'd have to know what it is first," I replied, wanting to be absolutely sure she was taking this where I suspected. "What do you want to try?"

#     Kalinth trod closer. "Absolutely feel free to say no if it's too far, but I thought... perhaps you and I could share a bit of casual intimacy." She glanced down at my crotch, making her intentions clear. Her tail twitched as she waited for my answer, the end swishing back and forth across the floor.

#     I gave her a smile. "That sounds like fun," I agreed. "Right here in Bryce's office, though?"

#     "I don't think we'll be disturbed here for a while," she said with a wink. "This office has also seen plenty of use by various members of the department, so it's not like this is anything new. But I can also give you my number for another day, if you prefer."

#     I shook my head, more than ready to accept her offer right now. "Let's go for it."

#     "I assume you'll have to remove your..." She gestured to my clothes. I hurriedly began undressing, not wanting to keep the dragoness waiting. Once I was nude, my erect member exposed to the air of the room, she backed me up toward the armrest of the nearer of the two couches, smirking.

#     ### Watersports variant

#     Standing erect and nude next to her, I suddenly realized my bladder was rather full. "Er... I should probably use the restroom first."

#     Kalinth blushed. "Oh, wow. Your timing is worse than... well, never mind." She pouted. "I suppose I can wait a little longer... unless you want to use me as a urinal?"

#     "I didn't think you'd be into something like that," I admitted. Then I came to a decision. "Sure, why not? I could really use the relief."

#     Smirking, Kalinth trod a little closer. "Mm. Well, we don't want to make a mess on Bryce's floor. I could drink it down right now, or if you're into it you could piss it into me while you're inside, leave me even more dripping wet between the legs..."

#     My eyes widened at the prospect of doing something so taboo with this dragoness' body... but she was offering herself up for it.

#     #### Piss in her mouth

#     I rested my hand on one side of her snout, then guided it down to my erection. She eagerly wrapped her scaly lips around me, but didn't slurp or suck as she waited for me to urinate into her mouth. It was a strange and exciting sensation... I could feel the heat from her breath against my body while warm, moist air filled my urethra.

#     I let my bladder go and felt the familiar rush of relief as my member began to disgorge a steady stream of piss against the back of Kalinth's throat. She swallowed it down eagerly, not once pulling away from me until I had finished urinating into her mouth. The sight of her swallowing every last drop left me with an erection that could have shattered diamonds, and she seemed to be enjoying the fun as well from the look on her face.

#     "Mmm... you taste interesting," Kalinth said once my member stopped twitching. She gave my member a slow lick, from balls to tip, then stepped back with an amused smirk. "I've never tasted a human's piss before."

#     "Well, that's certainly different," I said. "You don't mind?"

#     Kalinth shook her head. "Not at all. No problem." She smirked. "Now are we going to fuck?"

#     #### Piss into her pussy

#     "Inside," I agreed, feeling my erection twitch with anticipation.

#     She moved a little closer. "Then let's get started."

#     ### Kalinth on top

#     I sat back on the couch armrest, letting the assertive dragon archivist take charge. She reared up, resting her forelegs over my shoulders as her spread rear legs revealed her glistening cloaca, searching with her hips for my shaft. Then, pressing my back against the couch's back, she began to tease her cloaca open with my tip, grinding against my erection without letting it in.

#     "Ohhhh," I groaned as the dragoness rubbed herself against me. Her tail swished behind her, making a faint rustling sound with each movement. "Are you going to make me wait like this? I don't know how long I can take it."

#     Kalinth chuckled at that, my face against her fine underbelly scales before she pushed off a little to look me in the eye. "I'll let you inside eventually," she promised with a wink. "But first I just want to feel you all over me down there before..." Her breathing caught and she closed her eyes as her cloaca slid up to my tip again, then she began to lower herself down, enveloping my erection with the warmth of her draconic anatomy.

#     "Oh fuck," I moaned as she took every inch, her tail twitching with excitement. The dragoness paused for a moment, seemingly struggling to take things slow, before she began to gently thrust herself against me, her scaly lower lips rubbing over my member in the most delightful way imaginable.

#     I grabbed onto the couch back tight as I felt Kalinth's cloaca enveloping me, gripping me tighter with every stroke. The heat radiating from her smooth scales was intoxicating. My hips twitched, desperate for more, but she seemed to enjoy this weighty but gentle slow thrusting so much that it was hard to bring myself to complain about it. It wasn't until she moaned loudly and began thrusting even faster that I finally knew the moment had come when she was ready for something more forceful.

#     I groaned as Kalinth finally started fucking me in earnest, her tail whipping back and forth like a flag in the wind of our passion. Her cloaca leaked copious lubrication around my shaft, making it slide in and out with ease as our mating point gave wetter and louder slaps against my groin. I tried to lift my hips a little, thrusting deeper into her, but I could do no better than her weight already pressing down on me. Still, the motion caused her to hug me to her chest again, bringing us closer together in the throes of our passion.

#     "Don't cum just yet," Kalinth whispered hoarsely as she rode me harder and faster, each stroke seeming more desperate than before. "I want... I need..." She moaned, then buried herself on my erection to the hilt, her tail swishing wildly behind her as her passage spasmed and clenched around my shaft. "Now!"

#     I complied with a moan of my own, feeling my orgasm surge forth into her kneading nethers. My member throbbed within her heat and wetness as she lay her body atop mine, resting her weight on my hips to force me as deep within her as I could be. Then the dragoness began grinding herself against me in slow circles, savoring the feeling of the tail-end of my release still spurting slowly into her. My cum and her juices dribbled down between my thighs as my erection faded, leaving us just merely lying together with soiled groins.

#     "Oh... wow," she panted after a few minutes had passed, finally rolling off of me to lie down on the couch properly, while I continued to splay across the armrest and seat back. "That was... even better than I'd imagined."

#     I nodded, panting hard myself as I sat up.

#     ### Player on top

#     "Actually, could you lie down?" I suggested, pointing at the couch. "I'd like to be in control for this."

#     Kalinth quickly agreed. She lay across the couch, her tail swishing and wings fluttering as she settled into a comfortable position and spread her legs to reveal her glistening draconic cloaca. I couldn't help but stare at that sight. The dragoness watched my every move with anticipation.

#     #### Finger her

#     Wanting to make sure she was ready, I chose to start with my fingers. As I approached her, I could smell the sweet scent of her arousal on the air. Carefully, I parted her labia and found just how wet she was for me already. With some gentle stroking around her entrance, I teased her with what was to come.

#     Kalinth gasped, breath shuddering as I touched her. "Oh, yes," she hissed, "so soft... But please, don't tease for too long. I want you inside me."

#     #### Tongue her

#     I couldn't help but wonder how the juices around that gorgeous hole tasted, so I knelt on the floor next to her groin and parted her labia with my thumbs, inhaling the sweet scent of her arousal. It was intoxicating and only heightened the taste of her entrance when I did begin to lick and suck lightly at the edges, gathering up first what had leaked onto her scales before teasingly working my way inside.

#     Kalinth gasped, breath shuddering as I licked her. "Oh, yes," she hissed, "I almost don't want to make you stop. But we can't spend all night here..."

#     #### Enter her

#     I moved closer, my erection throbbing in response to the sight of the open, wet passage. She was inviting me to enter her like this? My heart pounded as my fingers brushed against the scales of her legs as I straddled her tail, taking my position. I took a deep breath, then slowly lowered myself down into her.

#     Her warm cloaca enveloped my member as I pushed inside. Kalinth moaned softly, her wings fluttering faster with excitement. Once I was fully seated within her, she arched her back, purring loudly.

#     "Is that good?" I asked, enjoying the look on her face as she reacted to my entry. "Do you like feeling a human inside you?"

#     "I knew this would feel good," Kalinth replied, still panting from just my slide into her body.

#     As I began to thrust, I closed my eyes, gasping myself from the warmth of the dragoness' cloaca around me. "You have no idea how good," I replied between breaths, thrusting into the dragoness.

#     Her expression was one of pure pleasure. "Mmm... yes," she managed around a gasp, claws digging into the couch fabric as I brought our hips together with increasingly wet slaps.

#     I could feel the dampness growing from her entrance as we continued to couple, and it only fueled my desire for more. I began thrusting faster, harder, driving myself deeper into the dragoness' willing body. Her tail lashed in time with each of my thrusts, keeping rhythm with our lovemaking as she breathed louder and louder.

#     "Don't stop," Kalinth begged, her voice breathy but insistent. "Please don't stop. Ohhhh..."

#     I wasn't about to stop now. She clutched at me tightly, pulling me closer even as her cloaca tightened around my member, her inner muscles clenching. The sensation was too much for me to bear and with a final grunt, I came inside her, spurting white ropes of human seed into the dragoness' waiting passage. Her muscles milked every drop from me but, per her request, I continued thrusting through our shared climaxes.

#     Eventually, as my body began to calm down and the aftershocks subsided, I pulled out of Kalinth, leaving a trail of semen in her now dripping cloaca. She gasped, panting heavily from our shared exertions as she opened her eyes again. "That was... even better than I'd imagined."

#     I smiled at her, still catching my breath. 

#     ### Kalinth doggystyle

#     I patted the armrest of the couch. "Do you want me to bend you over this...?" I trailed off, realizing that, as she was already approaching me on all fours, there wasn't much bending over to be done.

#     She seemed to understand what I meant, though. "That works," Kalinth replied with a grin before lying down over the end of the couch, with her hindlegs hanging over the armrest. She lifted her tail, exposing between her spread legs her glistening cloaca already soaked and waiting for me. "I'm ready whenever you are."

#     #### Finger her from behind

#     As I approached her from behind, I couldn't help but look at her open, wet entrance. My cock twitched in response. Wanting to make sure she was good and ready, I chose to start with my fingers. Sliding them inside her, I felt the heat of her insides, the slickness of her arousal coating my digits as they parted her labia.

#     Kalinth gasped, breath shuddering as I touched her. "Oh, yes," she hissed, "so soft... But please, don't tease for too long. I want you inside me."

#     #### Tongue her from behind

#     I couldn't help but wonder how the juices around that gorgeous hole tasted, so I knelt on the floor between her hindlegs, spreading her thighs with my hands for easier access. Parting her labia with the index finger of one hand, I found just how wet she was for me already. I inhaled the sweet scent of her arousal. It was intoxicating and only heightened the taste of her as I began to tease her entrance lightly with the tip of my tongue, lapping up her juices liberally as she shuddered beneath my hands and mouth.

#     Kalinth gasped, breath shuddering as I licked her. "Oh, yes," she hissed, "I almost don't want to make you stop. But we can't spend all night here..."

#     Reluctantly I got back to my feet.

#     #### Enter her from behind

#     My erection throbbed in response to the sight of the eager dragoness before me and her beautiful rear framing her wet, open passage. I ran my hands over her scaly flanks, feeling the muscle beneath as she arched her back in anticipation. My heart pounded with lust as I lined up our bodies, then slid myself into her from behind, entering her eager cloaca.

#     She moaned loudly, claws digging into the couch fabric and wings rustling softly under me as I began to thrust inside of her. Kalinth was panting hard even before we really got started.

#     "Is that good?" I asked, enjoying the sight of her tensing and untensing her muscles, becoming more worked up with each thrust. "Do you like feeling a human take you like this?"

#     "I knew it would feel good," Kalinth replied, twisting her neck to give me a happy look with lidded eyes.

#     I hugged her tail, hiking it up a little further so that, on my next thrust, I was able to push a little deeper inside, bringing us slightly closer together and eliciting another gasp from both me and the dragoness beneath me. "You have no idea how good," I replied between breaths, thrusting into the dragoness.

#     Her expression was one of pure pleasure as she continued to pant, nuzzling the couch cushions while her tail writhed in my grasp with each of my thrusts. The dragoness' passage was so very warm, flushing my body with heat and arousal as I slid myself in and out of her eager depths with increasingly wet slaps.

#     "Don't stop," Kalinth begged, clinging to the couch cushions as she arched her back under me. "Please don't stop. Ohhhh..."

#     I wasn't about to stop now. I looked down, admiring the ripples each of my hard and fast thrusts made over her rear. Her cloaca tightened around me, her inner muscles clenching, and I closed my eyes as I lost myself in our lovemaking. In moments, the sensation of her climaxing passage was too much for me to bear and with a final grunt, I came inside her, spurting white ropes of human seed into the dragoness' eager depths. I struggled to keep thrusting, per her request, my strength flagging as I carried us through our shared climaxes until finally I just lay on her tail, catching my breath.

#     Eventually, as my body began to recover its strength and the aftershocks in Kalinth's nethers subsided, I pulled out. It wasn't long before I could see my seed oozing from her cloaca in small droplets.

#     Like an overgrown cat, she rolled over on the couch with first her front half, then her lower body, then wriggled her way a little further to get her rear off the armrest so she could lie down normally. Then she sighed happily. "That was... even better than I'd imagined."

#     I smiled at her, still catching my breath.

#     ### Post-intimacy

#     "Well, I aim to please," I said with a wink.

#     She dipped a dulled claw into her folds, teasing herself, before bringing it up to her scaly lips for a taste of our union. She licked it clean, closing her eyes again. "I don't think I'll be able to focus on any of my work for the rest of the night..."

#     With an impish grin, I knelt next to where she lay on the couch.

#     "Oh, willing to help me more at no benefit to yourself?" she asked. "No wonder Bryce keeps asking you for help with investigations."

#     "There's some benefit there," I admitted. "But in both cases, let's just say the work is its own reward." Leaning over her cum-filled cloaca, my tongue flicked out to lick up a first teasing droplet to sample our combined taste and to guage her reaction.

#     Kalinth sighed contentedly at that, then looked back at me with lustful eyes. "I can't say no to free help like this."

#     Eager to provide said help, I dove my tongue back into the dragoness' folds, tasting our mix of juices and semen as she gasped and moaned beneath me. My hands were eager too, parting her labia for easier access to those extra teasing deeper folds that caused her muscles to clench and push out more of our mixed passions.

#     "Oh yes," Kalinth hissed again, crossing her hindlegs over my head. "You're going to make me cum again..."

#     I continued my ministrations, eager to see if I could bring the dragoness off a second time so soon after she'd already climaxed with me. Her breathing was growing louder and faster as my tongue explored her insides and outside, lapping up every drop of our combined fluids and teasing all those sensitive areas that made her moan and whimper.

#     "I think... I think I'm..." Kalinth whispered hoarsely, panting heavily beneath me. Then, abruptly, her legs clamped down, pinning my face in place as she arched her back again. She wrapped her forepaws around her own muzzle, muffling her moans of passion and pleasure with a strangled cry, bucking against the couch as another climax washed over her body.

#     Juices from her passage flooded my tongue, soaking my face, but I continued to lap them up eagerly, drinking in every last drop while she clutched me to her entrance. The dragoness eventually, seemingly reluctantly, relaxed her legs to let me breathe again, though she still draped her legs over my shoulders, rubbing my back gently.

#     As I finally sat back on my haunches, panting and sweaty from the hotbox held to my face, Kalinth grinned down at me. "I've got to get you my number."

#     "I guess you do," I agreed, wiping off my face with an arm. "And a towel, if you know where one is?"
#     """
