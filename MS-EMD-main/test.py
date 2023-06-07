import tensorflow as tf

print(tf.__version__)
tf.config.list_physical_devices('GPU')
print(tf.test.is_gpu_available())
# CUDA_VISIBLE_DEVICES=0,1 python src/train.py --input_dir datasets/243/train --output_dir results/243/train --save_summary 1 --style_num 3 --with_dis 1