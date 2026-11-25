import numpy as np

class TrigonometricFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial conditioning with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_factor = 1.0 + 0.8 * np.sin(0.4 * r) * np.cos(0.3 * r) * np.exp(-0.05 * r)
        
        # Multi-frequency trigonometric chaos with adaptive coupling
        f1 = 0.0
        for i in range(self.dim):
            freq1 = 1.5 + 4.0 * np.sin(0.1 * i + 0.2 * r)
            freq2 = 2.0 + 3.5 * np.cos(0.2 * i + 0.1 * r)
            f1 += (np.sin(freq1 * x[i]) + np.cos(freq2 * x[i])) * radial_factor
            
        # Complex fractal cross-dimensional interactions with time-varying couplings
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.7 + 0.3 * np.sin(0.15 * (i + j) + 0.25 * r)
                interaction = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                f2 += coupling_strength * interaction * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Dynamic phase-shifted harmonic terms with adaptive frequencies
        f3 = 0.0
        for i in range(self.dim):
            phase_shift = 0.8 * np.sin(0.15 * i + 0.4 * r)
            freq = 1.5 + 2.5 * np.cos(0.25 * i + 0.1 * r)
            f3 += np.sin(freq * x[i] + phase_shift) * np.exp(-0.07 * np.abs(x[i]))
            
        # Enhanced stochastic coupling with variable interaction strengths
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.4 + 0.6 * np.random.uniform(0, 1)
                f4 += strength * np.sin(x[i] * x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Stronger boundary repulsion with exponential scaling
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                penalty = 3.0 * np.sin(0.6 * (5.0 - np.abs(x[i])))**2
                f5 += penalty * np.exp(-0.15 * x[i]**2)
                
        # Enhanced multi-scale chaotic cubic terms with radial dependency
        f6 = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.6 * np.sin(0.35 * i + 0.15 * r)
            f6 += coeff * x[i]**3 * np.exp(-0.05 * x[i]**2)
            
        # Advanced fractal interactions with cosine modulation
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.2 + 0.6 * np.cos(0.25 * (i - j) + 0.35 * r)
                f7 += mod * np.sin(x[i] + x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic sine-wave interactions with variable amplitudes
        f8 = 0.0
        for i in range(self.dim):
            wave_freq = 4.0 + 5.0 * np.sin(0.2 * i)
            amp = 1.5 + 2.0 * np.cos(0.1 * i)
            f8 += amp * np.sin(wave_freq * x[i]) * np.exp(-0.08 * x[i]**2)
            
        # Adaptive radial harmonic terms with enhanced nonlinearity
        f9 = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.7 * np.cos(0.25 * i + 0.1 * r)
            freq = 3.0 + 4.0 * np.sin(0.15 * i + 0.05 * r)
            f9 += amp * np.sin(freq * x[i]) * np.exp(-0.02 * r**2)
            
        # Additional high-frequency chaotic component
        f10 = 0.0
        for i in range(self.dim):
            freq = 8.0 + 6.0 * np.sin(0.3 * i + 0.2 * r)
            f10 += np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Novel hybrid cubic-sine terms with enhanced radial coupling
        f11 = 0.0
        for i in range(self.dim):
            hybrid_coeff = 2.0 + 1.5 * np.sin(0.4 * i + 0.2 * r)
            f11 += hybrid_coeff * (x[i]**3 + np.sin(x[i])) * np.exp(-0.06 * x[i]**2)
            
        # Additional multi-scale fractal sine-cosine couplings
        f12 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 1.0 + 0.5 * np.sin(0.3 * (i - j) + 0.2 * r)
                f12 += scale_factor * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Enhanced chaotic Gaussian-like terms with variable amplitudes
        f13 = 0.0
        for i in range(self.dim):
            amp = 2.5 + 1.0 * np.sin(0.2 * i + 0.1 * r)
            f13 += amp * np.exp(-0.5 * (x[i] - np.sin(x[i]))**2) * np.exp(-0.03 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13