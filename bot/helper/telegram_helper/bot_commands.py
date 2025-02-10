# ruff: noqa: RUF012
from bot.core.config_manager import Config

i = Config.CMD_SUFFIX


class BotCommands:
    StartCommand = "start"
    MirrorCommand = [f"mirror{i}", f"Mirror{i}", f"m{i}", f"M{i}"]
    JdMirrorCommand = [f"jdmirror{i}", f"jm{i}"]
    YtdlCommand = [f"ytmirror{i}", f"ym{i}", f"Ym{i}"]
    LeechCommand = [f"leech{i}", f"Leech{i}", f"l{i}", f"L{i}", "rssl"]
    JdLeechCommand = [f"jdleech{i}", f"jl{i}"]
    YtdlLeechCommand = [f"ytleech{i}", f"yl{i}", f"Yl{i}"]
    CloneCommand = f"clone{i}"
    MediaInfoCommand = [f"mediainfo{i}", f"mi{i}", f"Mi{i}"]
    CountCommand = f"count{i}"
    DeleteCommand = f"del{i}"
    CancelAllCommand = f"cancelall{i}"
    ForceStartCommand = [f"forcestart{i}", f"fs{i}"]
    ListCommand = f"list{i}"
    SearchCommand = f"search{i}"
    StatusCommand = [f"status{i}", f"s{i}", f"S{i}"]
    UsersCommand = f"users{i}"
    AuthorizeCommand = [f"authorize{i}", f"a{i}", f"A{i}"]
    UnAuthorizeCommand = [f"unauthorize{i}", f"ua{i}", f"Ua{i}"]
    AddSudoCommand = f"addsudo{i}"
    RmSudoCommand = f"rmsudo{i}"
    PingCommand = f"ping{i}"
    RestartCommand = [f"restart{i}", f"r{i}", f"R{i}"]
    RestartSessionsCommand = [f"restartses{i}", f"rs{i}"]
    StatsCommand = f"stats{i}"
    HelpCommand = [f"help{i}", f"Help{i}", f"h{i}", f"H{i}"]
    LogCommand = f"log{i}"
    ShellCommand = f"shell{i}"
    AExecCommand = f"aexec{i}"
    ExecCommand = f"exec{i}"
    ClearLocalsCommand = f"clearlocals{i}"
    BotSetCommand = [f"botsettings{i}", f"Botsettings{i}", f"bs{i}", f"Bs{i}"]
    UserSetCommand = [f"usetting{i}", f"Usetting{i}" f"us{i}", f"Us{i}"]
    SpeedTest = [f"speedtest{i}", f"sp{i}", f"Sp{i}"]
    BroadcastCommand = [f"broadcast{i}", "broadcastall"]
    SelectCommand = f"sel{i}"
    RssCommand = f"rss{i}"
