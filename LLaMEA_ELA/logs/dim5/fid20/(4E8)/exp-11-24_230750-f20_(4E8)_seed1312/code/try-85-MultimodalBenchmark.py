import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine waves with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(25 * np.pi * np.sin(1.9 * x)) * np.cos(5.0 * np.pi * np.cos(0.9 * x)))
        
        # Radial basis function components with dynamic centers and adaptive widths
        rbfs = 0.0
        for i in range(min(6, self.dim)):
            center = np.sin(i * np.pi / 4.0) * 2.5
            width = 1.0 + 0.3 * np.cos(i * 0.7)
            rbfs += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Dynamic conditioning based on dimensionality and position with non-linear scaling
        dynamic_condition = 1.0 + 0.9 * np.sin(self.dim * 0.2) * np.mean(np.abs(x))**1.8
        
        # Quadratic basin with non-uniform weights and additional harmonic terms
        quadratic = dynamic_condition * np.sum((x**2) * (1.0 + 0.4 * np.abs(x) + 0.15 * x**4))
        
        # Cross-term interactions with enhanced chaotic coupling and higher-order correlations
        cross_terms = 0.8 * np.sum(np.sin(1.8 * x[:-1] * x[1:]) * np.cos(3.0 * x[:-1] + 2.0 * x[1:]))
        
        # Novel cubic polynomial interaction term with asymmetric weighting
        cubic_interaction = 0.5 * np.sum(x[:-2]**3 * x[1:-1] * x[2:] * (1.0 + 0.25 * np.abs(x[:-2])))
        
        # Additional quartic polynomial coupling for increased complexity
        quartic_interaction = 0.25 * np.sum(x[:-3]**4 * x[1:-2] * x[2:-1] * x[3:])
        
        # Improved noise term with directional bias and structured correlation
        noise = 0.2 * np.random.rand() * np.sum(np.sin(15 * x) * np.cos(9.0 * x)) + \
                0.1 * np.mean(np.sin(8 * x)) * np.std(x)
        
        # Add a novel hyperbolic tangent coupling term for enhanced landscape irregularity
        tanh_coupling = 0.35 * np.sum(np.tanh(3.5 * x) * np.sin(1.6 * x**2))
        
        # Add a novel sigmoidal modulation term for increased non-linearity
        sigmoid_modulation = 0.28 * np.sum(1 / (1 + np.exp(-2.0 * x)) * np.cos(1.3 * x))
        
        # Add a fractional Brownian motion-inspired term for long-range dependencies
        fbm_term = 0.18 * np.sum(np.sin(2.1 * x) * np.cos(1.7 * x) * np.sin(0.5 * x**3))
        
        # Combined function value
        return quadratic + chaotic_terms + rbfs + cross_terms + cubic_interaction + quartic_interaction + noise + tanh_coupling + sigmoid_modulation + fbm_term