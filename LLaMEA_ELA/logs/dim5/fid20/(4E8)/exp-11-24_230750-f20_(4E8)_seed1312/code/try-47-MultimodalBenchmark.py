import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine waves with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(20 * np.pi * np.sin(1.5 * x)) * np.cos(4 * np.pi * np.cos(0.7 * x)))
        
        # Radial basis function components with dynamic centers and adaptive widths
        rbfs = 0.0
        for i in range(min(5, self.dim)):
            center = np.sin(i * np.pi / 4) * 2.5
            width = 0.8 + 0.3 * np.cos(i * 0.5)
            rbfs += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Dynamic conditioning based on dimensionality and position with non-linear scaling
        dynamic_condition = 1.0 + 0.7 * np.sin(self.dim * 0.15) * np.mean(np.abs(x))**1.5
        
        # Quadratic basin with non-uniform weights and additional harmonic terms
        quadratic = dynamic_condition * np.sum((x**2) * (1.0 + 0.3 * np.abs(x) + 0.1 * x**4))
        
        # Cross-term interactions with enhanced chaotic coupling and higher-order correlations
        cross_terms = 0.6 * np.sum(np.sin(1.5 * x[:-1] * x[1:]) * np.cos(2.5 * x[:-1] + 1.8 * x[1:]))
        
        # Novel cubic polynomial interaction term with asymmetric weighting
        cubic_interaction = 0.4 * np.sum(x[:-2]**3 * x[1:-1] * x[2:] * (1.0 + 0.2 * np.abs(x[:-2])))
        
        # Additional quartic polynomial coupling for increased complexity
        quartic_interaction = 0.2 * np.sum(x[:-3]**4 * x[1:-2] * x[2:-1] * x[3:])
        
        # Add noise term with varying intensity and directional bias
        noise = 0.15 * np.random.rand() * np.sum(np.sin(12 * x) * np.cos(8 * x))
        
        # Combined function value
        return quadratic + chaotic_terms + rbfs + cross_terms + cubic_interaction + quartic_interaction + noise