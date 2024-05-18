
# Table of contents:
# Anna oral: Line 208. Tags used: Cloacas
# Male player oral: Line 353
# Female player oral: Line 466. Tags used: Cerv pen
# Anna fingering: Line 523. Tags used: Cerv pen (Note: Scene is diffrent if done fingering in Anna2)
# Male player tailfuck: Line 839
# Female player tailfuck: Line 969. Tags used: Cerv pen
# Anna riding male player: Line 1179. Tags used: Knots
# Afterglow: Line 1275

init python in bangok_anon_anna4:

    unplayed = True

    anna4choices = 0

    annaride = False
    playerride = False

    annaoral = False
    playeroral = False
    annafinger = False
    tailfuck = False

    tailinwomb = False


label bangok_four_anna4_replay_start:
    scene black with dissolve
    play music "mx/anna4.ogg" fadein 2.0
    $ renpy.pause(0.5)
    scene o at Pan((0, 250), (0, 250), 0.1)
    show anna smirk
    with dissolvemed

    if bangok_four_common.bangnokay.check():
        jump bangok_four_bangnokay_kill_replay

    jump bangok_anon_anna4_start


label bangok_anon_anna4_skipmenu:

# Hook from:
# An face "好了，好了。太挑剔了。"

stop music fadeout 1.0
$ renpy.pause (0.3)
play sound "fx/system3.wav"
s "你想看BangOK的GHS内容还是跳转到最后"
menu:
    "是的, 我想要猥亵安娜":
        play sound "fx/system3.wav"
        if bangok_four_common.bangnokay.check():
            s "太遗憾了.{cps=2}..{/cps}{w=1.0}{nw}"
            scene black with dissolvemed
            python:
                renpy.pause (2.5)
                mp.annaromance = True
                mp.save()
                annastatus = "good"
                annascenesfinished = 4
            jump _mod_fixjmp
        else:
            s "如你所愿.{cps=2}..{/cps}{w=1.0}{nw}"
            play music "mx/anna4.ogg" fadein 2.0
            jump bangok_anon_anna4_start

    "不,跳转到最后.":    
        s "如你所愿.{cps=2}..{/cps}{w=1.0}{nw}"
        scene black with dissolvemed
        python:
            renpy.pause (2.5)
            mp.annaromance = True
            mp.save()
            annastatus = "good"
            annascenesfinished = 4
        jump _mod_fixjmp
        

label bangok_anon_anna4_start:

# An face "好了，好了。太挑剔了。"
An smirk "现在, 让我们把这些东西从你身上移开..."
m "安娜给了我一个诱人的眼神, 开始脱我的衣服. 她首先解开我的衬衫扣子,接着就把它扔到沙发上."
c "呃，我们至少不应该先去卧室吗?"
m "安娜一言不发地拽着我的手腕, 接着把我带到了卧室里."
m "然后我们一到卧室, 她就把我推到床上, 接着不失时机地继续给我脱衣服."
play sound "fx/undress.ogg"
if bangok_four_playerhasdick == None:
    m "她开始脱下我的裤子，然后是内衣, 接着露出…"
    menu: 
        "我的阴茎.":
            m "她开始脱下我的裤子，然后是内衣, 接着露出{fast} 我的阴茎."
            $ bangok_four_playerhasdick = True

        "我的外阴.":
            "她开始脱下我的裤子，然后是内衣, 接着露出{fast} 我的外阴."
            $ bangok_four_playerhasdick = False

else:
    if bangok_four_playerhasdick == True:
        m "她开始脱下我的裤子，然后是内衣, 接着露出我的阴茎。"

    else:
        m "她开始脱下我的裤子，然后是内衣，接着露出我的外阴。"

if bangok_four_anna2.unplayed == True:
    if bangok_four_playerhasdick == True: # Male and didn't do the Anna 2 scene
        An "哈, 你肯定比我习惯的尺寸要小的多，但我相信我们还是会找到能让彼此都互相享受的方式."
    else: # Female and didn't do the Anna 2 scene
        An "呃, 这肯定不是我平时习惯的方式，但我相信我们还是会找到能让彼此都互相享受的办法."

else: # Did the Anna 2 scene
    An "哼哼, 就算你这次爽了我也不会停下来.{w} 除非你让 {i}我{/i} 爽翻了."

c "等等…… 保护措施呢？"
An normal "至少从我对你做的那么些测试中得到的少量数据显示, 我们的免疫系统非常相似. 所以我们在这方面的相性自然是很好的."

if bangok_four_playerhasdick == True:
    An "你显然不能让我怀孕，而且我也没有性病。"
else: 
    An "我们显然不能让对方怀孕，而且我也没有任何性病。"

c "我很确定我也没有那些玩意."
An smirk "那我们就没什么需要担心的了."

if bangok_four_playerhasdick == True:
    m "毫无疑问的, 她抓住了我的阴茎, 接着用长而温柔的触摸试着唤醒它."
    c "O-Oh!"
    m "她继续温柔地抚摸着，接着慢慢地加快了动作，直到我的下面完全勃起."

else:
    m "毫无疑问的, 她开始用爪子轻轻地拨弄着我的小穴, 用爪子尖温柔地翻动着我的阴唇."
    c "O-Oh!"
    m "她继续这么干着, 直到我被她的动作弄的舒服."

m "然后她后退了一步, 接着微笑着看着我."
An "既然我感觉不错，那我就让你选择我们从哪开始."


$ bangok_four_femalepartners += 1
$ bangok_anon_anna4.unplayed = False


label bangok_anon_anna4_beforemenu:

if bangok_anon_anna4.anna4choices == 1:
    An smirk "我会说这是一个不错的开始."
    c "一个好的 {i}开始?{/i}"
    An "你没想到我们会做得这么少, 是吗?"
    An "你很幸运, 我是如此的慷慨，甚至让你来挑选一切. 那么, 接下来呢?"

elif bangok_anon_anna4.anna4choices == 2:
    if bangok_four_playerhasdick == True: # If male and done two things jump to Anna riding the player
        An smirk "行了, 我想前戏已经做的够多了, 现在是时候来做点正事了."
        jump bangok_anon_anna4_playerride
    
    else: # If female and done two things Anna comments baced and what you did and lets you pick a thrid and final choice
        if bangok_anon_anna4.annaoral == True and bangok_anon_anna4.annafinger == True:
            An smirk "我会说我对此很满意。现在轮到你的回合了."

        elif bangok_anon_anna4.playeroral == True and bangok_anon_anna4.tailfuck == True:
            An smirk "行了，你已经玩得很开心了, 该轮到我了."

        else:
            An smirk "我们俩都爽到了... 但是我想我们还能更进一步不是么..."
            c "我也可以…"
            An "那么...接下来是什么呢?"

elif bangok_anon_anna4.anna4choices == 3: # F/F excusive to get to this point
    m "之后，我们两个一起倒在床上，沐浴在我们的余辉中。"
    jump bangok_anon_anna4_afterglow 

else:
    pass



label bangok_anon_anna4_menu:

menu: 
    "我可以骑你吗？" if bangok_four_playerhasdick == True and bangok_anon_anna4.playerride == False:
        $ bangok_anon_anna4.playerride = True
        c "我可以骑你吗？"
        An smirk "做你的梦去, 不管你喜不喜欢, 我永远都是那个掌管一切的龙"
        jump bangok_anon_anna4_menu

    "你能骑我吗？" if bangok_four_playerhasdick == True and bangok_anon_anna4.annaride == False:
        $ bangok_anon_anna4.annaride = True
        c "你能骑我吗？"
        An smirk "哈, 我早就想这么干了"
        An bangok blush "但现在不行. 我想充分利用这一点, 所以你必须等到我主动的去提出来."
        jump bangok_anon_anna4_menu

    "我能把你吃掉吗?" if bangok_anon_anna4.annaoral == False:
        $ bangok_anon_anna4.annaoral = True
        $ bangok_anon_anna4.anna4choices += 1
        jump bangok_anon_anna4_anna_oral

    "我能用你的嘴吗?" if bangok_anon_anna4.playeroral == False:
        $ bangok_anon_anna4.playeroral = True
        $ bangok_anon_anna4.anna4choices += 1
        if bangok_four_playerhasdick == True:
            jump bangok_anon_anna4_player_m_oral
        else:
            jump bangok_anon_anna4_player_f_oral

    "我能用指头扣你吗?" if bangok_anon_anna4.annafinger == False:
        $ bangok_anon_anna4.annafinger = True
        $ bangok_anon_anna4.anna4choices += 1
        jump bangok_anon_anna4_anna_finger

    "我能用尾巴操我吗?" if bangok_anon_anna4.tailfuck == False:
        $ bangok_anon_anna4.tailfuck = True
        $ bangok_anon_anna4.anna4choices += 1
        if bangok_four_playerhasdick == True:
            jump bangok_anon_anna4_player_m_tail
        else:
            jump bangok_anon_anna4_player_f_tail



