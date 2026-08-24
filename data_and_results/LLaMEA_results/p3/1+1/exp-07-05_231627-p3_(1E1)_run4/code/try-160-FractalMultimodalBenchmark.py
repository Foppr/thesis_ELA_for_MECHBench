import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal component with self-similar structure at multiple scales
        fractal = 0.0
        scales = [1, 2, 3, 5]
        for scale in scales:
            # Logarithmic chaotic component with varying frequency
            log_term = np.sum(np.log(1 + scale * np.abs(x_norm)) * np.sin(scale * np.pi * x_norm))
            # Self-similar peak arrangement with adaptive positioning
            peak_term = np.sum(np.exp(-scale * (x_norm - np.sin(scale * x_norm))**2))
            fractal += log_term * peak_term
            
        # Adaptive peak positioning with dynamic center adjustment
        adaptive_peaks = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / self.dim) * 0.5
            adaptive_peaks += np.exp(-5 * (x_norm[i] - center)**2) * (1 + 0.5 * np.sin(10 * x_norm[i]))
            
        # Multi-scale harmonic interference with frequency modulation
        harmonic = 0.0
        for freq in [1, 3, 7, 11]:
            harmonic += np.sum(np.sin(freq * x_norm**2) * np.cos(freq * x_norm) * 
                              np.exp(-0.5 * np.abs(x_norm)))
                              
        # Rugged terrain with controlled roughness using fractional calculus concept
        rugged = np.sum(np.abs(x_norm)**1.7 + 0.3 * np.sin(20 * x_norm) * np.cos(15 * x_norm))
        
        # Cross-dimensional coupling with exponential interaction
        coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling += np.exp(-np.abs(x_norm[i] - x_norm[i+1]) * (1 + 0.1 * np.abs(x_norm[i])))
                
        # Combine all components with dynamic weighting based on input magnitude
        magnitude = np.abs(np.sum(x_norm))
        weights = [0.25, 0.3, 0.2, 0.15, 0.1]
        result = weights[0] * fractal + weights[1] * adaptive_peaks + weights[2] * harmonic + \
                 weights[3] * rugged + weights[4] * coupling
        
        # Add dynamic noise proportional to function value
        noise = 0.02 * (1 + magnitude) * np.random.uniform(-0.5, 0.5)
        
        return result + noise