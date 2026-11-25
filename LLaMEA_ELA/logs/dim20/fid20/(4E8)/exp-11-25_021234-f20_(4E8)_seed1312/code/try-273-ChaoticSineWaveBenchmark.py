import numpy as np

class ChaoticSineWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave potential terms with varying frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.3 * i + 0.1 * np.sum(x))
            amp = 1.5 + 2.0 * np.cos(0.2 * i + 0.05 * np.sum(x**2))
            f1 += amp * np.sin(freq * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Radial harmonic conditioning with dynamic scaling
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.1 * i + 0.03 * r)
            f2 += scale * np.cos(1.5 * x[i]) * np.exp(-0.1 * r**2)
            
        # Dynamic cross-dimensional couplings with time-varying weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.8 + 0.4 * np.sin(0.2 * (i - j) + 0.15 * r)
                f3 += weight * np.sin(x[i] + x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Boundary repulsion with exponential decay and chaotic modulation
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                chaos_mod = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * r)
                f4 += dist**3 * np.exp(-0.5 * dist) * chaos_mod
                
        # Multi-scale chaotic interactions with sine and cosine components
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) + np.cos(x[i] * x[j])
                scale = 0.6 + 0.4 * np.sin(0.3 * (i + j) + 0.1 * r)
                f5 += scale * interaction * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Adaptive quartic terms with chaotic frequency modulation
        f6 = 0.0
        for i in range(self.dim):
            freq_mod = 1.2 + 0.8 * np.sin(0.25 * i + 0.1 * r)
            f6 += x[i]**4 * np.exp(-0.03 * x[i]**2) * freq_mod
            
        # Fractal-like coupling with recursive sine-wave interactions
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.4 * (i - j) + 0.1 * r)
                f7 += phase * np.sin(x[i] + x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Hybrid polynomial-sine terms with dynamic weights
        f8 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(0.3 * i + 0.08 * r)
            f8 += weight * x[i]**3 * np.sin(x[i]) * np.exp(-0.07 * x[i]**2)
            
        # Enhanced chaotic cross-dimensional interactions with variable coupling
        f9 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_coupling = 0.5 + 0.3 * np.cos(0.2 * (i + j) + 0.1 * r)
                f9 += dynamic_coupling * np.tan(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Novel radial sine-wave with multi-harmonic components
        f10 = 0.0
        for i in range(self.dim):
            multiharmonic = np.sin(2.0 * x[i]) + 0.5 * np.sin(3.0 * x[i])
            f10 += multiharmonic * np.exp(-0.02 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10