label bangok_anon_anna4_anna_oral:

c "我能把你吃掉吗?"
if bangok_anon_anna4.playeroral == True and bangok_four_playerhasdick == False:
    An smirk "既然这是唯一能满足你的喜好的方式, 那就去做吧."

elif bangok_four_anna2.lick == False:
    An smirk "既然你这么执着地想, 那就去做吧."

else:
    An smirk "行, 去吧."

$ renpy.pause (0.2)
show anna:
    ease 1.0 xpos 0.2
$ renpy.pause(0.8)
show anna smirk flip:
    ypos 1.3 rotate -15
with dissolve

if persistent.bangok_cloacas == False:
    m "安娜于是仰卧在床上. 接着她张开了双腿，让我一览无余地看到她的缝隙和她的后穴."
else:
    m "安娜于是仰卧在床上。接着她张开了她的腿，给了我一个畅通无阻的视角去观赏她的缝隙."

m "我把脑袋放在她的双腿之间，脸离她的缝隙只有几英寸。安娜把她的双腿缠在我的肩膀后面，保持住我的姿势."
show anna bangok blush flip with dissolve
m "我开始玩弄她，轻轻地舔舐她的缝隙和它周围的区域."
m "我继续我温柔的调戏的动作，但安娜突然把一只前爪放在我的后脑勺上，接着直接把我的脸推到她的缝隙上."
An smirk flip "我真是受够了你的这些温柔的把戏, 你要是想让我爽, 你就得搞快点!"
m "我遵循了安娜的命令，我加快了步伐，用我的舌头穿过她的缝隙."
An "真是个听话的人类"
m "我开始更快的移动我的舌头. 探索她缝隙里那光滑的通道."
An bangok blush flip "哦~你的舌头比龙类的要短. 不过你的舌头更柔软和更厚一些."
m "意识到这对安娜来说还不够，我试着去吮吸她的下面."
An bangok lipbite flip "哦啊! 那是什么?!"
m "由于我担心我的动作不小心伤害了她, 我停了下来, 开始抬起头来准备回答, 但很快就被推倒了."
An "别, 别说话... {w=0.8} 不...不管那是什么, 继续做就是了."
m "我不得不继续把我的嘴贴在她的下面, 用嘴巴贴着她的缝隙, 继续把舌头伸进去舔舐和吮吸着"
An "该死的. 这绝对是新的体验."
m "安娜轻轻地紧咬着嘴唇. 好像是想忍住自己的声音. 但是她发出的微妙的声音和她下身渗出的液体告诉了我我需要知道的一切."
An "哈啊…"
m "她把我推得更深了一些。她的汁液覆盖在我的舌头, 嘴巴, 还有脸上。我更深入地探索，感觉到她的缝隙紧紧地贴合在我的舌头上."
if persistent.bangok_cloacas == True:
    m "然后我把注意力转移到她的后穴上. 我的吮吸和舌头的舔舐使她身体微微地颤抖."
$ renpy.pause (0.5)
m "我继续我的动作, 从她的缝隙中挤出来的汁液味道很不错. 但后来我突然被打断了."

play sound "fx/bed.ogg"
scene bangok_anon_o_ceiling at Pan((0,360), (0,120), 1.5) with dissolvemed
$ renpy.pause (1.7)
show anna smirk at Position(ypos=1.5) with easeinbottom
show anna:
    ease 1.2 ypos 1.4 zoom 1.3
$ renpy.pause (0.5)
m "安娜放开了我, 接着把我们俩都翻了过来. 所以她现在是上面的那个龙, 而我则躺在她的下面."
An "这是你自找的..."
show anna smirk at Position(ypos=1.1) with ease
$ renpy.pause (0.2)
show anna smirk:
    ease 1.5 zoom 1.7
m "安娜把我抬起来, 把她的膝盖放在我头的两侧, 她的缝隙正在我的脸上往下滴着淫液."
An "现在, 该让你的嘴巴动起来了~"
show anna:
    ease 1.5 ypos 1.05 zoom 2.3
m "她又把前爪放在我的后脑勺，同时把我拉到她身边，把她自己的身体降下来一些。"
m "接着我从我刚刚停止的地方开始继续的吮吸着她的缝隙"
An bangok lipbite "哈啊! 妈的... 那...那是..."
m "安娜被我给她带来的全新的感觉的冲击而说不出话来."
$ renpy.pause (1.5)

show anna:
    ease 1.3 ypos 1.0
    ease 1.3 ypos 1.05
    repeat

m "为了最大限度地利用这一点，安娜开始在我的脸上磨蹭自己的小穴。这让我的动作开始充满挑战性，但我设法做到了。"
m "突然，她没有继续推我的后脑勺，而是直接抓住我的头发，开始把我拉向她的身体里。"
menu:
    "[[阻止她.]":
        play sound "fx/slap1.wav"
        show anna sad with dissolve
        show anna:
            ease 1.0 zoom 1.7 ypos 1.2
        m "我一巴掌拍开她的手，然后动了动头，这样我就可以说话了。"
        c "请不要那样拉我的头发。那样真的很痛。"
        if bangok_four_hornincident == True:
            c "这就像我抓住你的角一样把你拉到身边。"
            An face "看来，我真的应该假设这种情况......不好意思。"

        else:
            An face "事后看来，我真的应该认为考虑着去抓住某龙的角也是相当不愉快的......不好意思。"
            $ bangok_four_hornincident = True

        c "你仍然可以推我的后脑勺。只是不要扯我的头发。"
        $ renpy.pause (0.5)
        show anna bangok blush with dissolve
        show anna at Position(ypos=1.0) with ease
        $ renpy.pause (0.2)
        show anna bangok blush with dissolve
        show anna:
            ease 1.2 zoom 2.3 ypos 1.05
        m "我回到了原来的位置，安娜又慢慢地加快了步伐。"
        show anna:
            ease 1.3 ypos 1.0
            ease 1.3 ypos 1.05
            repeat
        $ renpy.pause (2.2)
        An bangok lipbite "嗯......"
        
    "[[随她去.]":
        m "她现在这样做, 让我更加地紧贴着她的小穴. 我的牙齿轻微地碰撞在她的小穴上, 这又使得她的身体猛地颤抖了一下."
        An "Nngh!"

m "我试着尝试使用更多的吸力，安娜此起彼伏的呻吟向我证明了这是正确的做法。"
An "他妈的......几乎..."
$ renpy.pause (3.0)
show anna:
    ease 0.6 zoom 2.5 ypos 1.15
show anna orgasm with dissolve
play sound "fx/snarl.ogg"
m "突然间，安娜把大部分的重量都压在了我身上，她的小穴内壁紧紧地夹住了我的舌头。接着她发出一声咆哮，在这之后她的汁液浸湿了我的脸。"
$ renpy.pause (2.0)
show anna bangok lipbite with dissolve
m "从性高潮中回过神后，她紧紧积压着我舌头的内壁放松了，她慢慢地从我身上下来。"
$ renpy.pause (1.5)
scene black with fadequick
$ renpy.pause (0.3)
scene o at Pan((0, 250), (0, 250), 0.1) with dissolveslow
show anna smirk flip at Position(xpos=0.2) with dissolve
$ renpy.pause (0.5)
An "既然这样了...{w=0.5} 绝对是有点东西的..."
An bangok blush flip "考虑到你舌头的大小和形状，这比我想象的要好得多。"
An smirk flip "现在，告诉我......你到底做了什么，突然让我感觉起来变得更舒服了？"
c "吮吸, 人类的嘴唇可以很好地密封. 所以，我猜你以前从未有过这样的感觉？"
An "不, 以前从来没有过, 这绝对是全新的体验"
$ renpy.pause (1.0)
show anna at center with ease
show anna normal flip with dissolve
$ renpy.pause (1.0)

jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_player_m_oral:

c "你能用你的嘴对我吗？"
An bangok blush "行吧。我想我会发现人类的味道与龙的味道有多大不同。"
$ renpy.pause (0.5)
play sound "fx/undress.ogg"
$ renpy.pause (1.0)
show anna at Position(xpos=0.6, ypos=1.1) with ease
show anna at Position(ypos=1.3) with ease
$ renpy.pause (0.5)
m "我坐在床沿上，而安娜则下了床，跪在我面前。"
show anna smirk with dissolve
show anna:
    ease 1.5 ypos 1.48
    ease 1.5 ypos 1.49
    repeat

m "她没有把我的阴茎放在她的龙吻里，而是用舌头上下舔我的阴茎。虽然她的舌头感觉有点粗糙，但这并没有带来更多的不适, 反而更舒服."
$ renpy.pause(3.5)
show anna bangok orgasm with dissolve
show anna:
    ease 1.0 ypos 1.5
m "然后我的阴茎被她的龙吻整个地含住，我从她的牙齿在我的阴茎表面的接触和触摸感到了相当的刺激"
m "她一开始只少少地舔舐。她的舌头缠绕在我的尖端，探索并拉扯着我的阴茎。"
show anna:
    ease 1.0 ypos 1.52
m "然后她把我的下面含的更深，她的舌头在我的阴茎根部附近形成了一个紧紧的环。我忍不住发出一声低沉的呻吟。"
m "然后她把手放在我的大腿上。同时支撑着自己，把我固定在原地。"
show anna:
    ease 1.0 ypos 1.54
if bangok_four_anna2.doneoral == True:
    m "然后她把我含进了比上次更深的喉咙里。她的鼻子压在我的腹股沟里，嘴唇摩擦着我的蛋蛋。"
else:
    m "然后她把我含进了比上次更深的喉咙里。她的鼻子压在我的腹股沟里，嘴唇摩擦着我的蛋蛋。"
c "O-Oooh…"
$ renpy.pause (1.0)
show anna:
    ease 1.0 ypos 1.51
m "之后，她开始向后移动，她的舌头轻轻地擦过我的阴茎的尖端。"
menu:
    "[[抓住她的角.]" if not bangok_four_hornincident:
        $ bangok_four_hornincident = True
        show anna disgust with dissolve
        m "我以为安娜已经拉开了，我抓住她的角，试图把她拉回我的腹股沟里。但她一巴掌拍开了我的手。"
        play sound "fx/slap1.wav"
        $ renpy.pause (0.2)
        show anna at Position(ypos=1.25) with ease
        An face "你至少可以先问然后再抓住我的角。唉, 与经验不足的人在一起，这对你来说不会有好结果。"
        c "你是什么意思？"
        An sad "这是一个敏感区域, 这可以防止它们从我们的头上被扯下来，所以用它们来控制我们头部的运动是......非常不可取的。"
        c "啊，对不起。那我能抓住你的角吗？"
        An normal "做梦吧，我才是那个控制你的龙。"
        $ renpy.pause (1.0)
        show anna bangok orgasm with dissolve
        show anna at Position(ypos=1.51) with ease
        m "没过多久，安娜又回到了我的腹股沟，把我的阴茎带回了她的嘴里。"

    "我-我可以抓住你的角吗......？":
        c "我-我可以抓住你的角吗......？"
        m "她没有再往上退，轻蔑地摇了摇头，让我的阴茎在短时间内部分离开了她的龙吻。"
        m "我很失望，但尊重安娜不抓住她的角的意愿。{w} 不过，我的失望并没有持续太久。"

    "[[享受.]":
        pass
    
play soundloop "fx/rub2.ogg" fadein 1.5
show anna:
    ease 0.75 ypos 1.52
    ease 1.0 ypos 1.50
    ease 0.4 ypos 1.52
    ease 0.6 ypos 1.50
$ renpy.pause (2.75)
show anna:
    ease 0.25 ypos 1.52
    ease 0.4 ypos 1.50
    repeat

$ renpy.pause (2.0)
m "接着安娜加快了她的动作，在我的鸡阴茎上更快地运动着，并用重新调整了收缩在我的阴茎底部的舌头环"
m "她的嘴唇闭在我的下面和她的舌环上，就像我的阴茎在她的嘴里同时被操了两次。"
m "我忍不住呻吟了一声，把头向后仰，享受着愉快的快感."
c "A-Ah!"
m "她紧绷的舌环不停地在我的上上下移动，挤压和拉扯它，让我一秒一秒地接近我的极限."
$ renpy.pause (6.0)
stop soundloop fadeout 0.5
show anna bangok blush at Position(ypos=1.3) with ease
show anna smirk with dissolve
m "但就在我快要达到高潮的时候，安娜完全离开。接着她紧紧地握住我的阴茎的底部，只让一小滴前液漏出来。"
$ renpy.pause (1.5)
show anna at Position(ypos=1.1) with ease
show anna:
    ease 1.0 xpos 0.5 ypos 1.0

if bangok_anon_anna4.tailfuck == True:
    $ renpy.pause (2.5)
    c " 边缘控制... {i}这个{/i} 这太残忍了."
    An smirk "行吧。如果你要抱怨这么多，那么这已经足够了。"
    jump bangok_anon_anna4_playerride

else:
    c "嘿!"
    An smirk "什么？你以前没有听说过边缘控制吗?"
    c "嗯，我有......"
    An bangok blush "那就别抱怨了, 你就继续享受吧。"

$ renpy.pause (1.0)
show anna normal with dissolve
$ renpy.pause (1.0)

jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_player_f_oral:

c "你能用你的嘴对我吗？"
if bangok_anon_anna4.annaoral == True:
    An smirk "好吧，我回报这个恩惠是公平的，对吧？"
else:
    An bangok blush "这可能是我经验最少的一个姿势，但我相信无论如何我都能让你爽翻的。"

m "我坐在床沿上，安娜下了床，跪在我面前。"
show anna at Position(xpos=0.6, ypos=1.1) with ease
show anna at Position(ypos=1.3) with ease
show anna smirk with dissolve
show anna:
    ease 1.0 ypos 1.50
m "我张开双腿，让安娜很容易接触到我的腹股沟，几乎立刻，她就开始舔我的阴道外唇来取悦我。她的舌头感觉有点粗糙，但谢天谢地，这足以带来更多的快乐而不是不适。"
m "然后她把手放在我的大腿上。同时，她支撑着自己，把我抱在原地，继续挑逗我，他的舌头穿透了我的阴道。"
show anna at Position(ypos=1.51) with ease
m "然后她开始更深入，她的舌头在她进入时微微擦过我的阴蒂，让我颤抖和不断地呻吟。"
c " A-Ah!"
m "她继续在那个区域舔了相当长的时间，保持着一种疯狂的挑逗感，让我迫切地想要她更深。"
show anna:
    ease 1.5 ypos 1.52
m "我开始向下推入安娜的舌头，她认为这是在邀请她更深入，张大嘴巴以免用牙齿抓伤我."
m "她加快了步伐，在我湿漉漉的通道里舔舐和探索，试图在我身上找到那个敏感点。"
if persistent.bangok_cervpen:
    m "然后她的舌尖刚好弹了一下我的子宫颈，让我再次呻吟起来。我把头向后仰，由于纯粹的快感而暂时瘫痪了。"
    m "她继续用舌头轻弹我的子宫颈。每一次都在我的身体里发出一波快感，让我在一秒钟内更接近我的极限。"
    $ renpy.pause (2.5)
    show black with fadequick
    m "突然，我的内壁紧紧地咬住她的舌头，用我的汁液浸湿了它。尽管有额外的阻力，但安娜仍然设法将舌尖推到我的子宫颈上."

