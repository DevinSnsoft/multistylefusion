import torch
import torchvision.transforms as transforms
import torchvision.datasets as dsets

# Directory containing the data.
from torch.utils.data import TensorDataset, DataLoader

root = 'data/'


def get_data(dataset, batch_size):
    # # Get MNIST dataset.
    # if dataset == 'MNIST':
    #     transform = transforms.Compose([
    #         transforms.Resize(28),
    #         transforms.CenterCrop(28),
    #         transforms.ToTensor()])
    #
    #     dataset = dsets.MNIST(root + 'mnist/', train='train',
    #                           download=False, transform=transform)
    #
    # # Get SVHN dataset.
    # elif dataset == 'SVHN':
    #     transform = transforms.Compose([
    #         transforms.Resize(32),
    #         transforms.CenterCrop(32),
    #         transforms.ToTensor()])
    #
    #     dataset = dsets.SVHN(root + 'svhn/', split='train',
    #                          download=True, transform=transform)
    #
    # # Get FashionMNIST dataset.
    # elif dataset == 'FashionMNIST':
    #     transform = transforms.Compose([
    #         transforms.Resize(28),
    #         transforms.CenterCrop(28),
    #         transforms.ToTensor()])
    #
    #     dataset = dsets.FashionMNIST(root + 'fashionmnist/', train='train',
    #                                  download=True, transform=transform)
    #
    # # Get CelebA dataset.
    # # MUST ALREADY BE DOWNLOADED IN THE APPROPRIATE DIRECTOR DEFINED BY ROOT PATH!
    # elif dataset == 'CelebA':
    #     transform = transforms.Compose([
    #         transforms.Resize(256),
    #         transforms.CenterCrop(256),
    #         transforms.ToTensor(),
    #         transforms.Normalize((0.5, 0.5, 0.5),
    #                              (0.5, 0.5, 0.5))])
    #
    #     dataset = dsets.ImageFolder(root=root + 'celeba/', transform=transform)
    #
    # # Get Font dataset.
    # # MUST ALREADY BE DOWNLOADED IN THE APPROPRIATE DIRECTOR DEFINED BY ROOT PATH!
    # elif dataset == 'Font':
    #     transform = transforms.Compose([
    #         # transforms.Grayscale(num_output_channels=1),  # 彩色图像转灰度图像num_output_channels默认1
    #         transforms.Resize(28),
    #         transforms.CenterCrop(28),
    #         transforms.ToTensor(),
    #         transforms.Normalize((0.5, 0.5, 0.5),
    #                              (0.5, 0.5, 0.5))])
    #
    #     dataset = dsets.ImageFolder(root=root + 'font/', transform=transform)
    #
    # # Create dataloader.
    # dataloader = torch.utils.data.DataLoader(dataset,
    #                                          batch_size=batch_size,
    #                                          drop_last=True,
    #                                          shuffle=True)

    # 加载本地的数据集文件
    data = torch.load('training.pt')

    # 获取数据和标签
    x, y = data

    # 将数据和标签封装为TensorDataset
    dataset = TensorDataset(x, y)

    # 创建数据加载器
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True)
    return dataloader
