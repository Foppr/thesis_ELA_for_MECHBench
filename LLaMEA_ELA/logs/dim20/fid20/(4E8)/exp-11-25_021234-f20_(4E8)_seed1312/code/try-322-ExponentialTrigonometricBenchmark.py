import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with varying rates and adaptive amplitudes
        f1 = 0.0
        for i in range(self.dim):
            rate = 0.4 + 0.2 * np.sin(0.5 * i)
            amp = 1.2 + 0.3 * np.cos(0.4 * i)
            f1 += amp * np.exp(-rate * np.abs(x[i])) * np.sin(2.0 * x[i])**2
            
        # Trigonometric wave interactions with frequency modulation and phase coupling
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.5 + 1.2 * np.sin(0.6 * i + 0.3 * np.sum(x))
            phase = 0.4 * np.cos(0.5 * i + 0.2 * np.sum(x))
            f2 += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
            
        # Radial conditioning with adaptive scaling and exponential penalties
        r = np.sqrt(np.sum(x**2))
        f3 = 0.0
        for i in range(self.dim):
            scale = 1.8 + 0.6 * np.sin(0.4 * i + 0.3 * r)
            penalty = scale * np.exp(-0.15 * x[i]**2) * (1.0 + 0.4 * np.sin(0.7 * x[i]))
            f3 += penalty
            
        # Cross-dimensional coupling with exponential interaction weights and sine modulation
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.08 * (i + j)) * (1.0 + 0.6 * np.cos(0.3 * (i - j)))
                interaction = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                f4 += weight * interaction * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Multi-scale oscillatory terms with varying periods and amplitudes
        f5 = 0.0
        for i in range(self.dim):
            period = 1.8 + 1.2 * np.sin(0.4 * i)
            amp = 0.9 + 0.3 * np.cos(0.3 * i)
            f5 += amp * np.sin(period * x[i]) * np.exp(-0.03 * x[i]**2)
            
        # Boundary repulsion with exponential decay and varying strength
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                strength = 1.8 + 0.7 * np.sin(0.6 * i + 0.4 * r)
                f6 += strength * np.exp(-1.8 * (5.0 - np.abs(x[i]))**2)
                
        # Adaptive harmonic components with time-varying frequencies and amplitudes
        f7 = 0.0
        for i in range(self.dim):
            freq = 1.8 + 1.4 * np.sin(0.3 * i + 0.4 * r)
            amp = 1.0 + 0.7 * np.cos(0.4 * i + 0.3 * r)
            f7 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Polynomial cross-terms with exponential weighting and variable coefficients
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.6 + 0.2 * np.sin(0.3 * (i + j))
                weight = np.exp(-0.04 * (x[i]**2 + x[j]**2)) * (1.0 + 0.5 * np.cos(0.4 * (i - j)))
                f8 += coeff * x[i]**2 * x[j]**3 * weight
                
        # Fractal-like radial interactions with recursive sine modulation
        f9 = 0.0
        for i in range(self.dim):
            mod = 1.2 + 0.4 * np.sin(0.7 * i + 0.5 * r)
            f9 += mod * np.sin(np.pi * x[i] / (1.0 + 0.3 * r))**3
            
        # Multi-modal penalty terms with varying scales and exponential decay
        f10 = 0.0
        for i in range(self.dim):
            scale = 0.6 + 0.2 * np.sin(0.5 * i)
            f10 += scale * np.exp(-0.08 * (x[i] - 2.0)**2) + scale * np.exp(-0.08 * (x[i] + 2.0)**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10