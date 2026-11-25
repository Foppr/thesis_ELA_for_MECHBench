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
            
        # Fractal cross-dimensional interactions with dynamic coupling strengths
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.7 + 0.3 * np.sin(0.15 * (i + j) + 0.25 * r)
                interaction = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                f2 += coupling_strength * interaction * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Dynamic phase-shifted harmonic terms with stochastic modulation
        f3 = 0.0
        for i in range(self.dim):
            phase_shift = 0.8 * np.sin(0.1 * i + 0.4 * r + 0.5 * np.random.uniform(-1, 1))
            freq = 1.5 + 2.5 * np.cos(0.2 * i + 0.3 * np.random.uniform(-1, 1))
            f3 += np.sin(freq * x[i] + phase_shift) * np.exp(-0.06 * np.abs(x[i]))
            
        # Stochastic coupling with varying interaction strengths and fractal scaling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.4 + 0.6 * np.random.uniform(0, 1) * np.sin(0.2 * (i - j))
                f4 += strength * np.sin(x[i] * x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Enhanced boundary repulsion with multi-scale trigonometric penalties
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                penalty = 3.0 * np.sin(0.6 * (5.0 - np.abs(x[i])))**2
                f5 += penalty * np.exp(-0.15 * x[i]**2)
                
        # Multi-scale chaotic cubic terms with dynamic coefficients
        f6 = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.6 * np.sin(0.4 * i + 0.2 * r) * np.cos(0.3 * r)
            f6 += coeff * x[i]**3 * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional fractal interactions with enhanced sine modulation
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.2 + 0.6 * np.sin(0.3 * (i - j) + 0.4 * r)
                f7 += mod * np.sin(x[i] + x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic sine-wave interactions with exponential decay
        f8 = 0.0
        for i in range(self.dim):
            wave_freq = 4.0 + 5.0 * np.sin(0.2 * i + 0.15 * r)
            f8 += np.sin(wave_freq * x[i]) * np.exp(-0.07 * x[i]**2)
            
        # Adaptive radial harmonic terms with enhanced complexity
        f9 = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.7 * np.cos(0.3 * i + 0.2 * r)
            freq = 3.0 + 4.0 * np.sin(0.15 * i + 0.1 * r)
            f9 += amp * np.sin(freq * x[i]) * np.exp(-0.02 * r**2)
            
        # Additional chaotic coupling with exponential weights
        f10 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.sin(0.1 * (i + j) + 0.3 * r)
                f10 += weight * np.cos(x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Added cubic cross-terms with modified weights for increased complexity
        f11 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.3 + 0.4 * np.sin(0.25 * (i - j) + 0.3 * r)
                f11 += weight * x[i]**3 * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Quartic cross-terms with time-varying coefficients
        f12 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                time_coeff = 1.0 + 0.5 * np.sin(0.1 * (i + j) + 0.2 * r + 0.3 * np.random.uniform(-1, 1))
                f12 += time_coeff * x[i]**4 * x[j]**2 * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Time-varying radial harmonic terms with quartic modulation
        f13 = 0.0
        for i in range(self.dim):
            time_amp = 2.0 + 1.0 * np.cos(0.2 * i + 0.1 * r + 0.4 * np.random.uniform(-1, 1))
            time_freq = 5.0 + 3.0 * np.sin(0.1 * i + 0.05 * r + 0.2 * np.random.uniform(-1, 1))
            f13 += time_amp * np.sin(time_freq * x[i]) * np.exp(-0.08 * x[i]**4)
            
        # Enhanced boundary repulsion with quartic penalties
        f14 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty = 2.0 * np.sin(0.7 * (5.0 - np.abs(x[i])))**4
                f14 += penalty * np.exp(-0.2 * x[i]**4)
                
        # Dynamic fractal cross-terms with exponential decay and quartic interactions
        f15 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_weight = 0.8 + 0.2 * np.sin(0.3 * (i - j) + 0.4 * r + 0.1 * np.random.uniform(-1, 1))
                f15 += dynamic_weight * np.sin(x[i] * x[j]**2) * np.exp(-0.06 * (x[i]**2 + x[j]**4))
                
        # Additional enhancement with modified exponential weights and refined interactions
        f16 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.6 + 0.4 * np.sin(0.2 * (i - j) + 0.3 * r)
                f16 += weight * x[i]**2 * x[j]**3 * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Final refined quartic interactions with adaptive scaling
        f17 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale_factor = 1.5 + 0.5 * np.sin(0.1 * (i + j) + 0.2 * r)
                f17 += scale_factor * x[i]**4 * x[j]**3 * np.exp(-0.07 * (x[i]**2 + x[j]**2))
                
        # Additional sine-cosine harmonics with complex exponential decay
        f18 = 0.0
        for i in range(self.dim):
            freq1 = 2.0 + 3.0 * np.sin(0.15 * i + 0.1 * r)
            freq2 = 1.5 + 2.5 * np.cos(0.2 * i + 0.05 * r)
            f18 += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])) * np.exp(-0.03 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18