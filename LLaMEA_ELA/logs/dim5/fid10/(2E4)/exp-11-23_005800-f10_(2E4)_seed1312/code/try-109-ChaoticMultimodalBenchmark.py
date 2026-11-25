import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for chaotic dynamics and nested structures
        self.lambda1 = 3.95
        self.lambda2 = 3.75
        self.lambda3 = 3.85
        self.fractal_dim = 1.6
        self.noise_level = 0.12
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic base with nested logistic maps
        chaotic = 0.0
        for i in range(self.dim):
            # Nested logistic map dynamics
            xi = x[i]
            for _ in range(4):
                xi = self.lambda1 * xi * (1 - xi)
            chaotic += xi**2
            
        # Multi-scale harmonic interference with fractal components
        harmonic = 0.0
        for i in range(self.dim):
            # Fractal-like harmonic structure with varying frequencies
            freqs = [1.0, 2.5, 4.5, 8.5, 16.5]
            amplitudes = [1.0, 0.6, 0.3, 0.15, 0.075]
            for f, a in zip(freqs, amplitudes):
                harmonic += a * np.sin(f * x[i]) * np.cos(f * x[i] / 2.0) * (1.0 + self.fractal_dim * np.sin(x[i]))
                
        # Dynamic cross-dimensional coupling with adaptive modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Slightly increased range
                diff = x[i] - x[j]
                # Adaptive coupling based on solution proximity
                coupling_factor = 1.0 / (1.0 + np.exp(-0.4 * abs(diff)))
                coupling += coupling_factor * np.sin(2.5 * diff) * np.cos(3.5 * diff)
                
        # Fractal noise and dimensionality complexity
        fractal = 0.0
        for i in range(self.dim):
            # Add fractal noise with dimensionality scaling
            noise = np.random.normal(0, self.noise_level)
            fractal += (x[i]**3 + x[i]**2) * np.exp(-abs(x[i])) * noise
            
        # Global modulation with chaotic behavior near optima
        modulation = 0.0
        norm_x = np.linalg.norm(x)
        if norm_x < 1.0:
            # Chaotic behavior near global optimum
            for i in range(self.dim):
                modulation += np.sin(self.lambda2 * x[i]) * np.cos(self.lambda3 * x[i])
        elif norm_x > 4.0:
            # Exponential decay away from optimum
            modulation = 2.5 * np.exp(-(norm_x - 4.0)**2
            
        # Combine all components with modified weights and added cubic terms
        result = 1.2 * chaotic + 1.1 * harmonic + 0.8 * coupling + 0.6 * fractal + 0.4 * modulation
        
        # Add cubic polynomial terms to increase conditioning difficulty
        cubic_terms = np.sum(x**3)
        
        # Add modified chaotic offset and scale appropriately
        return result + 12.0 * self.dim + cubic_terms * 0.015 + np.random.normal(0, 0.012)