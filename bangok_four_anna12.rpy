init python:
    bangok_four_anna1_discourseonmorphologicalvariations = True
    bangok_four_anna1_sexrequested = False

init python in bangok_four_anna2:
    unplayed = True

    boughtcondoms = False
    havecondoms = False

    havestrapon = False
    havefauxcum = False
    leash = False

    waitvert = True
    finger = True
    lick = True

    position = None
    hornsgrabbed = None

    annacame = False

    tail = False

    annacomment = ""
    doneoral = False
    fisting = False

    straponplayerreceiveoral = False


label bangok_four_anna1_skipmenu:
    play sound "fx/system3.wav"
    s "与安娜打赌做爱?"
    menu:
        "是的。与安娜打赌做爱。":
            if bangok_four_common.bangnokay.check():
                play sound "fx/system3.wav"
                s "哦，恐怕这不在桌面上。下次祝你好运。"
            else:
                $ bangok_four_anna1_sexrequested = True
        "不。没那么远。":
            pass
    jump bangok_four_anna1_skipmenu_return

label bangok_four_anna1_winmenu:
    $ bangok_four_anna1_sexrequested = False
    menu:
        c "比方说，如果我赢了......"
        "真正的约会.":
            jump bangok_four_anna1_winmenu_return
        "做爱.":
            c "我们打赌如果我赢了{fast} 你会和我发生性关系."
            if bangok_four_common.bangnokay.check():
                An disgust flip "什么鬼?"
                An face flip "我不知道你这边是什么感觉，但你不能在第一次和别人去喝咖啡时问这种事情。"
                $ renpy.pause (0.5)
                An sad flip "..."
                $ renpy.pause (0.5)
                An normal flip "不如，我们让它更随意一点——"
                jump bangok_four_anna1_winmenu_return
            else:
                $ bangok_four_anna1_sexrequested = True
                An face flip "我想你希望我回应，“如果我赢了，我就可以和你发生性关系”？"
                c "好吧，我不能说我会反对这一点。"
                An smirk flip "太糟糕了。如果我赢了，我会让你在某个时候进来我的实验室，这样我就可以对你进行更多的测试。"
                if blood == False:
                    An "我甚至不再需要你的血了."
                jump bangok_four_anna1_winmenu_afterannablood
        "关于龙物种形态变异的论述，包括大脑、身体和社会因素，特别感兴趣的是理解尽管进化途径明显不同，但智力水平显然相当。" if bangok_four_anna1_discourseonmorphologicalvariations:
            c "我们打赌如果我赢了{fast} 你能帮我理解所有这些龙种是如何以相同的智力水平产生的？有点生物学上的权衡。"
            python:
                bangok_four_anna1_discourseonmorphologicalvariations = False
                annamood -= 1
            An face flip "开什么玩笑？"
            An sad flip "我看起来有时间和你一起复习龙生物学101吗？"
            An face flip "只需从图书馆拿起一本教科书即可。"
            An sad flip "如果您有什么高级问题，那么也许会。但是教你基础知识? 不值得, 不过是一个孩子的游戏。"
            c "哦。那好吧。花费更少时间的东西......"
            jump bangok_four_anna1_winmenu

label bangok_four_anna1_medending:
    An normal flip "但你知道吗，这毕竟没有那么糟糕。也许我会让你做爱。"
label bangok_four_anna1_ending_merge:
    c "真的？我很惊讶你对此没意见。"
    An normal flip "这不是不合理的，我当然不会让你回头。"
    An sad flip "为什么？你{i}不想{/i}和我发生性关系吗？"
    menu:
        "我可没这么说。":
            An smirk flip "那就没问题了。"
            An normal flip "不过，我暂时不会在实验室里做测试，所以我想下次我们见面时，会是为了做爱。"
        "人类有这样一句话， \"晚餐和电影......\"":
            $ bangok_four_anna1_sexrequested = False
            An normal flip "好。然后，我们可以将您的赌注结束时间给给到一个约会。"
            An smirk flip "除非事情进展得非常顺利。"
            c "这对我来说听起来很公平。"
            An normal flip "不过，我暂时不会在实验室里做测试，所以我想下次我们见面时，会是为了约会。"
        "我这么说是为了报复你的粗鲁。":
            $ bangok_four_anna1_sexrequested = False
            $ annamood -= 2
            An face flip "真不敢相信."
            c "听着，对不起。如果我们，我不知道，去看电影怎么办？"
            An sad flip "什么，比如约会?"
            An face flip "我真的希望你不要突然试图把它扭曲成更长期的东西。"
            $ renpy.pause(0.8)
            An normal flip "好。我暂时不会在实验室里做测试，所以我想下次我们见面时，会是你的这个约会。"
    c "行啊."
    if annaanswers == 3:
        jump bangok_four_anna1_goodending_after_thankyou
    else:
        jump bangok_four_anna1_medending_uptoyou

label bangok_four_anna1_goodending_nvl:
    n "尽管我强迫她和我发生性关系的赌注更多的是为了报复她之前的粗鲁行为，但我没有预料到这个结果。一开始我甚至不确定我对这次会面的期望是什么，但现在我被锁定在与她发生性关系中，并成为她自己的私人豚鼠。"
    if bangok_four_malepartners + bangok_four_femalepartners < 1:
        n "我以前没有尝试过龙。到时候这还能让我产生性趣吗？"
    else:
        n "我以前睡过一条龙，但睡安娜似乎是一种全新的体验。"
    jump bangok_four_anna1_goodending_nvl_end

label bangok_four_anna1_medending_nvl:
    n "毕竟，求婚是我向她提出性行为的方式，因为她很粗鲁。"
    n "即使我输了赌注，她似乎也不介意和我发生性关系，只要她得到她想要的东西。不过，我是否会跟进取决于我。"
    if bangok_four_malepartners + bangok_four_femalepartners < 1:
        n "我以前没有尝试过龙。到时候这还能让我产生性趣吗？"
    else:
        n "我以前睡过一条龙，但睡安娜似乎是一种全新的体验."
    jump bangok_four_anna1_medending_nvl_end

label bangok_four_anna1_badending:
    An normal flip "我想你只是在经历剧烈的后痛，因为你现在不能和我发生性关系。"
    menu:
        "我从一开始就不想和你发生性关系":
            c "我从一开始就不想和你发生性关系, 我只是想教你一些礼仪."
            An disgust flip "就像我曾经和你这样的哺乳动物发生过性关系一样。"
            c "哦，我现在对你还不够好吗？"
            An normal flip "坦率地说，如果你是一个大使，一个人类的光辉榜样，我会说你的整个物种对任何人来说都不够好。"
            An sad flip "这就是你散发出文明和谦逊等美德的方式? 试图强迫某人与你发生性关系?"
        "我没想到会输。":
            c "这是一个孩子的游戏。这不应该这么难。"
            An disgust flip "你居然想在打赌时强迫我做爱？而且我没有任何好处？"
            c "我可以对你说同样的话，试图强迫我进行一堆实验。你要干什么，把我切开？"
            An normal flip "当然不是。你认为我们活在什么年代，{i}第一次战争{/i}？我有更好的方法来观察你的身体内部。"
            An sad flip "并不是说我敢肯定我什至想看到这一点，你假装散发出的文明和谦逊的扭曲."
    jump bangok_four_anna1_badending_end









label bangok_four_chap2storehealth_anna12:
    if bangok_four_playerhasdick == True:
        m "想起我和安娜的安排，我意识到我可能应该得到一些保护。毕竟，我正在与一个完全不同的物种打交道。"
    else:
        m "想起我和安娜的安排，一个关于她的尾巴的侵入性想法突然出现在我的脑海中。"
    menu:
        "购买避孕套。":
            $ bangok_four_anna2.boughtcondoms = True
            "我拿起一个小尺寸的盒子，盒子上贴着驰龙的标签"
            c "(希望这对店员来说不会太奇怪。)"
        "还是别了":
            $ bangok_four_anna2.boughtcondoms = False
            c "(他们可能在某个地方的公寓里有一些。否则我就不需要这个了。)"
    jump bangok_four_chap2storehealth_anna12_return

label bangok_four_chap2storehealth_checkout_anna12:
    play sound "fx/register.ogg"
    $ renpy.pause (5.0)
    stop sound fadeout 1.0
    m "店员检查了我拿的东西，没有发表评论。"
    jump bangok_four_chap2storehealth_checkout_anna12_return















label bangok_four_anna2_nomorewaiting:
    m "最后，我决定受够了。我不想再等了，我离开了，尽管她仍然欠我一次做爱。"
    jump bangok_four_anna2_nomorewaiting_end

label bangok_four_anna2_wantthisornot:
    An disgust "我刚刚告诉过你，我是，所以从我的背上下来。你到底想不想操我？"
    jump bangok_four_anna2_wantthisornot_end

label bangok_four_anna2_whatnow:
    An "好吧，我们不是在实验室里这样做的。我想我们可以回到你那个由政府资助的公寓里。"
    menu:
        "为什么不呢？":
            $ renpy.pause(0.5)
            $ anna2mood -= 1
            An face "因为它几乎可以保证我们会破坏一些东西."
            An sad "更不用说卫生问题了."
            c "好了，好了。到了, 这就是我的地方。"
            if anna2mood >= 0 and persistent.bangok_dev == True:
                An normal "也就是说，我想得到一些我藏在实验室里的东西。"
        "行啊.":
            $ renpy.pause(0.5)
            $ anna2mood += 1
            if anna2mood >= 0 and persistent.bangok_dev == True:
                An smirk "啊，差点忘了。我在实验室里落下了一些东西。"
        "这样的等待让我有点饿了......":
            $ renpy.pause(0.5)
            An face "这应该是一个“外出就餐”的笑话吗？因为我有坏消息要告诉你."
            menu:
                "事实正是如此。":
                    $ renpy.pause(0.5)
                    c "你说的坏消息是什么意思？"
                    An normal "我不喜欢牙医。尤其是你的，没有嘴巴就不能把嘴放在我的生殖器上。"
                    c "哦."
                    An "忘掉它。让我们来做这个。"
                    if anna2mood >= 0 and persistent.bangok_dev == True:
                        An face "哦，该死的。差点忘了。我在实验室为此准备了一些东西。"
                "不，我是字面意思。":
                    An sad "你希望我做什么，为你用魔法变出食物？"
                    c "出去吃饭并不疯狂，尤其是因为我假设你也没吃过东西。"
                    An "好。也许咖啡店还开着。我也不知道。"
                    jump bangok_four_anna2_alley

    if anna2mood >= 0 and persistent.bangok_dev == True:
        c "Oh?"
        hide anna with dissolve
        play sound "fx/door/door_open.wav"
        $ renpy.pause (3.0)
        show anna normal with dissolve
        m "她带着一个皮革手提包回来了，关上了自己身后的实验室门。"
        $ bangok_four_anna2.havestrapon = True
        menu:
            "这里面有什么？":
                $ renpy.pause(0.5)
                $ anna2mood += 1
                An smirk "我会私下给你看."
            "真的?":
                $ renpy.pause(0.5)
                An normal "是的."
            "那是你的钱包吗？":
                $ renpy.pause(0.5)
                $ anna2mood -= 1
                c "大名科学家随身携带小淑女钱包吗?"
                An sad "这不是钱包."
                c "那么里面有什么呢？"
                An normal "继续发表这样烦人的评论，也许我就不会给你看了."

    $ renpy.pause(0.9)
    jump bangok_four_anna2_apartment

label bangok_four_anna2_romanticdate_alley:
    An sad "对不起?"
    c "我的意思是，去吃晚饭，基本上就是这样."
    An face "这不是我所同意的."
    c "但你也饿了，对吧？我不会让你不吃晚饭就和我发生性关系。"
    An "..."
    c "我的公寓里应该有一些食物供应。我会想办法为我们做饭的。"
    An normal "实际上，我知道一个应该仍然开放的地方。"
    An smirk "我怀疑它会比你计划的任何东西都好。"
    c "行啊."
    jump bangok_four_anna2_romanticdate_alley_end

label bangok_four_anna2_romanticdate_unusualbutfun:
    if anna2mood > 4:
        An smirk c "好玩吗？谁说晚饭后乐趣就停止了？"
        if bangok_four_anna1_sexrequested == True:
            c "哦，对了。我差点忘了。"
        else:
            c "Oh?"
    elif anna2mood > 0 and bangok_four_anna1_sexrequested == True:
        An normal c "这也不是晚上的结束."
        c "哦，对了。我差点忘了."
    else:
        An sad c "好吧。至少我们中的一个人正在享受它."
    jump bangok_four_anna2_romanticdate_unusualbutfun_return

