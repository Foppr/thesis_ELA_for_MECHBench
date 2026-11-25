import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similarity pattern with recursive scaling
        fractal = 0.0
        for i in range(1, min(6, self.dim + 1)):
            scale = 2 ** (-i)
            fractal += scale * np.sum(np.sin(scale * x) * np.cos(scale * x**2))
        
        # Quantum harmonic oscillator potential with complex coupling
        quantum_potential = 0.5 * np.sum(x**2 + 0.3 * np.sin(2 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Adaptive gradient field with direction-dependent scaling
        grad_field = 0.0
        for i in range(self.dim - 1):
            grad_field += (x[i] - x[i+1])**2 * (1.0 + 0.1 * np.sin(x[i] * x[i+1]))
        
        # Multi-scale Gaussian ridges with varying amplitudes and widths
        ridge_sum = 0.0
        for i in range(min(4, self.dim)):
            amplitude = 1.0 + 0.5 * np.sin(i * 0.5)
            width = 0.5 + 0.3 * np.cos(i * 0.3)
            ridge_sum += amplitude * np.exp(-0.5 * ((x[i] - 2 * np.sin(i)) / width)**2)
        
        # Polynomial chaos expansion with mixed monomial terms
        chaos_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_poly += x[i]**3 * x[j]**2 * np.sin(0.1 * (x[i] + x[j]))
        
        # Dynamic conditioning based on problem dimension and input magnitude
        condition = 1.0 + 0.3 * np.sin(self.dim * 0.2) * np.mean(np.abs(x)) + \
                   0.2 * np.cos(self.dim * 0.1) * np.std(x)
        
        # Combined function with additional coupling and noise
        base_value = condition * (np.sum(x**4) + 0.5 * np.sum(x**3) + 0.1 * np.sum(x**2))
        
        # Add adaptive noise component with improved variance control
        noise = 0.05 * np.random.rand() * np.sum(np.sin(5 * x) * np.cos(3 * x)) * (1.0 + 0.1 * np.sin(self.dim))
        
        # Introduce enhanced multimodality through coupled sine waves and periodic shifts
        coupled_terms = 0.0
        for i in range(self.dim):
            coupled_terms += np.sin(x[i] * np.pi / 2) * np.cos(x[i] * np.pi / 4) * \
                            np.sin(0.5 * x[i] + i * 0.1) * np.cos(0.3 * x[i] - i * 0.05)
        
        return base_value + fractal + quantum_potential + grad_field + ridge_sum + chaos_poly + noise + coupled_terms