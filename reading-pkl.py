import joblib

def prepare_rendering_results(vibe_results, nframes):
    frame_results = [{} for _ in range(nframes)]
    for person_id, person_data in vibe_results.items():
        for idx, frame_id in enumerate(person_data['frame_ids']):
            frame_results[frame_id][person_id] = {
                'verts': person_data['verts'][idx],
                'cam': person_data['orig_cam'][idx],
            }

    # naive depth ordering based on the scale of the weak perspective camera
    for frame_id, frame_data in enumerate(frame_results):
        # sort based on y-scale of the cam in original image coords
        sort_idx = np.argsort([v['cam'][1] for k,v in frame_data.items()])
        frame_results[frame_id] = OrderedDict(
            {list(frame_data.keys())[i]:frame_data[list(frame_data.keys())[i]] for i in sort_idx}
        )

    return frame_results

pkl2= joblib.load("vibe_output3.pkl")
pkl = joblib.load("000.pkl")
# results= prepare_rendering_results(pkl2,142)
# print(results)
print(pkl2[1].keys())
print(pkl2[1]['pose'][142][0:3])
print(pkl2[1]['global_orient'][142].shape)
print(pkl['body_pose'].shape)
print(pkl2[1]['pose'][142].shape)
print(pkl2[1]['orig_cam'][142].shape)
ljaldjas()
for key,value in pkl2.items():
    # print(value)
    print(key)
    print(value.keys())
    print(value['pose'][142].shape)
