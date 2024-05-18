init python:
    bangok_four_bryce2_unplayed = True

init python in bangok_four_bryce2_store:
    forepaw_tickle = False


    hindpaw_tickle = False
    hindpaw_suckle = False
    hindpaw_lick = False
    hindpaw_massage = False


    player_came = False
    bryce_came = False
    cumlube = False


label bangok_four_bryce2_skipmenu:
    play sound "fx/system3.wav"
    s "你想要玩弄布莱斯的脚吗？"
    menu:
        "是的，我想玩弄布莱斯的脚。":
            play sound "fx/system3.wav"
            if bangok_four_common.bangnokay.check():
                s "太糟糕了。{cps=2}..{/cps}{w=1.0}{nw}"
            else:
                s "如你所愿。{cps=2}..{/cps}{w=1.0}{nw}"
                scene black with dissolvemed
                $ renpy.pause (1.0)

                $ persistent.skipnumber += 1
                call skipcheck from _bangok_four_call_skipcheck_bryce2_1

                $ bryce2mood += 1

                scene pad at Pan ((0, 360), (0,360), 0.0)
                show bryce brow bangok foreleg flip
                with dissolvemed

                play music "mx/campfire.ogg" fadein 2.0
                jump bangok_four_bryce2_explorepaw
        "不，不要那么远。":
            pass
    jump bangok_four_bryce2_skipmenu_return


