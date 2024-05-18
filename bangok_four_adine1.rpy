label bangok_four_adine1_angercheck:
    if adinemood < 0:
        $ renpy.pop_call()
        jump bangok_four_adine1_abruptexit
    return

label bangok_four_adine1_abruptexit:
    stop music fadeout 1.0
    Ad frustrated b "你知道吗？我受够你和这个游戏了。"
    c "但是--"
    Ad "我宁愿应对这场雨也不愿再忍受你的变态。"
    hide adine with dissolve
    m "我还没来得及说话，艾丁已经朝着门口走去了。"
    c "嘿！"
    play sound "fx/door/doorclose3.wav"

    $ adinestatus = "bad"
    $ adinescenesfinished = 1
    jump _mod_fixjmp

label bangok_four_adine1_ToD_refused:
    Ad think b "老实说我有点讨厌你。外面还在下雨吗？"
    m "暴风雨还没停，虽然稍微减弱了一些。"
    c "不太严重，所以你应该留下--"
    Ad disappoint b "不，够了。我现在要走了。"
    hide adine with dissolve
    $ renpy.pause (0.3)
    play sound "fx/door/doorclose3.wav"
    m "我还没来得及再说一句话，她就已经消失在薄薄的雨幕中飞走了。"

    $ adinestatus = "bad"
    $ adinescenesfinished = 1
    jump _mod_fixjmp

