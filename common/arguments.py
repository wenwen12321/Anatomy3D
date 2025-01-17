# # Copyright (c) 2018-present, Facebook, Inc.
# # All rights reserved.
# #
# # This source code is licensed under the license found in the
# # LICENSE file in the root directory of this source tree.
# #

# import argparse

# def parse_args():
#     parser = argparse.ArgumentParser(description='Training script')

#     # General arguments
#     parser.add_argument('-d', '--dataset', default='h36m', type=str, metavar='NAME', help='target dataset') # h36m or humaneva
#     parser.add_argument('-k', '--keypoints', default='cpn_ft_h36m_dbb', type=str, choices=['cpn_ft_h36m_dbb', 'detectron_ft_h36m', 'gt'], metavar='NAME', help='2D detections to use')
#     parser.add_argument('-str', '--subjects-train', default='S1,S5,S6,S7,S8', type=str, metavar='LIST',
#                         help='training subjects separated by comma')
#     parser.add_argument('-ste', '--subjects-test', default='S9,S11', type=str, metavar='LIST', help='test subjects separated by comma')
#     parser.add_argument('-a', '--actions', default='*', type=str, metavar='LIST',
#                         help='actions to train/test on, separated by comma, or * for all')
#     parser.add_argument('-c', '--checkpoint', default='checkpoint', type=str, metavar='PATH',
#                         help='checkpoint directory')
#     parser.add_argument('--checkpoint-frequency', default=10, type=int, metavar='N',
#                         help='create a checkpoint every N epochs')
#     parser.add_argument('--eva-frequency', default=5, type=int, metavar='N',
#                         help='do end-of-epoch evaluation every N epochs')
#     parser.add_argument('-r', '--resume', default='', type=str, metavar='FILENAME',
#                         help='checkpoint to resume (file name)')
#     parser.add_argument('--evaluate', default='', type=str, metavar='FILENAME', choices=['pretrained_model.bin'], help='checkpoint to evaluate (file name)')
#     parser.add_argument('--render', action='store_true', help='visualize a particular video')
#     parser.add_argument('--by-subject', action='store_true', help='break down error by subject (on evaluation)')
#     parser.add_argument('--export-training-curves', action='store_true', help='save training curves as .png images')
#     parser.add_argument('-bi', '--boneindex', default='16,15,15,14,13,12,12,11,10,9,9,8,8,7,8,11,8,14,7,0,3,2,2,1,6,5,5,4,1,0,4,0', type=str, metavar='LIST', help='bone index (each two indexs correspond to the two joints a bone)')

#     # Model arguments
#     #-s should be fixed to 1
#     parser.add_argument('-s', '--stride', default=1, type=int, metavar='N', help='chunk size to use during training')
#     parser.add_argument('-e', '--epochs', default=80, type=int, metavar='N', help='number of training epochs')
#     parser.add_argument('-b', '--batch-size', default=1024, type=int, metavar='N', help='batch size in terms of predicted frames')
#     parser.add_argument('-drop', '--dropout', default=0.25, type=float, metavar='P', help='dropout probability')
#     parser.add_argument('-lr', '--learning-rate', default=0.001, type=float, metavar='LR', help='initial learning rate')
#     parser.add_argument('-lrd', '--lr-decay', default=0.95, type=float, metavar='LR', help='learning rate decay per epoch')
#     parser.add_argument('-no-da', '--no-data-augmentation', dest='data_augmentation', action='store_false',
#                         help='disable train-time flipping')
#     parser.add_argument('-no-tta', '--no-test-time-augmentation', dest='test_time_augmentation', action='store_false',
#                         help='disable test-time flipping')
#     parser.add_argument('-arc', '--architecture', default='3,3,3', type=str, metavar='LAYERS', help='filter widths separated by comma')
#     parser.add_argument('--causal', action='store_true', help='use causal convolutions for real-time processing')
#     parser.add_argument('-ch', '--channels', default=1024, type=int, metavar='N', help='number of channels in convolution layers')
#     parser.add_argument('-l', '--randnum', default='50', type=int, metavar='N', help='number of randomly sampled frames for bone length prediction')
#     parser.add_argument('-de', '--augdegree', default='0.6', type=float, metavar='H', help='bone length augmentation degree')
#     parser.add_argument('-tem', '--temperature', default='10', type=float, metavar='H', help='temperature (attention degree) of the bone length attention module')
#     parser.add_argument('-lt', '--randnumtest', default=50, type=int, metavar='N', help='number of randomly sampled frames for bone length prediction for inference (causal mode)')
#     parser.add_argument('-jsw', '--wjs', default=2, type=float, metavar='HP', help='weight of relative joint shift loss')
#     parser.add_argument('-dw', '--wd', default=0.3, type=float, metavar='HP', help='weight of direction loss')
#     parser.add_argument('-lw', '--wl', default=100, type=float, metavar='HP', help='weight of length loss')
#     parser.add_argument('-snd', '--snd', default=0.5, type=float, metavar='HP', help='loss decay between sub-networks')