else:
    m "然后她的舌尖在我更深的内壁上轻弹，让我再次呻吟。我把头向后仰，由于纯粹的快感而暂时瘫痪了。"
    m "她继续用舌头在我体内深处轻弹。每一次都在我的身体里发出一波快感，让我在一秒钟内更接近我的极限。"
    $ renpy.pause (2.5)
    show black with fadequick
    m "突然，我的内壁紧紧地咬住她的舌头，用我的汁液浸湿了它。尽管有额外的阻力，安娜仍然设法将舌尖尽可能深地插入我体内。"

hide black with dissolveslow
$ renpy.pause (0.5)
m "安娜慢慢地收回了她的舌头，而我还处于性高潮的余震中。"
show anna bangok blush with dissolve
show anna at Position(ypos=1.3) with ease
show anna at center with ease
show anna smirk with dissolve
$ renpy.pause (0.5)
An "所以我干的怎么样?"
c "我再也不会满足于另一个人类来这样玩我了。"
An "我就知道"
$ renpy.pause (1.0)
show anna normal with dissolve
$ renpy.pause (2.0)

jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_anna_finger:

c "我能用指头扣你吗?"
if bangok_four_anna2.annacame == True:
    An smirk "哦，我很乐意用你的胳膊去开启第二轮。"
    show anna at Position(xpos=0.25) with ease
    show anna bangok blush flip with dissolve 
    m "安娜从床上下来，站在床边，示意我也起床。"
    An "跪在这里，这次把你的胳膊肘撑在床上。"
    c "是的Ma'ma "
    An smirk flip "真是听话的小人类啊"
    show anna smirk with dissolve
    m "我跪下，按照指示支撑我的肘部。安娜用我的手把她已经湿漉漉的缝隙铺开，她的一条腿在我面前垂下来，另一条腿支撑在床上。"
    show anna:
        ease 1.2 ypos 1.01
    m "安娜没有像我预期的那样慢慢开始，而是立即尝试一下子包裹住我的整只手。"
    c "等等，你难道不应该先放松一下，而不是试图裹住我的整只手吗？"
    An "我为什么要这样做？你知道我可以包裹住你的整条胳膊。在上次之后，你不会再开始挑逗我了。"
    m "我答应了，把拇指合在手里。然后安娜开始下降到我的手上，当她的缝隙在我的手腕上合拢时停了下来。"
    show anna:
        ease 1.2 ypos 1.02
    $ renpy.pause (0.5)
    An bangok lipbite "Ngh…"
    m "她的缝隙紧紧地包裹住我的手腕，再一次，更多的液体开始从她身上渗出，浸湿了我的手和手臂。就像上次我把天然润滑剂涂在手臂上一样，为即将到来的事情做好准备。"
    show anna:
        ease 1.2 ypos 1.04
    m "安娜把更多的胳膊伸进了她的身体里。她通道里的肌肉开始地挤压我的胳膊。"

    if bangok_four_anna2.fisting == True:
        m "就像上次一样，我把手握成拳头."
        An "嗯......好..."
        $ renpy.pause (0.5)
        show anna:
            ease 1.2 ypos 1.02
            ease 0.4 ypos 1.06
        m "然后安娜把自己的身体抬起来，然后迅速地下压了。"
        show anna bangok orgasm with dissolve
        An "A-Ah! F-Fuck!"

    else:
        m "我没有像上次那样做，而是试着把手握成拳头。"
        An sad "你在...干什么..."
        m "安娜转过身来，试图感受一下我手的新位置。"
        An bangok blush "Hm."
        show anna:
            ease 1.0 ypos 1.02
            ease 0.4 ypos 1.06
        m "安娜站了起来。然后换了个方向，接着把身体快速地下降。"
        show anna bangok orgasm with dissolve
        An "F-Fuck! Yes!"

    show anna bangok lipbite with dissolve
    show anna:
        ease 0.7 ypos 1.02
        ease 0.5 ypos 1.04
    show anna:
        ease 0.4 ypos 1.02
        ease 0.25 ypos 1.04
        repeat

    play soundloop "fx/rub2.ogg" fadein 3.0
    m "安娜又开始操我的手腕和胳膊。但这一次，她没有那么慢，也不需要时间去休息。"
    $ renpy.pause (2.5)
    m "她体内的肌肉紧紧地挤在我的手臂上，她的汁液开始更快地从我的手臂上滴落。"

    if persistent.bangok_cervpen:
        m "再一次，我的拳头抵住了她子宫颈。每次我的手都推得更远一点。"
        An "F-Fuck, a-almost…"
        $ renpy.pause (4.0)
        show anna bangok orgasm at Position(ypos=1.07) with ease
        stop soundloop fadeout 0.5
        play sound "fx/snarl.ogg"
        m "突然，安娜更加用力地往下推，我的手又穿过了她的子宫颈。她的阴道夹住了我的胳膊，她咆哮着，尾巴拍打着床。"
        $ renpy.pause (2.0)
        show anna bangok lipbite with dissolve 
        $ renpy.pause(1.0)
        m "性高潮过后，安娜休息了一会儿，喘了口气。"
        An smirk "我以前说过，但你的胳膊真是不错。我很确定我永远不会厌倦这样做。"
        $ renpy.pause (0.5)
        show anna bangok orgasm with dissolve
        show anna:
            ease 1.8 ypos 1.1
        $ renpy.pause(1.8)
        show anna bangok lipbite with dissolve
        show anna:
            ease 1.5 ypos 1.07
            ease 1.5 ypos 1.1
            ease 1.5 ypos 1.07
            ease 1.5 ypos 1.1
        m "她尽可能多地抓住我的胳膊，直到我的手停在她的子宫上。她继续坐在我的前臂上，偶尔四处晃动，享受我尽可能深入她的感觉。"
        $ renpy.pause (3.5)
        show anna:
            ease 1.5 ypos 1.04
        $ renpy.pause (1.0)
        show anna bangok orgasm:
            ease 1.0 ypos 1.07
        $ renpy.pause(1.0)
        show anna bangok lipbite with dissolve
        m "过了一段时间，她终于试着站起来了。当我的手离开她的子宫颈时，她摇摇晃晃，让她的体重落回子宫颈上。我帮她伸出胳膊，帮助她完成这个过程."
        $ renpy.pause(2.0)
        play sound "fx/uncork.ogg"
        show anna bangok blushpalm at Position(ypos=1.08) with ease
        An "谢了."

    else:
        m "她不停地用力地挤压我的胳膊，每次都把自己推得更深一点。"
        An "F-Fuck, a-almost…"
        $ renpy.pause (4.0)
        show anna bangok orgasm at Position(ypos=1.08) with ease
        stop soundloop fadeout 0.5
        play sound "fx/snarl.ogg"
        m "突然，她把自己推得更深了。她的阴道夹住了我的胳膊，她咆哮着，尾巴拍打着床。"
        $ renpy.pause (2.0)
        show anna bangok lipbite with dissolve 
        $ renpy.pause(1.0)
        m "高潮过后，安娜休息了一会儿，喘了口气。"
        An smirk "我以前说过，但你的胳膊真是不错。我很确定我永远不会厌倦这样做。"
        $ renpy.pause (1.5)
        show anna bangok lipbite with dissolve
        show anna:
            ease 1.5 ypos 1.05
            ease 1.5 ypos 1.08
            ease 1.5 ypos 1.05
            ease 1.5 ypos 1.08
        $ renpy.pause (2.5)
        m "她停了下来，靠在我的胳膊上，享受着我深入她体内的感觉，偶尔移动一下。"
        $ renpy.pause (1.0)
        m "我感觉到她身体深处的阻力，就在我的拳头外面，我以为她不会被束缚。"
        $ renpy.pause (0.5)
        show anna:
            ease 1.7 ypos 1.05
        $ renpy.pause (2.5)
        m "过了一段时间，她终于试着站起来了。她花时间慢慢地移动了一下，随后又稍微停了一下。我为她伸出手臂，帮助了整个过程。"
        $ renpy.pause(2.0)
        play sound "fx/uncork.ogg"
        show anna bangok blushpalm at Position(ypos=1.03) with ease
        An "谢了."


