init python:
    bangok_anoney_xemera2_set_condition = False
    bangok_anoney_xemera2_clean_arms = None
    bangok_anoney_xemera2_refuse_participate = False
    bangok_anoney_xemera2_lick_slit = None
    bangok_four_xemera2_ws_mouth_unasked = True
    bangok_anoney_xemera2_massage_only = None

$ mp.emeraromance == True # 必须在Xemera进行按摩才能继续。

label bangok_anoney_xemera2_set_condition:
    $ bangok_anoney_xemera2_set_condition = True
    jump bangok_anoney_xemera2_set_condition_return

label bangok_anoney_xemera2_answ_machine:
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (0.5)
    Em "你好，[player_name]。 对不起这么晚才留言。"
    Em ques "今天一天很长，我们刚开完一个即将到来的节日的计划会议。"
    Em laugh "上次你给我的按摩很棒。我从未感觉这么好过。"
    Em frown "但在节日和你的同伴大使的事情之间，所有这些官僚主义让我很疲惫。"
    Em ques "我想请求你再给我一次那双神奇的手的按摩。"
    Em normal "今晚和明天我会在图书馆的办公室里。希望你能来。"
    play sound "fx/answeringmachine.ogg"
    $ renpy.pause (0.8)
    c "（文化和艺术部长想要一个和我手的夜晚约会。显然我留下了很好的印象。）"
    jump ml_answeringmachine_end

