import cv2
import numpy as np

# Define a function to track the object
def start_tracking():
    # Iniatilize the video capture object
    cap = cv2.VideoCapture(0)

    # Define the scaling factor for the frame s
    scaling_factor = 0.40

    # Number of frames to track 
    num_frames_to_track = 5

    # Skipping factor 
    num_frames_jump = 2

    #Initialize variables
    tracking_paths = []
    frame_index = 0

    # Define tracking parameters 
    tracking_paths = dict(winSize = (11,11), maxlevel =2,
        criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                    10, 0.03))

    # Iterate until the users hits the 'Esc' key
    while True:
        # Capture the frame
        _, frame = cap.read()

        # Resize the frame
        frame = cv2.resize(frame, None, fx = scaling_factor, fy= scaling_factor,
                           interpolation = cv2.INTER_AREA )

        # Convert to grayscale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Create output image
        output_img = frame.copy()

        if len(tracking_paths) > 0:
            # Get Images
            prev_img, current_img = prev_gray, frame_gray

            # Organize the feature points
            feature_points_0 = np.float32([tp[-1] for tp in \
                tracking_paths]).reshape(-1, 1, 2)

            # Compute optical flow 
            feature_points_1, _, _ = cv2.calcOpticalFlowPyrLK(
                prev_img, current_img, feature_points_0,
                None, **tracking_params)

            # Compute revere optical flow
            feature_points_0_rev, _, _ = cv2.calcOpticalFlowPyrLK(
                prev_img, prev_img, feature_points_1,
                None, **tracking_params)

            # Compute the difference between forward and 
            # reverse optical flow
            diff_feature_points = abs(feature_points_0 - \
                feature_points_0_rev).reshape(-1,2).max(-1)
 
            # Extract the good points 
            good_points = diff_feature_points < 1

            # Initialize the points
            new_tracking_paths = []

            # Iterate through all the good feature points
            for tp, (x, y), good_points_flag in zip(tracking_paths,
                        feature_points_1.reshape(-1, 2), good_points):
                        # if the flag is not true , then continue
                        if not good_points_flag:
                            continue

                        # Append the X and Y coordinates and check if
                        # its length is greater than the threshold
                        tp.append((x,y))
                        if len(tp) > num_frames_to_track:
                            del tp[0] 

                        new_tracking_paths.append(tp)

                        # Draw a circle around the feature points
                        cv2.circle(output_img, (x,y), 3, (0, 255, 0) -1)

            # Update the tracking paths
            tracking_paths = new_tracking_paths

            # Draw lines
            cv2.polylines(output_img, [np.int32(tp) for tp in \
              tracking_paths], False, (0, 150, 0))

        # Go into this 'if' condition  after skipping the
        # right numbers of frames
        if not frame_index % num_frames_jump:
            # Create a mask and drow the circles
            mask = np.zeros_like(frame_gray)
            mask[:] = 255
            for x,y in [np.int32(tp[-1]) for tp in tracking_paths]:
                cv2.circle(mask, (x,y), 6, 0 ,-1)

            # Compute the features to track
            feature_points = cv2.goodFeaturesToTrack(frame_gray,
               mask = mask, maxCorners = 500, qualityLevel = 0.3,
               minDistance= 7,blockSize = 7)
    
            # Check if feature point exist. IF so, append them
            # to the tracking paths
            if feature_points is not None:
                for x,y in np.float32(feature_points).reshape(-1, 2):
                   tracking_paths.append([(x,y)])

        # Update the variables
        frame_index += 1
        prev_gray = frame_gray

        # Display output
        cv2.imshow('Optical Flow', output_img)

        # Check if the user enter 'Esc' key
        c = cv2.waitKey(1)
        if c == 27:
            break

if __name__ == '__main__':
    # Start the tracker
    start_tracking()

    # CLose all the windows
    cv2.destroyAllWindows()     