label bangok_four_bryce2_explorepaw:
    $ renpy.pause (0.5)
    m "我把手滑到布莱斯的前腿下，感觉到他前腿上的粗糙鳞片保护着厚实的肌肉结节，这些肌肉赋予他力量。"
    show bryce brow bangok foreleg flip with dissolve
    m "他让我抬起他的腿，几乎接触到地板，给我他的前爪时带着一种看着我的表情。"
    $ renpy.pause (0.8)
    c "美极了。"
    if bangok_four_bryce1_unplayed == False and persistent.nsfwtoggle == True:
        Br laugh bangok foreleg flip "好吧，我以为我们这次说好了不发生性行为。"
        Br smirk bangok foreleg flip "听起来你好像在调戏我。"
    else:
        Br laugh bangok foreleg flip "好吧，你不必这么夸我。"
        show bryce smirk bangok foreleg flip with dissolve

    menu:
        "我不能赞美一个好看的龙吗？":
            $ renpy.pause (0.5)
            $ bryce2mood += 1
            Br flirty bangok foreleg flip "好吧，我想我不能阻止你。"

        "[[吻他的脚。]":
            $ renpy.pause (0.5)
            show bryce brow bangok foreleg flip with dissolve
            play sound "fx/kiss.wav"
            $ renpy.pause (1.1)
            $ bryce2mood -= 1
            Br brow bangok foreleg flip "...呃。嗯。"

        "嘿，我只是说说。关于那个案子...":
            jump bangok_four_bryce2_explorepaw_end

    m "再往下摸了一下，我的手指触碰到他爪子的光滑掌心——或者说他的脚底，如果我应该这么叫的话。"
    c "那么你把这些叫做什么？脚？还是爪子？前爪？"

    Br brow bangok foreleg flip "随便叫什么都行。我不太在意。"
    c "什么时候“前爪”比“脚”更容易说？"
    Br laugh bangok foreleg flip "我不知道。我刚刚说过，我不太在意。"
    m "他的尾巴晃动了一下，他调整了一下体重。"
    Br normal bangok foreleg flip "你对这个很有兴趣啊，是吧？"
    m "我没有注意到，但在我们聊天期间，我无意识地在揉捏着他的爪子，摸索着他鳞片下的复杂生物关节，那里他的脚趾与脚的主体连接。"

    menu:
        "[[把他的脚还给他。]":
            c "哦，对不起。"
            label bangok_four_bryce2_explorepaw_exit:
            show bryce normal with dissolve
            m "布莱斯稍微挪动了一下，把他的前爪按在地板上。"
            Br normal "没关系，我不介意。"
            c "无论如何，关于那个案子..."
            $ bryce2mood -= 1
            jump bangok_four_bryce2_explorepaw_end

        "[[挠他痒痒。]":
            $ renpy.pause (0.5)
            $ bangok_four_bryce2_store.forepaw_tickle = True
            m "用一只手抓住他的前爪，我用手指在他的掌心上来回划动。"
            show bryce brow bangok foreleg flip with dissolve
            $ renpy.pause (0.8)
            Br "呃。你在干什么？"
            c "挠你痒痒？"
            Br "在我的前爪上？"
            Br smirk bangok foreleg flip "你知道我经常用这个拿东西和移动东西吧？它不太痒。"
            c "哦。"
            Br laugh bangok foreleg flip "但现在我知道对等是公平的，你的脚也很痒吧？"
            c "呃。"
            Br smirk bangok foreleg flip "放松。我不能通过你穿的东西挠到你的脚。"
            Br brow bangok foreleg flip "而且我不想在那切到你。那会很尴尬的。"

            m "说到尴尬，我还在握着他的脚。"
            menu:
                "[[把他的脚还给他。]":
                    $ renpy.pause (0.5)
                    jump bangok_four_bryce2_explorepaw_exit
                "想要脚部按摩吗？":
                    $ renpy.pause (0.5)
                    Br "... 脚部按摩？"
                    c "我是说，毕竟我刚才试图挠你痒痒，这是我能做的最少的事。"
                    Br laugh bangok foreleg flip "哈哈！好吧，我猜可以。"
                    Br normal bangok foreleg flip "我不会拒绝的。毕竟是免费的？这个价格无敌了。"

        "呃。你希望我停下来吗？":
            $ renpy.pause (0.5)
            Br "不。"
            Br brow bangok foreleg flip "我是说，我不想强迫你做什么...我有点享受。"
            Br laugh bangok foreleg flip "天哪。我不记得上次有人给我这么好的脚部按摩了。"
            Br normal bangok foreleg flip "所以，如果你愿意的话，继续做你在做的事吧。"
            menu:
                "停下来。":
                    $ renpy.pause (0.5)
                    jump bangok_four_bryce2_explorepaw_exit
                "继续。":
                    pass

        "我想我是这样的。":
            $ renpy.pause (0.5)
            Br "好吧，不要让我阻止你。我有点享受。"

    $ renpy.pause (0.5)
    $ bryce2mood += 1
    m "我加上了另一只手，现在有意地用双拇指挤压，感觉到他鳞片下的骨骼结构。"
    $ renpy.pause (1.5)
    Br laugh bangok foreleg flip "嗯，这感觉不错。"
    $ renpy.pause (1.0)
    show bryce normal flip with dissolve
    m "挤压他的鳞片是个辛苦的工作，在我的手掌酸痛之前，我换到布莱斯的另一只前爪。"
    c "你保持得很干净。"
    Br "是啊。也要保持地板干净，毕竟谁愿意住在一片混乱中呢？"
    Br "再加上我现在有点时间放假，这也是我为什么邀请你来，而不是回到案发现场。"
    Br stern flip "我今天实际上还没有出门，因为我担心一出去就会直接回到工作中，休息不到。"
    $ renpy.pause (0.5)
    Br brow flip "你知道，我邀请你来不是为了让你给我按摩。我应该是招待你，不是反过来。"
    Br normal flip "如果你可以，那我就不需要按摩了。"
    if persistent.nsfwtoggle and not bangok_four_common.bangnokay.check():
        menu:
            "吻他的脚。":
                $ renpy.pause (0.5)
                show bryce brow bangok foreleg flip:
                    xalign 0.3
                with dissolve
                $ renpy.pause (0.3)
                show bryce brow bangok foreleg flip:
                    zoom 1.0
                    ease 0.5 zoom 1.5
                    zoom 1.5
                with None
                $ renpy.pause (0.5)
                play sound "fx/kiss.wav"
                $ renpy.pause (1.0)

            "放手。":
                jump bangok_four_bryce2_hosting_challenge_exit
    else:
        label bangok_four_bryce2_hosting_challenge_exit:
            c "是的，这是公平的。"
            c "还是要说：你有一些好看的腿，布莱斯。"
            Br laugh "谢谢。"
            jump bangok_four_bryce2_explorepaw_end

    $ renpy.pause (0.5)
    c "我现在觉得很有趣。"
    if bryce2mood < 0:
        show bryce stern with dissolve
        m "布莱斯怒目而视地把他的脚收回。"
        Br "你知道吗？不。你已经够侮辱我了。你要么停止对我的腿毛手毛脚，要么就离开。自己决定吧。"
        menu:
            "抗议。":
                c "哦拜托。“变态”？我给你免费脚部按摩。"
                if bangok_four_bryce1_unplayed == False:
                    Br "没错。我明确表示我想慢慢来，而你却一开始就开始在我的腿上动手动脚。"
                else:
                    Br "没错。我邀请你过来只是想让我们两个朋友一起闲聊，彼此了解，而你却一开始就开始在我的腿上动手动脚。"
                c "是你邀请我的！"
                Br "我邀请你摸摸我的腿。"
                Br brow "我会说你在那之后就已经多待了，当你把嘴放在我身上的时候。"
                Br stern "无意冒犯，我不知道这是人类的事还是你的事，但我不想看看一个混蛋像你一样试图把事情带到哪里。"
                jump bangok_four_bryce2_canon_jerk_ending
            "道歉。":
                c "对不起。我以为你喜欢脚的东西，也许我之前的评论有点过分..."
                Br brow "我是说，也许是，但在侮辱之后感觉怪怪的，即使你夸我肌肉。"
                show bryce at center with ease
                m "我挪开了一些，给布莱斯一些空间。"
                c "好的。其他话题..."
                jump bangok_four_bryce2_explorepaw_end
            "离开。":
                jump bangok_four_bryce2_canon_jerk_ending_departure
    else:
        Br flirty bangok foreleg flip "原来这就是你的意图。"
        if bangok_four_bryce1_unplayed == False:
            Br stern bangok foreleg flip "看来上次说好慢慢来也没用。"
            c "我是说，我们不一定要走那么远。"
            Br brow bangok foreleg flip "那我的脚对你来说就是这样，对吧？"
            $ renpy.pause (0.8)

    if bryce2mood < 1:
        m "布莱斯轻轻地把他的爪子收回。"
        Br normal flip "让我现在就终结这个。我不感觉到。"
        c "哦。"
        if bangok_four_bryce1_unplayed == False:
            Br laugh flip "我告诉过你，我想慢慢来。"
        else:
            Br laugh flip "我不会这么快投入。"

        Br normal flip "让我们把玩弄脚的事情留到下次吧。"
        c "好吧。"
        show bryce at center with ease
        m "我挪开了一些，给布莱斯一些空间。"
        c "好的。其他话题..."
        jump bangok_four_bryce2_explorepaw_end

    $ bangok_four_malepartners += 1

    Br laugh bangok foreleg flip "啊，算了。"
    Br smirk bangok foreleg flip "我还有两只脚需要注意，是吧？"

    show black with dissolvemed
    play sound "fx/cartslide.ogg"
    m "布莱斯躺在他的沙发上，弹簧在他的重量下呻吟。"
    m "我抓住他的一只后腿，当他把另一只腿撑在沙发上时，迅速将手伸到他后腿上感兴趣的地方。"
    m "布莱斯的后爪结构与他的前爪相似，虽然我可以感觉到一个关节缺失或移动了，他的前爪上他可以对折一个脚趾。"
    m "他的脚和背后的腿肌肉比我预期的更像人类，如果我忽略了鳞片、爪子和只有三个脚趾的话。"
    if bangok_four_bryce2_store.forepaw_tickle == True:
        Br smirk "现在，不要想着在下面挠我痒痒。我还有三条腿和一条尾巴空着。"
        c "大警察局长怕点小痒痒？"
        Br laugh "我怕会不小心把你撞倒。"