label bangok_anoney_xemera2_emera:
    stop music fadeout 2.0
    $ renpy.pause (0.5)
    scene black with dissolvemed
    $ renpy.pause (0.5)
    play sound "fx/steps/clean2.wav"
    scene bangok_four_library night at Pan((60, 228), (0, 228), 2.0) with dissolveslow

    m "今晚图书馆很安静。"
    c "（我猜大家已经有了他们的深夜阅读材料。）"
    m "我经过一条过道时，看见雷米把头埋在一个大盒子里，显然是在寻找某种小玩意来进一步他的研究。"
    m "我继续向图书馆的私人区域走去，上次访问时我也在那里。"

    scene black with dissolvemed
    play sound "fx/steps/clean2.wav"
    $ renpy.pause (0.5)
    scene bangok_anoney_library_corridor_night with dissolvemed

    m "找到那个熟悉的门，上面写着文化和艺术部长，我敲了敲门。"

    play sound "fx/knocking1.ogg"

    $ renpy.pause (2.0)

    Em "进来吧。"

    play sound "fx/door/door_open.wav"

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emeraroom_night with dissolvemed

    $ renpy.pause (0.5)

    play sound "fx/door/close2.wav"

    show emera laugh b with dissolve

    play music "mx/eveningmelody.ogg" fadein 2.0

    Em "你好，[player_name]！很高兴再次见到你。由于目前的广泛警察调查，我不确定你是否会有时间。"

    c "我需要从不断的警察工作中休息一下。当我穿过传送门时，这并不是我打算全职做的工作。再说了，作为大使意味着体验构成社会的龙的故事。"
    
    Em ques b "我明白了。我很高兴你会认为我是你要体验的龙之一。很多时候，我觉得自己被当作只是另一个高高在上、自命不凡、冷漠的龙，需要用身体彩绘和珠宝来装点自己以显得重要。"

    menu:
        "窃笑。":
            c "（有趣的是，这正是我对你的看法。）"
            Em frown b "你说什么？"
            m "我咳嗽了一下，试图掩盖我的失言。"
            play sound "fx/throat_clear.ogg"
            c "抱歉，只是清清嗓子。"
        "奉承。":
            c "你是一个非常重要的政治家，来自一个富裕的家庭，你的工作不是一种活跃的生活方式。"
            c "那么你为什么不应该戴珠宝或使用鳞片彩绘以彰显你的地位呢？"
            Em "确实。没有这种状态，我怎么进行这些压力大、复杂的谈判呢？"
    
    Em ques b "如果警察局长能到处带着胸前的大徽章来展示他的权威，为什么我被鄙视展示我的地位呢？"
    Em "啊，布莱斯，至今为止在离开城市后唯一适合我做伴的龙。"
    c "你为什么这么认为？"
    Em normal b "因为他是和我一样的地龙。"
    Em ques b "他忠诚且能应付大量的工作。"
    Em normal b "他喉咙上的疤痕是个遗憾；那是角亮（Horn Shine）永远无法掩盖的。但如同钻石，最精美的宝石是那些有瑕疵的。"
    
    if brycescenesfinished >= 1 and not leftbryce:
        c "（显然她从未见过布莱斯在酒吧关门时摇摇晃晃走出来。）"
    elif katsuavailable or (katsuunplayed == False):
        c "（我在想提起我遇到的那条龙，卡特苏哈鲁，会不会是个坏主意。）"
        c "我记得你在他把车拉到龙公园时见过卡特苏哈鲁，你们似乎认识很久了。"
        c "为什么他不合适呢？"
        Em ques b "嗯，我们确实认识很久了。他做的手工冰淇淋非常精致，如果他有库存的话。"
        Em laugh b "尤其是新鲜制作的。"
        
        if bangok_four_xkatsu.unplayed == False:
            c "的确，就在那天我帮他准备了一批新鲜的。这确实很精致，正如你所说。"
        else:
            c "我明白了。如果有机会，我一定要记住这点，看看它是否像你说的那么好。"
        
        Em normal b "无论如何，他对我来说太老了。如果他年轻二十岁，那也许。"
    else:
        c "（她确实有道理；我没有见过其他地龙。）"

    Em "总之，闲话少说，回到我给你留言的原因。"
    Em "我想你还记得上次的按摩技巧吧？"
    m "我点了点头。"
    Em ques b "很好。"

    scene black with dissolvemed

    $ renpy.pause (0.5)

    show bangok_anoney_emeramassage_night at Pan((960, 250), (960, 0), 6.0) with fade

    $ renpy.pause (1.0)
    play sound "fx/sheet.wav"
    m "和上次一样，她拿出了同样的垫子和枕头，然后背对着我躺下。"

    m "我跪在垫子的边缘，开始按摩她脖子上的鳞片，小心不要让我的手臂碰到她头上的刺。上次差点刮到，我可不想再经历一次。"

    Em laugh b "啊，是的，很好。"

    m "当我移到她的肩膀时，她靠向我的按摩，像人们在旧世界里养的猫一样。"

    show bangok_anoney_emeramassage_night at Pan((960, 0), (960, 250), 4.0)

    c "你把这垫子和枕头放在这儿就是为了按摩吗？"

    if (persistent.nsfwtoggle == False) or bangok_four_common.bangnokay.check():
        $ bangok_anoney_xemera2_massage_only = True
        jump bangok_anoney_xemera2_massage_only
    else:
        pass # 继续到情色内容！

    Em frown b "其实，这不是我唯一的用途。它还有一个相当个人和私密的原因。"

    c "哦？"

    Em ques b "你可能不知道，除非你读过关于龙生物学的教科书。"
    Em normal b "地龙母龙大约每三个月会排卵一次。即使卵未受精，它将在卵室内停留一段时间，直到硬壳形成。"
    Em frown b "当然，当下一个周期开始时，身体最终会排出卵。然而，显然，未计划的排卵可能非常尴尬，甚至危险。"

    if persistent.bangok_cervpen:
        Em "幸运的是，我们的创生过程，不管是什么，找到了一种方法来控制我们地龙的产卵时间。"
        Em "如果交配时雄龙的阴茎头部推入卵室，身体将提前进入下一个周期，并开始排卵过程。"
    else:
        Em "幸运的是，我们的创生过程，不管是什么，找到了一种方法来控制我们地龙的产卵时间。交配时，身体会提前进入下一个周期，并开始排卵过程。"

    m "我抬起上半身，以便能够到达她背上的硬鳞片，并用我的体重按在下面的肌肉上。"

    show bangok_anoney_emeramassage_night at Pan((960, 250), (960, 500), 4.0)

    Em ques b "由于我目前没有雄龙伴侣来满足我的需求，并且担心任何其他我可能请求的人可能会试图勒索我或要求政治上的好处，我通常自己解决问题；使用一个模仿地龙工具的愉悦棒。"

    Em mean b "鉴于你目前的大使身份，这意味着你没有嵌入通常的龙政治，你的工作要求你与我和议会的其他成员保持良好的关系。"

    Em ques b "还有一个更个人的原因：{w=0.2}你那双手在我外部工作得如此神奇，我很好奇它们在我内部工作会不会同样神奇。"

    menu:
        "接受。":
            pass

        "拒绝。":
            $ bangok_anoney_xemera2_refuse_participate = True
            c "我没有想到要执行亲密的职责，我以为这只是一个按摩，既然你说你自己解决，我拒绝参与。"
            Em frown b "我明白，我猜是我愚蠢地认为你会对我们人民最重要的结合仪式感兴趣。"
            show bangok_anoney_emeramassage_night at Pan((960, 500), (960, 800), 6.0)
            m "我迅速绕到她的后面，现在在她的臀部和臀部工作。"
            m "接下来的按摩在沉默中进行。她说的话动摇了我的内心。调查谋杀案以及需要获得发电机以拯救人类，被要求取悦一个政治家对我来说太多了。"
            m "（我知道这次按摩不如第一次好，我只能希望这不会对人龙关系产生不利影响。）"
            jump bangok_anoney_xemera2_conclusion

    if bangok_four_anna2.annacame == True:
        c "（亲身体验了我的手能为安娜做什么魔法，我对能取悦她充满信心。）"
    else:
        c "（虽然没有与女性的经验，但我决定相信我的判断，正如她通过她的按摩指导我一样，她会让我知道什么感觉好。）"

    m "我绕到她的后面，现在在她的臀部和臀部工作。"

    show bangok_anoney_emeramassage_night at Pan((960, 500), (960, 800), 6.0)

    Em laugh b "是的，是的！那感觉太好了。哦，当你最终回到传送门时，我会想念被这样按摩。"

    m "剩下的就是她的尾巴了。我从尖端开始，然后慢慢向靠近她身体的地方移动。考虑到今晚我的手会有很多活动，这次我可以按摩之前被忽略的区域，因为我的手找到了她尾巴根部周围的地方。"

    m "完成按摩后，我站起来伸展了一下腿。意识到最好不要让任何人走进来打扰我们，我走到门口，把房间状态牌滑到“占用中”并锁上了门。"
    $ renpy.pause (1.0)
    play sound "fx/door/handle.wav"
    $ renpy.pause (1.0)
    play sound "fx/door/lock.ogg"

    m "我把窗帘拉到窗户上。最后一件艾梅拉希望的是让其他龙知道她在和人类进行亲密关系。"
    $ renpy.pause (0.5)
    play sound "fx/envelope.wav"
    $ renpy.pause (1.0)
    m "从门口转身，我决定脱衣服，考虑到今晚的活动可能会很混乱。"
    play sound "fx/zip.ogg"
    $ renpy.pause (1.5)
    play sound "fx/undress.ogg"
    Em laugh b "多么异国情调。我一直想知道你穿的布层下面有什么。"
    
    if bangok_four_playerhasdick is None:
        Em ques b "对不起，我们没有收到关于性别特征的信息；你有哪种生殖器官...？"
    elif bangok_four_playerhasdick == True:
        jump .male
    elif bangok_four_playerhasdick == False:
        jump .female

    menu:
        "一个阴茎。":
            $ bangok_four_playerhasdick = True
            label .male:
            if persistent.bangok_cloacas == True:
                Em mean b "真有趣，你的交配工具就这样挂在外面。看起来又小又皱又软。你没有裂缝来保护它吗？而且我也看不到你的肛门..."
                c "我们没有泄殖腔，所以我们的生殖器和肛门是分开的。"
            else:
                Em mean b "真有趣，你的交配工具就这样挂在外面。看起来又小又皱又软。你没有裂缝来保护它吗？"
                c "不，我们的生殖器没有裂缝。"

        "一个阴道。":
            $ bangok_four_playerhasdick = False
            label .female:
            if persistent.bangok_cloacas == True:
                Em "真有趣，但我相信我在你腿间看到两个开口？"
                c "我们没有泄殖腔，所以我们的生殖器和肛门是分开的。"

    m "我指了指我的衣服。"
    c "我们也穿衣服，作为鳞片的替代物，用来保护我们的身体，包括我们的生殖器，不受伤害并保持温暖。"

    c "与龙不同的是，脱掉衣服并暴露自己只是在我们想和某人亲密或洗澡时才会做的事。"

    c "在我们开始更“身体”的活动之前，在人类文化中，通常会为双方提供刺激，以进一步加深彼此的联系，并让伴侣为性交做好准备。"
    Em ques b "哦，一个人类的仪式，有人曾经推测人类是如何浪漫的。我从未想到能在现实中体验到这样的事情。"
    c "你能坐在沙发上，两腿分开吗？这对你来说应该比在地板上做更舒服。"
    Em laugh b "当然。我很想知道你打算做什么。我们已经有了很多身体接触，感谢你的按摩，我们龙足够坚韧，可以直接进入不需要准备的行动。"

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emera_sofa:
        yalign 1.0
        linear 2.0 yalign 0.0
        yalign 0.0
    with dissolveslow


    m "艾梅拉从地板上起来，坐在她的沙发上。"
    play sound "fx/bed.ogg"
    show bangok_anoney_emera_sofa:
        yalign 0.0
        linear 1.0 yalign 1.0
        yalign 1.0
    $ renpy.pause (2.5)
    m "我把她的枕头移过来，坐在上面，{w=0.5}{nw}"
    play sound "fx/sheet.wav"
    m "我把她的枕头移过来，坐在上面，{fast} 面对她的腹股沟。"
    play soundloop "fx/purr.ogg" fadein 1.0
    if persistent.bangok_cloacas == True:
        m "我把手放在她的腹股沟上，开始摩擦她单一的垂直裂缝周围的小鳞片。"
    else:
        m "我把手放在她的腹股沟上，开始摩擦她裂缝周围的小鳞片。"
    play sound ["fx/rub1.ogg", "fx/wipe.ogg", "fx/rub1.ogg", "fx/wipe.ogg", "fx/rub1.ogg"]
    Em laugh b "那很痒，但感觉很好。龙爪并不适合这种精细的工作，因为我们的爪子和有限的灵活性，至少对那些用它们走路的龙而言。"
    m "艾梅拉轻轻地把前爪放在我的头上，用爪子梳理我的头发。"

    if bangok_four_playerhasdick == True:
        Em normal b "你头上的毛发真是奇怪。虽然有些更奇异的物种也有毛发，但通常是短而硬的，会自己竖立起来。"
    else:
        Em normal b "你头上的毛发真是奇怪。虽然有些更奇异的物种也有毛发，但通常是短而硬的，会自己竖立起来。我没想到人类会让他们的头发长这么长。和其他大使的头发不同。"

    c "你所说的毛发，其实是头发，它由角蛋白组成，类似于你的爪子，只是明显更细。"
    m "我笑了笑。她的爪子在我头发中移动，让我想起在博物馆中看到过的金属头部按摩器。"
    Em ques b "我没有弄疼你吧？"
    c "没有。没事的。在旧时代，我们有这些多叉的金属棒，把叉子分散在头上，然后移动棒子来按摩头部。我几年前在博物馆里见过一个。"

    if persistent.bangok_cloacas == True:
        m "艾梅拉的裂缝开始张开，露出她粉红色的内壁，还有她的兴奋的光泽。我能感觉到周围的区域因为血流增加而变得更温暖。"
        m "向前伸出手指，我把拇指钩进她的裂缝墙上，然后拉开。"
    else:
        m "艾梅拉的上裂缝开始张开，露出她粉红色的内壁，还有她的兴奋的光泽。我能感觉到周围的区域因为血流增加而变得更温暖。"
        m "向前伸出手指，我把拇指钩进她的上裂缝墙上，然后拉开。"

    m "裂缝轻易地张开，显示出极大的弹性。"
    c "（我猜雄龙可能不是最佳位置，所以需要一些灵活性来确保他能够成功地插入。）"
    c "（或者，也许龙族被创造得如此有弹性，以便能够容纳其他龙种，当然是有一定范围的。）"
    
    menu:
        "舔。":
            $ bangok_anoney_xemera2_lick_slit = True
            m "我把嘴靠近她张开的裂缝，开始用舌头舔她内壁能达到的地方。"
            c "（她的内壁的质地如预期般光滑，但也感觉既密实又可塑，类似于一种密实但可压缩的聚合物。）"
            play sound "fx/sniff.ogg"
            c "（这么近的地方味道很浓。我只能想象这种气味对敏感度更高的龙有什么影响。）"
            play sound "fx/buck.ogg"
            m "艾梅拉的腿在我的舌头碰到她内壁时不由自主地踢了一下。"
            m "艾梅拉四处看了看，以防她的动作伤到我。"
            Em frown b "对不起。我不习惯感觉到像你舌头那样的质地在敏感区域。你没事吧？"
        "仅用手指。":
            $ bangok_anoney_xemera2_lick_slit = False
            m "我让手指在她张开的裂缝开口处游走，按摩能达到的内壁，而不超过几个指关节深。"
            c "（她的内壁的质地如预期般光滑，但也感觉既密实又可塑，类似于一种密实但可压缩的聚合物。）"
            play sound "fx/sniff.ogg"
            c "（这么近的地方味道很浓。我只能想象这种气味对敏感度更高的龙有什么影响。）"
            play sound "fx/buck.ogg"
            m "艾梅拉的腿在我的手指碰到她内壁时不由自主地踢了一下。"
            m "她四处看了看，以防她的动作伤到我。"
            Em frown b "对不起。我不习惯感觉到像你手指那样的光滑质地在敏感区域。你没事吧？"
    
    m "我摇了摇头，继续探索她的裂缝。"

    Em ques b "哦，我可以永远这样坐着，你在下面。你有没有考虑过在完成所有大使事务后成为我的助手？"
    m "我从她的裂缝中退出来，喘了几口气，回答她的问题。"
    c "我认为这样做不明智。虽然了解更多的龙文化是很有趣的，但你之前说你希望建立一个家庭。"
    c "我不能给你一个家庭，我也不想妨碍你和你未来伴侣之间的关系，一旦你找到了合适的伴侣。"
    
    if bangok_anoney_xemera2_lick_slit:
        m "我重新开始用嘴探索她的裂缝。她的兴奋达到了顶峰。我的脸上沾满了她的液体，{w=0.5}{nw}"
        play sound "fx/singlesplash.ogg"
        m "我重新开始用嘴探索她的裂缝。她的兴奋达到了顶峰。我的脸上沾满了她的液体，{fast} 多余的液体开始滴落，形成一个小水坑在地板上。"
    else:
        m "我重新开始探索她的裂缝。她的兴奋达到了顶峰。我的手几乎都沾满了她的液体，{w=0.5}{nw}"
        play sound "fx/singlesplash.ogg"
        m "我重新开始探索她的裂缝。她的兴奋达到了顶峰。我的手几乎都沾满了她的液体，{fast} 多余的液体开始滴落，形成一个小水坑在地板上。"
    
    $ renpy.pause (0.5)
    play sound "fx/singlesplash.ogg"
    m "艾梅拉深吸一口气，盯着天花板，分析着我的回答，无疑在内心进行着激烈的争论。"
    m "过了一会儿，她低下头，叹了口气。"
    Em "你当然是对的。我习惯于得到我想要的，所以没有完全考虑到我想要的后果。"
    stop soundloop fadeout 5.0 #停止呼噜声，58秒长，也许可以更改为循环如果这个场景花费超过1分钟？
    if bangok_anoney_xemera2_lick_slit:
        Em bangok blush b "我觉得我已经准备好了，一种欲望在我的内壁深处产生，你的舌头无法触及。"
    else:
        Em bangok blush b "我觉得我已经准备好了，一种欲望在我的内壁深处产生，你的手指无法触及。"
    
    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emera_presenting at Pan((960, 250), (960, 500), 4.0)

    $ renpy.pause (2.0)
    play sound "fx/sheet.wav"
    if persistent.bangok_cloacas == True:
        m "艾梅拉回到了垫子上，把头靠在枕头上。不同于之前，她抬起后腿，站在后腿上，腿分得很开，显示出她的单一垂直裂缝。"
        m "周围的鳞片在光线下闪闪发光，显然不是因为鳞片亮。显然我的前戏让她情绪高涨。"
    else:
        m "艾梅拉回到了垫子上，把头靠在枕头上。不同于之前，她抬起后腿，站在后腿上，腿分得很开，显示出她的裂缝和肛门。"
        m "周围的鳞片在光线下闪闪发光，显然不是因为鳞片亮。显然我的前戏让她情绪高涨。"

    m "艾梅拉用爪子示意身后的一个柜子。"
    Em normal b "你会在里面找到润滑剂和其他需要的用品。"
    show black with dissolvemed
    
    m "我走到艾梅拉指示的柜子前，打开柜门。"
    play sound "fx/cabinet.ogg"
    # if persistent.havetestresults == True:
    #     Em ques b "我看过你的测试结果。数据说我们在性兼容性方面没有问题，所以不必使用保护措施。"
    # else:
    #     Em ques b "如果你想用保护措施，这里有。考虑到我是地龙，我们应该很坚韧，所以我怀疑我能从你那里感染任何东西。"

    if bangok_four_playerhasdick == True:
        Em ques b "如果你想用保护措施，这里有。"
    if bangok_anoney_xemera2_lick_slit:
        Em laugh b "不过，鉴于你对我解剖结构的口头探索，我认为我们现在已经过了那个阶段。"

    m "我看了一眼柜子的内容。有一瓶润滑剂和一些小号的避孕套。在后角塞满了看起来像是大龙用的避孕套。"

    if bangok_four_playerhasdick == True:
        menu:
            "使用保护措施":
                m "我打开一个小号的避孕套包裹，把它套在我的阴茎上。"
                play sound "fx/unwrap.ogg"
                $ bangok_anoney_xemera2_protection_dick = True

            "不使用保护措施。":
                $ bangok_anoney_xemera2_protection_dick = False
    else:
        m "我看到她提到的用于自我愉悦的棒子在下层架子上。"
        c "（也许我以后可以尝试用那个...）"

    if (chap2storehealth == False) and (bangok_anoney_xemera2_lick_slit == True):
        menu:
            "看到后面的巨型避孕套让我想起了一些我之前想过的事情。":
                    $ bangok_anoney_xemera2_clean_arms = True
                    m "我记得在杂货店看到那些大龙避孕套的大小，意识到事情可能会变得混乱，我从柜子的后面拿出了两个大号避孕套并把它们套在我的手臂上。它们部分有肋骨结构，可以给艾梅拉带来更多的愉悦。"
                    play sound "fx/unwrap.ogg"

            "只拿润滑剂":
                pass

    if persistent.bangok_four_playerhasdick and (not bangok_anoney_xemera2_protection_dick) and (not bangok_anoney_xemera2_clean_arms):
        m "忽略避孕套，我拿起润滑剂，回到艾梅拉面前跪在她张开的腿前。"
    else:
        m "拿起润滑剂，我回到艾梅拉面前，跪在她张开的腿前。"

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emera_presenting at Pan((960, 250), (960, 500), 4.0)

    if persistent.bangok_cloacas == True:
        m "用拇指和手指把她的裂缝撑开，我把一些润滑剂挤进她的洞里。她发出咕噜声，全身颤抖，感受到凉爽的润滑剂进入她的入口，但它很快便温暖起来，适应她的体温。"
    else:
        m "用拇指和手指把她的上裂缝撑开，我把一些润滑剂挤进她的洞里。她发出咕噜声，全身颤抖，感受到凉爽的润滑剂进入她的入口，但它很快便温暖起来，适应她的体温。"

    m "为了确保万无一失，我也在手上挤了一些润滑剂，然后开始在手和手臂上涂抹。"

    if bangok_anoney_xemera2_clean_arms == True:
        Em laugh b "哦，我差点忘了那些还在里面。"
        Em ques b "你真有创意，迫不及待想感受那些肋骨的触感。"
        Em laugh b "现在把那只手臂放进来吧。"
    else:
        Em laugh b "好吧，看起来你已经准备好了。现在把那只手臂放进来吧。"

    m "把拇指折进手心，把手指合拢，我轻轻推入她已经涂满润滑剂的裂缝。"

    if persistent.c4eggs == True:
        m "我在拉扎的藏身处见过一些龙蛋，虽然我没直接看到她自己的蛋，但我觉得她的蛋应该比我的手大。"
    else:
        m "我没见过龙蛋，但我觉得她的蛋应该比我的手大。"
    
    m "艾梅拉在我手进入她体内时发出一声咆哮。{w=0.5}{nw}"
    play sound "fx/varagrowl.ogg"
    m "艾梅拉在我手进入她体内时发出一声咆哮。{fast} 由于体型差异，她轻松地接纳了我的整个手。"
    
    if persistent.bangok_watersports == True:
        m "就在她入口的上墙壁，我感觉到一个开口，猜想那是她的尿道。我记下了它的位置，以便以后探索，如果我们都愿意的话。"

    m "我继续把手臂推入她体内，轻轻摇动着。"
    play sound "fx/mud.ogg"
    m "她的兴奋提供了充足的润滑，加上我之前在手臂上涂的润滑剂。"
    m "我决定把手指握成拳头，模仿龙的阴茎头部。{w=0.1}{nw}"
    play sound "fx/purr.ogg"
    m "我决定把手指握成拳头，模仿龙的阴茎头部。{fast} 艾梅拉立刻发出咕噜声，全身颤抖，感受到极大的愉悦。"

    if bangok_anoney_xemera2_clean_arms == True:
        m "我的手臂慢慢消失到肘部，隧道还很长。现在肋骨结构的避孕套开始进入她体内。"
        Em laugh b "那感觉太好了。比尝试把一个静止的工具推入要好得多，而且避孕套的肋骨纹理感觉很神奇。"
    else:
        m "我的手臂慢慢消失到肘部，隧道还很长。"
        Em laugh b "那感觉太好了。比尝试把一个静止的工具推入要好得多。"

    if persistent.bangok_cervpen == True:
        m "仅再过一分钟的慢慢推送，我终于到达了她隧道的尽头，超出了其后是她的卵室。"
    else:
        m "仅再过一分钟的慢慢推送，我终于到达了她隧道的尽头，我的手臂大部分都在她体内。"
        Em frown b "嗯，那是你能走到最深的地方了。"

    m "现在我知道有多少长度可以工作了，开始慢慢从她的隧道中撤出我的浸透的手臂。当大部分手臂都出来时，我再次推入，设定一个节奏。"
    play soundloop "fx/massage.ogg"

    $ renpy.pause (3.0)

    if bangok_four_xipsum.unplayed == False:
        if bangok_four_xipsum.vag_and_ass == True:
            c "我知道你的文化研究的一部分也包括龙的交配仪式。我有机会和一个有两根阴茎的龙有过接触。交配时它们都同时使用，每个进入一个孔吗？"
            Em frown b "你真的需要现在知道答案吗？"
            Em ques b "为了满足你的好奇心；虽然遇到这样异常的龙是很不寻常的。"
        else:
            c "我有过和一个有两根阴茎的龙的接触，同时充满了两个通道。那是一次天堂般的体验。"
            Em ques b "确实吗？遇到这样异常的龙是很不寻常的。"
        Em ques b "不过，有记录显示它们确实使用了两个通道进入雌性，双方都感到非常愉悦。"
        c "你觉得体验一下记录中的那种感觉怎么样？"
        Em bangok blush b "你能做到吗？"
        menu:
            "让我施展我的魔法。":
                stop soundloop fadeout 0.5
                jump bangok_anoney_xemera2_double_fisting
                "On second thought, maybe it is best to carry on as planned.":
                jump bangok_anoney_xemera2_vaginal_only
    else:
        jump bangok_anoney_xemera2_vaginal_only