label bangok_four_adine1:
    if bangok_four_common.bangnokay.check():
        jump bangok_four_adine1_return

    m "当我提起这个话题时，我想了一些..."
    $ headgear = True
    menu:
        m "当我提起这个话题时，我想了一些...{fast}"
        "...愚蠢的问题和挑战的想法。":
            jump bangok_four_adine1_return
        "...淫荡的问题和挑战的想法。":
            $ adinemood = 2 if adinemood > 0 else 2 + adinemood // 5
            if adinemood < 0:
                jump bangok_four_adine1_ToD_refused
    
    Ad normal b "那是什么？"
    c "我们彼此问问题，但如果你不想回答，你就得做我告诉你的任何事，反之亦然。"
    Ad disappoint b "我想不出什么要你做的事。至少，没有什么我想说出口的。"
    c "只要在这个房子里，我会做你敢让我做的任何事。"
    Ad think b "真的？任何事吗？"
    c "嗯，要记住，紧接着我也会轮到我，所以要小心一个同样有趣的反击。"
    Ad normal b "好吧，那么谁先开始？"
    c "你问了最后几个问题，所以公平起见，我先开始。"
    Ad annoyed b "公平就是这样吧。"

    show adine normal b with dissolve
    m "我花了一点时间仔细思考我要问什么。"
    menu:
        "你身体哪个部位最怕痒？":
            $ adinemood += 1
            $ renpy.pause (0.5)
            Ad think b "可能是我的侧面，虽然它们不是我最敏感的区域。"
            c "很好知道。为了研究，当然。"
            Ad sad b "你不会滥用这份知识来对付我吧？"
            c "当然不会。除非你让我这样做。"
            show adine think b with dissolve

        "你多紧，多常做爱？":
            $ adinemood -= 1
            Ad frustrated b "什么鬼？这是什么问题？"
            c "一个直接的问题。它用得多还是你仍然--"
            Ad annoyed b "去你的，我认为这问题不值得回答。"
            c "我觉得你--{w=0.5}{nw}"
            call bangok_four_adine1_angercheck
            Ad frustrated b "我接受一个挑战。"
            call .dare_table_1
            
        "你做过最小的运送是什么？":
            Ad think b "我曾经在一个大学派对上。当唯一的飞行员，我的任务是去拿避孕套。"
            c "最小的运送？只有一个盒子还是他们的尺寸那么小？"
            Ad annoyed b "只有五个人，加上我。我不知道他们的尺寸。"
            c "他们不是排队要...你知道的。"
            Ad think b "不，那还有另一个女孩，加上四个男孩。他们都在和她玩，我等了一会儿就无聊离开了。"
            c "啊，说得通。"

    Ad normal b "无论如何，现在轮到我了。你最大的愿望是什么？"

    menu:
        "世界和平。":
            c "比起其他任何东西，我想要地球上有和平。"
            Ad "一个高尚的愿望，虽然有点泛泛。"
            c "虽然泛泛，但我觉得那会让一切感觉好很多。"
            Ad think b "确实，冲突只会给所有参与者带来痛苦。"
        "我想在回去之前尽可能多地和龙做爱。":
            $ adinemood -= 1
            $ renpy.pause (0.5)
            Ad think b "真的，在所有你能有的愿望中，你就只想做爱？"
            c "是啊，挺有意思的！"
            call bangok_four_adine1_angercheck
            Ad disappoint b "我不会评判你，只要你安全地做。"
            c "老实说，我觉得我现在有点懈怠了，如果你懂我的意思。"
            Ad annoyed b "老实说，我不想知道。让我们继续吧。"
        "想住在这里。":
            $ adinemood += 1
            c "老实说，我选择永远住在这里，回到地球也只是为了探访。"
            Ad think b "真的？我知道你没有人会想你，但你不会想家吗？"
            c "不会，这个地方对人类来说真的很舒适。"
            Ad "你真的没有一个人会想你吗？"
            c "没有，我认识的每个人都已经走了自己的路。反过来，还有很多龙我想更了解。"
            Ad giggle b "说得通。让我们继续吧。"

    menu:
        "你在卧室里会戴着护目镜吗？":
            Ad think b "你为什么问这个？"
            c "我只是好奇，我没见过你摘下它们。"
            Ad annoyed b "我觉得这不关你的事。"
            Ad think b "不过，想一想，我好像从没想过在做爱时摘下它们..."
            menu:
                "现在给我示范。":
                    $ adinemood -= 1
                    c "那是我可以接受的提议，来吧，给我一个示范，现在就来，抬高你的尾巴。"
                    Ad frustrated b "你有什么毛病？那不是一个提议。"
                    c "对，但可以是--"
                    call bangok_four_adine1_angercheck
                    Ad "不，不行。"
                "你愿意为我示范吗？":
                    $ adinemood += 1
                    Ad giggle b "也许哪天吧，但不是现在。"
                    c "谢谢你考虑，美丽的。"
                    Ad giggle b "嘿，奉承是作弊！"
                "只是其中的一件事，是吧？":
                    c "我猜这是你从未想过的事情之一，是吧？"
                    Ad think b "是的，我想是这样。"
            Ad normal b "现在轮到我了。你最喜欢龙的什么？"
        "如果你一天隐形你会做什么？":
            Ad think b "隐形，嗯？"
            Ad think b "这不容易回答。我的主要爱好是飞行，我希望人们能看到这点。"
            c "好吧，这个问题更多是关于如果你无法被抓住，你会进行什么恶作剧，比如犯罪或公共自慰。"
            Ad "假装没听到你最后一句，{nw}"
            Ad normal b "假装没听到你最后一句，{fast}其实我知道我要做什么。我会检查他们在传送门旁发现的建筑。"
            c "等等，建筑？"
            Ad "你没听说吗？他们发现了一整个建筑，几乎完整的，和传送门一起。"
            Ad "它其实在地下，除了一个考古学家团队，没人被允许进入。我觉得里面可能有很多关于传送门和它存在原因的秘密和答案。"
            c "有趣。我其实也想看看。"
            $ renpy.pause (0.5)
            Ad normal b "你最喜欢龙的什么？"
        "你是上位者还是下位者？":
            Ad think b "你是指在床上吗？你为什么对这个感兴趣？"
            c "只是好奇，我认为通过平常观察你看不出来。"
            Ad giggle b "好吧，如果你坚持，我其实是个开关。我想。"
            c "你想？"
            Ad think b "我只做过下位者，但那是因为我只和上位者在一起。我其实对尝试掌控感兴趣。"

            menu:
                "现在在这里掌控我。":
                    $ adinemood -= 1
                    c "嘿，我在这里，你现在可以掌控。"
                    Ad annoyed b "如果我想和你做爱，我早就问你了，混蛋。"
                    c "别用那种语气对我，我只是提个建议。"
                    call bangok_four_adine1_angercheck
                    Ad annoyed b "这个建议太过分了。让我们继续。"
                "如果你愿意，我可以给你机会。":
                    $ adinemood += 1
                    $ renpy.pause (0.5)
                    Ad giggle b "好吧，我没想到你这么会调情。也许我会，但不是现在。"
                    c "随时准备好。"
                    Ad "我们到时候再说。现在轮到我了。"
                "也许有一天。":
                    c "也许有一天你会有机会。"
                    Ad "确实。到那时，轮到我了。"
            Ad normal b "你最喜欢龙的什么？"

    menu:
        "自从我来到这里，我一直盯着龙的屁股看。":
            $ adinemood -= 1
            $ renpy.pause (0.5)
            Ad "真的？这就是你所做的一切？真恶心。"
            c "你真的能怪我吗？"
            call bangok_four_adine1_angercheck
            Ad "你一直在盯着我的屁股吗？"
            menu:
                "是的，它很漂亮。":
                    $ adinemood += 1
                    $ renpy.pause (0.5)
                    Ad giggle b "至少你诚实，小变态。"
                "是的，而且它很胖。":
                    $ adinemood -= 2
                    c "我有，它是我见过最胖的龙屁股之一。"
                    $ renpy.pause (0.5)
                    Ad sad "什么？为什么你--"
                    c "不不，这不是坏事！我喜欢它胖！"
                    Ad sad "我--让我们继续。"
                "没有。":
                    $ renpy.pause (0.5)
                    Ad annoyed "我可能不喜欢变态，但我还是更喜欢一个诚实的变态。"

        "你们都有自己优雅的方式。":
            $ adinemood += 1
            Ad think b "怎么说？"
            c "嗯，看看有翅膀的龙，比如你自己。你可以迅速在空中飞翔，高高地乘风而上。"
            c "而像警察局长那样的大型四足龙，看起来像野兽，似乎可以轻松地拖动和自己一样大的实心钢块。"
            c "然后是双足龙，虽然不像人类那么灵活，但他们仍然可以用手轻轻移动东西。"
            Ad "嗯，我从没想过，但你说得对。"
            c "更不用说他们美丽的鳞片图案，比如你的。"
            Ad giggle b "不过不是我的鼻环。"
            c "是的，我喜欢你的鼻环。"
            Ad giggle b "好吧好吧，够了奉承。"
        "没什么特别的。":
            $ adinemood -= 1
            c "老实说，没什么特别的。人类更敏捷，我只是觉得他们更好看。"
            Ad "说得通，我猜你更喜欢自己的物种。不过，一些龙有翅膀能飞，对吧？"
            c "是的，但我一直觉得翅膀有点丑，它们让我想起蝙蝠。"
            Ad sad "天哪，你不必这么说。"
            c "糟糕，对不起，我不是--"
            call bangok_four_adine1_angercheck
            Ad sad "是你轮到问问题了，对吧？"
            c "是的，确实是。"

    c "好吧，我的问题。"
    show adine think b with dissolve

    menu:
        "如果我让你和我做爱，你会吗？":
            $ renpy.pause (0.5)
            if adinemood >= 2:
                show adine giggle b with dissolve
            else:
                show adine annoyed b with dissolve
            Ad "这是个好问题。你不会得到答案；我选择一个挑战。"
            call .dare_table_2
        "你飞得最高有多高？":
            Ad think b "我不确定。应该很高。我发现当所有东西在你下面看起来像蚁丘时，你会很快失去信心，而且唯一能集中注意力的事情就是你能多快掉下来。"
            c "想象一下，我不知道为什么有人会害怕终端速度。"
            Ad giggle b "你让我想起了通过文字传达语气有多难。我不得不重读我书中的几行，因为作者没有告诉我一个角色在讽刺。"
        "你有没有试过倒挂着睡觉？":
            $ adinemood += 1
            Ad think b "那听起来很荒唐。我为什么要那样做？"
            c "地球上有一种会飞的哺乳类动物就那样做。你有点让我想起它们。"
            Ad normal b "好吧，我最后一次检查时我不是哺乳动物，但说得通。这听起来很像蝙蝠。"
            c "等等，它们在地球上也叫这个名字。奇怪。"
            Ad giggle b "很高兴我能让你想起它们，它们很可爱。"
        "你曾经在飞行中小便吗？" if persistent.bangok_watersports:
            Ad annoyed b "呃，别让我想起那一次。是的，有一次。幸好我离城很远，下面没人。"
            c "所以你有做过。感觉怎么样？"
            Ad think b "比在地上做不那么乱，但感觉不对。如果你明白我的意思，好像“嘿，你应该在下面做这个”。"
            c "对，确实。"

    Ad normal b "好吧，到目前为止，你在这里遇到的龙中，你最喜欢谁？"

    menu:
        "你":
            $ adinemood += 1
            Ad giggle b "我？抱歉，这是不是有点早了？"
            c "也许是，但到目前为止你给我的印象最好。"
            Ad normal b "谢谢。也许有一天。"
        "雷米" if remyscenesfinished > 0 and remystatus in ["neutral","good"] and not remydead:
            $ adinemood += 1
            Ad think b "他啊？谢谢。他需要有人照顾他。"
            c "你为什么这么说？"
            Ad normal b "没什么特别的，我只是担心他而已。"
        "布莱斯" if brycescenesfinished > 0 and brycestatus in ["neutral","good"] and not brycedead:
            Ad giggle b "他确实是个很好的选择，不是吗？"
            c "那么强壮，那么忠诚，而且很有魅力。"
            Ad normal b "而且听说他在好几英里范围内酒量最大。" ## 你是故意用“英里”这个词的吗？
        "安娜" if annascenesfinished > 0 and annastatus in ["neutral","good"] and not annadead:
            $ adinemood -= 1
            Ad annoyed b "老实说，我不知道你看上她什么了。"
            c "你是什么意思？"
            Ad think b "那天的那个婊子？她在每个可能的场合都对每个人粗鲁？"
            c "我知道，她有点粗糙，但我觉得她不仅仅是这样。"
            Ad frustrated b "那是什么意思--{w=0.5}{nw}"
            Ad annoyed b "那是什么意思--{fast}算了。我不想谈这个。"
        "洛雷姆" if loremscenesfinished > 0 and loremstatus in ["neutral","good"] and not loremdead:
            Ad think b "抱歉，我不认识这个名字。是谁？"
            c "可爱的送货飞行员，蓝色鳞片。"
            Ad "其实我好像见过他几次，但从没知道他的名字。"
        "现在下结论太早了":
            Ad normal b "是的，这说得通。你在这里的时间不长。"
            c "我想等到感觉对了再说。"
            Ad think b "老实说，我也是这样感觉的。你不能强求这些事情。"
        "接受挑战":
