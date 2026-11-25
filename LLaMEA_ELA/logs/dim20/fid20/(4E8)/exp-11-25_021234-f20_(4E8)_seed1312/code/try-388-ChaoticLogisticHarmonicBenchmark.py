import numpy as np

class ChaoticLogisticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map components with time-varying parameters
        f1 = 0.0
        for i in range(self.dim):
            r = 3.9 + 0.2 * np.sin(0.25 * i + 0.15 * np.sum(x**2))
            logistic_term = r * x[i] * (1.0 - x[i]**2)
            f1 += logistic_term * (1.0 + 0.15 * np.cos(0.55 * x[i]))
            
        # Radial harmonic interactions with dynamic frequency modulation
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            freq_mod = 1.4 + 0.7 * np.sin(0.35 * i + 0.25 * r)
            f2 += np.sin(freq_mod * x[i])**2 * np.exp(-0.12 * x[i]**2)
            
        # Adaptive gradient conditioning with elliptic coupling
        f3 = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.45 * np.cos(0.45 * i)
            f3 += (x[i]**2) / (1.0 + condition_factor * np.sin(0.35 * x[i])**2)
            
        # Multi-scale chaotic dynamics with fractal-like recursion
        f4 = 0.0
        for i in range(self.dim):
            scale_factor = 1.25 + 0.35 * np.cos(0.65 * i)
            recursive_term = np.sin(scale_factor * x[i] / (1.0 + 0.12 * np.sum(x**2)))**3
            f4 += recursive_term * (1.0 + 0.25 * np.sin(0.45 * x[i]))
            
        # Cross-dimensional chaotic couplings with time-varying weights
        f5 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 + 0.25 * np.cos(0.55 * (i + j) + 0.25 * np.sum(x**2))
                    coupling = x[i] * x[j] * weight
                    coupling_sum += coupling
            f5 += coupling_sum * np.exp(-0.12 * x[i]**2)
            
        # Boundary-sensitive chaotic oscillations with adaptive damping
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                damping_factor = 1.15 + 0.45 * np.cos(0.65 * i)
                f6 += damping_factor * np.exp(-2.0 * (5.0 - np.abs(x[i]))**2)
                
        # Resonant chaotic components with dynamic frequency shifts
        f7 = 0.0
        for i in range(self.dim):
            freq = 1.05 + 1.45 * np.sin(0.45 * i + 0.35 * np.sum(x**2))
            f7 += np.sin(freq * x[i]) * np.cos(freq * x[i]) * (1.0 + 0.35 * np.sin(0.55 * x[i]))
            
        # Adaptive penalty terms with chaotic conditioning
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.5:
                chaos_factor = 1.05 + 0.65 * np.cos(0.55 * i + 0.25 * np.sum(x**2))
                f8 += chaos_factor * np.exp(-0.22 * (np.abs(x[i]) - 3.5)**2)
                
        # Multi-modal chaotic sinusoidal components with dynamic phase shifts
        f9 = 0.0
        for i in range(self.dim):
            phase_shift = 0.45 * np.cos(0.65 * i + 0.45 * np.sum(x**2))
            freq_mod = 1.15 + 0.75 * np.sin(0.35 * i)
            f9 += np.sin(freq_mod * x[i] + phase_shift)**2
            
        # Exponential radial conditioning with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        f10 = 0.0
        for i in range(self.dim):
            modulator = 1.15 + 0.35 * np.cos(0.35 * i + 0.25 * r)
            f10 += modulator * np.exp(-0.12 * x[i]**2) * np.sin(2.0 * x[i])**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10