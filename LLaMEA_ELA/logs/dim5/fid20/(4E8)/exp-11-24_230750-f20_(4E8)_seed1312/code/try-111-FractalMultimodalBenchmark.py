import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal component with recursive self-similarity
        fractal = 0.0
        for i in range(self.dim):
            # Recursive scaling with phase shift
            scaled_x = x[i] * (1.0 + 0.1 * np.sin(i * 0.7))
            fractal += np.sin(scaled_x) * np.cos(2.0 * scaled_x) * np.exp(-0.1 * abs(scaled_x))
        
        # Dynamic phase shift component
        phase_shift = 0.0
        for i in range(self.dim):
            phase_shift += np.sin(i * 0.5 + np.sum(x[:i])) * np.cos(i * 0.3 + np.sum(x[:i]))
        
        # Spectral frequency modulation with multiple harmonics
        spectral = 0.0
        frequencies = [1.0, 2.0, 3.0, 4.0]
        for i, freq in enumerate(frequencies):
            if i < self.dim:
                spectral += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * (1.0 + 0.2 * np.sin(i * 0.8))
        
        # Ridge and valley structure with varying conditioning
        ridge_valley = 0.0
        for i in range(self.dim - 1):
            ridge_valley += (x[i]**2 + x[i+1]**2) * np.cos(0.5 * (x[i] + x[i+1]))
        
        # Directional bias with cross-dimensional coupling
        bias = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                bias += x[i] * x[i+1] * np.sin(0.3 * (x[i] - x[i+1]))
        
        # Adaptive conditioning based on variable magnitude and dimension
        condition = 1.0 + 0.5 * np.mean(np.abs(x)) + 0.3 * np.std(x)**2
        
        # Final function value with dynamic scaling
        return condition * (fractal + phase_shift + spectral + ridge_valley + bias)