#     # Experimental
#     parser.add_argument('--subset', default=1, type=float, metavar='FRACTION', help='reduce dataset size by fraction')
#     parser.add_argument('--downsample', default=1, type=int, metavar='FACTOR', help='downsample frame rate by factor (semi-supervised)')
#     parser.add_argument('--no-eval', action='store_true', help='disable epoch evaluation while training (small speed-up)')
#     parser.add_argument('--dense', action='store_true', help='use dense convolutions instead of dilated convolutions')
#     parser.add_argument('--disable-optimizations', action='store_true', help='disable optimized model for single-frame predictions')
#     parser.add_argument('--linear-projection', action='store_true', help='use only linear coefficients for semi-supervised projection')
#     parser.add_argument('--no-bone-length', action='store_false', dest='bone_length_term',
#                         help='disable bone length term in semi-supervised settings')
#     parser.add_argument('--no-proj', action='store_true', help='disable projection for semi-supervised setting')
    
#     # Visualization
#     parser.add_argument('--viz-subject', type=str, metavar='STR', help='subject to render')
#     parser.add_argument('--viz-action', type=str, metavar='STR', help='action to render')
#     parser.add_argument('--viz-camera', type=int, default=0, metavar='N', help='camera to render')
#     parser.add_argument('--viz-video', type=str, metavar='PATH', help='path to input video')
#     parser.add_argument('--viz-skip', type=int, default=0, metavar='N', help='skip first N frames of input video')
#     parser.add_argument('--viz-output', type=str, metavar='PATH', help='output file name (.gif or .mp4)')
#     parser.add_argument('--viz-bitrate', type=int, default=3000, metavar='N', help='bitrate for mp4 videos')
#     parser.add_argument('--viz-no-ground-truth', action='store_true', help='do not show ground-truth poses')
#     parser.add_argument('--viz-limit', type=int, default=-1, metavar='N', help='only render first N frames')
#     parser.add_argument('--viz-downsample', type=int, default=1, metavar='N', help='downsample FPS by a factor N')
#     parser.add_argument('--viz-size', type=int, default=5, metavar='N', help='image size')
    
#     parser.set_defaults(bone_length_term=True)
#     parser.set_defaults(data_augmentation=True)
#     parser.set_defaults(test_time_augmentation=True)
    
#     args = parser.parse_args()
#     # Check invalid configuration
#     if args.resume and args.evaluate:
#         print('Invalid flags: --resume and --evaluate cannot be set at the same time')
#         exit()
        
#     if args.export_training_curves and args.no_eval:
#         print('Invalid flags: --export-training-curves and --no-eval cannot be set at the same time')
#         exit()

#     return args


# ###############################
# # For Debug
# #     python run.py -k cpn_ft_h36m_dbb -arc 3,3,3,3,3 --evaluate pretrained_model.bin
# ###############################

#     # Copyright (c) 2018-present, Facebook, Inc.
# # All rights reserved.
# #
# # This source code is licensed under the license found in the
# # LICENSE file in the root directory of this source tree.
# #

# import argparse

# def parse_args():
#     parser = argparse.ArgumentParser(description='Training script')

