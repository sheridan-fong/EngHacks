import ffmpeg

class FFMConverter:

    def convert_to_mp4(self, input_file, output_file):
        try:
            stream = ffmpeg.input(input_file)
            stream = ffmpeg.output(stream, output_file)
            ffmpeg.run(stream)
        except:
            print("Conversion Failed")

    def convert_to_wav(self, input_file, output_file):
        try:
            stream = ffmpeg.input(input_file)
            stream = ffmpeg.output(stream, output_file)
            ffmpeg.run(stream)
        except:
            print("Conversion Failed")