label bangok_four_anna2_romanticdate_conclusion:
    if bangok_four_anna1_sexrequested == False:
        if anna2mood > 4 and not (bangok_four_common.bangnokay.check()):
            An sad c "我不得不说，考虑到今晚的进展情况，我很惊讶。"
            c "好吧，我不能把所有的功劳都归功于他。"
            An normal c "你可以吃够了。"
            An sad c "我知道我们计划的电影没有成功，但是......"
            An smirk c "如果我们把我的狩猎能力看作是一场表演，那就是晚餐和电影。"
            c "Oh?"
            An "在我们收工之前，你想做点别的事情吗？"
            menu:
                "接受.":
                    pass
                "拒绝.":
                    c "不,谢谢。你已经完全完成了我们的赌注."
                    $ anna2mood += 1
                    An normal c "你输了."
                    An "那么，这已经足够了。回到设施，这样我就可以清理并完成一些事情。"
                    jump bangok_four_anna2_romanticdate_conclusion_return
        else:
            menu:
                "这真的是我们的整个约会吗?":
                    c "你知道，人类有一句谚语：“吃饭和看电影。"
                    An normal c "我们也有这句话。"
                    c "好吧，我们刚刚吃了饭，你的狩猎能力真是太棒了..."
                    An face c "那真的应该是一条接送线吗？"
                    if anna2mood < 1 or (bangok_four_common.bangnokay.check()):
                        c "你敢打赌是."
                        An disgust c "滚开。"
                        An normal c "我同意了一个约会，没有别的。"
                        An "如果你想要更多机会，你必须坐下来看我的实验，然后找到我愿意用它来换取的其他东西。"
                        $ renpy.pause(0.8)
                        c "..."
                        $ renpy.pause(0.8)
                        An sad c "跟着我回设施就行了。我需要给它收尾，我还有一两件事要完成。"
                    else:
                        c "视情况而定，你有兴趣吗?"
                        if anna2mood > 2:
                            An normal c "..."
                            An smirk c "我可能是."
                        else:
                            An sad c "..."
                            An normal c "不."
                            c "那好吧。忘了我说过什么."
                            An "已经完成了。"
                            jump bangok_four_anna2_romanticdate_conclusion_end
                "[[同意并跟随她。]":
                    jump bangok_four_anna2_romanticdate_conclusion_return

    if bangok_four_anna1_sexrequested == True:
        if anna2mood > 2:
            An smirk c "现在，关于你的奖励。"
            c "我的位置，对吧？"
        else:
            if anna2mood > 0:
                c "所以，关于那个赌注奖励。"
                An face c "没有心情。"
                c "我。。。知道了。我们应该重新安排时间吗？"
                An sad c "那行不通。至少对我来说不是."
                An face c "今天是我唯一可以早点离开的日子。我不会再有下一次机会了。"
                menu:
                    "我理解。":
                        c "我的意思是，这不是我所希望的，但我不会强迫这个问题。"
                        $ renpy.pause(0.8)
                        $ anna2mood += 1
                        An normal c "谢谢。我很高兴你能通情达理。"
                        c "大使还有什么用？"
                        An smirk c "好点子。"
                        c "不管怎样，你说我们可能应该去。"
                        An normal c "对."
                        jump bangok_four_anna2_romanticdate_conclusion_end
                    "这不是我们达成的协议。":
                        pass
            else:
                An sad c "然后回到设施。我想我已经浪费了足够多的时间。"
                c "我的奖励呢？"
                An normal c "哦，对不起。你决定饿着肚子。"
                An sad c "此外，我还以为你不喜欢狂野的一面。你不会想操一个浑身是血的人吧？"
                menu:
                    "你敢打赌我会的。":
                        if nofood == True:
                            An "血液使你失去你的食欲, 但不会失去性欲? 真奇怪."
                        else:
                            An "太糟糕了。"
                    "好吧，也许不是......":
                        An normal c "好."
            c "不过，我们在性方面达成了一致。"
            An sad c "你选择把它选入一个浪漫的约会。那是你的问题，不是我的问题。"
            An normal c "我不会站在这里整夜争论它。"
            c "..."
            scene black with dissolve
            $ renpy.pause(0.5)
            m "走回设施的路让我有机会冷静下来，尽管我无法读懂安娜脑海中的情绪。"
            jump bangok_four_anna2_romanticdate_conclusion_end
    else:
        An smirk c "现在，问题在于我们去哪里。"
        c "我猜我的公寓？"

    An normal c "听上去很好."
    An sad c "不过，我宁愿不要在你的客厅里留下证据，所以我可能需要毁掉一两条毛巾才能把血弄掉。"
    c "行."
    jump bangok_four_anna2_apartment

label bangok_four_anna2_apartment:
    scene black with dissolve
    $ renpy.pause (1.0)
    scene o2 at Pan((0, 250), (0, 250), 0.1)
    show anna normal
    with dissolvemed

    if bangok_four_common.bangnokay.check():
        jump bangok_four_bangnokay_kill_replay

    if bangok_four_anna2.havestrapon == True:
        $ renpy.pause(0.5)
        c "所以。袋子里有什么？"
        show anna smirk with dissolve
        play sound "fx/undress.ogg"
        show anna smirk dildohand with dissolve

        $ renpy.pause(0.8)

        menu:
            "那是双头假阳具吗？":
                $ renpy.pause(0.5)
                c "这些额外的绑带有什么用？"
            "那是绑带吗？":
                $ renpy.pause(0.5)
                An smirk dildohand "是的。"
            "哦，我的天。":
                $ renpy.pause(0.5)
            "不。":
                $ renpy.pause(0.5)
                show anna sad dildohand with dissolve
                c "不管那是什么，我们都没有使用它。"
                label bangok_four_anna2_apartment_nostrapon:
                An sad dildohand "明白了。你介意告诉我为什么吗？"
                menu:
                    "不是我的事.":
                        $ renpy.pause(0.5)
                        An normal dildohand "很公平"
                        play sound "fx/undress.ogg"
                        show anna normal with dissolve
                    "它很大！":
                        $ renpy.pause(0.5)
                        An sad dildohand "较大的一端不会进入 {i}你{/i}."
                        c "即使如此."
                        An normal dildohand "很公平"
                        play sound "fx/undress.ogg"
                        show anna normal with dissolve
                    "你为什么要去把这弄得很奇怪?":
                        $ renpy.pause(0.5)
                        $ anna2mood -= 1
                        play sound "fx/undress.ogg"
                        An face "好吧，我把它收起来。"
                    "不.":
                        $ renpy.pause(0.5)
                        $ anna2mood -= 1
                        play sound "fx/undress.ogg"
                        An face "好吧, 我把它收起来."

                m "安娜把玩具放进包里，放在一边。"
                $ bangok_four_anna2.havestrapon = False
                jump bangok_four_anna2_apartment_under_layers

        An normal dildohand "我买了这个和前任一起使用，但我永远无法说服他。"
        An smirk dildohand "它旨在用作挂钩的绑带，但我相信还有其他几种方法可以使用它。"
        menu:
            "听起来很有趣。":
                $ renpy.pause(0.5)
                $ anna2mood += 1
            "我。。。猜猜我们可以试试。":
                $ renpy.pause(0.5)
            "我不确定那件事。":
                $ renpy.pause(0.5)
                jump bangok_four_anna2_apartment_nostrapon
            "好吧，没门。":
                $ renpy.pause(0.5)
                $ anna2mood -= 1
                jump bangok_four_anna2_apartment_nostrapon
        show anna normal with dissolve
        m "安娜把玩具放在茶几上。"


    label bangok_four_anna2_apartment_under_layers:
    $ renpy.pause (0.5)
    if anna2mood > 0:
        An smirk "我想现在我们看到了所有这些层之下的东西。"
    else:
        An sad "我想现在我们看到了所有这些层之下的东西。"
    if bangok_four_playerhasdick is None:
        menu:
            "展示你的老二":
                $ bangok_four_playerhasdick = True
            "展示你没有老二":
                $ bangok_four_playerhasdick = False

    play sound "fx/undress.ogg"
    $ renpy.pause (1.5)

    if bangok_four_playerhasdick == True:
        label bangok_four_anna2_apartment_maleshow:
        An normal "绝对是哺乳动物。也绝对是男性。"
        menu:
            "实际上，我更喜欢一组不同的代词......":
                An "好。我们不需要代词来使用你的那个东西。"
            "[[什么都不说。]":
                pass

        if bangok_four_anna1_sexrequested == True:
            An "现在，你确实为这个场合买了避孕套，对吧？"
            menu:
                "等等，什么？":
                    c "我们是不同的物种。我很确定我不能让你怀孕。"
                    An sad "在我有机会在实验室里研究你们的生殖器的微生物之前，我宁愿不要发现你们的物种有某种与龙相容的细菌成为性病的起因之一。"
                    c "Ah. 很公平"
                "答案是肯定的。" if bangok_four_anna2.boughtcondoms == True:
                    pass
                "Uh..." if bangok_four_anna2.boughtcondoms == False:
                    pass
            if bangok_four_anna2.boughtcondoms == True:
                $ bangok_four_anna2.havecondoms = True
                show anna normal with dissolve
                c "当然，我买到了一些。"
                m "我取回了我在逛商店时买的盒子，取下了一个用铝箔包裹的小保护装置。"
            else:
                c "Uh..."
                An face "哦，大声哭泣吧"
                menu:
                    "你的包里没有带任何东西吗？" if bangok_four_anna2.havestrapon == True:
                        $ renpy.pause(0.5)
                        $ bangok_four_anna2.havecondoms = True
                        An normal "我做到了，但我认为你会货比三家，以确定什么对你来说是安全的。"
                        c "哦。那么，制作一个安全的避孕套有多难？我相信会没事的。"
                        An "如果它伤害了你，那就是你自己的选择。"
                        m "她递过来一个."
                    "我以为你会带点东西。":
                        $ renpy.pause(0.5)
                        c "毕竟，我是来自另一个世界的访客。"
                        An sad "这就是为什么你有责任选择一个对你安全的。"
                        c "让我们环顾四周。我敢肯定有些是有库存的。"
                    "我以为这个地方会放一点的。":
                        $ renpy.pause(0.5)
                        c "它有我需要的所有其他东西。"
                        An "你找过他们吗？"
                        c "..."
                        An "明白了."
                    "让我们环顾四周。我敢肯定有些是有库存的。":
                        $ renpy.pause(0.5)
        else:
            An face "该死的."
            c "什么?"
            An sad "我没想到会做这样的事情，所以我没有带任何避孕套."
            An normal "在你问之前，不，如果没有一个套套，我不会暴露我的生物学风险去发生性行为。"
            An normal "在我有机会在实验室里研究你们的生物动物之前，我宁愿不要发现你们的物种有某种与龙相容的细菌会变成性病。"
            $ renpy.pause (0.8)
            c "好吧，让我们环顾四周。我敢肯定有些是有库存的。"

        if bangok_four_anna2.havecondoms == False:
            An normal "好。我去检查浴室，你去检查卧室。"
            hide anna with dissolve
            $ renpy.pause (0.5)
            play sound "fx/rummage.wav"
            m "我检查床头柜的第一个抽屉里放着一盒避孕套，塞在后面。"
            m "我回过头来，高高举起它，却发现安娜已经坐在沙发上，旁边还有一个。"
            show anna normal at center with dissolve
            c "等等，你也在那里找到了一些？"
            An smirk "答案是肯定的。我敢肯定他们在整个公寓里都有它们。最好避免与来自另一个世界的大使发生健康事故，对吧？"
            c "哦."
            An "这里。使用这个品牌而不是那个品牌。"
            m "我把找到的盒子放在一边，拿起她递来的单避孕套."

        m "我用手抽了几下才能戴上避孕套。"
        show anna sad with dissolve
        m "安娜有些担心地看着。"
        An "它应该像那样吊在你的身下吗？大多数龙 - 大多数物种 - 都有一个杆状物，以防止它太软而无法插入。"
        menu:
            "什么是杆状体？":
                $ anna2mood -= 1
                An face "没关系."
                An sad "我想只要你努力进去，没关系。"
            "呀，这对我们来说很正常。":
                An normal "明白了。"
            "当我们看到某人或某事进行一些性刺激时，就会变得很硬。":
                if anna2mood > 2:
                    An smirk "行吧."
                else:
                    An "行吧."
        c "那对你来说呢？"
        An normal "你还没看过科学课本吗？"
        c "没有。我更愿意从人们那里了解这些东西，建立联系。"
        if anna2mood > 3:
            An smirk "像这样的连接？"
            c "我不得不说这是出乎意料的，但我认为这将是一件好事。"
        else:
            An face "像这样的连接？"
            c "绝对是的."
            if bangok_four_anna1_sexrequested == True:
                An sad "让我们结束它。"
            else:
                show anna normal with dissolve
    else:
        An normal "绝对是哺乳动物。我猜是女性，因为我敢肯定，作为一个男性，你的鸡巴在性爱的前景中已经可见了。"
        menu:
            "实际上，我更喜欢一组不同的代词......":
                An "好。我们不需要代词来享受你所依附的东西。"
            "[[什么都不说。]":
                pass

        if bangok_four_anna2.havestrapon == False:
            label bangok_four_anna2_apartment_nodick:
            show black with None
            play sound "fx/system3.wav"
            s "很抱歉，但这个模组的作者更倾向于男同性恋的一面，并不打算尝试写 F/F。"
            play sound "fx/system3.wav"
            s "如果您愿意，您可以随时为 mod 的开发贡献 F/F 脚本。"
            play sound "fx/system3.wav"
            s "同时，你想跳到最后吗？或者你能接受以男性的身份继续这个场景吗？"
            menu:
                "是的。我想跳过.":
                    play sound "fx/system3.wav"
                    s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                    hide black with dissolveslow
                    jump bangok_four_anna2_apartment_done
                "不。不要跳过.":
                    play sound "fx/system3.wav"
                    s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                    hide black with dissolvemed
                    jump bangok_four_anna2_apartment_maleshow

        An normal dildohand "我倾向于喜欢更大的插入物，所以你可能应该穿上它。"

    if bangok_four_anna2.havestrapon == True:
        An smirk dildohand "或者你想先收到?"
        jump bangok_four_anna2_apartment_strapon_consideringmenu