label bangok_four_bryce2_hindpaw_menu:
    if sum([bangok_four_bryce2_store.hindpaw_tickle,bangok_four_bryce2_store.hindpaw_suckle,bangok_four_bryce2_store.hindpaw_lick,bangok_four_bryce2_store.hindpaw_massage]) < 3:
        menu:
            "挠痒痒。" if bangok_four_bryce2_store.hindpaw_tickle == False:
                $ renpy.pause (0.8)
                $ bangok_four_bryce2_store.hindpaw_tickle = True
                play sound "fx/tableslap.wav"
                Br laugh "哦-好了！该死的你成功了。"
                m "布莱斯的尾巴来回摆动。他显然在努力不再撞到茶几。"
                Br stern "看，停下——停止，那样我会不小心撞到你。我不想伤到你。"
            "按摩。" if bangok_four_bryce2_store.hindpaw_massage == False:
                $ renpy.pause (0.4)
                $ bangok_four_bryce2_store.hindpaw_massage = True
                m "用双手握住布莱斯的脚，我用拇指揉捏他的脚底，摸索着下面的结构。"
                Br laugh "嗯，这就是位置。"
            "吮吸爪子。" if bangok_four_bryce2_store.hindpaw_suckle == False:
                $ renpy.pause (0.5)
                $ bangok_four_bryce2_store.hindpaw_suckle = True
                m "我把布莱斯的一只爪子含进嘴里，把冷硬的角质滑过我的舌头，直到爪子长出的地方。"
                Br smirk "嘿——这感觉真是特别。"
                m "我放开了他的爪子。"
                c "好感觉吗？"
                Br smirk "相当不错，是的。只是那种触碰我脚趾尖和爪子根部的感觉。我不知道怎么形容。"
            "舔脚垫。" if bangok_four_bryce2_store.hindpaw_lick == False:
                $ renpy.pause (0.5)
                $ bangok_four_bryce2_store.hindpaw_lick = True
                m "我的舌头在布莱斯脚底光滑的鳞片上摩擦，那些鳞片因支持他的体重和运动而被磨得光滑。"
                m "布莱斯挪了一下尾巴。"
                Br brow "有点痒。感觉不太明显。"
        jump bangok_four_bryce2_hindpaw_menu

    show bryce laugh
    hide black
    with dissolvemed

    if bangok_four_bryce2_store.hindpaw_tickle == True:
        m "当我换到布莱斯的另一条后腿，施以相同的待遇时（除了挠痒痒），布莱斯长舒了一口气。"
    else:
        m "当我换到布莱斯的另一条后腿，施以相同的待遇时，布莱斯长舒了一口气。"

    if bangok_four_bryce1_unplayed == False:
        Br laugh "我知道我说过不发生性行为，但你崇拜我的脚真让我兴奋。"
    else:
        Br laugh "我没有邀请你来做这种事，天哪，这可能是个外交事件，但你崇拜我的脚真让我兴奋。"

    Br smirk "那我的脚再按到你身上的其他地方？或者我可以把脚放在你身上的某个地方？"

    $ bangok_four_bryce2_unplayed = False
    if bangok_four_playerhasdick is None:
        m "很难忽视..."
        menu:
            m "很难忽视...{fast}"
            "...我裤子里的帐篷":
                $ bangok_four_playerhasdick = True
            "...我裤子里湿了":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick == True:
        m "很难忽视布莱斯的建议带来的反应。"
    else:
        m "很难忽视布莱斯的建议引起的湿意。"

    menu:
        "你能用你的脚帮我解决吗？":
            $ renpy.pause (0.5)
            Br laugh "当然。"
            Br smirk "只要你愿意之后也帮我。"
            c "成交。"

            show black with dissolve

            play sound "fx/undress.ogg"
            $ renpy.pause (0.8)
            m "我脱下了我的衬衫，踢掉鞋子，然后挣扎着脱下裤子。"
            jump bangok_four_bryce2_footjob

        "我想更多地崇拜你。":
            $ renpy.pause (0.5)
            Br flirty "过来吧。"
            show black with dissolve

            play sound "fx/undress.ogg"
            $ renpy.pause (0.8)
            m "我脱下了我的衬衫，踢掉鞋子，然后挣扎着脱下裤子。"
            m "我跪在他旁边，研究我即将给予仔细关注的对象。"
            jump bangok_four_bryce2_worship


