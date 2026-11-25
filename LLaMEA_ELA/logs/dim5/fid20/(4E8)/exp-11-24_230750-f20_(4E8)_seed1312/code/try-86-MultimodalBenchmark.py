import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similarity pattern with modified recursive scaling
        fractal = 0.0
        for i in range(1, min(5, self.dim + 1)):
            scale = 3 ** (-i)
            fractal += scale * np.sum(np.sin(scale * x) * np.cos(scale * x**2))
        
        # Quantum harmonic oscillator potential with altered coupling
        quantum_potential = 0.5 * np.sum(x**2 + 0.4 * np.sin(2 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Adaptive gradient field with modified direction-dependent scaling
        grad_field = 0.0
        for i in range(self.dim - 1):
            grad_field += (x[i] - x[i+1])**2 * (1.0 + 0.15 * np.sin(x[i] * x[i+1]))
        
        # Multi-scale Gaussian ridges with adjusted amplitudes and widths
        ridge_sum = 0.0
        for i in range(min(3, self.dim)):
            amplitude = 1.2 + 0.3 * np.sin(i * 0.6)
            width = 0.7 + 0.2 * np.cos(i * 0.4)
            ridge_sum += amplitude * np.exp(-0.5 * ((x[i] - 2.5 * np.sin(i)) / width)**2)
        
        # Polynomial chaos expansion with modified monomial terms
        chaos_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_poly += x[i]**3 * x[j]**2 * np.sin(0.15 * (x[i] + x[j]))
        
        # Dynamic conditioning based on problem dimension and input magnitude
        condition = 1.0 + 0.4 * np.sin(self.dim * 0.25) * np.mean(np.abs(x)) + \
                   0.25 * np.cos(self.dim * 0.15) * np.std(x)
        
        # Combined function with additional coupling and noise
        base_value = condition * (np.sum(x**4) + 0.6 * np.sum(x**3) + 0.12 * np.sum(x**2))
        
        # Add adaptive noise component
        noise = 0.06 * np.random.rand() * np.sum(np.sin(5 * x) * np.cos(3 * x))
        
        return base_value + fractal + quantum_potential + grad_field + ridge_sum + chaos_poly + noise