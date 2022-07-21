# eg3d_pti_inversion

Installation Instructions

Download the following zip file:

```
https://drive.google.com/file/d/1yYCeiZXbFatYObGhUXyvk2aHyfG8KYjY/view?usp=sharing
```

This should contain an align.dat file and two directories named checkpoints and BFM. Move the BFM and checkpoints directories into eg3d_pti_inversion/Deep3DFaceRecon_pytorch. Move the align.dat file into eg3d_pti_inversion/inversion/utils.

To prepare an input image for inversion, create a directory and place an input image inside it. Then, call the process_test_images.py script inside Deep3DFaceRecon_pytorch. This will output a cropped image in INPUT_DIR/crop_1024 and camera pose parameters in INPUT_DIR/epoch_20_000000.

You may need to install nvdiffrast:
```
cd Deep3DFaceRecon_pytorch/nvdiffrast
pip install .
```

To pre-process your input image:
```
cd Deep3DFaceRecon_pytorch
python process_test_images.py --input_dir INPUT_DIR --gpu 0
```

To perform PTI GAN inversion, download the following pre-trained EG3D model and place it inside eg3d_pti_inversion/inversion/utils.

```
https://drive.google.com/file/d/1xwMlnPSvbfjQ4AHoJogs1ldKLitSwCcc/view?usp=sharing
```

Next, modify the paths_config.py file located in eg3d_pti_inversion/inversion/configs/paths_config.py. Set the pre-trained model paths to the locations of align.dat and the EG3D checkpoint, which should be in eg3d_pti_inversion/inversion/utils. Modify the ##Input info section with the location and name of your pre-processed input image data. The inversion output will be located in embedding_base_dir/input_data_id.

```
cd inversion
python run_pti.py
```

To edit hyperparameters such as how many steps you want to perform W optimization and generator fine-tuning, you can modify the Steps section of eg3d_pti_inversion/inversion/configs/hyperparameters.py.

