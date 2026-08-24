import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similar component with recursive scaling
        fractal = 0
        for i in range(self.dim):
            # Use sine and cosine with varying frequencies to create fractal structure
            freq1 = 2 + 3 * np.sin(x[i] * 0.5)
            freq2 = 1 + 2 * np.cos(x[i] * 0.3)
            fractal += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Dynamic saddle-point distribution with hyperbolic components
        saddle = 0
        for i in range(self.dim):
            # Hyperbolic tangent and secant create saddle points
            saddle += np.tanh(x[i]) * np.sech(x[i]) * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
        
        # Adaptive conditioning through logarithmic scaling
        cond = 0
        for i in range(self.dim):
            # Logarithmic scaling with dynamic base
            base = 1.5 + 0.5 * np.sin(x[i] * 0.8)
            cond += np.log(np.abs(x[i]) + 1) * np.exp(-0.1 * x[i]**2) * np.sin(0.6 * x[i])
        
        # Multi-scale oscillatory component
        oscillatory = 0
        for i in range(self.dim):
            # Combine multiple frequencies for complex oscillation
            freqs = [1, 2, 3, 4, 5]
            osc = 0
            for f in freqs:
                osc += np.sin(f * x[i]) * np.cos(f * x[i] * 0.7)
            oscillatory += osc * np.exp(-0.03 * x[i]**2)
        
        # Cross-term interactions with dynamic coupling
        cross = 0
        for i in range(self.dim-1):
            j = (i + 1) % self.dim
            coupling = 1.2 + 0.8 * np.sin(0.5 * (x[i] + x[j]))
            cross += coupling * np.sin(0.3 * (x[i]**2 + x[j]**2)) * np.cos(0.2 * (x[i] - x[j]))
        
        # Combine all components with adaptive weights
        return 0.25 * fractal + 0.20 * saddle + 0.25 * cond + 0.20 * oscillatory + 0.10 * cross