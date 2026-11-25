import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced nested fractal radial component with chaotic coupling
        radial = np.sum(x**2)
        fractal = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.9 * np.sin(0.9 * i) * np.cos(0.5 * i)
            freq = 15.0 + 4.0 * np.sin(0.7 * i)
            fractal += scale * np.sin(freq * np.sqrt(radial + 1e-8)) * np.cos(11.0 * x[i] + 0.6 * np.sin(0.8 * i))
        
        # Enhanced rotation-equivariant chaotic component with cross-dimension coupling
        chaotic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i]) + 0.3 * np.sin(0.5 * (i + j)) * np.cos(0.4 * (i - j))
                coupling = np.exp(-0.07 * (x[i]**2 + x[j]**2)) * np.sin(25.0 * angle) * np.cos(20.0 * angle)
                chaotic += coupling * (1.0 + 0.4 * np.sin(0.6 * i) * np.cos(0.6 * j))
        
        # Multi-scale interference with non-linear frequency modulation
        interference = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(0.4 * i) * np.cos(0.3 * i)
            for k in range(1, 7):
                freq = k * freq_mod * (2.5 + 0.6 * np.sin(0.5 * i))
                amp = 1.0 / k**1.5 * (0.9 + 0.1 * np.cos(0.7 * i))
                interference += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + k * np.pi/8)
        
        # Adaptive conditioning with dynamic dimension interaction
        condition = 2.0 + 0.4 * np.log(self.dim + 1) + 0.3 * np.sin(0.5 * self.dim) + 0.15 * np.cos(0.4 * self.dim)
        
        # Cross-dimension polynomial weighting for enhanced conditioning
        poly_weight = 0.0
        for i in range(self.dim):
            poly_weight += (i + 1)**1.5 * np.sin(0.6 * x[i])**2
        
        # Combine all components with dynamic mixing weights
        total = condition * (0.3 * radial + 0.4 * fractal + 0.2 * chaotic + 0.1 * interference) + 0.08 * poly_weight
        
        # Add complex noise pattern with periodic perturbations and enhanced chaos
        noise = 0.03 * np.sum(np.sin(70.0 * x) + np.cos(50.0 * x) + np.sin(30.0 * x**2))
        
        # Introduce a new chaotic modulation component based on the entire vector
        vector_mod = np.sum(np.sin(13.0 * x) * np.cos(9.0 * x) * np.exp(-0.1 * radial))
        total += 0.05 * vector_mod
        
        # Add a new fractal-based interaction term between dimensions
        fractal_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                fractal_interaction += np.sin(30.0 * dist) * np.cos(25.0 * dist) * (i + j)
        total += 0.02 * fractal_interaction
        
        return total + noise