import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Fractal-like chaotic component using generalized tent map
        r = np.sqrt(np.sum(x_norm**2))
        tent_map = np.where(r < 0.3, 3.2 * r, np.where(r < 0.6, 1.5 * (1 - r), 2.8 * (r - 0.6)))
        fractal_term = r**3 * np.exp(-r**3) * tent_map
        
        # Multi-peak sinusoidal interaction with varying amplitudes and frequencies
        peak_term = 0.0
        for i in range(min(5, self.dim)):
            freq = (i + 1) * 2.0
            amp = 1.0 / (1.0 + i * 0.5)
            peak_term += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Radial polynomial with exponential modulation and multiple local minima
        radial_poly = np.sum((x_norm**2 + 0.1) * np.exp(-0.5 * x_norm**2))
        
        # Angular coupling with multiple harmonic interactions
        angular_coupling = 0.0
        if self.dim > 1:
            for i in range(min(4, self.dim)):
                for j in range(i+1, min(4, self.dim)):
                    angular_coupling += np.sin((i+1) * (j+1) * np.arctan2(x_norm[j], x_norm[i]))
        
        # Cross-term with hyperbolic tangent modulation for steep gradients
        cross_term = np.sum(np.tanh(2.0 * x_norm) * np.sin(5.0 * x_norm)**2)
        
        # Additional chaotic logistic map component with time-delayed feedback
        logistic = 3.8 * r * (1 - r)
        delayed_feedback = np.sin(r * 10.0) if r > 0.1 else 0.0
        logistic_term = logistic * delayed_feedback * np.exp(-0.2 * r**2)
        
        # Combine all terms with dynamic weights based on dimensionality
        dim_factor = 1.0 + 0.1 * (self.dim - 1)
        result = (0.3 * fractal_term + 
                 0.25 * peak_term + 
                 0.2 * radial_poly + 
                 0.15 * angular_coupling + 
                 0.05 * cross_term + 
                 0.05 * logistic_term) * dim_factor
        
        return result