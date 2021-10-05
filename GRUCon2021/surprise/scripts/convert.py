#!/usr/bin/env python3

from sigmf import SigMFFile, sigmffile
import numpy as np

# Load a dataset
filename = 'hamcap.sigmf-data' # extension is optional
signal = sigmffile.fromfile(filename)

# Get some metadata and all annotations
sample_rate = signal.get_global_field(SigMFFile.SAMPLE_RATE_KEY)
sample_count = signal.sample_count
signal_duration = sample_count / sample_rate
annotations = signal.get_annotations()

# Iterate over annotations
for adx, annotation in enumerate(annotations):
    annotation_start_idx = annotation[SigMFFile.START_INDEX_KEY]
    annotation_length = annotation[SigMFFile.LENGTH_INDEX_KEY]
    annotation_comment = annotation.get(SigMFFile.COMMENT_KEY, "[annotation {}]".format(adx))

    # Get capture info associated with the start of annotation
    capture = signal.get_capture_info(annotation_start_idx)
    freq_center = capture.get(SigMFFile.FREQUENCY_KEY, 0)
    freq_min = freq_center - 0.5*sample_rate
    freq_max = freq_center + 0.5*sample_rate
    print("freq_center={} freq_min={} freq_max={}".format(freq_center, freq_min, freq_max))

    # Get frequency edges of annotation (default to edges of capture)
    freq_start = annotation.get(SigMFFile.FLO_KEY)
    freq_stop = annotation.get(SigMFFile.FHI_KEY)

    # Get the samples corresponding to annotation
    samples = signal.read_samples(annotation_start_idx, -1 if annotation_length==0 else annotation_length)
    print(len(samples))

    # suppose we have an complex timeseries signal
    #data = np.zeros(1024, dtype=np.complex64)

    # write those samples to file in cf32_le
    samples.tofile('hamcap.cf32')
    samples.tofile('hamcap.complex32')