label bangok_four_anna2_apartment_annaliesdown:
    # hide anna with dissolve
    # $ renpy.pause(0.3)
    show anna:
        xanchor 0.5
        ease 1.0 pos (0.8, 1.0)
    with None
    $ renpy.pause(0.7)
    show anna:
        pos (0.8, 1.3)
        rotate 15
    with dissolve
    m "安娜退到沙发上，然后坐了下来，尾巴在两腿之间摇晃着坐在沙发上，露出了她的屁股。"
    m "现在在这个位置，我可以清楚地看到她的一条垂直缝隙，隐藏在她双腿之间的一个小凸起上。"
    if persistent.bangok_cloacas == False:
        m "再往下一两英寸，一朵小玫瑰花蕾向我眨眼。"
        
    $ bangok_four_anna2.unplayed = False
    $ bangok_four_femalepartners += 1

    if bangok_four_anna2.havestrapon == False:
        jump bangok_four_anna2_apartment_male_nostrapon_startingmenu
    else:
        An normal "你想先戴上避孕套吗？我有几个可以适配较大的一段的避孕套, 它们被我放在我的包里。"
        c "为什么?"
        An bangok blush "以防你想要射在这里面, 前提是你对你的尺寸自信的话."
        if persistent.bangok_watersports == True:
            An smirk "或是玩弄其他液体."
        An normal "它的感觉基本上没有任何变化，所以我不在乎任何一种方式。我只是想要没有障碍地玩弄你."
        # The player has put his personal condom on already if he's male, so reusing this variable is fine.
        menu:
            "在玩具上戴上避孕套。":
                $ bangok_four_anna2.havecondoms = True
            "不要。":
                $ bangok_four_anna2.havecondoms = False

    show anna bangok blush with dissolve
    m "当我拿着玩具走近时，安娜把双腿张开了一点。"
    An "现在，用你的手指让我做好准备。但是注意你的爪子。我不希望你伤到我的里面的肉。"
    menu:
        "我觉得这不是个问题。":
            c "除非你比那里的人类更脆弱......"
            An normal "不可能那么脆弱。不过，不要做任何愚蠢的事情."
        "你想先润滑它吗？":
            An normal "我什么都没带，你洗手间里也没看到。"
            c "哦."
        "小穴还是你的后穴？":
            An "阴道。我们不要在这里倒退到俚语术语。"
            An bangok blush "以及, 我很抱歉地说，如果没有润滑剂，那它就根本不适合我的肛门，我没有带润滑剂，也没有在你的洗手间看到。"
            c "哦."
    
    $ bangok_four_anna2.finger = False
    m "我走近了，伸手抚摸她的开口。"
    m "过了一会儿，我慢慢地将两根手指按在里面，继续用手的其余部分轻轻地画着小圆圈。安娜悬在空中的双腿微微颤抖。"
    $ renpy.pause (0.8)
    if anna2mood > -1:
        An smirk "你可以继续这样做."
    else:
        show anna sad with dissolve
    $ renpy.pause (0.5)
    m "在这种温柔的挑逗中又给了她一会儿之后，我又加了第三根手指，发现它比前两根更容易滑进去，因为她的天然润滑剂开始滑过她的小穴。"
    if anna2mood < 1:
        An face "好了，停下."
        c "哼？我以为你喜欢这个."
        An sad "只需转到绑带即可。"
    else:
        An smirk "该死你真的说对了。你的爪子完全不是问题。"
        An bangok blush "而且你的皮肤比任何龙的鳞片都要柔软得多."
        menu:
            "[[添加第四根手指。]":
                m "这根手指稍微有一些阻力。但是在她的自然润滑下，它很顺利地进去了，其次是我的大部分手掌。"
                $ anna2mood += 1
                An bangok lipbite "Mm."
                c "继续下去？"
                if anna2mood > 2:
                    $ renpy.pause(0.5)
                    An "是的."
                    m "我轻轻地把手伸进捏出，每动一下，安娜的呼吸都会稍微加快一点。"
                    $ renpy.pause(0.8)
                    An bangok lipbite "现在你开始上道了。"
                    c "Huh?"
                    call bangok_four_anna2_apartment_yourarm from bangok_four_anna2_apartment_strapon_fourthfinger
                else:
                    An bangok blush "让我们继续穿上绑带."
            "[[转到绑带。]":
                pass

    m "我从茶几上拿起玩具，把她的湿漉漉的手指涂到大头的尖端。"
    if bangok_four_anna2.position == "dildo":
        c "你确定你能接受这个大的一端吗？"
        An bangok blush "我在空闲时间有很多练习。我不明白为什么会受不了。"
        if bangok_four_anna2.annacame == True:
            An smirk "尤其是在你把我下面扩张得那么充分之后。"

    if bangok_four_anna2.annacame == True:
        m "安娜的缝隙在我操完胳膊后仍然微微分开，就像我的胳膊仍然随着她的兴奋而闪闪发光一样."
        if bangok_four_anna2.position == "dildo":
            m "我滑下绑带，打算把它留在她身上，只留下双头玩具，我把玩具较大的一端的尖端贴在她的小穴上。"
        else:
            m "我握住绑带，想把它拆下她的身上，我把玩具较大的一端的尖端贴在她的小穴上."
        show anna bangok lipbite with dissolve
        m "它平稳地滑了进去，尽管我可以看到它几乎和我的手臂一样扩张着她。"
        show anna bangok orgasm with dissolve
        m "安娜喘着粗气，而玩具的阻力突然增强，尽管还没有达到我之前观察到的身体颤抖的程度。然后玩具穿过她的宫颈，她的外阴缠绕在玩具宽度减小的地方。我的手指拂过她饱满的缝隙，同时稳稳地握住玩具。"
        c "我才刚刚全部插进去你就去了吗"
        An bangok lipbite "不...不完全是。但也快了..."
    else:
        m "安娜的缝隙因我的手指操而闪闪发光。"
        if bangok_four_anna2.position == "dildo":
            m "我滑下绑带，打算把它留在她身上，只留下双头玩具，我把玩具较大的一端的尖端贴在她的小穴上。"
        else:
            m "我握住绑带，想把它拆下她的身上，我把玩具较大的一端的尖端贴在她的小穴上."
        show anna bangok lipbite with dissolve
        m "它把她撑得大大的，需要一点力气才能滑动，但安娜似乎只是通过扩张的小穴来适应它而进一步兴奋."
        m "即便如此，她还是在玩具较大的一端的中途耗尽了润滑剂，当我未能将它滑得更深时，她鳞片状的小穴向内拉扯。"
        An bangok blush "仔细地。明显地。"
        c "你{i}完全确定{/i}这东西适合你吗？"
        An normal "如果我认为它没有，我会要求你把它放在我身上吗？"
        An bangok blush "只管插就完了"

        m "按照她的要求，我把玩具滑了回去，直到尖端从她的小穴上扯过。她湿漉漉的几乎要滴水了，一团水顺着玩具流下来，滑溜溜地擦湿了她的小穴。"
        An bangok lipbite "然后回到..."
        m "我把它推回她的体内，着迷地看着她小穴上的光滑的淫液从她的紧绷的小穴进一步蔓延到玩具上。"
        m "玩具突然停了下来，大头的四分之三完全在她的体内，并且不是因为没有润滑而卡住。"
        An "继续往里."
        menu:
            "它怎么停下来了？":
                pass
            "安娜，这玩意到头了!":
                $ anna2mood -= 1
            "如果你坚持这么说......":
                $ renpy.pause(0.5)
                m "我把更多的重量靠在玩具上，以为只要再用一点压力，它就会继续深入。不过似乎没有。"
        $ renpy.pause(0.5)
        An bangok blushpalm "哦，看在他妈的份上."
        show anna bangok lipbite with dissolve
        m "她握住我的手腕，向后推了推玩具，示意我应该把它从她身上拉出来."
        m "然后她反转了拉扯，阻止了我."
        An bangok lipbite "现在推进去。再用力些."
        menu:
            "你不是想让我不要在那里伤害你吗？":
                $ renpy.pause(0.5)
                $ anna2mood -= 1
                An bangok blushpalm "我会没事的。你已经操的我大声叫唤了！"
            "[[服从.]":
                pass
        $ renpy.pause(0.5)
        m "我狠狠地把玩具塞了进去，抵住了她身体的阻力，但还是犹豫了。"
        An bangok blushpalm "再来!一路到底!"
        m "我稍微后退了一点，再次用力地往里推。"
        show anna bangok orgasm with dissolve
        m "我不确定这是否是我的想象，但玩具感觉大约有尖端长度的一半"
        show anna bangok lipbite with dissolve
        An "再深点! [player_name]."
        m "我把她的话当作鼓励，把玩具轻轻地往后拉，又推了进去，这次我几乎把我的体重全靠在上面。"
        An bangok blushpalm "更...更接近了..."
        show anna bangok lipbite:
            ease 0.8 xpos 0.8
            ease 0.15 xpos 0.81
            repeat
        with None
        m "我又拉了又推，然后又推了一遍。玩具插得更深了一点，但显然还不足以满足安娜贪得无厌的龙性。"
        $ renpy.pause(0.8)
        play sound "fx/tableslap.wav"
        play sound2 "fx/snarl.ogg"
        $ bangok_four_anna2.annacame = True 
        show anna bangok orgasm:
            xpos 0.8
        with hpunch
        m "然后，突然间，玩具继续深入里面，安娜变成了一个咆哮、颤抖的混乱，她的尾巴拍打着桌子。"
        m "我差点从惊讶中松开手，但我紧紧抓住她的双腿，在这个过程中我试图让她脚上看起来很危险的爪子远离我的身体。"
        show anna smirk with dissolve
        $ renpy.pause(0.5)
        m "安娜咧嘴一笑，从性高潮中下来。"
        $ renpy.pause(0.5)
        An "终于...当我独自一龙时，我是很难获得这种快感的."
        menu:
            "你没事吧？":
                $ renpy.pause (0.9)
                $ anna2mood += 1
                An smirk flip "实际上, 我他妈爽爆了."
            "刚刚发生了什么？":
                $ renpy.pause (0.6)
                An "你终于把那个玩具穿过了我的子宫颈。"
            "那个玩具现在你的子宫里了吗？":
                $ renpy.pause (0.5)
                An smirk flip "是的, 是的，它整个进去了."
        An bangok blush "我都跟你说了我更喜欢更大的. 还有你为什么会觉得那玩意太大了?"
        An normal "从技术上讲，它被设计成以另一种方式穿着，适合我这个体型的龙去取悦四足龙。但这对他们是微不足道的，所以我把它倒过来玩"
        show anna bangok lipbite with dissolve
        m "她拉着我的手，把玩具放得更深一点，直到她的小穴缠绕在玩具宽度缩小的地方。我的手指拂过她饱满的狭缝，同时稳稳地握住玩具。"

    if bangok_four_anna2.position == "dildo":
        m "当它进入她体内时，它看起来有点像我抓住了从她的狭缝中伸出的阴茎，除了它是一种灰色的柔性材料"
        An smirk "我想我可以再来一次。"
    else:
        m "当它进入她体内时，它看起来有点像我抓住了从她的狭缝中伸出的阴茎，除了它是一种灰色的柔性材料，并被将它固定到位的带子环绕。"

    play sound "fx/system3.wav"
    s "内容不足。加载存档或准备崩溃."
    $ renpy.error("TODO: ")


