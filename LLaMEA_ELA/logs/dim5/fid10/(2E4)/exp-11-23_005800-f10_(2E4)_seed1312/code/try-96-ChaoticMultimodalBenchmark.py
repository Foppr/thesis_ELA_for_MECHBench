import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for chaotic dynamics and nested structures
        self.lambda1 = 3.9
        self.lambda2 = 3.8
        self.lambda3 = 3.7
        self.fractal_dim = 1.5
        self.noise_level = 0.1
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic base with nested logistic maps
        chaotic = 0.0
        for i in range(self.dim):
            # Nested logistic map dynamics
            xi = x[i]
            for _ in range(3):
                xi = self.lambda1 * xi * (1 - xi)
            chaotic += xi**2
            
        # Multi-scale harmonic interference with fractal components
        harmonic = 0.0
        for i in range(self.dim):
            # Fractal-like harmonic structure with varying frequencies and modified amplitudes
            freqs = [1.0, 2.0, 4.0, 8.0, 16.0]
            amplitudes = [1.2, 0.6, 0.3, 0.15, 0.075]  # Slightly increased lower frequencies
            for f, a in zip(freqs, amplitudes):
                harmonic += a * np.sin(f * x[i]) * np.cos(f * x[i] / 2.0) * (1.0 + self.fractal_dim * np.sin(x[i]))
                
        # Dynamic cross-dimensional coupling with adaptive modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for complexity
                diff = x[i] - x[j]
                # Adaptive coupling based on solution proximity
                coupling_factor = 1.0 / (1.0 + np.exp(-0.5 * abs(diff)))
                coupling += coupling_factor * np.sin(2.0 * diff) * np.cos(3.0 * diff)
                
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
            modulation = 2.0 * np.exp(-(norm_x - 4.0)**2
            
        # Add cubic polynomial terms for increased conditioning
        cubic_term = 0.0
        for i in range(self.dim):
            cubic_term += 0.15 * x[i]**3  # Slightly increased coefficient
            
        # Combine all components with slightly modified weights
        result = 1.4 * chaotic + 1.2 * harmonic + 0.8 * coupling + 0.5 * fractal + 0.3 * modulation + 0.25 * cubic_term
        
        # Add chaotic offset and scale appropriately
        return result + 10.0 * self.dim + np.random.normal(0, 0.01)