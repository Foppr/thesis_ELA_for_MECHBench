import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for chaotic dynamics and nested structures
        self.lambda1 = 4.0
        self.lambda2 = 3.95
        self.lambda3 = 3.85
        self.fractal_dim = 1.7
        self.noise_level = 0.15
        self.amplitude_mod = 2.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic base with nested logistic maps and enhanced nonlinearity
        chaotic = 0.0
        for i in range(self.dim):
            # Higher order chaotic dynamics with multiple nested maps
            xi = x[i]
            for _ in range(5):
                xi = self.lambda1 * xi * (1 - xi)
            chaotic += xi**3
            
        # Multi-scale harmonic interference with fractal components and amplitude modulation
        harmonic = 0.0
        for i in range(self.dim):
            # Fractal-like harmonic structure with varying frequencies and modulated amplitudes
            freqs = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0]
            amplitudes = [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125]
            for f, a in zip(freqs, amplitudes):
                harmonic += a * self.amplitude_mod * np.sin(f * x[i]) * np.cos(f * x[i] / 2.0) * (1.0 + self.fractal_dim * np.sin(x[i]))
                
        # Dynamic cross-dimensional coupling with enhanced interaction range and complexity
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended range for increased complexity
                diff = x[i] - x[j]
                # Enhanced adaptive coupling based on solution proximity with exponential modulation
                coupling_factor = 1.0 / (1.0 + np.exp(-0.7 * abs(diff)))
                coupling += coupling_factor * np.sin(3.0 * diff) * np.cos(4.0 * diff) * np.exp(-abs(diff))
                
        # Fractal noise and dimensionality complexity with higher-order polynomial terms
        fractal = 0.0
        for i in range(self.dim):
            # Add fractal noise with dimensionality scaling and higher-order terms
            noise = np.random.normal(0, self.noise_level)
            fractal += (x[i]**4 + x[i]**3 + x[i]**2) * np.exp(-abs(x[i])) * noise
            
        # Global modulation with chaotic behavior near optima and enhanced complexity
        modulation = 0.0
        norm_x = np.linalg.norm(x)
        if norm_x < 1.0:
            # Enhanced chaotic behavior near global optimum with multiple chaotic maps
            for i in range(self.dim):
                modulation += np.sin(self.lambda2 * x[i]) * np.cos(self.lambda3 * x[i]) + np.sin(self.lambda1 * x[i]**2)
        elif norm_x > 4.0:
            # Exponential decay away from optimum with higher-order terms
            modulation = 3.0 * np.exp(-(norm_x - 4.0)**3) + 0.5 * np.exp(-(norm_x - 4.0)**2)
            
        # Combine all components with enhanced weights and nonlinearity
        result = 2.0 * chaotic + 1.5 * harmonic + 1.0 * coupling + 0.7 * fractal + 0.5 * modulation
        
        # Add enhanced chaotic offset and scale appropriately
        return result + 15.0 * self.dim + np.random.normal(0, 0.02)