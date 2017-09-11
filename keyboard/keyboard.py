import pyaudio
import wave

def KeyboardMaker(path_to_sounds):
	class Keyboard:
		def __init__(self):
			# initialize a keyboard
			self.keys = []
			self.p = pyaudio.PyAudio()
			for i in range(88):
				self.keys.append(False)

		def press(self, key):
			# depress a key if it's currently released, otherwise do nothing
			k = self.keys[key]
			if k == False:
				#start a stream
				track_num = 39148 + key
				if key > 43:
					track_num += 1
				wf = wave.open(path_to_sounds + str(track_num) + "__jobro__piano-ff-" + str(key + 1).zfill(3) + ".wav", "rb")

				def callback(in_data, frame_count, time_info, status):
					data = wf.readframes(frame_count)
					return (data, pyaudio.paContinue)

				stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
	                channels=wf.getnchannels(),
	                rate=wf.getframerate(),
	                output=True,
	                stream_callback=callback)
				self.keys[key] = (wf, stream)

		def release(self, key):
			# release a key if it's currently depressed, otherwise do nothing
			k = self.keys[key]
			if k != False:
				#stop stream and replace with False
				wf, stream = self.keys[key]
				stream.stop_stream()
				stream.close()
				wf.close()
				self.keys[key] = False
	return Keyboard

class Keyboard:
	def __init__(self):
		# initialize a keyboard
		self.keys = []
		self.p = pyaudio.PyAudio()
		for i in range(88):
			self.keys.append(False)

	def press(self, key):
		# depress a key if it's currently released, otherwise do nothing
		k = self.keys[key]
		if k == False:
			#start a stream
			track_num = 39148 + key
			if key > 43:
				track_num += 1
			wf = wave.open("2489__jobro__piano-ff/" + str(track_num) + "__jobro__piano-ff-" + str(key + 1).zfill(3) + ".wav", "rb")

			def callback(in_data, frame_count, time_info, status):
				data = wf.readframes(frame_count)
				return (data, pyaudio.paContinue)

			stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
			self.keys[key] = (wf, stream)

	def release(self, key):
		# release a key if it's currently depressed, otherwise do nothing
		k = self.keys[key]
		if k != False:
			#stop stream and replace with False
			wf, stream = self.keys[key]
			stream.stop_stream()
			stream.close()
			wf.close()
			self.keys[key] = False