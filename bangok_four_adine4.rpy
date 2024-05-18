label bangok_four_adine4_shower_sceneselect:
    play music "mx/fireplace.ogg" fadein 2.0
    scene black with dissolve
    $ renpy.pause (0.5)
    play sound "fx/purr.ogg"
    $ renpy.pause (2.0)
    c "那是...你在咕噜吗？"
    show adineshower at Pan ((00,608), (00,608), 0.0) with dissolvemed
    stop sound fadeout 4.0

label bangok_four_adine4_shower_purring:
    stop soundloop fadeout 2.0

    if bangok_four_common.bangnokay.check():
        show adineshower at Pan ((00, 608), (400,0), 10.0) with None
        m "突然间，她的表情变了，她看向肩膀。"
        Ad think "哦，你做好了吗？如果你不想被水溅到，应该退后一步。"
        c "如果我把衣服脱掉，我不介意被弄湿。"
        show adineshower thinkblush at Pan ((400,0), (400,0), 10.0) with dissolve
        Ad giggle "你不必那样做，只要退后一步就好。"
        c "你确定吗？"
        show adineshower annoyedblush at Pan ((400,0), (400,0), 10.0) with dissolve
        Ad annoyed "是的，[player_name]。你在这里是为了帮我洗干净，不是为了让我看到你裸体或什么的。"
        c "哦。"
        $ renpy.end_replay()
        jump bangok_four_adine4_leave_the_shower

    show adineshower blush at Pan ((00, 608), (400,0), 10.0) with None
    m "突然间，她的表情变了，她看向肩膀。她明显脸红了。"
    Ad think "哦，你做好了吗？你应该...呃，脱掉衣服，这样你的衣服就不会弄湿了。"
    $ renpy.pause (0.5)
    m "我花了一会儿才处理她刚刚的请求。然后我明白了。"
    c "等等，这个洗澡是个借口来让我裸体吗？"
    show adineshower thinkblush at Pan((400,0),(400,0),0.0) with dissolve
    Ad giggle "不完全是。我的肩膀受伤了，真的很难自己洗背。"

    menu:
        "我不愿意。":
            $ renpy.pause (0.5)
            show adineshower think at Pan((400,0),(400,0),0.0) with dissolve
            Ad disappoint "哦。"
            c "这和你无关，只是..."
            show adineshower at Pan((400,0),(400,0),0.0) with dissolve
            Ad disappoint "不，不，没事。对不起，啊，试图那样骗你。"
            show adineshower think at Pan((400,0),(400,0),0.0) with dissolve
            Ad think "如果你不想被水溅到，最好退后一步。"
            $ renpy.end_replay()
            jump bangok_four_adine4_leave_the_shower
        "[[脱掉衣服。":
            $ renpy.pause (0.8)
    play sound "fx/undress.ogg"
    scene black with dissolve
    m "她看起来有点紧张，虽然考虑到她的请求，这是可以理解的。"
    if bangok_four_playerhasdick is None:
        menu:
            m "为了安慰她，我开始脱掉衣服，把它们扔到淋浴范围之外，让我的..."
            "...勃起露出来。":
                $ bangok_four_playerhasdick = True
                pass
            "...湿润的洞露出来。":
                $ bangok_four_playerhasdick = False
                play sound "fx/system3.wav"
                scene black with None
                s "糟糕！这个场景目前只有男性玩家内容。"
                s "你想继续这个场景作为男性玩家，还是跳到结尾？"
                menu:
                    "是的，让我以男性玩家的身份查看这个场景。\n（临时的，场景结束后会恢复。）":
                        play sound "fx/system3.wav"
                        s "如你所愿。{cps=2}..{/cps}{w=1.0}{nw}"
                        pass
                    "不，跳到结尾。":
                        play sound "fx/system3.wav"
                        s "如你所愿。{cps=2}..{/cps}{w=1.0}{nw}"
                        stop soundloop fadeout 2.0
                        $ renpy.end_replay()
                        jump bangok_four_adine4_leave_the_shower
    # if bangok_four_playerhasdick == True
    m "为了安慰她，我开始脱掉衣服，把它们扔到淋浴范围之外，让我的勃起在她面前露出来。"
    Ad giggle "哦，哦！帅哥，看起来不错啊！"
    play soundloop "fx/shower.ogg" fadein 1.0
    m "我轻笑着回应她，她按下墙上的一个按钮，淋浴头打开了，温暖的水流覆盖了我们两个。"
    m "水流下来，艾丁动了动，迅速洗掉我擦的所有泡沫。即使她已经洗干净了，我们仍然站在那里，水继续流淌着。"

    menu:
        "我应该离开。":
            Ad think "你确定吗？你看起来有点，啊，兴奋。和我一起洗澡。你知道..."
            menu:
                "我很好，谢谢。":
                    stop soundloop fadeout 2.0
                    $ renpy.pause (0.8)
                    Ad disappoint "哦。"
                    $ renpy.end_replay()
                    jump bangok_four_adine4_leave_the_shower
                "你是说你想做点什么吗？":
                    jump .adine_presents_rear
        "想尝尝我的阴茎吗？":
            jump .oral
        "介意抬起你的屁股吗？":
            jump .adine_presents_rear