label bangok_four_anna2_apartment_male_nostrapon_startingmenu:
    menu:
        "[[用手指抚弄.]" if bangok_four_anna2.finger == True:
            $ bangok_four_anna2.finger = False
            m "我走近了，伸手抚摸她的开口."
            An sad "你的手干净吗?"
            menu:
                "足够干净.":
                    pass
                "我洗过它们了!":
                    pass
                "你要我去找手套吗?":
                    An face "不."
            An normal "小心你的爪子。我不希望你把我的内壁给划破了."
            c "除非你比人类更脆弱，否则我怀疑这将不是一个问题。"
            m "慢慢地，我把两根手指按进去，用剩下的手继续我的小而温柔的圆圈。安娜的双腿微微颤抖，它们悬在空中."
            $ renpy.pause (0.8)
            if anna2mood > -1:
                An smirk "你可以继续这样做."
            else:
                show anna sad with dissolve
            $ renpy.pause (0.5)
            m "在这种温柔的挑逗中又给了她一会儿之后，我又加了第三根手指，发现它比前两根更容易滑入，因为她的自然润滑开始滑过她的小穴."
            $ renpy.pause (0.8)
            if anna2mood < 1:
                An face "好了，停下。"
                c "哼？我以为你喜欢这个."
                An sad "我们是来做爱的。去他妈的快来操我."
                menu:
                    "[[添加第四根手指。]":
                        if anna2mood > -2:
                            $ anna2mood += 1
                            m "安娜浑身发抖，但我感觉到她紧紧地搂着我的手指，她没有阻止我。"
                            $ renpy.pause(0.8)
                            An smirk "好吧, 随便了, 但你最好能让我高潮。"
                            c "我尽量."
                        else:
                            $ anna2mood -= 2
                            $ bangok_four_anna2.lick = False
                            show anna disgust with dissolve
                            play sound "fx/impact3.ogg"
                            # play sound2 "fx/chair.wav"
                            $ renpy.pause(0.1)
                            hide anna with None
                            $ renpy.pause(0.0)
                            show o2 at Pan((0,150),(0,150),0.0)
                            show anna disgust at Position(xpos=0.8,ypos=1.0, xanchor='center')
                            with vpunch
                            m "安娜狠狠地把我从她身上踢了下来，用爪子在我的胸口留下了针刺一样的划痕。我跌跌撞撞地坐在沙发旁边的扶手椅上。"
                            An rage "我们交易的条款非常明确。性。不是他妈的指头，是性。"
                            An sad "我和你一起到这里。但我会遵守我们交易的条款。所以他妈的过来，把它贴在我身上。不管那是什么，都不要再说了。"
                            c "..."
                            $ renpy.pause(0.8)
                            show o2 at Pan((0,250),(0,250),0.0) with ease
                            m "我重新站了起来，更加警惕, 心里想着如果我惹她生气，她还会对我做什么。"
                            show anna disgust:
                                pos (0.8, 1.3)
                                rotate 15
                            with dissolve
                            m "安娜躺了下来，看起来如果我再激怒她，她会把我撕开。"
                            jump bangok_four_anna2_apartment_male_nostrapon_startingmenu
                    "如果你坚持。":
                        jump bangok_four_anna2_apartment_male_nostrapon_startingmenu
            else:
                An smirk "你是对的。你的爪子根本不是问题。"
                An bangok blush "而且你的皮肤比任何龙的鳞片都要柔软得多。"
                menu:
                    "[[添加第四根手指.]":
                        m "这根手指稍微抗拒了一点。但是在她的自然润滑下，它适合，其次是我的大部分手掌。"
                        $ anna2mood += 1
                        An bangok lipbite "现在你开始上道了."
                        c "Huh?"
                    "[[继续做别的事情。]":
                        show anna sad with dissolve
                        $ renpy.pause(0.3)
                        show anna normal with dissolve
                        m "当我退出时，安娜内部的褶皱拉扯着我的手指，但她没有对我的行为发表任何评论。"
                        jump bangok_four_anna2_apartment_male_nostrapon_startingmenu

            call bangok_four_anna2_apartment_yourarm from bangok_four_anna2_apartment_male_nostrapon_startingmenu_finger
            jump bangok_four_anna2_apartment_male_nostrapon_startingmenu

            label bangok_four_anna2_apartment_yourarm:
            An smirk "我想要你的胳膊。让我们看看剩下的软肉是什么感觉。"
            menu:
                "什么，就像，从我的身体中分离出来？":
                    c "我想留着我的手臂，谢谢."
                    An bangok blush "他妈的, 你可以留着你的手臂."
                    An smirk "但首先，我希望它尽可能深入我的身体内部."
                    c "O-Oh."
                "不可能。" if bangok_four_anna2.position not in ["dildo","strapon"]:
                    $ anna2mood -= 2
                    c "我只是在探索。我没想到你会......"
                    show anna sad with dissolve
                    $ renpy.pause(1.2)
                    An bangok blushpalm "认真地？"
                    An sad "好吧。把你的手拿出来操我，如果这就是你想要的."
                    return
                "我宁愿继续讨论绑带。" if bangok_four_anna2.position in ["dildo","strapon"]:
                    $ anna2mood -= 1
                    c "我只是在探索。我没想到你会......"
                    show anna sad with dissolve
                    $ renpy.pause(1.2)
                    An bangok blushpalm "认真地？"
                    An sad "好。把你的手伸出来，戴上那个绑带去，如果这就是你想要的。"
                    return
                "好.":
                    An smirk "真是听话的小人类."

            show anna bangok blush with dissolve
            m "我进进出出我到目前为止伸进去的四根手指，让她习惯这个大小，直到我的手湿透并埋到我的拇指根部。"
            $ renpy.pause(0.5)
            c "你确定？"
            An bangok blushpalm "如果我不想这样做，我会要求你这样做吗？"
            m "我抽回指尖，然后将拇指折叠在掌心，将整只手按在她体内。"
            An bangok lipbite "Ngh..."
            m "她的缝隙紧紧地搂着我的手腕，里面起伏着，因为它们在我的手上挤压着收缩着，渴求着我的手臂无法提供的物质。"
            c "你没事吧?"
            An bangok blush "你能不能别再问我了然后再深入些?"
            c "当我的手臂全伸进去时，我该怎么办？"
            An bangok blushpalm "到那时我会告诉你怎么办的."
            show anna bangok blush with dissolve
            m "听从她的吩咐，我把更多的胳膊伸进了她的体内。很快，到目前为止，我的手被她的液体润滑的部分已经结束了，她的小穴内的摩擦力急剧增加。"
            An bangok blushpalm "应该考虑润滑油."
            An bangok blush "无所谓。拔."
            show anna bangok lipbite with dissolve
            m "我照做了，取回了我手腕的一小部分和我进入的整个手。安娜一直咬着嘴唇，然后松了一口气。"
            hide anna with None
            $ renpy.pause(0.0)
            show anna bangok blush at Position(xpos=0.8,ypos=1.0, xanchor='center')
            m "然后她站了起来。"
            An normal "跪在这里，把你的胳膊肘撑在桌子上，这里."
            menu:
                "我以为我们要做爱了。":
                    An smirk "你是让我爽的人。现在首先是我，然后是你。"
                "这已经是你给我的很多命令了...":
                    $ anna2mood -= 1
                    An face "嘘嘘。要我帮你写下来吗？"
                    An normal "只需将肘部放在桌子上，然后将手伸上去."
                "是的，安娜.":
                    $ anna2mood += 1
                    show anna smirk with dissolve
                    $ renpy.pause (0.5)
                    An "你。我喜欢你."
            m "一旦我的手就位，安娜确保我的手指处于我插入她时使用的形状，并且我保持这种状态."
            show anna bangok blush flip at Position(xpos=0.7) with dissolve
            m "然后她转过身来，把她光滑的缝隙重新对准上去，她的一条腿正好落在我面前。"
            $ renpy.pause(0.3)
            show anna bangok lipbite flip at Position(xpos=0.7,ypos=1.02) with ease
            An "Nnh!"
            m "安娜通道中的肌肉地压在我的手上，在我的手腕上挤压和覆盖更多的天然润滑剂，让它沿着我的手臂流淌。"
            $ renpy.pause (0.4)
            An bangok blush flip "真是流的到处都是"
            m "我按照吩咐做了，试图将她的汁液更均匀地分布在我手臂的下一部分。安娜颤抖着，我另一只手的手指拂过她的缝隙。"
            An smirk flip "你还靠在桌子上的，对吧？"
            c "是啊."
            An bangok blush flip "好."
            show anna bangok lipbite flip at Position(xpos=0.7,ypos=1.0) with ease
            show anna bangok lipbite flip at Position(xpos=0.7,ypos=1.04) with ease
            m "安娜站起身来，她的小穴紧紧地挤压着, 几乎要把我的胳膊拉扯在一起。就在我的手指即将离开之前，她调转方向，向后压，像假阳具一样把自己操在我的手上."
            An "Ah!"
            if persistent.bangok_cervpen:
                m "我们几乎立刻就遇到了摩擦力，但这个摩擦力来自她的体内。"
                show anna smirk flip with dissolve
                m "她回头看了一眼。无论这对她来说是什么感觉，这应该都是一种很好的感觉。"
            else:
                show anna smirk flip with dissolve
                m "她故意握紧，让自己的身子停了下来, 紧紧地收缩挤压我的胳膊和手。"
                c "(我想知道我是否能让她的事情变得更有趣......)"
            menu:
                "[[握拳.]":
                    $ bangok_four_anna2.fisting = True
                    $ anna2mood += 1
                    $ renpy.pause (0.5)
                    An sad flip "你干了什么...?"
                    m "安娜在我的手臂上移动，感觉到我给她扩张了额外的空间，裹着我的拳头."
                    An bangok blush flip "Hm."
                    show anna bangok lipbite flip:
                        ease 1.0 ypos 1.02
                    with None
                    m "她抬起头来，内壁在她体内移动并围绕着我的拳头移动着."
                    m "接着她改变了方向，快速地把身体向下压。"
                    show anna bangok lipbite flip:
                        ease 0.4 ypos 1.06
                    with None
                    c "安娜，等等——"
                    show anna bangok orgasm flip with dissolve
                    An "他...他妈的！是的！"
                    m "我愣住了."
                    c "(嗯?)"
                    show anna bangok lipbite flip with dissolve
                    $ bangok_four_anna2.position = "fist"
                "[[张开手指.]":
                    $ renpy.pause (0.5)
                    $ anna2mood -= 3
                    An sad flip "你在干...?"
                    m "当她的内壁围绕在我手的周围移动时，我的手指戳进了她的内壁."
                    An disgust flip "啊! 嗷! [player_name], 看在他妈的份上!"
                    show anna at Position(xpos=0.8, ypos=1.0) with ease
                    show anna sad with dissolve
                    m "她走开了，把我的手拉开，瞪着我，我一边研究我的手指从她的体内伸展时所经历的刺耳。"
                    c "不好意思..."
                    An disgust "别他妈说 “对不起。” 不要他妈的捉弄我的生殖器！"
                    An sad "把你的手指放回原来的样子."
                    m "我做到了。在检查了我和我的手很久之后，安娜把尾巴转向我，然后又沉了下去。"
                    show anna sad flip with dissolve
                    show anna at Position(xpos=0.7, ypos=1.0) with ease
                    show anna at Position(xpos=0.7, ypos=1.02) with ease
                    show anna at Position(xpos=0.7, ypos=1.04) with ease
                    An sad flip "该死的。还是有点疼。"
                "[[没有任何想法。]":
                    pass
            show anna:
                ease 1.0 ypos 1.02
                ease 1.0 ypos 1.04
                ease 0.7 ypos 1.02
                ease 0.5 ypos 1.04
                block:
                    ease 0.40 ypos 1.02
                    ease 0.25 ypos 1.04
                    repeat
            with None
            play soundloop "fx/rub2.ogg" fadein 4.0
            m "安娜开始操我的手腕和手，起初是温柔的，然后越来越用力。"
            show anna bangok lipbite flip with dissolve
            if persistent.bangok_cervpen:
                m "每一次，她都更用力地用我的手抵挡她小穴内的摩擦力。"
            else:
                m "每一次，她都把我的手伸得更深一点，随着更多的汁液顺着我的手臂滴落，她挤得更紧了."
            An "快要..."
            menu:
                "安娜，别伤到你自己！":
                    $ anna2mood += 1
                    An "我比这努力得多。"
                "嘿，别伤到我的手！":
                    $ anna2mood -= 1
                    An bangok blushpalm flip "啊....你们人类...真的太脆弱了...."
                    show anna bangok lipbite flip with dissolve
                "[[什么都不说.]":
                    pass
            $ renpy.pause(0.5)
            stop soundloop fadeout 0.5
            play sound "fx/tableslap.wav"
            play sound2 "fx/snarl.ogg"
            $ bangok_four_anna2.annacame = True 
            show anna bangok orgasm flip:
                ease 0.3 ypos 1.07
            with None
            $ renpy.pause(0.8)
            if persistent.bangok_cervpen:
                m "突然，安娜用力往下压，终于冲破了阻力。她的尾巴拍打着桌子，我的胳膊又消失在她体内几英寸。我手上的压力减轻了，而手臂上起伏的压力越来越大，最终更宽的部分塞进了她狭窄的小穴。"
            else:
                m "突然，安娜把自己一路往下推。我喘着粗气，感觉到她的外唇紧紧地攥着，几乎一直到我的肘部。我胳膊上起伏的压力越来越大，痉挛着，更宽的部分现在塞进了她深而紧的内部。"
            $ renpy.pause(0.5)
            show anna bangok lipbite flip with dissolve
            m "安娜在那里安静呆了好一会儿，只是在咆哮和她所做的一切之后喘了口气."
            $ renpy.pause(0.8)
            menu:
                "你没事吧？":
                    $ renpy.pause (0.9)
                    $ anna2mood += 1
                    An smirk flip "说实话,爽爆了."
                "刚刚发生了什么？":
                    $ renpy.pause (0.6)
                    if persistent.bangok_cervpen:
                        An "我把你的手推过我的子宫颈."
                    else:
                        An "我挽着你的胳膊，就像我说的那样."
                "我的手现在在你子宫里吗？" if persistent.bangok_cervpen:
                    $ renpy.pause (0.5)
                    An smirk flip "是的。是的，它在里面."
            if bangok_four_playerhasdick == True:
                An "毕竟我以前的大多数合作伙伴都是......比你大。"
                An smirk flip "但是至于你的胳膊? 天哪那他们可比不上"
            An bangok blush flip "这对任何龙来说都是不安全的。由于鳞片和锋利的爪子，并且非没有保护措施可以做到这一点。"
            An smirk flip "现在? 嗯?"
            show anna bangok orgasm flip:
                ease 1.5 ypos 1.1
            with None
            $ renpy.pause(1.5)
            show anna bangok lipbite flip with dissolve
            if persistent.bangok_cervpen:
                m "安娜在我的胳膊上沉得更深，现在被她的汁液浸透了，直到她几乎坐在我的前臂上。她内心还有另一种摩擦力，我以为她不会试图克服这种阻力。"
            else:
                m "安娜在我的胳膊上沉得更深，现在被她的汁液浸透了，直到她几乎坐在我的前臂上。她内心深处有一种摩擦力，我以为她不会试图玩弄这种感觉。"
            $ renpy.pause(1.5)
            An smirk flip "好吧，我不会在这里做所有的活。"
            c "我也不能这样来移动我的手臂."
            An "我想也是。让我回到沙发上."
            show anna bangok lipbite flip:
                ease 1.5 ypos 1.04
            with None
            $ renpy.pause(1.5)
            show anna bangok orgasm flip:
                ease 0.25 ypos 1.07
            with None
            $ renpy.pause(0.8)
            show anna bangok blush flip with dissolve
            if persistent.bangok_cervpen:
                m "安娜开始振作起来，双腿颤抖。当我感觉到她的子宫颈靠近我的手时，她摇摇晃晃，她的体重落回那扇紧绷的宫颈口上，把我挤压了回去，尽管不是很顺利。"
            else:
                m "安娜开始振作起来，双腿颤抖。她踉踉跄跄地爬了起来，她的体重在压紧我的胳膊时落回了我的手臂上，并发出了一声轻微的喘息。"
            menu:
                "[[拔出来.]":
                    show anna bangok lipbite flip with dissolve
                    $ renpy.pause(2.0)
                    play sound "fx/uncork.ogg"
                    show anna bangok blushpalm flip at Position(ypos=1.08) with ease
                    $ anna2mood += 1
                    An "谢了."
                "[[让她来处理吧.]":
                    show anna bangok lipbite flip:
                        ease 1.5 ypos 1.04
                    with None
                    $ renpy.pause(1.5)
                    show anna bangok lipbite flip:
                        ease 1.5 ypos 1.00
                    with None
                    $ renpy.pause(1.5)
                    play sound "fx/uncork.ogg"
            show anna at Position(xpos=0.75, ypos=1.0) with ease
            show anna at Position(xpos=0.8, ypos=1.0) with ease
            show anna bangok blush with dissolve
            $ renpy.pause(0.3)
            show anna bangok blush:
                pos (0.8, 1.3)
                rotate 15
            with dissolve
            m "摇摇晃晃地走到沙发上，安娜又倒在了沙发上。她的缝隙仍然微微张开，在她的兴奋中闪闪发光。"
            An smirk "把你的胳膊伸回去."
            show anna bangok lipbite with dissolve
            if persistent.bangok_cervpen:
                if bangok_four_anna2.position == "fist":
                    m "我答应了，握紧拳头（小心翼翼地把指甲伸进去）又捏回了她身上。一旦穿过她的外阴，它就开始挤压起来，四处摩擦，直到我伸到她的宫颈."
                else:
                    m "我答应了，把手伸进她的外阴，然后穿过她的阴道，滑到她的宫颈。"
            else:
                if bangok_four_anna2.position == "fist":
                    m "我答应了，握紧拳头（小心翼翼地把指甲伸进去）又捏回了她身上。一旦穿过她的小穴，宫颈就收缩起来，向各个方向摩擦，直到她完全收紧以阻止我的前进。"
                else:
                    m "我答应了，把手伸进她的外开口，然后滑得更深，直到她紧缩住我的拳头来阻止我的深入。"

            An smirk "直接塞进去."
            menu:
                "你确定这是安全的吗？":
                    $ anna2mood -= 1
                    jump bangok_four_anna2_finger_punch
                "只是打一拳？":
                    label bangok_four_anna2_finger_punch:
                    $ anna2mood += 1
                    An bangok blush "你觉得我刚刚是怎么做到的?"
                    An smirk "我和我的恋人做过几次。他们没有你想象的那么温柔。"
                    m "我往后退了一点，然后推了推."
                    show anna bangok lipbite with dissolve
                    $ renpy.pause(0.3)
                    An "再用点力"
                    $ renpy.pause(0.8)
                    if persistent.bangok_cervpen:
                        m "我又试了一次，更加努力。即使她把所有的天然润滑剂都涂在我的胳膊上，在她狭窄的通道中，所有的摩擦力都很难快速移动。尽管如此，当我压在她的子宫颈上时，我还是感觉到了一点不同的东西，还有一些小的阻力。"
                    else:
                        m "我又试了一次，更加努力。即使她把所有的天然润滑剂都涂在我的胳膊上，在她狭窄的通道中，所有的摩擦力都很难快速移动。尽管如此，当我排得恰到好处时，还是有办法滑得更深。"
                    An smirk "怎么了？弱小的人类大使还不够强大？"
                    c "(就是这样!)"
                    if persistent.bangok_cervpen:
                        m "我往前挪了挪，把被龙缠住的手往后拉，然后又推了推，把力传到肩膀之间，我把我的胳膊拉到她的胯部。有了新的角度，我在她的子宫颈上施加了更大的力."
                        show anna bangok orgasm with dissolve
                        m "它像她最外层的开口一样在我的手上蔓延开来。"
                    else:
                        m "我往前挪了挪，把被龙缠住的手往后拉，然后又推了推，把力传到肩膀之间，把我的胳膊拉到她的胯部。有了新的角度，我把她带到了我的肘部。"
                        show anna bangok orgasm with dissolve
                "我会先尝试推动......":
                    m "我把上半身的重量更多地靠在我的手臂上，按在上面。"
                    An bangok blush "认真地, [player_name]. 重复用力比--"
                    if not persistent.bangok_cervpen:
                        m "找到合适的角度，我一路滑了进去，尽管她紧紧地挤压着。"
                    show anna bangok orgasm with dissolve
                    $ renpy.pause (0.4)
                    show anna bangok blushpalm with dissolve
                    An "别管了."

            An bangok lipbite "干的好。现在操我."
            if persistent.bangok_cervpen:
                m "我开始移动，几乎把我的胳膊推到肘部，然后向后拉，直到她的子宫颈快要放开我，我把我的指关节弹出来。"
            else:
                m "我开始移动，向后拉，然后把我的手臂几乎推到肘部，然后向后拉，直到她的外唇快要放开我了。"
            m "安娜欣喜若狂地扭动着身子."
            $ renpy.pause(0.5)
            An "不要...不要停!"
            m "我正要问我为什么要这样做，因为她的通道被狠狠地夹住了，摩擦力翻了两番。我甚至几乎无法移动。这并不重要，因为她的一条腿过了一会儿就把我拉到了她的肚子上。"
            show anna bangok orgasm with dissolve
            show black with fadequick
            play sound "fx/snarl.ogg"
            $ bangok_four_anna2.annacame = True 
            m "安娜又发出一声闷闷的咆哮，她把自己的手塞进嘴里，尽量不让自己叫的太大声."
            $ renpy.pause (0.8)
            hide black
            show anna bangok lipbite 
            with dissolvemed
            m "过了好一会儿，安娜的阴道松开了，她把手臂放到身体两侧，松开了我。"
            $ renpy.pause (0.5)
            An smirk "天哪。 那。。。那太他妈爽了.{w=0.8} 一晚两次."
            menu:
                "你很容易高潮?":
                    $ renpy.pause (0.5)
                    if persistent.bangok_cervpen:
                        An smirk "你第一次穿过我的子宫颈."
                    else:
                        An smirk "我第一次把你的前臂砍下来."
                "现在轮到我了？":
                    $ renpy.pause (0.6)
                    An smirk "是的。该你了。"
                "嘿！那我呢？":
                    $ anna2mood -= 1
                    An bangok blush "是的。该你了。"
            m "我从她现在松开的通道上抽出湿漉漉的胳膊，考虑我的下一步行动。"
            return



        "[[舔她.]" if bangok_four_anna2.lick == True:
            $ anna2mood -= 1
            $ bangok_four_anna2.lick = False
            m "我跪在安娜旁边，把脸凑得更近。"
            An disgust "嘿!"
            m "当她双腿交叉在她的时，我不得不向后躲避，当她挡住我的去路时，差点割伤我的脸。"
            An face "我同意做爱，而不是任何形式的性行为。"
            An sad "在我知道你的嘴里有什么之前我是不会让你这么碰我的."
            if anna2mood < 1:
                c "你会以此为借口做我试图做的任何事情吗?"
                An face "你认为避孕套是做什么用的？"
            m "我重新站了起来."
            jump bangok_four_anna2_apartment_male_nostrapon_startingmenu



        "[[用她的嘴。]":
            $ bangok_four_anna2.doneoral = True
            c "实际上。。。"
            m "我坐在沙发上，张开双腿。"
            c "你为什么不用你的嘴对我？"
            if bangok_four_anna2.annacame == True:
                show anna smirk with dissolve
                An "我想这倒是公平的，在你用让我爽过之后."
                hide anna with None
                $ renpy.pause(0.0)
                show anna bangok blush at Position(xpos=0.8,ypos=1.0, xanchor='center')
            else:
                show anna sad with dissolve
                $ renpy.pause(0.9)
                if anna2mood < 4:
                    show anna face with dissolve
                An "呃, 好吧."
                hide anna with None
                $ renpy.pause(0.0)
                show anna sad at Position(xpos=0.8,ypos=1.0, xanchor='center')
            show anna normal at Position(xpos=0.7) with ease
            show anna normal at Position(xpos=0.6, ypos=1.1) with ease
            show anna normal at Position(ypos=1.3) with ease
            m "安娜从沙发上站起来，然后跪在我面前."
            $ renpy.pause(0.3)
            show anna normal with dissolve
            m "她用一只手抚摸着我的下体，把避孕套的环一直压到底部。她手上粗糙的鳞片和冰冷的爪子是一种令人兴奋和新鲜的感觉，让我的下体处于抽搐状态。"
            $ renpy.pause (0.8)
            show anna bangok orgasm at Position(ypos=1.5) with ease
            m "然后她张开嘴巴落在我的胯部，短暂的牙齿闪光让我内心深处有一种危险的快感。"
            menu:
                "小心牙齿！":
                    $ anna2mood -= 1
                    show anna face with dissolve
                    show anna at Position(ypos=1.4) with ease
                    m "在她真正开始做任何事情之前，安娜用爪子捂住了她的脸后退了。"
                    An "你有足够的机会看到我的嘴巴是什么样子的。你以为我要做什么？咬你一口？然后让脸上满是鲜血?"
                    An sad "你到底要不要这个口交？"
                    $ renpy.pause(0.8)
                    c "我的意思是，我当然——"
                    An normal "那就闭上你的嘴, 我知道我在干什么."
                    show anna bangok orgasm at Position(ypos=1.5) with ease
                    m "她没有再给我抗议的机会，接着把头埋了回去。"
                "O-hoohh...":
                    pass
            m "安娜的舌头在我的上滑来滑去，拉扯着它，向她的嘴巴后面撸动着。"
            m "她闭上了嘴唇，牙齿在我的阴茎上摩擦，鳞片状的嘴唇向下滑动。"
            m "她粗糙的舌头整个地贴合在我的下面，舌头像吸吮一样扭动和拉扯，但没有任何真空密封."
            $ renpy.pause(0.6)
            m "我把头向后仰，暂时迷失在全新的感觉中。"
            $ renpy.pause(0.6)
            show anna bangok blush at Position(ypos=1.49) with ease
            m "她的舌尖从我的根部抽回，当她向我的阴茎拉回时，缠绕收紧。她的嘴唇也跟着动了起来，有那么一会儿，我担心她会抽离。"
            m "然后我感觉到她的舌头在我的尖端下方收紧，在避孕套周围形成一个挤压环。"
            show anna bangok blush at Position(ypos=1.52) with ease
            m "她把头往后推，嘴唇和牙齿在我的阴茎上摩擦，然后舌环在底下不断地挤压。"
            m "我差点就在那里失控了。但安娜在我的根部展开了她的舌头，在她安排舌头进行第二次时，分开的嘴唇向后拉。"
            show anna bangok blush at Position(ypos=1.5) with ease
            menu:
                "[[抓住她的角。]" if bangok_four_hornincident == False:
                    if anna2mood < 1:
                        m "这种只推动的速度对我不起作用。幸运的是，大自然给了我一对完美的把手，可以向安娜解释我想要的东西."
                    else:
                        m "安娜对我的身体所做的一切令人难以置信，但我想要一个更积极的角色。"
                    m "我用双手握住安娜的角，她的舌头又变成了一个环，更快地把她拉回了我的腹股沟。"
                    $ anna2mood -= 1
                    $ bangok_four_anna2.hornsgrabbed = True
                    show anna disgust at Position(ypos=1.52) with ease
                    m "在这次下降中，她的牙齿收紧了不少，以至于我几乎无法专注于她的舌头，因为危险的快感又回来了，担心我把我的血粘在什么危险的地方。"
                "我可以用你的角来......？":
                    $ anna2mood += 1
                    $ bangok_four_anna2.hornsgrabbed = False
                    m "安娜点了点头，让我的阴茎在她啜饮我的尖端时晃动。"
                    m "我给了她一点时间来调整她紧绷的舌环，然后用两只角把她的头拉到我的小腹上。"
                    show anna bangok orgasm at Position(ypos=1.52) with ease
                "[[呻吟.]":
                    pass
            m "当她下来时，我稍微了看了看她的脸。感觉就像他妈的某种异国情调的、有牙齿的小穴，这种感觉与我以前有过的任何感觉都不一样。"
            $ renpy.pause (0.5)
            m "安娜用她的前臂支撑着我的大腿，让我靠在沙发上。"
            $ renpy.pause(0.3)
            if bangok_four_anna2.hornsgrabbed is not None:
                m "我把安娜靠在我的胯部一会儿，享受着她用舌头在我的上舔舐。然后我把她拉回来，感觉到她的舌头在我的尖端上展开。"
                show anna sad at Position(ypos=1.50) with ease
                m "我扯了扯她的龙角，示意我会加快步伐。在给她一点时间准备舌头后，我把她拖了回去。"
                play soundloop "fx/rub2.ogg" fadein 0.5
                show anna:
                    ease 0.25 ypos 1.51
                    ease 0.4 ypos 1.50
                    repeat
                with None
            else:
                show anna bangok lipbite at Position(ypos=1.50) with ease
                m "安娜又缩了回去，这次用舌头夹住了避孕套底下的环，隔着避孕套给我挤奶."
                play soundloop "fx/rub2.ogg" fadein 0.5
                show anna:
                    ease 0.25 ypos 1.51
                    ease 0.4 ypos 1.50
                    repeat
                with None
                m "她现在对她对我的阴茎的控制充满信心，她开始加快步伐，把自己对准我的鸡巴。"
            $ renpy.pause(2.0)
            menu:
                "我、我快要......":
                    pass
                "[[射精.]":
                    pass
            if bangok_four_anna2.hornsgrabbed is not None:
                show anna bangok blush at Position(ypos=1.53) with ease
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                show black with fadequick
                m "我把安娜深深地拉进我的胯部，把我的阴茎夹在她鳞片状的嘴唇之间."
                m "她的舌头不停地移动，搜索和拉扯我们之间的橡胶屏障."
                $ renpy.pause(0.5)
                hide black with dissolveslow
                $ renpy.pause(0.5)
                m "我松开了安娜的角，让她自由地让我的鸡巴从她的嘴唇上掉下来"
                show anna normal at Position(ypos=1.4) with ease
                m "安娜一边往后移，一边用舌头弹了弹避孕套前面鼓起来的小泡泡."
            else:
                show anna bangok blush at Position(ypos=1.4) with ease
                m "安娜立刻拉开了，用一只手把我推向了高潮。"
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                show black with fadequick
                $ renpy.pause(0.5)
                hide black with dissolveslow
                $ renpy.pause(0.5)
                m "她不停地撸动，直到我的阴茎开始软化，我的精液储备消耗殆尽。然后她用拇指弹了弹避孕套前面鼓起来的小泡泡。"

            call bangok_four_anna2_apartment_harvest from bangok_four_anna2_apartment_bjdone

            if bangok_four_anna2.hornsgrabbed is None:
                show anna at center with ease
            else:
                if bangok_four_anna2.hornsgrabbed == True:
                    show anna normal at center with ease
                    An normal "我应该注意，你很幸运，我能像我一样四处走动。像这样抓住我的角可能会导致一个经验不足的龙的感到不适。"
                    label bangok_four_anna2_apartment_hornincident_description:
                    c "你是什么意思?"
                    An sad "这是一个敏感领域。有一种生物驱动力可以防止它们从我们的头上被扯下来，所以用它们来控制我们头部的运动是......不可取的。"
                    An bangok blush "除非我们看到它的到来。但这并不适合所有人."
                    c "明白了."
                else:
                    show anna bangok blush at center with ease
                    An "谢谢你{i}先询问{/i}再抓住了我的角。之前有一个混蛋毫无征兆地抓住了他们，然后......"
                    if bangok_four_hornincident == True:
                        c "答案是肯定的。没关系."
                    else:
                        jump bangok_four_anna2_apartment_hornincident_description
                $ bangok_four_hornincident = True

            jump bangok_four_anna2_apartment_done



        "[[用她的屁股.]":
            $ bangok_four_anna2.position = "ass"
            if persistent.bangok_cloacas == True:
                if bangok_four_anna2.annacame == True:
                    m "安娜的缝隙在我操完胳膊后仍然微微分开，就像我的胳膊仍然随着她的兴奋而闪闪发光。我用我操她的那只胳膊给我的鸡巴一个泵，润滑避孕套，然后进入她的双腿之间。"
                    c "在，我用胳膊操完你之后，你说你通常会用更大的家伙."
                    c "那我可以试试你的屁股吗？因为我认为它会更小......"
                    An smirk "呃, 行吧."
                else:
                    if anna2mood > 0:
                        show anna bangok blush with dissolve
                        m "她的缝隙是一条细细的、闪闪发光的线。我钻进她的两腿之间，把我包裹着避孕套的鸡巴直接对准它。"
                        c "我猜你的屁股在你的缝隙里更靠后，在这里？因为你是爬行动物，而且......"
                        An "对的。没错，你可以操那里."
                    else:
                        show anna sad with dissolve
                        m "她的缝隙是一条细线。我钻进她的两腿之间，把我用避孕套包裹的鸡巴对准它的底部，我以为她的屁股会在那里。"
            else:
                if bangok_four_anna2.annacame == True:
                    m "安娜的缝隙在我操完胳膊后仍然微微分开，就像我的胳膊仍然随着她的兴奋而闪闪发光。我用我操她的那只胳膊给我的鸡巴一个泵，润滑避孕套，准备进入她两腿之间稍靠后的小洞。"
                    c "在，我用胳膊操完你之后，你说你通常会用更大的家伙."
                    c "那我可以试试你的屁股吗？因为我认为它会更小......"
                    An smirk "呃, 行吧."
                else:
                    if anna2mood > 0:
                        show anna bangok blush with dissolve
                        m "她的褶皱由几个小鳞片环表示，在她细而闪亮的狭缝线下方一两英寸处。我钻进她的两腿之间，把我包裹着避孕套的鸡巴直接对准它。"
                        m "我只是先用我的尖端敲了敲它，抬头疑惑地看着她。"
                        An "哦，你......"
                        An smirk "呃, 行吧."
                    else:
                        show anna sad with dissolve
                        m "她的褶皱由几个小鳞片表示，在她狭缝的细线下方一两英寸处，我钻到她的两腿之间，将我包裹着避孕套的鸡巴直接对准它。"

            if anna2mood < 1:
                $ anna2mood -= 1
                show anna disgust with dissolve
                m "在我塞进去的那一刻，她狠狠地握紧了拳头，愤怒在她的脸上闪过。"
                An "看在他妈的份上。你不能先{i}问问我{/i}吗?"
                if bangok_four_anna2.lick == True:
                    c "哦，你是不是要告诉我我也不能这样做?"
                    An sad "通常性行为是在阴茎和阴道之间，以防你不记得生物学 101。讨论后，其他漏洞也参与其中。"
                    c "我们现在正在讨论它。不是吗？"
                else:
                    c "我们现在正在讨论它。不是吗？"
                $ renpy.pause (0.8)
                An sad "哦, 去他妈的, 继续吧."
                m "即使在她承认了这一点之后，她还是花了一点时间放松下来，让我的鸡巴再次移动，缓慢地滑入她温暖、包裹的直肠。"
            else:
                show anna bangok blush with dissolve
                m "当我进入时，她的屁股紧紧地拉扯着我的，但以一种缓慢的方式，而不是痉挛或疼痛。"
                m "她的动作使我放慢了进入的速度，带着需要的疼痛刺痛滑入她温暖、包裹的直肠。"

            $ renpy.pause (0.8)

            m "我停了下来，握住了阴茎，享受着她的屁股紧紧地挤压着我的根部。"

            $ renpy.pause (0.8)
            if anna2mood < 1:
                An sad "你还没有射精，是吗?"
            else:
                c "你需要时间来调整吗?"
                An smirk "丝毫不。我以前玩过后穴, [player_name]. 甚至是比你大的家伙."
                if anna2mood < 2:
                    An normal "现在做你的事."
                else:
                    An bangok blush "现在，开始动。"
            jump bangok_four_anna2_apartment_vaganal_merge



        "[[使用她的小穴.]":
            $ bangok_four_anna2.position = "vag"
            if bangok_four_anna2.annacame == True:
                m "安娜的缝隙在我操完胳膊后仍然微微分开，就像我的胳膊仍然随着她的兴奋而闪闪发光。我用我操她的那只胳膊给我的鸡巴一个泵，润滑避孕套，然后进入她的双腿之间。"
                m "当我溜进去时，我意识到我的热情已经把她分散到令人失望的几乎没有抵抗的地步。"
            else:
                if anna2mood > 2:
                    show anna bangok blush with dissolve
                    m "她的缝隙是一条闪闪发光的细线。我钻进她的两腿之间，把我包裹着避孕套的鸡巴直接对准它."
                    m "令人失望的是，进入她几乎没有阻力，她的狭缝显然意味着要带走更大的伙伴."
                else:
                    show anna sad with dissolve
                    m "她的缝隙是一条细线。我钻进她的两腿之间，把我包裹着避孕套的鸡巴直接对准它."
                    m "她绷紧了神经，在我一路逼入时与我的进入作斗争了一会儿。然而，一旦进入，压力就消失了，她的通道显然是为更大的伴侣准备的。"
            m "我停顿了一下，感觉到她的通道在我周围移动，肌肉按摩着我的，即使没有紧紧地挤压，也像一种全方位的温暖爱抚."
            $ renpy.pause(0.8)
            c "你能感觉到我在里面吗?"
            if anna2mood < 0:
                An disgust "这他妈是什么问题，“我能感觉到吗？” 它已经在我的身体里了，难道不是吗？"
                An face "只管操和射就完事了."
                c "呃, 好."
            elif anna2mood < 3:
                $ bangok_four_anna2.annacomment = "small"
                An sad "是的。但你还挺小的。"
                c "啊。好吧，我会尽我所能。"
            else:
                $ bangok_four_anna2.annacomment = "adorable"
                An smirk "你很可爱。但你根本不可能只用那件事就让我满足."
                c "这是一个挑战吗?"
                An bangok blush "只是陈述一个事实."

            label bangok_four_anna2_apartment_vaganal_merge:
            play soundloop "fx/rub2.ogg" fadein 2.0
            
            if anna2mood < 0:
                show anna sad with dissolve
            else:
                show anna bangok blush with dissolve
            $ renpy.pause(1.2)
            m "把她的话当作一种挑战，我开始抽动我的臀部，在滑回家之前，在我的尖端之外拉出。"
            $ renpy.pause(0.8)
            if annamood >= 0:
                show anna smirk with dissolve
            m "当我们做爱时，我感觉到安娜的尾巴蜷缩在我的两腿之间，抚摸着我的后背，鼓励我的步伐。"
            m "然后她的尾巴尖刺进了我的裂缝，在我的脸颊之间。"
            menu:
                "O-Oh!":
                    $ renpy.pause(0.5)
                    $ bangok_four_anna2.tail = True
                "呃。请不要。":
                    $ renpy.pause(0.5)
                    show anna bangok blush with dissolve
                "[[把尾巴拍开.]":
                    $ renpy.pause(0.5)
                    $ anna2mood -= 1
                    show anna sad with dissolve
                    c "那到底是什么？"
                    An "那么，我认为你不感兴趣。"
                    c "不。不，我不是."

            if bangok_four_anna2.tail == True:
                $ anna2mood += 1
                show anna bangok blush with dissolve
                m "她的尾巴骑在我的屁股上，进进出出，然后在我进入她的时候突然固定住."
                c "Ah!"
                m "我的呼吸急促起来，从她身上抽出，把尾巴插进我的屁股里，反之亦然。"
                $ renpy.pause(0.8)
                c "你——你去哪儿了——你是怎么发现你的尾巴的......?"
                An smirk "实践."
            else:
                m "她的尾巴从我的背上后退，沿着我一条大腿的曲线，沿着我的腿，在我填满它主人的洞时，她一直骑在上面。"

            $ renpy.pause(2.0)

            m "当各种感觉将我推向巅峰时，安娜将她的脚踝交叉在我的背后，在她把我拉近时减少了我的深度."

            if bangok_four_anna2.tail == True:
                m "然后她的尾巴探索得更深了一点。"
                c "W--"
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                show black with fadequick
                m "突然她找到我体内的那个敏感点，接着她开始猛攻，把我推到她体内高潮的边缘。"
                $ renpy.pause(0.5)
                hide black with dissolvemed
                $ renpy.pause(0.5)
                m "她把尾巴从我的屁股上抽出来，松开双腿，让我自由地用颤抖的腿站起来。"
            else:
                show anna bangok blush with dissolve
                m "我离她光滑的鳞片更近了一些，随着她温暖的增加，呼吸变得又热又重，脸红得通红。"
                m "然后她把双腿紧紧地靠在我的背上，把我拉了进去，我再也忍不住高潮了。"
                stop soundloop fadeout 0.5
                play sound "fx/extinguish.ogg"
                show black with fadequick
                $ renpy.pause(1.0)
                hide black with dissolvemed
                $ renpy.pause(0.5)
                m "一旦我从上面下来，她就松开了双腿，让我可以自由地站起来，双腿略微不稳。"

            hide anna with None
            $ renpy.pause(0.0)
            show anna bangok blush at Position(xpos=0.8,ypos=1.2, xanchor='center')
            m "然后她从沙发上站起来，用一只爪子的平顶戳了戳避孕套里装满液体的膨大部分。"
            call bangok_four_anna2_apartment_harvest from bangok_four_anna2_apartment_vaganaldone
            jump bangok_four_anna2_apartment_done



        "等等，它是垂直的?" if bangok_four_anna2.waitvert == True and bangok_four_malepartners > 0:
            $ bangok_four_anna2.waitvert = False
            An sad "不然呢."
            An face "哦。在我之前，你一定和一个雄性龙在一起过."
            An normal "这是我们为数不多的性别二态性之一，除了声音、一些眼睛结构和生殖设备的明显差异。"
            if anna2mood < 2:
                An sad "现在我们继续这个?"
            else:
                An smirk "现在，你能继续吗？"
            jump bangok_four_anna2_apartment_male_nostrapon_startingmenu