label bangok_anoney_xemera2_vaginal_only:
    if persistent.bangok_cervpen == True:
        m "Reforming my hand into a point again, I began to put pressure at the end of my stokes onto the centre of the rear wall of her tunnel"
        Em bangok blush b "You need to go faster. Faster and harder. Put your body into it."
        stop soundloop fadeout 0.5
        play soundloop "fx/massage2.ogg" fadein 0.5
        m "Gradually I could feel the barrier yielding and a hole starting to open up."
        Em "Don't stop now, [player_name]. Give it all you got!"
        m "Over the next few minutes the hole widened even more,{w=0.5}{nw}"
        play sound "fx/varagrowl.ogg"
        m "Over the next few minutes the hole widened even more,{fast} until eventually my hand pushed through."
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I broke through into her egg chamber. I could feel the smooth hard surface of her egg held within her inner castle."
        stop soundloop fadeout 0.5
        m "I stopped moving my arm with my hand in her egg chamber, just moving around the egg."
        play sound "fx/breathing.ogg"
        $ renpy.pause (5.0)
        m "Emera panted needily."
        Em "Why did you stop?"
        m "I smoothly withdrew my arm until my fist was at her entrance and punched it through her tunnel back into her egg chamber."
        play soundloop "fx/massage2.ogg"
        Em "More, More!"
        m "I quickly picked up the pace, pushing my arm deep each time, touching the egg with my knuckles."
        $ renpy.pause(3.5)
        Em bangok orgasm b "I am almost there just need a few more fast strokes and..."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{w=0.8}{nw}"
        play sound "fx/bitescr.ogg"
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{fast} I felt her tunnel tense up with pulsing waves travelling down to her egg chamber. The barrier once there had disappeared; the entrance had dilated completely."
        $ renpy.pause(0.8)
    else:
        m "I began to move my fist around inside her, stimulating her walls around the entrance to her egg chamber"
        Em bangok blush b "You need to go faster. Faster and harder, put your body into it."
        stop soundloop fadeout 0.5
        play soundloop "fx/massage2.ogg" fadein 0.5
        m "Over the next few minutes, her tunnel gradually got looser."
        Em "Don't stop now, [player_name]. Give it all you got!"
        play sound "fx/varagrowl.ogg"
        m "I could speed up my thrusts, making sure to move my wrist each time I kissed the entrance to her egg chamber with my knuckles."
        play sound "fx/breathing.ogg"
        $ renpy.pause (5.0)
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I found a particularly sensitive area near the end of her tunnel. I angled my hand so that I would continually rub this area each time I plunged my arm back in"
        $ renpy.pause(0.5)
        Em bangok orgasm b "I am almost there just need a few more fast strokes and..."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{w=0.8}{nw}"
        play sound "fx/bitescr.ogg"
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{fast} I felt her tunnel tense up with pulsing waves travelling down to her egg chamber. The barrier that until a few moments ago was at the end of her tunnel rapidly disappeared, the entrance dilating completely."
        $ renpy.pause(0.8)
        
    m "Her tunnel clenched so tight around my arm that I could no longer move it,{w=0.8}{nw}"
    play sound "fx/spray.ogg"
    m "Her tunnel clenched so tight around my arm that I could no longer move it,{fast} her opening spraying copious amounts of lubrication all over my lower body."

    if persistent.bangok_watersports == True:
        m "I suddenly felt a much warmer and wetter fluid surrounding my arm. Given the position Emera was standing, I was glad that it was moving further inside her instead of streaming out onto the floor and embarrassing her."
        m "She didn't mention that the laying hormones also made her lose control of her bladder, though it could be an evolutionary trait to provide more lubrication for the egg."
        m "I was equally glad I had removed my clothing and now appreciated why she performed this on an easy-to-clean mat."

    else:
        m "I am glad that I had removed my clothing and now appreciated why she performed this on an easy-to-clean mat."

    m "After what felt like several minutes I felt her tunnel relaxing. Though I could still feel pulses along the sides of her tunnel, now they were going in the opposite direction."
    m "Emera was breathing heavily as she spoke to me again."
    Em bangok blush b "Thank you for that. You have done it. My egg is now going to be starting its journey out of me, and for the first time I can enjoy it."
    Em "You have already done so much for me by getting this far, but I would ask you to do more."
    Em "The hormones that are released to prepare to lay the egg severely limit any discomfort I would experience from the egg passing out."
    Em "There is something that I have always wanted to try after reading about it in our records, but have not been able to do, because of my lack of a partner or flexible enough tail."
    Em "When the egg is travelling down my tunnel, are you able to stop it before it comes out and push it back?"
    c "If that is what you want."
    m "I pulled my arm back until just my hand remained inside and I could see the muscles around her groin area working to push the egg down her tunnel."
    m "The look of rapture on the dragon's face confirmed that she was as high as a stunt-performing flyer."
    m "After a few moments I could feel the smooth oval end of her egg that was pressing on my fingers at the entrance to her vagina.{w=0.8}{nw}"
    play sound "fx/mud.ogg"
    m "After a few moments I could feel the smooth oval end of her egg that was pressing on my fingers at the entrance to her vagina.{fast} I held the egg for a moment whilst her contractions passed, then I drove my arm back into her slick canal."
    if persistent.bangok_cervpen == True:
        m "The copious lubrication meant it was easy to push the egg back in. I pushed it back, deep inside her, until I could feel my hand slipping it through the still-dilated entrance to her egg chamber."
    else:
        m "The copious lubrication meant it was easy to push the egg back in. I even went further  than before given the entrance to her egg chamber was still dilated."
    m "It didn't appear to cause her any discomfort.{w=0.8}{nw}"
    play sound "fx/bitescr.ogg"
    m "It didn't appear to cause her any discomfort.{fast} In fact, there was another muffled roar as another set of bite marks were added to the same cushion used before."
    m "I could feel her tunnel spasm around my arm, almost in confusion as the instinct to draw the male fluids to the egg chamber was competing with the signals from her egg chamber that is currently occupied in trying to evict the egg."
    m "Some moments later, her tunnel again went limp and I moved my hand back to the beginning to prepare to go again."
    m "I repeated the operation five more times before my arm was starting to get tired. I removed it from her and finally allowed her body to expel her egg."
    $ renpy.pause (2.5)
    m "I caught the egg in my hands as it fell from her slit.{w=0.8}{nw}"
    play sound "fx/slurp.ogg"
    $ renpy.pause(0.8)
    play sound "fx/bitescr.ogg"
    m "I caught the egg in my hands as it fell from her slit.{fast} I was surprised by its weight and size: about as large as a melon. The color was a pale yellow, nearly matching her belly."
    $ renpy.pause(0.8)
    play sound "fx/breathing.ogg"
    m "Emera panted heavily, her body still in the throes of her orgasms."
    Em bangok orgasm b "That was amazing. Those old records were not wrong when they recorded their observations."
    jump bangok_anoney_xemera2_what_will_you_do

