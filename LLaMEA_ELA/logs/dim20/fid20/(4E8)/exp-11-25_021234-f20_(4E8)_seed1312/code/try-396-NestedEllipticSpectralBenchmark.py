import numpy as np

class NestedEllipticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested elliptic potentials with varying eccentricities
        f1 = 0.0
        for i in range(self.dim):
            eccentricity = 1.0 + 0.5 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            f1 += (x[i]**2) / (1.0 + eccentricity * np.cos(0.4 * x[i])**2)
            
        # Adaptive spectral filtering with dynamic frequency components
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            f2 += np.sin(freq * x[i])**4 + np.cos(freq * x[i])**4
            
        # Dynamic gradient modulation with time-varying coupling strengths
        f3 = 0.0
        for i in range(self.dim):
            coupling_strength = 1.0 + 0.8 * np.cos(0.6 * i + 0.4 * np.sum(x**2))
            f3 += coupling_strength * x[i] * np.exp(-0.1 * x[i]**2)
            
        # Multi-scale harmonic interactions with fractal-like frequency nesting
        f4 = 0.0
        for i in range(self.dim):
            scale_factor = 1.5 + 0.5 * np.sin(0.7 * i)
            f4 += np.sin(scale_factor * x[i]) * np.cos(scale_factor * x[i] / 2.0) * (1.0 + 0.3 * np.sin(0.5 * x[i]))
            
        # Cross-dimensional elliptic couplings with adaptive weights
        f5 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 + 0.4 * np.cos(0.4 * (i - j) + 0.3 * np.sum(x**2))
                    coupling = x[i] * x[j] * weight
                    coupling_sum += coupling
            f5 += coupling_sum * np.exp(-0.05 * x[i]**2)
            
        # Boundary-sensitive elliptic oscillations with adaptive damping
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                damping_factor = 1.3 + 0.7 * np.sin(0.5 * i)
                f6 += damping_factor * np.exp(-1.5 * (5.0 - np.abs(x[i]))**2)
                
        # Resonant spectral components with dynamic amplitude modulation
        f7 = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.6 * np.cos(0.4 * i + 0.3 * np.sum(x**2))
            f7 += amp_mod * np.sin(1.5 * x[i]) * np.cos(1.5 * x[i])
            
        # Adaptive penalty terms with elliptic conditioning
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.0:
                penalty_factor = 1.2 + 0.8 * np.sin(0.6 * i + 0.4 * np.sum(x**2))
                f8 += penalty_factor * np.exp(-0.15 * (np.abs(x[i]) - 3.0)**2)
                
        # Nested harmonic components with dynamic phase shifts
        f9 = 0.0
        for i in range(self.dim):
            phase_shift = 0.4 * np.sin(0.7 * i + 0.5 * np.sum(x**2))
            f9 += np.sin(1.8 * x[i] + phase_shift)**3
            
        # Exponential radial conditioning with spectral modulation
        r = np.sqrt(np.sum(x**2))
        f10 = 0.0
        for i in range(self.dim):
            modulator = 1.0 + 0.5 * np.sin(0.4 * i + 0.3 * r)
            f10 += modulator * np.exp(-0.08 * x[i]**2) * np.cos(1.2 * x[i])**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10