import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric Gaussian peaks with chaotic height variations
        gaussians = np.sum(0.8 * np.exp(-3.0 * (x_scaled - 0.2)**2) * 
                          (1.0 + 0.3 * np.sin(15.0 * x_scaled)) +
                          0.4 * np.exp(-5.0 * (x_scaled + 0.6)**2) * 
                          (1.0 + 0.2 * np.cos(12.0 * x_scaled)) +
                          0.3 * np.exp(-2.0 * (x_scaled - 0.9)**2) * 
                          (1.0 + 0.4 * np.sin(8.0 * x_scaled)) +
                          0.2 * np.exp(-4.0 * (x_scaled + 0.8)**2) * 
                          (1.0 + 0.3 * np.cos(10.0 * x_scaled)))
        
        # Chaotic sinusoidal interference terms
        chaotic_sin = np.sum(np.sin(20.0 * x_scaled + np.sin(7.0 * x_scaled)) +
                           0.7 * np.cos(18.0 * x_scaled + np.cos(9.0 * x_scaled)) +
                           0.5 * np.sin(25.0 * x_scaled**2 + np.sin(11.0 * x_scaled**2)) +
                           0.3 * np.cos(15.0 * x_scaled**3 + np.cos(8.0 * x_scaled**3)))
        
        # Dynamic dimensional coupling with exponential decay
        coupling = np.sum(np.exp(-0.5 * np.abs(x_scaled)) * 
                         (1.0 + 0.5 * np.sin(6.0 * x_scaled) * np.cos(4.0 * x_scaled)) +
                         np.exp(-0.3 * np.abs(x_scaled)) * 
                         (1.0 + 0.4 * np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled)))
        
        # Cross-dimensional polynomial interactions with chaotic coefficients
        cross_poly = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**1.5 * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) +
                           (x_scaled[:-2]**3 + x_scaled[2:]**3)**1.2 * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) +
                           (x_scaled[:-1]*x_scaled[1:]) * 
                           np.sin(5.0 * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Asymmetric harmonic modulation with time-varying frequencies
        harmonics = np.sum(0.9 * np.sin(6.0 * x_scaled + 0.3 * np.sin(13.0 * x_scaled)) +
                         0.6 * np.cos(8.0 * x_scaled**2 + 0.4 * np.cos(15.0 * x_scaled**2)) +
                         0.4 * np.sin(12.0 * x_scaled**3 + 0.5 * np.sin(17.0 * x_scaled**3)))
        
        # Combine all components with adaptive weights
        return 0.3 * gaussians + 0.25 * chaotic_sin + 0.2 * coupling + 0.15 * cross_poly + 0.1 * harmonics + 2.1