label .oral:
    $ bangok_four_femalepartners += 1
    m "艾丁转过身来面对我，显然对我的提议感到满意。"
    Ad think "我希望你不会失望。我从杂志上读过一些关于如何做这件事的建议，但这是我第一次实践。"
    m "我摇了摇头，安慰地揉了揉她的脸颊。"
    c "没问题，我完全相信你会做得很棒，艾丁。"
    m "她俏皮地把我推到地上，然后迅速用她的嘴把我的勃起含住，让她的舌头在其长度上游走。"
    c "那么急切吗？"
    m "她假装愤怒地瞪了我一眼，但保持了沉默，她的大嘴上下移动，带出我嘴里轻轻的喘息和呻吟。"
    m "我能感觉到小滴润滑剂从我的顶端渗出，然后被龙贪婪地舔舐。"
    m "当她用嘴取悦我时，我注意到她的翅膀伸到她的后腿之间，开始急需地摩擦她自己的裂缝。"
    c "对不起忽略了你，艾丁，我以后会补偿你的。"
    m "她哼了一声作为回应，然后开始一连串的呻吟，我的呻吟也很快加入了她的。"
    m "水流在我们周围拍打，把我们俩都浸透了，我接近了高潮。无论她读过的建议似乎都奏效了。"
    m "我伸出一只手轻轻抚摸她的头，让她知道我很享受。"
    m "与此同时，我准备好爆发，艾丁也知道。只是几秒钟的事情。"

    menu:
        "抓住她的头，在她嘴里射精。":
            $ renpy.pause (0.5)
            play sound "fx/extinguish.ogg"
            m "我用双臂环绕龙的头，把它拉下来，我的伴侣发出震惊的喘息声，我的精液充满了她的嘴。"
            m "没有任何抵抗，她吞下了每一波流体，涂抹在她的舌头上。"
            m "在我被舔干净后，艾丁的努力也得到了回报，她在高潮中向墙壁喷射，她的头向后仰起，发出响亮的呻吟。"
        "向后靠，享受它。":
            $ renpy.pause (0.5)
            play sound "fx/extinguish.ogg"
            m "我让自己向后倒下，抬起臀部，射精。就在第一滴射出之前，艾丁把嘴移开，让乳白色的液体涂满她的脸。"
            m "淋浴头的水迅速将其冲洗掉，清洗了我们俩的体液。"
            m "当我完成后，艾丁向后仰起头，在高潮中向墙壁喷射她自己的液体。"

    m "我们俩都喘着气，湿透了，但我们的脸显示出对这次经历的共同享受。"
    c "谢谢，这是我有过的最好的龙口交。"
    Ad giggle "不客气，这是我尝过的最好的阴茎。"
    m "我们一起笑了，在高潮后的愉悦中轻松地调侃。"
    hide adineshower with dissolve
    $ renpy.pause (0.5)
    scene adineapt2 at Pan ((128, 300), (128,300), 0.0) with dissolvemed
    m "我告辞去擦干，离开淋浴找一条毛巾，艾丁则回头继续淋浴。"
    stop soundloop fadeout 2.0
    $ renpy.end_replay()
    jump bangok_four_adine4_when_she_turned_off_the_water_again

