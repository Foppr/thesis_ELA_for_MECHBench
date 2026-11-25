import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric Gaussian peaks with chaotic height variations
        peak1 = 0.8 * np.exp(-3.0 * (x_scaled - 0.2)**2) * (1.0 + 0.3 * np.sin(15.0 * x_scaled))
        peak2 = 0.4 * np.exp(-5.0 * (x_scaled + 0.5)**2) * (1.0 + 0.2 * np.cos(12.0 * x_scaled))
        peak3 = 0.6 * np.exp(-2.0 * (x_scaled - 0.8)**2) * (1.0 + 0.4 * np.sin(18.0 * x_scaled))
        
        gaussian_peaks = np.sum(peak1 + peak2 + peak3)
        
        # Chaotic sine-wave modulation with dynamic frequencies
        chaotic_sin = np.sum(np.sin(10.0 * x_scaled + np.sin(7.0 * x_scaled)) + 
                           0.7 * np.sin(15.0 * x_scaled**2 + np.cos(9.0 * x_scaled)) + 
                           0.5 * np.sin(20.0 * x_scaled**3 + np.sin(11.0 * x_scaled)))
        
        # Dynamic dimensional coupling with polynomial interaction
        dim_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**1.5 * 
                            np.cos(5.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                            (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                            np.sin(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric landscape with exponential decay and phase shifts
        asym_landscape = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * 
                              (1.0 + 0.5 * np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled)) + 
                              0.3 * np.exp(-4.0 * np.abs(x_scaled**2)) * 
                              np.sin(12.0 * x_scaled))
        
        # Multi-scale harmonic interference with chaotic phase shifts
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(9.0 * x_scaled) + 
                         0.6 * np.sin(14.0 * x_scaled**2) * np.cos(13.0 * x_scaled**2) + 
                         0.4 * np.sin(22.0 * x_scaled**3) * np.cos(21.0 * x_scaled**3))
        
        # Combine all components with adaptive weights
        return 0.4 * gaussian_peaks + 0.3 * chaotic_sin + 0.15 * dim_coupling + 0.1 * asym_landscape + 0.05 * harmonics + 2.1