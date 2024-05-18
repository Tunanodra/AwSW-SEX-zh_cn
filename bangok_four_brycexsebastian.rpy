##################### NOTICE #####################
# Per request from the artist of the work forming
#  the basis of this scene, absolutely no water-
#  -sports (nor any mention thereof) is to be
#  added to this scene.

if bangok_four_common.bangnokay.check():
    jump bangok_four_brycexsebastian_abort_merge

m "然而，在我进入布莱斯的办公室之前，我听到了里面传来的沉重呼吸声，还有低语。"

menu:
    "靠近听。"：
        pass
    "稍后再来。"：
        m "不想打扰他们，我决定在站里等到声音停止，或者有人出来迎接我。"
        jump bangok_four_brycexsebastian_abort_merge

m "我走近了一些，靠近那扇微微开着的门，试图听清楚里面的动静。"

Br pantflirt "嗯... 就是这种深度。"  # 副驾驶的建议: "嗯... 我真高兴你在这里，塞巴斯蒂安。"
m "接着是湿润的“咯”声，像是有人在窒息。"
stop soundloop fadeout 0.8
$ renpy.pause (0.8)
Br brow "你还好吧？"
Sb shy "嗯... 只是弄错了地方。"

menu:
    "窥视。"：
        pass
    "稍后再来。"：
        m "不想打扰他们，我决定在站里等到布莱斯和塞巴斯蒂安结束。"
        jump bangok_four_brycexsebastian_abort_merge

$ renpy.pause (0.5)
# TODO: 显示布莱斯和塞巴斯蒂安
scene bangok_four_brycexsebastian frameA:
    zoom 0.9
    xpos 600
    linear 1.0 xpos 400
    xpos 400
show white:
    alpha 1.0
    ease 1.0 alpha 0.0
    alpha 0.0
show bangok_four_officedoor track:
    anchor (0, 0)
    pos (-800, -6600)
    zoom 9.0
    ease 1.0 zoom 10.0 xpos -1100
    zoom 10.0
    xpos -1100
with dissolvemed
$ renpy.pause (0.5)
hide white with None

Br flirty "现在好了？"
Sb smile "嗯。"
Br flirty "那么我可以..."
show bangok_four_brycexsebastian frameB brycesmile bryceeyeopen with dissolve

m "毫无疑问，他们正在做的是私密的事。站在走廊里，有人可能会看到我并告诉他们。"
m "那样他们就会知道我一直在看。"

menu:
    "留下。"：
        pass
    "稍后再来。"：
        show black with dissolveslow
        m "让他们继续，我决定在站里等到布莱斯和塞巴斯蒂安结束。"
        jump bangok_four_brycexsebastian_abort_merge

show bangok_four_brycexsebastian frameA with dissolve

show bangok_four_officedoor track:
    zoom 10.0
    pos (-1100, -6600)
    ease 0.5 zoom 15.0 pos (-2200, -9900)
    zoom 15.0
    pos (-2200, -9900)
show bangok_four_brycexsebastian frameA:
    xpos 400
    ease 0.5 xpos 200
    xpos 200
with None

m "我调整了位置，毫不羞愧地从门缝更近的位置窥视。"

Br normal "这样行吗？"
Sb smile "嗯嗯。"
Br smirk "好吧，我还有一个想法..."
Br flirty "你觉得你能把我的所有精华都吞下去，不吞咽吗？"
Sb shy "嗯？！"
$ renpy.pause (0.8)
Sb smile "嗯嗯。"
Br laugh "我们来试试。"
Br pantflirt "现在让我再进去一点。"

play soundloop "fx/breathing.ogg" fadein 2.0
show bangok_four_brycexsebastian animate bryceclosedsmile sebastianopen with None
$ renpy.pause (6.0)
Br laugh "好孩子。"
$ renpy.pause (6.0)
show bangok_four_brycexsebastian animate bryceclosed with None
$ renpy.pause(0.8)
Br laugh "天哪，我太需要这个了。"
Br flirty "谢谢你，塞巴斯蒂安。"
Sb smile "嗯..."
$ renpy.pause (4.0)
Br smirk "准备好测试你的容量了吗？"
$ renpy.pause (0.5)
stop soundloop fadeout 0.5
play sound "fx/snarl.ogg"
show bangok_four_brycexsebastian frameB nocum with dissolve
$ renpy.pause (0.8)
show bangok_four_brycexsebastian frameB cum with dissolve
Sb shy "咯！"
$ renpy.pause (0.5)
if persistent.bangok_inflation == True:
    show bangok_four_brycexsebastian frameB sebcheekbulge sebthroatbulge sebeyeshocked morecum with dissolve
    Sb shy "咯。"
    show bangok_four_brycexsebastian frameB sebcheekbulge sebthroatbulge morecum with dissolve
    $ renpy.pause (0.5)
    Br pantflirt "现在吞下去。"
    play sound "fx/gulpslow2.wav" fadein 0.5
    $ renpy.pause (0.5)
    show bangok_four_brycexsebastian frameB bryceeyeroll brycesmile sebcheekbulge morecum with dissolve
    $ renpy.pause (0.5)
    show bangok_four_brycexsebastian frameB bryceeyeroll brycesmile morecum with dissolve
    $ renpy.pause (0.6)
    show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile sebeyeopen morecum with dissolve
    $ renpy.pause (0.3)
    stop sound fadeout 0.5

    Br smirk "不是我泼冷水，但看起来你需要多练习。"
    show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile morecum with dissolve
else:
    $ renpy.pause (0.5)
    Br pantflirt "现在吞下去。"
    play sound "fx/gulpslow2.wav" fadein 0.5
    show bangok_four_brycexsebastian frameB bryceeyeroll brycesmile cum with dissolve
    $ renpy.pause(4.5)
    show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile sebeyeopen cum with dissolve
    stop sound fadeout 0.5

    Br brow "那么，你洒了多少？"
    Br smirk "哦。"
    Br smirk "不是我泼冷水，但看起来你需要多练习。"


show bangok_four_brycexsebastian_lickpanel:
    zoom 0.9
    xpos 200
    ypos -200
    linear 2.0 ypos 0
    ypos 0
with dissolveslow
$ renpy.pause (1.0)
Br smirk "现在把它舔干净..."
$ renpy.pause (2.0)

show bangok_four_brycexsebastian frameB bryceeyeopen sebeyeshocked cum with dissolve

Br brow "呃... 我会给你拿条毛巾，但你得先解开这些手铐。"  # 副驾驶的建议: "呃... 你得暂时少吃点东西。"

show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile sebeyeshocked cum with dissolve
Br smirk "如果你再吞一次，这应该能给你更多的手臂长度。"
Sb drop "等等--"

hide bangok_four_brycexsebastian_lickpanel
show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile sebeyeshocked cum
with dissolve

$ renpy.pause (0.8)

show bangok_four_brycexsebastian frameB bryceeyeopen brycesmile sebeyeopen cum with dissolve

Sb disapproval "咯。"
Br brow "什么？"

scene black with dissolve

m "当布莱斯转过身看向塞巴斯蒂安时，我赶紧躲开，免得他的目光扫到门口。"

Sb drop "我把手铐的钥匙掉了。"
Br laugh "在哪儿？"
Sb drop "我不知道！当你在的时候它弹到了你的背上..."
Br smirk "好吧，好吧。小声点。看来你得多粘在我身上多一会儿了。"
Sb disapproval "我相信你会喜欢的。"
Br laugh "当然！"

m "趁他们在找钥匙时，我悄悄地溜回了警局的入口。"
jump bangok_four_brycexsebastian_abort_merge