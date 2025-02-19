class PhotographyCamera:
	photographies = []

	def __init__(self, storage_size_in_mb):
		# each photo takes around 10mb
		self.max_photographies = storage_size_in_mb // 10
	
	def take_photo(self, photography):
		if len(self.photographies) >= self.max_photographies:
			print("My storage is full!")
			return

		self.photographies.append(photography)
		print(f"Photo {photography} taken!")
		
		
camera = PhotographyCamera(storage_size_in_mb=20)
camera.take_photo(1)
camera.take_photo("photo_2")
camera.take_photo("photo_3")
camera.take_photo("photo_4")
print(camera.photographies)