else:
    An normal "好吧。小心你的指甲。我不想你在里面抓我。"
    c "除非你比人类更脆弱，否则我怀疑这将不是一个问题。"
    $ renpy.pause (0.7)
    show anna:
        ease 1.0 xpos 0.2
    $ renpy.pause(0.8)
    show anna flip:
        ypos 1.3 rotate -15
    with dissolve
    show anna smirk flip with dissolve
    $ renpy.pause(1.0)
    m "我走近安娜，她现在仰面躺在床上，向我露出她的缝隙。"
    m "慢慢地，我把两根手指按进去，用剩下的手继续我的小而温柔的画圈圈。安娜悬在空中的双腿微微颤抖。"
    show anna smirk flip with dissolve
    $ renpy.pause (0.5)
    m "在这种温柔的挑逗中又给了她一会儿之后，我又加了第三根手指，发现它比前两根更容易滑入，因为她的自然润滑液开始渗出她的小穴"
    An smirk flip "你说的是对的。你的指甲不是问题。"
    An bangok blush flip "而且你的皮肤比任何龙的鳞片都要柔软得多。"
    m "我又加了一根第四根手指，安娜的小穴稍微有一些阻力。但是在她的自然润滑液下，它直接进去了，随后就是我的大部分的手掌。"
    An bangok lipbite flip "现在, 你慢慢地上道了"
    An smirk flip "我想要你的胳膊。让我们看看剩下的软肉是什么感觉。"
    c "哦哦，好..."
    An "真是个听话的小人类"
    m "到目前为止的四根手指在她的缝隙里不断地滑进滑出，让她习惯这个大小，直到我的手湿透并埋到我的拇指根部。"
    An bangok blush flip "让我起来。我有不同的想法。"
    m "我同意了，抽出我伸进去的那部分手。不久之后，安娜站了起来。"
    $ renpy.pause (0.5)
    hide anna with dissolve
    $ renpy.pause (0.0)
    show anna bangok blush flip at Position(xpos=0.25, ypos=1.0) with dissolve
    show anna:
        ease 1.0 xpos 0.6
    $ renpy.pause (0.7)
    show anna bangok blush with dissolve
    An "跪在这里，把你的胳膊肘撑在床上，这里。"
    m "我跪在床边。一旦我的手就位，安娜确保我的手指是我在插入她时使用的形状，并且我保持这种状态。"
    show anna at Position(xpos=0.25) with ease
    m "然后她转过身来，把她光滑的缝隙重新合起来，她的一条腿正好落在我面前，另一条腿支撑在床上。"
    $ renpy.pause (0.5)
    show anna:
        ease 1.2 ypos 1.02
    show anna bangok lipbite with dissolve
    An "Nnh!"
    $ renpy.pause (0.5)
    m "安娜通道中的肌肉地压在我的手上，在我的手腕上覆盖了更多的天然润滑剂，让它沿着我的手臂流淌。"
    $ renpy.pause (0.4)
    An bangok blush "流的到处都是..."
    m "我按照吩咐做了，试图将她的汁液更均匀地分布在我手臂的下一部分。安娜颤抖着，我另一只手的手指拂过她的缝隙。"
    An smirk "你还靠在床上，对吧？"
    c "是的."
    An bangok blush "好的."
    show anna bangok lipbite with dissolve
    show anna at Position(ypos=1.0) with ease
    show anna at Position(ypos=1.04) with ease 
    m "安娜站起身来，她的子宫几乎要把我的胳膊挤压在一起。就在我的手指即将离开之前，她调转方向，向下压，像假阳具一样把自己压在我的手上。"
    An "Ah!"
    if persistent.bangok_cervpen:
        m "我们几乎立刻就遇到了阻力，但这个阻力来自她的体内。"
    else:
        m "她停顿了一下，调整了一下自己的表情。"

    show anna smirk with dissolve
    m "她回头看了一眼。无论这对她来说是什么感觉，这都是一种很好的感觉。"
    m "为了让安娜更愉快，我试着把手变成拳头。"
    $ renpy.pause (0.5)
    An sad "你干了什么…?"
    m "安娜在我身边扭动，感觉到我给她撑开了额外的房间，可以继续压着我的胳膊。"
    An bangok blush "Hm."
    show anna bangok lipbite with dissolve
    show anna:
        ease 1.0 ypos 1.02
    m "她抬起头，微微地移动并围绕着我的拳头在她体内运动。"
    m "然后她改变了方向，快速向下压."
    show anna bangok lipbite:
        ease 0.4 ypos 1.06
    $ renpy.pause (0.3)
    show anna bangok orgasm with dissolve
    An "F-Fuck! Yes!"
    play soundloop "fx/rub2.ogg" fadein 5.0
    show anna bangok lipbite with dissolve
    show anna:
        ease 1.0 ypos 1.02
        ease 1.0 ypos 1.04
        ease 0.7 ypos 1.02
        ease 0.5 ypos 1.04
    $ renpy.pause (3.0)
    show anna:
        ease 0.40 ypos 1.02
        ease 0.25 ypos 1.04
        repeat
    m "安娜开始操我的手腕和手，起初是温柔的，然后是越来越大的力度."
    show anna bangok lipbite with dissolve

    if persistent.bangok_cervpen:
        m "每一次，她都用力地用我的手抵住她体内的阻力."
        An "快要..."
        $ renpy.pause(3.0)
        stop soundloop fadeout 0.5
        play sound2 "fx/snarl.ogg"
        show anna bangok orgasm:
            ease 0.3 ypos 1.07
        m "突然，安娜用力往下推，终于冲破了阻力。她的尾巴拍打着床，我的胳膊又消失在她体内几英寸。我手上的压力减轻了，手臂上起伏的压力越来越大，现在她狭窄的通道里塞满了更宽的部分."
        m "安娜在那里呆了好一会儿，只是在她发出的咆哮声后喘了口气。"
        show anna bangok lipbite with dissolve
        $ renpy.pause (1.5)
        An smirk "唷。。。你确实有点东西."
        An bangok blush "这对任何龙来说都是不安全的。由于鳞片和锋利的爪子，并且没有保护罩可以保护。"
        An smirk "不过，现在..."
        show anna bangok orgasm with dissolve
        show anna:
            ease 1.5 ypos 1.1
        $ renpy.pause(1.5)
        show anna bangok lipbite with dissolve
        m "安娜在我的胳膊上沉得更深，现在被她的汁液浸透了，直到她几乎坐在我的前臂上。她内心还有另一种阻力，我以为她不会试图克服这种阻力。"
        m "有那么一会儿，她继续坐着，我的手在她的子宫里，享受着我深深地在她体内的感觉。"
        $ renpy.pause(2.5)
        show anna bangok lipbite with dissolve
        show anna:
            ease 1.5 ypos 1.04
        $ renpy.pause(1.5)
        show anna bangok orgasm with dissolve
        show anna:
            ease 0.25 ypos 1.07
        $ renpy.pause (0.8)
        show anna bangok lipbite with dissolve
        m "过了一段时间，她终于试着站起来了。当我的手离开她的子宫颈时，她摇摇晃晃，让她的体重落回子宫颈上。我帮她伸出胳膊，帮助她完成了这个过程。"
        $ renpy.pause(2.0)
        play sound "fx/uncork.ogg"
        show anna bangok blushpalm at Position(ypos=1.08) with ease
        An "谢谢."

    else:
        m "她不停地用力地我的胳膊，每次都把自己推得更深一点。"
        An "几乎..."
        $ renpy.pause(3.0)
        stop soundloop fadeout 0.5
        play sound "fx/snarl.ogg"
        show anna bangok orgasm:
            ease 0.3 ypos 1.08
        m "突然，她把自己推得更深了。她的阴道夹住了我的胳膊，她咆哮着，尾巴拍打着床。"
        $ renpy.pause (1.5)
        show anna bangok lipbite with dissolve
        $ renpy.pause (1.0)
        An smirk "唷。。。你确实有点东西."
        m "当安娜用身子抵住我的前臂时，我感到她身体深处有一种阻力，我认为她不会试图玩弄这种阻力。"
        $ renpy.pause (2.0)
        show anna bangok lipbite with dissolve
        show anna:
            ease 1.7 ypos 1.06
        $ renpy.pause (2.5)
        m "过了一段时间，她终于试着站起来了。她慢慢来，慢慢地移动，中途停了下来。我帮她伸出胳膊，帮助她完成了这个过程。"
        $ renpy.pause(2.0)
        play sound "fx/uncork.ogg"
        show anna bangok blushpalm at Position(ypos=1.03) with ease
        An "谢谢."

    