label bangok_four_bryce2_footjob:
    m "布莱斯调整他的腿，试图把他的脚放在我胯部的高度，他躺在沙发上。"
    if bangok_four_playerhasdick == True:
        m "我观察着他鳞片覆盖的脚垫，充满欲望，想着即将做的事。"
        Br brow "抱歉我的爪子有点锋利，但你知道我的工作不允许我把它们剪掉。"
        c "我并不是要和你的爪子发生关系，对吧？"
        Br laugh "说得对！"
        show bryce normal with dissolve
        if bangok_four_bryce2_store.cumlube == True:
            m "我把他的脚垫挤压在我的长度周围，脚趾朝向我的顶端，挤压上下来分布他的精液在他的脚垫和我的长度上。"
            m "然后他轻轻地开始移动，他湿滑的脚在我的顶端移动，直到他只是抓住了我的顶端，然后再往下按压在我坚硬的杆子上。"
        else:
            m "我把他的脚垫挤压在我的长度周围，脚趾朝向我的顶端，感受到他脚垫上略微粗糙的质感挤压在我的私处。"
            m "然后他轻轻地开始移动，他粗糙的脚垫在我的坚硬的杆子上刮擦，让我的膝盖因为过度刺激而发软。"
        m "当他往下按压时，他的脚垫撞到我的骨盆几乎让我失去平衡，只是被他快速的反应用脚趾抓住我的顶端拉回。"
        c "哦——别弄伤我！"
        Br laugh "抱歉。"
        Br smirk "试图不让你倒下。"
        m "当他放松他的脚趾时，血液流回到我的顶端，让我的私处充满热量，同时也让我脑子里产生了一个新的想法。"
        menu:
            "用他的脚趾交替。":
                c "你能再次交错你的脚趾吗？"
                Br brow "嗯？"
                m "布莱斯按照要求做了，把他的脚趾和爪子交叉在一起，形成一团密集的鳞片和角质。"
                m "他的腿显然在这个角度上很吃力。"
                Br laugh "这真是测试我关节的极限啊。"
                c "这会值得的。"
                if bangok_four_bryce2_store.cumlube == True:
                    m "把他的精液湿滑的脚稍微分开一点，我打开一个由几个脚趾框起来的小洞，然后插了进去。"
                    m "感觉非常好。我揉捏着他的脚顶，把他的脚垫按在我的骨盆上，他的脚趾紧紧地抓住我的长度。"
                else:
                    m "把他的脚稍微分开一点，我打开一个由几个脚趾框起来的小洞，然后插了进去。"
                    m "这种结合虽然粗糙，但在所有正确的地方都挤压到位。我揉捏着他的脚顶，把他的脚垫按在我的骨盆上，他的脚趾紧紧地抓住我的长度。"
                play soundloop "fx/rub2.ogg" fadein 0.5
                $ renpy.pause (0.5)
                m "我开始真正地推动，在他的脚趾之间交替，他在下面笑着。"
                Br smirk "不能说我以前有过这种感觉。"
                $ renpy.pause (0.8)
                Br pant "就在我的脚趾之间。嗯。"

                if bangok_four_bryce2_store.cumlube == True:
                    m "随着我接近高潮，布莱斯的精液在我的胯部越来越少，脚趾交错的洞揉捏着我的杆子的顶部和底部，即使他的脚在我的速度下稍微分开。"
                else:
                    m "我没有语言，当我接近高潮时，脚趾交错的洞揉捏着我的杆子的顶部和底部，即使他的脚在我的速度下稍微分开。"

            "用他的脚弓。":
                c "你能把你的脚稍微抬起来吗？"
                m "布莱斯调整了他的脚，试图把脚抬起来，虽然他只抬了一个小角度。"
                Br laugh "测试我的关节极限。"
                c "这会值得的。"
                if bangok_four_bryce2_store.cumlube == True:
                    m "把他的精液湿滑的脚稍微分开一点，我打开一个小洞在他脚弓之间，然后向下插入。"
                    m "感觉非常好。我揉捏着他的脚顶，把他的脚跟按在我的骨盆上，他的脚垫紧紧地抓住我的杆子的底部。"
                else:
                    m "把他的脚稍微分开一点，我打开一个小洞在他脚弓之间，然后向下插入。"
                    m "他平滑的脚垫足够光滑，微微粗糙的质感让我的长度闪烁火花。我揉捏着他的脚顶，把他的脚跟按在我的骨盆上，他的脚垫紧紧地抓住我的杆子的底部。"
                play soundloop "fx/rub2.ogg" fadein 0.5
                $ renpy.pause (0.5)
                m "我开始真正地推动，在他的脚垫之间，尾巴摇摆，他笑着。"
                Br smirk "啊——嘿——好——啊，这感觉——"
                $ renpy.pause (0.8)
                m "显然他在努力控制这痒痒的感觉，而我则放弃了控制我的欲望。"
                Br pant "老天，这感觉太狂野了。"

                if bangok_four_bryce2_store.cumlube == True:
                    m "布莱斯的精液在我的杆子周围越来越少，当我接近高潮时。"

                m "他交错了脚趾，把我过度刺激的长度夹在他强壮的脚垫之间，稍微推回我。"
                m "这就是我忍耐的最后限度。"

        stop soundloop fadeout 0.5
        play sound "fx/rub1.ogg" fadein 0.5
        queue sound "fx/extinguish.ogg"
        $ bangok_four_bryce2_store.player_came = True
        $ renpy.pause (1.8)

        if bangok_four_bryce2_store.cumlube == True:
            m "我的射精量相比布莱斯的小得多，但仍然在他的生殖裂缝周围留下几条白色的绳索，他把我的长度指向他射精的地方。"
        else:
            if bangok_four_bryce2_store.bryce_came == "outside" or bangok_four_bryce2_store.bryce_came == "cleaned":
                m "布莱斯在我射精时把我的长度向下拉，在他的生殖裂缝上留下白色的绳索，与他之前留下的痕迹连接。"
            else:
                m "布莱斯在我射精时把我的长度向下拉，在他的生殖裂缝上留下白色的绳索，以展示他精湛的脚工。"

    elif bangok_four_playerhasdick == False:
        m "我观察着他鳞片覆盖的脚垫，充满欲望，想着即将做的事。"
        Br brow "抱歉我的爪子有点锋利，但你知道我的工作不允许我把它们剪掉。"
        Br stern "嗯，可能不太好，你把任何东西放进去，即使对于女龙也是不安全的。"
        c "说得对。"
        show bryce normal with dissolve
        if bangok_four_bryce2_store.cumlube == True:
            m "我把他的脚垫挤压在一起，然后按在我的下体上，挤压他的精液在他的脚底和我湿润、渴望的洞之间。"
        else:
            m "我把他的脚垫挤压在一起，然后按在我双腿之间的湿滑缝隙上，用他平滑的脚垫按摩我的下体。"
        m "他的力量很小，我开始轻轻地磨蹭他的脚，寻找更多的刺激。"
        $ renpy.pause (0.8)
        c "让我做所有的工作吗？"
        Br laugh "我会做更多，但我不想不小心把你踢飞。"
        Br smirk "此外，看起来你这样很开心。"
        m "抓住他的一只脚，我用手把他的脚趾弯曲，把他的爪子放在他的脚垫上，留下他脚趾关节的表面。"
        Br laugh "哦，天哪。这是解决锋利爪子的一个方法。"
        m "我在他的脚趾关节上滑动，感受着他们在我外部褶皱和阴蒂上的摩擦。"
        m "然后，突然，我感觉到他的另一只脚在我的背部，把我拉向他的脚，让两个脚趾关节同时进入我的外部褶皱。"
        c "哈——！"
        Br flirty "我想我找到一个帮助的方法了。"
        m "我几乎要晕倒了，双腿无力，他把我固定在原地，用他鳞片覆盖、粗糙的脚趾关节在我的湿滑缝隙上摩擦。"
        c "等——"
        if bangok_four_bryce2_store.cumlube == True:
            m "我把他的脚转回他的脚垫，粘稠的表面足够的刺激，他把我固定在原位，用他的脚在我的欲望上滑动，一些重量压在他身上。"
        else:
            m "我把他的脚转回他的脚垫，平滑的表面稍微粗糙，但足够的刺激，他把我固定在原位，用他的脚在我的欲望上滑动，一些重量压在他身上。"
        $ renpy.pause (0.8)
        c "嗯——"
        Br smirk "我的脚在所有正确的位置上吗？"
        $ renpy.pause (0.5)
        m "我把他的脚更用力地拉向我的下体，失去了语言。"
        $ renpy.pause (0.5)
        m "然后他的脚跟滑动在正确的位置，我达到了颤抖的高潮。"
        $ bangok_four_bryce2_store.player_came = True
        $ renpy.pause (1.5)

        Br smirk "感觉如何？"
        menu:
            "[[舔你在他脚上的液体。]":
                $ renpy.pause (0.5)
                if bangok_four_bryce2_store.cumlube == True:
                    m "我用舌头在他的湿滑脚垫上滑动，混合了我的液体和他的精液，成了一种粘糊糊、略带咸味的混合物。"
                else:
                    m "我用舌头在他的湿滑脚垫上滑动，我的液体留下了他的脚底闪亮和咸味，显示了我对他的脚工的赞赏。"
            "太棒了。":
                pass
            "我想轮到你了。" if bangok_four_bryce2_store.bryce_came == False:
                $ renpy.pause (0.5)
                Br smirk "我等不及了。"
    else:
        $ renpy.error ("对不起，您必须要么有阴茎，要么没有。")

    $ renpy.pause (0.8)
    Br laugh "我得让你再来更多的“脚部按摩”。"
    if bangok_four_bryce2_store.bryce_came == False:
        m "我看到布莱斯的粉红色龟头从他的裂缝中探出来。"
        Br smirk "好吧，你真的让我兴奋了。"
        Br flirty "你会帮忙吗？"
        jump bangok_four_bryce2_worship

    Br laugh "真是个好时光。"

    $ bryce2mood += 4
    show bryce:
        zoom 1.0
        xalign 0.5
    hide black
    with dissolvemed

    jump bangok_four_bryce2_canon_beer


