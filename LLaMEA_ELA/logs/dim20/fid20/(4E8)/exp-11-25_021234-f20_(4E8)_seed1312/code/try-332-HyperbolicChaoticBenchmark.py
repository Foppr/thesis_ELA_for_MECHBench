import numpy as np

class HyperbolicChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent chaotic components with dynamic modulation
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.tanh(0.5 * i + 0.3 * np.sin(0.4 * i))
            amp = 1.2 + 0.8 * np.tanh(0.6 * i + 0.2 * np.cos(0.3 * i))
            phase = 0.5 * np.tanh(0.7 * i + 0.4 * np.cos(0.2 * i))
            f1 += amp * np.tanh(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2)
            
        # Radial polynomial conditioning with chaotic exponents
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            exponent = 3.0 + 2.0 * np.tanh(0.4 * i + 0.2 * np.sin(0.3 * r))
            f2 += x[i]**exponent
            
        # Dynamic cross-dimensional couplings with hyperbolic interaction
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.8 + 0.4 * np.tanh(0.3 * (i + j) + 0.2 * np.cos(0.2 * r))
                interaction = np.tanh(x[i] + x[j]) * np.tanh(x[i] - x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                f3 += strength * interaction
                
        # Time-varying chaotic conditioning with hyperbolic scaling
        f4 = 0.0
        for i in range(self.dim):
            cond_factor = 1.5 + 0.9 * np.tanh(0.3 * r + 0.2 * np.sin(0.4 * i))
            f4 += cond_factor * x[i]**6
            
        # Fractal-like hyperbolic oscillations with recursive structure
        f5 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.tanh(0.6 * i + 0.3 * np.cos(0.4 * r))
            phase = 0.3 * np.tanh(0.5 * i + 0.2 * np.sin(0.3 * r))
            f5 += scale * np.tanh(3.0 * x[i] + phase) * np.tanh(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Boundary repulsion with hyperbolic exponential scaling
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                penalty = 3.0 * dist**2.5 * np.exp(-0.3 * dist)
                f6 += penalty
                
        # Hyperbolic self-similarity terms with dynamic scaling factors
        f7 = 0.0
        for i in range(self.dim):
            scale = 0.9 + 0.3 * np.tanh(0.8 * i + 0.2 * np.sin(0.5 * r))
            f7 += scale * np.tanh(4.0 * x[i]) * np.tanh(1.5 * x[i]) * np.exp(-0.08 * x[i]**2)
            
        # Dynamic coupling with time-varying weights and hyperbolic modulation
        f8 = 0.0
        for i in range(self.dim):
            weight = 1.6 + 0.5 * np.tanh(0.5 * i + 0.3 * np.cos(0.3 * r))
            f8 += weight * x[i]**4 * np.exp(-0.05 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8