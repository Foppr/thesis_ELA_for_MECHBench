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
            f1 += (x[i]**2) / (1.0 + eccentricity * np.cos(0.5 * x[i])**2)
            
        # Adaptive spectral filtering with dynamic frequency components
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.8 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            f2 += np.sin(freq * x[i])**2 * np.cos(freq * x[i])**2
            
        # Dynamic gradient modulation with time-varying coupling
        f3 = 0.0
        for i in range(self.dim):
            coupling = 1.0 + 0.4 * np.cos(0.6 * i + 0.2 * np.sum(x**2))
            f3 += coupling * x[i] * np.exp(-0.1 * x[i]**2)
            
        # Multi-scale harmonic interactions with recursive spectral components
        f4 = 0.0
        for i in range(self.dim):
            scale_factor = 1.2 + 0.6 * np.sin(0.5 * i)
            harmonic_sum = 0.0
            for k in range(1, 8):
                harmonic_sum += np.sin(k * x[i]) / (k**1.5)
            f4 += harmonic_sum * scale_factor * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional elliptic couplings with adaptive weights
        f5 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 + 0.3 * np.sin(0.7 * (i + j) + 0.4 * np.sum(x**2))
                    coupling = x[i] * x[j] * weight
                    coupling_sum += coupling
            f5 += coupling_sum / (1.0 + 0.2 * np.abs(x[i]))
            
        # Boundary-sensitive elliptic oscillations with adaptive damping
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                damping_factor = 1.5 + 0.5 * np.cos(0.8 * i)
                f6 += damping_factor * np.exp(-2.0 * (5.0 - np.abs(x[i]))**2)
                
        # Resonant elliptic components with dynamic phase shifts
        f7 = 0.0
        for i in range(self.dim):
            phase_shift = 0.4 * np.sin(0.6 * i + 0.3 * np.sum(x**2))
            freq = 1.2 + 1.0 * np.cos(0.5 * i)
            f7 += np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i] + phase_shift)
            
        # Adaptive penalty terms with elliptic conditioning
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.5:
                chaos_factor = 1.2 + 0.6 * np.sin(0.7 * i + 0.3 * np.sum(x**2))
                f8 += chaos_factor * np.exp(-0.3 * (np.abs(x[i]) - 3.5)**2)
                
        # Multi-modal elliptic sinusoidal components with dynamic scaling
        f9 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.7 * np.cos(0.6 * i + 0.4 * np.sum(x**2))
            f9 += scale * np.sin(2.0 * x[i])**2
            
        # Exponential radial conditioning with elliptic modulation
        r = np.sqrt(np.sum(x**2))
        f10 = 0.0
        for i in range(self.dim):
            modulator = 1.3 + 0.5 * np.sin(0.4 * i + 0.3 * r)
            f10 += modulator * np.exp(-0.2 * x[i]**2) * np.sin(3.0 * x[i])**2
            
        # Additional nested chaotic components
        f11 = 0.0
        for i in range(self.dim):
            nested_term = np.sin(4.0 * x[i] + 0.3 * np.sum(x**2)) * np.cos(3.0 * x[i])
            f11 += nested_term * (1.0 + 0.3 * np.sin(0.4 * x[i]))
            
        # Enhanced multi-scale elliptic interactions
        f12 = 0.0
        for i in range(self.dim):
            scale_factor = 1.5 + 0.4 * np.cos(0.6 * i)
            harmonic_sum = 0.0
            for k in range(1, 7):
                harmonic_sum += np.cos(k * x[i]) / (k**1.2)
            f12 += harmonic_sum * np.exp(-0.15 * x[i]**2) * scale_factor
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12