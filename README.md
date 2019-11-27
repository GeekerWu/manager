# manager
manager

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


