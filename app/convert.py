import imageio_ffmpeg

# From https://github.com/imageio/imageio-ffmpeg?tab=readme-ov-file#example-usage

print('-------------------------------------------------------')
print('STARTING convert.py')
print(f'The version of ffmpeg being used is ${imageio_ffmpeg.get_ffmpeg_version()}')

path_in = '/code/app/vid_in/video.mp4'
path_out = '/code/app/vid_out/video_out.mp4'

# Read a video file
reader = imageio_ffmpeg.read_frames(path_in)
meta = reader.__next__()  # meta data, e.g. meta["size"] -> (width, height)

# Write a video file
writer = imageio_ffmpeg.write_frames(path_out, meta["size"] )  # size is (width, height)
writer.send(None)  # seed the generator
for frame in reader:
    writer.send(frame)
writer.close()  # don't forget this
reader.close()

print('Conversion succeeeded!!!')
print('-------------------------------------------------------')
