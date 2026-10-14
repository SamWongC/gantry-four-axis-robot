# Software Guide

This directory preserves historical code. It has not been retested with the device or functionally refactored.

| Path | Role |
| --- | --- |
| `host-app/scara_host_app.py` | GUI entry point |
| `host-app/pyside6_app.py` | Base PySide6 interface logic |
| `host-app/scara_host_app.ui` | Qt interface source |
| `host-app/scara_host_app_ui.py` | Generated interface code, retained because the current program imports it directly |
| `host-app/scara_app.py` | Robot control logic |
| `host-app/scara_serial.py`, `host-app/base_serial.py` | Serial communication |
| `host-app/main.py`, `host-app/v_plan.py` | Historical motion-planning and debugging code with absolute paths from the original computer. Update these before using the corresponding experiments. |
| `host-app/二自由度.py`, `host-app/二自由度(1).py` | Workspace calculation scripts retained as historical versions |
| `host-app/c++/` | Historical C++ interface header, not a complete standalone C++ project |
| `experiments/wlfcode1.py` | Original experimental script |

See the root README for dependencies and startup commands. `requirements.txt` was inferred from imports and does not pin the historical environment.

The original debugging procedure is: enumerate serial ports, connect to the controller, add motion commands to a queue, synchronize the queue, and start execution. Check the port name, controller address and motion parameters against the actual device.

Local serial settings in `uart.cfg`, Python caches and virtual environments are excluded. Original `SCARA` identifiers remain unchanged. These names alone do not establish the whole robot's kinematic structure or validation status.

---

# 中文

# 软件说明

本目录保留历史程序，未进行设备联调或功能重构。

| 路径 | 作用 |
| --- | --- |
| `host-app/scara_host_app.py` | 含 GUI 启动入口 |
| `host-app/pyside6_app.py` | PySide6 界面基础逻辑 |
| `host-app/scara_host_app.ui` | Qt 界面源文件 |
| `host-app/scara_host_app_ui.py` | 生成的界面代码，当前程序直接导入，予以保留 |
| `host-app/scara_app.py` | 机械臂控制逻辑 |
| `host-app/scara_serial.py`、`host-app/base_serial.py` | 串口通信 |
| `host-app/main.py`、`host-app/v_plan.py` | 历史运动规划和调试代码，含原电脑绝对路径，需修改后才能用于对应实验 |
| `host-app/二自由度.py`、`host-app/二自由度(1).py` | 工作空间相关计算脚本，作为历史版本保留 |
| `host-app/c++/` | 历史 C++ 界面头文件；不是完整的独立 C++ 工程 |
| `experiments/wlfcode1.py` | 原始实验脚本 |

依赖安装与启动方式见根目录 README。`requirements.txt` 来自源码导入项，未锁定历史环境版本。

原始调试笔记描述的流程为：枚举串口 → 连接控制器 → 添加运动指令到队列 → 同步队列 → 启动执行。笔记中的串口名、控制器地址及运动参数需要针对实物确认。

个人串口配置 `uart.cfg`、Python 缓存及虚拟环境不纳入仓库。原始代码中的 `SCARA` 命名予以保留，不能仅凭该命名判断整机运动学结构或验证状态。
