import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential terms with higher-order terms and exponential damping
        f1 = 0.0
        for i in range(self.dim):
            f1 += (x[i]**2 + 0.4 * x[i]**4 + 0.2 * x[i]**6 + 0.1 * x[i]**8) * np.exp(-0.15 * x[i]**2)
            
        # Radial harmonic interactions with dynamic frequency modulation and time-varying weights
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            weight = 1.2 + 0.3 * np.sin(0.25 * i + 0.15 * r + 0.3 * np.random.uniform(-1, 1))
            freq = 2.5 + 1.5 * np.cos(0.2 * i + 0.1 * r)
            f2 += weight * np.sin(freq * x[i]) * np.cos(1.5 * x[i])
            
        # Cross-dimensional coupling with fractal-like interaction strengths and dynamic phase shifts
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.9 + 0.3 * np.sin(0.2 * (i + j) + 0.25 * r + 0.4 * np.random.uniform(-1, 1))
                phase_shift = 0.1 * np.sin(0.3 * i + 0.2 * j + 0.1 * r)
                interaction = np.sin(x[i] + x[j] + phase_shift) + np.cos(x[i] - x[j] + phase_shift)
                f3 += coupling_strength * interaction * np.exp(-0.07 * (x[i]**2 + x[j]**2))
                
        # Enhanced boundary attraction with multiple penalty functions
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                penalty = 1.5 * (np.abs(x[i]) - 4.0)**3 + 0.5 * (np.abs(x[i]) - 4.0)**4
                f4 += penalty * np.exp(-0.12 * x[i]**2)
                
        # Time-varying weights with chaotic modulation and dynamic scaling
        f5 = 0.0
        for i in range(self.dim):
            time_weight = 1.0 + 0.4 * np.sin(0.35 * i + 0.25 * r + 0.5 * np.random.uniform(-1, 1))
            scale_factor = 1.0 + 0.2 * np.cos(0.1 * i + 0.3 * r)
            f5 += time_weight * scale_factor * x[i]**5 * np.exp(-0.1 * x[i]**2)
            
        # Multi-scale fractal-like interactions with enhanced sine modulation and exponential decay
        f6 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(0.6 * i + 0.4 * r + 0.2 * np.random.uniform(-1, 1))
            f6 += scale_factor * np.sin(6.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Enhanced cross-dimensional quartic terms with adaptive weights
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.6 + 0.4 * np.cos(0.25 * (i - j) + 0.35 * r + 0.3 * np.random.uniform(-1, 1))
                f7 += weight * x[i]**4 * x[j]**2 * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Additional boundary repulsion with polynomial and exponential components
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty = 1.2 * np.exp(-0.25 * (np.abs(x[i]) - 4.5)**2) + 0.3 * (np.abs(x[i]) - 4.5)**3
                f8 += penalty * np.exp(-0.15 * x[i]**2)
                
        # Adaptive radial conditioning with enhanced polynomial scaling and dynamic modulation
        radial_factor = 1.0 + 0.7 * np.sin(0.35 * r) * np.cos(0.25 * r) + 0.2 * np.random.uniform(-1, 1)
        f9 = 0.0
        for i in range(self.dim):
            f9 += radial_factor * x[i]**3 * np.exp(-0.04 * x[i]**2)
            
        # Combined harmonic and polynomial terms with dynamic coupling and frequency modulation
        f10 = 0.0
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(0.15 * i + 0.08 * r + 0.2 * np.random.uniform(-1, 1))
            f10 += np.sin(freq * x[i]) * (x[i]**2 + 1.5) * np.exp(-0.09 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10