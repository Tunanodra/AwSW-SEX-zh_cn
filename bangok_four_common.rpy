init python:
    # Common game variables
    bangok_four_malepartners = 0
    bangok_four_femalepartners = 0
    bangok_four_playerhasdick = None
    bangok_four_hornincident = False

init python in bangok_four_common:
    import bangok_four
    renpy.pure('bangok_four_common.bangok_four.fetish_count')
    renpy.pure('bangok_four_common.bangok_four.fetish_iter')

    import bangok_four.trackcursor
    TrackCursor = bangok_four.trackcursor.TrackCursor

    import bangok_four.moredisplayables as md
    PersistentConditionalDisplayable = md.PersistentConditionalDisplayable
    LayeredImage = md.layeredimage.LayeredImage
    Always = md.layeredimage.Always
    Attribute = md.layeredimage.Attribute
    Condition = md.layeredimage.Condition
    PersistentConditionalLayer = md.PersistentConditionalLayer
    PersistentConditionalComposite = md.PersistentConditionalComposite

    import bangok_four.bangnokay as bangnokay

    @renpy.pure
    def bangnokay_quest_text(stage):
        if not stage:
            return _("Bang? No, Kay 设置")
        if stage < 2:
            return _("No Bang, Kay?")
        if stage < 3:
            return _("我们不会做的, 好吗?")
        if stage < 4:
            return _("等等, 不, 不做.")
        if stage < 5:
            return _("你在试图关闭这个？")
        if stage < 6:
            return _("但愚蠢的精神！")
        return _("好吧, 好吧. 下一次点击.")