label bangok_four_anna2_apartment_harvest:
    if blood == False:
        An "好吧. 看起来我有这个玩意之后, 我就不需要你的血液样本了"
        m "她捏了捏我的鸡巴尖和套套的根部，然后开始把它扯下来。"
        menu:
            "我还没同意呢！":
                $ anna2mood -= 1
                An sad "不。你已经同意在几天后进行更详细的检查了。这基本上没什么。"
                menu:
                    "把她的手拿开.":
                        $ anna2mood -= 2
                        m "我抓住她的手腕，把她的手从我的鸡巴上拽下来。"
                        c "这是我的DNA。这对我来说可不是“什么都没有”!"
                        An face "你他妈在逗我?"
                        An sad "这就是他妈几公里长的基本分子串在一起，一遍又一遍地复制。从程序上来看，保护它根本没有任何意义。我他妈能从你今晚在我手臂上脱落的皮肤细胞中得到这些玩意"
                        c "你这样做只是为了获得能够克隆我的信息？"
                        An disgust "我他妈的为什么要这样做?"
                        An face "不。这一切都是为了弄清楚你的身体是如何工作的。事实上我不需要这样做，但是当我把你带到我的实验室时，这些玩意让我更容易知道会发生什么以及要怎么做。"
                        menu:
                            "承认这一点。":
                                $ renpy.pause(0.5)
                                $ anna2mood += 2
                                c "好。听着，对不起。在人类中，将自己的样本送人并不正常."
                                An sad "这不是我对性自由主义观点的期望."
                                c "如果你只是想换一种方式，我想强迫你做所有这些工作是没有意义的。去吧，拿走它。"
                                show anna normal with dissolve
                                $ renpy.pause(0.8)
                                An "谢谢。"
                            "拒绝.":
                                $ anna2mood -= 1
                                stop music fadeout 2.0
                                c "我不在乎。你不能像有病那样那样保留我的精液样本."
                                An disgust "呃, 随你的便."
                                An sad "事实上在那种情况下，我已经完全完成了我的目的。当我在实验室有空位的时候我会给你打电话的"
                                label bangok_four_anna2_apartment_abruptdeparture:
                                stop music fadeout 0.5
                                if anna2mood > -2:
                                    c "安娜..."
                                hide anna with dissolvemed
                                $ renpy.pause(0.3)
                                play sound "fx/door/doorclose.ogg"
                                $ renpy.pause(1.0)
                                m "安娜二话不说，就离开了."
                                $ renpy.pause(1.0)
                                scene black with dissolvemed
                                $ renpy.pause(0.5)
                                $ annastatus = "bad"
                                $ annascenesfinished = 2
                                jump _mod_fixjmp
                    "刺破避孕套。":
                        $ anna2mood -= 1
                        m "我抓住她的手腕，强迫她的双手合拢，用爪子穿过避孕套的墙壁，刺穿她想要的样本。"
                        An disgust "搞什么？！"
                        c "这是我的DNA。这对我来说不是“什么都不是”！"
                        An "所以你要把它洒在我的手上？"
                        An sad "你知道这和把它交给我完全一样，不是吗？我需要几个细胞，而不是整个样品。"
                        An sad "这只是几公里长的基本分子串在一起，一遍又一遍地复制。事实上你去保护它根本没有任何意义。"
                        c "你这样做只是为了获得克隆我的信息？"
                        An disgust "我他妈的为什么要这样做？"
                        An sad "不。这一切都是为了弄清楚你的身体是如何工作的。事实上我不需要这样做，但是当我把你带到我的实验室时，这些玩意让我更容易知道会发生什么以及要怎么做。"
                        menu:
                            "道歉.":
                                $ renpy.pause(0.5)
                                $ anna2mood += 1
                                c "好。听着，对不起。在人类中，将自己的样本送人并不正常。"
                                An sad "这不是我对性自由主义观点的期望."
                                c "如果你只是想换一种方式，我想强迫你做所有这些工作是没有意义的。去吧，拿走它。"
                                show anna normal with dissolve
                                $ renpy.pause(0.8)
                                An "谢了。"
                                m "她扯下避孕套的残骸，一只手捏着它。"
                            "威胁.":
                                $ anna2mood -= 2
                                stop music fadeout 2.0
                                c "你要是拿走了那个样本，我就不会进你的实验室了。"
                                An disgust "呃, 好吧."
                                m "她在我裸露的腿上擦了擦。"
                                An "那里。现在开心了吗？还是要我洗手向你证明自己？"
                                $ renpy.pause(1.5)
                                An sad "事实上我完全实现了我的目标。当我在实验室有空位的时候我会给你打电话的"
                                stop music fadeout 0.5
                                if anna2mood > -2:
                                    c "安娜..."
                                hide anna with dissolvemed
                                $ renpy.pause(0.3)
                                play sound "fx/door/doorclose.ogg"
                                $ renpy.pause(1.0)
                                m "没有另一个词，安娜离开了。"
                                $ renpy.pause(1.0)
                                scene black with dissolvemed
                                $ renpy.pause(0.5)
                                $ annastatus = "bad"
                                $ annascenesfinished = 2
                                jump _mod_fixjmp
                    "尿在避孕套里。" if persistent.bangok_watersports:
                        $ anna2mood -= 2
                        play soundloop "fx/faucet1.ogg" fadein 1.0
                        queue soundloop "fx/faucet2.ogg"
                        $ renpy.pause(0.5)
                        show anna disgust with dissolve
                        An disgust "你他妈的...?"
                        m "她把装满的避孕套放在沙发上。"
                        An rage "你 {i} 知道 {/i} ph值这么低 会破坏样品!{i} 你怎么敢 {/i} !"
                        c "{i} 我 {/i} 怎么敢？你想拿走我的DNA。对我来说这不是 “什么都没有”!"
                        stop soundloop fadeout 0.5
                        An rage "这是几公里的基本分子链在一起，一遍又一遍地复制。根本就没有保护它的意义!"
                        c "现在已经这样了。你打算怎么办？"
                        $ renpy.pause(0.8)
                        show anna sad with dissolve
                        $ renpy.pause(0.5)
                        An sad "事实上我完全实现了我的目标。当我在实验室有空位的时候我会给你打电话的"
                        stop music fadeout 0.5
                        hide anna with dissolvemed
                        $ renpy.pause(0.3)
                        play sound "fx/door/doorclose.ogg"
                        $ renpy.pause(1.0)
                        m "没有别的话，安娜离开了."
                        $ renpy.pause(1.0)
                        scene black with dissolvemed
                        $ renpy.pause(0.5)
                        $ annastatus = "bad"
                        $ annascenesfinished = 2
                        jump _mod_fixjmp
                    "随她去.":
                        pass
            "[[随她去.]":
                pass
        m "把避孕套完全免费，她把它绑起来，用手掌。"
    else:
        c "你也要取样吗？"
        An normal "没什么意义.在你给我你的血液样本后，从性配子中测序你的完整DNA将是一堆额外的工作，没有任何好处。至少如果你的染色体像我们一样."
        c "我看得出来."
        m "她捏住我的鸡巴尖和避孕套，然后把我的避孕套从我的阴茎上拽下来，把它绑起来放在一边。"
    return





