# -*- coding: utf-8 -*-


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense,BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import os

main_dir = 'New Masks Dataset'
train_dir = os.path.join(main_dir,'Train')
test_dir = os.path.join(main_dir,'Test')
valid_dir = os.path.join(main_dir,'Validation')

train_mask_dir = os.path.join(train_dir,'Mask')
train_No_mask_dir = os.path.join(train_dir,'Non Mask')

train_mask_names = os.listdir(train_mask_dir)
print(train_mask_names[0:10])

train_No_mask_names = os.listdir(train_No_mask_dir)
print(train_No_mask_names[0:10])

mask_images = []

for i in train_mask_names:
  mask_images.append(os.path.join(train_mask_dir,i))

non_mask_images=[]

for i in train_No_mask_names:
  non_mask_images.append(os.path.join(train_No_mask_dir,i))

import plotly.express as px
from skimage import io
from skimage.transform import resize

fig,ax = plt.subplots(1,4,figsize=(15,5))
img1 = io.imread(mask_images[6])
img2 = io.imread(mask_images[9])
img3 = io.imread(mask_images[10])
img4 = io.imread(mask_images[18])

ax[0].imshow(img1)
ax[0].set_title("Mask_Image 6")

ax[1].imshow(img2)
ax[1].set_title("Mask_Image 9")

ax[2].imshow(img3)
ax[2].set_title("Mask_Image 10")

ax[3].imshow(img4)
ax[3].set_title("Mask_Image 18")


plt.show()

fig,ax = plt.subplots(1,4,figsize=(15,5))
img1 = io.imread(non_mask_images[0])
img2 = io.imread(non_mask_images[1])
img3 = io.imread(non_mask_images[2])
img4 = io.imread(non_mask_images[3])

ax[0].imshow(img1)
ax[0].set_title("Non_Mask_Image 1")

ax[1].imshow(img2)
ax[1].set_title("Non_Mask_Image 2")

ax[2].imshow(img3)
ax[2].set_title("Non_Mask_Image 3")

ax[3].imshow(img4)
ax[3].set_title("Non_Mask_Image 4")


plt.show()

train_datagen = ImageDataGenerator(rescale=1./255,
                                   zoom_range=0.2,
                                   rotation_range=25,
                                   horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
valid_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_dir,
                                                    target_size=(300,300),
                                                    batch_size=32,
                                                    class_mode='binary')
test_generator = test_datagen.flow_from_directory(test_dir,
                                                  target_size=(300,300),
                                                  batch_size=32,
                                                  class_mode='binary')
valid_generator = valid_datagen.flow_from_directory(valid_dir,
                                                    target_size=(300,300),
                                                    batch_size=32,
                                                    class_mode='binary')

train_generator.class_indices

train_generator.image_shape

model = Sequential()

model.add(Conv2D(filters=32,kernel_size=(3,3),padding='same',input_shape=(300,300,3),activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Dropout(0.5))

model.add(Conv2D(filters=64,kernel_size=(3,3),padding='same',activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Dropout(0.5))

model.add(Conv2D(filters=32,kernel_size=(3,3),padding='same',activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Dropout(0.5))

model.add(Flatten())

model.add(Dense(256,activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer=Adam(learning_rate=0.0001),metrics=['accuracy'])

model.summary()

from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor='val_loss',patience=4)

model_train = model.fit(train_generator,epochs=25,
          validation_data=valid_generator,
          batch_size=32)

import pandas as pd
metrics = pd.DataFrame(model.history.history)

metrics.head(10)

test_loss,test_accuracy = model.evaluate_generator(test_generator)

print('test_loss: ',test_loss)
print('test_accuracy: ',test_accuracy)

model.save('./roger.h5')

#from google.colab import drive
#drive.mount('/content/drive')

#!cp roger.h5 ./drive/MyDrive/roger.h5

#drive.flush_and_unmount()
#print('All changes made in this colab session should now be visible in Drive.')


if __name__ == '__main__':
    
    main()
  
