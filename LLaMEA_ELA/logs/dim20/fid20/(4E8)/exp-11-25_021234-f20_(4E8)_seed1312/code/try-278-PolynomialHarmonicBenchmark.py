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
            
        # Radial harmonic interactions with enhanced frequency modulation
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.5 + 2.5 * np.sin(0.15 * i + 0.08 * r)
            f2 += np.sin(freq * x[i]) * np.exp(-0.15 * r**2)
            
        # Cross-dimensional coupling with enhanced time-varying weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.7 + 0.7 * np.sin(0.15 * (i + j) + 0.25 * r)
                f3 += weight * x[i] * x[j] * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Enhanced boundary attraction terms with modified decay
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                f4 += dist**3 * np.exp(-0.3 * dist)
                
        # Multi-scale polynomial interactions with enhanced coefficients
        f5 = 0.0
        for i in range(self.dim):
            coeff = 1.2 + 0.9 * np.sin(0.4 * i + 0.15 * r)
            f5 += coeff * x[i]**4 * np.exp(-0.05 * x[i]**2)
            
        # Fractal-like harmonic coupling with more complex structure
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.2 + 0.8 * np.sin(0.25 * (i - j))
                f6 += scale * np.cos(x[i] + x[j]) * np.exp(-0.07 * (x[i]**2 + x[j]**2))
                
        # Adaptive quartic terms with enhanced radial conditioning
        f7 = 0.0
        for i in range(self.dim):
            coeff = 1.8 + 0.7 * np.cos(0.2 * i + 0.15 * r)
            f7 += coeff * x[i]**4 * np.exp(-0.03 * r**2)
            
        # Mixed trigonometric and polynomial cross-terms with enhanced interaction
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f8 += np.sin(x[i] * x[j]) * x[i]**2 * x[j]**2 * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Enhanced boundary repulsion with modified penalties
        f9 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty = 2.5 * (5.0 - np.abs(x[i]))**4
                f9 += penalty * np.exp(-0.15 * x[i]**2)
                
        # Dynamic harmonic modulation with improved amplitudes
        f10 = 0.0
        for i in range(self.dim):
            amp = 2.5 + 1.5 * np.sin(0.25 * i + 0.35 * r)
            freq = 1.2 + 2.0 * np.cos(0.12 * i + 0.25 * np.random.uniform(-1, 1))
            f10 += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Combined polynomial and harmonic terms with refined weights
        f11 = 0.0
        for i in range(self.dim):
            weight = 1.2 + 0.7 * np.sin(0.3 * i + 0.15 * r)
            f11 += weight * x[i]**3 * np.cos(x[i]) * np.exp(-0.06 * x[i]**2)
            
        # Cross-dimensional quartic interactions with refined coupling
        f12 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_weight = 0.9 + 0.5 * np.sin(0.35 * (i - j) + 0.25 * r)
                f12 += dynamic_weight * x[i]**3 * x[j]**3 * np.exp(-0.07 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic modulation with enhanced complexity
        f13 = 0.0
        for i in range(self.dim):
            chaos_factor = 0.4 * np.sin(0.6 * i + 0.15 * r + np.pi/3)
            f13 += x[i]**2 * np.exp(-0.02 * x[i]**2) * chaos_factor
            
        # Hybrid coupling with enhanced sine and cosine components
        f14 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hybrid_term = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                f14 += hybrid_term * x[i]**2 * x[j]**2 * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Novel chaotic cross-dimensional term with improved interaction
        f15 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(0.3 * (i + j) + 0.15 * r)
                scale_factor = 1.2 + 0.4 * np.cos(0.2 * (i - j) + 0.08 * r)
                interaction = np.tan(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                f15 += scale_factor * phase_shift * interaction
                
        # Novel radial polynomial with enhanced higher-order terms
        f16 = 0.0
        for i in range(self.dim):
            coeff = 2.5 + 2.0 * np.sin(0.25 * i + 0.15 * r)
            radial_term = x[i]**4 * np.exp(-0.02 * r**2)
            f16 += coeff * radial_term
            
        # Add a new fractal-like term for enhanced multimodality
        f17 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_term = np.sin(3 * x[i] + 2 * x[j]) * np.cos(2 * x[i] - x[j])
                f17 += fractal_term * x[i]**3 * x[j]**3 * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17