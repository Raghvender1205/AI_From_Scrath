import torch
from xunet import XUnet

unet = XUnet(
    dim=64,
    dim_mults=(1, 2, 4, 8),
    nested_unet_depths=(7, 4, 2, 1),
    consolidate_upsample_fmaps=True
)

img = torch.randn(1, 3, 256, 256)
out = unet(img)
# print(out) 
"""
[ 0.0380,  0.0524,  0.1453,  ..., -0.0223, -0.0405,  0.0023],
          [ 0.0400,  0.0619,  0.1685,  ...,  0.0065,  0.0143,  0.0937],
          ...,
          [-0.0794, -0.0961, -0.1332,  ...,  0.1109,  0.1138,  0.1426],
          [-0.0194, -0.0478, -0.0103,  ...,  0.2075,  0.0722,  0.0709],
          [-0.0239, -0.0073,  0.0277,  ...,  0.0982,  0.0593,  0.0042]],

         [[-0.0728,  0.0352,  0.0971,  ..., -0.0381,  0.0413,  0.0020],
          [-0.0164,  0.1088,  0.0485,  ...,  0.0729,  0.0621,  0.0259],
          [ 0.0574,  0.1652,  0.1461,  ...,  0.0709,  0.2084,  0.0269],
          ...,
          [ 0.0408,  0.0005,  0.0528,  ..., -0.1068, -0.0393, -0.0514],
          [-0.0347,  0.1110,  0.1136,  ...,  0.1109,  0.0425, -0.0112],
          [-0.0501,  0.1037,  0.0483,  ...,  0.0863,  0.0847,  0.0133]]]],
       grad_fn=<ReshapeAliasBackward0>)
"""
# For 3D (Video / CT Scans)
unet3d = XUnet(
    dim=64,
    frame_kernel_size=3,
    dim_mults=(1, 2, 4, 8),
    nested_unet_depths=(5, 4, 2, 1),
    consolidate_upsample_fmaps=True,
    weight_standardize=True
)

