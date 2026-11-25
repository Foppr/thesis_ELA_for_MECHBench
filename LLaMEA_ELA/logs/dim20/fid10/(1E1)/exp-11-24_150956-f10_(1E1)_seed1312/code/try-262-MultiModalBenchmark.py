import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced Gaussian peak components with chaotic height variations
        peaks = np.sum(0.8 * np.exp(-5.0 * (x_scaled - 0.3)**2) + 
                      0.4 * np.exp(-3.0 * (x_scaled + 0.4)**2) + 
                      0.3 * np.exp(-7.0 * (x_scaled - 0.8)**2) + 
                      0.2 * np.exp(-2.0 * (x_scaled + 0.9)**2) +
                      0.15 * np.exp(-4.5 * (x_scaled - 0.1)**2) +
                      0.1 * np.exp(-6.0 * (x_scaled + 0.6)**2))
        
        # Chaotic sinusoidal modulation with fractional frequencies
        sin_mod = np.sum(np.sin(15.0 * x_scaled) * np.cos(13.0 * x_scaled) + 
                        0.7 * np.sin(20.0 * x_scaled**1.5) * np.cos(18.0 * x_scaled**1.5) + 
                        0.5 * np.sin(25.0 * x_scaled**2.5) * np.cos(22.0 * x_scaled**2.5) +
                        0.3 * np.sin(30.0 * np.sqrt(np.abs(x_scaled))) * np.cos(28.0 * np.sqrt(np.abs(x_scaled))))
        
        # Exponential dimensionality scaling with chaotic phase shifts
        dim_scaling = np.sum(np.exp(-0.8 * np.abs(x_scaled)) * (1.0 + 0.6 * np.sin(5.0 * x_scaled) * np.cos(4.0 * x_scaled)))
        
        # Enhanced cross-dimensional interaction terms with higher-order coupling
        cross_terms = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                           np.sin(4.0 * (x_scaled[:-1] + x_scaled[1:])) + 
                           (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                           np.cos(3.0 * (x_scaled[:-2] - x_scaled[2:])) +
                           (x_scaled[:-3]**2 + x_scaled[3:]**2) * 
                           np.sin(2.5 * (x_scaled[:-3] + x_scaled[3:])))
        
        # Novel chaotic harmonic interference with dynamic phase modulation
        harmonics = np.sum(np.sin(6.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                         0.9 * np.sin(12.0 * x_scaled**2) * np.cos(14.0 * x_scaled**2) + 
                         0.7 * np.sin(18.0 * x_scaled**3) * np.cos(20.0 * x_scaled**3) +
                         0.5 * np.sin(24.0 * np.sqrt(np.abs(x_scaled))) * np.cos(26.0 * np.sqrt(np.abs(x_scaled))))
        
        # Asymmetric landscape with dynamic weighted sum and chaotic noise
        chaos_noise = 0.1 * np.random.rand() * np.sum(np.sin(30.0 * x_scaled) * np.cos(35.0 * x_scaled))
        
        return 0.4 * peaks + 0.3 * sin_mod + 0.15 * dim_scaling + 0.1 * cross_terms + 0.05 * harmonics + chaos_noise + 2.1