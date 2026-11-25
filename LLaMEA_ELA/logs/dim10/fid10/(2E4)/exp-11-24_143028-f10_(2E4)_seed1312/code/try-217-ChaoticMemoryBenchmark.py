import numpy as np

class ChaoticMemoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic map parameters
        self.chaotic_params = np.random.rand(dim) * 4.0 + 0.5  # r values for logistic map
        self.memory_strength = np.random.rand(dim) * 0.5 + 0.1  # Memory decay factors
        self.noise_levels = np.random.rand(dim) * 0.3 + 0.1  # Noise intensities
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic iterated map component with memory
        chaotic_term = 0.0
        for i in range(self.dim):
            # Logistic map with memory effect
            r = self.chaotic_params[i]
            memory = self.memory_strength[i]
            
            # Initialize chaotic sequence with current x value
            xi = x[i]
            chaotic_sum = 0.0
            for t in range(10):  # Iterate for 10 steps
                xi = r * xi * (1 - xi)
                if t > 0:
                    chaotic_sum += xi * np.exp(-memory * t)
            
            chaotic_term += chaotic_sum
            
        # Polynomial chaos expansion component
        poly_chaos = 0.0
        for i in range(self.dim):
            # Use Hermite polynomials (simplified version)
            poly_chaos += (x[i]**2 - 1)**2 + 0.5 * x[i]**4
            
        # Adaptive noise injection
        noise_term = 0.0
        for i in range(self.dim):
            noise = np.random.normal(0, self.noise_levels[i])
            noise_term += noise * np.sin(x[i] * (i + 1))
            
        # Fractal-like structure using multi-resolution wavelet components
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(1, min(6, self.dim+1)):
                freq = 2**(j-1)
                fractal_term += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) / (j**1.5)
                
        # Coupling between dimensions with time-delay effects
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                delay = abs(x[i] - x[j])
                coupling_term += np.sin(delay) * (x[i]**2 + x[j]**2)
                
        # Combine all components
        result = 0.8 * chaotic_term + 0.6 * poly_chaos + 0.4 * noise_term + \
                 0.7 * fractal_term + 0.5 * coupling_term
                
        return result