$ renpy.pause (0.5)
show anna bangok blushpalm flip with dissolve
show anna at Position(xpos=0.35, ypos=1.02) with ease
$ renpy.pause (0.2)
show anna at Position(xpos=0.4, ypos=1.0) with ease
$ renpy.pause (0.2)
show anna at Position(xpos=0.5) with ease
$ renpy.pause (0.2)
m "在不安地走了几步后，她回到了床上，我跟了上去。"
show anna bangok blush with dissolve
An "在那之后，我需要更长的时间休息......"
$ renpy.pause (2.5)
An smirk "唷。。。好。"
$ renpy.pause (2.5)

jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_player_m_tail:

c "我能用尾巴操我吗?"
if bangok_four_anna2.tail == True:
    An smirk "所以，你很喜欢我上次给你的那一小点的恩惠，以至于你想知道我的整条尾巴是什么样子的吗？"
    c "好吧，不是你的 {i}整条{/i} 尾巴......"
    An bangok blush "明显地。但不仅仅是用尖端来挑逗你。"

else:
    An smirk "哦。我没想到你会喜欢尾交，因为你们人类没有尾巴。不过我不是在抱怨。"

$ renpy.pause (1.0)
play sound "fx/bed.ogg"
scene bangok_anon_o_ceiling at Pan((0,360), (0,120), 2.5) with dissolvemed
$ renpy.pause (2.5)
show anna smirk at Position(ypos=1.3) with easeinbottom
m "我继续仰卧，安娜把自己放在我的双腿之间，尾巴指向我。"
An bangok blush "第一件事......"
m "安娜以惊人的灵活性将尾巴向后卷曲，朝向自己和两腿之间。然后她用一只手把它引导到她光滑的缝隙中。"
c "你在做什么...?"
An smirk "如果没有某种润滑，这不会那么令人愉快，并且我也想从中得到一些东西来取悦自己"
$ renpy.pause (0.5)
show anna bangok lipbite with dissolve
show anna:
    ease 1.2 ypos 1.285
m "然后安娜把尾巴深深地伸进了自己的体内，只是在到达尾巴较粗的部分时才放慢速度。"
An "Ngh…"
$ renpy.pause (1.0)
show anna:
    ease 1.0 ypos 1.27
    ease 0.9 ypos 1.3
show anna:
    ease 0.6 ypos 1.27
    ease 0.8 ypos 1.3
    repeat
$ renpy.pause (2.0)
m "然后她开始把尾巴伸进伸出她的通道，简直是在操她自己。每一次，她的汁液都沾满了她的尾巴，让它每次都以更小的阻力滑进去。"
$ renpy.pause (3.0)
show anna:
    ease 1.2 ypos 1.3
$ renpy.pause (0.5)
show anna smirk with dissolve
m "持续了一段时间后，她慢慢地开始从她体内取回她现在润滑的尾巴，并将其对准我的双腿之间."
m "她用双手搂住我的腰，用尾巴戳我的屁眼，尾巴的尖端勉强能压进去."
An "你准备好了吗?"
c "是的..."
$ renpy.pause (0.5)
show anna:
    ease 1.7 ypos 1.26
m "慢慢地，安娜一开始只把尾巴的尖端和一小部分的长度推入我体内。多亏了她的自然润滑，它很容易进入。"
$ renpy.pause (0.7)
show anna:
    ease 1.0 ypos 1.3
    ease 0.7 ypos 1.26
    ease 0.8 ypos 1.3
    ease 0.5 ypos 1.26
$ renpy.pause (0.7)
m "几乎立刻，她就尝试了几次浅浅的往深处深入。打了我一个措手不及，我忍不住发出了轻微的呻吟。"
c "O-Oh!"
m "安娜把这个尾巴推得更深，试图找到我深处的敏感点。"
show anna:
    ease 1.3 ypos 1.24
$ renpy.pause (2.5)
show anna:
    ease 1.7 ypos 1.3
$ renpy.pause (0.5)
m "推得更深后，到达了她尾巴的较粗部分，它开始将我的洞拉得更长。然后安娜开始往回缩。"
m "我担心她已经拔出来了，但后来她开始真正地操我，把她的尾巴来回插入我。"
play soundloop "fx/rub2.ogg" fadein 4.0
show anna:
    ease 1.2 ypos 1.26
    ease 0.8 ypos 1.29
    ease 0.9 ypos 1.24
$ renpy.pause(3.0)
show anna:
    ease 0.5 ypos 1.29
    ease 0.3 ypos 1.22
    repeat
$ renpy.pause (1.5)
c "A-Ah!"
$ renpy.pause (2.0)
m "就这样做着，没过多久，安娜就找到了我的敏感点，让我在一秒钟内更接近我的极限。"
m "然后她开始更深，直到她的尾巴把我深入得更深处，几乎是快要到达疼痛的程度。她尽可能地走得更远，直到她的汁液停止润滑。"
m "由于她尾巴的速度和深度，我的整个下半身开始感到麻木，但随着她尾巴的每一次，一股快感从我身上传来。"
m "以这个速度，我知道我不能再坚持太久了。"
show anna:
    ease 0.5 ypos 1.28
    ease 0.3 ypos 1.2
    repeat
$ renpy.pause (5.5)
stop soundloop fadeout 3.5
show anna:
    ease 0.7 ypos 1.3
    ease 0.5 ypos 1.24
    ease 1.0 ypos 1.3
    ease 0.7 ypos 1.26
    ease 1.3 ypos 1.3
    ease 1.7 ypos 1.28
    ease 1.5 ypos 1.3
$ renpy.pause (3.0)
m "但就在我快要达到极限的时候，安娜放慢了速度，然后完全收回了她的尾巴，让我接近高潮的开始慢慢消失。"
$ renpy.pause (1.5)

scene black with fade
$ renpy.pause (0.3)
scene o at Pan((0, 250), (0, 250), 0.1)
show anna smirk at center
with dissolveslow

$ renpy.pause (1.0)
if bangok_anon_anna4.playeroral == True:
    $ renpy.pause (2.5)
    c "边缘控制 {i}这{/i} 这是很残忍的."
    An smirk "行了。如果你要抱怨这么多，那么这已经足够了。"
    jump bangok_anon_anna4_playerride

else:
    c "嘿!"
    An smirk "什么？你以前没有听说过边缘控制吗？"
    c "嗯，我有......"
    An bangok blush "那就闭上你的嘴停止抱怨, 接着享受."

$ renpy.pause (1.0)
show anna normal with dissolve
$ renpy.pause (1.0)

jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_player_f_tail:

c "我能用尾巴操我吗?"
An smirk "哦。我没想到你会喜欢尾交，因为你们人类没有尾巴。不过我不是在抱怨。"

$ renpy.pause (1.0)
play sound "fx/bed.ogg"
scene bangok_anon_o_ceiling at Pan((0,360), (0,120), 2.5) with dissolvemed
$ renpy.pause (2.5)
show anna smirk at Position(ypos=1.3) with easeinbottom
m "我继续仰卧，安娜把自己放在我的双腿之间。然后她用双手握住我的腰，将尾巴指向我已经光滑的阴道。"
An "准备好了吗？"
c "是的。。。"
$ renpy.pause (0.5)
show anna:
    ease 1.0 ypos 1.26