label bangok_anoney_xemera2_what_will_you_do:
    c "What will you do with the egg now?"
    Em ques b "Usually I donate it to a charity in the city. They have an anonymous drop off box here at the library."
    Em "They extract the contents of the egg, fill it with a dense foam then paint designs on the shell, with the eggs then sold as souvenirs, presents and the like."
    Em normal b "The profits gained are then shared with orphanages and counseling for low income families all over."
    Em frown b "The level of pleasure that is had by both partners from encouraging the beginning of the cycle can fuel an addiction."
    Em "The consequences of which are seen in the large range of contraceptives. You must have seen them at the local grocery store. This is also unfortunately evident in the unwanted fertilized eggs that are sometimes also left in the donation box."
    c "Really?"
    Em normal b "Of course any eggs left in the box at the end of the day are checked by simply shining a light through them. Given the shells are slightly translucent, it is possible to tell if they are viable or not."
    m "I carefully placed the egg down onto the mat before it could slip out my hands."

    menu:
        "I wonder if I can fit both my arms in...":
            pass
        "Ask to be satisfied." if bangok_four_playerhasdick == True:
            jump bangok_anoney_xemera2_satisfy_male
        "Ask to borrow Emera's pleasure stick." if bangok_four_playerhasdick == False:
            jump bangok_anoney_xemera2_satisfy_female
        "Just finish up.":
            jump bangok_anoney_xemera2_toweling_showercomment_conclusion
    c "Emera, there is something new I wish to try. You found the experience of one of my arms inside you was amazing. Now that you have laid your egg, how about both arms?"
    Em laugh b "I am certainly interested enough to try."
    m "I pulled the mat over to a wall, then knelt down against the wall facing her. I bought my arms together, and twined my fingers together."
    c "You will need to do the work, I can't brace against you with both my arms inside."
    m "Emera backed up slowly until my clenched hands were under her tail."
    if persistent.bangok_cloacas == True:
        m "I lined up my arms with her cloaca, which was still swollen and spread from passing the egg."
    else:
        m "I lined up my arms with her vaginal slit, which was still swollen and spread from passing the egg."
    $ renpy.pause (1.5)
    m "Emera leaned back until she forced my hands into her slit."
    Em blush b "Yes, I feel that now.{w=0.8}{nw}."
    play sound "fx/varagrowl.ogg"
    Em blush b "Yes, I feel that now.{fast} Both your arms together will be larger than any dragon cock."
    m "Emera continued to lean back, pushing more and more of my arms into her."
    play sound "fx/mud.ogg"
    Em "Gosh your arms are so big when pressed together like that."
    m "She continued to back up until my elbows had entered her slit."
    m "Emera started to rock her body back and forth,{w=0.8}{nw}"
    play soundloop "fx/massage.ogg"
    m "Emera started to rock her body back and forth,{fast} sliding my arms up and down her tunnel."
    $ renpy.pause (2.5)
    Em "So, so big, it is like the egg yet all the way along."
    m "Now that she had gotten used to my arms inside her she decided to push even harder."
    $ renpy.pause (2.5)
    m "I could feel more of my arms sliding inside,{w=0.8}{nw}"
    play sound "fx/varagrowl.ogg"
    m "I could feel more of my arms sliding inside,{fast} as her slit stretched even wider."
    stop soundloop fadeout 0.5
    play soundloop "fx/massage2.ogg" fadein 0.5
    m "Emera sped up but did not move as far, keeping my forearms within her warmth."
    Em "Almost there...., nearly at the end of my tunnel, just a little further"
    m "I can feel her passage starting to clamp down. Emera really had to put some effort into forcing me through."
    play sound "fx/breathing.ogg"
    $ renpy.pause (7.0)
    m "Finally Emera gave one last shove back and my arms reached the end of her tunnel."
    Em orgasm b "Words... so... full"
    stop soundloop fadeout 0.5
    m "Her tunnel clamped down, hard.{w=0.8}{nw}"
    play sound "fx/roar2.ogg"
    m "Her tunnel clamped down, hard.{fast} As I was trapped between her and a wall, pinned in place, I could do almost nothing but enjoy the sight of the dragon in the throes of the longest orgasm she had ever experienced."
    $ renpy.pause (1.5)
    m "I did what I could, which was to wiggle my arms to prolong her pleasure."
    $ renpy.pause (1.5)
    m "A fresh flood of juices spurted out around my arms, spattering my chest in the fresh, warm liquid."
    play sound "fx/water2.ogg"
    $ renpy.pause (2.5)
    m "Finally, after what felt twice the length of her previous orgasms, her tunnel finally relaxed,{w=0.8}{nw}."
    play sound "fx/rolldownhill.ogg"
    m "Finally, after what felt twice the length of her previous orgasms, her tunnel finally relaxed,{fast} her legs become weak, and she tumbled to the mat on her side, pulling me down too."
    play sound "fx/breathing.ogg"
    m "After minutes of laying on the mat, my arms still trapped within her passage, they were starting to ache."
    c "Emera, could you move forwards so I can pull my arms out?"
    Em blush b "Oh of course. Apologies, I don't know what came over me. The pleasure was just so, so very good and then I just felt so weak, I couldn't continue standing."
    m "She began to move forward, slowly pulling my arms out of her slit, leaving a trail of her juices on the mat beneath them."
    m "She let out a snarl as my hands finally left her now thoroughly abused slit."
    play sound "fx/varagrowl.ogg"
    Em "Words cannot describe how good that felt."

    menu:
        "Ask to be satisfied." if bangok_four_playerhasdick == True:
            jump bangok_anoney_xemera2_satisfy_male
        "Ask to borrow Emera's pleasure stick." if bangok_four_playerhasdick == False:
            jump bangok_anoney_xemera2_satisfy_female
        "Just finish up.":
            jump bangok_anoney_xemera2_toweling_showercomment_conclusion

