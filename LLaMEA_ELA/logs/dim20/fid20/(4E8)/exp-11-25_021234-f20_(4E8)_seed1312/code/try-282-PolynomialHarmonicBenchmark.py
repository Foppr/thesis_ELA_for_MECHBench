import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential terms with chaotic degree variations
        f1 = 0.0
        for i in range(self.dim):
            degree = 3 + int(5 * np.sin(0.3 * i + 0.15 * np.sqrt(np.sum(x**2))))
            f1 += x[i]**degree
            
        # Modified radial harmonic interactions with fractal frequency scaling
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 2.0 * np.sin(0.15 * i + 0.1 * r + 0.2 * np.sin(r))
            f2 += np.sin(freq * x[i]) * np.exp(-0.15 * r**2)
            
        # Novel cross-dimensional coupling with fractal weight variations
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.8 + 0.5 * np.sin(0.2 * (i + j) + 0.3 * r + 0.1 * np.cos(r))
                f3 += weight * x[i] * x[j] * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Enhanced boundary attraction with logarithmic decay
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                f4 += dist**3 * np.exp(-0.5 * dist)
                
        # Multi-scale polynomial interactions with dynamic coefficients
        f5 = 0.0
        for i in range(self.dim):
            coeff = 1.5 + 0.8 * np.sin(0.4 * i + 0.15 * r + 0.2 * np.cos(r))
            f5 += coeff * x[i]**5 * np.exp(-0.05 * x[i]**2)
            
        # Fractal-like harmonic coupling with recursive structure and phase modulation
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.5 + 0.4 * np.sin(0.3 * (i - j) + 0.08 * r + 0.1 * np.sin(r))
                phase = 0.2 * np.cos(0.2 * i + 0.1 * j + 0.15 * r)
                f6 += scale * np.cos(x[i] + x[j] + phase) * np.exp(-0.07 * (x[i]**2 + x[j]**2))
                
        # Adaptive quartic terms with enhanced radial conditioning
        f7 = 0.0
        for i in range(self.dim):
            coeff = 2.0 + 0.4 * np.cos(0.2 * i + 0.15 * r + 0.1 * np.sin(r))
            f7 += coeff * x[i]**5 * np.exp(-0.04 * r**2)
            
        # Mixed trigonometric and polynomial cross-terms with chaotic modulation
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_mod = 0.5 + 0.3 * np.sin(0.2 * (i + j) + 0.1 * r)
                f8 += chaos_mod * np.sin(x[i] * x[j]) * x[i]**3 * x[j]**3 * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Enhanced boundary repulsion with exponential penalties
        f9 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty = 3.0 * (5.0 - np.abs(x[i]))**4
                f9 += penalty * np.exp(-0.15 * x[i]**2)
                
        # Dynamic harmonic modulation with chaotic amplitudes and frequencies
        f10 = 0.0
        for i in range(self.dim):
            amp = 2.0 + 1.5 * np.sin(0.25 * i + 0.4 * r + 0.3 * np.sin(r))
            freq = 1.5 + 1.8 * np.cos(0.15 * i + 0.25 * np.sin(r))
            f10 += amp * np.sin(freq * x[i]) * np.exp(-0.12 * x[i]**2)
            
        # Combined polynomial and harmonic terms with chaotic weights
        f11 = 0.0
        for i in range(self.dim):
            weight = 1.5 + 0.6 * np.sin(0.3 * i + 0.15 * r + 0.2 * np.cos(r))
            f11 += weight * x[i]**4 * np.cos(x[i]) * np.exp(-0.07 * x[i]**2)
            
        # Cross-dimensional quintic interactions with chaotic coupling
        f12 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_weight = 1.0 + 0.4 * np.sin(0.35 * (i - j) + 0.25 * r + 0.1 * np.cos(r))
                f12 += dynamic_weight * x[i]**4 * x[j]**4 * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic modulation with higher-order terms
        f13 = 0.0
        for i in range(self.dim):
            chaos_factor = 0.6 * np.sin(0.6 * i + 0.15 * r + 0.2 * np.cos(r) + 0.1 * np.sin(r))
            f13 += x[i]**3 * np.exp(-0.03 * x[i]**2) * chaos_factor
            
        # Hybrid coupling with enhanced sine and cosine components
        f14 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hybrid_term = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                f14 += hybrid_term * x[i]**3 * x[j]**3 * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Novel chaotic cross-dimensional term with complex interaction
        f15 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(0.3 * (i + j) + 0.15 * r + 0.2 * np.cos(r))
                scale_factor = 1.3 + 0.3 * np.cos(0.2 * (i - j) + 0.08 * r + 0.1 * np.sin(r))
                interaction = np.tan(x[i] * x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                f15 += scale_factor * phase_shift * interaction
                
        # Novel radial polynomial with higher-order terms and chaotic scaling
        f16 = 0.0
        for i in range(self.dim):
            coeff = 2.5 + 1.5 * np.sin(0.25 * i + 0.15 * r + 0.2 * np.cos(r))
            radial_term = x[i]**5 * np.exp(-0.02 * r**2)
            f16 += coeff * radial_term
            
        # Fractal dimensionality scaling term
        fractal_scale = 0.5 + 0.3 * np.sin(0.2 * r + 0.1 * np.cos(r))
        f17 = 0.0
        for i in range(self.dim):
            f17 += x[i]**6 * fractal_scale * np.exp(-0.03 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17