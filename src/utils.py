import os

# Get the directory where utils.py is located (the 'src' folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level to get the project root directory
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Define paths relative to the project root
MASK_DIR = os.path.join(PROJECT_ROOT, "data", "masks")
IMGS_DIR = os.path.join(PROJECT_ROOT, "data", "imgs")
OUTPUT_CSV_PATH = os.path.join(PROJECT_ROOT, "data", "testing_features.csv")

TEST_SUBSET = [
    "PAT_10_18_830",
    "PAT_13_21_350",
    "PAT_14_22_850",
    "PAT_15_1001_749",
    "PAT_15_23_240",
    "PAT_15_3138_959",
    "PAT_16_24_691",
    "PAT_20_29_850",
    "PAT_20_30_44",
    "PAT_21_31_965",
    "PAT_21_982_266",
    "PAT_26_37_865",
    "PAT_27_38_240",
    "PAT_29_40_561",
    "PAT_8_15_820",
    "PAT_9_17_80"
]