label bangok_anoney_xemera2_toweling_showercomment_conclusion:
    play sound "fx/cabinet.ogg"
    m "Emera bought some towels out of another cupboard and we proceeded to dry ourselves as best as we could until we could both take showers."
    $ renpy.pause (2.5)
    play sound "fx/rub2.ogg"
    $ renpy.pause (2.5)
    jump bangok_anoney_xemera2_conclusion

label bangok_anoney_xemera2_satisfy_male:

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emeraroom_night

    show emera normal b

    c "Now that I have satisfied you, I wish to take care of myself. Given how large your reproductive passage is, I would like to try your other entrance."
    Em bangok blush b "Of course ambassador. My body is yours to use after what you have done for me. It is quite fair that you should also get some pleasure out of this."

    show emera bangok blush b flip:  #Trying to do something similar to the anna lays down in anna chapter 2, rotate property is only clockwise. not sure how to do counter clockwise.
        xanchor 0.5
        ease 1.0 pos (0.8, 1.0)
    with None
    $ renpy.pause(0.7)
    show emera bangok blush b flip:
        pos (0.2, 1.0)
    with dissolve
    m "I asked Emera to roll over onto her back.{w=0.8}{nw}"
    play sound "fx/leather.ogg"
    m "I asked Emera to roll over onto her back.{fast} Then I got up from the floor and went over to the fruit bowl on one of the cabinets."
    play sound "fx/basket.ogg"
    m "Selecting three firm fruits that were slightly larger than my hand I returned to Emera."
    show emera ques b flip
    m "Emera, on her back, gave me a confused look until I spread apart the large slit that her egg had recently come out of, which was still very wet with the multiple orgasms she'd experienced earlier."
    show emera bangok blush b flip
    m "I started to push the fruits into her tunnel, until all three were in her birthing passage."

    if persistent.bangok_cloacas == True:
        m "Then I lay atop her, reached down to spread apart her cloaca, found the opening to her anal passage, then buried my lubed length within."
    else:
        m "Then I lay atop her, reached down to finding the lower slit leading to her anal passage, then buried my lubed length within."
    
    m "Our lower bodies were covered with the slippery mating fluids from her orgasms, enabling me to slide my body quickly over her scales as I thrust into her anal passage."
    play soundloop "fx/flap1.ogg"
    m "I could feel her mating muscles clamping down on the fruit in her canal, the contractions against which then also slightly contracted her anal passage."
    Em bangok blush b flip "Oh this is new, I have never thought of using food items in this way, or using my other tunnel for such..."
    m "I had been rock hard through the whole egg laying procedure, so I knew that I would not last long."
    m "I continued to thrust into her, the fruits in her tunnel moving around with the motion of my hips."
    play sound "fx/varagrowl.ogg"
    m "The pressure of the fruits against the entryway of her egg chamber caused her to moan in pleasure."
    m "I could feel my orgasm building up. I was not going to last much longer."
    stop soundloop fadeout 0.5
    if bangok_anoney_xemera2_protection_dick == True:
        m "It was only a couple more thrusts until I blew my load, the condom containing my relatively small spurts compared to what a dragon would probably produce."
    else:
        m "It was only a couple more thrusts until I blew my load, my relatively small spurts compared to what a dragon would probably produce still painting the walls of her lower passage."
    m "My last thrust, coupled with the movement from the fruits in her tunnel threw Emera into yet another orgasm.{w=0.8}{nw}"
    show emera bangok orgasm b flip
    $ renpy.pause (1.5)
    play sound "fx/bitescr.ogg"
    $ renpy.pause(0.8)
    m "My last thrust, coupled with the movement from the fruits in her tunnel threw Emera into yet another orgasm.{fast} Her lower passage tightened further around me, milking out of me a few extra spurts."
    m "Once her tunnel loosened up to allow me to pull out I got up from her underside and proceeded to reach into her vaginal passage to remove the fruit."
    show emera bangok blush b flip
    play sound "fx/varagrowl.ogg"
    m "Emera gave a moan each time her lips were stretched by their expulsion."
        
    if bangok_anoney_xemera2_clean_arms == True:

        m "I reached down and quickly removed the condoms from my arms; the rubbers had served their purpose in keeping at least some of me relatively clean."

    if (persistent.bangok_watersports == True) and (bangok_four_playerhasdick == True):

        m "Given that it had been several hours since I had visited a restroom, nature suddenly decided to make its call."
        c "(Oh crap what do I do?)"
        c "(I can't go outside the office to the washroom, not in this state.)"
        c "(The last thing I want to do is accidently leave any evidence of our activities, especially with the heightened smell of the dragons.)"
        menu:
            "Don't think about it, just get cleaned up so you can go to the restroom.":
                pass

            "Relieve yourself inside Emera.":
                jump bangok_anoney_xemera2_ws_relief

    jump bangok_anoney_xemera2_toweling_showercomment_conclusion


