import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced Gaussian peak components with varied heights, widths, and positions
        peaks = np.sum(0.7 * np.exp(-3.5 * (x_scaled - 0.25)**2) + 
                      0.3 * np.exp(-2.0 * (x_scaled + 0.5)**2) + 
                      0.2 * np.exp(-5.0 * (x_scaled - 0.7)**2) + 
                      0.15 * np.exp(-1.8 * (x_scaled + 0.9)**2))
        
        # Increased sinusoidal complexity with higher frequencies and more terms
        sin_mod = np.sum(np.sin(15.0 * x_scaled) * np.cos(12.0 * x_scaled) + 
                        0.7 * np.sin(20.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                        0.5 * np.sin(28.0 * x_scaled**3) * np.cos(25.0 * x_scaled**3) + 
                        0.3 * np.sin(35.0 * x_scaled**4) * np.cos(32.0 * x_scaled**4))
        
        # Enhanced dimensionality scaling with additional harmonic components
        dim_scaling = np.sum(np.exp(-0.7 * np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(5.0 * x_scaled) + 
                           0.3 * np.cos(3.0 * x_scaled)))
        
        # Stronger cross-dimensional interaction terms with higher-order coupling
        cross_terms = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2)**1.5 * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) + 
                           (x_scaled[:-3]**4 + x_scaled[3:]**4) * 
                           np.sin(2.5 * (x_scaled[:-3] + x_scaled[3:])))
        
        # Multi-scale harmonic interference with more complex phase relationships
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.9 * np.sin(10.0 * x_scaled**2) * np.cos(13.0 * x_scaled**2) + 
                         0.6 * np.sin(18.0 * x_scaled**3) * np.cos(22.0 * x_scaled**3) + 
                         0.4 * np.sin(25.0 * x_scaled**4) * np.cos(30.0 * x_scaled**4))
        
        # Asymmetric landscape with modified weighted sum and additional noise component
        noise = 0.05 * np.random.rand()
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + 1.5 + noise