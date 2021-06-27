import ffmpeg

class FFMConverter:

    # def convert_webm_mp4_subprocess(self, input_file, output_file):
    #     try:
    #         cmd = f'ffmpeg -i {input_file} {output_file}'
    #         subprocess.run(cmd, shell=True)
    #     except:
    #         print("Conversion failed")

    def convert_to_mp4(self, input_file, output_file):
        print(input_file)
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.output(stream, output_file)
        ffmpeg.run(stream)
        # except:
        #     print("Conversion Failed")