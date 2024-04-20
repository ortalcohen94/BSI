
SEED_NUMBER = None
ZERO_FEATURES = False
PERFORM_WARMPUP = False
USE_TEST_GROUP = False
USE_MSE_LOSS = True
FT_FEATURE_SIZE = 128
NOT_USE_MSE_LOSS = False 
ZERO_VISITS = False
BERT_LR = 0
ATTN_DEPTH =  6 #6 #DONE
MODEL_PARAMS_PREFIX = 'module__'
FEATURE_ATTN_DEPTH = 6 #DONE
SAMPLE_PRECENTAGE = 0 #DONE
LAMBDA_PARAM = 0 #DONE
NUM_VISITS_BEFORE = 0 #DONE
ACTIVATION_LAYER = "GELU" #LeakyReLU" #DONE
ACTIVATION_LAYER_PARAMS = [] #Done
NUM_LAYERS_FREEZE = 0 #done
K_FOLD_SIZE = None #done
SAMPLE_FACTOR_TRAINING = 1 #DONE
NUM_WORKERS = 4 #DONE
USE_CNN = False #DONE
SCORE_TYPE = "focal" #can be (fms, f1, focal, bce) #Done
FOCAL_GAMMA = 2 #DONE
FOCAL_ALPHA = 0.25 # 0.9 #DONE
MAX_GRAD_NORM = 2 #DONE
RESERVE_P = 0.8 #The lower the reserve p is, the less params are trained. #DONE
IS_PRETRAINING = False #DONE
DATA_GETTER_POSTFIX = '_postprocessed_tensor' #DONE 
TRANSFORMER_TYPE = "Regular" #(can be "Regular", "LRP") #DONE
USE_COMBINATION_AS_TRAIN_SET = False #DONE
ENSEMBLE_SIZE = 1 #DONE
TRAIN_FEATURE_TRANSFORMER = False #DONE
XAVIER_GAIN = 0.15 #0.1 #0.5 #DONE
FEATURE_DROPOUT = 0.3 #.1 #0.05  #DONE
FEATURE_WEIGHT_DECAY = 1e-16 
FEATURE_LR = 1e-4 #5e-5 
SHOULD_USE_GCT_COMPONENT = True
ADDITIONAL_NAME = ""  #DONE
NUM_MESUREMENTS = 100   #DONE
NUM_LAST_VISITS = 1
FEATURES_INFO_PRECENTAGE_FOR_STAY_LOWER_THRESHOLD = 0#.3
STAY_INFO_PRECENTAGE_LOW_THRESHOLD = 0

USE_RNN = False
USE_LSTM = False
USE_SIMPLE_MODEL = False
DO_WARMUP = True
USE_INIT_DATA = False

CALC_EXTERNAL = False
OPTIMIZER = "ChildTuningAdamW"

LOCATION_WEIGHTS = None
HIDDEN_LAYERS = 0
NUM_WORMUP_STEPS = 0
WEIGHT_DECAY = 0
WARMUP_PRECENTAGE = 0
NUM_LEFT_STEPS = 0
DROPOUT = 0
CONDUCT_TRANSFER_LEARNING = False
#Can be ("rnn", "lstm", 
# "reconstruction_mimiciv", "bsi_mimiciv_train", "bsi_mimiciv_train_no_gct")
experiment_name = "bsi_mimiciv_train"

