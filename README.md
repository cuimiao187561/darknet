![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

# Darknet #
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).

------

## Using yolov3 to detect traffic light.
### some changes
- Modify
	- Makefile: GPU=0 -> GPU=1
	- cfg/voc.data
	- cfg/yolov3-voc.cfg: filters=75->filters=27, [yolo] classes=20->clasess=4, random=1->random=0
	- data/voc_2018.names
- Add
	- your_training_data
	- scrpts/VOCdevkit

more details about training yolov3 on traffic light data see: [yolo系列（1）：使用yolov3检测红绿灯](https://maozezhong.github.io/2018/04/29/yolo%E7%B3%BB%E5%88%97%EF%BC%881%EF%BC%89%EF%BC%9A%E4%BD%BF%E7%94%A8yolov3%E6%A3%80%E6%B5%8B%E7%BA%A2%E7%BB%BF%E7%81%AF/)