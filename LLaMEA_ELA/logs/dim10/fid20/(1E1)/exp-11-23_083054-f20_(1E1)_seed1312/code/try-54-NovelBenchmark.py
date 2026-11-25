import numpy as np

class NovelBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base with mixed degrees
        poly_term = np.sum(0.5 * x_scaled**2 + 0.3 * x_scaled**4 + 0.1 * x_scaled**6)
        
        # Trigonometric components with varying frequencies and phases
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) +
                          0.7 * np.sin(5 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Exponential interaction terms to create sharp gradients
        exp_term = np.sum(np.exp(-0.5 * x_scaled**2) * np.sin(4 * np.pi * x_scaled)**2)
        
        # Cross-terms creating non-separability and complex interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_scaled[i] * x_scaled[j]) / (1 + np.abs(x_scaled[i] - x_scaled[j]))
        
        # Add a global minimum perturbation
        penalty = 0.5 * np.sum((x_scaled + 0.2)**2)
        
        return 0.8 * poly_term + 0.3 * trig_term + 0.2 * exp_term + 0.1 * cross_term + penalty