init:
    # 设置菜单
    style bangok_four_switch is image_button:
        activate_sound "se/sounds/yes.wav"
        hover_sound "se/sounds/select.ogg"

    style bangok_four_smallwindowclose is smallwindowclose:
        activate_sound "se/sounds/close.ogg"
        hover_sound "se/sounds/select.ogg"

    style bangok_four_close is button:
        activate_sound "se/sounds/close.ogg"
        hover_sound "se/sounds/select.ogg"

    screen bangok_modsettings():
        default bangok_four_bangnokay_quest=0
        tag smallscreen2
        modal True
        window id "bangok_modsettings" at popup2:
            style "smallwindow_big2"
            if bangok_four_common.bangnokay.check():
                textbutton bangok_four_common.bangnokay_quest_text(bangok_four_bangnokay_quest):
                    yalign 0.06
                    xalign 0.5
                    text_size 44
                    action [
                        Function(bangok_four_common.bangnokay.set_bangnokay, (bangok_four_bangnokay_quest<6)),
                        SetScreenVariable('bangok_four_bangnokay_quest', ((bangok_four_bangnokay_quest+1)%7)),
                    ]
                    style "bangok_four_switch"
            else:
                textbutton "BangOk 设置":
                    yalign 0.06
                    xalign 0.5
                    text_size 44
                    action Function(bangok_four_common.bangnokay.set_bangnokay, True)
                    style "bangok_four_switch"


            if not persistent.nsfwtoggle:
                vbox:
                    text "这个mod的内容主要是" xalign 0.5
                    text "---- 成人内容 ----" xalign 0.5
                    text "重新启用成人场景或卸载此mod." xalign 0.5
                    text "禁用成人场景时，此mod并不保证所有的成人内容都不可访问，尽管已经尽力." xalign 0.5
            else:
                vbox:
                    align (0.5, 0.3)
                    if bangok_four_common.bangnokay.bangnokay_raw:
                        text "可爱的按钮:" xalign 0.5
                    else:
                        text "癖好:" xalign 0.5
                        text "如果你不知道一个选项的含义，保持未选中状态（或自行查阅）.":
                            xalign 0.5
                            size 32

                    grid ((bangok_four_common.bangok_four.fetish_count(bangok_four_common.bangnokay.bangnokay_raw)+1)//2) 2:
                        align (0.5,0.5)
                        transpose True
                        spacing 10
                        for fetish in bangok_four_common.bangok_four.fetish_iter(bangok_four_common.bangnokay.bangnokay_raw):
                            vbox:
                                add fetish.get_switch(bangok_four_common.bangnokay.bangnokay_raw)
                                showif bangok_four_common.bangnokay.bangnokay_raw:
                                    text "[fetish.clean_label]"
                                showif not (bangok_four_common.bangnokay.bangnokay_raw):
                                    text "[fetish.label]"
                        if bangok_four_common.bangok_four.fetish_count(bangok_four_common.bangnokay.bangnokay_raw) % 2 == 1:
                            null

                hbox:
                    xalign 0.5
                    yalign 0.8
                    spacing 20
                    imagebutton:
                        idle im.Scale("ui/nsfw_chbox-unchecked.png", 55, 55)
                        hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 55, 55), 64, 64, 64)
                        selected_idle im.Scale("ui/nsfw_chbox-checked.png", 55, 55)
                        selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 55, 55), 64, 64, 64)
                        action MTSTogglePersistentBool('bangok_dev')
                        style "bangok_four_switch"
                        focus_mask None
                    text "危险: 启用开发中的场景"

                showif persistent.bangok_dev == True and not (bangok_four_common.bangnokay.bangnokay_raw):
                    text "开发中的场景可能没有结局，并且 {i}会{/i}有导致崩溃的路径.":
                        yalign 0.875
                        xalign 0.5
                        size 40

            showif persistent.bangok_dev == True and main_menu and not (bangok_four_common.bangnokay.bangnokay_raw):
                textbutton "[[重放首次启动体验.]":
                    xalign 0.5 
                    yalign 1.1
                    action [Hide("bangok_modsettings"), Start("bangok_four_mod_firstboot")]
                    style "bangok_four_close"

            imagebutton:
                idle "image/ui/close_idle.png"
                hover "image/ui/close_hover.png"
                action [Hide("bangok_modsettings"), Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")]
                hovered Play("audio", "se/sounds/select.ogg")
                style "bangok_four_smallwindowclose"
                at nav_button

    # 场景
    image bangok_anon_o_ceiling = "bg/in/apts/o_ceil.png"
    
    image bangok_four_bryce1_apartment night = "bg/in/apts/pad_night.png"
    image bangok_four_bryce1_apartment night ceiling = "bg/in/apts/pad_night_ceil.png"

    image bangok_four_xipsum_bedroom normal = "bg/in/apts/ipsum_bedroom.png"
    image bangok_four_xipsum_bedroom_bed = "bg/in/apts/ipsum_bedroom_bed.png"
    image bangok_four_xipsum_bedroom ceiling = "bg/in/apts/ipsum_bedroom_ceiling.png"

    image bangok_four_xsebastian_cave2_dk = im.Recolor("bg/in/cave2_dk.png", 70, 70, 100, 255)

    image bangok_four_library night = im.Recolor("bg/in/bangok_library_night.png", 70, 70, 100, 255)
    image bangok_four_library outside night = im.Recolor("bg/out/town/town5.jpg", 60, 70, 100, 255)

    image bangok_anoney_library_corridor_night = "bg/in/bangok/library_corridor_night.png"
    image bangok_anoney_emeraroom_night = "bg/in/bangok/bangok_anoney_emeraroom_night.png"

    image bangok_four_labdoor = "bg/in/bangok/labdoor.png"
    image bangok_four_labdoor dk = im.Recolor("bg/in/bangok/labdoor.png", 60, 70, 100, 255)
    image bangok_four_labdoor dk track = bangok_four_common.TrackCursor(
        im.Recolor("bg/in/bangok/labdoor.png", 60, 70, 100, 255),
        posxmin=-8, posxmax=42,
        posymin=-40, posymax=40)

    image bangok_four_officedoor = "bg/in/bangok/officedoor.png"
    image bangok_four_officedoor track = bangok_four_common.TrackCursor(
        "bg/in/bangok/officedoor.png",
        posxmin=0, posxmax=16,
        posymin=0, posymax=40)


    # CGs
    image bangok_four_xipsum_afterglow = "cg/lorem-x-ipsum_purpleroom.png"


    image bangok_four_annaxdamion = bangok_four_common.LayeredImage([
        bangok_four_common.Always("cg/bangok/annaxdamion_lab/base.png"),
        bangok_four_common.PersistentConditionalLayer(
            'bangok_cloacas', None,
            None, "cg/bangok/annaxdamion_lab/vaginal.png",
            pos=(-68, 130)
        ),
        bangok_four_common.Attribute('bulge','bulge', "cg/bangok/annaxdamion_lab/bulge.png"),
        bangok_four_common.Attribute('cum', 'cum',
            bangok_four_common.PersistentConditionalDisplayable(
                'bangok_cloacas', "cg/bangok/annaxdamion_lab/cloacal_cum.png",
                None, "cg/bangok/annaxdamion_lab/vaginal_cum.png",
            ),
            if_not=['bulge'],
            pos=(-68, 130),
        ),
        bangok_four_common.Attribute('cum', 'cum',
            im.Composite((1280,988),
                (0,0),"cg/bangok/annaxdamion_lab/cloacal_cum.png",
                (0,0),"cg/bangok/annaxdamion_lab/vaginal_cum.png",
            ),
            if_all=['bulge'],
            pos=(-68, 130),
        ),
        bangok_four_common.PersistentConditionalLayer(
            ('bangok_balls', 'bangok_inflation'), "cg/bangok/annaxdamion_lab/dm_ballz_big.png",
            'bangok_balls', "cg/bangok/annaxdamion_lab/dm_ballz.png",
            None, None
        ),
    ])


    image bangok_four_brycexsebastian = bangok_four_common.LayeredImage([
        bangok_four_common.Always("cg/bangok/brycexsebastian_office/officecut.jpg"),
        bangok_four_common.Attribute('frame',        'frameA', "cg/bangok/brycexsebastian_office/frameA_base.png"),
        bangok_four_common.Attribute('frame',        'frameB', "cg/bangok/brycexsebastian_office/frameB_base.png"),
        bangok_four_common.PersistentConditionalLayer(
            'bangok_balls', "cg/bangok/brycexsebastian_office/frameA_balls.png",
            None, None,
            if_all=['frameA']
        ),
        bangok_four_common.PersistentConditionalLayer(
            'bangok_balls', "cg/bangok/brycexsebastian_office/frameB_balls.png",
            None, None,
            if_all=['frameB']
        ),
        bangok_four_common.Attribute('bryceeye',     'bryceeyeclosed', "cg/bangok/brycexsebastian_office/bryceeyeclosed.png"),
        bangok_four_common.Attribute('bryceeye',     'bryceeyeopen', "cg/bangok/brycexsebastian_office/bryceeyeopen.png"),
        bangok_four_common.Attribute('bryceeye',     'bryceeyeroll', "cg/bangok/brycexsebastian_office/bryceeyeroll.png"),
        bangok_four_common.Attribute('brycemouth',   'brycesmile', "cg/bangok/brycexsebastian_office/brycesmile.png"),
        bangok_four_common.Attribute('cumspill',     'nocum',
            bangok_four_common.PersistentConditionalDisplayable(
                'bangok_balls', "cg/bangok/brycexsebastian_office/frameB_cumcoverup_balls.png",
                None, "cg/bangok/brycexsebastian_office/frameB_cumcoverup.png",
            ),
            default=True,
            if_all=['frameB']
        ),
        bangok_four_common.Attribute('cumspill',     'cum', renpy.display.layout.Null(), if_all=['frameB']),
        bangok_four_common.Attribute('cumspill',     'morecum', "cg/bangok/brycexsebastian_office/frameB_cumspill+.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebcheek',     'sebcheekbulge', "cg/bangok/brycexsebastian_office/frameB_sebcheekbulge.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebthroat',    'sebthroatbulge', "cg/bangok/brycexsebastian_office/frameB_sebthroatbulge.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebeye',       'sebeyeopen', "cg/bangok/brycexsebastian_office/frameB_sebeyeopen.png", if_all=['frameB']),
        bangok_four_common.Attribute('sebeye',       'sebeyeshocked', "cg/bangok/brycexsebastian_office/frameB_sebeyeshocked.png", if_all=['frameB']),
    ])
    image bangok_four_brycexsebastian_lickpanel = bangok_four_common.PersistentConditionalComposite((1920,1200),
        (0,0),"cg/bangok/brycexsebastian_office/lickpanel.png",
        (0,0),bangok_four_common.PersistentConditionalDisplayable('bangok_balls', "cg/bangok/brycexsebastian_office/lickpanel_balls.png", None, None),
    )

    image bangok_four_brycexsebastian animate bryceclosedsmile sebastianopen:
        "bangok_four_brycexsebastian frameA bryceeyeclosed brycesmile sebeyeopen"
        "bangok_four_brycexsebastian frameB bryceeyeclosed brycesmile sebeyeopen" with dissolve
        pause 1.5
        "bangok_four_brycexsebastian frameA bryceeyeclosed brycesmile sebeyeopen" with dissolve
        pause 1.5
        repeat
    image bangok_four_brycexsebastian animate bryceclosed:
        "bangok_four_brycexsebastian frameA bryceeyeclosed"
        "bangok_four_brycexsebastian frameB bryceeyeclosed" with dissolve
        pause 1.5
        "bangok_four_brycexsebastian frameA bryceeyeclosed" with dissolve
        pause 1.5
        repeat

    image bangok_anoney_emera_sofa = "cg/bangok/xemera2/bangok_anoney_emera_sofa.png"
    image bangok_anoney_emera_presenting = "cg/bangok/xemera2/bangok_anoney_emera_presenting.png"
    image bangok_anoney_emeramassage_night = "cg/bangok/xemera2/bangok_anoney_emeramassage_night.png"


    # 人物
    image adineshower blush = im.Composite(
        (3000,1688),
        (0,0), "cg/chap4/adineshower.jpg",
        (0,0), "cg/bangok/adineshower/adineshower_blush.png",
    )
    image adineshower think = im.Composite(
        (3000,1688),
        (0,0), "cg/chap4/adineshower.jpg",
        (0,0), "cg/bangok/adineshower/adineshower_think.png",
    )
    image adineshower thinkblush = im.Composite(
        (3000,1688),
        (0,0), "cg/chap4/adineshower.jpg",
        (0,0), "cg/bangok/adineshower/adineshower_blush.png",
        (0,0), "cg/bangok/adineshower/adineshower_think.png",
    )
    image adineshower annoyedblush = im.Composite(
        (3000,1688),
        (0,0), "cg/chap4/adineshower.jpg",
        (0,0), "cg/bangok/adineshower/adineshower_blush.png",
        (0,0), "cg/bangok/adineshower/adineshower_annoyed.png",
    )


label bangok_four_mod_firstboot:
    $ _skipping = False
    stop music
    scene black with dissolve
    play sound "fx/system3.wav"
    s "正在初始化mod \"BangOk\"{cps=2}...{/cps}{w=0.5}{nw}"
    s "正在初始化mod \"BangOk\"... {fast}完成!"
    $ _skipping = True
    s "BangOk改变目标坐标至多个不同的宇宙，具有稍微不同的龙类生物学和性癖偏好."
    s "你想现在配置这些坐标，还是接受最原始、最接近人类的默认设置?"
    menu:
        "是的，我现在想配置我的BangOk癖好.":
            show screen bangok_modsettings
        "不，我稍后会在设置菜单中进行配置.":
            pass
    s "重新计算到达坐标.{cps=2}..{/cps} (关闭所有菜单以继续.)"
    play sound "fx/system.wav"
    s "计算完成."
    s "BangOk模块已添加至你的 {i}设置{/i} 菜单下的 {i}Mod 设置.{/i} 你可以在 {i}任何时候{/i} 修改你的坐标，但在某些...活动进行中修改可能会导致时间线不稳定."
    $ persistent.bangok_four_menu_firstboot_complete = True
    s "返回主菜单初始化.{cps=2}..{/cps}{w=0.5}{nw}"
    jump bangok_four_mod_firstboot_return

label bangok_four_bangnokay_kill_replay:
    play sound "fx/system3.wav"
    s "哎呀! 这里没有什么可看的."
    play sound "fx/system3.wav"
    s "让我把这个清理干净..."
    $ renpy.end_replay()
    jump ml_main_menu