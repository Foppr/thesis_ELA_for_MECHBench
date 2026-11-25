import numpy as np

class TrigonometricFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial conditioning with trigonometric modulation
        r = np.sqrt(np.sum(x**2))
        radial_factor = 1.0 + 0.5 * np.sin(0.3 * r) * np.cos(0.2 * r)
        
        # Trigonometric chaos with multiple frequency components
        f1 = 0.0
        for i in range(self.dim):
            freq1 = 2.5 + 2.5 * np.sin(0.1 * i)
            freq2 = 1.8 + 2.2 * np.cos(0.2 * i)
            f1 += (np.sin(freq1 * x[i]) + np.cos(freq2 * x[i])) * radial_factor
            
        # Fractal-like cross-dimensional interactions with recursive coupling
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.6 + 0.4 * np.sin(0.15 * (i + j) + 0.25 * r)
                interaction = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                f2 += coupling_strength * interaction * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Dynamic phase-shifted harmonic terms
        f3 = 0.0
        for i in range(self.dim):
            phase_shift = 0.6 * np.sin(0.15 * i + 0.35 * r)
            freq = 1.2 + 1.8 * np.cos(0.25 * i)
            f3 += np.sin(freq * x[i] + phase_shift) * np.exp(-0.05 * np.abs(x[i]))
            
        # Stochastic coupling with varying interaction strengths
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.2 + 0.8 * np.random.uniform(0, 1)
                f4 += strength * np.sin(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Boundary repulsion with trigonometric scaling
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                penalty = 2.5 * np.sin(0.6 * (5.0 - np.abs(x[i])))**2
                f5 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Multi-scale chaotic cubic terms
        f6 = 0.0
        for i in range(self.dim):
            coeff = 0.9 + 0.3 * np.sin(0.35 * i + 0.15 * r)
            f6 += coeff * x[i]**3 * np.exp(-0.04 * x[i]**2)
            
        # Cross-dimensional fractal interactions with sine modulation
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.1 + 0.3 * np.sin(0.25 * (i - j) + 0.35 * r)
                f7 += mod * np.sin(x[i] + x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic sine-wave interactions
        f8 = 0.0
        for i in range(self.dim):
            wave_freq = 3.5 + 3.5 * np.sin(0.18 * i)
            f8 += np.sin(wave_freq * x[i]) * np.exp(-0.06 * x[i]**2)
            
        # Adaptive radial harmonic terms
        f9 = 0.0
        for i in range(self.dim):
            amp = 1.1 + 0.4 * np.cos(0.25 * i)
            freq = 2.2 + 2.8 * np.sin(0.12 * i)
            f9 += amp * np.sin(freq * x[i]) * np.exp(-0.01 * r**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9