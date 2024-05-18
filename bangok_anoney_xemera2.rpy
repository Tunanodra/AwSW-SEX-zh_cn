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