Ad giggle b "早该如此！"
            Ad think b "嗯，我该怎么对付你呢？"
            if adinemood < 3:
                c "你想要什么都行。"
                Ad disappoint b "我真的没有头绪。"
                c "要不我们先暂停一下？"
                Ad think b "是的，我们先进行你的回合。"
            else:
                c "你想要我做什么都行。"
                Ad think b "好吧，我一直对某件事很有兴趣。"
                c "那是什么呢？"
                Ad normal b "你介意把衣服脱掉吗？我从没见过不穿衣服的人类。"
                menu:
                    "脱光衣服。":
                        m "我毫不犹豫地脱下衣服，赤裸身体给艾丁看。"
                        Ad think b "比我想象的要光滑。实际上看起来有点可爱。"
                        c "谢谢。我暂时把这些放在一边。"
                    "解释人类视裸体为性的。":
                        Ad sad b "哦，抱歉，我不是故意的。我不知道，我只是--"
                        menu:
                            "脱光衣服。":
                                $ adinemood += 1
                                m "我开始脱衣服，无视艾丁突然的沉默。她脸红了，似乎很享受观看。"
                                Ad giggle b "谢谢！我想。天哪，现在我觉得我欠你点什么。"
                                c "也许以后我会要求报答。或者也许你的下一个挑战会很痛苦。"
                                Ad normal b "别逼我太紧！不过谢谢。我真的很好奇。"
                            "安慰她。":
                                c "别担心，我怀疑你有很多人类告诉你衣服的重要性。"
                                Ad giggle b "对吧？我只是想知道你长什么样。我不知道我听起来有多直接。"
                                c "你有什么备用的挑战吗？"
                                Ad think b "很遗憾，没有，那是我唯一想到的。"
                                c "那我们以后再说这个吧。"

    menu:
        "如果我敢让你和我做爱，你会吗？":
            Ad giggle b "好吧，你真直接。"
            c "也许，但我真的想知道。"
            Ad normal b "为什么不试试呢？看看结果吧。"
        "反过来。你对谁最感兴趣？":
            Ad giggle b "哦不，你别想。这次我接受挑战。"
            c "对我来说也不错。"
        "你经常用尾巴当电话吗？":
            Ad think b "你--什么？这是什么意思？"
            c "你知道，它大致像个电话。你有没有用它作为电话？"
            Ad disappoint b "我真的不知道怎么回答。我接受挑战。"
    jump .dare_table_3

