import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**25) + 0.98 * np.sum(x**24) + 0.85 * np.sum(x**23) + 0.70 * np.sum(x**22) + 0.50 * np.sum(x**21)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 20 + 15 * np.sin(x[i] * 1.2)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 1.2) * np.exp(-0.15 * x[i]**2) * np.sin(1.0 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.9, 4.9, min(20, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 4.0 + 3.0 * np.sin(0.9 * i)
            rbf += weight * np.exp(-0.8 * (x[i] - center)**2) * np.sin(12 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 7.0 + 2.0 * np.sin(1.0 * (x[i] + x[j]))
            cross += coupling * (x[i]**16 + x[j]**16) * np.sin(1.0 * (x[i] - x[j])**16)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 1.2 * np.sin(15 * x[i]))) * np.cos(x[i] * np.pi * (1 + 1.2 * np.cos(15 * x[i]))) * np.exp(-0.4 * x[i]**2)
        
        # Fractal-like self-similarity component with memory-dependent interactions
        fractal = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                fractal += np.sin(150 * dist) * np.exp(-0.6 * dist**2) * (1 + 0.15 * np.sin(7 * x[i]) * np.cos(7 * x[j]))
        
        # Memory-dependent interaction term
        memory = 0
        for i in range(self.dim):
            memory += np.sin(0.6 * x[i]) * np.cos(0.6 * x[i]) * np.exp(-0.25 * x[i]**2) * (1 + 0.08 * np.sum(x[:i]))
        
        # Novel hybrid term with dimensionality-dependent scaling and enhanced non-linearity
        hybrid = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < self.dim and j < self.dim:
                    diff = x[i] - x[j]
                    hybrid += (np.sin(20 * diff) * np.cos(10 * diff) * np.exp(-0.3 * diff**2) * 
                              (1 + 0.2 * np.sin(3 * x[i]) * np.cos(3 * x[j])) * 
                              (1 + 0.1 * (i + j) / self.dim))
        
        # Scale and combine all components with dynamic weights
        return 0.35 * poly + 0.30 * trig + 0.25 * rbf + 0.15 * cross + 0.08 * chaotic + 0.05 * fractal + 0.02 * memory + 0.05 * hybrid