label bangok_four_bryce2_worship:
    m "布莱斯张开他的后腿，欢迎我靠近他的胯部。"
    if bangok_four_bryce2_store.player_came:
        m "我的液体滴在他的鳞片上，围绕着一个水平裂缝，我能看到一个小的粉红色尖端从里面探出来。"
        m "然后他的一条腿绕在我的头后，脚侧压在我的脸颊上，把我的脸拉向他的裂缝，把我的液体抹在我的脸上，我的鼻子和嘴巴贴在他的尖端上。"
        m "我能感觉到他的另一只脚跟在我的背上，把我往上拉进他的第一条后腿的怀抱。"
        $ renpy.pause (0.5)
        m "我顺从地开始舔和吮吸，清理自己的液体，同时试图引出他更多的长度。"
    else:
        m "在两个腹部鳞片之间的水平裂缝中，我能看到一个小的粉红色尖端从里面探出来。"
        m "然后他的一条腿绕在我的头后，脚侧压在我的脸颊上，把我的脸拉向他的裂缝，我的鼻子和嘴巴贴在他的尖端上。"
        m "我能感觉到他的另一只脚跟在我的背上，把我往上拉进他的第一条后腿的怀抱。"
        $ renpy.pause (0.5)
        m "我顺从地开始舔和吮吸，试图引出他更多的长度。"

    Br pantflirt "嗯。"

    m "更多的龙阴茎探出来，擦过我的脸颊，我吻着吮吸，闭着眼睛舔过底部，完全被这个大生物强大的腿掌控。"
    m "我感觉到他的脚趾蜷缩，一只爪子擦过我的额头。"

    $ renpy.pause (0.5)
    Br smirk "现在你已经尝过两者，哪个更好？我的脚，还是我的阴茎？"
    menu:
        "脚。":
            $ renpy.pause (0.5)
            Br flirty "好吧，允许我展示更多的后者。"
        "阴茎。":
            $ renpy.pause (0.5)
            Br laugh "同意，但你让我看到我的其他部分也有乐趣。"
        "[[呻吟。]":
            $ renpy.pause (0.5)
            m "我在布莱斯的胯部呻吟，他又大笑起来。"
            Br laugh "两者都有点？"

    $ renpy.pause (0.5)
    Br smirk "我真的不确定我的腿能不能这样抓住你。"
    m "他的脚在我的脸上摩擦，脚跟在我的背上，他把我拉到他的阴茎上。厚厚的龙肉擦过我的脸，把我的嘴唇放在他的顶端。"
    m "然后他的前爪下来，抓住我的头，把我最后一点距离拉到他的头下，剩下的擦在我的胸上。"
    m "这也把他的前爪放在我的舌头范围内。"
    menu:
        "舔他的脚。":
            $ renpy.pause (0.5)
            Br laugh "嘿！"
            Br smirk "哦，你喜欢那个，是吧？"
            m "他把他的前爪在我的脸上摩擦。"
            Br smirk "搞定我之后，我会让你舔干净这些。"
        "吮吸他的阴茎。":
            pass

    $ renpy.pause (0.5)
    m "我把他的顶端含进嘴里，品尝到他龙阴茎上的甜蜜前液，饱满的味道让我的舌头从他的硬鳞片和滑嫩的肉体之间的粗糙中获得不同的体验。"
    m "我在他的脚下上下摆动我的头，把他的阴茎擦过我的胸膛，急切地想要看到结果，带给这个大型龙更多的快乐。"

    Br pant "哦，嗯。快要到了。"
    menu:
        "让布莱斯自己解决。":
            $ bangok_four_bryce2_store.bryce_came = "outside"
            m "布莱斯感觉到我从他的顶端退了开，他把他的前爪从我的头上移开，正好挡住了喷射。"
            play sound "fx/snarl.ogg"
            m "精液溅在他的前爪和腹部上，有些甚至溅到我继续舔他的顶端时的脸。"
            if persistent.bangok_inflation == True:
                m "一股又一股的射出，直到白色的液体在布莱斯的腹部形成一个水坑，向沙发流去。"
            m "然后脉动结束了，布莱斯松开了他的后腿。"
        "吞下。":
            $ bangok_four_bryce2_store.bryce_came = "inside"
            play sound "fx/snarl.ogg"
            m "浓稠的精液喷溅在我的嘴里，然后布莱斯的臀部猛地推向我，试图把整个头都推进我的嘴里。"
            m "在这个角度，被他的脚掌固定住，我很难吞咽。"
            m "我咳嗽着，第二、第三股精液填满了我的嘴，精液从我的嘴唇漏出，只能被他的前爪抓住。"
            if persistent.bangok_inflation == True:
                m "我努力吞咽，但量太多了，很快我感觉到一股精液从我的鼻子喷出，我的喉咙被布莱斯的种子塞满了。"
            m "然后脉动结束了，布莱斯松开了他的后腿，我才能完全吞下他留下的精液。"

    Br pant "哈..."
    Br flirty "我的前爪上留下了不少呢。"
    if bangok_four_bryce2_store.bryce_came == "outside":
        Br flirty "我的肚子上也都是。"
    Br smirk "你要帮忙清理吗？"

    menu:
        "[[把一些涂在你的下体作为润滑剂。]]" if bangok_four_bryce2_store.player_came == False:
            $ renpy.pause (0.5)
            $ bangok_four_bryce2_store.cumlube = True
            Br flirty "如果你这么喜欢我的精液，也许我应该直接把这根杆子放进你体内。"
            c "但这样我就不能玩这些了。"
            Br smirk "哦？"
            jump bangok_four_bryce2_footjob
        "[[把一些涂在他的后爪上作为润滑剂。]]" if bangok_four_bryce2_store.player_came == False:
            $ renpy.pause (0.5)
            $ bangok_four_bryce2_store.cumlube = True
            Br laugh "你是想让我在紫外灯下留下很多脚印吗？"
            c "不，只是让这些更有趣。"
            Br smirk "哦？"
            jump bangok_four_bryce2_footjob
        "[[帮忙舔干净。]]":
            $ renpy.pause (0.5)
            if bangok_four_bryce2_store.bryce_came == "outside":
                if persistent.bangok_inflation == True:
                    m "我在布莱斯的肚子上抓住了那滩精液，防止它流到沙发上，用手收集起来，直到我能把脸放到位置开始舔干净他的精液。"
                    m "布莱斯的腹部鳞片在我舔舐时移动着，他躺在那享受着我的工作，同时他的前爪沾满了等着我处理的液体。"
                    m "当我舔干净他的腹部后，我把布莱斯的前爪放在一起，用我已经沾满精液的舌头舔干净。"
                else:
                    m "我把布莱斯的黏糊糊的前爪放在一起，用舌头舔干净厚厚的白绳。"
            else:
                if persistent.bangok_inflation == True:
                    m "我把布莱斯粘糊糊的前爪放在一起，慢慢舔掉厚厚的白绳，发现即使我已经吃饱了主菜，吞咽还是很困难。"
                else:
                    m "我把布莱斯的前爪放在一起，舔掉我溢出的精液，把他的脚垫舔干净。"
            m "当我完成时，布莱斯的前爪的平滑鳞片闪闪发光，像是被抛光了一般。"
            Br laugh "如果我能让你像这样给我全身洗澡就好了。"

            $ bangok_four_bryce2_store.bryce_came = "cleaned"
        "抱歉，布莱斯。我不确定我能帮上忙。":
            $ renpy.pause (0.5)
            Br laugh "啊，算了。值得一试，看能不能让你再用嘴巴在我身上多玩一会儿。"
            m "布莱斯把他的前爪抬到他的口中，迅速舔掉了他的精液，这可能耗时好几分钟。"
            if bangok_four_bryce2_store.bryce_came == "outside":
                m "然后他向前弯曲，同样清理了他腹部上的精液，虽然他错过了很多地方，太迟了，不能阻止一些流到沙发上。"

            $ bangok_four_bryce2_store.bryce_came = "cleaned"

    if bangok_four_bryce2_store.player_came == False:
        Br smirk "看来现在是我帮你的时候了。或者脚。或者脚掌。"
        menu:
            "对。":
                $ renpy.pause (0.5)
                jump bangok_four_bryce2_footjob
            "其实，我觉得够了。":
                $ renpy.pause (0.5)
                Br laugh "“好”绝对是我形容你的词。"
                Br brow "你啊，不后悔吧，对吧？"
                c "一点也不。只是...不想要回报。"
                Br normal "好吧。只要你开心就好。"
    else:
        Br laugh "天哪，真是个好时光。"

    $ bryce2mood += 4
    show bryce:
        zoom 1.0
        xalign 0.5
    hide black
    with dissolvemed

    jump bangok_four_bryce2_canon_beer


label bangok_four_bryce2_show_bryce_no_tail:
    m "我转过身，向布莱斯展示我缺少的尾巴。"
    Br laugh "我不相信。几分钟前我怎么没看到这个？"
    c "我稍微转移了你的注意力。"
    Br smirk "稍微吧。"
    Br brow "还有你穿的那些东西。为什么要把它们都盖住？"
    c "这是人类的事情。我们通常不会向陌生人展示我们的身体。"
    Br normal "那么，朋友可以吗？"
    c "那样的友谊很不寻常。让我们说展示那个区域通常意味着...我们做了什么。"
    Br flirty "是这样吗？"
    $ bryce2mood += 1
    jump bangok_four_bryce2_show_bryce_no_tail_end

label bangok_four_bryce2_talking_otherthings:
    Br flirty "...和其他事情。"
    jump bangok_four_bryce2_talking_otherthings_return