label .adine_presents_rear:
    $ bangok_four_femalepartners += 1
    m "艾丁翻了个白眼，但她愉快的笑容显示她只是装模作样。"
    Ad annoyed "好吧，我想我欠你这个，因为我用这种残忍的方式骗你脱光衣服。"
    m "那是一幅壮丽的景象，各种颜色完美地框住了一个渴望被蹂躏的阴部和肛门。"
    m "我快失去时间感了，但几秒钟后，艾丁的声音打破了沉默。"
    Ad think "怎么了？你打算整天盯着还是教我人类是怎么做的？"

    menu:
        "干她的阴道。":
            jump .vaginal
        "用她的肛门。":
            jump .anal

label .vaginal:
    m "我靠近她，迅速插入她，从她胸口发出一声介于呻吟和咕噜之间的声音。那是湿的，不是因为淋浴。"
    Ad giggle "哦，我的，你这么大胆，嗯，把我这样带走。所有人类都是这么野蛮的吗？"
    c "如果你让我们这样做的话。"
    m "对这个回答感到满意，艾丁进一步向前倾，压下她的后臀以抵住我的推力。虽然她的裂缝对我的人类阴茎来说太大，但她似乎很高兴能和我一起做这件事。"
    m "或者，也许我比我自己认为的更大。她的洞穴令人愉快地紧致，她的随意呻吟表明她和我一样享受。"
    c "你比我想象的龙要紧，嗯，给你的体型来说。"
    Ad think "我不经常，啊，做这个。"
    m "无法通过呻吟交谈，我们回到默默享受彼此的陪伴。"
    m "我臀部的稳定推力慢慢占据了我的思绪，我把所有的努力都放在了手中的天使身上。"
    m "当我越来越接近高潮时，我对她臀部的握力越来越紧。我比希望的更快准备好，但淋浴头洗掉了所有的润滑剂，让我们俩都感觉每一次推入更...粘稠。"
    m "至少我不是一个人。艾丁期待地看着我。她也准备好了。"

    menu:
        "在里面射精。":
            $ renpy.pause (0.5)
            play sound "fx/extinguish.ogg"
            m "再几次推力后，我开始把精液注入我面前美丽的鳞片。白色的液体从她的裂缝中流出，我一波一波地填满了她。"
            m "与此同时，艾丁自己也高潮了，她的阴部颤抖着，我的胯部被她的液体浸湿。"
            Ad giggle "我需要这个！"
            m "我没有立即回应，还在把减少的精液注入她。当我终于完全空了，我喘着气回应。"
            c "是的，我也是。你知道你很美吗？"
            m "艾丁咯咯地笑了起来，那是一种昏昏欲睡、疲惫的笑声。"
            Ad giggle "这会是一个有趣的方式，发现人类可以让龙怀孕。"
            m "我也笑了，同样因为努力而筋疲力尽。"
        "拔出来。":
            m "我拔出来，轻轻地撸动我的阴茎。同时，艾丁伸手回去开始用她的爪子自慰。"
            $ renpy.pause (0.5)
            play sound "fx/extinguish.ogg"
            m "几乎一秒钟后我们一起高潮了，我的腹部被她的液体浸透，而绳绳的精液射向她的臀部。"
            m "这些液体迅速被水冲洗掉，像什么都没发生过一样流向下水道。然而，我和艾丁都喘着粗气，显示出我并没有幻想整个互动。"
            Ad disappoint "我本来希望你能在里面完成的。"
            c "抱歉，旧习惯。这在人类世界中是粗鲁且无效的避孕手段。"
            Ad normal "不过，这很有趣。我们需要再做一次。"
            c "也许下次我们可以试试另一个洞。"
            m "艾丁静静地思考着这个主意，慢慢恢复镇定，就像她之前那样疯狂地叫喊一样。"

    m "在我恢复镇定后，我离开了淋浴，确保给艾丁一个挑逗的拍打，她回应用尾巴拍了我的后背。"
    m "我找到了一条龙大小的毛巾，擦干后，收拾好衣服穿上。"
    c "再次感谢你的乐趣，这是我有过的最好的。"
    Ad giggle "应该是我谢谢你，我很久没有这么好的高潮了。"

    hide adineshower with dissolve
    $ renpy.pause (0.5)
    scene adineapt2 at Pan ((128, 300), (128,300), 0.0) with dissolvemed
    m "我回到客厅，等待艾丁完成她的事情。结果没花多久时间。"
    stop soundloop fadeout 2.0
    $ renpy.end_replay()
    jump bangok_four_adine4_when_she_turned_off_the_water_again

