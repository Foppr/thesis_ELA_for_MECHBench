import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion components with varying Hurst parameters
        f1 = 0.0
        for i in range(self.dim):
            hurst = 0.3 + 0.4 * np.sin(0.2 * i)
            fbm_term = np.sin(x[i] * (1.0 + 0.5 * np.cos(0.3 * i))) * np.exp(-0.1 * x[i]**2)
            f1 += fbm_term * (1.0 + hurst * np.sin(0.4 * x[i]))
            
        # Elliptic conditioning with adaptive eccentricity
        f2 = 0.0
        for i in range(self.dim):
            eccentricity = 1.5 + 0.8 * np.cos(0.3 * i)
            f2 += (x[i]**2) / (1.0 + eccentricity * np.sin(0.2 * x[i])**2)
            
        # Gradient-based saddle-point interactions
        f3 = 0.0
        for i in range(self.dim):
            grad_term = np.cos(x[i]) * np.exp(-0.05 * x[i]**2)
            f3 += grad_term * (1.0 + 0.3 * np.sin(0.5 * x[i]))
            
        # Multi-scale fractal-like interactions with recursive structure
        f4 = 0.0
        for i in range(self.dim):
            scale_factor = 1.2 + 0.3 * np.cos(0.6 * i)
            f4 += scale_factor * np.sin(np.pi * x[i] / (1.5 + 0.2 * np.sum(x**2)))**3
            
        # Cross-dimensional elliptic couplings with adaptive weights
        f5 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 + 0.2 * np.cos(0.4 * (i + j))
                    coupling = x[i] * x[j] * weight
                    coupling_sum += coupling
            f5 += coupling_sum * np.exp(-0.1 * x[i]**2)
            
        # Boundary-sensitive harmonic oscillations
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.3 + 0.4 * np.cos(0.5 * i)
                f6 += boundary_factor * np.exp(-1.5 * (5.0 - np.abs(x[i]))**2)
                
        # Resonant saddle-point components with time-varying frequencies
        f7 = 0.0
        for i in range(self.dim):
            freq = 1.2 + 1.0 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            f7 += np.sin(freq * x[i]) * np.cos(freq * x[i]) * (1.0 + 0.2 * np.sin(0.4 * x[i]))
            
        # Adaptive penalty terms with elliptic conditioning
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.5:
                penalty_strength = 1.2 + 0.6 * np.cos(0.4 * i)
                f8 += penalty_strength * np.exp(-0.15 * (np.abs(x[i]) - 3.5)**2)
                
        # Multi-modal sinusoidal components with dynamic phase shifts
        f9 = 0.0
        for i in range(self.dim):
            phase_shift = 0.4 * np.cos(0.5 * i + 0.3 * np.sum(x**2))
            freq_mod = 1.0 + 0.7 * np.sin(0.2 * i)
            f9 += np.sin(freq_mod * x[i] + phase_shift)**2
            
        # Exponential radial conditioning with fractal modulation
        r = np.sqrt(np.sum(x**2))
        f10 = 0.0
        for i in range(self.dim):
            modulator = 1.1 + 0.3 * np.cos(0.2 * i + 0.1 * r)
            f10 += modulator * np.exp(-0.08 * x[i]**2) * np.sin(1.5 * x[i])**2
            
        # Small mutation: Adjusted coupling weights and phase shifts
        f5 += 0.1 * np.sum(np.array([x[i] * x[(i+1)%self.dim] for i in range(self.dim)])) * np.exp(-0.05 * np.sum(x**2))
        f9 += 0.2 * np.sin(1.3 * x[0] + 0.5 * np.sum(x**2))**2
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10