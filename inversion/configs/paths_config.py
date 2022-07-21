## Pretrained models paths
eg3d_ffhq = '/media/data6/connorzl/pigan/S-GAN/stylegan3/pti_inversion_data/pretrained_models/final_2200.pkl'
dlib = '/media/data6/connorzl/pigan/S-GAN/stylegan3/pti_inversion_data/pretrained_models/align.dat'

## Dirs for output files
checkpoints_dir = './checkpoints'
embedding_base_dir = './embeddings'
experiments_output_dir = './output'
logdir = '/media/data6/connorzl/pigan/S-GAN/stylegan3/pti_inversion/logs'

## Input info
# Location of the cameras json file
input_pose_path = '/media/data6/connorzl/pigan/inversion_release/Deep3DFaceRecon_pytorch/inputs/epoch_20_000000/cameras.json'
# The image tag to lookup in the cameras json file
input_id = 'taylor2'
# Where the input image resides
input_data_path = '/media/data6/connorzl/pigan/inversion_release/Deep3DFaceRecon_pytorch/inputs/crop_1024'
# Where the outputs are saved (i.e. embeddings/{input_data_id})
input_data_id = 'taylor2'

## Keywords
pti_results_keyword = 'PTI'
e4e_results_keyword = 'e4e'
sg2_results_keyword = 'SG2'
sg2_plus_results_keyword = 'SG2_plus'
multi_id_model_type = 'multi_id'