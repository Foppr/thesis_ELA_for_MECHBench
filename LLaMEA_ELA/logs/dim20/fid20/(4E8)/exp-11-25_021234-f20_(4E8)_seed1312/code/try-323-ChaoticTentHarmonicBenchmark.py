import numpy as np

class ChaoticTentHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r = 1.5
        self.tent_map = np.zeros(dim)
        for i in range(dim):
            self.tent_map[i] = 0.3 + 0.4 * np.sin(0.5 * i)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map dynamics with adaptive scaling
        f1 = 0.0
        for i in range(self.dim):
            # Tent map with parameter modulation
            param = self.tent_map[i] * (1.0 + 0.3 * np.cos(0.4 * i))
            if x[i] < 0.5:
                chaotic_val = param * x[i]
            else:
                chaotic_val = param * (1.0 - x[i])
            f1 += chaotic_val * np.sin(2.0 * x[i])**2
            
        # Radial harmonic interactions with varying frequencies
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i + 0.2 * r)
            amp = 1.0 + 0.5 * np.cos(0.4 * i + 0.1 * r)
            f2 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Adaptive gradient conditioning with exponential penalties
        f3 = 0.0
        for i in range(self.dim):
            grad_amp = 1.5 + 0.8 * np.sin(0.5 * i)
            penalty = grad_amp * np.exp(-0.1 * x[i]**2) * (1.0 + 0.4 * np.cos(0.6 * x[i]))
            f3 += penalty
            
        # Cross-dimensional coupling with chaotic interaction weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic weight based on tent map
                weight = (0.5 + 0.3 * np.sin(self.tent_map[i] + self.tent_map[j])) * \
                         np.exp(-0.1 * (i + j))
                interaction = np.sin(x[i]) * np.cos(x[j]) - np.cos(x[i]) * np.sin(x[j])
                f4 += weight * interaction * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Multi-scale chaotic oscillations with varying amplitudes
        f5 = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.6 * np.sin(0.4 * i)
            freq = 3.0 + 2.0 * np.cos(0.3 * i)
            f5 += amp * np.sin(freq * x[i]) * np.exp(-0.08 * x[i]**2)
            
        # Boundary repulsion with chaotic strength modulation
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                strength = 1.5 + 0.7 * np.sin(0.6 * i + 0.3 * r)
                f6 += strength * np.exp(-1.5 * (5.0 - np.abs(x[i]))**2)
                
        # Fractal-like chaotic radial terms with recursive tent dynamics
        f7 = 0.0
        for i in range(self.dim):
            # Recursive tent modulation
            mod = 1.0 + 0.4 * np.sin(0.5 * i + 0.3 * r)
            f7 += mod * np.sin(np.pi * x[i] / (1.0 + 0.3 * r))**2
            
        # Multi-modal chaotic penalty terms with adaptive scales
        f8 = 0.0
        for i in range(self.dim):
            scale = 0.8 + 0.4 * np.sin(0.5 * i)
            f8 += scale * np.exp(-0.1 * (x[i] - 1.5)**2) + \
                   scale * np.exp(-0.1 * (x[i] + 1.5)**2)
            
        # Adaptive harmonic coupling with chaotic phase shifts
        f9 = 0.0
        for i in range(self.dim):
            freq = 2.5 + 1.0 * np.sin(0.3 * i)
            phase_shift = 0.2 * np.cos(0.4 * i + 0.1 * r)
            f9 += np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i] + phase_shift)
            
        # Polynomial chaotic cross-terms with exponential weighting
        f10 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.7 + 0.3 * np.sin(0.2 * (i + j))
                weight = np.exp(-0.03 * (x[i]**2 + x[j]**2)) * \
                         (1.0 + 0.3 * np.cos(0.4 * (i - j)))
                f10 += coeff * x[i]**3 * x[j]**2 * weight
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10