#     # General arguments
#     parser.add_argument('-d', '--dataset', default='h36m', type=str, metavar='NAME', help='target dataset') # h36m or humaneva
#     parser.add_argument('-k', '--keypoints', default='cpn_ft_h36m_dbb', type=str, choices=['cpn_ft_h36m_dbb', 'detectron_ft_h36m', 'gt'], metavar='NAME', help='2D detections to use')
#     parser.add_argument('-str', '--subjects-train', default='S1,S5,S6,S7,S8', type=str, metavar='LIST',
#                         help='training subjects separated by comma')
#     parser.add_argument('-ste', '--subjects-test', default='S9,S11', type=str, metavar='LIST', help='test subjects separated by comma')
#     parser.add_argument('-a', '--actions', default='*', type=str, metavar='LIST',
#                         help='actions to train/test on, separated by comma, or * for all')
#     parser.add_argument('-c', '--checkpoint', default='checkpoint', type=str, metavar='PATH',
#                         help='checkpoint directory')
#     parser.add_argument('--checkpoint-frequency', default=10, type=int, metavar='N',
#                         help='create a checkpoint every N epochs')
#     parser.add_argument('--eva-frequency', default=5, type=int, metavar='N',
#                         help='do end-of-epoch evaluation every N epochs')
#     parser.add_argument('-r', '--resume', default='', type=str, metavar='FILENAME',
#                         help='checkpoint to resume (file name)')
#     parser.add_argument('--evaluate', default='pretrained_model.bin', type=str, metavar='FILENAME', choices=['pretrained_model.bin'], help='checkpoint to evaluate (file name)')
#     parser.add_argument('--render', action='store_true', help='visualize a particular video')
#     parser.add_argument('--by-subject', action='store_true', help='break down error by subject (on evaluation)')
#     parser.add_argument('--export-training-curves', action='store_true', help='save training curves as .png images')
#     parser.add_argument('-bi', '--boneindex', default='16,15,15,14,13,12,12,11,10,9,9,8,8,7,8,11,8,14,7,0,3,2,2,1,6,5,5,4,1,0,4,0', type=str, metavar='LIST', help='bone index (each two indexs correspond to the two joints a bone)')

#     # Model arguments
#     #-s should be fixed to 1
#     parser.add_argument('-s', '--stride', default=1, type=int, metavar='N', help='chunk size to use during training')
#     parser.add_argument('-e', '--epochs', default=80, type=int, metavar='N', help='number of training epochs')
#     parser.add_argument('-b', '--batch-size', default=1024, type=int, metavar='N', help='batch size in terms of predicted frames')
#     parser.add_argument('-drop', '--dropout', default=0.25, type=float, metavar='P', help='dropout probability')
#     parser.add_argument('-lr', '--learning-rate', default=0.001, type=float, metavar='LR', help='initial learning rate')
#     parser.add_argument('-lrd', '--lr-decay', default=0.95, type=float, metavar='LR', help='learning rate decay per epoch')
#     parser.add_argument('-no-da', '--no-data-augmentation', dest='data_augmentation', action='store_false',
#                         help='disable train-time flipping')
#     parser.add_argument('-no-tta', '--no-test-time-augmentation', dest='test_time_augmentation', action='store_false',
#                         help='disable test-time flipping')
#     parser.add_argument('-arc', '--architecture', default='3,3,3, 3, 3', type=str, metavar='LAYERS', help='filter widths separated by comma')
#     parser.add_argument('--causal', action='store_true', help='use causal convolutions for real-time processing')
#     parser.add_argument('-ch', '--channels', default=1024, type=int, metavar='N', help='number of channels in convolution layers')
#     parser.add_argument('-l', '--randnum', default='50', type=int, metavar='N', help='number of randomly sampled frames for bone length prediction')
#     parser.add_argument('-de', '--augdegree', default='0.6', type=float, metavar='H', help='bone length augmentation degree')
#     parser.add_argument('-tem', '--temperature', default='10', type=float, metavar='H', help='temperature (attention degree) of the bone length attention module')
#     parser.add_argument('-lt', '--randnumtest', default=50, type=int, metavar='N', help='number of randomly sampled frames for bone length prediction for inference (causal mode)')
#     parser.add_argument('-jsw', '--wjs', default=2, type=float, metavar='HP', help='weight of relative joint shift loss')
#     parser.add_argument('-dw', '--wd', default=0.3, type=float, metavar='HP', help='weight of direction loss')
#     parser.add_argument('-lw', '--wl', default=100, type=float, metavar='HP', help='weight of length loss')
#     parser.add_argument('-snd', '--snd', default=0.5, type=float, metavar='HP', help='loss decay between sub-networks')

#     # Experimental
#     parser.add_argument('--subset', default=1, type=float, metavar='FRACTION', help='reduce dataset size by fraction')
#     parser.add_argument('--downsample', default=1, type=int, metavar='FACTOR', help='downsample frame rate by factor (semi-supervised)')
#     parser.add_argument('--no-eval', action='store_true', help='disable epoch evaluation while training (small speed-up)')
#     parser.add_argument('--dense', action='store_true', help='use dense convolutions instead of dilated convolutions')
#     parser.add_argument('--disable-optimizations', action='store_true', help='disable optimized model for single-frame predictions')
#     parser.add_argument('--linear-projection', action='store_true', help='use only linear coefficients for semi-supervised projection')
#     parser.add_argument('--no-bone-length', action='store_false', dest='bone_length_term',
#                         help='disable bone length term in semi-supervised settings')
#     parser.add_argument('--no-proj', action='store_true', help='disable projection for semi-supervised setting')
    