label .anal:
    m "我向前走，双手抓住她的臀部，欣赏她光滑湿润的鳞片的感觉。过了一会儿，我的阴茎靠近她的肛门。"
    Ad think "等等，那不是--"
    m "我猛地插入她，从她口中发出一声混乱的呻吟。它很紧，挤压着我的阴茎，我开始像活塞一样进出。"
    Ad giggle "哦哦，没关系，继续。"
    c "你还是很享受，是吗？"
    Ad annoyed "闭嘴，继续干吧，大男孩。"
    m "我轻拍了她的臀部几下，默默地按照她说的做。我的推力慢慢加快，随着快感侵蚀我的思维过程，变得更有力。"
    m "我进去时就知道这是正确的洞穴。考虑到她的体型，我本以为她的阴道会感觉松弛。但这种感觉让我重新考虑了。"
    m "她用它挤压我的阴茎，给我比我准备的更多的快感。最终我只是环抱住她，像怪物对猎物一样疯狂。"
    m "艾丁也很喜欢它。我偶尔能感觉到她的爪子刷过我的腿，因为她伸手回去疯狂地自慰。"
    m "不久后，我们都准备好高潮，渴望享受高潮的幸福。"

    menu:
        "在里面射精。":
            $ renpy.pause (0.5)
            play sound "fx/extinguish.ogg"
            m "再几次推力后，我发现自己把精液注入她的屁股，然后很快艾丁也高潮了，她的液体涂在我的腿上。"
            m "我们都喘着气，疲惫不堪，花了比我们注意到的更多的能量。几次喷射后，我终于把精液完全注入了她体内。"
            m "享受这个感觉了一会儿，我最终拔出来，坐在地板上，欣赏这美景。"
        "拔出来。":
            $ renpy.pause (0.5)
            play sound "fx/extinguish.ogg"
            m "我在高潮之前拔出了我的阴茎，开始撸动它，精液绳绳地射在她的屁股上，同时艾丁也达到了高潮，她的液体喷在我的腿上。"
            m "所有这些液体很快被淋浴水冲洗掉，我们俩都喘着粗气。"
            m "我最终向后倒下，坐在地板上恢复体力，水流舒缓地冲刷着我们。"
    Ad think "哈，这比我预想的要好。"
    c "什么，你以前没做过这个吗？"
    Ad think "没有。我以为会很疼，所以一直避开。"
    c "嗯，幸好我比龙小，是吧？"
    Ad giggle "你知道的，大小不是问题！"
    m "我站起来，轻轻吻了艾丁的嘴。她有点惊讶，但很快接受了，回应了这个吻，直到我退开。"
    c "谢谢你的愉快时光。我去快点擦干，好吗？"
    Ad normal "去吧，我得再洗一次。这次不洗后背了！"

    hide adineshower with dissolve
    $ renpy.pause (0.5)
    scene adineapt2 at Pan ((128, 300), (128,300), 0.0) with dissolvemed
    m "我找到了最小的毛巾，虽然对我来说还是个毯子，擦干自己，然后站在一边等艾丁完成洗澡。"
    stop soundloop fadeout 2.0
    $ renpy.end_replay()
    jump bangok_four_adine4_when_she_turned_off_the_water_again