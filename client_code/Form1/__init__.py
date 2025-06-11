from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_klasifikasi_click(self, **event_args):
    # 1. Ambil file gambar dari FileLoader
    file_gambar = self.file_loader_1.file

    if file_gambar is not None:
      # 2. Tampilkan gambar di komponen Image
      self.image_preview.source = file_gambar

      # 3. Panggil fungsi server 'classify_image' dan kirim file
      hasil = anvil.server.call('classify_image', file_gambar)

      # 4. Tampilkan hasil klasifikasi di Label
      self.label_hasil.text = f"Hasil klasifikasi: {hasil}"
    else:
      self.label_hasil.text = "Silakan unggah gambar terlebih dahulu."