#     # Visualization
#     parser.add_argument('--viz-subject', type=str, metavar='STR', help='subject to render')
#     parser.add_argument('--viz-action', type=str, metavar='STR', help='action to render')
#     parser.add_argument('--viz-camera', type=int, default=0, metavar='N', help='camera to render')
#     parser.add_argument('--viz-video', type=str, metavar='PATH', help='path to input video')
#     parser.add_argument('--viz-skip', type=int, default=0, metavar='N', help='skip first N frames of input video')
#     parser.add_argument('--viz-output', type=str, metavar='PATH', help='output file name (.gif or .mp4)')
#     parser.add_argument('--viz-bitrate', type=int, default=3000, metavar='N', help='bitrate for mp4 videos')
#     parser.add_argument('--viz-no-ground-truth', action='store_true', help='do not show ground-truth poses')
#     parser.add_argument('--viz-limit', type=int, default=-1, metavar='N', help='only render first N frames')
#     parser.add_argument('--viz-downsample', type=int, default=1, metavar='N', help='downsample FPS by a factor N')
#     parser.add_argument('--viz-size', type=int, default=5, metavar='N', help='image size')
    
#     parser.set_defaults(bone_length_term=True)
#     parser.set_defaults(data_augmentation=True)
#     parser.set_defaults(test_time_augmentation=True)
    
#     args = parser.parse_args()
#     # Check invalid configuration
#     if args.resume and args.evaluate:
#         print('Invalid flags: --resume and --evaluate cannot be set at the same time')
#         exit()
        
#     if args.export_training_curves and args.no_eval:
#         print('Invalid flags: --export-training-curves and --no-eval cannot be set at the same time')
#         exit()

#     return args

