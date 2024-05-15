<img src="https://www.geekrar.com/wp-content/uploads/2021/11/1200x675VB_Kali.jpg" />

# Setting Up a Virtual Environment in Kali Linux

Welcome to today's workshop! Let's start by setting up your virtual environment in Kali Linux.

### Download Kali Linux Image

First, navigate to your 'goinfre' directory:

```bash
cd ~/goinfre
```

Now, download the Kali Linux virtualbox image using wget:

```bash
wget https://kali.download/base-images/kali-2024.1/kali-linux-2024.1-hyperv-amd64.7z
```

### Download and Unzip 7z Program

Next, let's download the 7z program to extract the image:

```bash
wget https://www.7-zip.org/a/7z2301-linux-x64.tar.xz
```

Extract the 7z program:

```bash
tar -xvf 7z2301-linux-x64.tar.xz
```

### Unzip Kali Image

Use the 7z program to unzip our Kali Linux image:

```bash
./7zz x kali-linux-2023.3-virtualbox-amd64.7z
```

### Access Kali Linux Image

Open the directory containing the image:

```bash
open kali-linux-2023.3-virtualbox-amd64
```

Double click on the file named `kali-linux-2023.3-virtualbox-amd64.vdi` to configure the VirtualBox image.

### Start the Virtual Environment

Once configured, start running the environment by clicking on "Start" in VirtualBox.
