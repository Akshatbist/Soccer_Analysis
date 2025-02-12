# Soccer Analysis
![Image](https://github.com/user-attachments/assets/fd2d8c9c-01aa-4799-b132-e0201f603bff)

This project is designed to analyze soccer videos by tracking player and ball movements, estimating camera movements, transforming views, and calculating speed and distance metrics. The output is an annotated video with detailed information about player positions, ball possession, and other metrics.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/Soccer_Analysis.git
   cd Soccer_Analysis
   ```

2. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Set up the environment variables in the [.env](http://_vscodecontentref_/8) file.

## Usage

1. Place your input video in the [input_videos](http://_vscodecontentref_/9) directory.

2. Run the main script:

   ```sh
   python main.py
   ```

3. The output video with annotations will be saved in the [output_videos] directory.

## Components

- **Trackers**: Tracks the objects (players and ball) in the video.
- **Camera Movement Estimator**: Estimates the camera movement and adjusts the object positions accordingly.
- **View Transformer**: Transforms the view to a top-down perspective.
- **Speed and Distance Estimator**: Calculates the speed and distance covered by the players.
- **Team Assigner**: Assigns team colors to the players.
- **Player Ball Assigner**: Determines which player has possession of the ball.

## Training

The training scripts and data are located in the [training]directory. You can use the provided Jupyter notebooks to train your models.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or issues, please open an issue on the GitHub repository.
