import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with varying rates
        exp_decay = np.sum(np.exp(-0.5 * (x / (1.0 + 0.1 * np.abs(x)))**2))
        
        # Trigonometric wave interactions with dynamic frequencies
        trig_waves = np.sum(np.sin(2 * np.pi * x) * np.cos(4 * np.pi * x) * 
                           np.exp(-0.1 * np.abs(x)))
        
        # Hyperbolic tangent coupling terms for complex landscape interactions
        tanh_coupling = 0.5 * np.sum(np.tanh(x[:-1] + x[1:]) * 
                                   np.tanh(2 * x[:-1] - x[1:]))
        
        # Radial basis functions with adaptive widths and shifted centers
        rbf_sum = 0.0
        for i in range(min(3, self.dim)):
            center = np.sin(i * np.pi / 3) * 4.0
            width = 1.0 + 0.5 * np.cos(i * np.pi / 3)
            rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Polynomial cross-terms with alternating signs for increased complexity
        poly_cross = 0.3 * np.sum(x[:-1]**2 * x[1:]**3 - x[:-1]**3 * x[1:]**2)
        
        # Dynamic conditioning based on dimensionality and position
        condition_factor = 1.0 + 0.3 * np.sin(self.dim * 0.2) * np.mean(np.abs(x))
        
        # Quadratic basin with non-uniform weights and dynamic scaling
        quadratic = condition_factor * np.sum((x**2) * (1.0 + 0.1 * x**2))
        
        # Add noise term with varying intensity
        noise = 0.05 * np.random.rand() * np.sum(np.sin(5 * x))
        
        # Combined function value
        return quadratic + exp_decay + trig_waves + tanh_coupling + rbf_sum + poly_cross + noise