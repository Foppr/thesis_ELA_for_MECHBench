import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like self-similarity with chaotic scaling
        fractal = 0.0
        for i in range(1, min(6, self.dim + 1)):
            scale = 2 ** (-i * 1.2)
            fractal += scale * np.sum(np.sin(scale * x) * np.cos(scale * x**1.5))
        
        # Quantum harmonic oscillator with modified coupling and phase shifts
        quantum_potential = 0.5 * np.sum(x**2 + 0.3 * np.sin(3 * np.pi * x) * np.cos(3 * np.pi * x))
        
        # Adaptive gradient field with directional dependency and dynamic scaling
        grad_field = 0.0
        for i in range(self.dim - 1):
            dx = x[i] - x[i+1]
            grad_field += dx**2 * (1.0 + 0.2 * np.sin(x[i] * x[i+1] * 0.5))
        
        # Multi-scale Gaussian ridges with dynamic amplitudes and widths
        ridge_sum = 0.0
        for i in range(min(4, self.dim)):
            amplitude = 1.5 + 0.2 * np.sin(i * 0.8)
            width = 0.6 + 0.3 * np.cos(i * 0.5)
            ridge_sum += amplitude * np.exp(-0.5 * ((x[i] - 2.0 * np.sin(i * 0.7)) / width)**2)
        
        # Polynomial chaos expansion with higher-order monomial terms and coupling
        chaos_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                chaos_poly += x[i]**4 * x[j]**3 * np.sin(0.2 * (x[i] + x[j]))
        
        # Hyperbolic tangent coupling with dynamic conditioning
        tanh_coupling = 0.0
        for i in range(self.dim):
            tanh_coupling += np.tanh(x[i]) * np.sin(0.3 * x[i]**2)
        
        # Dynamic conditioning based on problem dimension and input magnitude
        condition = 1.0 + 0.5 * np.sin(self.dim * 0.3) * np.mean(np.abs(x)) + \
                   0.3 * np.cos(self.dim * 0.2) * np.std(x)
        
        # Combined function with additional coupling and noise
        base_value = condition * (np.sum(x**4) + 0.5 * np.sum(x**3) + 0.15 * np.sum(x**2))
        
        # Add adaptive noise component
        noise = 0.05 * np.random.rand() * np.sum(np.sin(6 * x) * np.cos(4 * x))
        
        return base_value + fractal + quantum_potential + grad_field + ridge_sum + chaos_poly + tanh_coupling + noise