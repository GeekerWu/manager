#Docker &releate command：
docker commit 90586a96e128 debiandev
docker run -itd --privileged=true -p 5000:22 -p 5001:5901 --device=/dev/video0 --name debiandev debiandev:latest
sudo vncserver

# manager
Agenda:
main provide robot releate feature,and other test case maybe used in feature.
hardware:Servo PWM and Voltage feed back Feature,PCA9685,Ardiuno,Raspberry Pi,webcamera microphone,speaker,


Ardiuno folder：
colect Analog pin read Voltage，convert to servo angle，using serial package I2C port pass to Raspberry Pi.

back-end-prj folder:
miniserverraspberry.py is main pyserver script.provied UI api ,Database DDL,Ardinuo data reader,socket,servo control service
other py file is different feature test case.

front-end-prj folder:
UI project,contain webgl case,posenet(ml5.js) case,voice management,animation management,table show,video stream,chart...and others case.


nginx folder:
frontend proxy

tf-prj foilder:
tensorflow test environment

wumi folder:
wumi UI test case


ffmpeg-win64-static folder:
main feature is generate m3u8 file to support video stream service.

example
ffmpeg -i D:\video-manager\nginx\temp\tester.mp4 -c:v libx264 -c:a copy -f hls D:\video-manager\nginx\temp\hls\tester.m3u8
ffmpeg -i D:\tstsrc\tester.mp4 -c:v libx264 -c:a copy -f hls D:\video-manager\nginx\html\hls\tester.m3u8

ffmpeg -i E:\videos\video.mp4 -i E:\videos\logo.png -filter_complex overlay -profile:v baseline -level 3.0 -s 1024x1080 -start_number 0 -hls_time 0.5 -b:v 125k -bufsize 150k -hls_list_size 0 -f hls E:\videos\video\video.m3u8

1. 给视频加上水印图片
-i E:\videos\logo.png 给视频加上水印图片 -filter_complex overlay 位置位于视频左上角

右上角： -filter_complex overlay=W-w
左下角： -filter_complex overlay=0:H-h
右下角： -filter_complex overlay=W-w:H-h
2.输出视频的尺寸
-s 1024x1080
3.输出文件的起始文件
-start_number 0
4.输出文件的最小大小 和 最大的大小（会影响视频质量）
-b:v 125k -bufsize 150k
作者：elileo
链接：https://www.jianshu.com/p/36475d6f4558
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


