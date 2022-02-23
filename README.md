# Nosie Mask Detection
This model was trained on aws dl1 ec2 instance

# Access your VM
Lunch your dl1 instance

Access your ec2 instance via ssh

Once you are logged in check the habana developer page for more documentation

# Download and Install docker(ubuntu18.04)
Run the following code to download

docker pull vault.habana.ai/gaudi-docker/1.3.0/ubuntu18.04/habanalabs/tensorflow-installer-tf-cpu-2.7.1:1

Run the following code to install docker

docker run -it --runtime=habana -e HABANA_VISIBLE_DEVICES=all -e OMPI_MCA_btl_vader_single_copy_mechanism=none --cap-add=sys_nice -v /sys/kernel/debug:/sys/kernel/debug -v /data:/data -v /opt/habanalabs/ocpl.json:/opt/habanalabs/optl.json --net=host vault.habana.ai/gaudi-docker/1.3.0/ubuntu18.04/habanalabs/tensorflow-installer-tf-cpu-2.7.1:1.3.0-499

We downloaded and installed docker for ubuntu version 18.04 and tensorflow version 2.7.1

# Install requisite python libraries(gdown and unzip)

Gdown

pip3 install gdown

Unzip

pip3 install unzip
# Download data via

https://drive.google.com/file/d/1TEv3o58BZG78QKQWXWkctl1On9lnDT2k/view?usp=sharing

After successfully downloading dataset we can now unzip and extract by using unzip data.zip
  
