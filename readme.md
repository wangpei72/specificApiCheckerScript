本脚本用于执行对于大型项目组或者多个代码仓库中废弃的api调用进行搜索，并将结果输出至xls文件.

需要为脚本提供的资源文件包括：

- 放置所有待搜索代码仓库文件的文件夹目录；
- xls文件输入目录
- 提供一个可以供放置fileList.txt(代码仓库下所有文件信息的文本文件)的目录

以上参数可以在workFlowForAGroup.py的main函数中修改。

目前目标搜索的api硬编码在updatedApiChecker.py中，需要补充或更改搜索目标的可以在代码基础上添加。

如果有需要，欢迎联系wpkkstr@gmail.com