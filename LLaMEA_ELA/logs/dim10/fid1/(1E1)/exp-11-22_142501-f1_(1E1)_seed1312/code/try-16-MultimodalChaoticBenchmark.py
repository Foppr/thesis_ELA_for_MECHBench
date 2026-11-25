import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled) + 
                         0.5 * np.sin(7 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Polynomial barrier terms creating multiple local minima
        poly_barrier = np.sum((x_scaled**2 - 1)**4 + 0.3 * (x_scaled**2 - 1)**2)
        
        # Radial basis function component with multiple centers
        rbf_term = np.sum(np.exp(-5 * np.sum((x_scaled.reshape(1, -1) - np.linspace(-1, 1, self.dim).reshape(-1, 1))**2, axis=0)))
        
        # Saddle point structure using mixed quadratic and cubic terms
        saddle_term = np.sum(x_scaled**4 - 2 * x_scaled**2 + 0.5 * x_scaled**3)
        
        # High-frequency oscillation with varying amplitudes
        high_freq = np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled) + 
                          0.7 * np.sin(25 * np.pi * x_scaled))
        
        # Ridge structure with gradual elevation
        ridge_term = np.sum(0.1 * x_scaled**6 + 0.2 * x_scaled**4 + 0.3 * x_scaled**2)
        
        # Combine all components with appropriate weights
        return 0.25 * sin_term + 0.3 * poly_barrier + 0.15 * rbf_term + 0.1 * saddle_term + 0.1 * high_freq + 0.05 * ridge_term + 2.0