if experiment_name == "simple":
    ZERO_FEATURES = False
    ZERO_VISITS = False
    CURR_TASK = 'bsi'
    NUM_EXPERIMENTS = 10
    NUM_MESUREMENTS = 100
    NUM_HOURS_FOR_WINDOW = 4
    NUM_TRAINING_HOURS = 5 * 24 
    MAX_VISITS = int(NUM_TRAINING_HOURS // NUM_HOURS_FOR_WINDOW)
    DEVICE_NUM = 1
    ADDITIONAL_NAME = ""
    DF_PRECENTAGE = 1
    MBSZ = 512
    TEST_VAL_PRECENTAGE = 0.2
    FT_EPOCHS = 1

elif experiment_name == "bsi_mimiciv_train":
#BSI - Only eICU
    RESERVE_P = 0.6
    LOCATION_WEIGHTS = "outputs/Weights/Transformerreconstruction_mimiciv_no_transfer"
    USE_TEST_GROUP = True
    ADDITIONAL_NAME = ""
    NUM_EXPERIMENTS = 10
    MBSZ =  17 #DONE
    DROPOUT = 0.5 #DONE
    FEATURE_DROPOUT = 0.3
    TEST_VAL_PRECENTAGE = 0.1
    FT_EPOCHS =  2 #20 #DONE
    LR = 1e-3 #DONE
    WEIGHT_DECAY = 0.3  #DONE
    HIDDEN_LAYERS = [1024, 512] #Was 512   #DONE
    NUM_LAST_VISITS = int(1) #12   #DONE
    WARMUP_PRECENTAGE = 0.2    #DONE
    NUM_WORMUP_STEPS = int(SAMPLE_FACTOR_TRAINING *FT_EPOCHS * WARMUP_PRECENTAGE * (10000  / MBSZ ))   #DONE
    NUM_LEFT_STEPS = int(SAMPLE_FACTOR_TRAINING  * FT_EPOCHS * (1 - WARMUP_PRECENTAGE) * (10000 / MBSZ ))    #DONE
    BERT_LR = 2e-3
    EARLY_STOPPING_EPOCHS = 4     #DONE
    CONDUCT_TRANSFER_LEARNING = True if TRANSFORMER_TYPE == "Regular" else False
    OPTIM_TYPE = "ChildTuning-D" if CONDUCT_TRANSFER_LEARNING else 'AdamW'
    CURR_TASK = 'bsi'
    USE_MIMIC_AS_TEST_DATA = False
    USE_INIT_DATA = False
    MIMIC_PRECENTAGE_IN_TRAINING_DATA = 0 
    FEATURES_INFO_PRECENTAGE_FOR_STAY_LOWER_THRESHOLD = 0#.3
    STAY_INFO_PRECENTAGE_LOW_THRESHOLD = 0
    SHOULD_USE_VAL_SET = False
    MONITOR_TYPE = 'val_roc_auc_best' if SHOULD_USE_VAL_SET else 'roc_auc_best'
    OUTLIERS_HIGHER_THRESHOLD = -1.5
    NUM_HOURS_FOR_WINDOW = 4
    NUM_TRAINING_HOURS = 5 * 24 
    MAX_VISITS = int(NUM_TRAINING_HOURS // NUM_HOURS_FOR_WINDOW)
    DF_PRECENTAGE = 1
    DEVICE_NUM = 0
    USE_SAMPLER = True
    ENSEMBLE_SIZE = 1
    SCORE_TYPE = "focal"
    CALC_EXTERNAL = True
    ZERO_FEATURES = True
    SAMPLE_PRECENTAGE = 0 #0.05
    PERFORM_WARMPUP = False

elif experiment_name == "bsi_mimiciv_train_no_gct":
#BSI - Only eICU
    SHOULD_USE_GCT_COMPONENT = False
    USE_MSE_LOSS = False
    RESERVE_P = 0.6
    LOCATION_WEIGHTS = None
    USE_TEST_GROUP = True
    ADDITIONAL_NAME = ""
    NUM_EXPERIMENTS = 10
    MBSZ =  17 #DONE
    DROPOUT = 0.6 #DONE
    FEATURE_DROPOUT = 0.3
    TEST_VAL_PRECENTAGE = 0.1
    FT_EPOCHS = 5 #20 #DONE
    LR = 1e-3 #DONE
    WEIGHT_DECAY = 0.3  #DONE
    HIDDEN_LAYERS = [1024, 512] #Was 512   #DONE
    NUM_LAST_VISITS = int(1) #12   #DONE
    WARMUP_PRECENTAGE = 0.2    #DONE
    NUM_WORMUP_STEPS = int(SAMPLE_FACTOR_TRAINING *FT_EPOCHS * WARMUP_PRECENTAGE * (10000  / MBSZ ))   #DONE
    NUM_LEFT_STEPS = int(SAMPLE_FACTOR_TRAINING  * FT_EPOCHS * (1 - WARMUP_PRECENTAGE) * (10000 / MBSZ ))    #DONE
    BERT_LR = 1e-4
    EARLY_STOPPING_EPOCHS = 4     #DONE
    CONDUCT_TRANSFER_LEARNING = True if TRANSFORMER_TYPE == "Regular" else False
    OPTIM_TYPE = "ChildTuning-D" if CONDUCT_TRANSFER_LEARNING else 'AdamW'
    CURR_TASK = 'bsi'
    USE_MIMIC_AS_TEST_DATA = False
    USE_INIT_DATA = False
    MIMIC_PRECENTAGE_IN_TRAINING_DATA = 0 
    FEATURES_INFO_PRECENTAGE_FOR_STAY_LOWER_THRESHOLD = 0#.3
    STAY_INFO_PRECENTAGE_LOW_THRESHOLD = 0
    SHOULD_USE_VAL_SET = False
    MONITOR_TYPE = 'val_roc_auc_best' if SHOULD_USE_VAL_SET else 'roc_auc_best'
    OUTLIERS_HIGHER_THRESHOLD = -1.5
    NUM_HOURS_FOR_WINDOW = 4
    NUM_TRAINING_HOURS = 5 * 24 
    MAX_VISITS = int(NUM_TRAINING_HOURS // NUM_HOURS_FOR_WINDOW)
    DF_PRECENTAGE = 1
    DEVICE_NUM = 0
    USE_SAMPLER = True
    ENSEMBLE_SIZE = 1
    SCORE_TYPE = "focal"
    CALC_EXTERNAL = True
    ZERO_FEATURES = True
    SAMPLE_PRECENTAGE = 0 #0.05
    PERFORM_WARMPUP = False



elif experiment_name == "reconstruction_mimiciv":
    CURR_TASK = 'reconstruction_mimiciv'
    LOCATION_WEIGHTS = "outputs/MIMICIV-Experiments/ratchet_tl/best_best_model_Transformerreconstruction_mimiciv_no_transfer"
    USE_TEST_GROUP = False
    ZERO_VISITS = True
    ZERO_FEATURES = True
    CONDUCT_TRANSFER_LEARNING = False
    IS_PRETRAINING = True
    NOT_USE_MSE_LOSS = True
    MBSZ =  32 #32 * 4 
    DROPOUT = 0.1
    FEATURE_DROPOUT = 0.1
    TEST_VAL_PRECENTAGE = 0.1
    FT_EPOCHS = 100 #000 #5 #4000
    LAMBDA_PARAM = 0.0001 #1
    LR = 1e-4 #0.0000001
    WEIGHT_DECAY = 0.2 #1e-5
    HIDDEN_LAYERS = [100]
    NUM_LAST_VISITS = 10 #3 #12
    NUM_WORMUP_STEPS = int(FT_EPOCHS * 0.1)
    BERT_LR = 1e-4 #1e-7 #1e-7 #1e-16
    EARLY_STOPPING_EPOCHS = 1
    MAX_VISITS = int(512) #int(512)
    SAMPLE_PRECENTAGE = 0.4
    FEATURE_SAMPLE_PRECENTAGE = 0.3
    USE_CNN = False
    SCORE_TYPE = None
    K_FOLD_SIZE = 10
    MAX_GRAD_NORM = 0.5
    OPTIM_TYPE = None
    DEVICE_NUM = 0
    TRAIN_FEATURE_TRANSFORMER = False
    DF_PRECENTAGE = 1 #0.01  #0.01 #0.1
    WARMUP_PRECENTAGE = 0.2 * 10
    NUM_WORMUP_STEPS = int(SAMPLE_FACTOR_TRAINING * FT_EPOCHS * WARMUP_PRECENTAGE * (DF_PRECENTAGE * 140000  / MBSZ ))
    NUM_LEFT_STEPS = int(SAMPLE_FACTOR_TRAINING *  FT_EPOCHS * (1 - WARMUP_PRECENTAGE) * (DF_PRECENTAGE * 140000 / MBSZ ))
    NUM_HOURS_FOR_WINDOW = 4
    OPTIMIZER = "AdamW"

elif experiment_name == "reconstruction_mimiciv_no_gct":
    SHOULD_USE_GCT_COMPONENT = False
    USE_MSE_LOSS = False
    CURR_TASK = 'reconstruction_mimiciv'
    LOCATION_WEIGHTS = "outputs/MIMICIV-Experiments/ratchet_tl/best_best_model_Transformerreconstruction_mimiciv_no_transfer"
    USE_TEST_GROUP = False
    ZERO_VISITS = True
    ZERO_FEATURES = True
    CONDUCT_TRANSFER_LEARNING = False
    IS_PRETRAINING = True
    NOT_USE_MSE_LOSS = True
    MBSZ =  32 #32 * 4 
    DROPOUT = 0.1
    FEATURE_DROPOUT = 0.1
    TEST_VAL_PRECENTAGE = 0.1
    FT_EPOCHS = 100 #000 #5 #4000
    LAMBDA_PARAM = 0.0001 #1
    LR = 1e-4 #0.0000001
    WEIGHT_DECAY = 0.2 #1e-5
    HIDDEN_LAYERS = [100]
    NUM_LAST_VISITS = 10 #3 #12
    NUM_WORMUP_STEPS = int(FT_EPOCHS * 0.1)
    BERT_LR = 1e-4 #1e-7 #1e-7 #1e-16
    EARLY_STOPPING_EPOCHS = 1
    MAX_VISITS = int(512) #int(512)
    SAMPLE_PRECENTAGE = 0.4
    FEATURE_SAMPLE_PRECENTAGE = 0.3
    USE_CNN = False
    SCORE_TYPE = None
    K_FOLD_SIZE = 10
    MAX_GRAD_NORM = 0.5
    OPTIM_TYPE = None
    DEVICE_NUM = 0
    TRAIN_FEATURE_TRANSFORMER = False
    DF_PRECENTAGE = 1 #0.01  #0.01 #0.1
    WARMUP_PRECENTAGE = 0.2 * 10
    NUM_WORMUP_STEPS = int(SAMPLE_FACTOR_TRAINING * FT_EPOCHS * WARMUP_PRECENTAGE * (DF_PRECENTAGE * 140000  / MBSZ ))
    NUM_LEFT_STEPS = int(SAMPLE_FACTOR_TRAINING *  FT_EPOCHS * (1 - WARMUP_PRECENTAGE) * (DF_PRECENTAGE * 140000 / MBSZ ))
    NUM_HOURS_FOR_WINDOW = 4
    OPTIMIZER = "AdamW"


elif experiment_name == "lstm":
    USE_LSTM = True
    USE_TEST_GROUP = True
    ADDITIONAL_NAME = "_mimiciv"
    NUM_EXPERIMENTS = 10
    RNN_LAYERS = 1
    DO_WARMUP = False
    RNN_HIDDEN_SIZE = 64
    USE_SIMPLE_MODEL = True
    USE_LSTM = True
    MBSZ =  128 
    DROPOUT = 0.6
    TEST_VAL_PRECENTAGE = 0.3
    FT_EPOCHS = 10 #20
    LR = 1e-5
    WEIGHT_DECAY = 0.02 #0.02 
    HIDDEN_LAYERS = [128]
    NUM_LAST_VISITS = int(1) #12
    WARMUP_PRECENTAGE = 0
    NUM_WORMUP_STEPS = int(SAMPLE_FACTOR_TRAINING * FT_EPOCHS * WARMUP_PRECENTAGE * (1913  / MBSZ ))
    NUM_LEFT_STEPS = int(SAMPLE_FACTOR_TRAINING *  FT_EPOCHS * (1 - WARMUP_PRECENTAGE) * (1913 / MBSZ ))
    EARLY_STOPPING_EPOCHS = 4 
    NUM_HOURS_FOR_WINDOW = 4 #0.5
    NUM_TRAINING_HOURS = 5 * 24
    MAX_VISITS = int(NUM_TRAINING_HOURS // NUM_HOURS_FOR_WINDOW)
    CONDUCT_TRANSFER_LEARNING = False
    OPTIM_TYPE = 'AdamW'
    CURR_TASK = 'bsi'
    USE_MIMIC_AS_TEST_DATA = False
    USE_INIT_DATA = False
    MIMIC_PRECENTAGE_IN_TRAINING_DATA = 0
    FEATURES_INFO_PRECENTAGE_FOR_STAY_LOWER_THRESHOLD = 0
    USE_MSE_LOSS = False
    STAY_INFO_PRECENTAGE_LOW_THRESHOLD = 0
    SHOULD_USE_VAL_SET = False
    MONITOR_TYPE = 'val_roc_auc_best' if SHOULD_USE_VAL_SET else 'roc_auc_best'
    OUTLIERS_HIGHER_THRESHOLD = -1.5
    STAY_INFO_PRECENTAGE_LOW_THRESHOLD_VAL_TEST = 0
    DF_PRECENTAGE = 1
    DEVICE_NUM = 0
    USE_SAMPLER = True
    ENSEMBLE_SIZE = 1
    SCORE_TYPE = "bce"
    OPTIMIZER = "AdamW"

elif experiment_name == "rnn":
    USE_RNN = True
    USE_TEST_GROUP = True
    ADDITIONAL_NAME = "_mimiciv"
    NUM_EXPERIMENTS = 10
    RNN_LAYERS = 1
    DO_WARMUP = False
    RNN_HIDDEN_SIZE = 64
    USE_SIMPLE_MODEL = True
    MBSZ =  128
    DROPOUT = 0.7
    TEST_VAL_PRECENTAGE = 0.3
    FT_EPOCHS = 10 #20
    LR = 1e-5
    WEIGHT_DECAY = 0.02 #0.02 
    HIDDEN_LAYERS = [128]
    NUM_LAST_VISITS = int(1) #12
    WARMUP_PRECENTAGE = 0
    NUM_WORMUP_STEPS = int(SAMPLE_FACTOR_TRAINING * FT_EPOCHS * WARMUP_PRECENTAGE * (1913  / MBSZ ))
    NUM_LEFT_STEPS = int(SAMPLE_FACTOR_TRAINING *  FT_EPOCHS * (1 - WARMUP_PRECENTAGE) * (1913 / MBSZ ))
    EARLY_STOPPING_EPOCHS = 4 
    NUM_HOURS_FOR_WINDOW = 4 #0.5
    NUM_TRAINING_HOURS = 5 * 24
    MAX_VISITS = int(NUM_TRAINING_HOURS // NUM_HOURS_FOR_WINDOW)
    CONDUCT_TRANSFER_LEARNING = False
    OPTIM_TYPE = 'AdamW'
    CURR_TASK = 'bsi'
    USE_MIMIC_AS_TEST_DATA = False
    USE_INIT_DATA = False
    MIMIC_PRECENTAGE_IN_TRAINING_DATA = 0
    FEATURES_INFO_PRECENTAGE_FOR_STAY_LOWER_THRESHOLD = 0
    USE_MSE_LOSS = False
    STAY_INFO_PRECENTAGE_LOW_THRESHOLD = 0
    SHOULD_USE_VAL_SET = False
    MONITOR_TYPE = 'val_roc_auc_best' if SHOULD_USE_VAL_SET else 'roc_auc_best'
    OUTLIERS_HIGHER_THRESHOLD = -1.5
    STAY_INFO_PRECENTAGE_LOW_THRESHOLD_VAL_TEST = 0
    DF_PRECENTAGE = 1
    DEVICE_NUM = 0
    USE_SAMPLER = True
    ENSEMBLE_SIZE = 1
    SCORE_TYPE = "bce"
    OPTIMIZER = "AdamW"