m "然后安娜突然把尾巴伸进了我的身子。我措手不及，尾巴不断抽插, 我因为快感发出了呻吟。"
c "A-Ah!"
m "我能感觉到我的阴道在她的尾巴上向内压，用更多的汁液覆盖它，让她更容易插入我。"
$ renpy.pause (0.5)
play soundloop "fx/rub2.ogg" fadein 6.0
show anna:
    ease 0.8 ypos 1.29
    ease 1.2 ypos 1.26
    ease 0.8 ypos 1.29
    ease 0.7 ypos 1.26
$ renpy.pause (3.5)
show anna:
    ease 0.8 ypos 1.29
    ease 0.5 ypos 1.25
    repeat
m "然后她加快了步伐，尾巴的每一次抽插都让我操得更深更快。"
m "在这个新的深度，她找到了我的敏感点，现在让我更接近我的极限。"
c "Ngh…"
$ renpy.pause (4.5)
if persistent.bangok_cervpen:
    stop soundloop fadeout 3.5
    show anna:
        ease 0.8 ypos 1.29
        ease 1.2 ypos 1.25
        ease 1.3 ypos 1.29
        ease 1.6 ypos 1.25
    $ renpy.pause (3.0)
    m "突然，她的尾巴遇到了一些阻力，不是她的尾巴造成的，而是来自我的身体。她的尾巴抵在我的子宫颈上！"
    c "等-等等。你正对着我的子宫颈."
    An bangok blush "我知道"
    show anna:
        ease 1.7 ypos 1.24
    m "她只用尾巴尖戳了戳。"
    An smirk "你想让我插进去吗？"
    menu:
        "请...请你这么做...":
            $ bangok_anon_anna4.tailinwomb = True
            c "是的, 请你这么做..."
            $ renpy.pause (0.5)
            show anna:
                ease 2.0 ypos 1.22
            $ renpy.pause (0.5)
            m "她答应了，慢慢地将更多的尾巴推过我的子宫颈，在我身上发出另一股更强烈的疯狂快感，让我因为纯粹的快感而无法动弹。"
            c "A-Ah! F-Fuck!"

        "这安全吗？":
            $ bangok_anon_anna4.tailinwomb = True
            c "深入那么深安全吗？"
            An bangok blush "当然，我以前做过很多次。"
            An smirk "让我们用少量的实验，看看你的想法。"
            show anna:
                ease 2.0 ypos 1.22
            $ renpy.pause (0.5)
            m "然后安娜慢慢地将她的尾巴推过我的子宫颈，在我身上发出另一股更强烈的疯狂快感，让我无法动弹，因为纯粹的快感."
            c "A-Ah! F-Fuck!"
            $ renpy.pause (1.5)
            An "你想让我继续前进吗?"
            $ renpy.pause (1.5)
            c "是...是的..."

        "这已经够深了。":
            $ bangok_anon_anna4.tailinwomb = False
            c "不，这已经够深了......"
            An bangok blush "好吧, 既然你都这么说了."

    if bangok_anon_anna4.tailinwomb == True:
        $ renpy.pause (1.0)
        show anna smirk with dissolve
        play soundloop "fx/rub2.ogg" fadein 4.0
        show anna:
            ease 1.5 ypos 1.25
            ease 1.0 ypos 1.23
            ease 1.0 ypos 1.25
            ease 0.7 ypos 1.22
        $ renpy.pause (3.0)
        show anna:
            ease 0.7 ypos 1.25
            ease 0.4 ypos 1.2
            repeat
        m "安娜继续用她的尾巴操我，她经过我的子宫颈，现在操我的子宫，比以前更刺激。她太深了，我们伸到了她尾巴的更大的部分，它开始伸展我最外层的嘴唇，刚好快到要疼痛的点了."
        m "我不知道我还能坚持多久，但时间不长。"
        $ renpy.pause (4.0)
     
    else:
        $ renpy.pause (1.0)
        show anna smirk with dissolve
        play soundloop "fx/rub2.ogg" fadein 4.0
        show anna:
            ease 1.5 ypos 1.29
            ease 1.0 ypos 1.27
            ease 1.0 ypos 1.29
            ease 0.7 ypos 1.25
        $ renpy.pause (3.0)
        show anna:
            ease 0.7 ypos 1.29
            ease 0.4 ypos 1.23
            repeat
        m "安娜继续用她的尾巴操我。但她没有穿过我的子宫颈，而是在它之前开始盘绕她的尾巴，让我接受更多，并开始伸展我的外阴，但只是靠近疼痛的点。"
        m "在这个更令人愉快的姿势下，我知道我撑不了多久了。"
        $ renpy.pause (4.5)

    show black with fadequick
    stop soundloop fadeout 1.5
    m "突然，我的通道地紧紧地咬住了她的尾巴，用我更多的汁液浸湿了它。"
    if bangok_anon_anna4.tailinwomb == True:
        show anna at Position(ypos=1.2) with ease
    else:
        show anna at Position(ypos=1.23) with ease
    $ renpy.pause (1.5)
    hide black with dissolveslow
    m "安娜在我高潮后给了我一会儿时间，然后从我手中接过她的尾巴。"
    if bangok_anon_anna4.tailinwomb == True:
        $ renpy.pause (0.5)
        show anna:
            ease 2.0 ypos 1.25
        $ renpy.pause (2.0)
        m "当我的子宫颈在她的尾巴上闭合时，她十分地小心，但这种感觉仍然让我微妙地喘息。"
        show anna:
            ease 1.4 ypos 1.3
        $ renpy.pause (2.0)

    else:
        $ renpy.pause (0.5)
        show anna:
            ease 1.4 ypos 1.3
        $ renpy.pause (2.0)

else:
    stop soundloop fadeout 4.5
    show anna:
        ease 0.8 ypos 1.29
        ease 1.2 ypos 1.25
        ease 1.3 ypos 1.29
        ease 1.6 ypos 1.25
    $ renpy.pause (3.0)
    m "安娜试着把尾巴推得更深，但还是遇到了一些阻力，不是她的尾巴造成的，而是来自我的身体。她的尾巴抵在我的子宫颈上!"
    c "等-等等。你正对着我的子宫颈。"
    An bangok blush "好吧，那我就不深入了。"
    c "是的，谢谢......"
    $ renpy.pause (1.0)
    An smirk "其实，我可能有一个主意。"
    c "干什么。。。?"
    $ renpy.pause (0.5)
    show anna:
        ease 1.3 ypos 1.23
    m "安娜没有试图更深入，而是开始盘绕她的尾巴，让我接受更多，并开始伸展我的小穴，但只是接近疼痛的程度。"
    c "O-Oh!"
    $ renpy.pause (0.5)
    play soundloop "fx/rub2.ogg" fadein 5.0
    show anna:
        ease 1.0 ypos 1.29
        ease 0.7 ypos 1.25
        ease 0.7 ypos 1.29
        ease 0.5 ypos 1.25
    $ renpy.pause (3.0)
    show anna:
        ease 0.6 ypos 1.29
        ease 0.3 ypos 1.23
        repeat
    m "在安娜卷起尾巴的这种更愉快的姿势下，我知道我撑不了多久了。"
    $ renpy.pause (4.0)
    show black with fadequick
    stop soundloop fadeout 1.5
    show anna at Position(ypos=1.23) with ease
    m "突然，我的通道地咬住了她的尾巴，用我更多的汁液浸湿了它。"
    $ renpy.pause (1.5)
    hide black with dissolveslow
    m "安娜在我高潮后给了我一会儿时间，然后从我手中接过她的尾巴。"
    $ renpy.pause (0.5)
    show anna:
        ease 1.4 ypos 1.3
    $ renpy.pause (2.0)


    
scene black with fadequick
$ renpy.pause (0.3)
scene o at Pan((0, 250), (0, 250), 0.1)
show anna smirk at center
with dissolveslow
$ renpy.pause (0.5)
An "我觉得你喜欢吗？"
c "远不止享受."
An "很高兴听到."

