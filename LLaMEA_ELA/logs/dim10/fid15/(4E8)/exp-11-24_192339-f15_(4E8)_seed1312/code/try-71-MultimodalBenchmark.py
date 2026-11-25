import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with fractal-like scaling
        r = np.sqrt(np.sum(x**2))
        radial = r * (1 + 0.1 * np.sin(10 * r))
        
        # Trigonometric couplings with adaptive frequencies based on dimension
        trig_coupling = 0
        for i in range(self.dim):
            freq_i = 1 + 0.5 * np.sin(0.2 * i)
            trig_coupling += np.cos(freq_i * x[i]) * np.sin(freq_i * x[i] / 2)
        
        # Cross-dimensional interactions with self-similarity
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross_interaction += np.sin(5 * dist) * np.exp(-0.1 * dist**2)
        
        # Adaptive conditioning based on position and dimension
        condition_factor = 1.0 + 0.3 * np.tanh(np.sum(x)**2 / self.dim)
        
        # Fractal-like polynomial terms with varying exponents
        fractal_poly = 0
        for i in range(self.dim):
            exp_factor = 2 + 0.5 * np.sin(i * 0.7)
            fractal_poly += (x[i]**exp_factor) * np.cos(3 * x[i])
        
        # Global shift component to increase complexity
        global_shift = 0.1 * np.sum(np.sin(x))
        
        # Combine all components with dynamic weights
        return condition_factor * (radial + 0.5 * trig_coupling + 0.3 * cross_interaction + 0.2 * fractal_poly) + global_shift