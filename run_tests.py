import pathlib
import logging
import os

# Importing the solution
from solution import find_common_node

# Setup Logger and log to a file
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    filename='test_results.log',
                    level=logging.DEBUG)

logging.info("\n")
logging.info(("==== " * 4) + "Starting New Run " + ("==== " * 4))

# Globals
DATASET_PATH = os.path.join(pathlib.Path().absolute(), "data.txt")
logging.info(f"Loading dataset from : {DATASET_PATH}")

# Test Results
samples_to_evaluate = [{
    "node_a": 290,
    "node_b": 10,
    "expected_label": 5,
}, {
    "node_a": 128,
    "node_b": 130,
    "expected_label": 129,
}, {
    "node_a": 762,
    "node_b": 762,
    "expected_label": 918,
}, ]

for sample_index, sample in enumerate(samples_to_evaluate):
    node_a = sample["node_a"]
    node_b = sample["node_b"]
    expected_label = sample["expected_label"]
    logging.info(f"sample #{sample_index}: node_a={node_a}, node_b={node_b}")

    actual_label = find_common_node(data_set_path=DATASET_PATH,
                                    node_a=node_a,
                                    node_b=node_b)

    if type(actual_label) != int:
        logging.warning(
            f"The expected label should be `int`, instead received {type(actual_label).__name__}")
        actual_label = int(actual_label)

    is_label_expected = actual_label == expected_label

    logging.log(level=20 if is_label_expected else 30,
                msg=f"expected={expected_label}, actual={actual_label}")

# End Message
logging.info(("==== " * 2) + "Please do not delete this file or it's contents.")
logging.info(("==== " * 2) + "It's ok to keep the results of your multiple runs. "
                             "In such cases we will consider the last run.")
logging.info(("==== " * 4) + "Run Complete " + ("==== " * 4))
