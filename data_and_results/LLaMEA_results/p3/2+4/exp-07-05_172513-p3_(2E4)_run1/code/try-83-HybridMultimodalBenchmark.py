import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base term with mixed degrees
        polynomial = np.sum(0.5 * x_scaled**2 + 0.3 * x_scaled**4 + 0.2 * x_scaled**6)
        
        # Trigonometric component with varying frequencies and amplitudes
        trigonometric = np.sum(2.0 * np.sin(3 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled) + 
                              1.5 * np.sin(7 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Radial basis function component with multiple centers
        rbfs = 0
        centers = np.linspace(-1, 1, 5)
        for center in centers:
            rbfs += np.exp(-5 * np.sum((x_scaled - center)**2))
        
        # Cross-dimensional coupling with sine and cosine interactions
        coupling = np.sum(np.sin(4 * np.pi * x_scaled[:-1]) * np.cos(3 * np.pi * x_scaled[1:]) * 
                         (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # High-frequency oscillation component
        high_freq = np.sum(0.8 * np.sin(15 * np.pi * x_scaled) + 0.6 * np.cos(12 * np.pi * x_scaled))
        
        # Asymmetric barrier terms
        barriers = np.sum(1.2 * np.exp(-2.5 * x_scaled**2) * (1 + 0.5 * np.sin(10 * np.pi * x_scaled)))
        
        # Cubic and quintic terms for additional complexity
        cubic_quintic = np.sum(0.4 * x_scaled**3 + 0.15 * x_scaled**5)
        
        # Combine all components with carefully tuned weights
        return 0.3 * polynomial + 1.5 * trigonometric + 0.8 * rbfs + 0.25 * coupling + 0.35 * high_freq + 0.4 * barriers + 0.2 * cubic_quintic