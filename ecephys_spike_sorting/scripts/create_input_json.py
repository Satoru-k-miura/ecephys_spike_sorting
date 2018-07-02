import os, io, json

def createInputJson(npx_file, output_file):

	probe_directory = os.path.dirname(npx_file)
	settings_xml = os.path.join(probe_directory, 'settings.xml')

	drive, tail = os.path.split(probe_directory)

	extracted_data_directory = os.path.join(r'C:\data', tail + '_sorted')
	probe_json = os.path.join(extracted_data_directory, 'probe_info.json')
	kilosort_output_directory = os.path.join(extracted_data_directory, r'continuous\Neuropix-3a-100.0')

	dictionary = \
	{
		"npx_file": npx_file,
		"settings_xml": settings_xml,
		"probe_json" : probe_json,

		"npx_extractor_executable": "C:\\Users\\svc_neuropix\\Documents\\GitHub\\npxextractor\\Release\\NpxExtractor.exe",
		"npx_extractor_repo": "C:\\Users\\svc_neuropix\\Documents\\GitHub\\npxextractor",

	    "median_subtraction_executable": "C:\\Users\\svc_neuropix\\Documents\\GitHub\\spikebandmediansubtraction\\Builds\\VisualStudio2013\\Release\\SpikeBandMedianSubtraction.exe",
	    "median_subtraction_repo": "C:\\Users\\svc_neuropix\\Documents\\GitHub\\spikebandmediansubtraction\\",

	    "kilosort_location": "C:\\Users\\svc_neuropix\\Documents\\MATLAB",
	    "kilosort_repo": "C:\\Users\\svc_neuropix\\Documents\\GitHub\\kilosort2",
	    "kilosort_version" : 2,
	    "surface_channel_buffer" : 15,

		"directories": {
			"extracted_data_directory": extracted_data_directory,
			"kilosort_output_directory": kilosort_output_directory
		},

		"ephys_params": {
			"sample_rate" : 30000,
			"lfp_sample_rate" : 2500,
			"bit_volts" : 0.195,
			"num_channels" : 384,
			"reference_channels" : [37, 76, 113, 152, 189, 228, 265, 304, 341, 380]
		}, 

		"depth_estimation_params" : {
			"hi_noise_thresh" : 50.0,
			"lo_noise_thresh" : 3.0,
			"save_figure" : 1,
			"figure_location" : "C:\\data\\test_run",
			"smoothing_amount" : 5,
			"power_thresh" : 2.5,
			"diff_thresh" : 0.07,
			"freq_range" : [0, 10],
			"max_freq" : 150,
			"channel_range" : [370, 380],
			"n_passes" : 1,
			"air_gap" : 100,
			"skip_s_per_pass" : 100
		}, 

		"kilosort2_params" : {
			"Nfilt" : 1024,
			"Threshold" : "[4, 10, 10",
			"lam" : "[5, 20, 20]",
			"InitializeTh" : -4,
			"InitializeNFilt" : 10000
		},

		"mean_waveform_params" : {
			"samples_per_spike" : 82,
			"pre_samples" : 20,
			"num_epochs" : 3,
			"spikes_per_epoch" : 100
		},

		"noise_waveform_params" : {
			"classifier_path" : "C:\\Users\\svc_neuropix\\Documents\\GitHub\\ecephys_spike_sorting\\ecephys_spike_sorting\\modules\\noise_templates\\classifier.pkl"

		}

	}

	with io.open(output_file, 'w', encoding='utf-8') as f:
		f.write(json.dumps(dictionary, ensure_ascii=False, sort_keys=True, indent=4))

	return dictionary