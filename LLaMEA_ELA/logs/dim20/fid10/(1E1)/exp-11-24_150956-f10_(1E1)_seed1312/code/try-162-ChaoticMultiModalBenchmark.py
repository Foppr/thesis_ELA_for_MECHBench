import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric Gaussian peaks with chaotic modulation
        gaussians = np.sum(0.8 * np.exp(-3.0 * (x_scaled - 0.2)**2) * 
                          (1.0 + 0.3 * np.sin(15.0 * x_scaled)) +
                          0.4 * np.exp(-5.0 * (x_scaled + 0.6)**2) * 
                          (1.0 + 0.2 * np.cos(12.0 * x_scaled)) +
                          0.3 * np.exp(-2.0 * (x_scaled - 0.9)**2) * 
                          (1.0 + 0.4 * np.sin(8.0 * x_scaled)))
        
        # Chaotic sinusoidal interactions with varying frequencies
        chaotic_sin = np.sum(np.sin(20.0 * x_scaled + np.sin(7.0 * x_scaled)) +
                           0.7 * np.cos(18.0 * x_scaled + np.cos(9.0 * x_scaled)) +
                           0.5 * np.sin(25.0 * x_scaled**2 + np.sin(5.0 * x_scaled**2)))
        
        # Adaptive dimensional coupling with polynomial interactions
        dim_coupling = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                            np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) +
                            (x_scaled[:-2]**2 * x_scaled[2:]) * 
                            np.sin(4.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric cross-dimensional terms with exponential decay
        asym_cross = np.sum(np.exp(-2.0 * np.abs(x_scaled[:-1])) * 
                          np.sin(6.0 * x_scaled[:-1]) * 
                          np.cos(3.0 * x_scaled[1:]) +
                          0.5 * np.exp(-1.5 * np.abs(x_scaled[:-2])) * 
                          np.cos(5.0 * x_scaled[:-2]) * 
                          np.sin(4.0 * x_scaled[2:]))
        
        # Multi-scale chaotic interference with phase modulation
        chaos_interference = np.sum(np.sin(10.0 * x_scaled + 0.3 * np.sin(20.0 * x_scaled)) +
                                 0.6 * np.cos(15.0 * x_scaled**2 + 0.4 * np.cos(18.0 * x_scaled**2)) +
                                 0.3 * np.sin(22.0 * x_scaled**3 + 0.5 * np.sin(12.0 * x_scaled**3)))
        
        # Weighted sum with asymmetric contribution
        return 0.4 * gaussians + 0.3 * chaotic_sin + 0.15 * dim_coupling + 0.1 * asym_cross + 0.05 * chaos_interference + 2.1