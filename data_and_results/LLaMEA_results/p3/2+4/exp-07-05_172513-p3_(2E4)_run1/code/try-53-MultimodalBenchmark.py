import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial basin term with mixed degrees
        polynomial = np.sum(x_scaled**6 + 0.5 * x_scaled**4 + 0.3 * x_scaled**2)
        
        # Multi-peak trigonometric component with varying frequencies
        trigonometric = np.sum(np.sin(15 * x_scaled) * np.cos(12 * x_scaled) * np.sin(8 * x_scaled))
        
        # Exponential barrier with varying decay rates and sinusoidal modulation
        barriers = np.sum(np.exp(-2 * x_scaled**2) * (1 + 0.5 * np.sin(10 * x_scaled)))
        
        # Saddle point structure with mixed polynomial and exponential terms
        saddle = np.sum(x_scaled**3 * np.exp(-0.5 * x_scaled**2) - 0.2 * x_scaled**4)
        
        # Cross-dimensional coupling with non-linear interaction
        coupling = np.sum(np.sin(3 * x_scaled[:-1] + x_scaled[1:]) * np.cos(2 * x_scaled[:-1] - x_scaled[1:]) * 0.8)
        
        # Add a global sinusoidal modulation to increase complexity
        global_modulation = 0.5 * np.sin(5 * np.sum(x_scaled**2))
        
        # Combine all components with different weights
        return 0.3 * polynomial + 1.5 * trigonometric + barriers + 0.4 * saddle + 0.2 * coupling + global_modulation