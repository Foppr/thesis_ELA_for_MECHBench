import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms and chaotic scaling
        poly = np.sum(x**27) + 0.99 * np.sum(x**26) + 0.88 * np.sum(x**25) + 0.72 * np.sum(x**24) + 0.55 * np.sum(x**23)
        
        # Enhanced trigonometric component with increased frequency modulation and chaotic coupling
        trig = 0
        for i in range(self.dim):
            freq = 25 + 20 * np.sin(x[i] * 1.3)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 1.3) * np.exp(-0.2 * x[i]**2) * np.sin(1.2 * x[i])
        
        # Enhanced radial basis function component with chaotic centers and dynamic weights
        rbf = 0
        centers = np.linspace(-4.8, 4.8, min(25, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 4.5 + 3.5 * np.sin(1.0 * i)
            rbf += weight * np.exp(-0.9 * (x[i] - center)**2) * np.sin(15 * (x[i] - center))
        
        # Enhanced cross-term interactions with chaotic coupling and multi-scale effects
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 8.0 + 2.5 * np.sin(1.2 * (x[i] + x[j]))
            cross += coupling * (x[i]**18 + x[j]**18) * np.sin(1.2 * (x[i] - x[j])**18)
        
        # Enhanced chaotic modulation component to increase non-linearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 1.5 * np.sin(18 * x[i]))) * np.cos(x[i] * np.pi * (1 + 1.5 * np.cos(18 * x[i]))) * np.exp(-0.5 * x[i]**2)
        
        # Fractal-like self-similarity component with memory-dependent interactions
        fractal = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                fractal += np.sin(180 * dist) * np.exp(-0.7 * dist**2) * (1 + 0.2 * np.sin(8 * x[i]) * np.cos(8 * x[j]))
        
        # Memory-dependent interaction term
        memory = 0
        for i in range(self.dim):
            memory += np.sin(0.7 * x[i]) * np.cos(0.7 * x[i]) * np.exp(-0.3 * x[i]**2) * (1 + 0.1 * np.sum(x[:i]))
        
        # Scale and combine all components with dynamic weights
        return 0.37 * poly + 0.32 * trig + 0.27 * rbf + 0.17 * cross + 0.09 * chaotic + 0.06 * fractal + 0.03 * memory