import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial basis function component with non-uniform center placements and higher variance
        rb = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / 2.5) * 0.85
            variance = 0.5 + 0.3 * np.cos(i * np.pi / 4.0)
            rb += np.exp(-8 * variance * (x_norm[i] - center)**2) * np.cos(15 * (x_norm[i] - center))
        
        # Stronger chaotic cosine modulation with frequency modulation and amplitude scaling
        chaos = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 3) * np.pi
            amp = 0.7 + 0.3 * np.sin(i * np.pi / 3.0)
            chaos += amp * np.cos(freq * x_norm[i] + np.sin(freq * x_norm[i] + 0.7 * np.sin(i)))
        
        # Asymmetric polynomial interactions with higher-order terms and stronger coupling
        poly = 0.0
        for i in range(self.dim):
            poly += (x_norm[i]**4 + 0.5 * x_norm[i]**6 + 0.2 * x_norm[i]**8 + 0.05 * x_norm[i]**10) * np.cos(x_norm[(i+1) % self.dim] * 1.5)
        
        # Cross-dimensional coupling with complex interaction terms and variable coupling strength
        cross = 0.0
        for i in range(self.dim - 1):
            coupling_strength = 0.8 + 0.4 * np.sin(i * np.pi / 3.0)
            cross += coupling_strength * np.sin(x_norm[i] * x_norm[i+1]) * (x_norm[i]**2 + x_norm[i+1]**2 + 0.2)
        
        # Enhanced chaotic interference with multiple exponential components and phase shifts
        interference = 0.0
        for i in range(self.dim):
            interference += np.exp(-0.3 * x_norm[i]**2) * np.sin(30 * x_norm[i] + np.cos(15 * x_norm[i]) + 0.5 * np.sin(7 * x_norm[i]))
        
        # Additional high-frequency oscillation component
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(50 * x_norm[i]) * np.cos(20 * x_norm[i]) * (0.5 + 0.5 * np.sin(i))
        
        # Final combined function with adjusted weights for increased complexity
        return 0.8 * rb + 0.6 * chaos + 0.4 * poly + 0.3 * cross + 0.2 * interference + 0.1 * oscillation + 0.08 * np.sum(x_norm**2)