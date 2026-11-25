import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine waves with varying frequencies and amplitudes
        chaotic_terms = np.sum(np.sin(25 * np.pi * np.tanh(1.8 * x)) * np.cos(5 * np.pi * np.sin(0.9 * x)))
        
        # Radial basis function components with dynamic centers and adaptive widths
        rbfs = 0.0
        for i in range(min(6, self.dim)):
            center = np.tanh(i * np.pi / 3) * 3.0
            width = 0.9 + 0.4 * np.sin(i * 0.6)
            rbfs += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Dynamic conditioning based on dimensionality and position with non-linear scaling
        dynamic_condition = 1.0 + 0.8 * np.tanh(self.dim * 0.2) * np.mean(np.abs(x))**1.7
        
        # Quadratic basin with non-uniform weights and additional harmonic terms
        quadratic = dynamic_condition * np.sum((x**2) * (1.0 + 0.4 * np.abs(x) + 0.15 * x**4))
        
        # Cross-term interactions with enhanced chaotic coupling and higher-order correlations
        cross_terms = 0.7 * np.sum(np.tanh(1.8 * x[:-1] * x[1:]) * np.sin(3.0 * x[:-1] + 2.0 * x[1:]))
        
        # Novel cubic polynomial interaction term with asymmetric weighting
        cubic_interaction = 0.5 * np.sum(x[:-2]**3 * x[1:-1] * x[2:] * (1.0 + 0.25 * np.abs(x[:-2])))
        
        # Additional quartic polynomial coupling for increased complexity
        quartic_interaction = 0.3 * np.sum(x[:-3]**4 * x[1:-2] * x[2:-1] * x[3:])
        
        # Fractional Brownian motion component for irregularity and memory effects
        fbm = 0.0
        hurst = 0.2 + 0.5 * np.cos(self.dim * 0.15)
        for i in range(1, min(7, self.dim)):
            fbm += (x[i] - x[i-1])**2 * np.tanh(i * hurst * np.pi / 3)
        
        # Add noise term with varying intensity and directional bias
        noise = 0.2 * np.random.rand() * np.sum(np.tanh(15 * x) * np.cos(10 * x))
        
        # Combined function value
        return quadratic + chaotic_terms + rbfs + cross_terms + cubic_interaction + quartic_interaction + fbm + noise