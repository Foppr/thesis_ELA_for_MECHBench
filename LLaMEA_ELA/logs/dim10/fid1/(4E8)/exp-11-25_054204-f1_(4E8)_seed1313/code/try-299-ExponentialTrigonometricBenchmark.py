import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute angular frequencies for trigonometric components
        self.frequencies = np.arange(1, dim + 1) * 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial quadratic term
        radial_term = np.sum(x**2)
        
        # Exponential decay with trigonometric modulation
        exp_decay = np.sum(np.exp(-0.1 * x**2) * np.cos(self.frequencies * x))
        
        # Radial symmetry with sine coupling
        radial_coupling = np.sin(np.sqrt(radial_term)) * np.sum(np.sin(x))
        
        # Cross-dimensional trigonometric interaction
        cross_trig = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_trig += np.cos(x[i] * x[j]) / (1.0 + abs(x[i] - x[j]))
        
        # Adaptive scaling based on dimension
        scale = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Additional multimodal component with Gaussian peaks
        gaussian_peaks = 0.0
        for i in range(self.dim):
            gaussian_peaks += np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i] + 2.0)**2))
        
        # Combined function with adjusted weights
        return scale * (0.5 * radial_term + 0.3 * exp_decay + 0.2 * radial_coupling + 
                       0.1 * cross_trig + 0.1 * gaussian_peaks)