label .dare_table_1:
    menu:
        "抬起屁股让我试试。":
            $ adinemood -= 2
            $ renpy.pause (0.5)
            Ad frustrated b "说真的？你就只想着这个？"
            c "你真的--"
            Ad frustrated b "去你的，去你的这个地方。"
            if adinemood < 0:
                $ renpy.pop_call()
                call bangok_four_adine1_angercheck
        "我敢你接受我的道歉。":
            $ adinemood += 1
            $ renpy.pause (0.5)
            Ad annoyed b "这是你道歉的方式？"
            c "是的，因为我真的抱歉。我以为我们在...你懂的..."
            Ad disappoint b "好吧，我猜我会原谅这个误会，但只是因为你的道歉有点聪明。"
        "脱光衣服！":
            $ headgear = False
            $ renpy.pause (0.5)
            show adine normal b with dissolve
            Ad "就这个？好吧，我猜。"
            stop music fadeout 1.0
            show black with fade
            play sound "fx/undress.ogg"
            $ renpy.pause(2.5)
            show adine giggle
            hide black
            with fade
            play music "mx/serene.ogg"
            Ad "好了。满意了吗？"
            c "当然，你有个好看的脸。"
            Ad frustrated "如果你认为奉承会让我原谅你粗鲁的行为，那你错了。"
            if persistent.c1disrobement == False:
                $ mp.disrobement = True
                $ mp.save()
                $ persistent.c1disrobement = True
                $ achievement.grant("Disrobement")
                $ persistent.achievements += 1
                call syscheck from _call_bangok_four_syscheck_48
                play sound "fx/system.wav"
                if system == "normal":
                    s "你让艾丁脱光了衣服！"
                elif system == "advanced":
                    s "你让艾丁脱光了衣服。哇。"
                elif True:
                    s "你让艾丁脱光了衣服。有趣的要求她摘下头饰的方法。"
            Ad normal "无论如何，让我赶紧把这些穿上，我已经习惯了它们的重量，摘掉它们反而不习惯。"
            show black with fade
            play sound "fx/undress.ogg"
            $ renpy.pause(1.0)
            show adine normal b
            hide black
            with fade
            $ renpy.pause (0.5)
    return

