import pyarrow as pa
import pyarrow.ipc as ipc
import numpy as np 
from PIL import Image


PATH = "../test_embeddings.arrow"

with pa.OSFile(PATH, "rb") as f:
    reader = ipc.open_stream(f)
    table = reader.read_all()

images = np.stack(table["X"]).transpose(0,2,3,1).astype(float)

for i, image in enumerate(images):
    image_array_uint8 = (image * 255).astype(np.uint8)

    # 4. Create an image object from the array
    pil_image = Image.fromarray(image_array_uint8)

    # Or save it to a file
    pil_image.save(
        f"/Users/rogersb/radioconda/lib/python3.12/site-packages/embedding_atlas/widget_static/streamlit/static/img_{i}.png"
    )