label bangok_anoney_xemera2_ws_relief:
    c "Emera, I'm afraid I desperately need to use the restroom. I..."
    Em bangok blush b flip "Oh, I understand. I have had to do the same thing myself after a particularly long session."
    c "No, I mean I need to use the restroom now, and I don't think I should leave your office in this state."
    Em ques b flip "Ah, I see. Well, I am aware some dragons fetishize the practice of relieving themselves in their partner, and I have immunized myself to the thought."
    Em laugh b flip "Experiencing it in practice is another matter, but I am willing to let you do so if you wish."
    if bangok_anoney_xemera2_protection_dick == True:
        m "Looking "
        menu:
            "Urinate unprotected.":
                m "I reached down and quickly removed the condom from my shaft."
                $ bangok_anoney_xemera2_protection_dick = False
            "Urinate in the condom.":
                pass
    label .ws_menu:
    menu:
        "Ass." if not persistent.bangok_cloacas:
            jump .ass
        "Vagina." if not persistent.bangok_cloacas:
            jump .vag
        "Anal vent." if persistent.bangok_cloacas:
            jump .ass
        "Cloaca." if persistent.bangok_cloacas:
            jump .vag
        "Mouth." if bangok_four_xemera2_ws_mouth_unasked:
            $ bangok_four_xemera2_ws_mouth_unasked = False
            c "May I use your mouth?"
            Em frown b flip "While I'm immunized to the thought, I highly doubt I'm immunized to the taste."
            Em ques b flip "I'd prefer if you keep this far from my face."
            jump .ws_menu
        "Urethra.":
            jump .urethra

    label .ass:
        c "May I use your ass?"
        Em ques b flip "If you so desire."
        m "Emera was still laying on her back{w=0.8}{nw}"
        play sound "fx/purr.ogg" 
        if persistent.bangok_cloacas:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly to reinsert my hardening dick into her anal vent."
            m "Emera's cloaca was still spread wide from her earlier activities. I stuck my dick in the mess at her vaginal entrance, evidence from the many orgasms that Emera had." 
            m "Once my dick was thoroughly coated in her juices, I pushed it into her anal vent."

        else:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly to reinsert my hardening dick into her ass"
            m "Emera's vagina was still spread wide from her earlier activities. I stuck my dick in the mess at her vaginal entrance, evidence from the many orgasms that Emera had." 
            m "Once my dick was thoroughly coated in her juices, I reached down to spread her ass and pushed my dick into her hole."
        show emera bangok blush b flip with dissolve
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        if bangok_anoney_xemera2_protection_dick == True:
            m "After adjusting my position to get both of us comfortable, I released my bladder into the reservoir of the condom, inflating it with my urine to mix with my earlier deposit in her rear."
        else:
            m "After adjusting my position to get both of us comfortable, I released my bladder into her rear, spraying away my cum with warm urine."
        $ renpy.pause (0.5)
        Em laugh b flip "Mmm. That feels... warm. Certainly far from unpleasant."
        stop soundloop fadeout 2.0
        if bangok_anoney_xemera2_protection_dick == True:
            m "When I was done, I slowly slid my penis free of the condom, leaving its overfilled reservoir within her rear, clenched shut by her anal sphincter."
        else:
            play sound "fx/uncork.ogg"
            m "When I was done, I quickly pulled out."
        stop soundloop fadeout 2.0
        jump .done

    label .vag:
        if persistent.bangok_cloacas:
            c "May I use your vagina?"
        else:
            c "May I use your cloaca?"
        show emera laugh b flip with dissolve
        m "Emera's expression changed to one both flustered and curious."
        Em bangok blush b "Well... I suppose. If you so desire."

        m "Emera was still laying on her back{w=0.8}{nw}"
        play sound "fx/purr.ogg" 
        if persistent.bangok_cloacas == True:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly to reinsert my hardening dick into her cloaca."
            m "Emera's cloaca was still spread wide from her earlier activities. I stuck my dick in the mess at her vaginal entrance, evidence from the many orgasms that Emera had, and pushed inwards." 
        else:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly, and this time stuck my dick insie her vagina."
            m "Emera's vagina was still spread wide from her earlier activities. I stuck my dick in the mess at her entrance, evidence from the many orgasms that Emera had, and pushed inwards."
        show emera bangok blush b flip with dissolve
        play soundloop "fx/faucet1.ogg" fadein 2.0
        queue soundloop "fx/faucet2.ogg"
        if bangok_anoney_xemera2_protection_dick == True:
            m "After adjusting my position to get both of us comfortable, I released my bladder into the reservoir of the condom, filling it with my urine in the soft, warm confines of her canal."
        else:
            m "After adjusting my position to get both of us comfortable, I released my bladder into her vagina, spraying away my cum within her body."
        $ renpy.pause (0.5)
        Em laugh b flip "That is a... unique feeling. Warm and rather pleasurable."
        stop soundloop fadeout 2.0
        if bangok_anoney_xemera2_protection_dick == True:
            m "When I was done, I slowly slid my penis free of the condom, leaving its reservoir filled with warm urine within her vagina."
        else:
            m "When I was done, I held my position for a few moments, savoring the feeling of Emera's insides' wet embrace."
            m "Then I slowly pulled out, wiping my tip on her outer lips to clean myself off as best as possible given our circumstances."
        jump .done


    label .urethra:
        m "Remembering the discovery of where Emera's urethra was, I hoped that her hormones would still prevent any discomfort as came up with my idea."
        c "Maybe... since you're so much larger than I am, I could urinate into your bladder?"
        Em laugh b flip "Why... I have never heard of such a thing."
        Em bangok blush b flip "I cannot say I am displeased with the idea... I am curious to see how it would feel."
        Em ques b flip "Proceed."
        m "Emera was still laying on her back{w=0.8}{nw}"
        play sound "fx/purr.ogg" 
        if persistent.bangok_cloacas == True:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly to reinsert my hardening dick into her cloaca."
            m "Emera's cloaca was still spread wide from her earlier activities. Reaching back I spread her slit easily and found her urethra exactly where I had remembered it."
        else:
            m "Emera was still laying on her back{fast} and gave a purr as I got back on to rest on her belly to reinsert my hardening dick into her vagina."
            m "Emera's vagina was still spread wide from her earlier activities. Reaching back I spread her slit easily and found her urethra exactly where I had remembered it."
        show emera ques b flip
        if bangok_anoney_xemera2_protection_dick == True:
            m "Emera had a bemused look on her face as I reached down with my other hand and pushed my condom-wrapped dick into her urethra."
        else:
            m "Emera had a bemused look on her face as I reached down with my other hand and pushed my dick into her urethra."
        m "I was dreading her reaction in case she faced too much discomfort, however after waiting a few moments without her expressing being in pain I felt relieved that her hormones must still be working."
        Em normal b flip "That feels... odd. I have never come across records that have shown that place to be penetrated, however given the larger size of dragons and not wanting to cause pain to a mate it is obvious why."
        c "It doesn't hurt?"
        Em bangok blush b flip "No. As I said it just feels odd. I would not like to be mated down there; even Earth dragons are not completely resistant in areas not expected to be mated. However I do want you to continue."
        m "I continued to press further in, the lube from her vagina helping to quicken the journey."
        m "I came to her sphincter seperating the entrance to her bladder. I gently put pressure until the head of my dick pushed through."
        show emera normal b flip
        $ renpy.pause (0.5)
        show emera frown b flip with dissolve
        m "Emera let out a gasp. I could tell from her face this was at least mildly uncomfortable for her."
        play soundloop "fx/faucet1.ogg" fadein 1.0
        queue soundloop "fx/faucet2.ogg"
        if bangok_anoney_xemera2_protection_dick == True:
            m "I quickly released my bladder into the reservoir of the condom, inflating it within her bladder, rushing to finish my business."
        else:
            m "I quickly released my own bladder inside her, rushing to finish my business."
        $ renpy.pause (1.5)
        stop soundloop fadeout 2.0

        if bangok_anoney_xemera2_protection_dick == True:
            m "When I was done, I quickly began to slide my penis free of the condom, leaving its overfilled reservoir within her bladder, clenched shut by her muscles."
        else:
            play sound "fx/uncork.ogg"
            m "When I was done, I quickly pulled out."
        show emera normal b flip with dissolve
        jump .done

    label .done:
        $ renpy.pause (0.5)
        show emera laugh b flip with dissolve
        m "I felt her rest one of her front paws pat me on my shoulder and I just laid a while, enjoying the warmth of her body heat."
        Em normal b flip "If everything is done, then we ought to clean up. It is already very late and you will probably be wanting to return to your apartment."
        play sound "fx/cabinet.ogg"
        $ renpy.pause (0.5)
        play sound "fx/rub2.ogg"
        m "Emera bought some towels out of another cupboard and we proceeded to dry ourselves as best as we could until showering."
        jump bangok_anoney_xemera2_conclusion
    