$ renpy.pause (1.5)
show anna bangok blush with dissolve
$ renpy.pause (1.5)


jump bangok_anon_anna4_beforemenu



label bangok_anon_anna4_playerride:

c "(这就是她认为的前戏？)"
$ renpy.pause (1.0)
play sound "fx/bed.ogg"
scene bangok_anon_o_ceiling at Pan((0,360), (0,120), 2.0) with dissolvemed
$ renpy.pause (2.5)
show anna smirk at Position(ypos=1.25) with easeinbottom
show anna:
    ease 1.5 ypos 1.2 zoom 1.2
$ renpy.pause (1.0)
m "安娜向我投去欲望的怒视，她坐在我身上，把我夹在她的双腿之间，用她的缝隙对准我的尖端，然后抓住我的肩膀，把我压在床上。"
if persistent.bangok_knot == True and bangok_four_anna2.unplayed == False:
    An bangok blush "只是为了确认一下，人类没有结，对吧？"
    c "呃，不是吗？"
    An smirk "好."
    $ renpy.pause (0.5)

$ renpy.pause (1.5)
show anna:
    ease 1.3 ypos 1.24
m "然后她把臀部放到我身上。有点令人失望的是，没有太多的抵抗，但她的内心却感到异常潮湿和炎热，她显然从她对我们之前的前戏的感知中非常兴奋。"
show anna:
    ease 1.2 ypos 1.2
    ease 1.0 ypos 1.24
$ renpy.pause (0.5)
show anna:
    ease 1.0 ypos 1.2
    ease 0.8 ypos 1.24
    repeat
$ renpy.pause (1.0)
m "然后她应该算是开始骑我."
m "她开始慢慢地，开始在我身上上下"
$ renpy.pause (4.0)
play soundloop "fx/rub2.ogg" fadein 5.0
show anna:
    ease 0.8 ypos 1.2
    ease 0.8 ypos 1.26
$ renpy.pause (1.5)
show anna:
    ease 0.7 ypos 1.2
    ease 0.5 ypos 1.28
    repeat
m "然后她开始加快步伐，向后倾斜，所以她的大部分体重都在我的骨盆上，在她和我一起动的时候，把我牢牢地固定在床上。"
m "她现在在我的长度允许的范围内尽可能多地吸收我，她滴水的阴道使我几乎毫不费力地插入她，甚至更加刺激。"
m "每次她向下推时，我都感觉到她的臀部拍打着我自己的臀部，每次都在我身上发出一波又一波的快感。"
An bangok lipbite "Mmh…"
$ renpy.pause (3.0)
m "然后，随着她越来越投入，我很享受她骑着我时她的缝隙开始收紧我下面的感觉。我忍不住发出了一声快乐的呻吟。"
c "A-Ah!"
$ renpy.pause (4.5)
show anna:
    ease 0.5 ypos 1.2
    ease 0.3 ypos 1.28
    repeat
m "突然间，安娜骑着我变得更加狂野和有活力。她开始更快地操我，她对我肩膀的抓握越来越紧，以至于她的爪子开始挖我的皮肤，但谢天谢地，还不足以伤害我。"
An "Ngh…"
m "我现在不仅感受到了被骑的乐趣，还感受到了危险的快感。"
$ renpy.pause (4.0)
m "尽管是为更大的伴侣准备的，但我仍然感觉到她的小穴挤压在我的下体上，她身体内在的肌肉以一种无所不包的温暖按摩着它。"
m "在那一刻，我知道我不能再坚持太久了。"
c "A-Anna…"
An "Almost…"
$ renpy.pause (4.0)
play sound "fx/varagrowl.ogg"
m "然后，安娜发出了一声声音，不是呻吟，而是咆哮。不是侵略性的，而是强度的，进一步巩固了这样的快感。"
$ renpy.pause (3.5)
play sound "fx/extinguish.ogg"
show black with fadequick
m "我再也忍不住高潮了，忍不住把我的精液射进了她体内。"
$ renpy.pause (2.5)
hide black with dissolveslow
$ renpy.pause (0.5)
m "而高潮过后我仍然坚硬的短暂时期，足以让安娜也达到她的极限。"
show anna:
    ease 0.4 ypos 1.28
stop soundloop fadeout 0.5
play sound "fx/snarl.ogg"
show anna bangok orgasm with dissolve
m "然后安娜把她的重量放在我身上，发出一声咆哮。她的耳阴道夹住了我的会员，并用她的汁液浸湿了她和我的腹股沟。"
$ renpy.pause (2.0)
show anna bangok lipbite with dissolve
m "然后我们在那里呆了一会儿，安娜仍然在我身上，我们俩都沐浴在余晖中。"
$ renpy.pause (2.0)
scene black with fadequick
$ renpy.pause (0.3)
scene o at Pan((0, 250), (0, 250), 0.1) with dissolveslow
show anna smirk at center with dissolveslow
$ renpy.pause (0.5)
m "等到安娜的小穴完全放松后，她从我身上下来，然后倒在我旁边，我们俩并排躺在床上。"
$ renpy.pause (1.5)

jump bangok_anon_anna4_afterglow



label bangok_anon_anna4_afterglow:

An smirk "天哪。"
$ renpy.pause (1.5)
if bangok_four_anna2.unplayed == False:
    An "这比上次好多了。"
    if bangok_four_anna2.annacomment == "adorable":
        c "你刚才说我不能让你下去，{i}就那件事吗？{/i}"
        An "哦他妈的闭嘴."
    elif bangok_four_anna2.annacomment == "small":
        c "你说我太小了吗？"
        An "哦他妈的闭嘴."
    else:
        pass
        
    $ renpy.pause (1.0)
    c "是什么让这次变得更好？"
    if bangok_four_anna1_sexrequested == True:
        An sad "好吧，上次只是为了你的赌注结束。我这样做不是为了我自己，我只是想让你下车，这样你就不会抱怨太多，也不会在你来参加这些测试时引起注意。"
    else:
        An sad "好吧，上次真的只是一时冲动而已。而且我真的不是为了我自己，我只是想确保你对我们的交易结果感到满意，这样你就不会抱怨太多，也不会在你来参加这些测试时引起注意。"

    An smirk "不过这一次呢？纯粹的快乐."

else:
    An "这比我想象的要好得多。"
    if bangok_four_playerhasdick == True:
        c "你说我比你习惯的要小吗？"
        An "哦他妈的闭嘴."

An bangok blush "老实说，我几乎忘记了当你出于匮乏而做爱时，性生活会好得多，而不是为了交易的一部分或操纵某人。"
c "我不知道如何回应。"
An normal "那就不要了。我需要休息，我已经筋疲力尽了。"

$ renpy.pause (2.5)
c "(我们现在只是紧挨着躺着，我应该做点什么吗？)"
menu:
    "[[什么都不做.]":
        m "我不想试图推动任何东西并破坏这一刻，所以我只是呆在床边。"
        m "很快，我就睡着了，仍然感觉到余晖的温暖。"
        scene black with dissolveslow
        $ renpy.pause (1.0)

    "[[试着拥抱.]":
        m "我走近了，把头靠在安娜的胸膛上。她没有说任何鼓励我继续的话，但她也没有反对。"
        $ renpy.pause (2.0)
        show anna smirk with dissolve
        m "然后她试图巧妙地用一只胳膊搂住我的背，我把这当作继续的信号。"
        m "现在，在一个更舒适的怀抱中，我仍然感受到余晖的温暖，我进入了平静的睡眠。"
        scene black with dissolveslow
        $ renpy.pause (1.0)
        play sound "fx/purr.ogg" fadein 3.0
        $ renpy.pause (7.0)
        stop sound fadeout 4.0

$ renpy.pause (3.0)

$ mp.annaromance = True
$ mp.save()
$ annastatus = "good"
$ annascenesfinished = 4
stop music fadeout 2.0
$ renpy.pause (0.5)
jump _mod_fixjmp

