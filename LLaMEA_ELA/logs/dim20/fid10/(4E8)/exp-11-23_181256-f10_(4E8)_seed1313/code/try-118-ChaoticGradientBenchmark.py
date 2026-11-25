import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gradient-based quadratic terms with variable conditioning
        quadratic = np.sum(x_scaled**2 * (1.0 + 0.3 * np.sin(2.0 * self.dim * x_scaled)))
        
        # Saddle point landscape with alternating curvature
        saddle = np.sum(np.sin(3.0 * x_scaled) * np.cos(2.5 * x_scaled) * 
                       (1.0 + 0.2 * np.tanh(x_scaled**2)))
        
        # Chaotic modulation using logistic map-like behavior
        chaotic = np.sum(np.sin(15.0 * np.sin(x_scaled)) * 
                        np.cos(12.0 * np.cos(x_scaled)) * 
                        np.exp(-0.5 * x_scaled**2))
        
        # Multi-scale harmonic interference with phase modulation
        harmonic = np.sum((np.sin(8.0 * x_scaled) + 0.5 * np.cos(6.0 * x_scaled)) * 
                         (1.0 + 0.1 * np.sin(4.0 * x_scaled**2)))
        
        # Variable exponential decay with oscillatory perturbations
        exp_decay = np.sum(np.exp(-x_scaled**2 * (1.0 + 0.2 * np.cos(3.0 * x_scaled))) * 
                          (1.0 + 0.15 * np.sin(7.0 * x_scaled)))
        
        # High-frequency oscillatory component with amplitude modulation
        high_freq = np.sum(np.sin(25.0 * x_scaled) * np.cos(20.0 * x_scaled**2) * 
                          (1.0 + 0.3 * np.sin(5.0 * x_scaled)))
        
        # Combined function with diverse curvature and complex topology
        return 2.5 * quadratic + 1.8 * saddle + 1.2 * chaotic + 0.9 * harmonic + 0.6 * exp_decay + 0.4 * high_freq