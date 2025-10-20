from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
from PIL import Image
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
            color = form.cleaned_data['color'] or '#000000'

            # Create QR code with color
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color=color, back_color="white").convert('RGB')

            # Save image
            file_name = res_name.replace(" ", "_").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            img.save(file_path, format='PNG')

            qr_url = os.path.join(settings.MEDIA_URL, file_name)

            context = {
                'res_name': res_name,
                'qr_url': qr_url,
                'file_name': file_name
            }
            return render(request, 'qr_result.html', context)
    else:
        form = QRCodeForm()

    return render(request, 'generate_qr_code.html', {'form': form})
