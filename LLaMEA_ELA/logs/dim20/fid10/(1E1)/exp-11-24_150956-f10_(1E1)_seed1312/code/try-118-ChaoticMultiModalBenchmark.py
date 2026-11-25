import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal-like structure using recursive sine components
        fractal = np.sum(np.sin(3.0 * x_scaled) * np.sin(9.0 * x_scaled) * 
                        np.sin(27.0 * x_scaled) + 
                        0.5 * np.sin(5.0 * x_scaled**2) * np.sin(15.0 * x_scaled**2) * 
                        np.sin(45.0 * x_scaled**2))
        
        # Time-delayed feedback with chaotic dynamics
        delay_feedback = np.sum(np.sin(2.0 * x_scaled) * np.cos(3.0 * np.roll(x_scaled, 1)) + 
                              0.7 * np.sin(4.0 * x_scaled) * np.cos(5.0 * np.roll(x_scaled, 2)) + 
                              0.3 * np.sin(6.0 * x_scaled) * np.cos(7.0 * np.roll(x_scaled, 3)))
        
        # Asymmetric saddle points with varying curvature
        saddles = np.sum((x_scaled**4 - 2.0 * x_scaled**2 + 1.0) * 
                        np.exp(-0.5 * (x_scaled - 0.5)**2) + 
                        0.5 * (x_scaled**3 - x_scaled) * 
                        np.exp(-0.3 * (x_scaled + 0.3)**2))
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = np.sum(np.exp(-np.abs(x_scaled[:-1] - x_scaled[1:])) * 
                              np.sin(2.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                              0.8 * np.exp(-np.abs(x_scaled[:-2] - x_scaled[2:])) * 
                              np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Chaotic modulation with logistic map influence
        chaotic_mod = np.sum(0.5 * np.sin(10.0 * x_scaled) * 
                           (1.0 - 2.0 * np.abs(x_scaled)) + 
                           0.3 * np.sin(15.0 * x_scaled**2) * 
                           (1.0 - 2.0 * np.abs(x_scaled**2)))
        
        # Asymmetric landscape with weighted components
        return 0.4 * fractal + 0.25 * delay_feedback + 0.2 * saddles + 0.1 * cross_coupling + 0.05 * chaotic_mod + 2.1