[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10044151.svg)](https://doi.org/10.5281/zenodo.10044151)
# Adaptive Filter for Acoustic Signal Segmentation

In the realm of modern signal processing, the application of gradient-based optimization frameworks offers groundbreaking solutions to complex challenges. This repository presents our innovative adaptive filter designed for segmenting acoustic signals. The work here is grounded in our research published in Nature Communications, titled "Harmonizing Sound and Light: X-Ray Imaging Unveils Acoustic Signatures of Stochastic Inter-Regime Instabilities during Laser Melting".


## Installation

1. Clone the repository.
2. Install the required libraries and dependencies:
```
pip install -r requirements.txt
```

## Usage

1. **Binary Acoustic Signal Segmentation**: For segmenting the acoustic signal into the two predominant melting regimes, refer to the `Binary.ipynb` notebook.
2. **Ternary Acoustic Signal Segmentation**: For a more advanced segmentation into three melting regimes, refer to the `Ternary.ipynb` notebook.
3. **Time Series Analysis and Visualization**: For an in-depth analysis and visualization of the time series data recorded in our experiments, refer to the `GroundTruth and Data Visualization.ipynb` notebook.

All notebooks provide detailed implementation, training processes, and visualization of results.

## Repository Structure

- `Binary.ipynb`: Jupyter notebook detailing the binary acoustic signal segmentation.
- `Ternary.ipynb`: Jupyter notebook detailing the ternary acoustic signal segmentation.
- `GroundTruth and Data Visualization.ipynb`: Jupyter notebook for time series analysis and visualization.
- `Models/`: Directory containing trained models.
- `Database/`: Directory storing the data and ground truth used for training and testing.
- `requirements.txt`: List of libraries and dependencies required for this project.

## Results

Our adaptive filter achieved high accuracy in segmenting acoustic signals. Detailed results, including visualizations and evaluations, are available within the respective Jupyter notebooks.

## Paper Accessibility

The paper accompanying this research is accessible via the following DOI: [https://doi.org/10.21203/rs.3.rs-2607808/v1](https://doi.org/10.21203/rs.3.rs-2607808/v1). Please refer to this link for the complete description and related materials.

## Contribution

We welcome contributions! If you wish to contribute, please follow the standard GitHub pull request process:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request for review.

Ensure your code adheres to the guidelines and standards set forth in this repository.

## Credits

This work is based on our research article published in Nature Communications:

**"Harmonizing Sound and Light: X-Ray Imaging Unveils Acoustic Signatures of Stochastic Inter-Regime Instabilities during Laser Melting"**  
Authors: Milad Hamidi Nasab, Giulio Masinelli, Charlotte de Formanoir, Lucas Schlenger, Steven Van Petegem, Reza Esmaeilzadeh, Kilian Wasmer, Ashish Ganvir, Antti Salminen, Florian Aymanns, Federica Marone, Vigneashwara Pandiyan, Sneha Goel, Roland Logé.

## License

This project is licensed under the CC0 1.0 Universal License. Please refer to the [LICENSE](./LICENSE) file for more details.

## Contact

For any queries or collaborations related to this part of the publication, please reach out to Giulio Masinelli at [giulio.masinelli@empa.ch](mailto:giulio.masinelli@empa.ch).
