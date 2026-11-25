import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential terms with adaptive degrees
        f1 = 0.0
        for i in range(self.dim):
            degree = 2 + int(2 * np.sin(0.3 * i) + 1)
            f1 += x[i]**degree
            
        # Adaptive harmonic interactions with dynamic frequencies and amplitudes
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 1.5 * np.sin(0.15 * i + 0.08 * r)
            amp = 1.0 + 0.5 * np.cos(0.2 * i + 0.1 * r)
            f2 += amp * np.sin(freq * x[i]) * np.exp(-0.05 * r**2)
            
        # Dynamic cross-dimensional coupling with time-varying weights and phase shifts
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.6 + 0.4 * np.sin(0.2 * (i + j) + 0.15 * r)
                phase_shift = np.sin(0.1 * (i - j) + 0.05 * r)
                f3 += weight * phase_shift * x[i] * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Improved boundary attraction with exponential decay and adaptive penalties
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                dist = np.abs(x[i]) - 4.2
                penalty = 2.0 * dist**2 + 0.5 * dist**3
                f4 += penalty * np.exp(-0.3 * dist)
                
        # Enhanced multi-scale polynomial interactions with varying coefficients
        f5 = 0.0
        for i in range(self.dim):
            coeff = 1.2 + 0.8 * np.sin(0.4 * i + 0.15 * r)
            f5 += coeff * x[i]**4 * np.exp(-0.02 * x[i]**2)
            
        # Fractal-like harmonic coupling with recursive structure and modified scaling
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 0.8 + 0.4 * np.sin(0.3 * (i - j) + 0.1 * r)
                f6 += scale * np.cos(x[i] + x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Adaptive quartic terms with enhanced radial conditioning
        f7 = 0.0
        for i in range(self.dim):
            coeff = 1.8 + 0.6 * np.cos(0.2 * i + 0.15 * r)
            f7 += coeff * x[i]**4 * np.exp(-0.01 * r**2)
            
        # Mixed trigonometric and polynomial cross-terms with enhanced complexity
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f8 += np.sin(x[i] * x[j]) * x[i]**2 * x[j]**2 * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Enhanced boundary repulsion with polynomial penalties and adaptive scaling
        f9 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.7:
                penalty = 2.5 * (5.0 - np.abs(x[i]))**3
                f9 += penalty * np.exp(-0.15 * x[i]**2)
                
        # Dynamic harmonic modulation with time-varying amplitudes and frequencies
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.8 * np.sin(0.25 * i + 0.4 * r + 0.3 * np.random.uniform(-1, 1))
            freq = 1.2 + 1.2 * np.cos(0.15 * i + 0.25 * np.random.uniform(-1, 1))
            f10 += amp * np.sin(freq * x[i]) * np.exp(-0.06 * x[i]**2)
            
        # Combined polynomial and harmonic terms with adaptive weights and enhanced nonlinearity
        f11 = 0.0
        for i in range(self.dim):
            weight = 1.3 + 0.7 * np.sin(0.3 * i + 0.15 * r)
            f11 += weight * x[i]**3 * np.cos(x[i]) * np.exp(-0.03 * x[i]**2)
            
        # Cross-dimensional quartic interactions with enhanced dynamic coupling
        f12 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_weight = 0.9 + 0.3 * np.sin(0.4 * (i - j) + 0.25 * r)
                f12 += dynamic_weight * x[i]**3 * x[j]**3 * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic modulation for increased complexity with modified parameters
        f13 = 0.0
        for i in range(self.dim):
            chaos_factor = 0.4 * np.sin(0.6 * i + 0.15 * r + np.pi/6)
            f13 += x[i]**2 * np.exp(-0.008 * x[i]**2) * chaos_factor
            
        # Hybrid coupling with sine and cosine components and enhanced interaction
        f14 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hybrid_term = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                f14 += hybrid_term * x[i]**2 * x[j]**2 * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Novel chaotic cross-dimensional term with modified interaction and scaling
        f15 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(0.3 * (i + j) + 0.1 * r)
                scale_factor = 1.2 + 0.4 * np.cos(0.2 * (i - j) + 0.08 * r)
                interaction = np.tan(x[i] * x[j]) * np.exp(-0.01 * (x[i]**2 + x[j]**2))
                f15 += scale_factor * phase_shift * interaction
                
        # Novel radial polynomial with higher-order terms and improved scaling
        f16 = 0.0
        for i in range(self.dim):
            coeff = 2.2 + 1.2 * np.sin(0.25 * i + 0.15 * r)
            radial_term = x[i]**4 * np.exp(-0.008 * r**2)
            f16 += coeff * radial_term
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16