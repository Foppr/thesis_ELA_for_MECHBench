import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Composite sinusoidal wave component with multiple frequencies and amplitudes
        sin_wave = np.sum(np.sin(2 * np.pi * x_scaled) + 
                         0.5 * np.sin(4 * np.pi * x_scaled) + 
                         0.3 * np.sin(8 * np.pi * x_scaled))
        
        # Radial basis function component with adaptive widths
        rbf_term = np.sum(np.exp(-np.sum((x_scaled[:, np.newaxis] - np.linspace(-1, 1, self.dim))**2, axis=0) / (2 * 0.3**2)))
        
        # Adaptive conditioning through variable exponentiation and modulation
        cond_term = np.sum(np.abs(x_scaled)**(1.5 + 0.5 * np.sin(3 * np.pi * x_scaled)))
        
        # Cross-term interaction with polynomial coupling
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.cos(2 * np.pi * x_scaled[:-1]))
        
        # Fractal-like self-similarity component with recursive scaling
        fractal_term = np.sum(np.sin(10 * x_scaled) * np.cos(5 * x_scaled) * 
                             np.exp(-0.1 * np.sum(x_scaled**2)))
        
        # Asymmetric penalty term to encourage exploration
        penalty = np.sum(np.where(x_scaled > 0, 0.1 * x_scaled**3, 0.2 * x_scaled**4))
        
        # Combine all components with appropriate weights
        return 0.4 * sin_wave + 0.3 * rbf_term + 0.15 * cond_term + 0.05 * cross_term + 0.05 * fractal_term + 0.05 * penalty + 2.0