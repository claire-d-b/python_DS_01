from load_image import ft_load, slice_me_3d, create_image
import matplotlib.pyplot as plt
import numpy as np

def main():
    narray = ft_load("../animal.jpeg")

    img = create_image(narray)
    print(narray)
    width, height = img.size
    sliced_array = slice_me_3d(narray, height-650, height-250, width-600, width-200)
    
    color_image = create_image(sliced_array)

    # Convert the image to grayscale
    image = color_image.convert('L')

    gray_array = np.array(image)

    # print("gray_array:", list(map(lambda gray: list([gray]), gray_array)))

    nlist = gray_array.tolist()

    image.save('output.jpg', format='JPEG')
    

    # Convert the Pillow image to a NumPy array
    data_np = np.array(image)

    # Step 3: Display the Image in a Matplotlib Figure
    fig, ax = plt.subplots()

    # Display the data as an image
    img_ax = ax.imshow(data_np, cmap='gray')

    # Save the figure (optional)
    fig.savefig('lili.jpeg', format='JPEG')

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

