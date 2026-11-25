import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine waves with varying amplitudes and frequencies
        chaotic_terms = np.sum(np.sin(15 * np.pi * np.sin(x)) * np.cos(3 * np.pi * np.cos(x)))
        
        # Radial basis function components with dynamic centers
        rbfs = 0.0
        for i in range(min(5, self.dim)):
            center = np.sin(i * np.pi / 5) * 3.0
            rbfs += np.exp(-0.5 * ((x[i] - center) / (1.0 + 0.1 * i))**2)
        
        # Dynamic conditioning based on dimensionality and position
        dynamic_condition = 1.0 + 0.5 * np.sin(self.dim * 0.1) * np.mean(np.abs(x))
        
        # Quadratic basin with non-uniform weights
        quadratic = dynamic_condition * np.sum((x**2) * (1.0 + 0.2 * np.abs(x)))
        
        # Cross-term interactions with chaotic coupling
        cross_terms = 0.5 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(3 * x[:-1] + 2 * x[1:]))
        
        # Add novel cubic polynomial interaction term
        cubic_interaction = 0.3 * np.sum(x[:-2]**3 * x[1:-1] * x[2:])
        
        # Add noise term with varying intensity
        noise = 0.1 * np.random.rand() * np.sum(np.sin(10 * x))
        
        # Combined function value
        return quadratic + chaotic_terms + rbfs + cross_terms + cubic_interaction + noise