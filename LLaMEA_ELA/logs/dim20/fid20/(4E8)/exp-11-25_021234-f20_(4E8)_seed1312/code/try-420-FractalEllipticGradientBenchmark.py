import numpy as np

class FractalEllipticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-based self-similarity patterns with recursive scaling
        f1 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.8 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            fractal_sum = 0.0
            for k in range(1, 10):
                fractal_sum += np.sin(k**1.7 * x[i]) / (k**1.3)
            f1 += fractal_sum * scale_factor * np.exp(-0.1 * x[i]**2)
            
        # Adaptive elliptic potentials with dynamic eccentricities
        f2 = 0.0
        for i in range(self.dim):
            eccentricity = 1.5 + 0.7 * np.cos(0.4 * i + 0.2 * np.sum(x**2))
            f2 += (x[i]**2) / (1.0 + eccentricity * np.sin(0.6 * x[i])**2)
            
        # Dynamic gradient modulation with time-varying coupling
        f3 = 0.0
        for i in range(self.dim):
            coupling = 1.2 + 0.6 * np.sin(0.7 * i + 0.3 * np.sum(x**2))
            f3 += coupling * x[i] * np.exp(-0.15 * x[i]**2)
            
        # Multi-scale harmonic interactions with recursive spectral components
        f4 = 0.0
        for i in range(self.dim):
            scale_factor = 1.3 + 0.5 * np.cos(0.6 * i)
            harmonic_sum = 0.0
            for k in range(1, 9):
                harmonic_sum += np.cos(k * x[i]) / (k**1.4)
            f4 += harmonic_sum * scale_factor * np.exp(-0.08 * x[i]**2)
            
        # Cross-dimensional elliptic couplings with adaptive weights
        f5 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 + 0.4 * np.cos(0.8 * (i + j) + 0.5 * np.sum(x**2))
                    coupling = x[i] * x[j] * weight
                    coupling_sum += coupling
            f5 += coupling_sum / (1.0 + 0.3 * np.abs(x[i]))
            
        # Boundary-sensitive elliptic oscillations with adaptive damping
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                damping_factor = 2.0 + 0.5 * np.sin(0.9 * i)
                f6 += damping_factor * np.exp(-1.5 * (5.0 - np.abs(x[i]))**2)
                
        # Resonant elliptic components with dynamic phase shifts
        f7 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.cos(0.7 * i + 0.4 * np.sum(x**2))
            freq = 1.5 + 0.8 * np.sin(0.6 * i)
            f7 += np.cos(freq * x[i] + phase_shift) * np.sin(freq * x[i] + phase_shift)
            
        # Adaptive penalty terms with elliptic conditioning
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.5:
                chaos_factor = 1.5 + 0.5 * np.cos(0.8 * i + 0.4 * np.sum(x**2))
                f8 += chaos_factor * np.exp(-0.25 * (np.abs(x[i]) - 3.5)**2)
                
        # Multi-modal elliptic sinusoidal components with dynamic scaling
        f9 = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.6 * np.sin(0.7 * i + 0.5 * np.sum(x**2))
            f9 += scale * np.cos(3.0 * x[i])**2
            
        # Exponential radial conditioning with elliptic modulation
        r = np.sqrt(np.sum(x**2))
        f10 = 0.0
        for i in range(self.dim):
            modulator = 1.5 + 0.4 * np.cos(0.5 * i + 0.4 * r)
            f10 += modulator * np.exp(-0.15 * x[i]**2) * np.cos(2.5 * x[i])**2
            
        # Additional nested chaotic components
        f11 = 0.0
        for i in range(self.dim):
            nested_term = np.cos(5.0 * x[i] + 0.4 * np.sum(x**2)) * np.sin(2.0 * x[i])
            f11 += nested_term * (1.0 + 0.4 * np.cos(0.5 * x[i]))
            
        # Enhanced multi-scale elliptic interactions
        f12 = 0.0
        for i in range(self.dim):
            scale_factor = 1.7 + 0.3 * np.sin(0.7 * i)
            harmonic_sum = 0.0
            for k in range(1, 6):
                harmonic_sum += np.sin(k * x[i]) / (k**1.1)
            f12 += harmonic_sum * np.exp(-0.2 * x[i]**2) * scale_factor
            
        # Fractal dimension scaling with self-similar modulation
        f13 = 0.0
        for i in range(self.dim):
            fractal_dim = 1.8 + 0.4 * np.sin(0.9 * i + 0.3 * np.sum(x**2))
            f13 += np.exp(-fractal_dim * np.abs(x[i])) * np.sin(4.0 * x[i])**2
            
        # Cross-correlation elliptic potentials with adaptive coupling
        f14 = 0.0
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    corr_factor = 1.0 + 0.5 * np.sin(0.6 * (i - j) + 0.3 * np.sum(x**2))
                    cross_sum += x[i] * x[j] * corr_factor
            f14 += cross_sum / (1.0 + 0.2 * np.abs(x[i]))
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14