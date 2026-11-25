import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced Gaussian peak components with varying heights, widths, and positions
        peaks = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.2)**2) + 
                      0.35 * np.exp(-3.0 * (x_scaled + 0.5)**2) + 
                      0.25 * np.exp(-7.0 * (x_scaled - 0.9)**2) + 
                      0.18 * np.exp(-2.0 * (x_scaled + 0.8)**2) + 
                      0.12 * np.exp(-4.5 * (x_scaled - 0.6)**2))
        
        # Enhanced sinusoidal modulation with higher frequencies and more complex amplitudes
        sin_mod = np.sum(np.sin(20.0 * x_scaled) * np.cos(15.0 * x_scaled) + 
                        0.7 * np.sin(25.0 * x_scaled**2) * np.cos(22.0 * x_scaled**2) + 
                        0.5 * np.sin(30.0 * x_scaled**3) * np.cos(28.0 * x_scaled**3) + 
                        0.3 * np.sin(35.0 * x_scaled**4) * np.cos(32.0 * x_scaled**4))
        
        # Enhanced adaptive dimensionality scaling with exponential decay and polynomial terms
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(5.0 * x_scaled) + 
                           0.2 * np.cos(3.0 * x_scaled**2)))
        
        # Enhanced cross-dimensional interaction terms with higher-order polynomial coupling
        cross_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) + 
                           (x_scaled[:-3]**2 + x_scaled[3:]**2) * 
                           np.sin(2.0 * (x_scaled[:-3] + x_scaled[3:])))
        
        # Enhanced multi-scale harmonic interference with phase shifts and additional frequencies
        harmonics = np.sum(np.sin(8.0 * x_scaled) * np.cos(10.0 * x_scaled) + 
                         0.9 * np.sin(12.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) + 
                         0.6 * np.sin(18.0 * x_scaled**3) * np.cos(20.0 * x_scaled**3) + 
                         0.4 * np.sin(25.0 * x_scaled**4) * np.cos(27.0 * x_scaled**4))
        
        # Additional noise and irregularity components
        noise = 0.05 * np.sum(np.sin(50.0 * x_scaled) + np.cos(45.0 * x_scaled))
        
        # Asymmetric landscape with weighted sum of all components
        return 0.3 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.12 * cross_terms + 0.1 * harmonics + 0.03 * noise + 1.8