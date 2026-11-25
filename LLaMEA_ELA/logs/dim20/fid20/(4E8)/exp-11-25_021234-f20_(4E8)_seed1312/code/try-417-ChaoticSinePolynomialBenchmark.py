import numpy as np

class ChaoticSinePolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave components with time-varying frequencies
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            f1 += np.sin(freq * x[i])**3 * (1.0 + 0.2 * np.cos(0.4 * x[i]))
            
        # Radial polynomial interactions with dynamic exponents
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            exp_mod = 2.5 + 1.2 * np.sin(0.35 * i + 0.25 * r)
            f2 += (x[i]**exp_mod) * np.exp(-0.12 * x[i]**2)
            
        # Adaptive elliptic conditioning with cross-dimensional coupling
        f3 = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.5 * np.cos(0.4 * i)
            f3 += (x[i]**2) / (1.0 + condition_factor * np.sin(0.3 * x[i])**2)
            
        # Multi-scale chaotic dynamics with recursive sine components
        f4 = 0.0
        for i in range(self.dim):
            scale_factor = 1.5 + 0.5 * np.cos(0.6 * i)
            recursive_term = np.sin(scale_factor * x[i] / (1.0 + 0.1 * np.sum(x**2)))**3
            f4 += recursive_term * (1.0 + 0.3 * np.sin(0.4 * x[i]))
            
        # Cross-dimensional polynomial couplings with variable weights
        f5 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 1.0 + 0.3 * np.cos(0.5 * (i + j) + 0.2 * np.sum(x**2))
                    coupling = x[i] * x[j]**2 * weight
                    coupling_sum += coupling
            f5 += coupling_sum * np.exp(-0.12 * x[i]**2)
            
        # Boundary-sensitive polynomial oscillations with adaptive damping
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                damping_factor = 1.2 + 0.6 * np.cos(0.6 * i)
                f6 += damping_factor * np.exp(-2.0 * (5.0 - np.abs(x[i]))**2)
                
        # Resonant polynomial components with dynamic exponent shifts
        f7 = 0.0
        for i in range(self.dim):
            exp_shift = 0.5 + 1.0 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            f7 += (x[i]**(2.0 + exp_shift)) * (1.0 + 0.4 * np.sin(0.5 * x[i]))
            
        # Adaptive penalty terms with polynomial conditioning
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.5:
                chaos_factor = 1.2 + 0.7 * np.cos(0.5 * i + 0.2 * np.sum(x**2))
                f8 += chaos_factor * np.exp(-0.22 * (np.abs(x[i]) - 3.5)**2)
                
        # Multi-modal polynomial sinusoidal components with dynamic phase shifts
        f9 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.cos(0.6 * i + 0.4 * np.sum(x**2))
            freq_mod = 1.3 + 0.8 * np.sin(0.3 * i)
            f9 += (np.sin(freq_mod * x[i] + phase_shift)**2) * (x[i]**2)
            
        # Exponential radial conditioning with polynomial modulation
        r = np.sqrt(np.sum(x**2))
        f10 = 0.0
        for i in range(self.dim):
            modulator = 1.3 + 0.4 * np.cos(0.3 * i + 0.2 * r)
            f10 += modulator * np.exp(-0.12 * x[i]**2)
            f10 += (x[i]**3) * np.sin(2.0 * x[i])**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10