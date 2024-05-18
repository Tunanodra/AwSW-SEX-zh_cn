init python in bangok_four_remy4_store:
    # 路径：
    # 舌头
    path = None

    protection = False

label bangok_four_remy4_more:
    menu:
        "问他是否想继续。":
            pass
        "说点别的。":
            $ renpy.pause (0.5)
            jump bangok_four_remy4_more_return
    c "这...就这样结束了吗？"
    Ry shy b "你是什么意思？"
    c "你想继续吗？"
    Ry shy b "我..."
    m "在他思考的过程中，我分不清自己听到的是我的心跳还是他的心跳。"
    $ renpy.pause (0.8)
    show remyrom at Pan((350, 326), (350, 320), 2.0) with fade
    $ renpy.pause (1.0)
    m "然后他倾身再次亲吻我。"
    show black with dissolvemed
    $ renpy.pause (0.5)
    m "他比上次靠得更近，把我稍微压向了沙发的扶手，但仍然有所保留，犹豫不决。"
    $ renpy.pause (0.5)
    hide black
    hide remyrom
    with dissolveslow
    $ renpy.pause (0.5)
    m "然后他退开了。"
    Ry shy b "对不起... 自从我遇到你以后，我还没想过会发生这样的事..."
    show remy look b with dissolve
    m "他看了看他的领带，然后摇了摇头。"
    Ry normal b "不，我在这里，而且如果我因为想继续活在过去而推开你，那是自私的。"
    c "如果你需要时间，我不介意等待。"
    Ry smile b "你为了让我开心，真是费了不少心思，是吧？"
    c "只要能让你感到舒服，我就愿意做。"
    Ry normal b "没关系的。我也想要这样。我想要... 我们。"
    menu:
        "接受。":
            pass
        "给他一些空间。":
            m "我叹了口气，试图放下自己的期望和激动感，把雷米的心理健康放在首位。"
            c "雷米... 如果你现在不觉得舒服，我理解。没关系..."
            show remy look b with dissolve
            m "他看着我，眼中浮现出新生的失望和担忧。"
            c "不，不是因为这个... 也许有一点，但主要是我不想急于进入这种关系而伤害你。"
            c "我在我们接吻后要求更多，我推得太远了。对不起。"
            $ renpy.pause (0.8)
            Ry shy b "没关系。你根本没有推我。我只是... 也许我还没有我想象中的那么准备好。"
            c "暂停一下今天的事，好吗？"
            Ry smile b "听起来是个好主意。"
            c "当然。"
            jump bangok_four_remy4_canon_shouldprobablygo
        "拒绝。":
            stop music fadeout 2.0
            m "我咬紧牙关，对他再次提起他已故的女友感到沮丧，即使我们今天的目的是帮助他从她的阴影中走出来。"
            Ry shy b "[player_name]？"
            c "我不知道我能不能继续这样下去。你还在紧紧抓住她的记忆。"
            Ry sad b "事情没那么简单..."
            m "我站起来，声音里充满了沮丧和失望。"
            c "也许我们现在就停止吧。我喜欢你，但我不想成为一个替代品，去取代一个已经不在这里的人。刚才吻我时你是不是在想她？"
            $ remystatus = "bad"
            Ry sad b "[player_name]... 拜托。"
            hide remy with dissolve
            m "我转身离开他，无法直视他眼中的痛苦。"
            c "给我一点空间。等你真正放下她的记忆，专注于我们时再回来找我。"
            play sound "fx/undress.ogg"
            m "我听到他系上领带，尽管我请求他不要这样，然后他走向门口，停了一下才说话。"
            show remy sad b with dissolve
            Ry "... 烟火呢？"
            c "等你走出这个情绪再打电话给我。"
            hide remy with dissolve
            $ renpy.pause (0.5)
            play sound "fx/door/doorclose3.ogg"
            m "在他离开后，我关上门，然后瘫倒在地，终于让情绪彻底爆发出来。"
            $ renpy.pause (2.0)
            $ remystatus = "bad"
            $ remyscenesfinished = 4
            jump _mod_fixjmp


    play sound "fx/kiss.wav"
    show remy shy b with dissolve
    m "这次是我主动，抱着他的脖子，在他的鼻尖上吻了一下，让他脸上泛起可爱的红晕，甚至耳朵也红了。"
    Ry "我... 我不知道你打算走多远。作为一条龙，我比你大一些..."
    c "我们会找到办法的。"
    Ry smile b "好吧，如果这是你想要的，让我们先试点简单的。"
    Ry normal b "我不确定在你穿着衣服的情况下能走多远..."
    c "让我处理这个。"
    play sound "fx/undress.ogg"
    $ renpy.pause (1.0)
    m "我小心翼翼地脱掉衣服，尽量不让他被我和他的龙鳞身体不同的人类身体吓到。"
    Ry smile b "你...很完美。"
    Ry shy b "我们可以先从拥抱开始吗？习惯彼此的身体这样靠在一起？"
    c "听起来很美好。"
    hide remy with dissolve
    m "雷米在沙发上躺下，张开他的翅膀和四肢来接受我。"
    m "在他后腿之间，我看到一点粉红色的东西刚刚露出来。但现在，我专注于爬上他的胸部，避免伤到他或自己，同时抱紧他前腿上方。"
    show grey with dissolvemed
    play soundloop "fx/breathing.ogg" fadein 10.0
    m "当我安全地窝在他的前腿之间时，他用翅膀包裹住我们两个，像一个茧一样把我拉得更紧，靠在他的腹部鳞片上。"
    Ry normal b "这样可以吗？如果太过分..."
    c "很完美。就这样..."
    $ renpy.pause (0.8)
    m "我们在那里待了一段时间，他的呼吸和我们的心跳是唯一的声音，他温柔地用鼻子轻轻蹭在我头上，在他的翅膀下。"
    m "他的热量充满了空间，慢慢地我开始感到自己的身体变暖，心跳加速。"
    if bangok_four_playerhasdick is None:
        m "在双腿之间，我感到..."
        menu:
            m "在双腿之间，我感到...{fast}"
            "我的勃起。":
                $ bangok_four_playerhasdick = True
            "我的湿润。":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick:
        m "在双腿之间，我感到我的勃起越来越难以忽视，因为我找不到一个它不压在他腹部鳞片上的姿势。"
    else:
        m "在双腿之间，我感到我的湿润越来越难以忽视，股间的热度逐渐增强。"
    m "雷米似乎注意到了我的呼吸变化，开始更执着地在我脖子上蹭。"
    m "他温暖的舌头在裸露的皮肤上画出懒散的图案，令我脊背发麻。"
    menu:
        "更多...":
            $ renpy.pause (0.5)
            Ry shy b "更多的...？"
            m "抬起头，我用一只手抓住他的下巴，我们的嘴唇又一次相遇。"
            c "更多的舌头。更低一点。"
            Ry smile b "我会尽力。"
            $ bangok_four_remy4_store.path = "tongue"
        "准备继续了吗？":
            jump todo_out_of_content_bangok_four_remy4
        "[[保持沉默。]]":
            m "当他继续挑逗时，我忍不住发出了一声轻哼。他的尾巴在沙发上轻轻摆动。"
            Ry normal b "你想让我...？"
            c "请..."
            Ry shy b "你确定吗？我不--"
            m "我从他的鼻子上拉开，看着他的眼睛，眼中充满了欲望。"
            c "是的。"
            jump todo_out_of_content_bangok_four_remy4

    play sound "fx/undress.ogg"
    hide grey with dissolve
    if bangok_four_remy4_store.path == "tongue":
        m "雷米展开翅膀，让我从他身上滑下来，检查当我们回到他身边时我要处理的东西。"
    elif bangok_four_remy4_store.path is None:
        m "雷米展开翅膀，让我从他身上滑下来，检查我要处理的东西。"
    show remy shy b with dissolve
    if persistent.bangok_balls == True:
        m "一个大而粉红的阴茎在房间的光线下闪闪发光，头部已经渗出一滴厚重的透明液体。他的睾丸也很大且饱满，低垂在下面。"
    else:
        m "一个大而粉红的阴茎在房间的光线下闪闪发光，头部已经渗出一滴厚重的透明液体。"
    Ry shy b "你...这样看起来很美。"
    c "你也是。"
    menu:
        "问一下保护措施。":
            $ bangok_four_remy4_store.protection = True
            m "在我们被彼此的身体分散注意力之前，我设法提到了保护措施的想法。"
            c "呃，我们应该用保护措施..."
            Ry normal b "不同的龙种之间无法让对方怀孕，我假设这个规则也适用于人类。我们之间并不存在这个问题。但如果你会感觉更舒服，我可以去拿一些。"
            c "我觉得可能是个好主意... 以防万一。"
            hide remy with dissolve
            jump todo_out_of_content_bangok_four_remy4
        "继续。":
            $ renpy.pause (0.5)

    if bangok_four_remy4_store.path == "tongue":
        if bangok_four_playerhasdick == True:
            if bangok_four_remy4_store.protection == True:
                jump todo_out_of_content_bangok_four_remy4
                # jump bangok_four_remy4_male_protected_tongue_path
            else:
                jump bangok_four_remy4_male_unprotected_tongue_path
        else:
            jump bangok_four_remy4_female_tongue_path

    jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_male_unprotected_tongue_path:
    m "我握住自己的阴茎，坐在咖啡桌尽头的扶手椅边缘，用脚稍微推开桌子，以便雷米更好地接近我的身体。"
    m "雷米从沙发上滚下来，慢慢走向我，他的眼睛始终盯着我，然后在我的面前用交叉的前腿趴在地毯上。"
    m "他小心翼翼地看着我的勃起，把我的人类器官的大小与他自己的龙形期待进行比较。我不禁轻笑了一下他的可爱表情。"
    Ry shy b "你说更多的舌头？"
    m "用一只手抬起他的下巴，另一只手轻轻拍了拍他的鼻子。"
    c "是的，就在这里。"
    m "轻轻地，我引导他靠近我的裆部，感受他的温暖呼吸扑在我的阴茎上，他犹豫了一下。"
    c "我可以用你的角引导你吗？"
    $ renpy.pause (0.8)
    Ry shy b "可以。"
    m "我抓住他较大的、高耸的角，然后把他拉得更近。他接受了邀请，把我的肉质顶端含在他的鳞片嘴唇之间，然后用舌头细心地舔舐。"
    c "如此...不同..."
    m "在他带来的感觉中，我呻吟着，我的身体紧张起来，他更多地关注我的阴茎头的敏感底部。"
    m "然后，渴望更多，我引导他一路到我的根部，感觉他的鼻子靠在我的腹股沟上，他的下巴靠在我的睾丸上。"
    m "他舔了舔我的整根阴茎，品尝每一寸。当他完全探索了所有在他嘴里的东西，他张开嘴，用舌头开始轻轻探索我的睾丸。"
    c "雷米..."
    m "看着他如此专注于取悦我，我忍不住呻吟。他从正在做的事情中抬起头，眼中充满了对我是否感到不适的担忧。"
    c "不要停下。"
    m "轻轻推拉他的角，我开始用短小而挑逗的动作轻轻地上下滑动他鳞片的嘴唇。"
    m "他的舌头继续在我的肉头下部画出懒散的图案，引得我微微颤抖，喘息着需要。"
    m "为了延长这段时间，我把他完全拉离我，然后把我湿润的阴茎放在他发红的鼻子上。"
    m "他继续尝试探索我，用舌头和嘴唇舔舐和咬我的睾丸，然后把它们吸进嘴里，轻轻地用舌头按摩。"
    m "感觉到我的睾丸因需要释放它们的内容而变得沉重，我决定自己动手。"
    m "轻轻地从他的嘴里脱离，我开始手淫，偶尔暂停几下，当他用舌头舔了舔我的顶端或睾丸时。"
    m "在即将达到高潮时，我的身体紧绷起来，呼吸急促而愉快地喘息着，试图忍住。"
    m "但我忍不住了。随着一声解脱的呻吟，我在他的嘴里和脸上释放了我的射精，把黏黏的精液喷在他的鼻子和舌头上。"
    m "他僵住了，脸上泛起深红色，感受着我对他的感激之情。"
    m "然后，当我射精完毕，他用舌头在嘴里搅动着已落入嘴里的东西，又从鼻子顶上舔了一点。"
    Ry shy b "你... 你比我们味道稍微咸一点。"
    menu:
        "亲吻他":
            m "我笑了，然后从沙发上滑下来，吻了他的嘴唇。我们的舌头相遇，交换了一点我的味道，我紧紧拥抱着他，他的翅膀无助地拍动，挣扎着要逃脱我的拥抱。"
            m "尝到他舌头上的咸甜混合味道，我知道我想要更多。"
            m "当我们终于结束吻时，他气喘吁吁，脸上仍然有一些我的精液在闪闪发光。"
        "夸奖他":
            c "那真是太棒了。你太棒了。"
            m "被我的赞美弄得有些尴尬，却也感到高兴，他转过脸去。"
            c "希望我也能做得同样好。"
            m "他脸红得更厉害，点了点头。"
        "尝尝你的精液。":
            m "伸手向前，我从他鼻子上还粘着的精液中舀起一些，送到嘴边。"
            m "轻轻点头表示认可，我把它吞了下去，品尝我们交换的味道。"
            c "现在我可以和你的相比较了。"
    jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_female_tongue_path:
    m "我坐在咖啡桌尽头的扶手椅边缘，用脚稍微推开桌子，以便雷米更好地接近我的身体。"
    m "雷米从沙发上滚下来，慢慢走向我，他的眼睛始终盯着我，然后在我的面前用交叉的前腿趴在地毯上。"
    m "他小心翼翼地看着我的阴部，把我的人类开口的大小与他自己的龙形期待进行比较。我不禁轻笑了一下他的可爱表情。"
    Ry shy b "你说更多的舌头？"
    m "用一只手抬起他的下巴，另一只手轻轻拍了拍他的鼻子。"
    c "是的，就在这里。"
    ```python
    m "轻轻地，我引导他靠近我的私处，感受他的温暖呼吸扑在我的阴部。"
    m "然后他自己前进，把他的鳞片鼻子嵌在我的大腿之间。我的臀部在接触时抽搐了一下，我的呼吸停滞了，因为他开始用舌头探索我的双唇。"
    m "他那粗糙而炽热的舌头滑过我的内阴唇，先是描绘外表面，然后深入到内部。"
    c "雷米..."
    m "他的舌头滑进我体内的感觉使我的身体几乎立即做出了反应，我的肌肉紧绷，呼吸急促，试图控制自己的反应。"
    m "他那灵活的长舌舔舐我的内壁，发现新的地方刺痒我的神经。"
    m "感觉到我的身体向他弓起，我伸手引导他的头更深入位置，想要更多。"
    m "他照做了，把他的鼻子压在我的阴蒂上，同时继续舔舐我的分泌物。我的身体因愉悦而颤抖，臀部随着他舌头的节奏起伏。"
    m "偶尔他会停下来，看着我，明显在寻找我喜欢的指导。"
    c "继续。"
    m "他继续他的舔舐，他的舌头轻拍和探索我的最私密的部位，引得我发出更多的快感声音。"
    m "当他更多地关注我的阴蒂时，我的身体抽搐着，从他舌头提供的刺激中颤抖。"
    c "太...太多了。"
    m "他停了下来，从他正在做的事情中抬起头，眼中充满了对我是否感到不适的担忧。"
    c "不，我喜欢。只是...慢点。"
    m "他点了点头，放慢动作，集中在阴蒂周围的区域，而不是直接在阴蒂上。然后，他回到较深的探索，用他的舌头平面按摩我的内壁。"
    m "我呻吟着，感觉到我的高潮在体内积聚。"
    m "最后，我在极乐中喊叫，我的身体不受控制地颤抖，一波接一波的快感冲击着我。当我从巅峰降下来时，雷米继续舔舐，延长我的快感，直到我请求他停下来。"
    m "我倒在椅背上，气喘吁吁，当他从我的双腿之间缩回鼻子时。"
    m "他看着我，鼻子因为我的液体而闪闪发亮，他脸红得厉害。"
    m "过了一会儿，他更进一步，清理他的舌头在口腔的顶部，当我还是气喘吁吁。"
    m "他看起来有些尴尬，但也对自己的努力结果感到满意。"
    Ry shy b "感觉如何？"
    menu:
        "亲吻他":
            m "我笑了，然后从沙发上滑下来，吻了他的嘴唇。我们的舌头相遇，交换了一点我的味道，我紧紧拥抱着他，他的翅膀无助地拍动，挣扎着要逃脱我的拥抱。"
            m "当我们终于结束吻时，他气喘吁吁，脸上仍然有一些我的液体在闪闪发光。"
        "夸奖他":
            c "那真是太棒了。你太棒了。"
            m "被我的赞美弄得有些尴尬，却也感到高兴，他转过脸去。"
            c "希望我也能做得同样好。"
            m "他脸红得更厉害，点了点头。"
        "尝尝你的体液。":
            m "伸手向前，我把他鼻子上还粘着的一些液体抹到我的手指上，然后送到嘴边。"
            m "轻轻点头表示认可，我把它吞了下去，品尝我自己的精华味道。"
            c "现在我可以和你的相比较了。"
    jump todo_out_of_content_bangok_four_remy4

label bangok_four_remy4_suck_him:
    m "我轻轻一推，把他引导躺平在背上。"
    m "看到他那勃起的阴茎高高挺立，让我的心跳漏了一拍。"
    Ry shy b "你...要...吗？"
    c "如果你愿意的话。"
    m "我用手指包裹住他的阴茎，开始按照他的心跳节奏抚摸他的长度，观看我的手指在他充足的润滑液上滑动上下。"
    m "看到我带给他的愉悦，我自己的渴望也在增长，他的瞳孔放大，舌头在上唇上轻轻颤动。"
    m "最后，我停下来，抬头看着他的眼睛，微笑着说。"
    c "准备好了吗？"
    Ry smile b "是的。"
    m "我把嘴唇贴在他的顶端，立刻品尝到他的前液的甜味和他身体的温暖，感受着他血管下的脉动。"
    m "绕着他的龟头旋转我的舌头，我尽量接受更多，想要好好品尝他。"
    m "他轻轻呻吟，臀部轻颤，他的阴茎因我的抚慰而抽动。"
    c "继续？"
    Ry smile b "...是的。"
    m "点点头，我从他的顶端退开，然后进入一个缓慢的节奏，吸吮和吞咽，随着他的心跳在他眼中保持联系。"
    m "每隔几秒钟，我抬头与他对视，微笑着，偶尔拍拍他的腿，以示安慰。"
    m "最终，他的身体僵硬，轻声叫出，他的热种子填满了我的喉咙。我呛了一下，迅速吞下尽可能多的东西，然后完全退开。"
    m "我倒在他旁边，用手背擦了擦嘴角，轻笑这情境的荒谬。"
    m "他躺在我旁边，气喘吁吁，他的鼻子和嘴上还沾有我的精液。"
    Ry shy b "你... 你喜欢吗？"
    m "把头埋在我的手臂里，我微笑着。"
    c "绝对的。"
    m "我们的心一同跳动，汗水覆盖着我们裸露的身体，形成了一种共享欲望和情感的亲密纽带。"
    Ry shy b "我可以... 我可以进入你吗？"
    m "抬起头，我看着他，看到他眼中的脆弱和声音中的渴望。"
    c "请。"
    m "他小心地在我身后，滑进了一根长长的、冰凉的手指。"
    m "我喘息着，身体因突然的寒意颤抖。"
    Ry shy b "对不起... 太久了，我忘记了这样感觉有多冷。"
    m "耸耸肩，我转过头对他笑了笑。"
    c "别担心。"
    m "再次摆好位置，我用手臂和膝盖撑在地板上，等待他进入我。"
    m "慢慢地，我感觉到他的龟头压在我的入口处。"
    Ry shy b "我...我伤到你了吗？"
    m "没有，"
    jump todo_out_of_content_bangok_four_remy4

label todo_out_of_content_bangok_four_remy4:
    play sound "fx/system3.wav"
    s "你已经达到了当前角色可用内容的结尾。"
    s "回滚或准备崩溃。"
    $ renpy.error("已达内容结尾。")
```