label .dare_table_2:
    menu:
        "吻我！":
            $ renpy.pause (0.5)
            Ad think b "这是你的挑战？"
            c "是的。"
            Ad annoyed b "好吧，我会做的。"
            stop music fadeout 1.0
            scene black with fade
            play sound "fx/kiss.wav"
            $ renpy.pause(1.0)
            scene o2 at Pan((0, 250), (0, 250), 0.1)
            show adine giggle b
            with fade
            play music "mx/serene.ogg"
            Ad giggle b "好了，满意了吗？"
            show adine normal b with dissolve
            c "绝对满意。"
        "吃一个生土豆。":
            $ adinemood -= 1
            Ad "我不知道你有这么邪恶。"
            c "你会做吗？"
            show adine annoyed b with dissolve
            Ad "好吧。"
            c "你可以在餐具室找到一个。"
            hide adine with dissolve
            play sound "fx/drmg.wav"
            $ renpy.pause(4.0)
            show adine normal b with dissolve
            m "艾丁去了餐具室，回来时手里拿着一个土豆。"
            Ad "呃，你不能选择一个更轻松的挑战吗。"
            c "这就是乐趣，对吧？"
            Ad "我发誓如果我有个好主意，我一定会报复的。"
            stop music fadeout 1.0
            show black with fade
            play sound "fx/bite.wav"
            $ renpy.pause(1.0)
            m "艾丁把土豆放进嘴里咬了一口。对于她的下巴来说，这个土豆太小了，一口就咬掉了一半，但她的脸形使得它很难塞进去。"
            m "艾丁迅速咀嚼着，显然不喜欢这种苦涩、淀粉质的口感。"
            m "过了一会儿，她吞下了它，然后把另一半放进嘴里，比前半部分更快地下咽。"
            show adine normal b
            hide black
            with fade
            play music "mx/serene.ogg"
            Ad "好了。谢谢你，现在轮到我了。"
        "把两根爪子插进你的阴道。":
            $ adinemood -= 1
            Ad annoyed b "你想让我自慰？"
            c "好吧，不是完全的。"
            call bangok_four_adine1_angercheck
            Ad disappoint b "好吧，给我点时间。我不习惯有观众。"
            stop music fadeout 1.0
            show black with fade
            $ renpy.pause (1.5)
            $ adinemood += 2
            Ad giggle b "嗯，嗯，天哪，我这么快就湿了吗？"
            Ad "哦，是的，这感觉好多了！我--等等！"
            hide black with fade
            Ad "抱歉，我有点失控了。"
            c "我不介意。感觉有点压抑吗？"
            Ad "有点，我会回家处理这个问题的。"
    return

