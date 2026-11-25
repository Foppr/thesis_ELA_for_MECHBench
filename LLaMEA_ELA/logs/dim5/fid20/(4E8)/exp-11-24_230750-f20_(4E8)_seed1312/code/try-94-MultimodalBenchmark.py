import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like self-similarity with hyperbolic tangent scaling
        fractal = 0.0
        for i in range(1, min(5, self.dim + 1)):
            scale = 2 ** (-i)
            fractal += scale * np.sum(np.tanh(scale * x) * np.cos(scale * x**2))
        
        # Quantum harmonic oscillator with complex coupling and phase modulation
        quantum_potential = 0.5 * np.sum(x**2 + 0.4 * np.sin(3 * np.pi * x) * np.cos(3 * np.pi * x) + 
                                       0.1 * np.tanh(x) * np.sin(0.5 * x))
        
        # Adaptive gradient field with directional coupling and dynamic scaling
        grad_field = 0.0
        for i in range(self.dim - 1):
            grad_field += (x[i] - x[i+1])**2 * (1.0 + 0.2 * np.tanh(x[i] * x[i+1]))
        
        # Multi-scale Gaussian ridges with dynamic amplitudes and widths
        ridge_sum = 0.0
        for i in range(min(5, self.dim)):
            amplitude = 1.0 + 0.6 * np.sin(i * 0.4)
            width = 0.3 + 0.4 * np.cos(i * 0.2)
            ridge_sum += amplitude * np.exp(-0.5 * ((x[i] - 1.5 * np.sin(i)) / width)**2)
        
        # Polynomial chaos expansion with mixed monomial terms and hyperbolic coupling
        chaos_poly = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced cross-terms for better conditioning
                chaos_poly += x[i]**2 * x[j]**3 * np.tanh(0.1 * (x[i] + x[j]))
        
        # Dynamic conditioning with enhanced dimension-adaptive parameters
        condition = 1.0 + 0.4 * np.sin(self.dim * 0.3) * np.mean(np.abs(x)) + \
                   0.3 * np.cos(self.dim * 0.15) * np.std(x) + \
                   0.1 * np.tanh(self.dim * 0.05)
        
        # Combined function with improved curvature control and noise modeling
        base_value = condition * (np.sum(x**4) + 0.6 * np.sum(x**3) + 0.2 * np.sum(x**2))
        
        # Enhanced noise component with improved variance control and temporal correlation
        noise = 0.08 * np.random.rand() * np.sum(np.sin(4 * x) * np.cos(2 * x)) * (1.0 + 0.2 * np.tanh(self.dim))
        
        # Introduce enhanced multimodality through coupled sine waves, periodic shifts, and hyperbolic modulation
        coupled_terms = 0.0
        for i in range(self.dim):
            coupled_terms += np.sin(x[i] * np.pi / 3) * np.cos(x[i] * np.pi / 6) * \
                            np.tanh(0.4 * x[i] + i * 0.15) * np.sin(0.2 * x[i] - i * 0.08)
        
        # Add novel hyperbolic tangent coupling for additional complexity
        tanh_coupling = 0.0
        for i in range(self.dim):
            tanh_coupling += np.tanh(x[i]) * np.sin(0.3 * x[i])
        
        return base_value + fractal + quantum_potential + grad_field + ridge_sum + chaos_poly + noise + coupled_terms + tanh_coupling