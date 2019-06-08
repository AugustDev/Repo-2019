# Google's EfficientNets  

Paper: EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks  

https://arxiv.org/pdf/1905.11946.pdf

<img src=https://github.com/RubensZimbres/Repo-2019/blob/master/Google-EfficientNet/Pics/efficient.png>  

# Using Checkpoints

<b>Get CIFAR-10</b>

```
$ wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
$ wget https://raw.githubusercontent.com/tiagosn/cifar-10_py2png/master/cifar-10_py2png.py
$ python cifar-10_py2png.py cifar-10-batches-py
```


<b> ATTACH AND CONFIGURE GOOGLE COMPUTE ENGINE DISK </b>

```
$ sudo mkfs.ext4 -m 0 -F -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb
$ sudo mkdir -p /mnt/disks/
$ sudo mount -o discard,defaults /dev/sdb /mnt/disks/
$ sudo chmod a+w /mnt/disks/
$ sudo cp /etc/fstab /etc/fstab.backup
$ sudo blkid /dev/sdb
$ sudo vi /etc/fstab

UUID=3f228fd9-1dce-4197-b1b2b3-12345 /mnt/disks/ ext4 discard,defaults,nobootwait 0 2
# ESC : wq

$ sudo lsblk

NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   60G  0 disk 
└─sda1   8:1    0   60G  0 part /
sdb      8:16   0  500G  0 disk /mnt/disks
$ cd /mnt/disks
```  

<b>Download IMAGENET --  SIZE = 155 GB</b>

```
$ pip install kaggle
$ export KAGGLE_USERNAME=rubens
$ export KAGGLE_KEY=xxxxxxxxxxxxxx
$ touch kaggle.json
$ vi kaggle.json # ADD CREDENTIALS
$ ~/.local/bin/kaggle competitions download -c imagenet-object-localization-challenge

# OR

$ mkdir data && cd data
$ wget https://raw.githubusercontent.com/RubensZimbres/Repo-2019/master/Google-EfficientNet/download_imagenet.sh
$ sudo bash download_imagenet.sh

$ exit
$ sudo chmod -R +X /home
$ ...

$ gsutil cp ~/.local/bin/dataset gs://efficient-net/data
$ gsutil mv gs://efficient-net/data/train0.csv gs://efficient-net/data/train.csv
```  

<img src=https://raw.githubusercontent.com/RubensZimbres/Repo-2019/master/Google-EfficientNet/Pics/kaggle_download1.png>  

<b>Project</b>

```
$ export MODEL=efficientnet-b0
$ wget https://storage.googleapis.com/cloud-tpu-checkpoints/efficientnet/efficientnet-b0.tar.gz
$ mkdir weights
$ tar -xvf efficientnet-b0.tar.gz
$ gsutil cp home/rubens/weights/* gs://efficient-net
$ wget https://upload.wikimedia.org/wikipedia/commons/f/fe/Giant_Panda_in_Beijing_Zoo_1.JPG -O panda.jpg
$ wget https://storage.googleapis.com/cloud-tpu-checkpoints/efficientnet/eval_data/labels_map.txt
$ python eval_ckpt_main.py --model_name=efficientnet-b3 --ckpt_dir=efficientnet-b3 --example_img=panda.jpg --labels_map_file=labels_map.txt
```  

<img src=https://github.com/RubensZimbres/Repo-2019/blob/master/Google-EfficientNet/Pics/panda.png>  

<img src=https://github.com/RubensZimbres/Repo-2019/blob/master/Google-EfficientNet/Pics/efficient0.png>  

# Training  

```
$ export PYTHONPATH="$PYTHONPATH:/home/rubens/efficient"
$ cd /tpu/models/official/efficientnet
$ python main.py --tpu=rubens --data_dir=gs://efficient-net/data --model_dir=gs://efficient-net
```  

<img src=https://github.com/RubensZimbres/Repo-2019/blob/master/Google-EfficientNet/Pics/efficient_01.png>  

<img src=https://github.com/RubensZimbres/Repo-2019/blob/master/Google-EfficientNet/Pics/efficient_00.png>  
