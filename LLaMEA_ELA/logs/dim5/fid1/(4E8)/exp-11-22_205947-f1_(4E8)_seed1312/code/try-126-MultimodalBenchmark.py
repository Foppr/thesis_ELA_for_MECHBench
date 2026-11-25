import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested fractal radial component with chaotic coupling
        radial = np.sum(x**2)
        fractal = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.7 * np.sin(0.8 * i) * np.cos(0.4 * i)
            freq = 12.0 + 3.0 * np.sin(0.6 * i)
            fractal += scale * np.sin(freq * np.sqrt(radial + 1e-8)) * np.cos(9.0 * x[i] + 0.5 * np.sin(0.7 * i))
        
        # Enhanced rotation-equivariant chaotic component with cross-dimension coupling
        chaotic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i]) + 0.2 * np.sin(0.4 * (i + j)) * np.cos(0.3 * (i - j))
                coupling = np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.sin(20.0 * angle) * np.cos(16.0 * angle)
                chaotic += coupling * (1.0 + 0.3 * np.sin(0.5 * i) * np.cos(0.5 * j))
        
        # Multi-scale interference with non-linear frequency modulation
        interference = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.4 * np.sin(0.3 * i) * np.cos(0.2 * i)
            for k in range(1, 5):
                freq = k * freq_mod * (2.0 + 0.5 * np.sin(0.4 * i))
                amp = 1.0 / k * (0.8 + 0.2 * np.cos(0.6 * i))
                interference += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + k * np.pi/6)
        
        # Adaptive conditioning with dynamic dimension interaction
        condition = 1.5 + 0.3 * np.log(self.dim + 1) + 0.2 * np.sin(0.4 * self.dim) + 0.1 * np.cos(0.3 * self.dim)
        
        # Cross-dimension polynomial weighting for enhanced conditioning
        poly_weight = 0.0
        for i in range(self.dim):
            poly_weight += (i + 1) * np.sin(0.5 * x[i])**2
        
        # Combine all components with dynamic mixing weights
        total = condition * (0.25 * radial + 0.35 * fractal + 0.25 * chaotic + 0.15 * interference) + 0.05 * poly_weight
        
        # Add complex noise pattern with periodic perturbations - increased sensitivity
        noise = 0.03 * np.sum(np.sin(65.0 * x) + np.cos(45.0 * x) + np.sin(30.0 * x**2))
        
        return total + noise