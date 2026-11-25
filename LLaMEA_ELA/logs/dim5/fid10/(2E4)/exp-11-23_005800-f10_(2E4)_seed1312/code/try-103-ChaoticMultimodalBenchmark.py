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
        self.amplitude_scale = 2.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic base with nested logistic maps and higher-order terms
        chaotic = 0.0
        for i in range(self.dim):
            # Nested logistic map dynamics with cubic and quartic terms
            xi = x[i]
            for _ in range(4):
                xi = self.lambda1 * xi * (1 - xi) + 0.1 * xi**3 - 0.05 * xi**4
            chaotic += xi**2
            
        # Multi-scale harmonic interference with fractal components and phase modulation
        harmonic = 0.0
        for i in range(self.dim):
            # Fractal-like harmonic structure with varying frequencies and phase shifts
            freqs = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0]
            amplitudes = [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125]
            phase_shifts = [0.0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4]
            for f, a, p in zip(freqs, amplitudes, phase_shifts):
                harmonic += a * np.sin(f * x[i] + p) * np.cos(f * x[i] / 2.0 + p) * (1.0 + self.fractal_dim * np.sin(x[i] + p))
                
        # Dynamic cross-dimensional coupling with adaptive modulation and interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased range for complexity
                diff = x[i] - x[j]
                # Adaptive coupling based on solution proximity with exponential scaling
                coupling_factor = 1.0 / (1.0 + np.exp(-0.7 * abs(diff)))
                # Add interaction terms between dimensions
                interaction = np.sin(2.0 * diff) * np.cos(3.0 * diff) * np.exp(-0.1 * abs(diff))
                coupling += coupling_factor * interaction
                
        # Fractal noise and dimensionality complexity with polynomial scaling
        fractal = 0.0
        for i in range(self.dim):
            # Add fractal noise with dimensionality scaling and polynomial terms
            noise = np.random.normal(0, self.noise_level)
            fractal += (x[i]**4 + x[i]**3 + x[i]**2) * np.exp(-abs(x[i])) * noise
            
        # Global modulation with chaotic behavior near optima and multi-modal peaks
        modulation = 0.0
        norm_x = np.linalg.norm(x)
        if norm_x < 1.0:
            # Chaotic behavior near global optimum with multiple peaks
            for i in range(self.dim):
                modulation += np.sin(self.lambda2 * x[i]) * np.cos(self.lambda3 * x[i]) + 0.5 * np.sin(2 * self.lambda2 * x[i])
        elif norm_x > 4.0:
            # Exponential decay away from optimum with oscillatory behavior
            modulation = 2.0 * np.exp(-(norm_x - 4.0)**2) * np.sin(5.0 * (norm_x - 4.0))
            
        # Combine all components with chaotic weights and amplitude scaling
        result = self.amplitude_scale * chaotic + 1.5 * harmonic + 1.0 * coupling + 0.7 * fractal + 0.5 * modulation
        
        # Add chaotic offset and scale appropriately
        return result + 15.0 * self.dim + np.random.normal(0, 0.02)
