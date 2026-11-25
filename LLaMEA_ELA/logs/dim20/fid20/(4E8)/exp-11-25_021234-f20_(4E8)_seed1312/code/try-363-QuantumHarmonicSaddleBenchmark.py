import numpy as np

class QuantumHarmonicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillations with phase modulation
        f1 = 0.0
        for i in range(self.dim):
            phase = np.sin(0.5 * i + 0.3 * np.sum(x**2))
            freq = 1.5 + 0.8 * np.cos(0.4 * i)
            amp = 1.2 + 0.6 * np.sin(0.3 * i)
            f1 += amp * np.sin(freq * x[i] + phase)**2
            
        # Adaptive elliptic conditioning with dynamic eccentricity
        f2 = 0.0
        for i in range(self.dim):
            eccentricity = 1.3 + 0.4 * np.cos(0.2 * i + 0.1 * np.sum(x**2))
            f2 += (x[i]**2) / (eccentricity**2) + (eccentricity**2) * (x[i]**2)
            
        # Gradient-based saddle-point interactions with complex coupling
        f3 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = 0.8 + 0.4 * np.sin(0.3 * (i + j))
                    saddle_sum += coupling_strength * x[i] * x[j]
            f3 += saddle_sum * np.exp(-0.1 * x[i]**2)
            
        # Multi-scale quantum harmonic components with superposition
        f4 = 0.0
        for i in range(self.dim):
            scale_factor = 1.1 + 0.3 * np.cos(0.6 * i + 0.2 * np.sum(x**2))
            f4 += scale_factor * np.sin(np.pi * x[i] / (1.5 + 0.3 * np.sum(x**2)))**4
            
        # Adaptive penalty with quantum tunneling effect
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                tunnel_prob = 0.7 + 0.3 * np.cos(0.5 * i + 0.2 * np.sum(x**2))
                f5 += tunnel_prob * np.exp(-0.15 * (np.abs(x[i]) - 4.2)**2)
                
        # Cross-dimensional quantum interference patterns
        f6 = 0.0
        for i in range(self.dim):
            interference_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_diff = np.sin(0.4 * (i - j) + 0.3 * np.sum(x**2))
                    interference_sum += np.cos(x[i] * x[j] * phase_diff)
            f6 += interference_sum * np.exp(-0.05 * x[i]**2)
            
        # Fractal-like quantum harmonic series with recursive structure
        f7 = 0.0
        for i in range(self.dim):
            fractal_factor = 1.4 + 0.3 * np.cos(0.7 * i + 0.2 * np.sum(x**2))
            f7 += fractal_factor * np.sin(np.pi * x[i] / (1.3 + 0.2 * np.sum(x**2)))**3
            
        # Adaptive polynomial interactions with quantum-like coefficients
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 1.0 + 0.5 * np.sin(0.4 * (i - j) + 0.2 * np.sum(x**2))
                interaction = x[i]**3 * x[j]**2
                f8 += coeff * interaction * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Boundary-sensitive quantum oscillations with complex amplitude
        f9 = 0.0
        for i in range(self.dim):
            boundary_amp = 1.3 + 0.5 * np.cos(0.6 * i + 0.3 * np.sum(x**2))
            if np.abs(x[i]) > 4.5:
                f9 += boundary_amp * np.exp(-1.5 * (5.0 - np.abs(x[i]))**2)
                
        # Resonant quantum harmonic components with time-varying frequencies
        f10 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.0 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            amp = 1.5 + 0.5 * np.cos(0.4 * i + 0.3 * np.sum(x**2))
            f10 += amp * np.sin(freq * x[i])**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10