video = torch.randn(1, 3, 10, 128, 128)
out = unet3d(video)
print(out)
"""
tensor([[[[[ 3.2020e-02,  5.6498e-03,  1.1780e-01,  ...,  1.1335e-01,
             1.9203e-01,  8.8971e-02],
           [ 5.7339e-04,  8.8974e-02,  9.8678e-02,  ...,  1.6146e-01,
             3.1102e-02,  5.7374e-02],
           [ 4.9776e-02,  5.4889e-02,  7.3156e-02,  ...,  3.9525e-02,
             9.4406e-02,  7.9310e-02],
           ...,
           [ 3.5685e-02,  2.0059e-01, -7.0898e-02,  ...,  6.4832e-02,
             2.0289e-01,  1.5934e-01],
           [-6.2325e-02,  1.0256e-01,  5.5716e-02,  ...,  1.0157e-01,
             4.0639e-02,  1.1088e-01],
           [-2.2862e-02, -1.9659e-03,  2.6383e-02,  ...,  5.3436e-02,
             5.8839e-02,  5.0554e-02]],

          [[ 5.6458e-02,  4.6260e-02, -5.4133e-03,  ...,  5.8810e-02,
             1.4232e-01,  2.4142e-02],
           [-5.3391e-02, -5.9107e-02,  3.3219e-03,  ...,  1.9909e-01,
             6.7565e-02,  1.4222e-01],
           [ 1.1319e-01,  8.1069e-02, -1.5490e-03,  ...,  1.1660e-01,
             4.4252e-02,  5.8511e-02],
           ...,
           [-7.8062e-04,  5.0542e-02,  1.7826e-01,  ..., -1.9456e-01,
            -1.7559e-01, -7.9239e-02],
           [ 1.0855e-02,  7.6265e-02,  2.3858e-01,  ..., -5.8323e-02,
            -2.7100e-02, -1.1866e-01],
           [ 3.8829e-02, -5.1041e-02, -1.6229e-02,  ..., -1.2420e-01,
            -1.0497e-01, -8.4949e-02]],

          [[ 6.3202e-02,  1.1099e-02,  2.3430e-02,  ...,  2.0412e-01,
             1.1321e-01,  1.0243e-01],
           [-1.0603e-01, -6.4231e-02, -3.2556e-02,  ...,  6.3571e-02,
             7.2364e-02, -4.0200e-03],
           [-1.5674e-02, -1.2233e-01,  1.3023e-01,  ..., -1.2302e-01,
             7.0839e-02, -2.1512e-02],
           ...,
           [ 5.5603e-02, -3.4763e-02,  3.5521e-01,  ...,  8.9203e-02,
             5.1347e-02,  8.6023e-02],
           [ 1.3584e-02,  7.5808e-02,  2.0420e-01,  ...,  1.8710e-01,
             7.6588e-02,  1.5962e-01],
           [ 3.5427e-02,  1.6819e-02,  5.5856e-02,  ...,  5.5013e-02,
             3.4773e-02,  4.4312e-02]],

          ...,

          [[-1.9501e-02, -4.7628e-02, -9.4433e-02,  ...,  2.3175e-01,
             2.0788e-01,  1.4955e-01],
           [ 2.0990e-01,  5.9456e-02, -7.9317e-02,  ...,  2.9066e-01,
             2.3536e-01,  1.3802e-01],
           [ 1.4399e-01,  1.3253e-01,  1.4149e-01,  ...,  1.8689e-01,
             2.4353e-01,  1.3914e-01],
           ...,
           [-1.4794e-02, -4.7495e-01, -5.7479e-01,  ..., -5.8182e-01,
            -4.9430e-01, -4.6831e-01],
           [-6.9828e-02, -3.5960e-01, -5.7718e-01,  ..., -7.9996e-01,
            -3.5228e-01, -5.0314e-01],
           [-1.9416e-01, -3.9452e-01, -4.2916e-01,  ..., -5.2436e-01,
            -4.3930e-01, -3.8067e-01]],

          [[ 1.6995e-01,  2.0365e-01,  2.2140e-01,  ...,  2.2762e-01,
             9.2042e-02,  1.1318e-01],
           [ 2.3694e-01,  2.1712e-01,  1.9884e-01,  ...,  1.6674e-01,
             1.2887e-01,  4.7539e-02],
           [ 5.8896e-02,  4.0063e-02,  1.6537e-01,  ...,  1.2672e-01,
             1.7654e-01,  1.6137e-01],
           ...,
           [ 3.9817e-02,  2.3589e-01,  6.5795e-04,  ..., -5.1861e-01,
            -4.1970e-01, -2.6709e-01],
           [ 1.0846e-01, -2.9327e-02,  2.2045e-01,  ..., -4.5037e-01,
            -2.8657e-01, -2.6726e-01],
           [-8.2652e-02,  2.8790e-02, -5.7845e-02,  ..., -3.7017e-01,
            -3.0106e-01, -2.9284e-01]],

          [[-1.1936e-01,  4.4973e-02, -2.9442e-02,  ..., -1.8896e-02,
             3.3126e-02,  1.7742e-02],
           [-1.4650e-01, -1.5961e-01, -1.8330e-01,  ...,  4.0459e-02,
             1.8699e-02,  6.1235e-02],
           [-2.1227e-01, -2.3546e-01, -1.1263e-01,  ..., -5.7942e-02,
            -3.6180e-02,  5.7588e-02],
           ...,
           [-1.2933e-01,  4.3430e-02, -4.9209e-02,  ..., -4.6865e-02,
             1.3473e-01,  1.1348e-01],
           [ 6.5509e-02, -1.0300e-01, -5.1613e-02,  ..., -2.4311e-02,
             1.2469e-01,  2.9561e-02],
           [ 1.7988e-02, -2.6213e-02, -7.9485e-02,  ..., -5.4591e-02,
             4.3865e-02,  1.1777e-01]]],


         [[[ 2.1434e-02,  4.0694e-02,  1.4566e-02,  ...,  8.7815e-02,
            -5.9592e-03,  8.2965e-02],
           [-1.0202e-02, -8.9829e-03,  1.0558e-01,  ...,  6.8777e-02,
             9.9864e-02,  6.0730e-02],
           [-5.8656e-02, -1.5033e-02,  1.1722e-01,  ...,  1.6699e-01,
             7.9605e-02,  6.4917e-02],
           ...,
           [-2.6513e-02,  1.0044e-01, -5.7976e-02,  ..., -2.6011e-02,
             8.2744e-03,  9.0241e-02],
           [-2.9317e-02,  1.7389e-02,  2.2199e-02,  ...,  8.0803e-02,
             1.3730e-01,  6.1004e-02],
           [ 1.6582e-02,  2.4035e-02, -1.9377e-02,  ...,  2.7161e-02,
             7.4826e-02,  8.0625e-02]],

          [[ 5.0270e-02,  6.4659e-02, -5.5400e-02,  ...,  3.0428e-02,
             2.1058e-02,  8.6411e-02],
           [ 7.3439e-02,  4.5384e-02,  1.2869e-01,  ..., -9.9960e-03,
            -2.1208e-02,  1.4317e-02],
           [-5.4180e-02,  4.6331e-02,  1.6354e-01,  ..., -2.1742e-02,
            -3.9285e-02,  2.7378e-02],
           ...,
           [-4.7580e-02, -7.5860e-02,  1.2631e-01,  ...,  1.6785e-01,
             2.3963e-01,  1.1813e-01],
           [-2.7704e-03,  7.9573e-03,  2.6478e-02,  ...,  1.8886e-01,
             2.6892e-01,  7.8376e-02],
           [ 7.2860e-03,  1.2711e-01,  9.7771e-02,  ...,  4.6048e-02,
             9.1393e-02,  1.1551e-01]],

          [[-4.1915e-02,  1.0655e-01,  7.0790e-02,  ...,  5.1863e-02,
             1.1546e-02,  4.7943e-02],
           [-4.6533e-02,  6.8925e-02,  1.1263e-01,  ...,  2.2509e-01,
            -7.2128e-02,  1.1038e-01],
           [-1.3183e-02,  1.6901e-01, -3.2427e-02,  ...,  1.4838e-01,
             1.2398e-02, -3.5716e-02],
           ...,
           [ 5.4905e-02,  2.3442e-01,  1.7240e-01,  ...,  7.9786e-02,
             1.9285e-01,  1.0237e-01],
           [ 6.2795e-02,  3.1770e-01,  3.1636e-01,  ...,  5.8404e-03,
             7.3021e-02,  1.3878e-01],
           [ 1.6179e-01,  2.2185e-01,  1.2725e-01,  ..., -1.4675e-02,
             1.2332e-01, -1.7236e-02]],

          ...,

          [[-1.4354e-02,  9.2237e-02, -1.7857e-02,  ..., -1.0416e-01,
            -1.0472e-01, -1.5789e-02],
           [-2.7006e-02, -1.4002e-01, -3.2295e-01,  ..., -2.6687e-02,
            -1.2378e-01,  1.1349e-01],
           [-9.1580e-02, -1.0223e-01, -6.1130e-02,  ..., -7.1549e-02,
             4.2341e-02, -1.1092e-01],
           ...,
           [-1.5511e-01,  2.0243e-01, -1.5410e-01,  ...,  4.3094e-02,
             1.6678e-01,  2.4307e-01],
           [-1.5346e-01,  7.6917e-02, -3.2481e-02,  ...,  1.6427e-03,
             1.7579e-01,  2.0304e-01],
           [-4.4100e-02,  8.6616e-02, -2.5247e-02,  ...,  1.7922e-01,
             3.2202e-01,  4.6984e-02]],

          [[ 4.3695e-02,  8.1736e-02,  1.1870e-01,  ...,  8.1362e-02,
             2.2295e-01,  2.1849e-01],
           [-8.3763e-02,  8.9576e-02, -1.6302e-01,  ...,  2.4919e-01,
             2.3995e-01,  2.7399e-01],
           [-1.0979e-02,  8.6237e-02,  8.7124e-02,  ...,  1.8251e-01,
             9.1407e-02,  2.6166e-01],
           ...,
           [ 1.5647e-01,  2.5907e-01,  3.2297e-01,  ...,  3.6271e-01,
             2.7881e-01,  2.5852e-01],
           [ 2.4670e-01,  1.5059e-01,  1.8125e-01,  ...,  3.8750e-01,
             4.4150e-01,  4.7228e-01],
           [-1.2701e-01, -2.6622e-02,  7.8476e-02,  ...,  3.6392e-01,
             2.7645e-01,  3.9958e-01]],

          [[-5.0043e-02, -2.7144e-02,  6.4027e-02,  ...,  9.3598e-02,
             7.5430e-02, -9.9566e-03],
           [-4.8491e-02, -6.6399e-02,  1.9611e-01,  ...,  3.6896e-02,
             5.8913e-03,  8.2385e-02],
           [-4.3461e-02,  1.3971e-02,  1.0633e-01,  ...,  3.4153e-02,
             2.4066e-02,  1.4447e-01],
           ...,
           [-3.7147e-02,  2.0321e-01,  1.9494e-03,  ...,  2.7480e-01,
             1.4585e-01,  1.0828e-01],
           [ 7.8500e-02,  1.1153e-02,  9.3258e-02,  ...,  1.4865e-01,
             3.9575e-02,  1.1169e-01],
           [ 9.5974e-04,  1.4747e-02,  1.3979e-01,  ...,  2.0598e-01,
             2.0581e-01,  1.7021e-01]]],


         [[[-3.1877e-02, -6.6992e-02, -6.6010e-03,  ..., -3.5132e-02,
             2.1983e-02, -1.4231e-02],
           [ 5.9398e-02, -4.5036e-02, -3.1354e-02,  ...,  3.7380e-02,
             2.3949e-03, -1.5037e-02],
           [-2.9007e-02,  7.5813e-02, -2.8233e-03,  ...,  2.9616e-02,
             3.0817e-02,  3.2796e-02],
           ...,
           [-7.7972e-03, -1.6224e-02, -1.4038e-02,  ..., -3.4354e-02,
            -4.4556e-02, -5.7156e-02],
           [ 2.6470e-02, -5.2054e-02,  4.8684e-02,  ..., -9.9742e-02,
            -6.5074e-02, -1.9777e-02],
           [-5.3551e-03, -2.6953e-02, -1.7056e-03,  ..., -7.2339e-02,
            -4.3874e-02, -1.7749e-02]],

          [[-5.2318e-02,  1.8835e-02,  3.0069e-02,  ...,  5.3641e-02,
             2.5306e-02,  5.3429e-04],
           [-2.4016e-02,  6.9485e-02,  3.9132e-02,  ...,  9.8625e-02,
             2.5746e-02, -8.4644e-02],
           [-7.4952e-02, -3.2077e-02, -1.9453e-02,  ...,  4.8277e-02,
            -6.2812e-03,  1.7153e-02],
           ...,
           [ 2.9563e-02,  7.4623e-04, -1.0999e-01,  ...,  1.5289e-02,
             1.2704e-01,  4.1427e-03],
           [-3.2116e-02,  1.3727e-01, -5.3845e-02,  ...,  3.5836e-02,
             1.2113e-01,  4.5830e-02],
           [-4.0754e-02, -1.4500e-01, -2.8344e-02,  ..., -1.6737e-03,
             1.9834e-02,  1.0815e-02]],

           [-2.4935e-01, -3.3675e-01, -3.2091e-01,  ..., -1.7639e-01,
            -1.5390e-01, -6.3598e-02]],

          [[-1.0668e-01, -3.9736e-02, -1.2302e-01,  ..., -1.3595e-01,
            -1.1031e-01,  3.3809e-02],
           [-9.3823e-02, -2.0168e-01, -1.8750e-01,  ..., -1.1324e-01,
            -9.1632e-02,  2.4054e-02],
           [-7.4587e-02, -1.4166e-01, -1.7940e-01,  ..., -5.6613e-02,
            -1.4704e-01, -1.0051e-01],
           ...,
           [-1.9260e-01, -5.1979e-01, -4.5542e-01,  ..., -3.3594e-01,
            -3.3658e-01, -1.4800e-01],
           [-1.0525e-01, -1.7568e-01, -2.9566e-01,  ..., -4.6588e-01,
            -3.2204e-01, -3.5242e-01],
           [ 2.3051e-01, -9.6122e-02, -1.6352e-01,  ..., -2.8065e-02,
            -5.2648e-02, -7.4181e-02]],

          [[-1.0706e-01, -2.4858e-01, -1.4258e-01,  ..., -6.8657e-02,
             2.6454e-02,  4.0144e-02],
           [-1.7632e-01, -2.5357e-01, -3.3669e-01,  ..., -4.0794e-02,
             7.1504e-03, -1.2209e-02],
           [-2.1692e-01, -3.1419e-01, -2.7656e-01,  ..., -1.2654e-01,
            -1.0674e-01, -3.0541e-02],
           ...,
           [-2.1991e-01, -7.7743e-02, -2.5442e-01,  ..., -7.3699e-02,
            -5.7050e-02,  4.5411e-02],
           [-1.4337e-01, -1.4148e-01, -1.0946e-01,  ..., -2.2238e-02,
            -6.8855e-02, -6.5325e-02],
           [-1.2157e-01, -1.3988e-01, -1.0536e-01,  ..., -2.5052e-02,
             2.5387e-03, -4.8159e-02]]]]], grad_fn=<ConvolutionBackward0>
"""