label .dare_table_3:
    menu:
        "让我看看你的屁股。":
            jump .ending
        "我想看看你的屁屁，如果这不过分的话。":
            jump .ending
        "裸体在外面裸奔！":
            Ad think b "等一下，除了头饰外，我已经是裸体了..."
            c "我没想好这件事。"
            Ad "哦！我刚注意到，雨停了！"
            c "我猜是时候你该出发了，是吧？"
            Ad "我猜也是。"
            Ad giggle b "顺便说一下，你不需要点任何东西，如果你想让我再过来。这里是我的私人号码。"
            c "谢谢，我会记住的。"
            Ad "再见！"

label .ending:
    if adinemood < 2:
        jump .poor_ending
    elif adinemood < 5:
        jump .med_ending
    elif adinemood < 7:
        jump .good_ending
    else:
        jump .best_ending

label .poor_ending:
    Ad annoyed b "这是你的挑战？说真的？"
    c "好吧，你会做吗？"
    Ad annoyed b "看起来雨停了。我该回家了。"
    c "抱歉。我们还是朋友吗？"
    Ad "我们会看到的。我会留个号码给你。"
    hide adine with dissolve
    m "艾丁在一张废纸上写下几个数字，然后什么也没说就走了。"
    stop music fadeout 2.0
    m "不过在她离开的时候，她回头看了我一眼，朝我投以无奈的表情，然后举起她的尾巴，完全展示了她那天使般的后臀。"
    play sound "fx/door/doorclose3.wav"
    $ renpy.pause(0.5)
    m "然后，她就这样走了。我只是松了一口气，她至少看起来原谅了我一点点。"
    $ persistent.adine1skip = True
    $ adinestatus = "neutral"
    $ adinescenesfinished = 1
    jump _mod_fixjmp

label .med_ending:
    Ad think b "嗯，这是你的挑战？"
    c "是的。我想看看。"
    Ad giggle b "你真是个色鬼，是吧？"
    c "如果我说不是，那我就是撒谎。"
    Ad annoyed b "好吧。"
    hide adine with dissolve
    m "不再说一句话，艾丁转过身，高高举起她的尾巴，展示她那美丽的臀部。"
    Ad giggle b "喜欢这景色吗？"
    c "当然喜欢，谢谢。"
    Ad normal b "好，因为看起来雨已经停了，我该走了。"
    show adine normal b with dissolve
    m "艾丁在一张废纸上写下一个号码，递给我。"
    Ad "这里，如果你想再看我，不需要再点食物了。"
    hide adine with dissolve
    play sound "fx/door/doorclose3.wav"
    $ renpy.pause(2.0)
    stop music fadeout 1.0
    $ persistent.adine1skip = True
    $ adinestatus = "neutral"
    $ adinescenesfinished = 1
    m "我们互道再见，她走出了建筑，留下我心情激动。"
    jump _mod_fixjmp

