import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential terms with chaotic degree variations and dynamic scaling
        f1 = 0.0
        for i in range(self.dim):
            degree = 3 + int(7 * np.sin(0.4 * i + 0.2 * np.sqrt(np.sum(x**2)) + 0.1 * np.cos(i)))
            f1 += x[i]**degree * (1.0 + 0.3 * np.sin(0.3 * i + 0.1 * np.sum(x**2)))
            
        # Modified radial harmonic interactions with fractal frequency scaling and phase modulation
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.2 * i + 0.15 * r + 0.25 * np.sin(r) + 0.1 * np.cos(r))
            phase = 0.1 * np.sin(0.2 * i + 0.1 * r)
            f2 += np.sin(freq * x[i] + phase) * np.exp(-0.2 * r**2)
            
        # Novel cross-dimensional coupling with fractal weight variations and chaotic interaction
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.7 + 0.6 * np.sin(0.25 * (i + j) + 0.3 * r + 0.15 * np.cos(r) + 0.08 * np.sin(i+j))
                f3 += weight * x[i] * x[j] * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (1.0 + 0.2 * np.sin(0.1 * i + 0.15 * j))
                
        # Enhanced boundary attraction with logarithmic decay and chaotic scaling
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                scale = 1.0 + 0.5 * np.sin(0.2 * i + 0.1 * r)
                f4 += dist**3 * np.exp(-0.6 * dist) * scale
                
        # Multi-scale polynomial interactions with dynamic coefficients and fractal modulation
        f5 = 0.0
        for i in range(self.dim):
            coeff = 1.2 + 1.0 * np.sin(0.4 * i + 0.2 * r + 0.25 * np.cos(r) + 0.1 * np.sin(i))
            f5 += coeff * x[i]**5 * np.exp(-0.08 * x[i]**2) * (1.0 + 0.3 * np.cos(0.1 * i + 0.1 * r))
            
        # Fractal-like harmonic coupling with recursive structure, phase modulation and dynamic scaling
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.2 + 0.5 * np.sin(0.3 * (i - j) + 0.1 * r + 0.15 * np.sin(r) + 0.08 * np.cos(i+j))
                phase = 0.15 * np.cos(0.2 * i + 0.1 * j + 0.2 * r + 0.1 * np.sin(r))
                f6 += scale * np.cos(x[i] + x[j] + phase) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (1.0 + 0.2 * np.sin(0.1 * i + 0.1 * j))
                
        # Adaptive quartic terms with enhanced radial conditioning and chaotic modulation
        f7 = 0.0
        for i in range(self.dim):
            coeff = 1.8 + 0.6 * np.cos(0.2 * i + 0.2 * r + 0.15 * np.sin(r) + 0.1 * np.cos(i))
            f7 += coeff * x[i]**5 * np.exp(-0.06 * r**2) * (1.0 + 0.25 * np.sin(0.1 * i + 0.1 * r))
            
        # Mixed trigonometric and polynomial cross-terms with chaotic modulation and fractal scaling
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_mod = 0.6 + 0.4 * np.sin(0.25 * (i + j) + 0.15 * r + 0.1 * np.cos(r))
                f8 += chaos_mod * np.sin(x[i] * x[j]) * x[i]**3 * x[j]**3 * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (1.0 + 0.2 * np.cos(0.1 * i + 0.1 * j))
                
        # Enhanced boundary repulsion with exponential penalties and chaotic scaling
        f9 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty = 2.5 * (5.0 - np.abs(x[i]))**4
                scale = 1.0 + 0.3 * np.sin(0.2 * i + 0.1 * r)
                f9 += penalty * np.exp(-0.2 * x[i]**2) * scale
                
        # Dynamic harmonic modulation with chaotic amplitudes, frequencies and fractal scaling
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.8 + 2.0 * np.sin(0.3 * i + 0.35 * r + 0.3 * np.sin(r) + 0.1 * np.cos(i))
            freq = 1.8 + 2.2 * np.cos(0.2 * i + 0.3 * np.sin(r) + 0.15 * np.cos(r))
            f10 += amp * np.sin(freq * x[i]) * np.exp(-0.15 * x[i]**2) * (1.0 + 0.2 * np.sin(0.1 * i + 0.1 * r))
            
        # Combined polynomial and harmonic terms with chaotic weights and fractal modulation
        f11 = 0.0
        for i in range(self.dim):
            weight = 1.3 + 0.7 * np.sin(0.35 * i + 0.2 * r + 0.25 * np.cos(r) + 0.1 * np.sin(i))
            f11 += weight * x[i]**4 * np.cos(x[i]) * np.exp(-0.1 * x[i]**2) * (1.0 + 0.3 * np.cos(0.1 * i + 0.1 * r))
            
        # Cross-dimensional quintic interactions with chaotic coupling and fractal scaling
        f12 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_weight = 0.9 + 0.5 * np.sin(0.4 * (i - j) + 0.3 * r + 0.15 * np.cos(r) + 0.1 * np.sin(i+j))
                f12 += dynamic_weight * x[i]**4 * x[j]**4 * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (1.0 + 0.2 * np.sin(0.1 * i + 0.1 * j))
                
        # Additional chaotic modulation with higher-order terms and fractal scaling
        f13 = 0.0
        for i in range(self.dim):
            chaos_factor = 0.7 * np.sin(0.7 * i + 0.2 * r + 0.25 * np.cos(r) + 0.15 * np.sin(r) + 0.08 * np.cos(i))
            f13 += x[i]**3 * np.exp(-0.04 * x[i]**2) * chaos_factor
            
        # Hybrid coupling with enhanced sine and cosine components, fractal modulation and chaotic scaling
        f14 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hybrid_term = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                f14 += hybrid_term * x[i]**3 * x[j]**3 * np.exp(-0.07 * (x[i]**2 + x[j]**2)) * (1.0 + 0.25 * np.sin(0.1 * i + 0.1 * j))
                
        # Novel chaotic cross-dimensional term with complex interaction, fractal scaling and dynamic phase
        f15 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(0.35 * (i + j) + 0.2 * r + 0.25 * np.cos(r) + 0.1 * np.sin(r))
                scale_factor = 1.4 + 0.4 * np.cos(0.25 * (i - j) + 0.1 * r + 0.15 * np.sin(r))
                interaction = np.tan(x[i] * x[j]) * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                f15 += scale_factor * phase_shift * interaction * (1.0 + 0.2 * np.sin(0.1 * i + 0.1 * j))
                
        # Novel radial polynomial with higher-order terms, chaotic scaling and fractal modulation
        f16 = 0.0
        for i in range(self.dim):
            coeff = 2.3 + 1.8 * np.sin(0.3 * i + 0.2 * r + 0.25 * np.cos(r) + 0.1 * np.sin(i))
            radial_term = x[i]**5 * np.exp(-0.03 * r**2)
            f16 += coeff * radial_term * (1.0 + 0.3 * np.cos(0.1 * i + 0.1 * r))
            
        # Fractal dimensionality scaling term with chaotic modulation and enhanced complexity
        fractal_scale = 0.6 + 0.4 * np.sin(0.25 * r + 0.15 * np.cos(r) + 0.1 * np.sin(r))
        f17 = 0.0
        for i in range(self.dim):
            f17 += x[i]**6 * fractal_scale * np.exp(-0.04 * x[i]**2) * (1.0 + 0.25 * np.sin(0.1 * i + 0.1 * r))
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17