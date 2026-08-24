import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degree terms, chaotic scaling, and fractal-like exponents
        poly = 0
        for i in range(self.dim):
            exp = 21 + 4 * np.sin(0.5 * i)
            poly += np.power(np.abs(x[i]), exp) * (1 + 0.1 * np.sin(3 * x[i]))
        
        # Enhanced trigonometric component with increased frequency modulation, chaotic coupling, and memory effects
        trig = 0
        for i in range(self.dim):
            freq = 15 + 10 * np.sin(x[i] * 0.8)
            trig += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.15 * x[i]**2) * np.sin(0.9 * x[i]) * (1 + 0.05 * np.cos(2 * x[i]))
        
        # Enhanced radial basis function component with chaotic centers, dynamic weights, and self-similarity
        rbf = 0
        centers = np.linspace(-4.8, 4.8, min(15, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            weight = 3.0 + 2.0 * np.sin(0.6 * i)
            rbf += weight * np.exp(-0.5 * (x[i] - center)**2) * np.sin(10 * (x[i] - center)) * (1 + 0.1 * np.sin(0.5 * (x[i] - center)))
        
        # Enhanced cross-term interactions with chaotic coupling, multi-scale effects, and memory dependencies
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 5.0 + 1.5 * np.sin(0.9 * (x[i] + x[j]))
            cross += coupling * (x[i]**14 + x[j]**14) * np.sin(0.8 * (x[i] - x[j])**14) * (1 + 0.08 * np.cos(0.3 * (x[i] + x[j])))
        
        # Enhanced chaotic modulation component with fractal-like nonlinearity and conditioning
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi * (1 + 0.9 * np.sin(10 * x[i]))) * np.cos(x[i] * np.pi * (1 + 0.9 * np.cos(10 * x[i]))) * np.exp(-0.35 * x[i]**2) * (1 + 0.1 * np.sin(5 * x[i]))
        
        # Memory-dependent fitness interactions
        memory = 0
        for i in range(self.dim):
            if i > 0:
                memory += 0.5 * np.sin(x[i] - x[i-1]) * np.cos(x[i] + x[i-1]) * np.exp(-0.2 * (x[i] - x[i-1])**2)
        
        # Scale and combine all components with dynamic weights
        return 0.35 * poly + 0.25 * trig + 0.2 * rbf + 0.15 * cross + 0.05 * chaotic + 0.05 * memory