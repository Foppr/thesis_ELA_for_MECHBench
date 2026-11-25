import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal frequency patterns for each dimension
        self.fractal_freqs = np.random.uniform(1.0, 10.0, dim)
        # Saddle point cluster centers
        self.saddle_centers = np.random.uniform(-5.0, 5.0, (15, dim))
        # Adaptive gradient modulation coefficients
        self.grad_coeffs = np.random.uniform(0.5, 2.0, dim)
        # Self-similar amplitude scaling factors
        self.amplitude_scales = np.random.uniform(0.1, 2.0, dim)
        # Condition number ratios for each dimension
        self.condition_ratios = np.random.uniform(1.0, 100.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Self-similar sinusoidal fractal component
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, 8):
                freq = self.fractal_freqs[i] * (2 ** k)
                amplitude = self.amplitude_scales[i] / (k ** 1.5)
                fractal_sum += amplitude * np.sin(freq * x[i])
            result += fractal_sum ** 2
            
        # Saddle point clustering component
        saddle_energy = 0.0
        for center in self.saddle_centers:
            distance = np.sum((x - center) ** 2)
            # Create saddle-like behavior with multiple negative curvature regions
            saddle_energy -= np.exp(-distance / (2.0 * (self.dim + 1.0))) * np.prod(
                [np.cosh(self.condition_ratios[i] * (x[i] - center[i])) for i in range(self.dim)]
            )
            
        # Adaptive gradient modulation
        grad_modulation = 0.0
        for i in range(self.dim):
            grad_modulation += self.grad_coeffs[i] * np.sin(x[i]) * np.cos(x[i])
            
        # Combine components with dynamic weighting based on x values
        total = 0.4 * result + 0.3 * saddle_energy + 0.3 * grad_modulation
        
        return total