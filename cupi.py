import tensorflow as tf

# Define the feature description dictionary that matches the data schema in the TFRecord file
feature_description = {
    'feature1': tf.io.FixedLenFeature([], tf.float32),
    'feature2': tf.io.FixedLenFeature([], tf.int64),
    'feature3': tf.io.VarLenFeature(tf.string),
}

# Function to parse a single example
def _parse_function(example_proto):
    # Parse the input tf.train.Example proto using the specified feature description
    return tf.io.parse_example(example_proto, feature_description)

# Create a TFRecordDataset
raw_dataset = tf.data.TFRecordDataset('path/to/your/tfrecord/file.tfrecord')

# Map the parse function to each example in the dataset
parsed_dataset = raw_dataset.map(_parse_function)

# Iterate over the dataset and print out each parsed example
for parsed_record in parsed_dataset:
    print(parsed_record)
