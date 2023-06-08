基于条件归一化网络的艺术字体多风格融合

## Instruction
### 一、core文件夹
##### 项目核心代码<br>
generateds：生成tfrecords训练集<br>
forward：前向传播过程，包括图像生成网络、损失函数网络和loss的计算<br>
backward：主要训练过程<br>
test：测试部分，完成图像风格融合和快速迁移<br>
app：JS网页应用调用test的接口文件

### 二、main.py
运行JS网页应用的入口，在网页上完成可视化操作

## Prepare
##### 一、运行环境
python3.6<br>
##### 二、下载coco数据集
http://images.cocodataset.org/zips/train2014.zip <br>
放在 ./core/MSCOCO/ 文件夹中<br>
##### 三、下载vgg16预训练模型
百度网盘（链接来自网络）：https://pan.baidu.com/s/1gg9jLw3  密码:umce，<br>
放在 ./core/vggnet 文件夹中<br>
##### 四、制作coco数据集tfRecords
```
$ python generateds.py
```

## 模型训练
```
$ python backward.py
```
1、提供断点续训功能<br>
2、提供已经训练好的模型（5万轮），可在5万轮的基础上继续训练，也可删掉checkpoint从0开始训练<br>
3、在训练过程中，每500轮将会保存一张训练图片在./core/save_training_imgs/中，可从中查看训练效果<br>

## 模型测试
1、将测试图片放在./core/test_imgs/中<br>
2、在test.py中，修改测试文件路径PATH_IMG<br>
3、在test.py中，修改风格编号LABEL_1至LABEL_4
```
$ python test.py
```
4、生成图片存储在./core/results/文件夹中

## 在线平台运行
```
$ python main.py
```
1、在浏览器中打开host地址：127.0.0.1:5000<br>
2、在网页上完成可视化操作<br>
3、若提示"OSError: [Errno 48] Address already in use"，请按以下步骤处理：<br>
```
$ sudo lsof -i:5000
```
找到占用5000端口进程的PID编号，然后kill掉此进程
```
$ sudo kill pid
```
重新运行main.py
```
$ python main.py
```