label .good_ending:
    Ad giggle b "我的天，这么直接的要求。我喜欢。"
    c "那么呢？"
    hide adine with dissolve
    m "艾丁回答了我的问题，转过身来，卷起她的尾巴，把末端的弯钩拉回来，分开她明显湿润的裂缝。"
    Ad disappoint b "我承认，呆在这里让我有点兴奋。只是很遗憾这是第一次约会。"
    c "我不介意帮你，你知道的。"
    Ad giggle b "那是个诱人的提议。确实如此，我想要。"
    Ad disappoint b "但这是第一次约会，我必须逗逗你！"
    c "确实。也许改天吧。"
    Ad normal b "同时，你记住了吗？你需要这个来自慰。"
    c "哦，绝对记住。我永远不会忘记。"
    Ad giggle b "好，因为看来雨停了。我回家也要自慰。"
    $ renpy.pause (1.0)
    m "最后，她放下尾巴，顶端在我的地板上滴了滴水，她拿起一些纸，在上面写下她的电话号码。"
    stop music fadeout 1.0
    m "在和我道别后，艾丁开始朝门口走去。不过，在她离开的时候，她又一次移开了尾巴，回头对我笑了一下，进一步逗弄我。"
    play sound "fx/door/doorclose3.wav"
    $ renpy.pause(2.0)
    $ persistent.adine1skip = True
    $ persistent.headgear = headgear
    $ adinestatus = "good"
    $ adinescenesfinished = 1
    jump _mod_fixjmp

label .best_ending:
    Ad think b "你真的很色，是不是？"
    c "超过一点点。"
    Ad giggle b "你和我一样，你真的让我激动起来了。"
    c "那么呢？"
    Ad normal b "我会做得更好。躺下，让我表现，不需要你费力。"
    ## 如果玩家不想和艾丁做爱，这里实现弹出序列，除非开头已经算作弹出序列。
    stop music fadeout 2.0
    play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/undress.ogg"]
    show black with dissolve
    $ renpy.pause(0.4)
    m "不加思索，我顺从地躺下，耐心等待艾丁走近。"
    m "如她所承诺，她不仅仅是向我展示她的后臀。她坐在我的胸口，低头看着我的眼睛，她湿润的裂缝在我身上摩擦。"
    m "当我们的目光相遇，脸上泛起红晕，她用低沉柔和的语调说话。"
    Ad think b "那么，你的舌头有多好？"
    c "足够好。"
    c "为什么，想教我龙是什么味道吗？"
    Ad giggle b "你欠我这么多，让我激动成这样。"
    m "她站起来，转过身。我有很多机会反对，如果我选择这样做，但我选择不反对。我闭上眼睛，张开手臂，她把屁股轻轻放在我的鼻子上，她湿漉漉的龙裂缝就在我舌头的范围内。"
    m "我毫不犹豫地抱住她的屁股，伸出舌头舔她。"
    Ad giggle b "哦，对，就是这样，[player_name]。"
    m "她的情欲呻吟重复了这个意思，当我大口大口地吸食她的液体时。"
    m "我感觉到自己因为这种近距离和气味的迷人混合而更加兴奋。"
    Ad think b "我希望你享受自己--嗯...就像我享受你一样。"
    m "我无法通过脸上的龙屁股回应，但几下安慰性的拍打她的臀部给了所有需要的保证。"
    m "过了一会儿，艾丁开始不由自主地摆动她的臀部，似乎接近高潮。"
    play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/varagrowl.ogg"]
    m "又过了一会儿，她高潮了，她的汁液溅到我的舌头上，而我还在继续舔。"
    m "当她开始平静下来时，她慢慢地从我身上滚下来，让我坐起来，与她对视。"
    $ renpy.pause (0.3)
    play sound "fx/undress.ogg"
    hide black
    show adine giggle b
    with dissolvemed
    Ad "谢谢，我真的需要这个。"
    c "不客气。现在轮到我了？"
    Ad normal b "改天再说。看来雨停了。"
    c "你欠我一个，明白吗？"
    Ad giggle b "是的，同意。这是我的私人号码。让我们再见面吧。"
    m "艾丁在一些废纸上写下她的号码，放在桌子上。"
    hide adine with dissolve
    play sound ["fx/silence.ogg","fx/silence.ogg","fx/silence.ogg","fx/door/doorclose3.wav"]
    m "在和我互道再见后，她走出了大门，留下我没有龙来满足我的欲望。"
    $ renpy.pause(1.0)
    $ persistent.adine1skip = True
    $ persistent