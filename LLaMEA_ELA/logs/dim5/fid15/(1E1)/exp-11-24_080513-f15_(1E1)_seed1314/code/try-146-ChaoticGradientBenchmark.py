import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic component with nested logistic maps and fractal scaling
        chaotic = 0.0
        r = 3.95
        for i in range(self.dim):
            x_prev = 0.5
            for _ in range(20):  # More iterations for stronger chaos
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * x_prev * 10) * np.exp(-np.abs(x_normalized[i]))
        
        # Dynamic gradient with time-varying conditioning and coupling
        gradient = 0.0
        for i in range(self.dim):
            condition = 2.0 + 2.5 * np.sin(i * 0.9 + np.sum(x_normalized[:i]) * 0.3)
            gradient += condition * (x_normalized[i] ** 4) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Stronger saddle point region with multi-dimensional coupling
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                saddle += np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * (x_normalized[i] - x_normalized[j])**3
        
        # Fractal-like discontinuity with nested step functions
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * np.sin(8 * x_normalized[i]) * np.cos(5 * x_normalized[i]) * np.exp(-np.abs(x_normalized[i]) * 2)
        
        # Multi-scale harmonic interaction with fractal weights and coupling
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 5.0) * (1 + 0.5 * np.sin(dist * 10))
                harmonic += weight * np.sin(4 * (x_normalized[i] + x_normalized[j])) * np.cos(4 * (x_normalized[i] - x_normalized[j]))
        
        # Enhanced nonlinearity with fractal-like scaling
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += (x_normalized[i]**5) * np.sin(x_normalized[i])**3
        
        # Additional global optima embedding through periodic modulation
        optima = 0.0
        for i in range(self.dim):
            optima += np.sin(2 * np.pi * x_normalized[i]) * np.cos(2 * np.pi * x_normalized[i])
        
        # Combined fitness with dynamic scaling factors and noise injection
        return (0.25 * chaotic + 0.3 * gradient + 0.18 * saddle + 
                0.18 * discontinuous + 0.08 * harmonic + 0.04 * nonlin + 0.07 * optima)