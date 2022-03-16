# Nose Mask Detection
This model was trained on Aws dl1 ec2 instance powered by Gaudi Accelerators

# Directories

The app folder contains the flask app am currently building

The model_training.py file contains our model training code

The requirements.txt file contains all the neccessary python libraries needed for our code to run

# Access your VM
Lunch your dl1 instance

Access your ec2 instance via ssh e.g Putty

Once you are logged in, check the habana developer page for more documentation https://developer.habana.ai

# Download and Install docker image for (Ubuntu 18.04 & tensorflow v2.7.1)
Run the following code to download docker image

docker pull vault.habana.ai/gaudi-docker/1.3.0/ubuntu18.04/habanalabs/tensorflow-installer-tf-cpu-2.7.1:1.3.0-499

Once downloading has finished, we can then run our docker image to start a secure shell

Run the following code to install docker image

docker run -it --runtime=habana -e HABANA_VISIBLE_DEVICES=all -e OMPI_MCA_btl_vader_single_copy_mechanism=none --cap-add=sys_nice -v /sys/kernel/debug:/sys/kernel/debug -v /data:/data -v /opt/habanalabs/ocpl.json:/opt/habanalabs/optl.json --net=host vault.habana.ai/gaudi-docker/1.3.0/ubuntu18.04/habanalabs/tensorflow-installer-tf-cpu-2.7.1:1.3.0-499

We downloaded and installed docker image for ubuntu version 18.04 and tensorflow version 2.7.1

# Install some python libraries(gdown and unzip)

Gdown - will be used to download dataset from google drive

pip3 install gdown

Unzip - will be used to unzip and extract dataset

pip3 install unzip

# Clone github reposetory

git clone https://github.com/rogerkorantenng/nose_mask_detection.git

# Export python path and habana json file

export PYTHONPATH=/nose_mask_detection:$PYTHONPATH

export HCL_CONFIG_PATH=/opt/habanalabs/ocpl.json

# Download dataset and unzip

Before downloading dataset, move to the working directory (nose_mask_detection)

cd noise_mask_detection

We can then download our dataset

gdown --id 1TEv3o58BZG78QKQWXWkctl1On9lnDT2k

Next you can unzip archive

unzip dataset.zip

# Install required python libraries

Next, you can then install the required python libraries using pip

pip3 install -r install requirements.txt

# Run our model_training.py file to start training

python3 model_training.py

After sometime when training is done, your .h5 and .json file should be available for you.
  