label bangok_anoney_xemera2_satisfy_female:
    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emeraroom_night

    $ renpy.pause (3.3)

    show emera normal b

    if bangok_anoney_xemera2_clean_arms == True:
        m "I reached down and quickly removed the condoms from my arms, the rubbers had served their purpose in keeping my arms clean."

    c "Emera, now that you are satisfied, would I be able to borrow your pleasure stick to help satisfy my own needs?"
    Em bangok blush b "Of course. Though are you sure you would be able to take it?"

    if bangok_four_malepartners > 1:
        c "As I have said, I have had other encounters with male dragons and have been able to take them. A dildo of the same size will be manageable."

    else:
        c "I used to have 'toys' for my own pleasure back in the human world. I had quite a nice collection of what I believe to be draconic size with which to state my desires when wanting to get a little rough."

    m "I went to the cupboard {w=0.8}{nw}."
    play sound "fx/cabinet.ogg"
    m "I went to the cupboard.{fast} And retrieved the dildo from the lower shelf."
    m "Examining the dildo, I found it was made out of a hard rubber and nearly the length of my arm, with a rounded tip. The head bulged out slightly about the size of my fist."
    m "The rest of the shaft, starting out at the base, was the thickness of my bicep decreasing to the diameter of my wrist just below the head. There was a length of wood sticking out of the base, evidently to make it easier to hold when in use."

    show emera normal b flip:  #Trying to do something similar to the anna lays down in anna chapter 2, probably got this wrong.
        xanchor 0.5
        ease 1.0 pos (0.8, 1.0)
    with None
    $ renpy.pause(0.7)
    show emera normal b flip:
        pos (0.2, 1.0)
    with dissolve
    play sound "fx/leather.ogg"
    m "Emera had rolled onto her back"
    Em laugh b flip "Come over here and lay on me whilst you have your fun."
    m "I sat on her lower belly and bent forwards to her groin."
    m "I pressed the dildo to Emera's vagina and pushed it in.{w=0.8}{nw}"
    play sound "fx/mud.ogg"
    m "I pressed the dildo to Emera's vagina and pushed it in.{fast} It slid in easily due to her tunnel being lubricated and still stretched from passing the egg."
    m "I then pulled the stick out of her, ensuring it was thoroughly coated in her fluids before placing the tip at my entrance and gently easing it in."
    m "I let out a low moan as I could feel the head stretch my outer lips."
    m "I continued to push it in slowly until the thickest part was inside, then all it took was a light clench to pull the rest of the head inside."
    c "Yes, I was ready for this..."
    m "It was amazing to feel this full, and it was only the head."
    m "I continued to gently push it in further. After about half of the way down I felt the head of the toy kiss my cervix."

    if persistent.bangok_cervpen == True:
        m "Knowing that I could take it further I continued to put pressure on my cervix, twisting the toy slightly to dilate it."
        m "I could feel my cervix loosening up as I started to lightly thrust the toy a few inches back and forth."
        m "A few moments later and I felt the head pop through and into my womb."

    else:
        m "This is as much as I can take, given the size of the toy."
        m "I started to lightly thrust the toy a few inches back and forth, getting used to the dildo."

    m "Emera put her hand on my belly and could feel the progress of the toy inside me."
    Em bangok blush b flip "I am impressed, it seems you have indeed had experience enough to take it."
    c "Thank you"
    m "Now that my vagina had conformed to the dildo safely I laid fully on my back on Emera."
    play soundloop "fx/massage.ogg"
    m "The dragon continued to rub her hand over my belly, feeling the toy through my body."
    play sound ["fx/rub1.ogg", "fx/wipe.ogg", "fx/rub1.ogg", "fx/wipe.ogg", "fx/rub1.ogg"]
    $ renpy.pause (5.5)
    stop soundloop fadeout 0.5
    m "After what felt like an age, but was probably only about five minutes my orgasm washed over me, I went limp as my body was consumed by euphoria."
    m "I decided to just lay there for a while, toy still hanging out of my vagina and bask in the afterglow on the warm belly of Emera."
    Em "If everything is done, then we ought to clean up. It is already very late and you will probably be wanting to back to your apartment"
    if persistent.bangok_cervpen == True:
        m "I gave a nod and reached down to gently tug the toy out of me, giving a shudder of pleasure as the head of the toy first left my womb, then stretched my lips."
    else:
        m "I gave a nod and reached down to gently tug the toy out of me, giving a shudder of pleasure as the head of the toy stretched my lips."
    play sound "fx/uncork.ogg"
    m "Emera took her toy off of me and stuck it in her mouth, licking it clean. afterwards she gave it back to me and I put it back into the cupboard"
    play sound "fx/cabinet.ogg"
    m "Emera bought some towels out of another cupboard and we proceeded to dry ourselves as best as we could until showering."
    $ renpy.pause (0.5)
    play sound "fx/rub2.ogg"
    jump bangok_anoney_xemera2_conclusion

label bangok_anoney_xemera2_double_fisting:

    if persistent.bangok_cloacas == True:
        m "Spreading her cloaca wide with one hand, I slowly withdrew my arm from her vaginal tunnel until it was out completely. It was coated in a slick mixture of lube and her plentiful arousal."
        m "I moved my arm slightly lower, the target being her anal passage towards the bottom of her slit. Once again I formed my fingers to a point and pushed at her anal entrance."
        m "Now that one arm was in the right place, I pushed my other arm back into her vacated vaginal canal, stretching her cloaca wide around both my arms."
    else:
        m "Spreading her scales around her anus with one hand, I slowly withdrew my arm from her vaginal slit until it was out completely. It was coated in a slick mixture of lube and her plentiful arousal."
        m "I moved my arm slightly lower, the target being her anal passage in her spread lower slit. Once again I formed my fingers to a point and pushed at her anal entrance."
        m "Now that one arm was in the right place, I removed the other from holding open her anal slit and moved it up to push back into her vacated vaginal canal, stretching both entrances wide around my arms."

    m "I started to push both my arms into her.{w=0.1}{nw}"
    play sound "fx/mud.ogg"
    m "I started to push both my arms into her.{fast} There was not much resistance due to the lube."
    c "How does that feel?"
    Em bangok blush b "MMmm! Having both my passages stretched at the same time is not something I had ever thought about before. I did once take my pleasure stick up there, but the feeling in isolation was not as pleasant as from my vagina."
    Em "But having both at once is just adding to the pleasure."
    if bangok_anoney_xemera2_clean_arms == True:
        m "By now my elbows are sinking in and the ribbed texture of the condoms on my arms was entering her."
    else:
        m "By now my elbows are sinking into her."
    play soundloop "fx/massage.ogg" fadein 0.5
    m "I pulled back both my arms and began alternating them in a piston motion pushing one in as the other was pulled almost out."
    m "Gradually I could feel her tunnels loosening,{w=0.1}{nw}"
    play sound "fx/water1.ogg"
    m "Gradually I could feel her tunnels loosening,{fast} her outer lips becoming more relaxed and her arousal flowing in a small trickle, keeping both arms topped up with fresh juices."
    m "By now I was able to push both arms halfway up my biceps into her and in her vagina, I could feel the entrance to her egg chamber once again."
    if persistent.bangok_cervpen == True:
        m "Reforming my hand into a point again, I began to put pressure at the end of my stokes onto the centre of the rear wall of her tunnel"
        Em bangok blush b "You need to go faster. Faster and harder. Put your body into it!"
        stop soundloop fadeout 0.5
        play soundloop "fx/massage2.ogg" fadein 0.5
        m "Gradually I could feel the barrier yielding and a hole starting to open up."
        Em "Don't stop now, [player_name]. Give it all you got!"
        m "Over the next few minutes the hole widened even more{w=0.5}{nw}"
        play sound "fx/varagrowl.ogg"
        m "Over the next few minutes the hole widened even more{fast} until eventually my hand pushed through."
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I broke through into her egg chamber. I could feel the smooth hard surface of her egg held within her inner castle."
        stop soundloop fadeout 0.5
        m "I stopped moving my arm with my hand in her egg chamber, just moving around the egg."
        play sound "fx/breathing.ogg"
        $ renpy.pause (5.0)
        m "Emera panted needily."
        Em "Why did you stop?"
        m "I smoothly withdrew both my arms until my fists were at her entrances, then punched both through her tunnels, with one sinking back into her egg chamber."
        play soundloop "fx/massage2.ogg"
        Em "More, More!"
        m "I quickly picked up the pace, pushing my arms deep each time, touching the egg with my knuckles."
        $ renpy.pause(3.5)
        Em bangok orgasm b "I am almost there... I just need a few more fast strokes and..."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{w=0.8}{nw}"
        play sound "fx/bitescr.ogg"
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{fast} I felt her tunnel tense up with pulsing waves travelling down to her egg chamber. The barrier once there had disappeared; the entrance had dilated completely."
        $ renpy.pause(0.8)
    else:
        m "I began to move my fists around inside her, stimulating her walls around the entrance to her egg chamber and the wall of her colon closer to her reproductive center."
        Em bangok blush b "You need to go faster. Faster and harder. Put your body into it!"
        stop soundloop fadeout 0.5
        play soundloop "fx/massage2.ogg" fadein 0.5
        m "Over the next few minutes, her tunnel gradually got looser."
        Em "Don't stop now, [player_name]. Give it all you got!"
        play sound "fx/varagrowl.ogg"
        m "I could speed up my thrusts, making sure to move my wrist each time I kissed the entrance to her egg chamber with my knuckles."
        play sound "fx/breathing.ogg"
        $ renpy.pause (5.0)
        m "By now Emera was visibly panting and let out a quickly stifled yelp when I found a particularly sensitive area near the end of her tunnel. I angled my hand so that I would continually rub this area each time I plunged both arms back in"
        $ renpy.pause(0.5)
        Em bangok orgasm b "I am almost there just need a few more fast strokes and..."
        stop soundloop fadeout 0.5
        $ renpy.pause (1.5)
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{w=0.8}{nw}"
        play sound "fx/bitescr.ogg"
        m "Emera quickly grabbed a cushion off her chair and bit down to deaden her roar.{fast} I felt her tunnel tense up with pulsing waves travelling down to her egg chamber. The barrier that until a few moments ago was at the end of her tunnel rapidly disappeared, the entrance dilating completely."
        $ renpy.pause(0.8)

    m "Her tunnel clenched so tight around my arms that I could no longer move them,{w=0.8}{nw}"
    play sound "fx/spray.ogg"
    m "Her tunnel clenched so tight around my arms that I could no longer move them,{fast} her vagina spurt copious amounts of lubrication all over my lower body and genitals."

    if persistent.bangok_watersports == True:
        m "I suddenly felt a much warmer and wetter fluid surrounding the arm in her birthing passage. Given the position Emera was standing, I was glad that it was moving further inside her."
        m "She didn't mention that the laying hormones also made her lose control of her bladder, though it could be an evolutionary trait to provide more lubrication for the egg."
        m "I found myself glad I had removed my clothing and now appreciated why she performed this on an easy-to-clean mat."

    else:
        m "I found myself glad that I had removed my clothing and now appreciated why she performed this on an easy to clean mat."

    m "After what felt like minutes I felt her passageways relaxing, though I could still feel pulses along the sides of her birthing tunnel, now going in an outward direction."
    m "Emera was breathing heavily as she spoke to me again."
    Em bangok blush b "Thank you for that. You have done it. My egg is now going to be starting its journey out of me, and for the first time I can enjoy it."
    Em "You have already done so much for me by getting this far, but I would ask you to do more."
    Em "The hormones that are released to prepare to lay the egg severely limit any discomfort I would experience from the egg passing out."
    Em "There is something that I have always wanted to try after reading about it in our records, but have not been able to do, because of my lack of a partner and of a flexible enough tail."
    Em "When the egg is travelling down my tunnel, are you able to stop it before it comes out and push it back?"
    m "I started to pull my arm out of her anal passage When I felt her muscles clamp down hard on my arm."
    Em "Please can you leave it in? I want to see how it feels expeling the egg with my lower passage filled. If I like it in the future, maybe I shall leave my pleasure stick in there whilst I lay my egg."
    c "If that is what you want."
    m "I pulled back my arm that was in her vagina until just my hand remained inside, and I could see and feel the muscles around her groin area working to push the egg down her tunnel."
    m "I could feel those same contractions mirrored in her anal passage as her muscles squeezed my arm."
    m "The look of rapture on the dragon's face confirmed that she was as high as a stunt-performing flyer."
    m "After a few moments I could feel the smooth oval end of her egg that was pressing on my fingers at the entrance to her vagina.{w=0.8}{nw}"
    play sound "fx/mud.ogg"
    m "After a few moments I could feel the smooth oval end of her egg that was pressing on my fingers at the entrance to her vagina.{fast} I held the egg for a moment whilst her contractions passed, then I drove my arm back into her slick canal."
    if persistent.bangok_cervpen == True:
        m "The copious lubrication meant it was easy to push the egg back in. I pushed it back, deep inside her, until I could feel my hand slipping it through the still-dilated entrance to her egg chamber."
    else:
        m "The copious lubrication meant it was easy to push the egg back in. I even went further than before given the entrance to her egg chamber was still dilated."
    m "It didn't appear to cause her any discomfort.{w=0.8}{nw}"
    play sound "fx/bitescr.ogg"
    m "It didn't appear to cause her any discomfort.{fast} In fact, there was another muffled roar as another set of bite marks were added to the same cushion she had abused before."
    m "I could feel her tunnels spasm around my arms, almost in confusion as the instinct to draw the male fluids to the egg chamber was competing with the signals from her egg chamber that is currently occupied and trying to evict the egg."
    m "Some moments later, her tunnels again went limp and I moved my hand back to the beginning of her birthing passage to prepare to go again."
    m "I repeated the operation five more times before my arms were starting to get tired. I removed them from her finally, allowing her body to expel her egg."
    $ renpy.pause (2.5)
    m "I caught the egg in my hands as it fell from her slit.{w=0.8}{nw}"
    play sound "fx/slurp.ogg"
    $ renpy.pause(0.8)
    play sound "fx/bitescr.ogg"
    m "I caught the egg in my hands as it fell from her slit.{fast} I was surprised by its weight and size: about as large as a melon. The color was a pale yellow, nearly matching her belly."
    $ renpy.pause(0.8)
    m "Emera panted heavily as she came down from her high."
    play sound "fx/breathing.ogg"
    Em bangok orgasm b "That was amazing. I had no idea that having something in my lower passage could feel so good. Those old records were not wrong when they recorded their observations."
    jump bangok_anoney_xemera2_what_will_you_do