label bangok_four_anna2_apartment_done:
    show anna at center with ease
    if bangok_four_anna2.annacame == False:
        An sad "那就这样吧.你满意吗?"
        if anna2mood > 2:
            c "是吗？我还没有为你做任何事."
            An "我想没有，但是在实验室里我真的需要处理一些事情。"
        else:
            c "应该有更多."
            An normal "很高兴听到这个消息。那样的话，我应该回实验室了。我还有几件事要完成。"
    else:
        An smirk "我想就是这样。你满意吗？"
        c "是的。你呢。"
        An "是啊."
        $ renpy.pause(0.8)
        An bangok blush "我该回实验室了.我还有几件事要完成。"
    c "在晚上的这个时候？"
    $ renpy.pause(0.8)
    An normal "如果你这么担心我，那你带我去那里。"
    $ renpy.pause(0.8)
    c "给我一点时间把衣服穿上。"
    An sad "那是个玩笑.你是认真的吗？"
    c "没问题。为什么不呢？这不就是很好的骑士精神。"
    $ renpy.pause(0.8)
    if persistent.bangok_watersports == True:
        An face "好吧。当你这么做的时候，我会借你的由政府资助的洗手间。"
        menu:
            "我可能不需要为此穿上衣服...":
                $ renpy.pause (0.5)
                An sad "你到底是什么...？"
                An bangok blush "哦."
                An smirk "如果你这么说."
                scene black with dissolvemed
                $ renpy.pause (0.5)
                play sound "fx/door/doorclose3.wav"
                $ renpy.pause (1.5)
            "好的.":
                hide anna with dissolve
                $ renpy.pause (0.5)
                play sound "fx/door/doorclose3.wav"
    else:
        An face "好."
    $ renpy.pause(0.5)
    $ renpy.end_replay()
    scene facin3 at Pan ((128, 250), (128, 250), 0.0)
    show anna normal
    with Fade(0.5,1.0,0.5)
    jump anna2skip