###############################
# For Debug
#     python run.py -e 1 -k cpn_ft_h36m_dbb -arc 3,3,3 --randnum 50
###############################

    # Copyright (c) 2018-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Training script')

    # General arguments
    parser.add_argument('-d', '--dataset', default='h36m', type=str, metavar='NAME', help='target dataset') # h36m or humaneva
    parser.add_argument('-k', '--keypoints', default='cpn_ft_h36m_dbb', type=str, choices=['cpn_ft_h36m_dbb', 'detectron_ft_h36m', 'gt'], metavar='NAME', help='2D detections to use')
    parser.add_argument('-str', '--subjects-train', default='S1,S5,S6,S7,S8', type=str, metavar='LIST',
                        help='training subjects separated by comma')
    parser.add_argument('-ste', '--subjects-test', default='S9,S11', type=str, metavar='LIST', help='test subjects separated by comma')
    parser.add_argument('-a', '--actions', default='*', type=str, metavar='LIST',
                        help='actions to train/test on, separated by comma, or * for all')
    parser.add_argument('-c', '--checkpoint', default='checkpoint', type=str, metavar='PATH',
                        help='checkpoint directory')
    parser.add_argument('--checkpoint-frequency', default=10, type=int, metavar='N',
                        help='create a checkpoint every N epochs')
    parser.add_argument('--eva-frequency', default=5, type=int, metavar='N',
                        help='do end-of-epoch evaluation every N epochs')
    parser.add_argument('-r', '--resume', default='', type=str, metavar='FILENAME',
                        help='checkpoint to resume (file name)')
    parser.add_argument('--evaluate', default='', type=str, metavar='FILENAME', choices=['pretrained_model.bin'], help='checkpoint to evaluate (file name)')
    parser.add_argument('--render', action='store_true', help='visualize a particular video')
    parser.add_argument('--by-subject', action='store_true', help='break down error by subject (on evaluation)')
    parser.add_argument('--export-training-curves', action='store_true', help='save training curves as .png images')
    parser.add_argument('-bi', '--boneindex', default='16,15,15,14,13,12,12,11,10,9,9,8,8,7,8,11,8,14,7,0,3,2,2,1,6,5,5,4,1,0,4,0', type=str, metavar='LIST', help='bone index (each two indexs correspond to the two joints a bone)')

    # Model arguments
    #-s should be fixed to 1
    parser.add_argument('-s', '--stride', default=1, type=int, metavar='N', help='chunk size to use during training')
    parser.add_argument('-e', '--epochs', default=1, type=int, metavar='N', help='number of training epochs')
    parser.add_argument('-b', '--batch-size', default=1024, type=int, metavar='N', help='batch size in terms of predicted frames')
    parser.add_argument('-drop', '--dropout', default=0.25, type=float, metavar='P', help='dropout probability')
    parser.add_argument('-lr', '--learning-rate', default=0.001, type=float, metavar='LR', help='initial learning rate')
    parser.add_argument('-lrd', '--lr-decay', default=0.95, type=float, metavar='LR', help='learning rate decay per epoch')
    parser.add_argument('-no-da', '--no-data-augmentation', dest='data_augmentation', action='store_false',
                        help='disable train-time flipping')
    parser.add_argument('-no-tta', '--no-test-time-augmentation', dest='test_time_augmentation', action='store_false',
                        help='disable test-time flipping')
    parser.add_argument('-arc', '--architecture', default='3,3,3', type=str, metavar='LAYERS', help='filter widths separated by comma')
    parser.add_argument('--causal', action='store_true', help='use causal convolutions for real-time processing')
    parser.add_argument('-ch', '--channels', default=1024, type=int, metavar='N', help='number of channels in convolution layers')
    parser.add_argument('-l', '--randnum', default='50', type=int, metavar='N', help='number of randomly sampled frames for bone length prediction')
    parser.add_argument('-de', '--augdegree', default='0.6', type=float, metavar='H', help='bone length augmentation degree')
    parser.add_argument('-tem', '--temperature', default='10', type=float, metavar='H', help='temperature (attention degree) of the bone length attention module')
    parser.add_argument('-lt', '--randnumtest', default=50, type=int, metavar='N', help='number of randomly sampled frames for bone length prediction for inference (causal mode)')
    parser.add_argument('-jsw', '--wjs', default=2, type=float, metavar='HP', help='weight of relative joint shift loss')
    parser.add_argument('-dw', '--wd', default=0.3, type=float, metavar='HP', help='weight of direction loss')
    parser.add_argument('-lw', '--wl', default=100, type=float, metavar='HP', help='weight of length loss')
    parser.add_argument('-snd', '--snd', default=0.5, type=float, metavar='HP', help='loss decay between sub-networks')

    # Experimental
    parser.add_argument('--subset', default=1, type=float, metavar='FRACTION', help='reduce dataset size by fraction')
    parser.add_argument('--downsample', default=1, type=int, metavar='FACTOR', help='downsample frame rate by factor (semi-supervised)')
    parser.add_argument('--no-eval', action='store_true', help='disable epoch evaluation while training (small speed-up)')
    parser.add_argument('--dense', action='store_true', help='use dense convolutions instead of dilated convolutions')
    parser.add_argument('--disable-optimizations', action='store_true', help='disable optimized model for single-frame predictions')
    parser.add_argument('--linear-projection', action='store_true', help='use only linear coefficients for semi-supervised projection')
    parser.add_argument('--no-bone-length', action='store_false', dest='bone_length_term',
                        help='disable bone length term in semi-supervised settings')
    parser.add_argument('--no-proj', action='store_true', help='disable projection for semi-supervised setting')
    
    # Visualization
    parser.add_argument('--viz-subject', type=str, metavar='STR', help='subject to render')
    parser.add_argument('--viz-action', type=str, metavar='STR', help='action to render')
    parser.add_argument('--viz-camera', type=int, default=0, metavar='N', help='camera to render')
    parser.add_argument('--viz-video', type=str, metavar='PATH', help='path to input video')
    parser.add_argument('--viz-skip', type=int, default=0, metavar='N', help='skip first N frames of input video')
    parser.add_argument('--viz-output', type=str, metavar='PATH', help='output file name (.gif or .mp4)')
    parser.add_argument('--viz-bitrate', type=int, default=3000, metavar='N', help='bitrate for mp4 videos')
    parser.add_argument('--viz-no-ground-truth', action='store_true', help='do not show ground-truth poses')
    parser.add_argument('--viz-limit', type=int, default=-1, metavar='N', help='only render first N frames')
    parser.add_argument('--viz-downsample', type=int, default=1, metavar='N', help='downsample FPS by a factor N')
    parser.add_argument('--viz-size', type=int, default=5, metavar='N', help='image size')
    
    parser.set_defaults(bone_length_term=True)
    parser.set_defaults(data_augmentation=True)
    parser.set_defaults(test_time_augmentation=True)
    
    args = parser.parse_args()
    # Check invalid configuration
    if args.resume and args.evaluate:
        print('Invalid flags: --resume and --evaluate cannot be set at the same time')
        exit()
        
    if args.export_training_curves and args.no_eval:
        print('Invalid flags: --export-training-curves and --no-eval cannot be set at the same time')
        exit()

    return args