label bangok_anoney_xemera2_massage_only:
    $ bangok_anoney_xemera2_massage_only = True
    Em normal b "Yes, it is just more comfortable to lay on the mat than the floor, plus allows all around access without having to move once the process is started."
    m "I nodded."
    m "I pushed my upper body up to be able to reach the hard plates on her back and as before used my weight on the muscles beneath."
    Em mean b "Oh, I could just lay like this with you massaging my back forever. Have you perhaps had any more thoughts about becoming my assistant once all this ambassador business wraps up?"
    m "I looked up from digging my palm into her back to answer her question."
    c "I do not think it would be wise to do that, as much as it would be fascinating to learn more of dragon culture, you have said before you wish to start a family."
    c "I can't give you a family, and I would not want to come between you and your future mate, once you have found a suitable suitor."
    m "I moved to her rear, kneading her thighs and rump."
    m "Emera took a deep breath and glanced at the ceiling, analyzing my response no doubt having an internal argument over how to reply."
    m "After a few moments she brings her head back down on the pillow and exhaled with a sigh."
    Em ques b "You are right of course, I am so used to getting what I want, that I do not fully think through the consequences of my needs."
    Em laugh b "Yes, Yes that feels so good, oh how I am going to miss having this performed when you eventually go back through the portal."
    m "All that was left to do is her tail. I started at the top, moving further up closer to her body. This time I could massage areas that had been neglected before as my hands found themselves around the base of her tail."
    m "After finishing the massage, I got up to stretch my legs"
    jump bangok_anoney_xemera2_conclusion

label bangok_anoney_xemera2_conclusion:
    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene bangok_anoney_emeraroom_night
    show emera normal b with dissolve
    $ renpy.pause (3.3)

    if bangok_anoney_xemera2_massage_only == True:
        Em laugh b "Thank you again for your wonderful massage. I feel great and the tension that had been building up is gone."
        Em ques b "I assume you can find your way back to your apartment?"
        c "Yes I can. I am glad to have helped. I do hope that you will chill out a bit more, and think about the outcomes of what you want for yourself."
        Em normal b "I shall try [player_name]."
        c "Goodnight."
        Em "Goodnight."
    elif bangok_anoney_xemera2_refuse_participate == True:
        Em frown b "I am disappointed that you would not help me, however I did still appreciate the massage. I assume you can find your way back to your apartment?"
        m "I nodded in reply."
        c "Goodbye."
        Em normal b "Goodbye."
    else:
        Em bangok blush b "Thank you again for your wonderful massage and for making tonight my best evening in a long time."
        Em laugh b "I feel great. The tension that had been building up is gone and I have been able to live one of my dreams."
        m "Bending down to the floor to pick up her egg, a movement she must be well practiced with by her motions, she held out her front paw, offering it to me."
        Em normal b"As a token of gratitude for providing your exquisite service, please accept my egg as a reminder of this wonderful evening and the time we shared."
        menu:
            "Accept.":
                m "I reached forward with my hands and wrapped them around the egg, carefully taking and hugging it to my chest."
                c "Thank you for this unique gift, I shall make sure to look after it well."
                c "(How would I even go about preserving it without raising questions?)"
                # So, yeah, how _would_ the player not raise a bunch of questions preserving it?
                # c "(I shall have to take it to the lab in order for it to be preserved properly.)"
            "Reject.":
                c "Sorry but I can't accept this gift. If it were to come to notice by either dragons or the humans back home, then I could be in serious trouble as to how I had gotten it."
                m "I saw Emera's head droop as she heard my refusal of her gift."
                Em frown b "Of course. I understand that it could cause trouble going forwards. The negotiations are still ongoing and, as you said, if it is discovered by the humans then it could lead to difficult questions."
                m "Seeing her crestfallen look, I stepped closer and put my hand on her other shoulder."
                c "I wish that times were better and that I could accept your gift, really I do."
        Em ques b "I assume you can find your way back to your apartment?"
        c "Yes I can. I am glad to have helped. I do hope that you will chill out a bit more and think about the outcomes of what you want for yourself."
        Em normal b "I shall try [player_name]."
        c "Goodnight."
        Em "Goodnight."


    stop music fadeout 2.0
    scene black with dissolvemed

    $ renpy.pause (1.0)
    play sound "fx/door/lock.ogg"
    $ renpy.pause (1.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (1.0)
    play sound "fx/door/close2.wav"
 
    scene bangok_anoney_library_corridor_night with dissolvemed

    $ renpy.pause (0.5)

    if (persistent.remy1played == True) and (remystatus == "good") or (remystatus == "neutral"):
        m "As I left Emera's office and walked down the corridor I could see that the light was on Remy's office was on and faint sounds of a computer game could be made out."
        m "I paused briefly outside the door and wondered if he is making progress on that RPG I accidentally broke."
    else:
        m "As I left Emera's office and walked down the corridor I could see that there was a light on in the next office down."
        m "I paused briefly outside the door to read the door plaque:"
        m "{size=+10}Head Archivist{/size}"
        m "I guessed this was probably Remy's office."
    play sound "fx/steps/clean2.wav"
    scene black with dissolvemed

    $ renpy.pause (0.5)
    play sound "fx/door/door_open.wav"
    scene o3
    play music "mx/campfire.ogg" fadein 2.0

    $ renpy.pause (3.3)
    play sound "fx/door/close2.wav"
    m "Soon I had returned home."

    if bangok_anoney_xemera2_refuse_participate == True:
        m "After cooling off during the walk home, I thought maybe I had made the wrong choice in refusing her offer."
        c "(Emera did seem heartbroken when I had refused. If only my head wasn't so much of a mess with the police investigation and the responsibility I feel being an ambassador. What could have happened?)"
        c "(Ah well, it would be extremely irresponsible of me to go back in time for this non-emergency, even if I did know the coordinates to before this evening's events.)"
        c "(Well, time for bed. Hopefully tomorrow will be a better day.)"
    elif bangok_anoney_xemera2_massage_only == True:
        c "(I hadn't thought I would be paying Emera a return visit, but the evening was pleasant enough.)"
        c "(It was nice to get to know her private side and to know that she can confide in me given my unique position as ambassador.)"
        c "(Well, time for bed. Let's see what tomorrow brings.)"
    else:
        c "(I hadn't even thought I would be paying Emera a return visit. Not only did I give her a massage, but I allowed her to experience pleasure she thought she would only be able to dream of.)"
        c "(It was nice to get to know her private side and to know she can confide in me given my unique position as ambassador.)"
        c "(Well, time for bed, Let's see what tomorrow brings.)"
    stop music fadeout 2.0
    scene black with dissolvemed
    call _mod_incc from bangok_anoney_xemera2_mod_incc
    jump _mod_fixjmp