label bangok_four_anna2_lab_good_hookupover:
    An smirk "说到这里，既然我们的事情已经正式结束，我们应该谈谈你的部分."
    jump bangok_four_anna2_lab_good_hookupover_end

label bangok_four_anna2_lab_normal_hookupover:
    An smirk "你知道，现在这个事情正式结束了，如果我不每天加班，我可以让你适应你的交易。"
    jump bangok_four_anna2_lab_normal_hookupover_end












label bangok_four_anna2_apartment_strapon_consideringmenu:
    menu:
        "我想我可以先尝试使用它。":
            $ anna2mood += 1
            $ bangok_four_anna2.position = "anna_strapon_receiving"
            $ renpy.pause(0.5)
            An bangok blush "优秀."
        "我想我可以尝试接收。":
            $ anna2mood += 1
            $ bangok_four_anna2.position = "player_receiving_strapon"
            $ renpy.pause(0.5)
            An smirk "我们渴望吗？"
            c "我承认我很感兴趣."
            An "在这种情况下..."
        "要不然我们把它当作你的假阳具怎么样？":
            $ renpy.pause(0.5)
            $ bangok_four_anna2.position = "dildo"
            c "我不太确定我内心是否有这个想法，但...听起来你想这么用它。"
            An bangok blush "我可以用它来工作。"
        "实际上，我现在不太确定要使用它...":
            $ renpy.pause(0.5)
            $ anna2mood -= 1
            An face "哦，为了-"
            An normal "行吧."
            if bangok_four_playerhasdick == False:
                jump bangok_four_anna2_apartment_nodick
            jump bangok_four_anna2_apartment_annaliesdown

    
    An bangok blush "如果你感兴趣，这有另一个有趣的功能。人造的精液."
    if bangok_four_anna2.position in ["anna_strapon_receiving","player_receiving_strapon"]:
        c "给我用的还是给你用的?"
        An "没有理由不能两者兼而有之。它是粉末形式的，所以我们基本上可以想做多少就做多少。它也是可配置的，因此我们可以稍后选择给谁来用。"
        An smirk "即使在人类的身体里面。"
    c "我明白了."

    An normal "如果我们以后要使用它，我现在应该去填补人造的。"
    menu:
        "那就别这样":
            $ renpy.pause(0.5)
            $ bangok_four_anna2.havefauxcum = False
            c "我不确定我很想玩这个。另外，清理是什么样的？"
            An "行吧"
        "好啊.":
            $ renpy.pause(0.5)
            $ bangok_four_anna2.havefauxcum = True
            show anna normal with dissolve
            play sound "fx/rummage.wav"
            $ renpy.pause(0.8)
            stop sound fadeout 1.0
            $ renpy.pause(0.8)
            hide anna with dissolve
            m "安娜翻遍了书包，抓起一个大包，细软管和几个没有标记的小包。{w = 0.3} 然后她消失在浴室里。"
            $ renpy.pause(0.5)
            play soundloop "fx/faucet1.ogg"
            queue soundloop "fx/faucet2.ogg"
            $ renpy.pause(1.0)
            menu:
                "等等, 你做了多少?":
                    $ renpy.pause(0.5)
                    An normal "嗯, 一个有趣的数量"
                "[[等待.]":
                    pass
            $ renpy.pause(1.0)
            stop soundloop fadeout 0.5
            show anna bangok blush with dissolve

    if bangok_four_anna2.position == "player_receiving_strapon":
        An "我还有一件事..."
        m "安娜放下玩具，又穿过她的书包，拉出一条黑色的皮带。"
        An smirk "嗯?"
        $ bangok_four_anna2.leash_asked = False
        label .leashmenu:
            menu:
                "继续吧":
                    $ anna2mood += 1
                    $ bangok_four_anna2.leash = True
                    $ renpy.pause (0.5)
                    hide anna with dissolve
                    $ renpy.pause (0.3)
                    play sound "fx/leather.ogg"
                    m "安娜解开我衣领侧面的带扣，然后将其放在我的脖子上并开始拧紧。"
                    play sound "fx/pda.wav"
                    An bangok blush "That feel good?"
                    m "我点点头。它很合身，但不够紧，无法限制我的呼吸。有很多的内部填充物来使其佩戴起来更舒适。"
                    show anna smirk with dissolve
                    An smirk "简直完美."
                "谁要戴着它?" if not bangok_four_anna2.leash_asked:
                    $ bangok_four_anna2.leash_asked = True
                    An normal "那肯定是你会穿着它。"
                    jump .leashmenu
                "不用了，谢谢.":
                    if bangok_four_malepartners > 0:
                        c "这不是我的事."
                    else:
                        c "我已经做了很多次这个事情了 ..."
                    An normal "行吧."
                    m "安娜把皮带放回包里."

    An bangok blush "好吗？"

    if bangok_four_anna2.position == "player_receiving_strapon":
        jump .player_receiving_strapon
    elif bangok_four_anna2.position == "anna_strapon_receiving":
        jump bangok_four_anna2_apartment_annaliesdown
    else: # dildo
        jump todo_bangok_four_anna2_dildo_content


    label .player_receiving_strapon:
        m "安娜从桌子上拿起带子，开始调整上面的许多带子。仔细看，似乎所有的带子都到了一个特定的点，把玩具分成两边。"
        if bangok_four_malepartners > 0:
            m "一侧的长度高于平均水平，仅比大多数人类稍大，而另一侧几乎是我前臂的长度 (和我认识的另一条龙差不多…)"
        else:
            m "一侧的长度高于平均水平，仅比大多数人类稍大，而另一侧几乎是我前臂的长度."
        show anna bangok blush with dissolve
        m "当安娜开始把带子抬到自己身上开始穿的时候，我意识到它奇怪的设计是这样的，当她使用玩具的时候，玩具的一端会进入她的身体。目前，根据她的情况，更大的一端将进入她的身子。"
        if bangok_four_malepartners > 0:
            menu:
                "其实...":
                    $ bangok_four_anna2.position = "player_receiving_larger"
                    c "我想试试看更大的那一端."
                    An sad "嗯？你是说-？你能...?"
                    An smirk "哦."
                    An "哦，我明白了。"
                    m "安娜迅速调整了绑带，以便为我使用较大的一端."
                    An "你确定你能处理好吗？"
                    c "相当肯定，是的."
                    show anna bangok lipbite with dissolve
                    m "安娜一路抬起皮带，用较小的一端很轻易地进入了自己的身体。"
                "[[什么也不说.]":
                    pass

        An normal "我有点担心你的任何可能的液体可能会从你的鸡巴上滴下来，因为我还没有研究你的基因组成。假设以后我们之间的物种之间有一些奇怪的微生物相容，那它们就会转化为感染的疾病。"
        c "绑带已经在我们之间提供了障碍，所以我们没有直接接触, 这应该是一个很好的预防措施。"
        An sad "即便如此，我还是更确定一点。给我一点时间."
        hide anna with dissolve
        m "安娜从桌子上的包装中取出一个避孕套，并用爪子迅速将其打开，将撕裂的橡胶包裹在绑带的底部，并形成临时的辅助屏障."
        show anna bangok blush with dissolve
        An normal "这样就行了."
        An bangok blush "至于你..."
        if bangok_four_anna2.leash == True:
            m "安娜向我走来，抓住皮带，轻快地拖拉，接着她在我的双腿之间摩擦了她佩戴的假阳具的尖端."
        else:
            m "安娜向我走来，用双臂搂着我的胸膛，她在我的双腿之间摩擦着她新佩戴的玩具的尖端。"
        An "我想你能搞定我?"
        c "呃... 是的?"
        An "你在说什么狗屁，但我选择相信你一次。"
        An bangok blush "我会让你先选，尽管我确实有一些特别的想法。"
        c "先挑?"
        An smirk "选择一个体位，人类。"

    label .player_receiving_strapon_assume_position:
        menu:
            "跪下." if bangok_four_anna2.straponplayerreceiveoral == False:
                $ bangok_four_anna2.straponplayerreceiveoral = True
                show anna sad:
                    ease 0.5 zoom 1.2
                show o2 at Pan((0, 150), (0, 150), 0.1)
                with ease
                show anna sad:
                    zoom 1.2
                with None
                m "当我下来，把我的脸和安娜的臀部放平时，我抬头看她有一种有点困惑的表情，或者也许是深思熟虑的表情,{w=0.3}{nw}"
                show anna smirk with dissolve
                m "当我下来，把我的脸和安娜的臀部放平时，我抬头看她有一种有点困惑的表情，或者也许是深思熟虑的表情, {fast}但这个表情很快就被她惯常的虚张声势所取代."
                c "这样好吗?"
                An "哦，没关系，我只是在想别的事情。"
                c "是关于什么的?"
                show anna face with dissolve
                $ renpy.pause (0.3)
                show anna smirk with dissolve
                An smirk "之后我会告诉你，现在你应该开始你的工作了。"
                show black with dissolve
                if bangok_four_anna2.position == "player_receiving_larger":
                    m "安娜拱起她的背，将她绝对巨大的玩具的尖端朝向我的脸。当我把嘴唇放在她的玩具的尖端时，她用一只爪子抚摸我的头。"
                else:
                    m "安娜拱起她的背，使她的鸡巴尖朝我的脸倾斜。当我把嘴唇放在尖端时，她用一只爪子抚摸我的头."
                An "如果你需要上来透气，给我点几下头，好吗？"
                m "我点了点头."
                An smirk "Good."
                if bangok_four_anna2.leash == True:
                    m "安娜用皮带伸到两腿之间，将皮带的手柄钩在尾巴的尖端上。当她毫不费力地用后躯拉扯它时，我立即被压了下去。"
                    m "这还不足以让我呕吐，但它给了我一个开始。我再次抬头看了她一眼，看到她已经交叉双臂，现在正以一种自鸣得意，霸气的表情低头看着我。我得到了她的信息，开始上下摆动我的头，进入一个节奏。"
                else:
                    m "安娜轻轻地将她的手移到我的后脑勺，突然以一种粗糙但可控的方式将我的头向下推到了她的长度的起点。"
                    m "这还不足以让我呕吐，但它给了我一个开始。我再次抬头看了她一眼，看到她现在正以一种自鸣得意，霸气的表情低头看着我。我得到了她的信息，开始上下摆动我的头，进入一个节奏。"

                if bangok_four_anna2.havefauxcum == True:
                    m "事实上玩具本身没有任何味道，这比我想象中的橡胶味要好。我很惊讶，突然感觉到并尝到了我舌头上少量的半甜液体。如果我不得不猜测，安娜把她制作的少量假精液灌进我的嘴里，以模仿前列腺液。"
                else:
                    m "事实上玩具本身没有任何味道，这比我想象中的橡胶味要好。"

                if bangok_four_anna2.position == "player_receiving_larger":
                    An smirk "继续，哺乳动物。我想看看你能让我有多舒服。"
                else:
                    An smirk "继续，哺乳动物。我期待你做出更好的努力。"
                menu:
                    "用你的手。":
                        if bangok_four_anna2.position == "player_receiving_larger":
                            m "我把我的手放上去，开始撸动的巨大玩具的其余部分，因为我吸的尽可能的多, 所以我没有作呕或窒息。"
                        else:
                            m "我握着我的手，一边吮吸上半部分，一边抽她玩具的下半部分。"
                        m "显然，绑带的双端性质也在为安娜高兴。她开始发出轻柔的咕咕和呻吟，因为我的努力转移并移动了她的玩具。"
                        An smirk "嗯，就是这样。继续这样做."
                        m "最初，我像实际的阴茎一样抽动玩具，但我意识到牢牢抓住它，而不是来回移动它会给安娜带来更愉快的体验。"
                        An bangok lipbite "Ohhh..."
                        m "事实上我的实验得到了来安娜呻吟的肯定，随后她稳定了自己，让我继续我正在做的事情。这样，我加快了步伐，更加努力地抽玩具。"
                        An bangok blush "老实说，你在这方面比我想象的要好得多，结果相当不错."
                        An bangok lipbite "你只管接着用你的手继续这样做。."
                        m "按照她的命令，我继续。虽然我不能移动玩具太多，我试图用它深深地操她，争取更深，更快的运动。"
                        if bangok_four_anna2.leash == True:
                            m "安娜坚定地拉着皮带，把我拉得更远。"
                        else:
                            m "据安娜给了一个强大的推在我的后脑勺，把我进一步推进了他的身体。"
                        m "尽管我没有作呕，但安娜的手势极大地考验了我保持镇定的能力。反射性地，我抓住安娜的大腿，以防止自己在她继续前进时离的太远。"
                        m "她的大腿摸上去是柔软的，但下面有强壮的肌肉，这与玩具的僵硬形成了令人愉快的对比。一种被唤醒的诱惑，我的手向上移动，我发现自己抚摸着她的后躯。比她的大腿柔软得多，但它们下面仍然有大量的肌肉。"
                        m "安娜停顿了一下，低头看着我，带着俏皮的微笑。"
                        An bangok blush "觉得怎么样?喜欢吗"
                        c "Mhm."
                        An smirk "那我们进入主要活动怎么样？毕竟只是抚摸这些腿可不算是身体检查。"
                        menu:
                            "继续":
                                hide black with dissolve
                                c "好吧，让我们继续前进，这样我就可以亲眼看看。"
                                An normal "好吧."
                                # Return to the "Get on your knees" choice menu, remove the "Get on your knees" option.
                                jump .player_receiving_strapon_assume_position
                            "完成工作.":
                                pass
                        c "我真的很喜欢这个..."
                        An "如果你坚持..."
                        An bangok blush "如果您需要我放手，请轻拍我的大腿，我怕因为快感我可能会变得有些粗鲁."
                        c "明白了."
                        m "安娜重新调整了姿势，然后将人造公鸡放回我的嘴里。我把一只手放回玩具上，回到和以前一样的节奏来取悦她。我的另一只手伸向我自己的生殖器，以愉悦自己。"
                        m "当安娜粗暴而深入地推我的头时，我对玩具的抓握很快受到了挑战。当玩具开始撞向我的喉咙后部时，我微微作呕。"
                        An bangok lipbite "嗯，有一些有趣的声音。不介意再听一些。"
                        m "安娜的推力速度加快了，当玩具开始进入我喉咙的最上部时，我终于被迫把手从她的玩具上拿开，放在她的大腿上。"
                        m "不自觉地，我做了更多的好笑和咯咯声，安娜的推力增加速度和稳步增长的节奏。很明显，以这种速度，我们将在不久的时间内达到高潮。"
                        An "希望你已经准备好了，因为这将是一个大的..."
                        m "我为安娜即将到来的高潮做好准备，也接近我自己的高潮。"
                        play sound "fx/snarl.ogg"
                        $ bangok_four_anna2.annacame = True 
                        if bangok_four_anna2.havefauxcum == True:
                            if bangok_four_anna2.leash == True:
                                m "安娜在咆哮宣布性高潮之前又做了几次深深的抽插，当她插入我的喉咙时，安娜用力拉着我的头."
                            else:
                                m "安娜在咆哮宣布性高潮之前又做了几次深深的抽插，当她插入我的喉咙时，安娜用力推了我的头。"
                            show white:
                                alpha 0.0
                                pause 1.0
                                ease 0.5 alpha 1.0
                                pause 1.5
                                linear 3.0 alpha 0.0
                            with dissolve
                            m "我不确定高潮会发生什么。但当我感觉到温暖的液体进入我的胃，再加上玩具的感觉和安娜的存在，我的本能接管了我的身体。随着狂喜，欣快感和温暖的浪潮冲过我，我的脑海里一片空白，当我释放出一种紧张而低沉的呻吟时，我也到达了高潮"
                            if persistent.bangok_inflation == True:
                                m "我觉得我的胃开始向外膨胀，安娜的意想不到的大量体液开始往外喷，并继续聚集在我体内。我很难全部吞下去，很快我觉得它溢出我的嘴，呼吸几乎是不可能的。安娜一定注意到了，因为她突然把我的头拉了出来，我松了一口气。"
                            else:
                                m "安娜俯身进入高潮，迫使她的公鸡留在我和她的身体深处。尽管我的高潮已经过去了，但我从安娜的表演中感到有些匆忙。最终，我开始意识到我无法呼吸，安娜显然也是如此，因为她很快就把玩具从我身上拉了出来。"
                        else:
                            if bangok_four_anna2.leash == True:
                                m "安娜又给了几个深深的抽插，然后用吼声宣布她的性高潮，当她大声呻吟并用大腿挤压我的头时，用力地猛拉我的头。"
                            else:
                                m "安娜又给了几个深深的抽插，然后用吼声宣布她的性高潮，当她大声呻吟并用大腿挤压我的头时，用力地猛拉我的头."
                            show white:
                                alpha 0.0
                                pause 1.0
                                ease 0.5 alpha 1.0
                                pause 1.5
                                linear 3.0 alpha 0.0
                            with dissolve
                            m "我不确定高潮会发生什么。但当我感觉到温暖的液体进入我的胃，再加上玩具的感觉和安娜的存在，我的本能接管了我的身体。随着狂喜，欣快感和温暖的浪潮冲过我，我的脑海里一片空白，当我释放出一种紧张而低沉的呻吟时，我也到达了高潮"
                            m "安娜俯身进入高潮，迫使她的公鸡留在我和她的身体深处。尽管我的高潮已经过去了，但我从安娜的表演中感到有些匆忙。最终，我开始意识到我无法呼吸，安娜显然也是如此，因为她很快就把玩具从我身上拉了出来。"
                    "深喉.":
                        m "我深吸了一口气，把头进一步抵住到她的鸡巴上，努力不让它堵住气管，因为它开始阻塞我的嘴和喉咙。"
                        if bangok_four_anna2.position == "player_receiving_larger":
                            m "我拉回来再吸一口气，我只成功地走了不到一半，我已经有一些麻烦了。"
                        else:
                            m "我又拉回来呼吸了一口气, 我设法得到了大部分空气, 但在我设法击中基地之前还有一两英寸。"
                        m "显然，绑带的双头性质也让安娜感到高兴。她开始发出轻柔的咕噜声和呻吟声，因为我那边的努力发生了变化，并移动了她那边的鸡巴。"
                        An bangok lipbite "嗯，上道了。继续这样做。"
                        m "安娜微微抬起臀部，让她的阴茎沿着我的嘴后滑动，然后又往下沉。这一次更深入我的喉咙。我不得不努力集中注意力，以免窒息或作呕，因为呻吟和咯咯声混合在一起。安娜似乎对此一点也不在意。事实上，她似乎对她所听到的感到相当高兴。"
                        if bangok_four_anna2.position == "player_receiving_larger":
                            m "她用自己的呻吟回应了我的惊呼，因为绑带像操我一样地操她。如果我必须估计的话，我仍然只走了大约四分之三的长度。她突如其来的粗暴，加上她的态度，让我很生气。于是我伸手下去，开始取悦自己，她继续说。"
                        else:
                            m "她用自己的呻吟回应了我的惊呼，因为绑带像操我一样操她。在她的帮助下，我现在已经走完全程了，不断地压在障碍物上。她突如其来的粗暴，加上她的态度，让我很生气。于是我伸手下去，开始取悦自己，她继续说。"
                        m "玩具在我喉咙里的感觉让我觉得我要爆炸了。被支配的感觉令人振奋。知道安娜也很享受，这让它变得更加紧张."
                        m "这种节奏持续了一段时间，我们享受着这种感觉，安娜最终松开了手，给了我片刻的呼吸时间。很明显，我们俩都将在不久内达到性高潮。"
                        hide black with dissolve
                        An bangok blush "那么，你是想继续参加主赛事，还是想继续这样做？"
                        menu:
                            "继续正事":
                                c "尽管这很愉快，但我想继续做其他事情。"
                                An normal "行吧."
                                # Return to the "Get on your knees" choice menu, remove the "Get on your knees" option.
                                jump .player_receiving_strapon_assume_position
                            "完成作业。":
                                pass
                        c "我真的很喜欢这个......"
                        An smirk "好吧，如果你坚持......"
                        if bangok_four_anna2.leash == True:
                            m "我心里有一瞬间的忐忑不安，安娜站起身来，继续把她的鸡巴抽进我的嘴里。皮带仍然挂在她尾巴的尾端。我知道接下来会发生什么，抬起头看到她脸上邪恶的笑容，她知道我想要它。"
                        else:
                            m "我心里有一瞬间的忐忑不安，安娜站起身来，继续把她的鸡巴抽进我的嘴里。我知道接下来会发生什么，抬起头看到她脸上邪恶的笑容，她知道我想要它。"
                        An smirk "记住，如果你需要我松口，请拍我几下。" 
                        show black with dissolve
                        $ renpy.pause (0.5)
                        m "她慢慢地又开始移动她的臀部，让我习惯了这种感觉。我能感觉到她的阴茎尖在我的喉咙后部再次发痒，因为她在我的嘴里进进出出。"
                        m "我不想让她久等，我开始沿着她的玩具往下走。这赢得了安娜的一声小小的呻吟，因为她更加用力地。"
                        An bangok lipbite "你非常擅长这个，我能感觉到你正在全力以赴。"
                        if bangok_four_anna2.leash == True:
                            m "我条件反射地咽了咽口水，鸡巴沉入了我的喉咙后部。安娜捋了捋我的头发，然后再次用皮带把我拉得更远。"
                        else:
                            m "我条件反射地咽了咽口水，鸡巴沉入了我的喉咙后部。安娜捋了捋我的头发，然后用爪子把我的头往下推。"

                        if bangok_four_anna2.position == "player_receiving_larger":
                            m "回到四分之三的标记，安娜咕哝了一声，她用力将剩下的鸡巴放下，一股轻微的灼烧感涌上我的胸膛。她压在我的脸上，开始用臀部磨蹭我。"
                        else:
                            m "到达基地后，安娜咕哝了一声，她压在我的脸上，开始用臀部磨蹭我。"
                        $ renpy.pause (0.8)
                        m "我只持续了几秒钟，然后我不得不开始敲打安娜的大腿。她往后退了一步，让我赶紧走。"
                        An bangok blush "下面还好吗？"
                        $ renpy.pause (0.5)
                        m "深吸了几口气后，我点了点头，然后又低下了头。"
                        m "安娜没有浪费时间，我的脸很快再次碰到她的臀部，她继续以极快的速度操我的脸。以她的速度，毫无疑问，我们两个很快就会达到极限。"
                        m "她的呼吸非常沉重，几乎是咆哮着，因为她的抽插越来越没有节奏。"
                        An bangok lipbite "我希望你已经准备好迎接这一切了......,{w=0.8}{nw}"
                        An orgasm "希望你已经准备好迎接这一切......,{fast}我快要..."
                        play sound "fx/snarl.ogg"
                        $ bangok_four_anna2.annacame = True 
                        if bangok_four_anna2.havefauxcum == True:
                            if bangok_four_anna2.leash == True:
                                m "安娜又深深地哼了几下，然后咆哮着宣布她的高潮，当她进入我的喉咙并用大腿挤压我的头时，她用力将我的头拉到底部。"
                            else:
                                m "安娜又深深地哼了几下，然后咆哮着宣布她的高潮，当她进入我的喉咙并用她的大腿挤压我的头时，她用力将我的头推到底部."
                            show white:
                                alpha 0.0
                                pause 1.0
                                ease 0.5 alpha 1.0
                                pause 1.5
                                linear 3.0 alpha 0.0
                            with dissolve
                            m "我不确定高潮会发生什么。但当我感觉到温暖的液体进入我的胃，再加上玩具的感觉和安娜的存在，我的本能接管了我的身体。随着狂喜，欣快感和温暖的浪潮冲过我，我的脑海里一片空白，当我释放出一种紧张而低沉的呻吟时，我也到达了高潮"
                            if persistent.bangok_inflation == True:
                                m "我感觉到我的胃开始向外膨胀，因为安娜出乎意料量开始稳定地喷出并继续聚集在我体内。很难把它全部吞下去，因为很快我就感觉到这些液体从我的嘴里溢出来，使呼吸比以前更加不可能。安娜一定注意到了，因为她突然退了出去了，我松了一口气。"
                            else:
                                m "安娜靠在高潮中，迫使她的阴茎深深地留在我体内，也留在她体内。尽管我的性高潮已经过去，但我还是从安娜的表演中感受到了一些冲动。但最终，我开始意识到我无法呼吸，安娜显然也注意到了如此，因为她迅速地把玩具从我身上拉了出来。"
                        else:
                            if bangok_four_anna2.leash == True:
                                m "安娜又深深地哼了几下，然后咆哮着宣布她的高潮，用力把我的头拉到底部，她大声呻吟，用大腿挤压我的头."
                            else:
                                m "安娜又深深地哼了几下，然后咆哮着宣布她的高潮，用力将我的头推到底部，同时她大声呻吟并用大腿挤压我的头."
                            show white:
                                alpha 0.0
                                pause 1.0
                                ease 0.5 alpha 1.0
                                pause 1.5
                                linear 3.0 alpha 0.0
                            with dissolve
                            m "我不确定高潮会发生什么。但当我感觉到温暖的液体进入我的胃，再加上玩具的感觉和安娜的存在，我的本能接管了我的身体。随着狂喜，欣快感和温暖的浪潮冲过我，我的脑海里一片空白，当我释放出一种紧张而低沉的呻吟时，我也到达了高潮"
                            m "安娜靠在高潮中，迫使她的阴茎深深地留在我体内，也留在她体内。尽管我的性高潮已经过去，但我还是从安娜的表演中感受到了一些冲动。但最终，我开始意识到我无法呼吸，安娜显然也注意到了如此，因为她迅速地把玩具从我身上拉了出来。"
                hide white with dissolve
                An sad "下面一切都还好吗？"
                hide black with dissolvemed
                m "我花了一点时间喘口气，然后向她竖起了大拇指."
                c "还好...这真是太棒了."
                show anna normal with dissolve
                m "安娜对我微微一笑，然后慢慢地取下现在非常光滑的绑带，在我旁边的地板上坐下。"
                # skip to either the scene where the player fucks anna, or the ending scene depending on who went first. The ending scene isn't written yet
                jump todo_bangok_four_anna2_dildo_content
            "仰卧。":
                if bangok_four_anna2.position == "player_receiving_larger":
                    m "我朝沙发走了一步，让自己躺在一个舒适的姿势上。安娜紧随其后，把自己放在我的双腿之间，绑带的巨大长度从我的大腿顶部一直延伸到我的胸部底部。"
                    c "(Oh boy...)"
                else:
                    m "我朝沙发走了一步，让自己躺在一个舒适的姿势上。安娜也跟着把自己放在我的两腿之间。"
                m "她开始用玩具在我的身体上磨蹭，然后隐约出现在我身上，看起来对自己能够让我蠕动感到非常满意。"
                jump todo_bangok_four_anna2_dildo_content
            "转身弯腰.":
                hide anna with dissolve
                if bangok_four_anna2.leash == True:
                    m "我走到其中一把椅子上。背对着安娜，我把膝盖放在座位上，用椅子的头抬起上半身。安娜也跟着走到我身后，用皮带轻轻地把我拽回她身边，把玩具磨在我的背上。"
                else:
                    m "我走到其中一把椅子上。背对着安娜，我把膝盖放在座位上，用椅子的头抬起上半身。安娜也跟着走到我身后，抓住我的腰，把玩具磨在我的背上。"
                jump todo_bangok_four_anna2_dildo_content
            "看看安娜的想法.":
                c "你有什么想法？"
                $ renpy.pause (0.8)
                hide anna with dissolve
                m "安娜朝沙发走了一步， "
                jump todo_bangok_four_anna2_dildo_content




label todo_bangok_four_anna2_dildo_content:
    play sound "fx/system3.wav"
    s "内容不足！回滚并保存或准备崩溃."
    $ renpy.error("Out of content.")