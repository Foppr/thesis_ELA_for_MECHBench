import numpy as np

class MultimodalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with varying curvature
        quadratic = np.sum(x_scaled**2)
        
        # Saddle point component with alternating signs
        saddle = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Multimodal component using Gaussian peaks with varying heights
        multimodal = 0.0
        for i in range(self.dim):
            for j in range(1, 4):
                multimodal += j * np.exp(-0.5 * (x_scaled[i] - j * 0.3)**2) * np.sin(j * np.pi * x_scaled[i])
        
        # Implicit constraint term creating a "banana" shaped valley
        constraint = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2 - 1)**2)
        
        # High-frequency oscillation with diminishing amplitude
        oscillation = np.sum(np.sin(20 * x_scaled) * np.cos(15 * x_scaled) * np.exp(-0.1 * np.abs(x_scaled)))
        
        # Cross-term interaction creating complex dependency
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(5 * np.pi * (x_scaled[:-1] + x_scaled[1:])))
        
        # Combine all components with different weights
        return 0.4 * quadratic + 0.3 * saddle + 0.2 * multimodal + 0.05 * constraint + 0.03 * oscillation + 0.02 * cross_term + 2.0